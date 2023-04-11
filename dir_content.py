import os
import time

#                     wyswietla sciezke katalogu w ktorym jestesmy

# print(os.getcwd())

#                     zmiana nazwy katalogu

# os.rename('dir_07', 'dir_01')

#           tworzenie i usuwanie katalogu

# os.mkdir("d:\\python\\moje projekty\\dir_content_in_file\\test_dir\\dir_01")
# os.rmdir("d:\\python\\moje projekty\\dir_content_in_file\\test_dir\\dir_01")

#           wyswietla wszystkie pliki i katalagi w danej lokalizacji (lepiej dac podwojne \\)

# list_of_dir = list(os.listdir("D:\\Python\\Moje projekty\\Dir_content_in_file\\test_dir"))


print(os.getcwd())

# podajemy sciezke do katalogu z ktorego chcemy pobrac nazwy pliow / katalogow
os.chdir('D:\\Python\\Moje projekty\\Dir_content_in_file\\test_dir')
print(os.getcwd())

# print(os.stat('test_file_02.txt').st_size)

# printujemy liste plikow i/lub katalogow w danej lokalizacji
list_of_files = os.listdir()
# print(list_of_files)

# tworzymy liste rozmiarow plikow dla poszczegolnych nazw plikow z listy list_of_files
# zamieniamy elementy takiej listy na str i dodajemy slowo "Bajtow"

# for i in list_of_files:
#     size = (os.path.getsize(i))
#     size_list.append(f' Wielkosc pliku: {size} Bajtow')
# print(size_list)

size_list = []
for i in list_of_files:
    size_list.append(f'Wielkosc pliku: {os.path.getsize(i)} Bajtow,'
                     f' Data utworzenia pliku: {time.ctime(os.path.getctime(i))}')
# print(size_list)


# łączymy dwie listy: liste nazw plikow i liste rozmiarow tych plikow
# w sposob naprzemienny (metoda ZIP) tzn. pierwszy element z listy 'list_of_files'
# z pierwszym elementem listy 'size_list' itd. --> wynik to lista tupli

# stats = list(zip(list_of_files, size_list))
# print(stats)

# drugi sposob laczenia list naprzemiennie - wynik to list wartosci/str
stats = []
for i in range(len(list_of_files)):
    stats.append(list_of_files[i])
    stats.append(size_list[i])
print(stats)

# keys = list_of_files
# values = size_list
# slownik = {}
# for keys, values in slownik.items():
#     slownik.update(iter())
# print(slownik)

# podajemy sciezke gdzie ma sie zapisac plik z nazwami plikow / katalogow

plik = open("D:\\Python\\Moje projekty\\Dir_content_in_file\\test_dir\\test_file_02.txt", 'w+')

# zapisuje w pliku elementy listy jeden pod drugim
for i in stats:
    plik.write(str(i) + '\n')

plik.close()

# print(os.walk("d:\\python\\moje projekty\\dir_content_in_file"))
