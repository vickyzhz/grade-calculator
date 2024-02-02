# Ziyi Zhang


# the function for user to start this system
def print_main_menu(the_menu):
    """
    takes as input a dictionary menu
    and prints the options from the dictionary
    line by line
    """
    print('**************************')
    print('What would you like to do?')
    for i , j in the_menu.items():
        print(f'{i} - {j}')
    print('**************************')

    
   
# the check option function to check
# whether a provided option is a valid menu option
def check_option(option, menu):
    """
    Returns "invalid" if the provided `option`
    is not one of the keys in the given `menu`.
    Returns "valid" otherwise.
    """
    if type(option) == str:
        if option not in menu:
            if option.isdigit() == True:
                print(f'WARNING: `{option}` is an invalid option.')
                print('Please enter a valid option.')
            else: 
                print(f'WARNING: `{option}` is not an integer.')
                print('Please enter an integer.')
            return "invalid"
        else:
            return "valid"
    else:
        if option not in menu:
            print(f'WARNING: {option} is an invalid option.')
            print('Please enter a valid option.')
            return "invalid"
        else:
            return "valid"



# option 1: Display a collection of categories

# the function that will display category
def list_categories(dic, showID = False):
    """
    The function takes two arguments: a dictionary
    and a Boolean flag that indicates whether to
    display the category IDs.
    The first argument is a dictionary, that stores a
    numeric ID as a key for each category;
    the corresponding value for the key is
    a list that contains a category item
    with 3 elements arranged as follows: 
    * `'name'` - the name of the category,
    * `'percentage'` - the percentage of the total grade,
    * `'grades'` - a list of numeric grades.

    By default, displays the dictionary values as
    CATEGORY NAME : PERCENTAGE%
    If showID is True, the values are displayed as
    ID - CATEGORY NAME : PERCENTAGE%
    If a dictionary is empty, prints "There are no categories."
    If a dictionary has a single category,
    prints "There is only 1 category:"
    Otherwise, prints "There are X categories:"
    where X is the number of records in the dictionary.
    Returns the number of records.
    """
    if len(dic) == 0:
        print('There are no categories.')
    elif len(dic) == 1:
        print('There is only 1 category:')
    else:
        print(f'There are {len(dic)} categories:')
    if showID == False:
        for i , j in dic.items(): # for each key and value in dictionary
            print(f'{j[0].upper()} : {j[1]}%')
    if showID == True:
        for i , j in dic.items():
            print(f'{i} - {j[0].upper()} : {j[1]}%')
    return len(dic)
        


# Option 2: Add a category

# step 1 - Create a category ID
# function that create an ID for a category
def create_id(db, offset = 0):
    """
    Return an integer ID that would be generated 
    for the next value inserted into the `db`.
    """
    if len(db) == 0:
        id = 0 + int(offset)
    if len(db) > 0:
        id = max(db.keys()) + 1 + int(offset) # id = maximun key + 1 + offset
    return id


# step 2 - Add a single category
# helper function that checks the provided string
def is_numeric(val):
    """
    Returns True if the string `val`
    contains a valid integer or a float.
    """
    if '.' in val:
        if val.count('.') == 1: # if there is only one '.'
            if val.replace('.','').isdigit() == True: 
                return True
        if val.count('.') > 1:
            return False
    else:
        if val.isdigit() == True:
            return True
        else:
            return False
    


# functiont that add a single category
def add_category(db, cid, info_str):
    """
    Inserts into the `db` collection (dictionary)
    `cid` - the integer category ID (the key), and its
    corresponding value, which is a list obtained from the
    `info_str` that contains two elements: the category name 
    and the corresponding percentage of the total grade.
    If the list does not contain two elements, returns -2.
    Calls is_numeric():
    If the last input value (the percentage) in `info_str`
    is not numeric (int or float), does not update the
    dictionary and returns -1 instead.
    Otherwise, returns the integer ID of the category.
    Stores the percentage as a float (not as a string).
    """
    info_list = info_str.split()
    if len(info_list) != 2:
        return -2
    if len(info_list) == 2:
        if is_numeric(info_list[-1]) == False:
            return -1
        else:
            db[int(cid)] = [info_list[0], float(info_list[1])]
            # store percentage as float
            return int(cid)



