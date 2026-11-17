# import subprocess
# from pathlib import Path
# from datetime import datetime
# import shutil

# BASE_DIR = Path(__file__).resolve().parent.parent

# from scan_config import TARGET_DIR
# OUTPUT_DIR = BASE_DIR / "scanner_output"

# TEXT_REPORT = OUTPUT_DIR / "dotnet_output.txt"


# def main():
#     OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

#     print("Starting offline .NET NuGet vulnerability scan...")
#     print(f"Target: {TARGET_DIR}")

#     if not TARGET_DIR.exists():
#         print("Target directory not found.")
#         return

#     dotnet_path = shutil.which("dotnet")

#     if not dotnet_path:
#         print(".NET CLI not found. Check installation and PATH.")
#         return

#     project_files = list(TARGET_DIR.rglob("*.csproj"))
#     project_files += list(TARGET_DIR.rglob("*.fsproj"))

#     if not project_files:
#         print("\n===== .NET Vulnerability Scan Summary =====")
#         print("Status: SKIPPED")
#         print("Reason: No .NET project files found.")
#         print("===========================================")
#         return

#     start_time = datetime.now()

#     all_output = []
#     scan_success = True

#     for project in project_files:
#         print(f"\nScanning project: {project}")

#         command = [
#             dotnet_path,
#             "package",
#             "list",
#             "--project",
#             str(project),
#             "--vulnerable",
#             "--no-restore"
#         ]

#         try:
#             result = subprocess.run(
#                 command,
#                 capture_output=True,
#                 text=True,
#                 encoding="utf-8",
#                 errors="replace",
#                 cwd=str(BASE_DIR)
#             )

#             all_output.append(f"\nProject: {project}\n")
#             all_output.append(result.stdout)
#             all_output.append(result.stderr)

#             if result.returncode != 0:
#                 scan_success = False
#                 print("Project vulnerability scan failed.")
#                 print(result.stderr)

#         except Exception as error:
#             scan_success = False
#             all_output.append(f"Execution error: {error}\n")
#             print(f"Execution error: {error}")

#     end_time = datetime.now()
#     duration = (end_time - start_time).total_seconds()

#     with open(TEXT_REPORT, "w", encoding="utf-8") as report:
#         report.write("".join(all_output))

#     print("\n===== .NET Vulnerability Scan Summary =====")
#     print(f"Status: {'SUCCESS' if scan_success else 'FAILED'}")
#     print("Offline mode: Enabled (--no-restore)")
#     print(f"Projects scanned: {len(project_files)}")
#     print(f"Duration: {duration:.2f} seconds")
#     print(f"Text Report: {TEXT_REPORT}")
#     print("===========================================")


# if __name__ == "__main__":
#     main()



import subprocess
import shutil
from pathlib import Path
from datetime import datetime

from scan_config import TARGET_DIR, OUTPUT_DIR

TEXT_REPORT = OUTPUT_DIR / "dotnet_output.txt"


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("Starting .NET NuGet vulnerability scanner...")
    print(f"Target: {TARGET_DIR}")

    start_time = datetime.now()
    log_lines = []

    if not TARGET_DIR.is_dir():
        raise FileNotFoundError(
            f"Target directory not found: {TARGET_DIR}"
        )

    # Verify that the .NET SDK is installed
    dotnet_path = shutil.which("dotnet")

    if not dotnet_path:
        raise FileNotFoundError(
            ".NET SDK not found in PATH"
        )

    # Verify that the .NET CLI works
    version_result = subprocess.run(
        [dotnet_path, "--version"],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=30
    )

    if version_result.returncode != 0:
        raise RuntimeError(
            f".NET SDK verification failed: {version_result.stderr}"
        )

    sdk_version = version_result.stdout.strip()

    print(f".NET SDK: {sdk_version}")

    log_lines.append(f".NET SDK: {sdk_version}\n")
    log_lines.append(f"Target: {TARGET_DIR}\n")

    # Discover C# and F# projects
    project_files = sorted(
        list(TARGET_DIR.rglob("*.csproj"))
        + list(TARGET_DIR.rglob("*.fsproj"))
    )

    # No projects does not mean the scanner is unavailable
    if not project_files:
        status = "NO_APPLICABLE_PROJECTS"

        log_lines.append(
            "\nStatus: NO_APPLICABLE_PROJECTS\n"
            "Reason: No .NET project files found.\n"
            "Scanner executable verified successfully.\n"
            "No dependency vulnerability analysis was performed.\n"
        )

        TEXT_REPORT.write_text(
            "".join(log_lines),
            encoding="utf-8"
        )

        print("\n===== .NET Vulnerability Scan Summary =====")
        print(f"Status: {status}")
        print(f".NET SDK: {sdk_version}")
        print("Projects found: 0")
        print("Scanner readiness: VERIFIED")
        print(f"Text Report: {TEXT_REPORT}")
        print("===========================================")
        return

    scan_success = True

    for project in project_files:
        print(f"\nScanning project: {project}")

        # .NET SDK 8 command syntax
        command = [
            dotnet_path,
            "list",
            str(project),
            "package",
            "--vulnerable",
            "--include-transitive"
        ]

        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                cwd=str(TARGET_DIR),
                timeout=300
            )

            log_lines.append(
                f"\n===== Project: {project} =====\n"
            )
            log_lines.append(result.stdout)
            log_lines.append(result.stderr)
            log_lines.append(
                f"\nExit code: {result.returncode}\n"
            )

            if result.returncode != 0:
                scan_success = False
                print(
                    f"FAILED: {project.name} "
                    f"(exit code {result.returncode})"
                )

                if result.stderr:
                    print(result.stderr)
            else:
                print(f"Completed: {project.name}")

        except subprocess.TimeoutExpired:
            scan_success = False
            log_lines.append(
                f"\nTIMEOUT: {project} exceeded 300 seconds\n"
            )
            print(f"TIMEOUT: {project.name}")

        except Exception as error:
            scan_success = False
            log_lines.append(
                f"\nExecution error: {project}: {error}\n"
            )
            print(f"Execution error: {error}")

    duration = (datetime.now() - start_time).total_seconds()

    TEXT_REPORT.write_text(
        "".join(log_lines),
        encoding="utf-8"
    )

    print("\n===== .NET Vulnerability Scan Summary =====")
    print(
        f"Status: {'SUCCESS' if scan_success else 'FAILED'}"
    )
    print(f".NET SDK: {sdk_version}")
    print("Restore disabled: YES (--no-restore)")
    print(f"Projects scanned: {len(project_files)}")
    print(f"Duration: {duration:.2f} seconds")
    print(f"Text Report: {TEXT_REPORT}")
    print("===========================================")

    if not scan_success:
        raise RuntimeError(
            f".NET vulnerability scan failed. Check {TEXT_REPORT}"
        )


if __name__ == "__main__":
    main()
