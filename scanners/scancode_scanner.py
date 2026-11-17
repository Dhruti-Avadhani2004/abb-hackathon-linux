
# import subprocess
# from pathlib import Path
# from datetime import datetime

# # Project directories
# BASE_DIR = Path(__file__).resolve().parent.parent

# SCANCODE_DIR = (
#     BASE_DIR
#     / "tools"
#     / "scancode"
#     / "scancode-toolkit-v32.5.0"
# )

# SCANCODE_CMD = SCANCODE_DIR / "scancode.bat"

# from scan_config import TARGET_DIR
# OUTPUT_DIR = BASE_DIR / "scanner_output"

# JSON_REPORT = OUTPUT_DIR / "scancode_output.json"
# LOG_FILE = OUTPUT_DIR / "scancode_output.txt"


# def main():

#     OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

#     if not SCANCODE_CMD.exists():
#         raise FileNotFoundError(
#             f"ScanCode executable not found: {SCANCODE_CMD}"
#         )

#     if not TARGET_DIR.exists():
#         raise FileNotFoundError(
#             f"Target directory not found: {TARGET_DIR}"
#         )

#     # Remove previous report to avoid treating stale output as current
#     if JSON_REPORT.exists():
#         JSON_REPORT.unlink()

#     command = [
#         "cmd",
#         "/c",
#         str(SCANCODE_CMD),
#         "--license",
#         "--copyright",
#         "--package",
#         "--info",
#         "--classify",
#         "--summary",
#         "--ignore",
#         "node_modules",
#         "--json-pp",
#         str(JSON_REPORT),
#         str(TARGET_DIR)
#     ]

#     start_time = datetime.now()

#     print("Starting ScanCode Toolkit scan...")
#     print(f"Target: {TARGET_DIR}")
#     print("Excluding: node_modules")

#     try:
#         result = subprocess.run(
#             command,
#             cwd=str(SCANCODE_DIR),
#             capture_output=True,
#             text=True,
#             encoding="utf-8",
#             errors="replace",
#             timeout=300
#         )

#         end_time = datetime.now()
#         duration = (end_time - start_time).total_seconds()

#         with open(LOG_FILE, "w", encoding="utf-8") as log:
#             log.write(result.stdout)
#             log.write("\n")
#             log.write(result.stderr)

#         if result.returncode != 0:
#             print("ScanCode scan failed.")
#             print(f"Check log: {LOG_FILE}")
#             print(result.stderr)
#             return

#         if not JSON_REPORT.exists():
#             print("ScanCode did not generate the expected JSON report.")
#             return

#         print("\n===== ScanCode Scan Summary =====")
#         print("Status: SUCCESS")
#         print(f"Duration: {duration:.2f} seconds")
#         print(f"JSON Report: {JSON_REPORT}")
#         print(f"Log: {LOG_FILE}")
#         print("=================================")

#     except subprocess.TimeoutExpired:
#         print("ScanCode scan timed out after 300 seconds.")
#         print("Check the target directory and exclusion pattern.")

#     except Exception as error:
#         print(f"ScanCode execution error: {error}")


# if __name__ == "__main__":
#     main()



import subprocess
from pathlib import Path
from datetime import datetime

from scan_config import TARGET_DIR, OUTPUT_DIR

BASE_DIR = Path(__file__).resolve().parent.parent

SCANCODE_DIR = (
    BASE_DIR
    / "tools"
    / "scancode"
    / "linux"
    / "scancode-toolkit-v32.5.0"
)

SCANCODE_CMD = SCANCODE_DIR / "scancode"

JSON_REPORT = OUTPUT_DIR / "scancode_output.json"
LOG_FILE = OUTPUT_DIR / "scancode_output.txt"


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    if not SCANCODE_CMD.is_file():
        raise FileNotFoundError(
            f"ScanCode executable not found: {SCANCODE_CMD}"
        )

    if not TARGET_DIR.is_dir():
        raise FileNotFoundError(
            f"Target directory not found: {TARGET_DIR}"
        )

    if JSON_REPORT.exists():
        JSON_REPORT.unlink()

    command = [
        str(SCANCODE_CMD),
        "--license",
        "--copyright",
        "--package",
        "--info",
        "--classify",
        "--summary",
        "--processes",
        "1",
        "--ignore",
        "node_modules",
        "--json-pp",
        str(JSON_REPORT),
        str(TARGET_DIR)
    ]

    print("Starting ScanCode Toolkit scan...")
    print(f"Target: {TARGET_DIR}")
    print("Excluding: node_modules")

    start_time = datetime.now()

    try:
        result = subprocess.run(
            command,
            cwd=str(SCANCODE_DIR),
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=900
        )

    except subprocess.TimeoutExpired as error:
        raise RuntimeError(
            "ScanCode scan timed out after 300 seconds"
        ) from error

    duration = (datetime.now() - start_time).total_seconds()

    LOG_FILE.write_text(
        result.stdout + "\n" + result.stderr,
        encoding="utf-8"
    )

    if result.returncode != 0:
        raise RuntimeError(
            f"ScanCode failed with exit code {result.returncode}. "
            f"Check {LOG_FILE}"
        )

    if not JSON_REPORT.is_file() or JSON_REPORT.stat().st_size == 0:
        raise RuntimeError(
            "ScanCode did not generate a valid-sized JSON report"
        )

    print("\n===== ScanCode Scan Summary =====")
    print("Status: SUCCESS")
    print(f"Duration: {duration:.2f} seconds")
    print(f"JSON Report: {JSON_REPORT}")
    print(f"Log: {LOG_FILE}")
    print("=================================")


if __name__ == "__main__":
    main()
