# TODO Напишите функцию find_common_participants

def find_common_participants(str_1, str_2, sep=","):
    set_of_str_1 = set(str_1.split(sep))
    # print(set_of_str_1)
    set_of_str_2 = set(str_2.split(sep))
    # print(set_of_str_2)
    set_common_participants = set_of_str_1.intersection(set_of_str_2)
    list_common_participants = list(set_common_participants)

    return list_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

common_participants = find_common_participants(participants_first_group, participants_second_group, sep="|")
common_participants.sort()

print(common_participants)


