import csv
import json


def make_fixture(csv_file_path: str, json_file_path: str, model_name: str):
    data = []

    with open(csv_file_path, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for row in csvReader:
            fixture_dict = {}
            fields_dict = {}
            for key, value in list(row.items())[1:]:
                if key == "is_published":
                    fields_dict[key] = bool(row[key])
                else:
                    fields_dict[key] = row[key]
            fixture_dict["model"] = "ads." + model_name
            fixture_dict["pk"] = row[list(row.keys())[0]]
            fixture_dict["fields"] = fields_dict

            data.append(fixture_dict)

    with open(json_file_path, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4, ensure_ascii=False))


make_fixture("categories.csv", "categories.json", "Category")
make_fixture("ads.csv", "ads.json", "Ad")
