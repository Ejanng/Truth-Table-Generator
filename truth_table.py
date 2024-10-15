
import sys
import os   

def remove_duplicates(array):
        seen = set()  # Initialize an empty set to keep track of seen items
        result = []  # List to store unique items

        # Iterate over each item in the array
        for item in array:
            if item not in seen:  # If the item hasn't been encountered yet
                result.append(item)  # Add it to the result list
                seen.add(item)  # Mark the item as seen by adding it to the set

        return result  # Return the list of unique items

def translate(variable_used, string_equation, translated_string_equation):
    # Initialize the count for each variable (p, q, r, s)
    countP = 0
    countQ = 0
    countR = 0
    countS = 0
    translations = []  # To store the translation pairs (symbol and its translation)
    
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
            i += 1
        
        elif string_equation[i] == 'q' and string_equation[i - 1] != 'e':  # Special check to avoid 'equivalent' confusion
            translations.append(("q", "q"))  # Add translation pair
            if countQ == 0:  # First encounter of 'q'
                variable_used += 1
                countQ += 1
            translated_string_equation += 'q'
            i += 1

        elif string_equation[i] == 'r':
            translations.append(("r", "r"))  # Add translation pair
            if countR == 0:  # First encounter of 'r'
                variable_used += 1
                countR += 1
            translated_string_equation += 'r'
            i += 1

        elif string_equation[i] == 's':
            translations.append(("s", "s"))  # Add translation pair
            if countS == 0:  # First encounter of 's'
                variable_used += 1
                countS += 1
            translated_string_equation += 's'
            i += 1
        
        # Check if the current character is a parenthesis
        elif string_equation[i] == '(':
            translations.append(("(", "("))  # Add translation for '('
            translated_string_equation += '('
            i += 1

        elif string_equation[i] == ')':
            translations.append((")", ")"))  # Add translation for ')'
            translated_string_equation += ')'
            i += 1

        # Check for logical operators like 'and', 'or', 'not', etc.
        elif string_equation[i:i+3] == 'and':  # Translate 'and' to '^'
            translations.append(("and", "^"))
            i += 3  # Move the index forward by 3 characters
            translated_string_equation += '^'

        elif string_equation[i:i+2] == 'or':  # Translate 'or' to 'v'
            translations.append(("or", "v"))
            i += 2  # Move the index forward by 2 characters
            translated_string_equation += 'v'

        elif string_equation[i:i+3] == 'not':  # Translate 'not' to '~'
            translations.append(("not", "~"))
            i += 3  # Move the index forward by 3 characters
            translated_string_equation += '~'

        elif string_equation[i:i+7] == 'implies':  # Translate 'implies' to '=>'
            translations.append(("implies", "=>"))
            i += 7  # Move the index forward by 7 characters
            translated_string_equation += '=>'

        elif string_equation[i:i+10] == 'equivalent':  # Translate 'equivalent' to '<=>'
            translations.append(("equivalent", "<=>"))
            i += 10  # Move the index forward by 10 characters
            translated_string_equation += '<=>'

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
    return variable_used, translated_string_equation

            
def calculate_dimensions(variable_used, row, col):
    # Check if there are no variables used (p, q, r, s)
    if variable_used < 1:
        os.system('cls')  # Clear the console
        print("Error: There is no variable used!.")
        print("Note: Variable must be p, q, r, s only!")
        sys.exit(1)  # Exit the program if no variables are used
    else:
        # Initialize holder and two_power variables
        holder = 2  # Start with 2 rows for one variable (2^1)
        power = 0
        two_power = 2  # Base value for calculating powers of 2

        # Calculate the number of rows (2^n) based on the number of variables
        for i in range(variable_used - 1):
            power = two_power * holder  # Multiply by 2 to get the next power
            holder = power  # Update holder with the new power value

        # The number of columns is equal to the number of variables
        col = variable_used
        # The number of rows is 2 raised to the power of the number of variables (2^n)
        row = holder

        return row, col  # Return the calculated row and column values


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
    

def assign_values(row, variable_used, p, q, r, s, matrix):
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


