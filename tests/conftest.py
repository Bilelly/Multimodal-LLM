"""
Pytest configuration file with shared fixtures and configurations.

This file contains shared fixtures, hooks, and configurations for all tests.
"""

import pytest
import os
from unittest.mock import patch


@pytest.fixture(scope="session")
def mock_hf_token():
    """Provide a mock Hugging Face token for testing."""
    return "hf_test_token_1234567890"


@pytest.fixture(autouse=True)
def set_test_env(mock_hf_token):
    """Automatically set test environment variables for all tests."""
    os.environ["HF_TOKEN"] = mock_hf_token
    yield
    # Cleanup
    if "HF_TOKEN" in os.environ:
        del os.environ["HF_TOKEN"]


@pytest.fixture
def mock_llm_client():
    """Provide a mock LLM client."""
    from unittest.mock import MagicMock
    return MagicMock()


@pytest.fixture
def mock_pdf_search():
    """Provide a mock PDF search."""
    from unittest.mock import MagicMock
    mock = MagicMock()
    mock.search_query.return_value = ("context", [0, 1], [0.1, 0.2])
    return mock
