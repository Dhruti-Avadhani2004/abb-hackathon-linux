import json
import subprocess
from pathlib import Path
from datetime import datetime

from scan_config import TARGET_DIR, OUTPUT_DIR

BASE_DIR = Path(__file__).resolve().parent.parent

# Reuse the existing offline ESLint installation
ESLINT_HOME = BASE_DIR / "sgc-gatekeeper-testbed"

ESLINT_CMD = (
    ESLINT_HOME / "node_modules" / ".bin" / "eslint"
)

ESLINT_CONFIG = ESLINT_HOME / "eslint.config.mjs"

JSON_REPORT = OUTPUT_DIR / "eslint_output.json"
TEXT_REPORT = OUTPUT_DIR / "eslint_output.txt"


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("Starting ESLint security scan...")
    print(f"Target: {TARGET_DIR}")
    print(f"ESLint executable: {ESLINT_CMD}")
    print(f"ESLint configuration: {ESLINT_CONFIG}")

    if not TARGET_DIR.is_dir():
        raise FileNotFoundError(
            f"Target directory not found: {TARGET_DIR}"
        )

    if not ESLINT_CMD.is_file():
        raise FileNotFoundError(
            f"ESLint executable not found: {ESLINT_CMD}"
        )

    if not ESLINT_CONFIG.is_file():
        raise FileNotFoundError(
            f"ESLint configuration not found: {ESLINT_CONFIG}"
        )

    start_time = datetime.now()

    # Remove stale reports before scanning
    JSON_REPORT.unlink(missing_ok=True)
    TEXT_REPORT.unlink(missing_ok=True)

    # Run ESLint with the centralized security configuration
    command = [
        str(ESLINT_CMD),
        ".",
        "--config",
        str(ESLINT_CONFIG),
        "--format",
        "json",
        "--output-file",
        str(JSON_REPORT)
    ]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        cwd=str(TARGET_DIR),
        timeout=300
    )

    # 0 = no lint findings
    # 1 = lint findings detected
    # 2 = execution/configuration failure
    if result.returncode not in (0, 1):
        raise RuntimeError(
            "ESLint scan failed:\n"
            + result.stdout
            + result.stderr
        )

    if not JSON_REPORT.is_file():
        raise RuntimeError(
            "ESLint JSON report was not generated."
        )

    with JSON_REPORT.open("r", encoding="utf-8") as report:
        data = json.load(report)

    if not isinstance(data, list):
        raise RuntimeError("Unexpected ESLint JSON format.")

    total_errors = sum(
        item.get("errorCount", 0) for item in data
    )

    total_warnings = sum(
        item.get("warningCount", 0) for item in data
    )

    # Produce human-readable output from the same configuration
    text_command = [
        str(ESLINT_CMD),
        ".",
        "--config",
        str(ESLINT_CONFIG)
    ]

    text_result = subprocess.run(
        text_command,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        cwd=str(TARGET_DIR),
        timeout=300
    )

    if text_result.returncode not in (0, 1):
        raise RuntimeError(
            "ESLint text scan failed:\n"
            + text_result.stdout
            + text_result.stderr
        )

    TEXT_REPORT.write_text(
        text_result.stdout + text_result.stderr,
        encoding="utf-8"
    )

    duration = (
        datetime.now() - start_time
    ).total_seconds()

    print("\n===== ESLint Scan Summary =====")
    print("Status: SUCCESS")
    print(f"Files scanned: {len(data)}")
    print(f"Total errors: {total_errors}")
    print(f"Total warnings: {total_warnings}")
    print(f"Duration: {duration:.2f} seconds")
    print(f"JSON Report: {JSON_REPORT}")
    print(f"Text Report: {TEXT_REPORT}")
    print("================================")


if __name__ == "__main__":
    main()