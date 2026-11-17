
# import subprocess
# import os

# from scan_config import TARGET_DIR

# repo_path = str(TARGET_DIR)
# output_file = r"scanner_output\trivy_output_offline.json"
# cache_dir = r"trivy-cache"

# os.makedirs("scanner_output", exist_ok=True)

# trivy_exe = os.path.join(
#     os.environ["LOCALAPPDATA"],
#     "Microsoft",
#     "WinGet",
#     "Packages",
#     "AquaSecurity.Trivy_Microsoft.Winget.Source_8wekyb3d8bbwe",
#     "trivy.exe"
# )

# command = [
#     trivy_exe,
#     "--cache-dir", cache_dir,
#     "fs",
#     "--scanners", "vuln,misconfig,secret",
#     "--skip-db-update",
#     "--skip-java-db-update",
#     "--skip-check-update",
#     "--offline-scan",
#     "--skip-version-check",
#     "--disable-telemetry",
#     "--format", "json",
#     "--output", output_file,
#     repo_path
# ]

# result = subprocess.run(
#     command,
#     capture_output=True,
#     text=True
# )

# print(result.stdout)

# if result.stderr:
#     print(result.stderr)

# print(f"Trivy scan completed. Output saved to {output_file}")
# print(f"Exit code: {result.returncode}")



import json
import shutil
import subprocess
from pathlib import Path

from scan_config import TARGET_DIR, OUTPUT_DIR

TRIVY_CACHE = Path.home() / "trivy-cache"
JSON_REPORT = OUTPUT_DIR / "trivy_output_offline.json"


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    if not TARGET_DIR.is_dir():
        raise FileNotFoundError(
            f"Target directory not found: {TARGET_DIR}"
        )

    trivy_exe = shutil.which("trivy")

    if trivy_exe is None:
        raise FileNotFoundError(
            "Trivy executable not found in PATH"
        )

    db_file = TRIVY_CACHE / "db" / "trivy.db"

    if not db_file.is_file():
        raise FileNotFoundError(
            f"Offline Trivy database not found: {db_file}"
        )

    command = [
        trivy_exe,
        "--cache-dir", str(TRIVY_CACHE),
        "fs",
        "--scanners", "vuln,misconfig,secret",
        "--skip-db-update",
        "--skip-java-db-update",
        "--skip-check-update",
        "--offline-scan",
        "--skip-version-check",
        "--disable-telemetry",
        "--format", "json",
        "--output", str(JSON_REPORT),
        str(TARGET_DIR)
    ]

    if JSON_REPORT.exists():
        JSON_REPORT.unlink()

    print("Starting offline Trivy scan...")
    print(f"Target: {TARGET_DIR}")
    print(f"Cache: {TRIVY_CACHE}")

    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.stdout:
        print(result.stdout)

    if result.stderr:
        print(result.stderr)

    if result.returncode != 0:
        raise RuntimeError(
            f"Trivy failed with exit code {result.returncode}"
        )

    if not JSON_REPORT.is_file():
        raise RuntimeError(
            "Trivy JSON report was not generated"
        )

    with JSON_REPORT.open("r", encoding="utf-8") as file:
        data = json.load(file)

    print("\n===== Trivy Scan Summary =====")

    for field in (
        "Vulnerabilities",
        "Misconfigurations",
        "Secrets"
    ):
        count = sum(
            len(section.get(field) or [])
            for section in data.get("Results", [])
        )

        print(f"{field}: {count}")

    print(f"JSON Report: {JSON_REPORT}")
    print("Status: SUCCESS")
    print("==============================")

if __name__ == "__main__":
    main()
