import os
import json

class CSVToJsonConverter:
    def __init__(self, directory):
        self.directory = directory
        self.json_format_list = []

    def read_csv_files(self):
        csv_files = [file for file in os.listdir(self.directory) if file.endswith(".csv")]

        for file in csv_files:
            with open(os.path.join(self.directory, file), mode="r") as f:
                csv_format = f.read()

            rows = csv_format.strip().split("\n")
            list_of_rows = [line.split(",") for line in rows]

            for row in list_of_rows:
                converted_dict = {index: item for index, item in enumerate(row)}
                self.json_format_list.append(converted_dict)
        self.json_format_list = json.dumps(self.json_format_list,indent=4)

    def write_to_file(self, filename):
        with open(filename, mode="w") as f:
            f.write(self.json_format_list)

if __name__ == "__main__":
    converter = CSVToJsonConverter(".")
    converter.read_csv_files()
    print(converter.json_format_list)
    
    converter.write_to_file("results.json")
