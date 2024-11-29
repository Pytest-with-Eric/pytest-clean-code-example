from unittest.mock import patch, Mock, ANY
from src.file_uploader import upload_file


@patch("src.file_uploader.requests.post")
def test_upload_file(mock_post):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "success": True,
        "status": 200,
        "id": "TEST",
        "key": "TEST",
        "name": "TEST.txt",
    }
    mock_post.return_value = mock_response

    result = upload_file("sample.txt")
    print(result)

    assert result["id"] == "TEST"
    assert result["name"] == "TEST.txt"
    mock_post.assert_called_once_with("https://file.io", files={"file": ANY})
