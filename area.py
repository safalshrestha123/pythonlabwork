# 2.Write a program that reads the length of the base and the height of a rt angle triangle
#and prints the area.every number is given on a separate line

length = int(input("Enter the value of lenth:"))
height = int(input("Enter the height: "))
area = (length*height)//2
##the floor division // rounds the result down to the nearest whole number

print(f"The area of right angled triangle is{area}")##

name = input("Enter your name:")
age = int(input("enter age:"))

print (f'my name is {name}. and my age is {age}.')
print("1.hello my name is "+name+" and i am "+str(age)+" years old. ")
print ("2.hello my name is", name, "and i am", age,"years old.")
print ("3.hello my name is {} and i am {} years old".format(name,age))
print("3.hello my name is %s and i am %d years old"%(name, age))



