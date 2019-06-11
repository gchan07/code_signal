#convert solution to a dictionary, solution_dict = {} 
#create a new list with decrypted letters, decrypt_list = []
#loop through each word, loop through each letter 
#return solution_dict value if letter in solution_dict 
#convert strings to int
#first check to see if the 0 index  = 0, return false 
#Else index into new list and check mathematical accuracy 

def isCryptSolution(crypt, solution):

    solution_dict = dict((x,y) for x,y in solution)
    decrypt_lists =[]
    for word in crypt:
        decrypt_list = []
        for letter in word:
            decrypt_list.append(solution_dict[letter])
        decrypt_lists.append(decrypt_list)
    single_int = []
    for number in decrypt_lists:
        if len(number) > 1 and number[0] == '0':
            return False
        single_int.append(int("".join(number)))
    print(single_int)
    if single_int[0] + single_int[1] == single_int[2]:
        return True 
    return False
        
         