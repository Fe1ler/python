# TODO  Напишите функцию count_letters

def count_letters(str_):
    lower_str_ = str_.lower()
    pure_str = ""

    for char in lower_str_:
        if char.isalpha():
            pure_str += char

    dict_str = dict.fromkeys(pure_str, 0)

    for char in pure_str:
        dict_str[char] += 1

    # print(dict_str)
    return dict_str

# TODO Напишите функцию calculate_frequency


def calculate_frequency(dict_str):
    dict_freq = {}
    quantity_of_letters = 0

    for value in dict_str:
        quantity_of_letters += dict_str[value]



    for value in dict_str:
        dict_freq[value] = (dict_str[value] / quantity_of_letters)

    for keys, value in dict_freq.items():
        print(f"{keys}: {value:.2f}")

    return None




main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

calculate_frequency(count_letters(main_str))






# TODO Распечатайте в столбик букву и её частоту в тексте
