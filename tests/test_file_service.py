from src.file_service import upload_file
from src.fileio_adaptor import FileIOAdapter, FileIOAdapterSession


class FakeFileIOAdapter:
    def __init__(self):
        self.files = {}

    def upload_file(self, file_path):
        self.files[file_path] = f"https://file.io/fake/{file_path}"
        return {
            "success": True,
            "status": 200,
            "name": file_path,
        }


def test_upload_file_with_real_api():
    file_name = "sample.txt"
    real_adapter = FileIOAdapter()
    result = upload_file(file_name, real_adapter)

    assert result["success"] is True
    assert result["status"] == 200
    assert result["name"] == file_name


def test_upload_file_with_fake():
    file_name = "sample.txt"
    fake_adapter = FileIOAdapter()
    result = upload_file(file_name, fake_adapter)

    assert result["success"] is True
    assert result["status"] == 200
    assert result["name"] == file_name
