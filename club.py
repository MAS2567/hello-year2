people = [
    {"name": "Орлов", "grade": 7, "hours": 12},
    {"name": "Белова", "grade": 9, "hours": 20},
    {"name": "Шаров", "grade": 10, "hours": 16},
    {"name": "Новикова", "grade": 8, "hours": 9},
]


def label(people_dict):
    n = people_dict["name"]
    g = people_dict["grade"]
    h = people_dict["hours"]
    return f"{n}, {g} класс, {h} ч."


def add():
    n = input("Введите фамилию: ")
    g = input("Введите номер класса: ")
    h = input("Введите кол-во часов: ")

    new_person = {}
    new_person["name"] = n
    new_person["grade"] = g
    new_person["hours"] = h
    return new_person
#people.append(add())

def by_grade(people, min_grade):
    people_2 = []
    for p in people:
        if p["grade"] >= min_grade:
            people_2.append(p)
    return people_2


found = by_grade(people, 9)
print(len(found))
for person in found:
    print(label(person))