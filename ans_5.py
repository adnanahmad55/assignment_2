#In Python, lists are mutable, which means if you modify a list inside a function, 
# the changes will reflect outside the function as well.

def modify_list(lst):
    lst.append("new item")  # Append a new item to the list
    print("Inside function:", lst)  # Print the list inside the function

# Define a list
my_list = [1, 2, 3]

# Call the function and modify the list
modify_list(my_list)

# Check the list outside the function
print("Outside function:", my_list)
