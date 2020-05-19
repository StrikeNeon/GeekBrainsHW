# -*- coding: utf-8 -*-

#1
def divide(n1, n2):
    if n2 == 0:
        return "division by zero"
    else:
        return n1 / n2
    
print(divide(4,2))

#2
def data_output(name, surname, YOB, city, email, phone_number):
    print(f"User {name} {surname}, born in {YOB}, lives in {city}, contact information: email: {email}, contact number {phone_number}")
    
data_output(name = "For", surname = "Chan", YOB = "2007", city = "Americaville", email = "4chan.org", phone_number = "666-666-666")

#3
def my_func(a,b,c):
    if a>=b>=c or b>=a>=c:
        return a+b
    elif c>=b>=a or b>=c>=a:
        return c+b
    elif c>=a>=b or a>=c>=b:
        return c+a
print(my_func(2,5,3))

#4
def power1(x,y):
    return 1/x**y

def power2(x,y):
    i = x
    while y !=1:
        x *= i
        y -=1
    return 1/x

print(power1(2,2), power2(2,2))

#5
def seq_sum():
    s = 0
    while True:
        inp = input("input number sequence, input 00 to stop the program")
        data = inp.split()
        for num in data:
            if num == "00":
                return s
            else:
                s += int(num)
    
print(seq_sum())

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