# step 3 - Interact with the user to add categories
# function that collect the necessary information and add categories
def add_categories(db, max_num, id_offset):
    """
    Prompts the user to enter a single-word category name
    and the corresponding percentage of the total grade.
    Calls `create_id()` to get the ID for the category.
    Calls `add_category()`, and keeps asking the user to
    input the correct value for that category, if
    its percentage is not a number (int or float).
    """
    print(f"You can add up to {max_num} categories.")
    print("::: How many categories will you add?")
    num_cate = input("> ")
    if num_cate.isdigit() == False: # if num_cate is not numeric
        while num_cate.isdigit() == False:
            print(f'`WARNING: {num_cate}` is not a valid integer.')
            print('::: Enter a valid number of categories you plan to add')
            num_cate = input("> ")
            
        if (int(num_cate) + len(db)) > int(max_num): # if the total number exceed max number
            print(f'WARNING: Adding {num_cate} categories would exceed the allowable max.')
            print(f'You can store up to {max_num} categories.')
            print(f'Current total of categories is {len(db)}.')
          
    else: # if num_cate is numeric
        if (int(num_cate) + len(db)) > int(max_num):
            print(f'WARNING: Adding {num_cate} categories would exceed the allowable max.')
            print(f'You can store up to {max_num} categories.')
            print(f'Current total of categories is {len(db)}.')
        
    if num_cate.isdigit() == True and (int(num_cate) + len(db)) <= int(max_num):
        i = 1
        while i <= int(num_cate):
            print(f'::: Enter the category {i} name (no spaces) followed by its percentage')
            cate_info = input("> ")
            if len(cate_info.split()) != 2:
                while len(cate_info.split()) != 2:
                    print('WARNING: invalid input for the name and percentage.')
                    print(f'::: Enter the category {i} name (no spaces) followed by its percentage')
                    print('::: or enter M to return back to the menu.')
                    cate_info = input("> ")
                    if (cate_info == 'M') or (cate_info == 'm'):
                        return None # end the while loop
                
            if len(cate_info.split()) == 2 and cate_info.split()[-1].isdigit() == False:
                while cate_info.split()[-1].isdigit() == False:
                    print('WARNING: invalid input for the name and percentage.')
                    print(f'::: Enter the category {i} name (no spaces) followed by its percentage')
                    print('::: or enter M to return back to the menu.')
                    cate_info = input("> ")
                    if (cate_info == 'M') or (cate_info == 'm'):
                        return None # end the while loop
                    
            if len(cate_info.split()) == 2 and cate_info.split()[-1].isdigit() == True:     
                new_id = create_id(db, id_offset)
                check = add_category(db, new_id, cate_info)
                if check == -2 or check == -1:
                    continue
                else:
                    i=i+1

     
        

    
# option 3: Update a category     
def update_category(db):
    """
    Prompts the user to enter the category ID
    and then asks to enter the updated information:
    name and the corresponding percentage of the total grade.
    Calls list_categories() at the beginning of the function,
    and add_category() to update the info.
    """
    print('Below is the info for the current categories.')
    list_categories(db, True)
    if len(db) > 0:
        print('::: Enter the category ID that you want to update')
        update_id = input('> ')
        while int(update_id) not in db:
            print(f'WARNING: `{update_id}` is not an ID of an existing category.')
            print('::: Enter the ID of the category you want to update')
            print('::: or enter M to return back to the menu.')
            update_id = input('> ')
            if update_id == 'M' or update_id == 'm':
                break # if user enter M, break out of the while loop
        
        if update_id.isdigit() == True:
            print(f'Found a category with ID `{update_id}`:')
            print('::: Enter the updated info:')
            print('    category name followed by the percentage.')

            update_info = input('> ')
            if add_category(db, update_id, update_info) == -2:
                print('WARNING: insufficient information for the update. ')
                print(f'Record with ID `{update_id}` was not updated!')

            elif add_category(db, update_id, update_info) == -1:
                print('WARNING: invalid input for the name and/or percentage. ')
                print(f'Record with ID `{update_id}` was not updated!')
            else:
                add_category(db, update_id, update_info)
            
        
