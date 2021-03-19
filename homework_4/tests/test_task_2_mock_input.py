from unittest.mock import Mock, patch

import pytest
from task02.task_2_mock_input import count_dots_on_i


# эксперимент
@patch(
    "urllib.request.urlopen",
    return_value=Mock(read=Mock(return_value=b"illustrative example")),
)
def test_count_dots_on_i(mock_urlopen):
    result = count_dots_on_i(mock_urlopen)
    assert result == 2


@patch(
    "urllib.request.urlopen",
    return_value=Mock(
        read=Mock(return_value=b"https://example.com/", side_effect=ValueError)
    ),
)
def test_count_dots_on_i_error(mock_urlopen):
    with pytest.raises(ValueError):
        count_dots_on_i(mock_urlopen)
