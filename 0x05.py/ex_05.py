
largest = None
smallest = None

while True:
    num_input = input("Enter a number or 'done' to finish: ")
    
    if num_input == 'done':
        break

    try:
        num = int(num_input)
        if largest is None or num > largest:
            largest = num
        if smallest is None or num < smallest:
            smallest = num
    except ValueError:
        print("Invalid input.")

if largest is not None and smallest is not None:
    print("Maximum is", largest)
    print("Minimum is", smallest)
else:
    print("No valid numbers were entered.")


