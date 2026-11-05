class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        "palindrome" - TWO POINTER METHOD

        inputs: s (string)
        outputs: true/false (boolean)

        things to keep in mind:
        - case insensitive so we can compare each character as upper or lower
        - ignores all non-alphanumeric characters like ! , " _ (not a-z and numbers)

        built-in functions used:
        .lower() <= DO NOT USE .islower()! they are different!
        .isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9)

        i think this solution is better than the one on neetcode:
        https://www.youtube.com/watch?v=Nxzstmv_U0U
        '''

        l = 0
        r = len(s) - 1

        while l < r: # don't need to use <= because = means l = r and we know that obviously means the same char
            # check if the character at l and r are non-alphanumeric, then move pointer on l or r
            if (s[l].isalnum() == False):
                l += 1 # skip this character, move to next character
                continue # jump back to while l < r and skip the rest of the conditional statements

            if (s[r].isalnum() == False):
                r -= 1
                continue

            if (s[l].lower() != s[r].lower()): # checks if the characters are the same characters after being converted to lowercase
                return False
            
            if (s[l].lower() == s[r].lower()): # if the characters are the same, keep going through the s
                l += 1
                r -= 1

        return True
