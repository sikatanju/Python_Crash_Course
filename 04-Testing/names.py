from name_function import get_formatted_name

print("Enter 'q' to quit any time.")

while True:
    first = input("Enter your first name: ")
    if first == 'q':
        break

    second = input("Enter your second name: ")
    if second == 'q':
        break

    print(f"Neatly formatted name : {get_formatted_name(first, second)}")
    print("\nEnter 'q' to quit.\n")