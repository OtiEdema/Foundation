# Write a program to find lagest and second largest number from range of x numbers inputed

large = larger = 0
x=int(input('Enter range'))
for i in range (x):
    n=int(input('Enter numbers'))
    if i == 0:
        large = n
    elif i == 1:
        if n >= large:
            larger=n
        else:
            larger = large
            large=n
    else:
        if n>larger:
            large=larger
            larger = n
        elif n > large:
            large = n
print('the  largest number is', larger)
print('the  secound largest number is', large)

