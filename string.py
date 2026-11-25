a = input("Enter a sentece: ")

a = a.strip().lower()

word = a.split()

cnt1 = len(word)

a = a.replace(" ","")

cnt2 = len(a)

longest = word[0]

for x in word:
    if len(x) > len(longest):
        longest = x

print(a)

print("Number of word:", cnt1)

print("Number of character:", cnt2)

print("Longest word:", longest)