def store_values_inside_the_array(row, translated_string_equation, p, q, r, s):
    i = 0  # Index for traversing the string
    integer_equation = []  # Temp list to hold solved values and operators
    string_equation = []
    solve_value_for_not = []
    
    def operator_not(row, a):
        solve_value = [0] * row  # Initialize the result list with 0s
        for i in range(row):
            solve_value[i] = int(not a[i])  # Perform NOT operation
        return solve_value  # Return the list of results

    while i < len(translated_string_equation):
        # Check for opening parenthesis '('
        if translated_string_equation[i] == '(':
            # Traverse string_solve from right to left to prioritize innermost expressions first
            integer_equation.append('(')  # Append '(' to the temp list
            string_equation.append('(')
            i += 1
        # Check for closing parenthesis ')'
        elif translated_string_equation[i] == ')':
            integer_equation.append(')')
            string_equation.append(')')
            i += 1
        # Check for variables (p, q, r, s) and append their values directly
        elif translated_string_equation[i] == 'p':
            integer_equation.append(p)
            string_equation.append('p')
            i += 1
        elif translated_string_equation[i] == 'q':
            integer_equation.append(q)
            string_equation.append('q')
            i += 1
        elif translated_string_equation[i] == 'r':
            integer_equation.append(r)
            string_equation.append('r')
            i += 1
        elif translated_string_equation[i] == 's':
            integer_equation.append(s)
            string_equation.append('s')
            i += 1

        # Check for operators ^ (and), v (or), => (implies), <=> (equivalence)
        elif translated_string_equation[i] == '^':
            integer_equation.append('^')  # Append 'and' operator
            string_equation.append('^')
            i += 1
        elif translated_string_equation[i] == 'v':
            integer_equation.append('v')  # Append 'or' operator
            string_equation.append('v')
            i += 1
        elif translated_string_equation[i] == '~' and translated_string_equation[i+1] != '(':
            if translated_string_equation[i+1] not in ['p', 'q', 'r', 's']:
                os.system('cls')
                print("Translated string: ", translated_string_equation)
                print("Error: Invalid use of 'not' operator.")
                print("Error: (not + operator) or (not + unregistered variable.)")
                print("Note: Must be not + variable. (e.g. not p, not q, not r, not s)")
                sys.exit(1)
            string_value = translated_string_equation[i+1]
            if string_value == 'p':
                solve_not_value = operator_not(row, p)
            elif string_value == 'q':
                solve_not_value = operator_not(row, q)
            elif string_value == 'r':
                solve_not_value = operator_not(row, r)
            elif string_value == 's':
                solve_not_value = operator_not(row, s)
            integer_equation.append(solve_not_value)
            solve_value_for_not.append(solve_not_value)
            string_equation.append('~')
            string_equation.append(translated_string_equation[i+1])
            i += 2
        elif translated_string_equation[i] == '~' and translated_string_equation[i+1] == '(':
            os.system('cls')
            print("Error: Invalid use of 'not' operator.")
            sys.exit(1)
        elif translated_string_equation[i:i+2] == '=>':
            integer_equation.append('=>')  # Append 'implies' operator
            string_equation.append('=>')
            i += 2
        elif translated_string_equation[i:i+3] == '<=>':
            integer_equation.append('<=>')  # Append 'equivalence' operator
            string_equation.append('<=>')
            i += 3

        else:
            i += 1  # Move forward if no parenthesis, variable, or operator found

    return integer_equation, string_equation, solve_value_for_not


