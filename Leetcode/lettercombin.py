def letterCombinations(digits: str) -> list[str]:
    """
    Given a string of digits from '2' to '9', returns all possible 
    letter combinations that the number could represent on a phone keypad.
    
    Example:
      Input: digits = "23"
      Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    """

    # --- Step 1: Handle edge case ---
    # If the input is empty (e.g., ""), there are no combinations to make,
    # so we immediately return an empty list [].
    if not digits:
        return []

    # --- Step 2: Phone keypad dictionary ---
    # Just like an old telephone keypad, map each digit (2 to 9) to its letters.
    # Note: 1 does not map to any letters.
    phone_map = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    result = []

    # --- Step 3: Backtracking (Exploration) ---
    # Think of this like making choices step by step:
    # - index: which digit we are currently looking at (0th digit, 1st digit, etc.)
    # - current_combination: the letters we have chosen so far
    def backtrack(index: int, current_combination: str):
        # Base condition:
        # If our combination has the same length as the input digits,
        # it means we have picked a letter for every digit! We save it.
        if len(current_combination) == len(digits):
            result.append(current_combination)
            return  # Go back and try other choices

        # Get the letters mapped to the current digit
        # For example, if current digit is '2', letters will be 'abc'
        current_digit = digits[index]
        letters = phone_map[current_digit]

        # Try picking each letter one by one
        for letter in letters:
            # Add the letter to current combination and move to the next digit (index + 1)
            backtrack(index + 1, current_combination + letter)

    # Start the backtracking from index 0 with an empty combination ""
    backtrack(0, "")
    
    return result


# -------------------------------------------------------------
# Alternative Approach: Iterative (Breadth-First / List building)
# -------------------------------------------------------------
def letterCombinationsIterative(digits: str) -> list[str]:
    """
    Builds combinations by expanding the list digit by digit.
    Start with [""]
    After '2': ["a", "b", "c"]
    After '3': ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    """
    if not digits:
        return []

    phone_map = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
    }

    # Start with a list containing one empty string
    combinations = [""]

    for digit in digits:
        new_combinations = []
        # For every string built so far, attach each letter of the new digit
        for prev in combinations:
            for letter in phone_map[digit]:
                new_combinations.append(prev + letter)
        combinations = new_combinations

    return combinations


# -------------------------------------------------------------
# Test cases to see it in action
# -------------------------------------------------------------
if __name__ == "__main__":
    # Example 1:
    print("Digits '23':", letterCombinations("23"))
    # Output: ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

    # Example 2:
    print("Digits '2':", letterCombinations("2"))
    # Output: ['a', 'b', 'c']

    # Example 3 (Empty input):
    print("Digits '':", letterCombinations(""))
    # Output: []
