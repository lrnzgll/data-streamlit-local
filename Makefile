default:
	cat tests/test_output.txt

test:
	@PYTHONDONTWRITEBYTECODE=1 pytest tests -c "./tests/pytest_kitt.ini" 2>&1 > tests/test_output.txt || true
	PYTHONDONTWRITEBYTECODE=1 pytest -v --color=yes
