import csv


def person_from_row(row):
    row["grade"] = int(row["grade"])
    row["hours"] = int(row["hours"])

    return row

people = []
total = 0

try:
    with open("club.csv", encoding= "utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            people.append(person_from_row(row))
except FileNotFoundError:
    print("Извините, файл не найден или был перемещен.")


with open("seniors.csv", "w", encoding= "utf-8", newline= "") as f:
    writer = csv.DictWriter(f, fieldnames= ["name", "grade", "hours"])
    writer.writeheader()
    for row in people:
        if row["grade"] >= 9:
            writer.writerow(row)
        total += row["hours"]
    print(total)
