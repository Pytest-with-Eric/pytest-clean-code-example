from unittest.mock import patch, Mock, ANY
from src.file_uploader import upload_file


@patch("src.file_uploader_refactor.requests.post")
def test_upload_file(mock_post):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"success": True, "id": "TEST"}
    mock_post.return_value = mock_response

    result = upload_file("sample.txt")
    assert result["id"] == "TEST"
    mock_post.assert_called_once_with("https://file.io", files={"file": ANY})
