def iterate(lst):
    for i in range(len(lst)):
        if lst[i] % 3 !=0:
            continue
        else:
            print(lst[i])
             

def demonstrate_continue():
    print("Demonstrating continue statement:")
    for num in range(1, 11):  # Loop from 1 to 10
        if num % 2 == 0:
            continue  # Skip even numbers
        print(num)  # Print only odd numbers


demonstrate_continue()
lst=[1,2,3,4,5,6,7,8,9]
print("next ")
iterate(lst)