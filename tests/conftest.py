"""
Shared fixtures for the Deploy Streamlit test suite.
"""

from pathlib import Path
import pytest
import tomllib


@pytest.fixture(scope="session")
def project_root():
    """Get the zoologist front project root path."""
    # Navigate up from the test file to find the zoologist project
    code_folder = next(
        parent for parent in Path(__file__).resolve().parents if "code" in parent.parent.name.lower()
    )
    return code_folder / "zoologist-front"


@pytest.fixture(scope="session")
def app_path(project_root):
    """Get the path to the Streamlit app entry point."""
    return project_root / "app.py"


@pytest.fixture
def pyproject_content(project_root):
    """Load and return pyproject.toml as a dictionary."""
    pyproject_path = project_root / "pyproject.toml"
    with open(pyproject_path, 'rb') as f:
        return tomllib.load(f)
