from torch.ao.quantization.backend_config.onednn import onednn_dynamic_int8_dtype_config

from util.check_palindrome import isPalindrome


def longestPalindrome(self, s):

    return checkPalindrome(s[0], 0, 1, s)

def checkPalindrome(maxpalindrome, span, index, s):
    if index == len(s):
        return maxpalindrome


    oddsubstring = s[index - span: index + span + 1]
    evensubstring = s[index - span - 1:index + span + 1]

    if isPalindrome(evensubstring):
        if len(evensubstring) > len(maxpalindrome):
            maxpalindrome = evensubstring
        return checkPalindrome(maxpalindrome, span + 1, index, s)
    elif isPalindrome(oddsubstring):
        if len(oddsubstring) > len(maxpalindrome):
            maxpalindrome = oddsubstring
        return checkPalindrome(maxpalindrome, span + 1, index, s)
    else:
        return checkPalindrome(maxpalindrome, 0, index + 1, s)

s = "ccc"
print(longestPalindrome(None, s))
