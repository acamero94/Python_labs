import math


def route_cipher_encrypt(plain_text, key, direction_flag):
    # Remove spaces from the string
    original_text = plain_text.replace(" ", "")

    # Check length to set number of rows and missing chars
    rows = int(math.ceil(len(original_text) / key))

    # Adding '*' for  missing chars
    missing_letters = (key * rows) - len(original_text)
    if missing_letters > 0:
        for i in range(missing_letters):
            original_text = original_text + '*'

    # Create a table for insert letters
    table = [[""] * key for i in range(rows)]

    # Filling The Table With Text
    index = 0
    for i in range(rows):
        for j in range(key):
            table[i][j] = original_text[index]
            index += 1

    # Start Encryption
    # Initialize default parameters for the route indexes
    current_row = -1
    current_col = key - 1
    # start direction (values "down", "up", "left", "right")
    direction = "down"
    encrypted_text = ""

    # Borders will define the index for leading the direction correctly
    bottom_border = rows - 1
    left_border = 0
    top_border = 0
    right_border = key - 1
    text_length = key * rows

    # From top-right corner clockwise to the center of the table
    if direction_flag:
        for j in range(text_length):

            # Go Down
            if direction == "down":
                current_row += 1  # If the direction is down, add 1 to row index
                # Breaking expression,
                # We set a border that stands for max index we can go downwards and checking if we got there.
                if current_row == bottom_border:
                    direction = "left"  # if we got here it means we need to shift direction because we hit the border.
                    right_border -= 1  # Finished going down we need to "close" the line

                encrypted_text += table[current_row][current_col]

            # Go Left
            elif direction == "left":
                current_col -= 1
                if current_col == left_border:
                    direction = "up"
                    bottom_border -= 1

                encrypted_text += table[current_row][current_col]

            # Go Up
            elif direction == "up":
                current_row -= 1
                if current_row == top_border:
                    direction = "right"
                    left_border += 1

                encrypted_text += table[current_row][current_col]

            # Go Right
            elif direction == "right":
                current_col += 1
                if current_col == right_border:
                    direction = "down"
                    top_border += 1

                encrypted_text += table[current_row][current_col]

        return encrypted_text

    # From top-right corner anticlockwise to the center of the table.
    else:
        direction = "left"
        current_row = 0
        current_col = key
        for j in range(text_length):

            # Go Left
            if direction == "left":
                current_col -= 1
                if current_col == left_border:
                    direction = "down"
                    top_border += 1
                encrypted_text += table[current_row][current_col]

            # Go Down
            elif direction == "down":
                current_row += 1
                if current_row == bottom_border:
                    direction = "right"
                    left_border += 1
                encrypted_text += table[current_row][current_col]

            # Go Right
            elif direction == "right":
                current_col += 1
                if current_col == right_border:
                    direction = "up"
                    bottom_border -= 1
                encrypted_text += table[current_row][current_col]

            # Go Up
            elif direction == "up":
                current_row -= 1
                if current_row == top_border:
                    direction = "left"
                    right_border -= 1
                encrypted_text += table[current_row][current_col]

    return encrypted_text


def route_cipher_decrypt(encrypted_text, key, direction_flag):
    # Building & Filling The Table
    rows = int(math.ceil(len(encrypted_text) / key))
    table = [[""] * key for i in range(rows)]
    # Start Decrypt
    # Initialize default parameters for the route indexes
    current_row = -1
    current_col = key - 1
    direction = "down"
    decrypted_text = ""
    bottom_border = rows - 1
    left_border = 0
    top_border = 0
    right_border = key - 1
    text_length = len(table[0] * rows)

    # From top-right corner clockwise to the center
    if direction_flag:
        for j in range(text_length):
            if direction == "down":
                current_row += 1
                if current_row == bottom_border:
                    direction = "left"
                    right_border -= 1
                # The Only Thing That Is Different Here From The Encryption Is
                # That We Are Building The Table As We Go Through Each Index That
                # The Route Takes Us And Filling In With The Encrypted Text.
                table[current_row][current_col] = encrypted_text[j]

            elif direction == "left":
                current_col -= 1
                if current_col == left_border:
                    direction = "up"
                    bottom_border -= 1
                table[current_row][current_col] = encrypted_text[j]

            elif direction == "up":
                current_row -= 1
                if current_row == top_border:
                    direction = "right"
                    left_border += 1
                table[current_row][current_col] = encrypted_text[j]

            elif direction == "right":
                current_col += 1
                if current_col == right_border:
                    direction = "down"
                    top_border += 1
                table[current_row][current_col] = encrypted_text[j]

        # After Done Filling The Table
        # We Need To Add Each Character To A String
        for line in table:
            for char in line:
                decrypted_text += char
        # Remove X from the return text
        decrypted_text = decrypted_text.strip("*")
        return decrypted_text

    # From top-right corner anticlockwise to the center of the table.
    else:
        direction = "left"
        current_row = 0
        current_col = key
        for j in range(text_length):
            if direction == "left":
                current_col -= 1
                if current_col == left_border:
                    direction = "down"
                    top_border += 1
                table[current_row][current_col] = encrypted_text[j]

            elif direction == "down":
                current_row += 1
                if current_row == bottom_border:
                    direction = "right"
                    left_border += 1
                table[current_row][current_col] = encrypted_text[j]

            elif direction == "right":
                current_col += 1
                if current_col == right_border:
                    direction = "up"
                    bottom_border -= 1
                table[current_row][current_col] = encrypted_text[j]

            elif direction == "up":
                current_row -= 1
                if current_row == top_border:
                    direction = "left"
                    right_border -= 1
                table[current_row][current_col] = encrypted_text[j]

        for line in table:
            for char in line:
                decrypted_text += char

        # Remove * from the return text
        decrypted_text = decrypted_text.strip("*")

        return decrypted_text


text = "this is a secret message"
column_key = 7
clock = True
anti_clock = False
while column_key != 0:
    column_key = int(input("Insert an encryption key between 3-9(for exit press 0):\n"))
    if column_key == 0:
        print("bye bye :)")
        break
    elif column_key < 3 or column_key > 9:
        print("Column key must be between 3-9")
        column_key = int(input("Insert an encryption key between 3-9(for exit press 0) : \n"))
        if column_key == 0:
            break
    if 10 > column_key > 3:
        text = input("Enter a message to encrypt : \n")
        direction_choice = int(input("Choose route encrypt direction:\n 1) Clockwise \n 2) Anti clockwise \n"))
        if direction_choice == 1:
            encrypted_message = route_cipher_encrypt(text, column_key, clock)
            print("The encrypt message: " + encrypted_message)

            original_message = route_cipher_decrypt(encrypted_message, column_key, clock)
            print("The original message: " + original_message)
        else:
            encrypted_message = route_cipher_encrypt(text, column_key, anti_clock)
            print("The encrypt message: " + encrypted_message)

            original_message = route_cipher_decrypt(encrypted_message, column_key, anti_clock)
            print("The original message: " + original_message)