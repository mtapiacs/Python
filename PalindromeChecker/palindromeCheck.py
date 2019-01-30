def palindromeCheck(phr):                                   # Function takes in a phr
    phr = phr.replace(" ", "")                              # Spaces are removed
    return phr == phr[::-1]                                 # Checks if the removed space string is equal to the phrase backwards

user_input = input("Choose a word: ")

#phrToTest = ["nurses run", "abcba", "not palindrome", "abcabafafead"]
print("The program is checking if \"{}\" is a palindrome! It is {}".format(user_input, palindromeCheck(user_input.lower())))