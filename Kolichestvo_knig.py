size_of_disk_megabites = 1.44
sheets = 100
lines = 50
symbols = 25
size_of_symbol_bites = 4

bites_to_kilobite = 1024
bites_to_megabite = bites_to_kilobite * 1024

size_of_book_bites = sheets * lines * symbols * size_of_symbol_bites

# print("Вес книги в байтах:", size_of_book_bites)

size_of_book_megabites = size_of_book_bites / bites_to_megabite

# print(size_of_book_megabites)










# TODO Найдите количество книг, которое можно разместить на дискете

print("Количество книг, помещающихся на дискету:", int(size_of_disk_megabites // size_of_book_megabites))
