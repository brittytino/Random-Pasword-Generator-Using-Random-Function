import random
a= int(input("Enter the length of Password :"))
b="01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()?"
c= "".join(random.sample(b,a))
print(c)
