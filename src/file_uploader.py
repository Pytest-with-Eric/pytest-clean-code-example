import requests


def upload_file(file_path):
    with open(file_path, "rb") as file:
        response = requests.post("https://file.io", files={"file": file})
        response.raise_for_status()
        return response.json()


if __name__ == "__main__":
    print(upload_file("sample.txt"))
