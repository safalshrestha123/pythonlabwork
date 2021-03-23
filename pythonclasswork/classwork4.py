"""import random

number=random.randint(1,10)
print(number)
guess=int(input('Guess the number?'))
while number !=guess:
    guess=int(input('uff!! try again : guess again:'))
else:
    print('congractulation!!!!! you are right..')"""


import random
num= random.randint(1,10)

while True:
    guess= int(input('Please guess the num:'))
    if guess== num:
        print("congracts")
        break
    print('uff!! try again')