def is_equation_valid(integer_equation, string_equation):
    i = 1
    operator = ['^', 'v', '=>', '<=>']  # List of valid operators
    operators = ['^', 'v', '=>', '<=>', 'p', 'q', 'r', 's']  # Extended list including variables

    # Check if the equation has invalid consecutive operators like "var op var op var"
    for j in range(len(operator)):
        for k in range(len(operator)):
            if i >= len(integer_equation) - 2:  # Prevent index out of range
                break
            # If two consecutive operators are found, the equation is invalid
            if integer_equation[i] == operator[j] and integer_equation[i + 2] == operator[k]:
                os.system('cls')
                print("Error: Invalid equation detected.")
                print("Error: e.g. 'var op var op var'.")
                print("Note: Must be valid equation only!")
                print("Note: e.g. 'var op var', '(var op var) op var', etc.")
                sys.exit(1)

    # Catch equations with unbalanced parentheses (e.g., "(var op var" - missing closing bracket)
    stack = []  # To keep track of opening parentheses
    for i in range(len(integer_equation)):
        # Push opening parenthesis onto the stack
        if integer_equation[i] == '(':
            stack.append(i)
        # When a closing parenthesis is found
        elif integer_equation[i] == ')':
            if len(stack) == 0:  # No matching opening parenthesis
                os.system('cls')
                print("Error: Invalid equation detected.")
                print("Error: No matching opening bracket for closing bracket at index:", i)
                print("Note: Must be valid equation only!")
                print("Note: e.g. (var op var), etc")
                sys.exit(1)
            else:
                stack.pop()  # Match found, pop the corresponding opening parenthesis

    # If there are unmatched opening parentheses left
    if len(stack) > 0:
        os.system('cls')
        print("Error: Invalid equation detected.")
        print(f"Error: No closing bracket for opening bracket at index: {stack[-1]}")
        print("Note: Must be valid equation only!")
        print("Note: e.g. (var op var), etc")
        sys.exit(1)

    # Catch invalid consecutive opening brackets like "((var op var)"
    i = 0
    while i < len(integer_equation):
        if i >= len(integer_equation) - 1:
            break
        # Detect two consecutive opening brackets
        if integer_equation[i] == '(' and integer_equation[i + 1] == '(':
            os.system('cls')
            print("Error: Invalid equation detected.")
            print("Error: Invalid use of opening brackets.")
            print("Note: Must be valid equation only!")
            print("Note: e.g. (var op var), etc")
            sys.exit(1)
        i += 1

    # Handle equations of the form "(var op var)" by rewriting them to "var op var"
    rewritten_integer_equation = []
    rewritten_string_equation = []
    i = 0
    # Check for equations enclosed in parentheses with exactly 5 elements "(var op var)"
    if len(integer_equation) == 5 and integer_equation[0] == '(' and integer_equation[4] == ')':
        while i < len(integer_equation):
            # If an opening parenthesis is found
            if integer_equation[i] == '(':
                i += 1  # Skip the opening parenthesis
                j = i
                # Collect the expression inside the parentheses
                while i < len(integer_equation) and integer_equation[i] != ')':
                    rewritten_integer_equation.append(integer_equation[i])
                    i += 1
                # Do the same for the string_equation
                while j < len(string_equation) and string_equation[j] != ')':
                    rewritten_string_equation.append(string_equation[j])
                    j += 1
            i += 1
        if len(rewritten_integer_equation) > 0:
            return rewritten_string_equation, rewritten_integer_equation

    # Catch equations like "(var op var) var", where there's no operator after a closing bracket
    i = 0
    while i < len(integer_equation):
        if i >= len(integer_equation) - 1:
            break
        # If a closing parenthesis is followed by something that is not an operator
        if integer_equation[i] == ')' and integer_equation[i + 1] not in ['^', 'v', '=>', '<=>']:
            os.system('cls')
            print("Error: Invalid equation detected.")
            print("Error: No operator after closing bracket.")
            print("Note: Must be valid equation only!")
            print("Note: e.g. (var op var), etc")
            sys.exit(1)
        i += 1

    # Catch equations like "var op (var", where there's no opening parenthesis for the last term
    i = 0
    while i < len(integer_equation):
        # Check if the current item is an operator and the next item is an opening parenthesis without a matching closing bracket
        if integer_equation[i] in operators and integer_equation[i + 1] == '(' and integer_equation[i - 1] != ')':
            os.system('cls')
            print("Error: Invalid equation detected.")
            print("Error: Invalid use of operator followed by a parenthesis.")
            print("Note: Must be valid equation only! (e.g. p and (q or r))")
            sys.exit(1)
        i += 1

    # Catch consecutive variables without an operator (e.g., "var var")
    i = 0
    for i in range(len(integer_equation)):
        if i >= len(integer_equation) - 1:
            break
        # If two consecutive variables are found without an operator in between
        if integer_equation[i] not in ['^', 'v', '=>', '<=>'] and integer_equation[i + 1] not in ['^', 'v', '=>', '<=>', ')'] and integer_equation[i] != '(':
            os.system('cls')
            print("Error: Invalid equation detected.")
            print("Error: Invalid use of variables.")
            print("Note: Must be valid equation only! (e.g. p and (q or r))")
            sys.exit(1)
    
    return 0, 0  # Return 0,0 if no errors are found, indicating the equation is valid


