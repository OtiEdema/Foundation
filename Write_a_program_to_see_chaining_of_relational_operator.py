# Write a program to see chaining of relational operator
num1 = 10
num2 = 20
if (num1 > num2):
    print ('num1 is greater than2')
else:
    print('num1 is not greater than num2')
#Chaining of relation1
num1 = 10
num2 = 20
num3 = 30
num = (num1<(num1 <= num3)>= (num1 < num2))
print(num)
