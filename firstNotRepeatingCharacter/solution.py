#create a dictionary. keys represent characters in string. values represent number of occurrences of key
#It must go through the whole string to count all characters
#    if we see a new key, add it to dict with value of 1
#    if we see a key we have already seen, increment its value
#    
#Now we have a dictionary in the form { letter : count }
#
#Iterate through the string s again
#    if fnr_dict[letter] == 1:
#       return letter
#return '_'   
#    
#

def firstNotRepeatingCharacter(s):

    fnr_dict = {}
    
    for letter_index in range(0,len(s)):
        if s[letter_index] in fnr_dict:
            # If this key is in the dict, increment its value
            fnr_dict[s[letter_index]] += 1
        else:
            # If this key is not in the dict, add it with value of 1
            fnr_dict[s[letter_index]] = 1   
    

    for letter_index in range (0,len(s)):  
        if fnr_dict[s[letter_index]] < 2:
            return s[letter_index]
    
    return'_'
    