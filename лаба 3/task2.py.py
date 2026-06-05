# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

def find_common_participants(first_group, second_group, delimiter=','):
    first_list = first_group.split(delimiter)
    second_list = second_group.split(delimiter)
    common = [p for p in first_list if p in second_list]  # Генератор списка
    common.sort()
    return common


participants_first = "Иванов,Петров,Сидоров"
participants_second = "Петров,Сидоров,Смирнов"

print(find_common_participants(participants_first, participants_second))


