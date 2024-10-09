# Need to implement the following:
# Negation is not yet fully implemented
# Parenthesis is not yet fully implemented
# Fix the bug in translating the equivalence
# In calculating the complex equation, the equation inside of parenthesis is not yet fully implemented to be calculated
# Implement the extra characters for the input string
# Fix Implies operator giving wrong results

 
import os
import sys

# Usable for future implementation
def invalid_input():
    # Clear the terminal
    if os.name == 'nt':  # For Windows
        os.system('cls')
    
    # Print "Invalid Input"
    print("Invalid Input")

    # Exit the program
    sys.exit()


def translate(variable_used, string_length, str_equation, final_str_equation):
    # Initialize the count of each variable
    countP = 0
    countQ = 0
    countR = 0
    countS = 0
    # Initialize the index
    i = 0
    while i < string_length:
        # Check the character of the string
        if str_equation[i] == 'p':
            print("p detected")
            if countP == 0:
                variable_used += 1
                countP += 1
            final_str_equation += 'p'
        elif str_equation[i] == 'q':
            print("q detected")
            if countQ == 0:
                variable_used += 1
                countQ += 1
            final_str_equation += 'q'
        elif str_equation[i] == 'r':
            print("r detected")
            if countR == 0:
                variable_used += 1
                countR += 1
            final_str_equation += 'r'
        elif str_equation[i] == 's':
            print("s detected")
            if countS == 0:
                variable_used += 1
                countS += 1
            final_str_equation += 's'
        # Check the operator of the string
        elif str_equation[i] == '(':
            print("( detected")
            final_str_equation += '('
        elif str_equation[i] == ')':
            print(") detected")
            final_str_equation += ')'
        elif str_equation[i] == 'a' and str_equation[i - 1] != 'v':
            print("and detected")
            i += 2
            final_str_equation += '^'
        elif str_equation[i] == 'o' and str_equation[i - 1] != 'n':
            print("or detected")
            i += 1
            final_str_equation += 'v'
        elif str_equation[i] == 'n' and str_equation[i - 1] != 'a' or str_equation[i] == 'n' and str_equation[i - 1] != 'e':
            print("not detected")
            i += 2
            final_str_equation += '~'
        elif str_equation[i] == 'i' and str_equation[i - 1] != 'u':
            print("implies detected")
            i += 6
            final_str_equation += '='
            final_str_equation += '>'
        elif str_equation[i] == 'e' and str_equation[i - 1] != 'i':
            print("equals detected")
            i += 5
            final_str_equation += '<'
            final_str_equation += '='
            final_str_equation += '>'

        i += 1
    # # Debugger
    # print(countP)
    # print(countQ)
    # print(countR)
    # print(countS)
    # # Debugger

    return variable_used, final_str_equation


def calculate_dimensions(variable_used, row, col):
    if variable_used == 1:
        row = 0
        col = 0
    else:
        holder = 2
        power = 0
        two_power = 2

        i = 0

        for i in range(variable_used - 1):
            power = two_power * holder
            holder = power

        col = variable_used
        row = holder

        return row, col
    

def fill_matrix_with_binary_count(row, col):
    # Initialize the matrix with zeros
    matrix = [[0 for i in range(col)] for j in range(row)]

    # Start filling the matrix with binary counting
    for i in range(1, row):
        # Copy the previous row
        for j in range(col):
            matrix[i][j] = matrix[i - 1][j]

        # Increment binary by flipping bits from the end
        for j in range(col - 1, -1, -1):
            if matrix[i][j] == 0:
                matrix[i][j] = 1
                break
            else:
                matrix[i][j] = 0

    return matrix


def assign_values_to_variables(row, matrix, y):
    x = [0] * row

    for i in range(row):
        x[i] = matrix[i][y]

    return x
    