def calculate_complex_equation(row, string_equation, integer_equation, solve_value_for_not, not_length):
    def calculate_equation(row, string_length, integer_equation):
        # Initialize variables
        i = 1  # Start from the second character
        a = [0] * row  # Placeholder for values of variable a
        b = [0] * row  # Placeholder for values of variable b
        solve_value = []  # List to store the results of operations

        def assign_values_for_a_and_b(final_string_equation, i):    
            # Assign values based on the characters adjacent to the operator
            a = final_string_equation[i - 1]  # Value before the operator
            b = final_string_equation[i + 1]  # Value after the operator
            return a, b  # Return the values of a and b

        # Logical operations defined within the function
        def operator_and(row, a, b):
            # Initialize a list to store results of the AND operation
            solve_value = [0] * row
            
            # Perform the AND operation for each corresponding pair of values in a and b
            for i in range(row):
                solve_value[i] = a[i] and b[i]  # Logical AND operation
            
            return solve_value  # Return the results

        def operator_or(row, a, b):
            # Initialize a list to store results of the OR operation
            solve_value = [0] * row  # Fill with 0s initially
            
            # Perform the OR operation for each corresponding pair of values in a and b
            for i in range(row):
                solve_value[i] = a[i] or b[i]  # Logical OR operation
            
            return solve_value  # Return the results

        def operator_implies(row, a, b):
            # Initialize a list to store results of the implication operation
            solve_value = [0] * row  # Fill with 0s initially
            
            # Calculate logical implication (not a or b) for each pair of values in a and b
            for i in range(row):
                solve_value[i] = int(not a[i]) or b[i]  # Logical implication operation
            
            return solve_value  # Return the results

        def operator_equivalent(row, a, b):
            # Initialize a list to store results of the equivalence operation
            solve_value = [0] * row  # Fill with 0s initially
            
            # Check equivalence for each pair of values in a and b (a == b)
            for i in range(row):
                solve_value[i] = int(a[i] == b[i])  # Logical equivalence operation
            
            return solve_value  # Return the results
            
        while i < string_length - 1:
            # Ensure 'i' is within the bounds of the integer_equation list to avoid IndexError
            if i >= len(integer_equation):
                break
            
            # Handle 'AND' operation (^)
            if integer_equation[i] == '^':
                a, b = assign_values_for_a_and_b(integer_equation, i)  # Get a and b values
                solve_value = operator_and(row, a, b)  # Perform AND operation
            
            # Handle 'OR' operation (v)
            elif integer_equation[i] == 'v':
                a, b = assign_values_for_a_and_b(integer_equation, i)  # Get a and b values
                solve_value = operator_or(row, a, b)  # Perform OR operation

            # Handle 'IMPLIES' operation (=>), check if we have enough characters left in the string
            elif integer_equation[i] == '=>':
                a, b = assign_values_for_a_and_b(integer_equation, i)  # Get a and b values
                solve_value = operator_implies(row, a, b)  # Perform implication
                i += 1  # Skip '>' to move to the next operator
            
            # Handle 'EQUIVALENT' operation (<=>), check if we have enough characters left in the string
            elif integer_equation[i] == '<=>':
                a, b = assign_values_for_a_and_b(integer_equation, i)  # Get a and b values
                solve_value = operator_equivalent(row, a, b)  # Perform equivalence
                i += 2  # Skip '=' and '>' to move to the next operator
            
            # Move to the next character
            i += 1
        
        return solve_value  # Return the final computed values of the equation

    # Initialize necessary lists and variables
    solve_value = []
    string_priority = []
    k = 0  # Index for operator check
    l = 0  # Index for parsing parentheses
    m = 0  # Index for single equation check
    n = 0  # Index for '~' check
    operator = []  # To store operators found
    temp_string_equation = []  # Temporary storage for equations during processing
    single_equation = []  # To store individual equations

    while 1:
        string_length = len(integer_equation)  # Length of the integer equation
        i = 0
        while i < string_length:
            l = i
            found_open_parenthesis = False  # Flag to track if '(' is found

            # Process the string_equation to handle '~' (NOT operation)
            while n < len(string_equation):
                if n >= len(string_equation) - 1:
                    break
                if string_equation[n] == '~':
                    # Pop the value to solve for NOT and append it to solve_value and temp_string_equation
                    value = solve_value_for_not.pop(0)
                    solve_value.append(value)
                    temp_string_equation.append(value)
                    value = []
                    # Track priority for '~'
                    string_priority.append(string_equation[n] + string_equation[n+1])
                n += 1

            # Loop to find and handle parenthesized expressions
            for t in range(len(string_equation)):
                found_open_parenthesis = False  # Reset the flag before each iteration
                if l >= len(string_equation) - 1:
                    break
                while string_equation[l] != ')':  # Keep scanning until we find a closing parenthesis
                    if l >= len(string_equation) - 1:
                        break
                    if string_equation[l] == '(':
                        found_open_parenthesis = True  # Set flag when '(' is found
                        o = l  # Store the position of '('
                    l += 1
                l += 1

                # If we found an open parenthesis and it has content, extract the expression inside
                if found_open_parenthesis and o + 1 < l:
                    string_priority.append(string_equation[o + 1:l-1])

            # Remove empty elements and duplicates from string_priority
            cleaned_array = [x for x in string_priority if x]
            string_priority = cleaned_array
            string_priority = [tuple(x) if isinstance(x, list) else x for x in string_priority]
            unique_string = remove_duplicates(string_priority)

            # Check for operators after closing parentheses
            while k < string_length - 1:
                if integer_equation[k] == ')':
                    operator.append(integer_equation[k+1])  # Store operator found after ')'
                k += 1

            # Extract single equation when not enclosed in parentheses
            while m < string_length:
                if m >= len(integer_equation) - 1:
                    break
                if integer_equation[m] == ')' and integer_equation[m+2] != '(':
                    single_equation.append(integer_equation[m+2])
                m += 1

            # Process each parenthesized equation
            if integer_equation[i] == '(':
                j = i
                while integer_equation[j] != ')':
                    if integer_equation[j] == '(':
                        i = j
                    j += 1
                # Calculate the value of the equation inside the parentheses
                value = calculate_equation(row, j - i, integer_equation[i + 1:j])
                solve_value.append(value)

                # Handle NOT (~) logic by resetting temp_string_equation if needed
                if not_length:
                    temp_string_equation = []
                    not_length = 0 

                temp_string_equation.append(value)
                value = []

                # Append operator and single equation to temp_string_equation
                if operator:
                    temp_string_equation.append(operator.pop(0))
                if single_equation:
                    temp_string_equation.append(single_equation.pop(0))
                
                i = j  # Move index past the processed parentheses

            # Process the case where the equation has only 3 elements (simple case)
            if len(integer_equation) == 3:
                value = calculate_equation(row, string_length, integer_equation)
                solve_value.append(value)

                # Keep temp_string_equation in sync
                if len(temp_string_equation) > 1:
                    temp_string_equation.pop(0)
                temp_string_equation.append(value)
                value = []

                # Final cleanup of the equation
                integer_equation = temp_string_equation
                solve_value = [tuple(x) if isinstance(x, list) else x for x in solve_value]
                unique_value = solve_value
                string_priority = [' '.join(item) for item in unique_string]

                # Remove duplicates from the solve_value
                for i in range(len(string_priority)):
                    for j in range(len(string_priority)):
                        if string_priority[i] == string_priority[j] and i != j:
                            unique_value = remove_duplicates(solve_value)
                solve_value = unique_value
                return solve_value, string_priority, integer_equation

            # If the equation has only one element, return it as the solution
            elif len(integer_equation) == 1:
                solve_value = integer_equation
                return solve_value, string_priority, integer_equation
            
            i += 1  # Move to the next element
        
        # Update integer_equation with the processed temporary equation
        integer_equation = temp_string_equation


