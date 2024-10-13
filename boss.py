

def translate(variable_used, string_equation, translated_string_equation):
    # Initialize the count of each variable
    countP = 0
    countQ = 0
    countR = 0
    countS = 0
    translations = []
    # Initialize the index
    i = 0
    while i < len(string_equation):
        # Check the character of the string
        if string_equation[i] == 'p':
            translations.append(("p", "p"))
            if countP == 0:
                variable_used += 1
                countP += 1
            translated_string_equation += 'p'
        elif string_equation[i] == 'q':
            translations.append(("q", "q"))
            if countQ == 0:
                variable_used += 1
                countQ += 1
            translated_string_equation += 'q'
        elif string_equation[i] == 'r':
            translations.append(("r", "r"))
            if countR == 0:
                variable_used += 1
                countR += 1
            translated_string_equation += 'r'
        elif string_equation[i] == 's':
            translations.append(("s", "s"))
            if countS == 0:
                variable_used += 1
                countS += 1
            translated_string_equation += 's'
        # Check the operator of the string
        elif string_equation[i] == '(':
            translations.append(("(", "("))
            translated_string_equation += '('
        elif string_equation[i] == ')':
            translations.append((")", ")"))
            translated_string_equation += ')'
        elif string_equation[i] == 'a' and string_equation[i - 1] != 'v':
            translations.append(("and", "^"))
            i += 2
            translated_string_equation += '^'
        elif string_equation[i] == 'o' and string_equation[i - 1] != 'n':
            translations.append(("or", "v"))
            i += 1
            translated_string_equation += 'v'
        elif string_equation[i] == 'n' and string_equation[i - 1] != 'a' or string_equation[i] == 'n' and string_equation[i - 1] != 'e':
            translations.append(("not", "~"))
            i += 2
            translated_string_equation += '~'
        elif string_equation[i] == 'i' and string_equation[i - 1] != 'u':
            translations.append(("implies", "=>"))
            i += 6
            translated_string_equation += '='
            translated_string_equation += '>'
        elif string_equation[i] == 'e' and string_equation[i - 1] != 'i':
            translations.append(("equivalent", "<=>"))
            i += 5
            translated_string_equation += '<'
            translated_string_equation += '='
            translated_string_equation += '>'
        i += 1
    # Printing the table header
    print(f"{'Symbol':<15} | {'Translation':<15}")
    print('-' * 35)  # Separator line
    
    # Print each translation
    for symbol, translation in translations:
        print(f"{symbol:<15} | {translation:<15}")

    print("\nEquation: ", translated_string_equation)
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
        solve_value[i] = int(not a[i]) or b[i]  # Logical implication (not a or b)
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


def store_values_inside_the_array(translated_string_equation, p, q, r, s):
    i = 0  # Index for traversing the string
    integer_equation = []  # Temp list to hold solved values and operators
    string_equation = []

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

    return integer_equation, string_equation


def assign_values_for_a_and_b(final_sring_equation, i):    
    a = final_sring_equation[i - 1]  # Assign values based on the previous character
    b = final_sring_equation[i + 1]  # Assign values based on the next character
    return a, b


def calculate_equation(row, string_length, integer_equation):
    i = 1
    a = [0] * row
    b = [0] * row
    solve_value = []

    while i < string_length:
        
        # Ensure 'i' is within the string's bounds to avoid IndexError
        if i >= len(integer_equation):
            break
        
        # Handle 'AND' operation (^)
        if integer_equation[i] == '^':
            a, b = assign_values_for_a_and_b(integer_equation, i)
            solve_value = operator_and(row, a, b)
        
        # Handle 'OR' operation (v)
        elif integer_equation[i] == 'v':
            a, b = assign_values_for_a_and_b(integer_equation, i)
            solve_value = operator_or(row, a, b)
        
        # Handle 'NOT' operation (~)
        elif integer_equation[i] == '~':
            solve_value = check_for_not_value(integer_equation, i)

        # Handle 'IMPLIES' operation (=>), check if we have enough characters left in the string
        elif integer_equation[i] == '=>' and (i + 1) < string_length:
            a, b = assign_values_for_a_and_b(integer_equation, i)
            solve_value = operator_implies(row, a, b)
            i += 1  # Skip '>'
        
        # Handle 'EQUIVALENT' operation (<=>), check if we have enough characters left in the string
        elif integer_equation[i] == '<=>' and (i + 2) < string_length:
            a, b = assign_values_for_a_and_b(integer_equation, i)
            solve_value = operator_equivalent(row, a, b)
            i += 2  # Skip '=' and '>'
        # Move to the next character
        i += 1
    
    return solve_value


