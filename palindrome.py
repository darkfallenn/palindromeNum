# This function determines if a number is a palindrome, in other words, the same as the reverse
# of itself. We'll use index skipping and list casting to do this.

def palindromeNum(num):
    if num < 0 or (num != 0 and num % 10 == 0): # Check if it's negative or divisible by 10.
        return False
    
    if list(str(num)) == list(str(num))[::-1]: # Check if it's equal to it's reverse
        return True
    
    return False

