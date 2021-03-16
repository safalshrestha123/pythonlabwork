'''N students take K apples and distribute them among each other evenly.the remaining (the undivisible)part remains in basket
how many apple each single student get?how many apples will remain on basket?The program reads the number N and K.
it should print the two answers for the question above'''

N = int(input("Enter the number of students in class:"))
K = int(input("Enter the number of apples:"))
D =(K//N)
R = (K%N)
print(f"each student got {D}")
print(f"the remaining apples are {R}")
