'''Problem Statement – Given a string S(input consisting) of ‘*’ and ‘#’.
# The length of the string is variable. The task is to find the minimum number of ‘*’ or ‘#’ to make it a valid string.
# The string is considered valid if the number of ‘*’ and ‘#’ are equal. The ‘*’ and ‘#’ can be at any position in the string.
Note : The output will be a positive or negative integer based on number of ‘*’ and ‘#’ in the input string.

(*>#): positive integer
(#>*): negative integer
(#=*): 0'''

str1 = str(input("enter a string in form of # and * only: "))
star_count = 0
hash_count = 0
for i in str1:
    if i == "*":
        star_count+=1
    elif i == "#":
        hash_count+=1

if star_count == hash_count:
    print(0)
elif star_count > hash_count:
    print(star_count-hash_count)
else:
    print(hash_count-star_count)