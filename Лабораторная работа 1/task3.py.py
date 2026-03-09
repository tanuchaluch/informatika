list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# индекс середины
middle_index = len(list_players) // 2 # делим количество игроков на 2 целочисленно и находим номер последнего игрока первой группы

first_team = list_players[:middle_index] # исключаем игроков второй группы и получаем игроков первой
second_team = list_players[middle_index:] # исключаем игроков первой группы и получаем игроков второй

print(first_team)
print(second_team)
