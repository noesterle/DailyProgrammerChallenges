__author__ = 'nathan'

import random

def typoglycemia(strng):
    ary = strng.split()
    final = ""
    for i in range(len(ary)):
        if not ary[i][-1].isalpha():
            mid = ary[i][1:-2]
            x = True
        else:
            mid = ary[i][1:-1]
            x = False
        result=[]
        for item in mid:
            result.append(item)
        random.shuffle(result)
        resultString=""
        for item in result:
            resultString += item
        if x:
            final += ary[i][0]+resultString+ary[i][-2:] + " "
        else:
            if len(ary[i])==1:
                final += ary[i] + " "
            else:
                final += ary[i][0]+resultString+ary[i][-1:] + " "
    return final

if __name__ == '__main__':
    s = input("Enter a string to scramble and read: ")
    scrambled = typoglycemia(s)
    print(scrambled)