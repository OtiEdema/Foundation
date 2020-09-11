# Write a program to find lowest and second lowest number from range of x numbers inputed

small  = smaller = 0
x=int(input('Enter range'))
for i in range (x):
    n=int(input('Enter numbers'))
    if i == 0:
        small = n
    elif i == 1:
        if n <= small:
            smaller=n
        else:
            smaller = small
            small=n
    else:
        if n<smaller:
            small=smaller
            smaller = n
        elif n < small:
            small = n
print('the  lowest number is', smaller)
print('the  secound lowest number is', small)

