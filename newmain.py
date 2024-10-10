

def translate(variable_used, string_equation, translated_string_equation):
    # Initialize the count of each variable
    countP = 0
    countQ = 0
    countR = 0
    countS = 0
    # Initialize the index
    i = 0
    while i < len(string_equation):
        # Check the character of the string
        if string_equation[i] == 'p':
            print("p detected")
            if countP == 0:
                variable_used += 1
                countP += 1
            translated_string_equation += 'p'
        elif string_equation[i] == 'q':
            print("q detected")
            if countQ == 0:
                variable_used += 1
                countQ += 1
            translated_string_equation += 'q'
        elif string_equation[i] == 'r':
            print("r detected")
            if countR == 0:
                variable_used += 1
                countR += 1
            translated_string_equation += 'r'
        elif string_equation[i] == 's':
            print("s detected")
            if countS == 0:
                variable_used += 1
                countS += 1
            translated_string_equation += 's'
        # Check the operator of the string
        elif string_equation[i] == '(':
            print("( detected")
            translated_string_equation += '('
        elif string_equation[i] == ')':
            print(") detected")
            translated_string_equation += ')'
        elif string_equation[i] == 'a' and string_equation[i - 1] != 'v':
            print("and detected")
            i += 2
            translated_string_equation += '^'
        elif string_equation[i] == 'o' and string_equation[i - 1] != 'n':
            print("or detected")
            i += 1
            translated_string_equation += 'v'
        elif string_equation[i] == 'n' and string_equation[i - 1] != 'a' or string_equation[i] == 'n' and string_equation[i - 1] != 'e':
            print("not detected")
            i += 2
            translated_string_equation += '~'
        elif string_equation[i] == 'i' and string_equation[i - 1] != 'u':
            print("implies detected")
            i += 6
            translated_string_equation += '='
            translated_string_equation += '>'
        elif string_equation[i] == 'e' and string_equation[i - 1] != 'i':
            print("equals detected")
            i += 5
            translated_string_equation += '<'
            translated_string_equation += '='
            translated_string_equation += '>'

        i += 1
    return variable_used, translated_string_equation


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
        solve_value[i] = (not a[i]) or b[i]  # Logical implication (not a or b)
    return solve_value


def operator_equivalent(row, a, b):
    solve_value = [0] * row  # Initialize the result list with 0s
    for i in range(row):
        solve_value[i] = (a[i] == b[i])  # Check equivalence (a == b)
    return solve_value  # Return the list of results


def check_for_not_value(row, translated_string_equation, i, p, q, r, s):
    solve_value = [0] * row  # Initialize list with zeros of size `row`
    
    # Check for the variable following 'not'
    if translated_string_equation[i + 1] == 'p':
        for j in range(row):
            solve_value[j] = int(not p[j])  # Negate the value of p
    elif translated_string_equation[i + 1] == 'q':
        for j in range(row):
            solve_value[j] = int(not q[j])  # Negate the value of q
    elif translated_string_equation[i + 1] == 'r':
        for j in range(row):
            solve_value[j] = int(not r[j])  # Negate the value of r
    elif translated_string_equation[i + 1] == 's':
        for j in range(row):
            solve_value[j] = int(not s[j])  # Negate the value of s

    return solve_value  # Return the complete list after the loop


def store_values_inside_the_array(translated_string_equation, solve_value, string_solve, p, q, r, s):
    i = 0  # Index for traversing the string
    j = 0  # Index for traversing the solve_value list
    temp_string_equation = []  # Temp list to hold solved values and operators

    while i < len(translated_string_equation):
        if len(solve_value) > 0:
            j = len(string_solve) - 1
            i += 1
            while j > 0:
                # Check if the substring matches the current solve string in reverse order
                if translated_string_equation[i:i+2] == string_solve[j]:
                    temp_string_equation.append(solve_value[j])  # Append precomputed solution
                    i += len(string_solve[j]) + 2  # Skip the processed part and the '(' and the ')'
                    j -= 1  # Move to the previous solve value (in reverse  )
                    break  # Exit the loop once a match is found
                else:
                    j -= 1  # Keep moving left in string_solve if no match found
        # Check for opening parenthesis '('
        elif translated_string_equation[i] == '(':
            # Traverse string_solve from right to left to prioritize innermost expressions first
            temp_string_equation.append('(')  # Append '(' to the temp list
            i += 1
        # Check for closing parenthesis ')'
        elif translated_string_equation[i] == ')':
            temp_string_equation.append(')')
            i += 1
        # Check for variables (p, q, r, s) and append their values directly
        elif translated_string_equation[i] == 'p':
            temp_string_equation.append(p)
            i += 1
        elif translated_string_equation[i] == 'q':
            temp_string_equation.append(q)
            i += 1
        elif translated_string_equation[i] == 'r':
            temp_string_equation.append(r)
            i += 1
        elif translated_string_equation[i] == 's':
            temp_string_equation.append(s)
            i += 1

        # Check for operators ^ (and), v (or), => (implies), <=> (equivalence)
        elif translated_string_equation[i] == '^':
            temp_string_equation.append('^')  # Append 'and' operator
            i += 1
        elif translated_string_equation[i] == 'v':
            temp_string_equation.append('v')  # Append 'or' operator
            i += 1
        elif translated_string_equation[i:i+2] == '=>':
            temp_string_equation.append('=>')  # Append 'implies' operator
            i += 2
        elif translated_string_equation[i:i+3] == '<=>':
            temp_string_equation.append('<=>')  # Append 'equivalence' operator
            i += 3

        else:
            i += 1  # Move forward if no parenthesis, variable, or operator found

    return temp_string_equation


