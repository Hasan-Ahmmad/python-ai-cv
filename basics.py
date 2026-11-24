# # # # # largest among three

# # # # # a = int(input("Enter first number: "))

# # # # # b = int(input("Enter second number: "))

# # # # # c = int(input("Enter third number: "))

# # # # # if a>=b and a>=c:
# # # # #     print(a, "is largest")
# # # # # elif b>=a and b>=c:
# # # # #     print(b, "is largest")
# # # # # else:
    
# # # # #     print(c, "is largest")




# # # # # time converter

# # # # a = int(input())

# # # # hr = a//3600

# # # # a %= 3600

# # # # min = a//60

# # # # a %= 60

# # # # print("Hours ", hr)

# # # # print("Minutes ",min)

# # # # print("Seconds ", a)



# # # # bill calculate

# # # bill = float(input())

# # # serviceCharge = int(input())

# # # friend = int(input())

# # # bill += bill*(serviceCharge/100)

# # # print("Bill per each: ", bill/friend)




# # # leap year

# # year = int(input())

# # if year%400 ==0 or (year%4 == 0 and year%100 != 0):
# #     print(year, "is Leap year")
# # else:
# #     print(year, "is Not leap year")



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
