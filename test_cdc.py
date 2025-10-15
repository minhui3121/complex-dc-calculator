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

def test_pop_err1():
    result = subprocess.run(
        ["python3", "cdc.py", "pop"],
        capture_output=True,
        text=True
    )
    assert result.stdout.strip("\n") == "Error: stack underflow"

def test_add_real1():
    result = subprocess.run(
        ["python3", "cdc.py", "push", "2", "push", "5", "add", "pop"],
        capture_output=True,
        text=True
    )
    assert result.stdout.strip("\n") == "7 + j0"

def test_add_cplx1():
    result = subprocess.run(
        ["python3", "cdc.py", "push", "3+j4", "push", "1-j2", "add", "pop"],
        capture_output=True,
        text=True
    )
    assert result.stdout.strip("\n") == "4 + j2"

def test_add_err1():
    result = subprocess.run(
        ["python3", "cdc.py", "push", "3", "add"],
        capture_output=True,
        text=True
    )
    assert result.stdout.strip("\n") == "Error: stack underflow"

def test_sub_real1():
    result = subprocess.run(
        ["python3", "cdc.py", "push", "5", "push", "2", "sub", "pop"],
        capture_output=True,
        text=True
    )
    assert result.stdout.strip("\n") == "3 + j0"

def test_sub_cplx1():
    result = subprocess.run(
        ["python3", "cdc.py", "push", "3+j4", "push", "1-j2", "sub", "pop"],
        capture_output=True,
        text=True
    )
    assert result.stdout.strip("\n") == "2 + j6"

def test_sub_err1():
    result = subprocess.run(
        ["python3", "cdc.py", "sub"],
        capture_output=True,
        text=True
    )
    assert result.stdout.strip("\n") == "Error: stack underflow"