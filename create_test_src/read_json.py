import json


def read_json_file(file_path):
    with open(file_path, 'r') as f:
        json_data = json.load(f)
    return json_data


if __name__ == "__main__":
    input_file = "test_input.json"
    json_object = read_json_file(input_file)
    print(json_object["text"])
