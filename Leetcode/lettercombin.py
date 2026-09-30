def letterCombinations(digits: str):
    # if empty digits, return empty list
    if digits == "":
        return []

    # mobail keypad mapping
    phone = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    # start with one empty string so we can add letters to it
    ans = [""]

    # loop to take each digit one by one from digits
    for d in digits:
        # taking letters for this dgit from phone map (ex: for '2' it takes 'abc')
        letters = phone[d]
        
        # temp list to store new words for this step
        temp = []
        
        # loop to take previous word from ans
        for word in ans:
            # loop to take each letter from letters
            for ch in letters:
                # join old word and new letter together and put in temp
                temp.append(word + ch)
                
        # update ans with temp list for next digit
        ans = temp

    return ans
