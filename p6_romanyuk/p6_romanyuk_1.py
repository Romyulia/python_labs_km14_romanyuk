phrase1 = input("Enter the first phrase: ")
first_phrase = set()
for i in phrase1:
    if i.isalpha():
        first_phrase.add(i.lower())
phrase2 = input("Enter the second phrase: ")
second_phrase = set()
for i in phrase2:
    if i.isalpha():
        second_phrase.add(i.lower())
print("Set of letters of the first phrase: " + str(first_phrase))
print("Set of letters of the second phrase: " + str(second_phrase))
if len(second_phrase - first_phrase) != 0:
    print("You can't make the second phrase.")
else:
    print("You can make the second phrase.")