def assign_values(row, variable_used, p, q, r, s, matrix):
    variables = [p, q, r, s]  # Create a list to store variables
    y = 0

    for i in range(variable_used):
        variables[i] = assign_values_to_variables(row, matrix, y)
        y += 1

    # Return the updated variables, unpacking the list
    return variables[0], variables[1], variables[2], variables[3]


def operator_and(row, a, b):
    solve_value = [0] * row
    for i in range(row):
        solve_value[i] = a[i] and b[i]
    return solve_value


def operator_or(row, a, b):
    solve_value = [0] * row  # Initialize the result list with 0s
    for i in range(row):
        solve_value[i] = a[i] or b[i]  # Perform OR operation
    return solve_value  # Return the list of results


def operator_implies(row, a, b):
    solve_value = [0] * row  # Initialize the result list with 0s
    for i in range(row):
        solve_value[i] = int((not a[i]) or b[i])  # Logical implication (not a or b)
    return solve_value


def operator_equivalent(row, a, b):
    solve_value = [0] * row  # Initialize the result list with 0s
    for i in range(row):
        solve_value[i] = (a[i] == b[i])  # Check equivalence (a == b)
    return solve_value  # Return the list of results


def check_for_not_value(row, final_str_equation, i, p, q, r, s):
    solve_value = [0] * row  # Initialize list with zeros of size `row`
    
    # Check for the variable following 'not'
    if final_str_equation[i + 1] == 'p':
        for j in range(row):
            solve_value[j] = int(not p[j])  # Negate the value of p
    elif final_str_equation[i + 1] == 'q':
        for j in range(row):
            solve_value[j] = int(not q[j])  # Negate the value of q
    elif final_str_equation[i + 1] == 'r':
        for j in range(row):
            solve_value[j] = int(not r[j])  # Negate the value of r
    elif final_str_equation[i + 1] == 's':
        for j in range(row):
            solve_value[j] = int(not s[j])  # Negate the value of s

    return solve_value  # Return the complete list after the loop


def assign_values_for_a_and_b(row, final_str_equation, i, p, q, r, s):
    def assign_values(char):
        if char == 'p':
            return p
        elif char == 'q':
            return q
        elif char == 'r':
            return r
        elif char == 's':
            return s
        return [0] * row  # Default case if no match
    
    a = assign_values(final_str_equation[i - 1])  # Assign values based on the previous character
    b = [0] * row  # Initialize `b` with 0s
    
    # Check the next character and assign values to `b`
    if i + 1 < len(final_str_equation):
        b = assign_values(final_str_equation[i + 1])
    
    # Handle other cases based on additional characters (for implies/equivalent)
    if i + 2 < len(final_str_equation):
        b = assign_values(final_str_equation[i + 2])
    if i + 3 < len(final_str_equation):
        b = assign_values(final_str_equation[i + 3])

    return a, b


def calculate_equation(row, string_length, final_str_equation, p, q, r, s):
    i = 0
    a = [0] * row
    b = [0] * row
    solve_value = []
    str_solve = final_str_equation

    while i < string_length:
        # Ensure 'i' is within the string's bounds to avoid IndexError
        if i >= len(final_str_equation):
            break
        
        # Handle 'AND' operation (^)
        if final_str_equation[i] == '^':
            a, b = assign_values_for_a_and_b(row, final_str_equation, i, p, q, r, s)
            solve_value = operator_and(row, a, b)
        
        # Handle 'OR' operation (v)
        elif final_str_equation[i] == 'v':
            a, b = assign_values_for_a_and_b(row, final_str_equation, i, p, q, r, s)
            solve_value = operator_or(row, a, b)
        
        # Handle 'NOT' operation (~)
        elif final_str_equation[i] == '~':
            solve_value = check_for_not_value(row, final_str_equation, i, p, q, r, s)

        # Handle 'IMPLIES' operation (=>), check if we have enough characters left in the string
        elif final_str_equation[i] == '=' and (i + 1) < string_length and final_str_equation[i + 1] == '>':
            a, b = assign_values_for_a_and_b(row, final_str_equation, i, p, q, r, s)
            solve_value = operator_implies(row, a, b)
            i += 1  # Skip '>'
        
        # Handle 'EQUIVALENT' operation (<=>), check if we have enough characters left in the string
        elif final_str_equation[i] == '<' and (i + 2) < string_length and final_str_equation[i + 1] == '=' and final_str_equation[i + 2] == '>':
            a, b = assign_values_for_a_and_b(row, final_str_equation, i, p, q, r, s)
            solve_value = operator_equivalent(row, a, b)
            i += 2  # Skip '=' and '>'

        # Move to the next character
        i += 1
    
    return solve_value, str_solve


