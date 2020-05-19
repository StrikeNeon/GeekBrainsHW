# -*- coding: utf-8 -*-

#6
def int_func1(string):
    conv_string = chr(ord(string[0])-32)+string[1:]
    return conv_string

print(int_func1('crocodile'))

def int_func2(string):
    words = string.split()
    for word in words:
        words[words.index(word)] = chr(ord(word[0])-32)+word[1:]
    words = ' '.join(words)
    return words
        
print(int_func2('see you later alligator in a while crocodile'))