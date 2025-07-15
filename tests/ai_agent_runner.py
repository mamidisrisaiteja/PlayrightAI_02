import pytest
import sys
import re

def select_marker_from_nl(nl_input: str) -> str:
    """Map natural language input to pytest marker/tag."""
    nl_input = nl_input.lower()
    if 'login' in nl_input or 'auth' in nl_input:
        return 'auth'
    if 'inventory' in nl_input:
        return 'inventory'
    if 'smoke' in nl_input:
        return 'smoke'
    return ''

if __name__ == "__main__":
    nl = sys.argv[1] if len(sys.argv) > 1 else ''
    marker = select_marker_from_nl(nl)
    pytest_args = [
        "--html=report.html",
        "--self-contained-html",
        "--reruns=2",
        "--maxfail=3",
        "step_definitions/"
    ]
    if marker:
        pytest_args.extend(["-m", marker])
    sys.exit(pytest.main(pytest_args))
