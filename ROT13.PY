def rot13(message):
    rot13 = str.maketrans(
        'ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz',
         'NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm')
        
    hello = message.translate(rot13)
    return hello

# https://www.codewars.com/kata/530e15517bc88ac656000716