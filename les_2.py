import csv
import re
import json
from os import listdir
from datetime import datetime
import yaml


# 1
def get_data():
    main_data = ["Изготовитель системы", "Название ОС", "Код продукта", "Тип системы"]
    manufacturers = []
    os_names = []
    product_codes = []
    system_types = []
    for item in listdir("./data"):
        if ".txt" in item:
            with open(f"./data/{item}", "r") as document:
                for line in document.readlines():
                    manufacturer_regexp = re.compile(f"{main_data[0]}:(.*)$").search(line)
                    if manufacturer_regexp:
                        manufacturers.append(manufacturer_regexp.group(1).strip(" "))
                    os_regexp = re.compile(f"{main_data[1]}:(.*)$").search(line)
                    if os_regexp:
                        os_names.append(os_regexp.group(1).strip(" "))
                    product_code_regexp = re.compile(f"{main_data[2]}:(.*)$").search(line)
                    if product_code_regexp:
                        product_codes.append(product_code_regexp.group(1).strip(" "))
                    system_type_regexp = re.compile(f"{main_data[3]}:(.*)$").search(line)
                    if system_type_regexp:
                        system_types.append(system_type_regexp.group(1).strip(" "))
    return main_data, manufacturers, os_names, product_codes, system_types


# 2
def write_to_csv(filename: str):
    main_data, manufacturers, os_names, product_codes, system_types = get_data()
    with open(f'{filename}.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',',
                                quotechar="'", quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(main_data)
        csv_writer.writerow(manufacturers)
        csv_writer.writerow(os_names)
        csv_writer.writerow(product_codes)
        csv_writer.writerow(system_types)


# 3
def write_order_to_json(item: str, quantity: int, price: float, buyer: str, date: datetime):
    formatted_datetime = date.isoformat()
    with open('./data/orders.json', 'w', encoding='utf-8') as json_file:
        order_to_write = {}
        order_to_write["item"] = item
        order_to_write["quantity"] = quantity
        order_to_write["price"] = price
        order_to_write["buyer"] = buyer
        order_to_write["date"] = formatted_datetime

        json.dump(order_to_write, json_file, indent=4)


# 4
def write_to_yaml(data: dict):
    with open('file.yaml', 'w', encoding='utf-8') as yaml_file:
        yaml.dump(data, yaml_file, default_flow_style=True, allow_unicode=True)


write_to_csv("output")
write_order_to_json("item", 1, 100.5, "buyer", datetime(2021, month=10, day=5, hour=12, minute=30, second=5))
write_to_yaml({"list": [1, 2, 3], "number": 1, "stuff": {"euro": "€", "yen": "¥", "utorrent": "µ"}})
# не совпадают, юникод символы записаны неверно
