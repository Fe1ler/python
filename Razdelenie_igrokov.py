list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

amount_players = len(list_players)

# print(amount_players)

middle_index = len(list_players) // 2

first_team = list_players[:middle_index]
second_team = list_players[middle_index:]

print(f"{first_team}\n{second_team}")

# TODO Разделите участников на две команды