# option 4: Delete a category 
def delete_category(db):
    """
    Calls list_categories() at the beginning of the function.
    Prompts the user to enter the category ID
    and then verifies the information and selection by printing 
    that record from the `db`.
    Deletes the category and its info, once the user confirms.
    """
    print('Below is the info for the current categories.')
    list_categories(db, True)
    if len(db) >0:
        print('::: Enter the category ID that you want to delete')
        delete_id = input('> ')
        while int(delete_id) not in db:
            print(f'WARNING: `{delete_id}` is not an ID of an existing category.')
            print('::: Enter the ID of the category you want to delete')
            print('::: or enter M to return back to the menu.')
            delete_id = input('> ')
            if delete_id == 'm' or delete_id == 'M':
                break # if user enter M, break out of the while loop

        if delete_id.isdigit() == True:
            print(f'Found a category with ID `{delete_id}`:')
            print(db[int(delete_id)])
            print('::: Are you sure? Type Y or N')
            yes_no = input('> ')
            if yes_no == 'Y':
                del db[int(delete_id)] # delete the category
                print('Deleted')
            else:
                print("Looks like you aren't 100% sure.\nCancelling the deletion.")
            
      
        
# Option 5: Add grades
def add_grades(db):
    """
    Calls list_categories() at the beginning of the function.
    Prompts the user to enter the category ID
    and then asks to enter the grades for that category. 
    Convert the grades string to the list of float values.
    Calls add_category_grades() to insert the record.
    Does not add the grades if not all provided grades
    contain numeric scores.
    """
    print('Below is the info for the current categories.')
    list_categories(db, True)
    if len(db) > 0: # when there is category in the dictionary
        print('::: Enter the category ID for which you want to add grades')
        addgrade_id = input('> ')
        while int(addgrade_id) not in db: # when the input id does not exist
            print(f'`{addgrade_id}` is not an ID of an existing category.')
            print('::: Enter the ID of the category to add grades to')
            print('::: or enter M to return back to the menu.')
            addgrade_id = input('> ')
            if addgrade_id == 'm' or addgrade_id == 'M':
                break
        if addgrade_id.isdigit() == True:
            int_id = int(addgrade_id)
            print(f'You selected a {db[int_id][0].upper()} category.')
            print('::: Enter space-separated grades')
            print('::: or enter M to return back to the menu.')
            grades_str = input('> ')
            if grades_str != 'm' and grades_str != 'M':
                grades_list = grades_str.split()
                count_n_numeric = 0
                for i in grades_list:
                    a = is_numeric(i)
                    if a == False:
                        count_n_numeric += 1
                if count_n_numeric > 0: # when there is non-numeric value
                    print('Do not add the grades. Not all provided grades contain numeric scores')
                else: # when all the grades are numeric value
                    if len(db[int_id]) == 2:
                        add_category_grades(db, int_id, grades_str)
                        print(f'Success! Grades for the {db[int_id][0].upper()} category were added.')
                    else:
                        add_category_grades(db, int_id, grades_str)
                        print(f'Success! Grades for the {db[int_id][0].upper()} category were updated.')


def add_category_grades(db, cid, grades_str):
    """
    Inserts into the `db` collection (a dictionary)
    a list of grades for the provided category ID.
    The list is obtained from the grades_str.
    Calls is_numeric() to check each grade in 
    grades_str: if all provided grades were not numeric, 
    does not update the dictionary and returns -1.
    Stores the grades as a list of floats (not as strings).
    Calls show_grades_category() if the user adds grades to a category
    that already has grades added to it. 
    If a category with the provided ID already has grades
    in it, then the new grades are appended to the existing
    grades and updated information is displayed.
    Returns the number of grades that were added.
    """
    grades_list = grades_str.split()
    count_n_numeric = 0
    for i in grades_list:
        a = is_numeric(i)
        if a == False:
            count_n_numeric += 1
    if count_n_numeric > 0: # when there is non-numeric value
        return -1
    else: # when all the grades are numeric value
        grades_list_f = [float(i) for i in grades_list]
        if len(db[cid]) < 3:
            db[cid].append(grades_list_f)
            return len(grades_list_f)
        if len(db[cid]) == 3:
            show_grades_category(db,cid)
            for i in grades_list_f:
                db[cid][2].append(i)
            show_grades_category(db,cid)
            return len(grades_list_f)                
    

def show_grades_category(db, cid):
    print(db[cid][0].upper(), 'grades',db[cid][2])


    
    
