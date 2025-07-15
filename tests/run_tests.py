import pytest
import sys

if __name__ == "__main__":
    # Example: Run all smoke tests with HTML report and rerun failed tests up to 2 times
    exit_code = pytest.main([
        "--bdd-features-base-dir=features",
        "--html=report.html",
        "--self-contained-html",
        "--reruns=2",
        "--maxfail=3",
        "-m", "smoke",
        "step_definitions/"
    ])
    sys.exit(exit_code)
