def isPalindrome(x: int) -> bool:
    """
    A palindrome is a number that reads the exact same forward and backward.
    Examples:
      121 -> reading backward is 121 (True)
     -121 -> reading backward is 121- (False, minus is at the end)
       10 -> reading backward is 01 (False)
    """

    # --- Step 1: Handle obvious cases ---
    
    # 1. Any negative number is NOT a palindrome because of the '-' sign.
    #    For example: -121 reversed is 121-, which does not match.
    # 
    # 2. Any number ending in 0 (except 0 itself) cannot be a palindrome.
    #    For example: 10 reversed is 01 (which is 1). Since numbers don't start with 0, 
    #    it can never match. But 0 by itself is fine.
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    # --- Step 2: Reverse only the back half of the number ---
    
    # Instead of reversing the whole number, we only reverse the second half.
    # If the first half and the reversed second half are identical, it's a palindrome!
    # This saves time and avoids number overflow.
    reversed_half = 0

    # We keep taking the last digit of x and adding it to reversed_half
    # We stop when reversed_half becomes equal to or bigger than x (that means we hit the middle)
    while x > reversed_half:
        # x % 10 gives us the last digit (for example: 123 % 10 = 3)
        last_digit = x % 10
        
        # Shift the existing reversed number to the left and add the new digit
        reversed_half = reversed_half * 10 + last_digit
        
        # Remove the last digit from x (for example: 123 // 10 = 12)
        x = x // 10

    # --- Step 3: Compare both halves ---
    
    # Case A: Even number of digits (like 1221)
    # When loop finishes: x = 12, reversed_half = 12
    # Both halves match directly: x == reversed_half
    #
    # Case B: Odd number of digits (like 12321)
    # When loop finishes: x = 12, reversed_half = 123
    # The middle digit '3' doesn't matter, so we drop it using reversed_half // 10 (123 // 10 = 12)
    # Then we check if: x == reversed_half // 10
    return x == reversed_half or x == reversed_half // 10


# -------------------------------------------------------------
# Alternative Approach: The easy way using String Conversion
# -------------------------------------------------------------
def isPalindromeString(x: int) -> bool:
    # Convert the number to text so we can read it like a word
    s = str(x)
    
    # s[::-1] flips the text completely backward
    # We just check if the original text equals the reversed text
    return s == s[::-1]


# -------------------------------------------------------------
# Test cases to see it in action
# -------------------------------------------------------------
if __name__ == "__main__":
    print(isPalindrome(121))    # True  (121 reads same both ways)
    print(isPalindrome(-121))   # False (reads as 121-)
    print(isPalindrome(10))     # False (reads as 01)
    print(isPalindrome(0))      # True  (0 reads as 0)
    print(isPalindrome(12321))  # True  (middle 3 stays in place, 12 matches 12)
