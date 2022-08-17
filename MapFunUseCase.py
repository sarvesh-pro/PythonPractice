def fun(n):

    return str(n).upper()
str1 = ['i', 'l', 'o', 'v', 'e', 't', 'o', 'c', 'o', 'd', 'e']
uppercase_string = list(map(fun,str1))
print(uppercase_string)