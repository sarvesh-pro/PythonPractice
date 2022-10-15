import array as ar
arr = ar.array("i",[int(input("enter element:")) for i in range(3)])

result = 0
temp = 0
for i in range(len(arr)):
    temp=0
    for j in range(i,len(arr)):
        temp += arr[j]
        result += temp

print(result)