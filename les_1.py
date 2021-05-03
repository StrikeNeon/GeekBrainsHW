import sys
import subprocess
import chardet

# 1
raw_strings = ["разработка", "сокет", "декоратор"]
encoded_strings = [raw_strings[0].encode('utf-8'), raw_strings[1].encode('utf-8'),
                   raw_strings[2].encode('utf-8')]
print(raw_strings[0], raw_strings[1], raw_strings[2])
print(type(raw_strings[0]), type(raw_strings[1]), type(raw_strings[2]))
print("Вес обьекта str ", sys.getsizeof(raw_strings[0]),
      sys.getsizeof(raw_strings[1]),
      sys.getsizeof(raw_strings[2]))

print(encoded_strings[0], encoded_strings[1], encoded_strings[2]) 
print(type(encoded_strings[0]), type(encoded_strings[1]), type(encoded_strings[2]))
print("Вес юникод строки ", sys.getsizeof(encoded_strings[0]),
      sys.getsizeof(encoded_strings[1]),
      sys.getsizeof(encoded_strings[2]))

# 2

raw_strings = ["class", "function", "method"]
encoded_strings = [b"class", b"function", b"method"]
print(raw_strings[0], raw_strings[1], raw_strings[2])
print(type(raw_strings[0]), type(raw_strings[1]), type(raw_strings[2]))
print("Вес обьекта str ", sys.getsizeof(raw_strings[0]),
      sys.getsizeof(raw_strings[1]),
      sys.getsizeof(raw_strings[2]))
print("длинна обьекта str ", len(raw_strings[0]),
      len(raw_strings[1]),
      len(raw_strings[2]))
print(encoded_strings[0], encoded_strings[1], encoded_strings[2]) 
print(type(encoded_strings[0]), type(encoded_strings[1]), type(encoded_strings[2]))
print("Вес битовой строки ", sys.getsizeof(encoded_strings[0]),
      sys.getsizeof(encoded_strings[1]),
      sys.getsizeof(encoded_strings[2]))
print("длинна битовой строки ", len(encoded_strings[0]),
      len(encoded_strings[1]),
      len(encoded_strings[2]))

# 3

raw_strings = [b"attribute",
               # класс
               # функция
               # все русские, их нет в ASCII таблице
               b"type"]
print(raw_strings[0], raw_strings[1])

# 4

encoded_strings = ["разработка".encode('utf-8'),
                   "администрирование".encode('utf-8'),
                   "protocol".encode('utf-8'),
                   "standard".encode('utf-8')]
decoded_strings = [encoded_strings[0].decode('utf-8'),
                   encoded_strings[1].decode('utf-8'),
                   encoded_strings[2].decode('utf-8'),
                   encoded_strings[3].decode('utf-8')]

print(encoded_strings[0], encoded_strings[1],
      encoded_strings[2], encoded_strings[3])
print(decoded_strings[0], decoded_strings[1],
      decoded_strings[2], decoded_strings[3])

# 5

args = [['ping', 'yandex.ru'], ['ping', 'youtube.com']]

for arg in args:
    subproc_ping = subprocess.Popen(arg, stdout=subprocess.PIPE)

    for line in subproc_ping.stdout:
        line = line.decode('cp866').encode('utf-8')
        print(line.decode('utf-8'))

# 6

write_test_lines = ["сетевое программирование", "сокет", "декоратор"]
try:
    with open("test_file.txt", "w") as write_file:
        for line in write_test_lines:
            write_file.write(line)
            write_file.write("\n")
except FileExistsError:
    pass

with open("test_file.txt", 'rb') as read_file:
    rawdata = b''.join([read_file.readline() for _ in range(3)])

print(chardet.detect(rawdata)['encoding'])

try:
    with open("test_file.txt", 'rb') as read_file:
        for line in read_file:
            print(read_file.readline().decode('utf8'))
except UnicodeDecodeError:
    # не прочитает
    pass
