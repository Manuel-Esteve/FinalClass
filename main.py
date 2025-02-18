import china

from japan import cook as japan_cook
from china import cook as china_cook
from japan import is_prime

def cook():
    print("We are Spanish we are making Paella")

from latam.peru import cook as peru_cook

print(china.greet)
japan.cook()
china_cook()
cook()
print(f"1027 is prime: {is_prime(1027)}")

peru.cook()