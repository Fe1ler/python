users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

dict_of_site = {
    "Общее количество": 0,
    "Уникальные посещения": 0,
}

amount_of_visit = len(users)

dict_of_site["Общее количество"] = amount_of_visit

set_users = set(users)

amount_of_unique_visit = len(set_users)


dict_of_site["Уникальные посещения"] = amount_of_unique_visit


print(dict_of_site)

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
