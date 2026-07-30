#"Read a document and return text.
import json


def load_dataset(file_path):

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data