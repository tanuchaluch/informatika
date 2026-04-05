# TODO импортировать необходимые молули
import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    ...  # TODO считать содержимое csv файла

    ...  # TODO Сериализовать в файл с отступами равными 4
    with open(INPUT_FILENAME, 'r') as f:
        reader = csv.DictReader(f, delimiter=',')  # преобразуем каждую строку в словарь
        data = list(reader)  # преобразуем все строки в список словарей

    with open(OUTPUT_FILENAME, 'w') as f:
        json.dump(data, f, indent=4)  # сериализуем в JSON формат

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
