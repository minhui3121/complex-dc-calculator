import subprocess


def test_push_real1():
    result = subprocess.run(
        ["python3", "cdc.py", "push", "5", "pop"],
        capture_output = True,
        text = True
    )
    assert result.stdout.strip("\n") == "5 + j0"