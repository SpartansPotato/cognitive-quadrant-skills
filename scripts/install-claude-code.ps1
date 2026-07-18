$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$Dest = Join-Path $HOME ".claude\skills"
New-Item -ItemType Directory -Force -Path $Dest | Out-Null
foreach ($Skill in @("cognitive-quadrant-general", "cognitive-quadrant-teacher-research")) {
    $Target = Join-Path $Dest $Skill
    if (Test-Path $Target) { Remove-Item -Recurse -Force $Target }
    Copy-Item -Recurse -Force (Join-Path $Root "skills\$Skill") $Target
    Write-Host "Installed $Skill -> $Target"
}
Write-Host "Claude Code installation complete. Invoke /cognitive-quadrant-general or /cognitive-quadrant-teacher-research."
