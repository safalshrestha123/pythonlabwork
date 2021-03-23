"""for val in "string":
    if val == "g":
        break
    print(val)
print("end")"""

'''fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)'''

'''num=int(input("enter the number for factorial:"))
product=1
for i in range(num,0,-1):
    product = product*i
print(f'the factorial of {num} is {product} ')'''

num=int(input("Enter the number:"))
for i in range(1,11):
    mul=num*i
    print(num,'*',i,'=',mul)