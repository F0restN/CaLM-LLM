import json


def output_as_file(data, file_path):
    with open(file_path, "w") as f:
        f.write(data)


def output_as_json(data, file_path):
    with open(file_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
