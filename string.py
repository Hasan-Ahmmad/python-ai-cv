# string operation on sentece

# a = input("Enter a sentece: ")

# a = a.strip().lower()

# word = a.split()

# cnt1 = len(word)

# a = a.replace(" ","")

# cnt2 = len(a)

# longest = word[0]

# for x in word:
#     if len(x) > len(longest):
#         longest = x

# print(a)

# print("Number of word:", cnt1)

# print("Number of character:", cnt2)

# print("Longest word:", longest)






# substring operation

a = input("Enter the string: ")

L = int(input("first integer:"))

R = int(input("Seconf integer:"))

b = a[L:R]

print("substring from l to r:", b)

print("first three char:", a[:3])

print('last three char:', a[-3:])

c = a[::-1]

print("reverse string:", c)

d = a[::2]

print(d)

