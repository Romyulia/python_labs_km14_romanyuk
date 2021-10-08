word_list = list(input("Enter objects' names:").split())
print(word_list[0], end=' ')
for i in range(1, len(word_list)-1):
    print(', ' + word_list[i], end=' ')
if len(word_list) > 1:
    print('and ' + word_list[-1])