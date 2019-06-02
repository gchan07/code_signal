#step 1: check existing rows/lists for duplicates, if duplicate return false
    #create a dictionary for each row 
    #keys = numbers in existing row, 
    #check to see if the key exists in the dictionary
#step 2: create new lists of the columns and check each of the new lists for duplicates, if there are duplicates, return false
#step 3: create new lists of each subgrid and check each of the subgrids for duplicates


def sudoku2(grid):
    
    #Step 1
    #for each row in sudoku
    for row in range(0, len(grid)):
        row_dict = {}
        for number in range(0, len(grid[0])):
            if grid[row][number] != ".":
                if grid[row][number] in row_dict:
                    return False
                else: 
                    row_dict[(grid[row][number])] = 1
        #print(row_dict)
            
    #Step 2 
    if not check_columns(grid):
        return False

    #Step 3 
    # for each subgrid in sudoku
    # 

def check_columns(grid):
    #for each column in sudoku
    for row in range (0, len(grid)):
        column_list =[]
        for number in range(0, len(grid[0])):
            column_list.append(grid[number][row])
        #print(column_list)
        column_dict = {}
        for blah in range(0,len(column_list)): 
            if column_list[blah] != ".":
                if column_list[blah] in column_dict:
                    return False
                else:
                    column_dict[column_list[blah]] = 1
        print(column_dict)
    return True