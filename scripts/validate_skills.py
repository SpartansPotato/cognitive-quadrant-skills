from pathlib import Path
import sys, zipfile, re
import xml.etree.ElementTree as ET
try:
    import yaml
except ImportError:
    print("PyYAML is required: pip install pyyaml", file=sys.stderr)
    raise

ROOT = Path(__file__).resolve().parents[1]
SKILLS = [
    ROOT / "skills" / "cognitive-quadrant-general",
    ROOT / "skills" / "cognitive-quadrant-teacher-research",
]
errors = []

CJK_RE = re.compile(r"[\u4e00-\u9fff]")
W_NS = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

def docx_visible_text_contains_cjk(path: Path) -> bool:
    with zipfile.ZipFile(path) as z:
        root = ET.fromstring(z.read("word/document.xml"))
    visible_text = "".join(node.text or "" for node in root.iter(W_NS + "t"))
    return bool(CJK_RE.search(visible_text))


for skill in SKILLS:
    required = [
        skill / "SKILL.md",
        skill / "manifest.yaml",
        skill / "agents" / "openai.yaml",
        skill / "references" / "workflow.md",
        skill / "references" / "workflow.zh-CN.md",
        skill / "references" / "evidence-and-search.md",
        skill / "references" / "evidence-and-search.zh-CN.md",
        skill / "references" / "deliverables.md",
        skill / "references" / "deliverables.zh-CN.md",
        skill / "references" / "safety.md",
        skill / "references" / "safety.zh-CN.md",
        skill / "assets" / "icon.png",
    ]
    for p in required:
        if not p.exists():
            errors.append(f"Missing: {p.relative_to(ROOT)}")


    if skill.name == "cognitive-quadrant-general":
        bilingual_docs = [
            skill / "assets/templates/en/00_Template_Pack_Guide.docx",
            skill / "assets/templates/en/01_Cognitive_Quadrant_Reflection_Template.docx",
            skill / "assets/templates/en/02_Deep_Cognition_and_Action_Plan_Template.docx",
            skill / "assets/templates/en/03_Completed_Example_Learning_AI_Systematically.docx",
            skill / "assets/templates/zh-CN/00_通用版模板包使用说明.docx",
            skill / "assets/templates/zh-CN/01_通用四象限认知梳理模板.docx",
            skill / "assets/templates/zh-CN/02_深度认知与行动方案模板.docx",
            skill / "assets/templates/zh-CN/03_填写示例_系统学习人工智能.docx",
        ]
    else:
        bilingual_docs = [
            skill / "assets/templates/en/00_Template_Pack_Guide.docx",
            skill / "assets/templates/en/01_Teacher_Cognitive_Quadrant_Reflection_Template.docx",
            skill / "assets/templates/en/02_Teacher_Research_Cognition_and_Innovation_Analysis_Template.docx",
            skill / "assets/templates/en/03_Completed_Example_Generative_AI_in_Vocational_Hospitality_Education.docx",
            skill / "assets/templates/zh-CN/00_模板包使用说明.docx",
            skill / "assets/templates/zh-CN/01_普通教师四象限认知梳理模板.docx",
            skill / "assets/templates/zh-CN/02_教师科研认知拓展与创新分析模板.docx",
            skill / "assets/templates/zh-CN/03_填写示例_生成式AI与高职酒店教学.docx",
        ]
    for p in bilingual_docs:
        if not p.exists():
            errors.append(f"Missing bilingual Word template: {p.relative_to(ROOT)}")
        elif "/en/" in p.as_posix() and docx_visible_text_contains_cjk(p):
            errors.append(f"CJK visible text found in English Word template: {p.relative_to(ROOT)}")

    text = (skill / "SKILL.md").read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append(f"Invalid frontmatter start: {skill.name}")
        continue
    try:
        fm_text = text.split("---", 2)[1]
        fm = yaml.safe_load(fm_text)
    except Exception as exc:
        errors.append(f"Frontmatter parse error in {skill.name}: {exc}")
        continue
    if fm.get("name") != skill.name:
        errors.append(f"Frontmatter name mismatch in {skill.name}")
    desc = fm.get("description", "")
    if len(desc) < 120 or not desc.lstrip().startswith("Use this"):
        errors.append(f"Description should be English-first and specific in {skill.name}")
    if "WorkBuddy 中" in text or "mainly installed in WorkBuddy" in text:
        errors.append(f"Host lock-in found in {skill.name}")

    manifest = yaml.safe_load((skill / "manifest.yaml").read_text(encoding="utf-8"))
    if manifest.get("name") != skill.name:
        errors.append(f"Manifest name mismatch in {skill.name}")
    if str(manifest.get("version")) != "1.1.0":
        errors.append(f"Manifest version mismatch in {skill.name}")

    openai = yaml.safe_load((skill / "agents/openai.yaml").read_text(encoding="utf-8"))
    icon = openai.get("interface", {}).get("icon_large")
    if icon and not (skill / icon).resolve().exists():
        errors.append(f"Missing OpenAI icon target in {skill.name}: {icon}")

# Validate release archives if present
release_map = {
    "cognitive-quadrant-general-v1.1.0.zip": "cognitive-quadrant-general",
    "cognitive-quadrant-teacher-research-v1.1.0.zip": "cognitive-quadrant-teacher-research",
}
for zip_name, root_name in release_map.items():
    p = ROOT / "releases" / zip_name
    if not p.exists():
        errors.append(f"Missing release archive: {zip_name}")
        continue
    with zipfile.ZipFile(p) as z:
        names = z.namelist()
        if f"{root_name}/SKILL.md" not in names:
            errors.append(f"Archive root invalid: {zip_name}")
        if f"{root_name}/manifest.yaml" not in names:
            errors.append(f"Archive missing manifest: {zip_name}")
        if not any(name.startswith(f"{root_name}/assets/templates/en/") and name.endswith(".docx") for name in names):
            errors.append(f"Archive missing English Word templates: {zip_name}")
        if not any(name.startswith(f"{root_name}/assets/templates/zh-CN/") and name.endswith(".docx") for name in names):
            errors.append(f"Archive missing Chinese Word templates: {zip_name}")

if errors:
    print("Validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)
print("Validation passed for all Skills and release archives.")
