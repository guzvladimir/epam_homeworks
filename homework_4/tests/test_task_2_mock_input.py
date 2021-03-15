from unittest.mock import Mock, patch

import pytest
from task02.task_2_mock_input import count_dots_on_i


@patch("urllib.request.urlopen")
def test_count_dots_on_i(mock_urlopen):
    mock = Mock()
    mock.read.return_value = b"illustrative example"
    mock_urlopen.return_value = mock
    result = count_dots_on_i(mock)
    assert result == 2


@patch("urllib.request.urlopen")
def test_count_dots_on_i_error(mock_urlopen):
    mock = Mock()
    mock.read.return_value = b"https://example.com/"
    mock_urlopen.return_value = mock
    mock_urlopen.side_effect = ValueError
    with pytest.raises(ValueError):
        count_dots_on_i(mock)
