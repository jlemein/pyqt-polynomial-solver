import subprocess

def test():
    """
    Run all unittests. Equivalent to:
    `poetry run python -u -m unittest discover
    """
    subprocess.run(
        ['poetry', 'run', 'python', '-u', '-m', 'unittest', 'discover']
    )

def coverage():
    """
    Run all unittests and generate coverage file result. Equivalent to:
    `poetry run python -u -m unittest discover
    """
    subprocess.run(['poetry', 'run', 'python', '-u', '-m', 'coverage', 'run', '-m', 'unittest', 'discover'])
    subprocess.run(['poetry', 'run', 'python', '-m', 'coverage', 'report', '-m'])