#Option 6: Show grades
def show_grades(db):
    """
    Calls list_categories() at the beginning of the function.
    If the dictionary is empty, return from the function.
    Otherwise, prompts the user to enter the category ID or 
    enter "A" to show grades of all categories that store them
    If the provided ID is not valid, prompt the user to enter 
    a valid ID or go back to the menu using ‘M’ or ‘m’ as input.
    Calls show_grades_category() with appropriate arguments 
    to show the grades.
    """
    print('Below is the info for the current categories.')
    list_categories(db, True)
    if len(db) > 0:
        print('::: Enter the category ID for which you want to see the grades')
        print('::: or enter A to list all of them.')
        see_id = input('> ')
        if see_id == 'A':
            for i in db: # check each id in the dictionary
                if len(db[i]) == 3: #show grades if there is existing grades
                    show_grades_category(db, i)
        else:
            while int(see_id) not in db:
                print(f'WARNING: `{see_id}` is not an ID of an existing category.')
                print('::: Enter a valid category ID to see the grades')
                print('::: or enter M to return back to the menu.')
                see_id = input('> ')
                if see_id == 'm' or see_id == 'M':
                    break
            if see_id.isdigit() == True:
                show_grades_category(db, int(see_id))
                    
        


def show_grades_category(db, cid):
    """
    Displays the grades the user added into the db collection (dictionary), 
    for the provided category ID `cid`.
    If there are no grades, display "No grades were provided for category ID `cid`."
    and return 0.
    Otherwise, print the capitalized category name followed by a word "grades",
    and then a list of grades. Print the grades list without any beautification. 
    Return the number of grades in the grades list.
    """
    if len(db[cid]) < 3:
        print(f'No grades were provided for category ID `{cid}`.')
        return 0
    else:
        int_grades_list = [float(i) for i in db[cid][2]]
        print(db[cid][0].upper(), 'grades',int_grades_list)
        return len(int_grades_list)


    

# Option 7: Grade statistics

def sum_percentages(db):
    """
    Given a collection (dictionary),
    where each value is a list whose
    second element is a percentage of
    a category, returns the sum of the
    percentages.
    """
    sum_percent = 0
    for i in db:
        sum_percent = sum_percent + db[i][1]
    return sum_percent



def get_avg_grade(grade_list):
    """
    Given a list of grades,
    returns the average value of the
    grades. Returns 0 if the list is
    empty.
    """
    if len(grade_list) == 0:
        return 0
    else:
        grade_avg = sum(grade_list)/len(grade_list)
        return grade_avg



def grade_stats(db):
    """
    Calls list_categories() at the beginning of the function.
    Calls show_grades_category() to display the grades.
    Calls sum_percentages() to get the total percentages;
    shows a warning if they do not add up to 100.
    Calls get_avg_grade() to compute the average score for
    each category.
    Returns the computed course grade or, if there are no
    categories, returns 0.
    """
    print('Below is the info for the current categories.')
    list_categories(db)
    if len(db) > 0: 
        print() # a new line
        print('Provided grades:')
        for i in db:
            if len(db[i]) > 3:
               show_grades_category(db, i)
        print()
        if sum_percentages(db) != 100:
            print("WARNING: Category percentages don't add up to 100.")
            print(f'Current category percentages comprise {sum_percentages(db)} of the total.')
            print()
        print('Grade calculation:')
        total = 0 # the total grade
        for i, j in db.items():
            result = j[1] / 100 * get_avg_grade(j[2]) # grade of each category
            percent = j[1] / 100 # change percent into a float
            print("{} = {:.2f} * {:.2f} = {:.2f}".format(j[0].upper(),
                                                         get_avg_grade(j[2]),
                                                         percent,
                                                         result))
            total = total + result 
        print('Total grade = {:.2f}'.format(total))
        return total
    else:
        return 0
        

# Option 8: Save the data

def save_data(db):
    """
    Calls list_categories() at the beginning of the function.
    If there are no categories, notify the user and return 0.
    By default, save the `db` to a CSV file.
    Asks the user whether to read from the default filename
    or ask for the filename to open.
    Calls save_dict_to_csv() to create the file.
    """
    print('Below is the info for the current categories.')
    list_categories(db, True)
    if len(db) == 0:
        print('Skipping the creation of an empty file.')
        return 0
    else:
        print('::: Save to the default file (grade_data.csv)? Type Y or N')
        w_save = input('> ')
        if w_save == 'Y':
            print('Saving the database in grade_data.csv')
            print('Database contents:')
            print(db)
            save_dict_to_csv(db, 'grade_data.csv')
        if w_save == 'N':
            print('::: Enter the name of the csv file to open.')  # ask user to input te filename 
            filename = input('> ')
            print(f'Saving the database in {filename}')
            print('Database contents:')
            print(db)
            save_dict_to_csv(db, filename)
            
            