def calculate_complex_equation (row, string_length, final_str_equation, p, q, r, s):
    value = []
    str_priority = []
    i = 0

    while i < string_length:
        if final_str_equation[i] == '(':
            j = i
            while final_str_equation[j] != ')':
                if final_str_equation[j] == '(':
                    i = j
                j += 1
            solve_value, str_solve = calculate_equation(row, j - i, final_str_equation[i + 1:j], p, q, r, s)
            value.append(solve_value)
            str_priority.append(str_solve)
            i = j
        i += 1 
        print("Solve Value: ", solve_value)
        print("String Value: ", str_priority)
    return value, str_priority


# logic to remove or calculate the parenthesis
def detect_operator(row, string_length, final_str_equation, p, q, r, s):
    i = 0
    checker = 0
    looper = 1
    while 1:
        for i in range(string_length):
            if final_str_equation[i] == '(':
                solve_value, str_solve = calculate_complex_equation(row, string_length, final_str_equation, p, q, r, s)
                checker += 1
                return solve_value, str_solve
            
        if checker == 0:
            for i in range(string_length):
                if final_str_equation[i] == '(' and checker == 0:
                    checker += 1
                
                if checker == 0:
                    solve_value, str_solve = calculate_equation(row, string_length, final_str_equation, p, q, r, s)
                    return solve_value, str_solve
            
    return solve_value, str_solve


def main ():
    # >> Integer <<
    row = 0
    col = 0
    variable_used = 0
    count = 0
    # >> String <<
    str_equation = "(p and q) implies r"
    # Translate the string
    final_str_equation = ""
    #                                               # For future implementation
    #                                               extra = "abcdefghijklmnotuvwxyz"
    # List of the final string matrix to be printed
    solve_value = []
    # array
    p = [0] * row
    q = [0] * row
    r = [0] * row
    s = [0] * row
    # length of the string
    string_length = len(str_equation)

    # translate the string
    variable_used, final_str_equation = translate(variable_used, string_length, str_equation, final_str_equation)
    # new length of the string  
    string_length = len(final_str_equation)
                                                    # For future implementation
                                                    # extra_length = len(extra)

    # 
    #                                           Future Implementation
    #                                           Check if the string is valid
    # 
    # check if the variable used is valid
    if variable_used < 0 or variable_used > 4:
        print("Invalid input");
        return 0;
    else:
        # calculate the dimensions
        row, col = calculate_dimensions(variable_used, row, col)
        # declare and initialize the matrix
        matrix = fill_matrix_with_binary_count(row, col)
        # assign values to the variables
        p, q, r, s = assign_values(row, variable_used, p, q, r, s, matrix)
        # append the result to the list
        solve_value, str_priority = detect_operator(row, string_length, final_str_equation, p, q, r, s)


        # Debugger
        print("The string is: ", str_equation)
        print("Translated string: ", final_str_equation)
        print("Variable Used: ", variable_used)
        print("String Length: ", string_length)
        print("Row: ", row)
        print("Col: ", col)
        # for row in matrix:
        #     print(row)
        print("P: ", p)
        print("Q: ", q)
        print("R: ", r)
        print("S: ", s)
        print("Solve Value: ", solve_value)
        print("String Value: ", str_priority)
        # Debugger


# Run the main function
if __name__ == "__main__":
    main()