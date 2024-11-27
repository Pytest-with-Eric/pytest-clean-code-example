import requests


def upload_file(file_path):
    with requests.Session() as session:
        with open(file_path, "rb") as file:
            response = session.post("https://file.io", files={"file": file})
            response.raise_for_status()
            return response.json()


if __name__ == "__main__":
    print(upload_file("sample.txt"))
