import base64
import json


def convert_file_to_base64(file_path):
    with open(file_path, "rb") as f:
        file_data = f.read()
    return base64.b64encode(file_data).decode("utf-8")


if __name__ == "__main__":
    input_file = "test_input.mp3"
    output_base64 = convert_file_to_base64(input_file)
    json_data = {"messages": [], "audio": output_base64}
    with open("test_input.json", "w") as file:
        json.dump(json_data, file)
    print(json_data)
