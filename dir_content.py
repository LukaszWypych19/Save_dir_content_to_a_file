import os

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

                    # printujemy liste plikow i/lub katalogow w danej lokalizacji
list_of_files = os.listdir()
print(list_of_files)

            # tworzymy liste rozmiarow dla poszczegolnych plikow
size_list = []
for i in list_of_files:
    size = (os.path.getsize(i))
    size_list.append(size)
print(size_list)


                       #podajemy sciezke gdzie ma sie zapisac plik z nazwami plikow / katalogow

plik = open("D:\\Python\\Moje projekty\\Dir_content_in_file\\test_dir\\test_file_02.txt", 'w+')

                        # zapisuje w pliku elementy listy jeden pod drugim
for i in list_of_files:
    plik.write(i + "\n")

plik.close()


# print(os.walk("d:\\python\\moje projekty\\dir_content_in_file"))