def save_dict_to_csv(db, filename):
    """
    Given the dictionary db,unwrap the key and value of db.
    Store id, category, percentage as float, and every grades as float
    without square brackets into the cvs file given the filename.
    """
    import csv
    rows=[] # create a list to store each row
    for i in db:
        row=[i,db[i][0],db[i][1]]
        if len(db[i]) == 3:
            for j in db[i][2]:
                row.append(j)
        rows.append(row)
    with open(filename, 'w', newline='') as csvfile:
        a=csv.writer(csvfile)
        a.writerows(rows)







# Option 9: Upload data from file
def load_dict_from_csv(filename):
    """
    Given a string containing the filename,
    Opens the file and stores its contents
    into the dictionary, which is returned
    from this function.
    The function assumes that the first element
    on each row will be an integer ID, stored
    as a key in the dictionary, and the values
    that are on the rest of the line are stored
    in a list as follows:
    [row[1], float(row[2]), [float(i) for i in row[3:]]]
    The function returns an empty dictionary
    if the CSV file is empty.
    """
    import csv
    dic={} # create a dictionary to store the file's content
    with open(filename, 'r') as csvfile:
        a=csv.reader(csvfile, delimiter=',')
        for i in a:
            if len(i) > 3:
                grades=[]
                for j in i[3:]:
                    grades.append(float(j)) # grades should be float
                dic[int(i[0])]=[i[1],float(i[2]),grades]
            else:
                dic[int(i[0])]=[i[1],float(i[2]),[]]
    return dic



def load_data(db):
    """
    ask for user to input the filename
    read data from the filename to the db dictionary
    if the user choose the default filename name,
    read data from default filename "grade_data.csv"
    if the user choose to input a filename,
    ask for the new filename.
    Check whether new filename correctly ends with '.csv.'
    if not, ask for the inout again>
    If so, check whether the file exists.
    Read the data from the filename using load_dict_from_csv()
    and store it db, if the file exists.
    Otherwise, print the warning message.
    """
    import csv
    import os
    filename = "grade_data.csv"
    print(f"::: Load the default file ({filename})? Type Y or N")
    w_load = input('> ')
    if w_load == 'Y':
        print(f'Reading the database from {filename}')
        new_db = load_dict_from_csv(filename)
        print("Resulting database:\n", new_db)
        db.update(new_db)
    if w_load == 'N':
        print('::: Enter the name of the csv file to load.')
        new_filename = input('> ')
        while new_filename[-4:] != '.csv':
            print('WARNING: data.txt does not end with `.csv`')
            print('::: Enter the name of an existing csv file.')
            new_filename = input('> ')
        if os.path.isfile(new_filename) == False:
            print(f"WARNING: Cannot find a CSV file named '{new_filename}'")
        else:
            print(f'Reading the database from {new_filename}')
            new_db = load_dict_from_csv(new_filename)
            print("Resulting database:\n", new_db)
            db.update(new_db)







# the main program
if __name__ == "__main__":
    # the dictionary contains options of the main menu
    the_menu = {'1': 'List categories',
                '2': 'Add a category',
                '3': 'Update a category',
                '4': 'Delete a category',
                '5': 'Add grades',
                '6': 'Show grades',
                '7': 'Grade statistics',
                '8': 'Save the data',
                '9': 'Upload data from file',
                'Q': 'Quit this program'}
    main_db = {} # stores the grading categories and info
    max_cat = 10 # the max total num of categories a user can provide
    cat_id_offset = 100 # the starting value for the category ID 

    opt = None

    while True:
        # print the menu
        print_main_menu(the_menu)
        print("::: Enter an option")
        opt = input("> ")

        if opt == 'Q' or opt == 'q':
            print("Goodbye")
            break # exit the main `while` loop
        else:
            if check_option(opt, the_menu) == "invalid":
                continue
            print("You selected option {} to > {}.".format(opt, the_menu[opt]))

        if opt == '1': 
            list_categories(main_db)

        elif opt == '2':
            add_categories(main_db, max_cat, cat_id_offset)

        elif opt == '3':
            update_category(main_db)

        elif opt == '4':
            delete_category(main_db)

        elif opt == '5':
            add_grades(main_db)

        elif opt == '6':
            show_grades(main_db)

        elif opt == '7':
            grade_stats(main_db)

        elif opt == '8':
            save_data(main_db)

        elif opt == '9':
            load_data(main_db)

        elif opt == 'Q' or opt == 'q':
            print('Goodbye!')
            break

        else:
            print("This option is not yet implemented.")
            
        opt = input("::: Press Enter to continue...")

    print("See you next time!")
    
