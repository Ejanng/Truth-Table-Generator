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
    y = 0

    if variable_used == 1:
        p = assign_values_to_variables(row, matrix, y)
    elif variable_used == 2:
        p = assign_values_to_variables(row, matrix, y)
        y += 1
        q = assign_values_to_variables(row, matrix, y)
    elif variable_used == 3:
        p = assign_values_to_variables(row, matrix, y)
        y += 1
        q = assign_values_to_variables(row, matrix, y)
        y += 1
        r = assign_values_to_variables(row, matrix, y)
    elif variable_used == 4:
        p = assign_values_to_variables(row, matrix, y)
        y += 1
        q = assign_values_to_variables(row, matrix, y)
        y += 1
        r = assign_values_to_variables(row, matrix, y)
        y += 1
        s = assign_values_to_variables(row, matrix, y)

    return p, q, r, s


def operator_and(row, a, b):
    result = []  # Initialize an empty list to store the results
    for i in range(row):
        if a[i] and b[i]:
            solve_value = 1
        else:
            solve_value = 0
        result.append(solve_value)  # Store each solve_value in the result list
    return result  # Return the list of results


def operator_or(row, a, b):
    result = []  # Initialize an empty list to store the results
    for i in range(row):
        if a[i] or b[i]:
            solve_value = 1
        else:
            solve_value = 0
        result.append(solve_value)  # Append each solve_value to the result list
    return result  # Return the list of results



def operator_implies(row, a, b):
    result = []  # Initialize an empty list to store the results
    for i in range(row):
        if not a[i] or b[i]:
            solve_value = 1  # If a implies b, set to 1
        else:
            solve_value = 0  # Otherwise, set to 0
        result.append(solve_value)  # Append solve_value to the result list
    return result  # Return the list of results



def operator_equivalent(row, a, b):
    result = []  # Initialize an empty list to store the results
    for i in range(row):
        if a[i] == b[i]:
            solve_value = 1  # If a and b are equivalent, set to 1
        else:
            solve_value = 0  # Otherwise, set to 0
        result.append(solve_value)  # Append solve_value to the result list
    return result  # Return the list of results


def priority (final_str_equation, string_length, count):
    temp_priority = ""
    while count < string_length:
        if final_str_equation[count] == '(':
            while count < string_length:
                temp_priority += final_str_equation[count]
                if final_str_equation[count] == ')':
                    return temp_priority, count
                count += 1
        return temp_priority, count
    
    
def check_for_not_value (row, final_str_equation, i, p, q, r, s):
    if final_str_equation[i + 1] == 'p':
        for i in range(row):
            p[i] = not p[i]
            return p
    elif final_str_equation[i + 1] == 'q':
        for i in range(row):
            q[i] = not q[i]
            return q
    elif final_str_equation[i + 1] == 'r':
        for i in range(row):
            r[i] = not r[i]
            return r
    elif final_str_equation[i + 1] == 's':
        for i in range(row):
            s[i] = not s[i]
            return s


def assign_values_for_a_and_b (row, final_str_equation, i, a, b, p, q, r, s):
    if final_str_equation[i - 1] == 'p':
        for i in range(row):
            a[i] = p[i]
    elif final_str_equation[i - 1] == 'q':
        for i in range(row):
            a[i] = q[i]
    elif final_str_equation[i - 1] == 'r':
        for i in range(row):
            a[i] = r[i]
    elif final_str_equation[i - 1] == 's':
        for i in range(row):
            a[i] = s[i]

    if final_str_equation[i + 1] == 'p':
        for i in range(row):
            b[i] = p[i]
    elif final_str_equation[i + 1] == 'q':
        for i in range(row):
            b[i] = q[i]
    elif final_str_equation[i + 1] == 'r':
        for i in range(row):
            b[i] = r[i]
    elif final_str_equation[i + 1] == 's':
        for i in range(row):
            b[i] = s[i]

    return a, b


def calculate_equation (row, string_length, final_str_equation, p, q, r, s):
    i = 0
    a = [0] * row
    b = [0] * row
    solve_value = 0
    while i < string_length:
        if final_str_equation[i] == '^':
            a, b = assign_values_for_a_and_b(final_str_equation, i, p, q, r, s)
            solve_value = operator_and(row, a, b)
            return solve_value
        elif final_str_equation[i] == 'v':
            a, b = assign_values_for_a_and_b(final_str_equation, i, p, q, r, s)
            solve_value = operator_or(row, a, b)
        elif final_str_equation[i] == '~':
            solve_value = check_for_not_value(row, final_str_equation, i, p, q, r, s)
            return solve_value
        elif final_str_equation[i] == '=' and final_str_equation[i + 1] == '>':
            a, b = assign_values_for_a_and_b(final_str_equation, i, p, q, r, s)
            solve_value = operator_implies()
        elif final_str_equation[i] == '<' and final_str_equation[i + 1] == '=' and final_str_equation[i + 2] == '>':
            a, b = assign_values_for_a_and_b(final_str_equation, i, p, q, r, s)
            solve_value = operator_equivalent()
        i += 1
    pass


def main ():
    # integer
    row = 0
    col = 0
    variable_used = 0
    count = 0
    # string
    str_equation = "(p and q) implies (r or s)"
    final_str_equation = ""
    temp_priority = ""
    priority_to_solve = []
    extra = "abcdefghijklmnotuvwxyz"
    final_str_matrix = []
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
    extra_length = len(extra)

    # 
    #                                           Future Implementation
    #                                           Check if the string is valid
    # 
    # # Check if there is an extra variable
    # for i in range(string_length):
    #     for j in range(extra_length):
    #         if str_equation[i] == extra[i]:
    #             invalid_input()

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
        # list of priority to solve
        while count < string_length:
            # checking the priority of the equation
            temp_priority, count = priority(final_str_equation, string_length, count)
            # append the priority to the list
            if temp_priority != "":
                priority_to_solve.append(temp_priority)
            count += 1

        
        # Debugger
        print("The string is: ", str_equation)
        print("Translated string: ", final_str_equation)
        print("Variable Used: ", variable_used)
        print("String Length: ", string_length)
        print("Row: ", row)
        print("Col: ", col)
        for row in matrix:
            print(row)
        print("P: ", p)
        print("Q: ", q)
        print("R: ", r)
        print("S: ", s)
        print("Priority: ", priority_to_solve)
        # Debugger


# Run the main function
if __name__ == "__main__":
    main()