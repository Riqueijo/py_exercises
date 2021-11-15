#!/usr/bin/env python

"""
some exercises to develop my logic
"""

__author__ = "Henrique Daguerre"

class ex:
    def o1(self):
        print("Hello, Word!")

    def o2(self):
        name = str(input("What is your name?\n"))
        print(f"Hi {name}")

    def o3(self):
        a = input(' ')
        print(f'Primitive type: {type(a)}')
        print(f'There is spaces? {a.isspace()}')
        print(f'Is a number? {a.isnumeric()}')
        print(f'Is alfabetic? {a.isalpha()}')
        print(f'is alphanumeric? {a.isalnum()}')
        print(f'Is in uppercase? {a.isupper()}')
        print(f'Is in lowecase? {a.islower()}')
        print(f'is capitalized? {a.istitle()}')

    def o4(self):
        num = int(input("Type a number\n"))
        print(f"predecessor {num - 1}\nsuccessor {num + 1}")

    def o5(self):
        num = int(input("Number: "))
        print(f"Double {num * 2}\nTriple {num * 3}\nsqrt {num ** (1/2)}")

    def o6(self):
        #arithmetic average
        nums = input("Numbers: ").split(sep=" ")
        count = len(nums)
        numsum = sum(list(map(int, nums)))
        print(f"arithmetic average {numsum / count}")

    def o7(self):
        med = float(input('distance in metters: '))
        mm = med * 1000
        cm = med * 100
        dm = med * 10
        dam = med / 10
        hm = med / 100
        km = med / 1000
        print(f'the measure of {med} is \n{km} \n{hm} \n{dam} \n{dm} \n{cm} \n{mm}')

    def o8(num):
        if isinstance(num, str) == True:
            print("ERRO")
            quit()
        else:
            for c in range(0, 11):
                print(c * num)

    def o9(money):
        dolar = 6.8
        print(f"you have R${dolar / money}")

    def I0(self):
        width = float(input('width: '))
        height = float(input('height: '))
        print(f'dimension: {width}x{height} area: {width * height}m².')
        print(f'you will need {width * (height / 2)}L of paint.')