def assign_values_for_a_and_b(final_sring_equation, i):    
    a = final_sring_equation[i - 1]  # Assign values based on the previous character
    b = final_sring_equation[i + 1]  # Assign values based on the next character
    return a, b


def calculate_equation(row, string_length, value_of_the_equation):
    i = 0
    a = [0] * row
    b = [0] * row
    solve_value = []
    string_solve = value_of_the_equation

    while i < string_length:
        
        # Ensure 'i' is within the string's bounds to avoid IndexError
        if i >= len(value_of_the_equation):
            break
        
        # Handle 'AND' operation (^)
        if value_of_the_equation[i] == '^':
            a, b = assign_values_for_a_and_b(value_of_the_equation, i)
            solve_value = operator_and(row, a, b)
        
        # Handle 'OR' operation (v)
        elif value_of_the_equation[i] == 'v':
            a, b = assign_values_for_a_and_b(value_of_the_equation, i)
            solve_value = operator_or(row, a, b)
        
        # Handle 'NOT' operation (~)
        elif value_of_the_equation[i] == '~':
            solve_value = check_for_not_value(value_of_the_equation, i)

        # Handle 'IMPLIES' operation (=>), check if we have enough characters left in the string
        elif value_of_the_equation[i] == '=>' and (i + 1) < string_length:
            a, b = assign_values_for_a_and_b(value_of_the_equation, i)
            solve_value = operator_implies(row, a, b)
            i += 1  # Skip '>'
        
        # Handle 'EQUIVALENT' operation (<=>), check if we have enough characters left in the string
        elif value_of_the_equation[i] == '<=>' and (i + 2) < string_length:
            a, b = assign_values_for_a_and_b(value_of_the_equation, i)
            solve_value = operator_equivalent(row, a, b)
            i += 2  # Skip '=' and '>'

        # Move to the next character
        i += 1
    
    return solve_value, string_solve


def calculate_complex_equation (row, translated_string_equation, value_of_the_equation, string_solve, p, q, r, s):
    solve_value = []
    str_priority = []
    string_length = len(value_of_the_equation)
    while 1:
        i = 0
        if len(value_of_the_equation) == 1:
            return solve_value, string_solve
        if len(string_solve) > 0:
            value_of_the_equation = store_values_inside_the_array(value_of_the_equation, solve_value, string_solve, p, q, r, s)
            string_length = len(value_of_the_equation)
        while i < string_length:
            if value_of_the_equation[i] == '(':
                j = i
                while value_of_the_equation[j] != ')':
                    if value_of_the_equation[j] == '(':
                        i = j
                    j += 1
                value, str_priority = calculate_equation(row, j - i, value_of_the_equation[i + 1:j])
                solve_value.append(value)
                string_solve.append(str_priority)
                i = j
            elif len(value_of_the_equation) == 3:
                value, str_priority = calculate_equation(row, string_length, value_of_the_equation)
                solve_value.append(value)
                string_solve.append(str_priority)
            i += 1


def main ():
    row = 0
    col = 0
    variable_used = 0
    string_equation = "(p and q) implies (r or s)"
    translated_string_equation = ""
    solve_value = []
    string_solve = []
    p = [0] * row
    q = [0] * row
    r = [0] * row
    s = [0] * row

    # translate the string
    variable_used, translated_string_equation = translate(variable_used, string_equation, translated_string_equation)
    # calculate the dimensions
    row, col = calculate_dimensions(variable_used, row, col)
    # declare and initialize the matrix
    matrix = fill_matrix_with_binary_count(row, col)
    # assign values to the variables
    p, q, r, s = assign_values(row, variable_used, p, q, r, s, matrix)
    # create a array with stored values
    value_of_the_equation = store_values_inside_the_array(translated_string_equation, solve_value, string_solve, p, q, r, s)
    # calculate the equation
    solve_value, string_solve = calculate_complex_equation(row, translated_string_equation, value_of_the_equation, string_solve, p, q, r, s)



    # Debugger
    print("The string is: ", string_equation)
    print("Translated string: ", translated_string_equation)
    print("Variable Used: ", variable_used)
    print("Row: ", row)
    print("Col: ", col)
    # for row in matrix:
    #     print(row)
    print("P: ", p)
    print("Q: ", q)
    print("R: ", r)
    print("S: ", s)
    print("Translated string: ", translated_string_equation)
    print("Value equation: ", value_of_the_equation)
    print("Length of the value equation: ", len(value_of_the_equation))
    
    # Debugger


# Run the main function
if __name__ == "__main__":
    main()