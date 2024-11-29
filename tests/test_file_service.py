from src.file_service import upload_file
from src.fileio_adaptor import FileIOAdapter, FileIOAdapterSession


class FakeFileIOAdapter:
    def upload_file(self, file_path):
        return {"success": True, "id": "fake-id", "name": file_path}


def test_upload_file_with_real_api():
    file_name = "sample.txt"
    real_adapter = FileIOAdapter()
    result = upload_file(file_name, real_adapter)

    assert result["success"] is True
    assert result["status"] == 200
    assert result["name"] == file_name


def test_upload_file_with_fake():
    fake_adapter = FakeFileIOAdapter()
    result = upload_file("test.txt", fake_adapter)

    assert result["success"] is True
    assert result["id"] == "fake-id"
