def isPalindrome(charSequence):
    """Checks whether any sequence of characters are the same when the sequence is reversed.

        Args:
            charSequence: Sequence of characters of any type.

        Returns:
            Returns a boolean on whether the char sequence is a Palindrome or not.
        """
    charList = list(charSequence)
    i = 0
    charLen = len(charList)
    while(i < (charLen/2)):
        if(charList[i] != charList[charLen - 1 - i]):
            return False
        i+=1

    return True
