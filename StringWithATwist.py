'''The program will recieve 3 English words inputs from STDIN

These three words will be read one at a time, in three separate line
The first word should be changed like all vowels should be replaced by %
The second word should be changed like all consonants should be replaced by #
The third word should be changed like all char should be converted to upper case
Then concatenate the three words and print them
Other than these concatenated word, no other characters/string should or message should be written to STDOUT

For example if you print how are you then output should be h%wa#eYOU.

You can assume that input of each word will not exceed more than 5 chars '''



sentence = str(input("enter three words saperated by space: "))
str1 = sentence.split()
vow = "aeiouAEIOU"
conso = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

if len(str1) == 3:
    for i in vow:
        str1[0]=str1[0].replace(i,"%")

    for i in conso:
        str1[1] = str1[1].replace(i,"#")

    for i in str1[2]:
        str1[2] = str1[2].upper()
for i in str1:
    print(i,end=" ")
