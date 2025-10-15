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

def test_push_cplx2():
    result = subprocess.run(
        ["python3", "cdc.py", "push", "3", "+", "j", "4", "pop"],
        capture_output=True,
        text=True
    )
    assert result.stdout.strip("\n") == "3 + j4"