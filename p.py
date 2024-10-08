def calculate_perimeter_of_rectangle(width, length):
    if not (str(width).isnumeric() and str(length).isnumeric()):
        print("Width and length have to be numbers. Program stopped.")
        return None

    width = int(width)
    length = int(length)

    # Check if width or length is 0
    if width == 0 or length == 0:
        print("Width and length cannot be 0. Program stopped")
        return None
    elif width < 0 or length < 0:
        print("Width and length have to be positive numbers. Program stopped")
        return None
    else:
        p = (width + length) * 2  # Calculate perimeter
        return p

if _name_ == "_main_":
    example_width_and_length = (5, 10)  # Example width and length
    width, length = example_width_and_length
    perimeter = calculate_perimeter_of_rectangle(width, length)

    if perimeter is not None:  # Check if the result is valid
        print("Perimeter of the rectangle is " + str(perimeter))
