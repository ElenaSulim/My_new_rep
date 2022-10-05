# Задание_1
# text = b'r\xc3\xa9sum\xc3\xa9'
# decod = text.decode()
# print(decod)
# text_2 = decod.encode('Latin1')
# print(text_2)
# text_3 = text_2.decode('Latin1')
# print(text_3)

# Задание_2
# name_1, name_2, name_3, name_4 = "Elena", "Svetlana", "Anna", "Viktoria"
# data = open('name.txt', 'w')
# data.write(name_1 + '\n' + name_2)
# data.close()

# data = open('name.txt', 'a')
# data.write('\n' + name_3 + '\n' + name_4)
# data.close()

# Задание_3
# import json
# data = {
#     111111: ("Elena", 20),
#     222222: ("Svetlana",22),
#     333333: ("Anna", 24),
#     444444: ("Viktoria", 26),
#     555555: ("Olga",28)
# }
# with open('name_2.json', 'w') as file:
#     json.dump(data, file)

# Задание_4
#
import json
data = {
    111111: ("Elena", 20),
    222222: ("Svetlana",22),
    333333: ("Anna", 24),
    444444: ("Viktoria", 26),
    555555: ("Olga",28)
}

dict = {}
a = []

for key, value in data.items():
    dict['id'] = key
    dict["name"] = value[0]
    dict["age"] = value[1]
    a.append(dict)
print(a)
with open("../../data.json", "w") as file:
     json.dump(data, file)


import csv

with open("list.json", "r") as file:
    json_data = json.load(file)
    print(json_data)

with open("../../list.csv", "w", newline="") as file:
    writer = csv.writer(file)
    header = ["id", "name", "age", "phone"]
    writer.writerow(header)

    for i in json_data:
        id_i = i
        name = json_data.get(i)[0]
        age = json_data.get(i)[1]
        phone = f"(+33){i}"

        writer.writerow(
            (id_i, name, age, phone))