def display_truth_table(propositions, translated_string, solve_value, string_solve):
    # Create a filtered version of propositions, ensuring only non-empty lists are included
    filtered_props = {k: v for k, v in propositions.items() if len(v) > 0}

    # Check if filtered_props is empty
    if not filtered_props:
        print("No valid propositions to display.")
        return

    # Extract filtered proposition names and their corresponding values
    prop_names = list(filtered_props.keys())
    prop_values = list(filtered_props.values())

    # Length of the value columns
    num_rows = len(prop_values[0]) if prop_values else 0

    # Prepare the header including the intermediate steps and the final equation
    header = prop_names + (string_solve if string_solve else ['']) + [translated_string]

    # Set fixed widths for headers and values
    fixed_width = 10  # Fixed width for each column

    # Prepare the header string with fixed widths
    header_str = " | ".join(name.ljust(fixed_width) for name in header)
    print("-" * len(header_str))
    print(header_str)
    print("-" * len(header_str))  # Separator line

    # Display each row of values, including intermediate and final values
    for i in range(num_rows):
        # Gather the truth values for the propositions in the current row
        row_values = [str(prop[i]).ljust(fixed_width) for prop in prop_values]

        # Add the corresponding intermediate values (from solve_value)
        intermediate_values = [str(solve_value[i]).ljust(fixed_width) for solve_value in solve_value]

        # Combine all row values
        row_values.extend(intermediate_values)

        # Print the aligned row with fixed-width columns
        print(" | ".join(row_values))
    print("-" * len(header_str))  # Separator line after the table


