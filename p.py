def calculate_perimeter_of_rectangle(width, length):
    p = (width + length) * 2
    return p

width = input("Enter the width of the rectangle: ")
length = input("Enter the length of the rectangle: ")
if(not (width.isnumeric()) and not(length.isnumeric())):
    print("Width and length have to be number. Program stopped.")
else:
    #convert width and length to integer
    width = int(width)
    length = int(length)

    #check if width or length is 0
    if(width == 0 or length == 0):
        print("Width and length cannot be 0. Program stopped")
    elif(width < 0 or length < 0):
        print("Width and length have to be positive number. Program stopped")
    else:
        p = calculate_perimeter_of_rectangle(width, length)
        print("Perimeter of the rectangle is " + str(p))