def calculate_complex_equation (row, string_equation, integer_equation):
    solve_value = []
    string_priority = []
    k = 0
    l = 0
    m = 0
    operator = []
    temp_string_equation = []
    single_equation = []
    reset = []
    def remove_last_duplicates(array):
        # Reverse the array to start checking from the last element
        reversed_array = array[::-1]

        # Use an ordered set to track seen elements while preserving order
        seen = set()
        result = []

        for item in reversed_array:
            # Only add the item if it hasn't been seen yet
            if item not in seen:
                result.append(item)
                seen.add(item)

        # Reverse the result back to the original order (with last duplicates removed)
        return result[::1]
    
    while 1:
        string_length = len(integer_equation)
        i = 0
        while i < string_length:
            l = i
            found_open_parenthesis = False  # Flag to track if we found '('
            while string_equation[l] != ')':
                if l >= len(string_equation) - 1:
                    break
                if string_equation[l] == '(':
                    found_open_parenthesis = True  # Set the flag when '(' is found
                    i = l
                l += 1
            if found_open_parenthesis and i + 1 < l:  # Ensure there is something to append
                string_priority.append(string_equation[i + 1:l])
            cleaned_array = [x for x in string_priority if x]
            string_priority = cleaned_array
            string_priority = [tuple(x) if isinstance(x, list) else x for x in string_priority]
            unique_values = remove_last_duplicates(string_priority)
            # Check for the operator
            while k < string_length - 1:
                if integer_equation[k] == ')':
                    operator.append(integer_equation[k+1])
                k += 1
            # Check for the single equation after parenthesis
            while m < string_length:
                if m >= len(integer_equation) - 1:
                    break
                if integer_equation[m] == ')' and integer_equation[m+2] != '(':
                    single_equation.append(integer_equation[m+2])
                m += 1
            # Process the equation
            if integer_equation[i] == '(':
                j = i
                while integer_equation[j] != ')':
                    if integer_equation[j] == '(':
                        i = j
                    j += 1
                value = calculate_equation(row, j - i, integer_equation[i + 1:j])
                solve_value.append(value)
                temp_string_equation.append(value)
                value = reset
                if operator:
                    temp_string_equation.append(operator.pop(0))
                if single_equation:
                    temp_string_equation.append(single_equation.pop(0))
                i = j
            elif len(integer_equation) == 3:
                value = calculate_equation(row, string_length, integer_equation)
                solve_value.append(value)
                temp_string_equation = reset
                temp_string_equation.append(value)
                value = reset
                integer_equation = temp_string_equation
                string_priority = [' '.join(item) for item in unique_values]
                return solve_value, string_priority, integer_equation
            i += 1
        integer_equation = temp_string_equation


def display_truth_table(propositions, translated_string, value_equation, solve_value, string_solve):
    # Create a filtered version of propositions
    filtered_props = {k: v for k, v in propositions.items() if len(v) > 0}

    # Check if filtered_props is empty
    if not filtered_props:
        print("No valid propositions to display.")
        return

    # Extract filtered proposition names and their values
    prop_names = list(filtered_props.keys())
    prop_values = list(filtered_props.values())

    # Length of the value columns
    num_rows = len(prop_values[0]) if prop_values else 0

    # Prepare the header including the intermediate steps and the final equation
    header = prop_names + (string_solve if string_solve else ['']) + [translated_string]
    header_str = " | ".join(header)
    print(header_str)
    print("-" * len(header_str))  # Separator line

    # Calculate maximum length for each column for alignment
    col_widths = [max(len(str(val)) for val in col) for col in zip(*prop_values)]
    max_string_solve_length = max(len(s) for s in string_solve) if string_solve else len('None')
    col_widths.append(max_string_solve_length)  # Width for string_solve
    col_widths.append(15)  # Width for Final Equation

    # Display each row of values, including the intermediate and final values
    for i in range(num_rows):
        # Gather the truth values for the propositions in the current row
        row_values = [str(prop[i]).ljust(col_widths[j]) for j, prop in enumerate(prop_values)]

        # Add the corresponding intermediate values (from solve_value)
        intermediate_values = [str(solve[i]).ljust(col_widths[-2]) for solve in solve_value]

        # Add the final result of the equation

        # final_value = str(value_equation[0][i]).ljust(col_widths[-1])

        # Combine all row values
        row_values.extend(intermediate_values)
        # row_values.append(final_value)

        # Print the aligned row
        print(" | ".join(row_values))


def main ():
    row = 0
    col = 0
    variable_used = 0
    string_equation = "(p implies q) or r"
    translated_string_equation = ""
    solve_value = []
    string_priority = []
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
    propositions = {'P': p, 'Q': q, 'R': r, 'S': s}
    # create a array with stored values
    integer_equation, string_equation = store_values_inside_the_array(translated_string_equation, p, q, r, s)
    # calculate the equation
    solve_value, string_priority, value_of_the_equation = calculate_complex_equation(row, string_equation, integer_equation)
    display_truth_table(propositions, translated_string_equation, value_of_the_equation, solve_value, string_priority)



    # # Debugger
    # print("The string is: ", string_equation)
    # print("Translated string: ", translated_string_equation)
    # print("Variable Used: ", variable_used)
    # print("Row: ", row)
    # print("Col: ", col)
    # # for row in matrix:
    # #     print(row)
    # print("P: ", p)
    # print("Q: ", q)
    # print("R: ", r)
    # print("S: ", s)
    # print("Translated string: ", translated_string_equation)
    # print("Value equation: ", value_of_the_equation)
    # print("Length of the value equation: ", len(value_of_the_equation))
    # print("Solve value: ", solve_value)
    # print("String Solve: ", string_priority)
    # print("Value of the equation: ", value_of_the_equation)
    
    # Debugger


# Run the main function
if __name__ == "__main__":
    main()