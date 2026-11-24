# largest among three

# a = int(input("Enter first number: "))

# b = int(input("Enter second number: "))

# c = int(input("Enter third number: "))

# if a>=b and a>=c:
#     print(a, "is largest")
# elif b>=a and b>=c:
#     print(b, "is largest")
# else:
    
#     print(c, "is largest")






# # time converter

# a = int(input())

# hr = a//3600

# a %= 3600

# min = a//60

# a %= 60

# print("Hours ", hr)

# print("Minutes ",min)

# print("Seconds ", a)






# # bill calculate

# bill = float(input())

# serviceCharge = int(input())

# friend = int(input())

# bill += bill*(serviceCharge/100)

# print("Bill per each: ", bill/friend)





# # leap year

# year = int(input())

# if year%400 ==0 or (year%4 == 0 and year%100 != 0):
#     print(year, "is Leap year")
# else:
#     print(year, "is Not leap year")





# # grade calculation

# mark = []

# total = average = 0

# for i in range(5):
#     num = int(input("Enter the mark: "))

#     while (num>100 or num<0):
#         print("Invalid mark")
#         num = int(input("Enter the mark: "))

#     mark.append(num)

# total = sum(mark)
# average = total/5

# if average>=80:
#     print("Grade: A+")
# elif average >=70:
#     print("Grade: A")
# elif average>=60:
#     print("Garde: A-")
# elif average>=50:
#     print("Grade: B")
# elif average>=40:
#     print("Grade: C")
# else:
#     print("Grade: F")

# print("Average: ", average)






# # divisibility cheak

# num = int(input("enter the number: "))

# cnt1 = cnt2 = cnt3 = cnt4 = 0

# for i in range(1,num+1):
#     if i%3 == 0:
#         cnt1 +=1
#     if i%5 == 0:
#         cnt2 +=1
#     if i%3 == 0 and i%5 == 0:
#         cnt3 +=1
#     if i%3 != 0 and i%5 !=0:
#         cnt4 +=1
    
# print("by 3:", cnt1)
# print("by 5:", cnt2)
# print("by both:",cnt3)
# print("by none:", cnt4)





# collatz sequence

# num = int(input("enter the number: "))

# print(num, end=" ")
# i = 0
# while num>1:
#     if num%2 == 0:
#         num //=2
#         i +=1
#         print(num , end=" ")
#     else:
#         num *=3
#         num +=1
#         i +=1
#         print(num, end=" ")

# print()
# print("steps:", i)


