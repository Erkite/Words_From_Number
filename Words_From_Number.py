# Words From Number
# Peyton Wall
# 2024-09-24

def wordsFromNumber(number):
    """
    >>> wordsFromNumber(0)
    'zero'
    >>> wordsFromNumber(19)
    'nineteen'
    >>> wordsFromNumber(909)
    'nine hundred nine'
    >>> wordsFromNumber(2005)
    'two thousand five'
    >>> wordsFromNumber(92373)
    'ninety-two thousand three hundred seventy-three'
    >>> wordsFromNumber(1111111111111)
    'one trillion one hundred eleven billion one hundred eleven million one hundred eleven thousand one hundred eleven'
    """
    largeNums_index = 0 # The index for largeNums
    largeNums = ["", "thousand", "million", "billion", "trillion", "quadrillion", "quintillion"] # I'm adding words at the end of large numbers
    finalResult = [] # Ending result that gets returned
    
    if number == 0:
        return 'zero'
    
    while number > 0 and largeNums_index < len(largeNums):
        n = number % 1000
        if n > 0:
            if n < 20: # 0s and teens
                part = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
                "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
                "nineteen"][n]
            
            elif n < 100: # tens and their spare numbers
                part = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty",
                "ninety"][n // 10] + ("-" + ["", "one", "two", "three", 
                "four", "five", "six", "seven", "eight", "nine"][n % 10] if n % 10 != 0 else "")
            
            else: # this deals with 100 - 999
                part = ["", "one", "two", "three", "four", "five", "six", "seven", "eight",
                "nine"][n // 100] + " hundred" + (" " + ["", "one", "two", "three", "four", "five", "six",
                "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
                "sixteen", "seventeen", "eighteen", "nineteen"][n % 100] if n % 100 < 20
                else " " + ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty",
                "ninety"][(n % 100) // 10] + ("-" + ["", "one", "two", "three", "four", "five", "six",
                "seven", "eight", "nine"][n % 10] if n % 10 != 0 else ""))
            
            finalResult.append(part + (" " + largeNums[largeNums_index] if largeNums[largeNums_index] else ""))
        number //= 1000
        largeNums_index += 1
    
    return " ".join(reversed(finalResult)).replace("  ", " ").strip() # This fixed the double spaces that kept failing me

if __name__ == "__main__":
    import doctest
    doctest.testmod()