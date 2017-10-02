def isPalindrome(charSequence):
    charList = list(charSequence)
    i = 0
    charLen = len(charList)
    while(i < (charLen/2)):
        if(charList[i] != charList[charLen - 1 - i]):
            return False
        i+=1

    return True