def main():
    # Initialize variables
    variable_used = 0
    equations = []  # List to store all equations from the text file

    # Read the logical equations from a file
    with open('equation.txt', 'r') as file:
        for line in file:
            line = line.strip()  # Remove leading and trailing whitespace
            if line.endswith(';'):
                equation = line[:-1]  # Remove the semicolon at the end
                equations.append(equation)  # Add the equation to the list

    # Process each equation independently
    for string_equation in equations:
        # Reset variables for each equation
        row = 0
        col = 0
        variable_used = 0
        translated_string_equation = ""  # Placeholder for the translated equation
        solve_value = []  # List to store results of calculations
        string_priority = []  # List to store the priority of the string
        p = []  # Placeholder for truth values of variable p
        q = []  # Placeholder for truth values of variable q
        r = []  # Placeholder for truth values of variable r
        s = []  # Placeholder for truth values of variable s

        print("Equation: " + string_equation)
        # Translate the string
        variable_used, translated_string_equation = translate(variable_used, string_equation, translated_string_equation)

        # Calculate the dimensions
        row, col = calculate_dimensions(variable_used, row, col)

        # Fill the matrix with binary values to represent all combinations of truth values
        matrix = fill_matrix_with_binary_count(row, col)

        # Assign truth values to the variables based on the binary matrix
        p, q, r, s = assign_values(row, variable_used, p, q, r, s, matrix)
        propositions = {'P': p, 'Q': q, 'R': r, 'S': s}  # Create a dictionary to store the variable values

        # Store values inside an array, processing the translated string equation
        integer_equation, string_equation, solve_value_for_not = store_values_inside_the_array(row, translated_string_equation, p, q, r, s)

        not_length = len(solve_value_for_not)  # Determine the number of NOT operations

        # Check if the equation is valid and rewrite it if necessary
        rewritten_string_equation, rewritten_integer_equation = is_equation_valid(integer_equation, string_equation)
        if rewritten_string_equation:
            integer_equation = rewritten_integer_equation  # Update the integer equation
            string_equation = rewritten_string_equation  # Update the string equation

        # Calculate the result of the complex equation
        solve_value, string_priority, value_of_the_equation = calculate_complex_equation(row, string_equation, integer_equation, solve_value_for_not, not_length)

        # Display the truth table of the evaluated propositions
        display_truth_table(propositions, translated_string_equation, solve_value, string_priority)

        new_lines = 3
        print("\n" * new_lines) # Add new lines for the next equation

# Run the main function
if __name__ == "__main__":
    main()


# Errors:
# (not p and not q) implies
# and p
# not p
# not p and
# p and
