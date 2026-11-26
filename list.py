# basics operations

# a = [2,3,4,5,67,90]

# Max = Min = a[0] 
# Sum = 0
# avg=0
# cnt1=0

# for x in a:
#     Max = max(Max, x)

#     Min = min(Min, x)

#     Sum += x

#     if x%2 == 0:
#         cnt1 +=1

# print("Max value ", Max)

# print("Min value ", Min)

# print("sum ", Sum)

# print("average value ", Sum/len(a))

# print("Even number ", cnt1)





# making list distinct

# numbers = [1, 2, 3, 2, 4, 1, 5, 3]

# a = []

# for i in numbers:
#     if i not in a:
#         a.append(i)

# print(a)





# finding second largest distinct element

# n = int(input("Enter list size: "))

# number = []

# for i in range(n):
#     x = int(input())
#     number.append(x)

# a = list(set(number))

# if len(a) <2:
#     print("No second largest element")
# else:
#     a.sort()

#     print("Second largest element is:", a[-2])





# without sorting

n = int(input("Enter list size: "))

number = []

for i in range(n):
    x = int(input())
    number.append(x)

a = number[0]
b = 0

for i in range(1,n):
    if number[i]>a:
        b = a
        a = number[i]
    elif number[i] > b and number[i] !=a:
        b = number[i]    

if b == 0:
    print("No second largest element")
else:
    print("Second largest element is:", b)









