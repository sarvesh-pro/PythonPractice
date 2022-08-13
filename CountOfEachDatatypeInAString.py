str1 = str(input("enter your sentence"))
count_dig = 0

def counter(str1):
    vowel = ['a', 'e', 'i', 'o', 'u']
    consonants = "bcdfghjklmnpqrstvwxyz"
    consosplit = [str(i) for i in consonants]
    special_char = [' ','@','$','%','^','&','(',')','?','-','_','!','<','>','#']
    count_dig = 0
    count_vow = 0
    count_cons= 0
    count_sp = 0
    for i in str1:
       if i.isdigit() == True:
           count_dig+=1

       elif i in vowel:
           count_vow+=1
       elif i in consosplit:
           count_cons+=1
       elif i in special_char:
           count_sp += 1

    print("digit:",count_dig)
    print("consonant:",count_cons)
    print("special:",count_sp)
    print("vowel:",count_vow)

    #return ''.join('vowel is {}'.format(count_vow) +'\n'+'digit is {}'.format(count_dig)) +'\n'+ "consonants is {}".format(count_cons)+'\n'+'special character is {}'.format(count_sp)

counter(str1)