import requests


class FileIOAdapter:
    def __init__(self, base_url="https://file.io"):
        self.base_url = base_url

    def upload_file(self, file_path):
        with open(file_path, "rb") as file:
            response = requests.post(self.base_url, files={"file": file})
            response.raise_for_status()
            return response.json()


class FileIOAdapterSession:
    def __init__(self, base_url="https://file.io"):
        self.base_url = base_url
        self.session = requests.Session()

    def upload_file(self, file_path):
        with open(file_path, "rb") as file:
            response = self.session.post(self.base_url, files={"file": file})
            response.raise_for_status()
            return response.json()
