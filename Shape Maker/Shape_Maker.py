
# CALL FUNCTIONS IN MAIN
def main():
    ascii_art()
    display_rectangle()
    display_triangle()
    display_pyramid()

# ***** RECTANGLE *****
def display_rectangle():
    # GET USER INPUT FOR RECTANGLE HEIGHT
    rectangle_height = int(input("Please input a value for the height of the RECTANGLE (1-10): "))
    print()

    # SOFT-VALIDATE (no letter checking)
    while rectangle_height < 1 or rectangle_height > 10:
        rectangle_height = int(input("ERROR, you need to input a value of 1 through 10. Try again: "))

    # PRINT RECTANGLE WITH NESTED for LOOP
    for y in range(rectangle_height):
        for x in range(16):
            print("*", end="")
        print()

         # CONFIRM AND DISPLAY SIZE 
    print("\nYour rectangle was {} tall and {} wide!".format(rectangle_height, x))
         
# ***** TRIANGLE *****
def display_triangle():
    # GET USER INPUT FOR TRIANGLE ROWS
    triangle_rows = int(input("Please input a value for the rows of the TRIANGLE (1-10): "))
    print()
    
    # SOFT-VALIDATE
    while triangle_rows < 1 or triangle_rows > 10:
        triangle_rows = int(input("ERROR, you need to input a value of 1 through 10. Try again: "))
    
    # PRINT TRIANGLE WITH NESTED while LOOPS
    y = 1  # INITALIZE ROW COUNTER
    while y <= triangle_rows:
        x = 1  # INITIALIZE COLUMN COUNTER
        while x <= y:
            print("*", end="")
            x += 1  # INCREMENT COLUMN BY ONE
        print()  
        y += 1  # INCREMENT ROW BY ONE
    
    # CONFIRM AND DISPLAY SIZE
    print("\nYour triangle had {} rows!".format(triangle_rows))

# ***** PYRAMID *****
def display_pyramid():
    # GET USER INPUT FOR LEVEL OF PYRAMID
    pyramid_height = int(input("Please input a value for the level of the PYRAMID (1-10): "))
    print()
    
    # SOFT-VALIDATE
    while pyramid_height < 1 or pyramid_height > 10:
        pyramid_height = int(input("ERROR, you need to input a value of 1 through 10. Try again: "))
    
    # PRINT PYRAMID
    for level in range(1, pyramid_height + 1):
        # PRINT SPACES
        print(" " * (pyramid_height - level), end="")
        # PRINT STARS 
        print("*" * (2 * level - 1))  

    # CONFIRM AND DISPLAY SIZE 
    print("\nYour pyramid had {} rows and had a base of {}!"\
          .format(pyramid_height, 2 * pyramid_height - 1))


# ***** ASCII ART *****
def ascii_art():
    print(r"""
        .----..-. .-.  .--.  .----. .----. .----.
       { {__  | {_} | / {} \ | {}  }| {_  { {__  
       .-._} }| { } |/  /\  \| .--' | {__ .-._} } 
       `----' `-' `-'`-'  `-'`-'    `----'`----'  
    """)

# EXECUTE CODE
main()                         
# CLOSING CONFIRMATION
input("Press any key to exit") 
