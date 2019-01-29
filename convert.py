import csv
# pip install pyyaml if this fails
import yaml

with open("text_data.yml") as fin:
    y = yaml.load(fin.read())

    with open("training.csv", "w") as fout:
        c = csv.writer(fout, delimiter=";", lineterminator="\n")

        # Collect all keys for writing header row
        header = []
        for item in y["training"]["trainings"]:
            for k in item.keys():
                if k not in header:
                    header.append(k)

        c.writerow(header)

        for item in y["training"]["trainings"]:
            row = []
            for k in header:
                row.append(item.get(k, ""))

            c.writerow(row)
