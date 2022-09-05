str1 = "oprah oprah pasa dhssd 12 $$%sada %w71"
sub_str = "op"
count = 0
for index in range(len(str1)):
    next_len = index+ len(sub_str)
    if str1[index:next_len] == sub_str:
        count+=1


print(count)