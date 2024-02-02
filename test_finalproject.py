# Ziyi Zhang, CSW8 (F21)


from CSW8_finalproject import *



# Test print_main_menu
test_menu = { 1: "Test option", 'b': "Bye!"}
print_main_menu(test_menu)

# Test check_option
my_menu0 = {}
my_menu1 = {'1': "One"}
my_menu2 = {'2': "twe"}
result = check_option(1, my_menu0)
print(f"--> check_option(1, my_menu0) returned `{result}`\n")
assert result == "invalid"

result = check_option(1, my_menu1)
print(f"--> check_option(1, my_menu1) returned `{result}`\n")
assert result == "invalid"

result = check_option('1', my_menu1)
print(f"--> check_option('1', my_menu1) returned `{result}`\n")
assert result == "valid"

result = check_option(2, my_menu2)
print(f"--> check_option(2, my_menu2) returned `{result}`\n")
assert result == "invalid"

result = check_option('2', my_menu2)
print(f"--> check_option('2', my_menu2) returned `{result}`")
assert result == "valid"


# Test list_categories
categories = {}
result = list_categories(categories)
print(f"--> list_categories with no records returned `{result}`")
assert result == 0

categories = {1: ['quiz', 20, [10, 20]]}
result = list_categories(categories)
print(f"--> list_categories with no records returned `{result}`")
assert result == 1

# Test create_id
categories0 = {}
result = create_id(categories0)
print(f"--> create_id with no records returned `{result}`")
assert result == 0

categories1 = {111: "Test"}
result = create_id(categories1)
print(f"--> create_id with max record key 111 returned `{result}`")
assert result == 112

categories2 = {111: "Test", 1000: "Test"}
result = create_id(categories2)
print(f"--> create_id with max record key 1000 returned `{result}`")
assert result == 1001

categories2 = {111: "Test", 1000: "Test"}
offset = 10
result = create_id(categories2, offset)
print(f"--> create_id with max record key 1000 and offset={offset} returned `{result}`")
assert result == 1011

# Test is_numeric
result = is_numeric('123')
print(f"--> is_numeric('123') returned `{result}`")
assert result == True

result = is_numeric('abc')
print(f"--> is_numeric('abc') returned `{result}`")
assert result == False

result = is_numeric('5.5')
print(f"--> is_numeric('5.5') returned `{result}`")
assert result == True

result = is_numeric('5.5.')
print(f"--> is_numeric('5.5.') returned `{result}`")
assert result == False

# Test add_category
categories0 = {}
catID = 1
result = add_category(categories0, catID, 'Quiz 25')
print(f"--> add_category(categories0, {catID}, 'Quiz 25') returned `{result}`")
assert result == catID

print("-->", categories0)
print("-->", categories0[catID])
assert categories0[1] == ["Quiz", 25.0]

categories0 = {}
catID = 1
print("-->", categories0)
result = add_category(categories0, catID, 'Quiz A')
print(f"--> add_category(categories0, {catID}, 'Quiz A') returned `{result}`")
assert result == -1
print("-->", categories0)
assert categories0 == {}

categories0 = {}
catID = create_id(categories0, 1000) # should be 1000
result = add_category(categories0, catID, 'Test 5.5')
print(f"--> add_category(categories0, {catID}, 'Test 5.5') returned `{result}`")
assert result == catID
print("-->", categories0)
print("-->", categories0[catID])
assert categories0[1000] == ["Test", 5.5]

categories0 = {1: ['A', 90]}
catID = create_id(categories0, 1000) # should be 1002
result = add_category(categories0, catID, 'Test 5.5')
print(f"--> add_category(categories0, {catID}, 'Test 5.5') returned `{result}`")
assert result == catID
print("-->", categories0)
print("-->", categories0[catID])
assert categories0[1002] == ["Test", 5.5]

# Test add_category_grades
categories1 = {1111: ["Test", 25]}
result = add_category_grades(categories1, 1111, '100 95')
print(f"--> add_category_grades(categories1, 1111, '100 95') returned `{result}`")
print(f"--> {categories1}\n")
assert result == 2
print(f"--> First inserted score is {categories1[1111][-1][0]}\n")
assert int(categories1[1111][-1][0]) == 100

result = add_category_grades(categories1, 1111, '100 95 80')
print(f"--> add_category_grades(categories1, 1111, '0 95 80') returned `{result}`")
print(f"--> {categories1}\n")
assert result == 3
print(f"--> Last inserted score is {categories1[1111][-1][-1]}\n")
assert int(categories1[1111][-1][-1]) == 80

# test the show_grades_category
cate = {1111: ["Test", 25, [1, 2, 3]]}
result = show_grades_category(cate, 1111)
print(f"--> show_grades_category(cate, 1111) returned `{result}`")
assert result == 3

# test save_data
my_db = {100: ['quiz', 20.0], 201: ['pa', 5.0]}
save_data(my_db)
save_dict_to_csv(my_db, "test_file1.csv")
