"""
Tests to check progress of the Streamlit challenge
"""

import re

import pytest
import requests


STREAMLIT_URL = "http://localhost:8501"


class TestStreamlitApp:
    """Basic checks that the Streamlit app is working (end of chapter 2)."""

    def test_streamlit_is_running(self):
        """The Streamlit app should start and respond on localhost:8501."""
        try:
            response = requests.get(STREAMLIT_URL, timeout=5)
        except requests.exceptions.ConnectionError:
            pytest.fail(
                f"Streamlit app is not reachable at {STREAMLIT_URL}. "
                "Make sure it can be started with: streamlit run app.py"
            )
        assert response.status_code == 200, \
            f"Streamlit app should respond with 200, got {response.status_code}"

    def test_app_calls_api_with_requests(self, app_path):
        """app.py should use the requests package to call the prediction API."""
        source = app_path.read_text()
        assert "import requests" in source, \
            "app.py should import the requests package to call the prediction API"
        assert re.search(r"requests\.(get|post)\(", source), \
            "app.py should call requests.get(...) or requests.post(...) to get a prediction"

    def test_scikit_learn_not_in_dependencies(self, pyproject_content):
        """scikit-learn should not be a dependency of the Streamlit front-end."""
        dependencies = pyproject_content.get("project", {}).get("dependencies", [])
        assert not any("scikit-learn" in dep.lower() for dep in dependencies), \
            "scikit-learn should not be needed by the Streamlit app: predictions come from the API"

