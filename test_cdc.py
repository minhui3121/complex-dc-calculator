import subprocess


def test_push_real1():
    result = subprocess.run(
        ["python3", "cdc.py", "push", "5", "pop"],
        capture_output = True,
        text = True
    )
    assert result.stdout.strip("\n") == "5 + j0"

def test_push_cplx1():
    result = subprocess.run(
        ["python3", "cdc.py", "push", "-2.5-j0.25", "pop"],
        capture_output=True,
        text=True
    )
    assert result.stdout.strip("\n") == "-2.5 - j0.25"