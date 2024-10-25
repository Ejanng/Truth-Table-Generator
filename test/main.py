import os  # Import the os module
import sys  # Import the sys module

from calculator import Calculator
calc = Calculator()
from stack import Stack
stack = Stack()


def remove_duplicates(array):
        seen = set()  # Initialize an empty set to keep track of seen items
        result = []  # List to store unique items

        # Iterate over each item in the array
        for item in array:
            if item not in seen:  # If the item hasn't been encountered yet
                result.append(item)  # Add it to the result list
                seen.add(item)  # Mark the item as seen by adding it to the set

        return result  # Return the list of unique items


def translate(string_equation):
    # Initialize variables
    variable_used = 0  # Count the number of variables used in the equation
    translated_string_equation = ""  # Initialize the translated string equation
    # Initialize the count for each variable (p, q, r, s)
    countP = 0
    countQ = 0
    countR = 0
    countS = 0
    translations = []  # To store the translation pairs (symbol and its translation)
    stack_list = []
    
    # Initialize the index for string traversal
    i = 0

    # Loop through each character in the string_equation
    while i < len(string_equation):
        # Check if the current character is a variable ('p', 'q', 'r', 's')
        if string_equation[i] == 'p':
            translations.append(("p", "p"))  # Add translation pair
            if countP == 0:  # Only increment variable_used if this is the first time encountering 'p'
                variable_used += 1
                countP += 1
            translated_string_equation += 'p'  # Append 'p' to the translated equation
            stack_list.append('p')
            i += 1
        
        elif string_equation[i] == 'q' and string_equation[i - 1] != 'e':  # Special check to avoid 'equivalent' confusion
            translations.append(("q", "q"))  # Add translation pair
            if countQ == 0:  # First encounter of 'q'
                variable_used += 1
                countQ += 1
            translated_string_equation += 'q'
            stack_list.append('q')
            i += 1

        elif string_equation[i] == 'r':
            translations.append(("r", "r"))  # Add translation pair
            if countR == 0:  # First encounter of 'r'
                variable_used += 1
                countR += 1
            translated_string_equation += 'r'
            stack_list.append('r')
            i += 1

        elif string_equation[i] == 's':
            translations.append(("s", "s"))  # Add translation pair
            if countS == 0:  # First encounter of 's'
                variable_used += 1
                countS += 1
            translated_string_equation += 's'
            stack_list.append('s')
            i += 1
        
        # Check if the current character is a parenthesis
        elif string_equation[i] == '(':
            translations.append(("(", "("))  # Add translation for '('
            translated_string_equation += '('
            stack_list.append('(')
            i += 1

        elif string_equation[i] == ')':
            translations.append((")", ")"))  # Add translation for ')'
            translated_string_equation += ')'
            stack_list.append(')')
            i += 1

        # Check for logical operators like 'and', 'or', 'not', etc.
        elif string_equation[i:i+3] == 'and':  # Translate 'and' to '^'
            translations.append(("and", "^"))
            i += 3  # Move the index forward by 3 characters
            translated_string_equation += '^'
            stack_list.append('^')

        elif string_equation[i:i+2] == 'or':  # Translate 'or' to 'v'
            translations.append(("or", "v"))
            i += 2  # Move the index forward by 2 characters
            translated_string_equation += 'v'
            stack_list.append('v')

        elif string_equation[i:i+3] == 'not':  # Translate 'not' to '~'
            translations.append(("not", "~"))
            i += 3  # Move the index forward by 3 characters
            translated_string_equation += '~'
            stack_list.append('~')

        elif string_equation[i:i+7] == 'implies':  # Translate 'implies' to '=>'
            translations.append(("implies", "=>"))
            i += 7  # Move the index forward by 7 characters
            translated_string_equation += '=>'
            stack_list.append('=>')

        elif string_equation[i:i+10] == 'equivalent':  # Translate 'equivalent' to '<=>'
            translations.append(("equivalent", "<=>"))
            i += 10  # Move the index forward by 10 characters
            translated_string_equation += '<=>'
            stack_list.append('<=>')

        # Skip over spaces in the string
        elif string_equation[i] == ' ':
            i += 1

        # Handle unrecognized characters
        else:
            os.system('cls')  # Clear the console screen
            print("Error: Unregistered character detected.")
            print("Error: Invalid character detected: ", string_equation)
            print("Note: Must be p, q, r, s, and, or, not, implies, equivalent only!")
            sys.exit(1)  # Exit the program with an error

    # Remove duplicate translation pairs (e.g., multiple 'p' translations)
    translations = remove_duplicates(translations)

    # Printing the table header for the translation
    print(f"{'Translation':<15} | {'Symbol':<15}")
    print('-' * 35)  # Separator line

    # Print each symbol and its corresponding translation
    for symbol, translation in translations:
        print(f"{symbol:<15} | {translation:<15}")

    # Print the final translated equation
    print("\nEquation: ", translated_string_equation)

    # Return the updated variable_used count and the translated string equation
    return variable_used, translated_string_equation, stack_list


def fill_matrix_with_binary_count(row, col):
    # Initialize the matrix with zeros
    matrix = [[0 for i in range(col)] for j in range(row)]

    # Start filling the matrix with binary counting
    for i in range(1, row):  # Start from the second row (since the first row is all zeros)
        # Copy the previous row's values
        for j in range(col):
            matrix[i][j] = matrix[i - 1][j]

        # Increment binary by flipping bits from the end
        for j in range(col - 1, -1, -1):  # Start from the last column and move backwards
            if matrix[i][j] == 0:  # If the bit is 0, flip it to 1 and stop
                matrix[i][j] = 1
                break
            else:
                matrix[i][j] = 0  # If the bit is 1, flip it to 0 and continue to the next column

    return matrix
    

def assign_values(row, variable_used, matrix):
    p = []  # Initialize the list for variable 'p'
    q = []  # Initialize the list for variable 'q'
    r = []  # Initialize the list for variable 'r'
    s = []  # Initialize the list for variable 's'
    
    # Nested function to assign values to each variable from a specific column of the matrix
    def assign_values_to_variables(row, matrix, y):
        # Initialize a list 'x' with zeros, one element per row
        x = [0] * row

        # Loop through each row to copy values from the matrix
        for i in range(row):
            # Assign the value from matrix at row 'i' and column 'y' to x[i]
            x[i] = matrix[i][y]

        return x  # Return the list of values for the given column 'y'

    # Create a list to store the variables p, q, r, and s
    variables = [p, q, r, s]
    y = 0  # Initialize column index 'y'

    # Loop through the number of variables being used
    for i in range(variable_used):
        # Assign values from the matrix to the appropriate variable by column
        variables[i] = assign_values_to_variables(row, matrix, y)
        y += 1  # Move to the next column for the next variable

    # Return the updated values of p, q, r, and s (some may remain empty if not used)
    return variables[0], variables[1], variables[2], variables[3]


def main ():
    # Initialize variables
    string_equation = "p and q and q and q and (p and q)"

    print("Equation: " + string_equation)
    # Translate the string
    variable_used, translated_string_equation, stack_list = translate(string_equation)
    # Calculate the dimensions
    row, col = calc.calculate_dimensions(variable_used)
    # Fill the matrix with binary values to represent all combinations of truth values
    matrix = fill_matrix_with_binary_count(row, col)
    # Assign truth values to the variables based on the binary matrix
    p, q, r, s = assign_values(row, variable_used,matrix)

    stack_list = stack.stack_list(stack_list)
    print(stack_list)



if __name__ == "__main__":
    main()