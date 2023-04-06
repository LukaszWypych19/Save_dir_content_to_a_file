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
os.chdir('D:\\Python\\Moje projekty\\Dir_content_in_file\\test_dir')
print(os.getcwd())

list_of_files = os.listdir()
print(list_of_files)

plik = open("test_file_02.txt", 'w+')

for i in list_of_files:
    plik.write(i + '\n')

plik.close()


# print(os.walk("d:\\python\\moje projekty\\dir_content_in_file"))
