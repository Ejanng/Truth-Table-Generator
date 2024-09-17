translate(variable_used, string_length, str_equation, final_str_equation):
### this function translate the str_equation (the equation to be solved) into mathematical or logical expression.
### countP, countQ, countR, countS; iterate to check how many varibales used. Without this iteration, in some cases if the str_equation = "(p and q) or p" the total variable is 3 because of (p, q, p). In my case, I want my program if there is a variable repeated it only count itself as one or iterate the variable_used which the outcome will be 2. 
### That's the use of countP, countQ, countR, countS varible. It will iterate itself and skip the if statement if the value is 1. And the detetected variable stored in final_str_equation.
### This function also check if there is a operator used, the operator to be stored in final_str_equation.
### The operator detect this following:
- and for ^
- or for v
- not for ~
- implies for =>
- equivalent for <=>
- and the prioritized variable which will be the first one to used which is "()" 
### The operator to be stored in final_str_equation if detected
### the program used while loop in order to manipulate the iteration of i.
### This function return two variable which is; variable_used and final_str_equation.


def calculate_dimensions(variable_used, row, col):
### This function calculate the dimensions of the matrix. The variable_used will be the basis of this matrix.
### The formula to create the matrix will be:
- col = variable_used
- row = 2^variable_used
### return the value of col and row


def fill_matrix_with_binary_count(row, col):
### This function create the matrix with the value of col and row, and start filling the values with 1 and 0, which indicate 1 as True and 0 as False
### For declaring the values I choose the formula for counting in binary which is more easier than declaring each value as True and False.
### return the value of matrix


def assign_values_to_variables(row, matrix, y):
### This function assign the values of the matrix into respective variable
### return the value of x


def assign_values(row, variable_used, p, q, r, s, matrix):
### This function detect how many variable is used and call the function assign_values_to_variable() to assign each variable
### For the values of first variable which located into matrix[][0] (or in col index 0) so on and so forth 
### return the value of p, q, r, s


def operator_and(row, a, b):
### This function calculate the two variable with the "and"  operator
### return value of solve_value


def operator_or(row, a, b):
### This function calculate the two variable with the "or"  operator
### return value of solve_value


def operator_implies(row, a, b):
### This function calculate the two variable with the "implies"  operator
### return value of solve_value


def operator_equivalent(row, a, b):
### This function calculate the two variable with the "equivalent"  operator
### return value of solve_value


def priority (final_str_equation, string_length, count):
# This function filter the equation, and store the


def check_for_not_value(row, final_str_equation, i, p, q, r, s):
### This function flip the value of x
### return value of solve_value

def assign_values_for_a_and_b(row, final_str_equation, i, p, q, r, s):
### This function assign the value of two variable to be calculated


def calculate_equation(row, string_length, final_str_equation, p, q, r, s):
### This function calculate the variables

def priority_equation_function(string_length, final_str_equation, values_of_priority_equation, count):
### This function filter the priority or the equation has "()"

def main ():
### This function contains that calls all functions and logic in order to create and calculate the Truth Table.


# Run the main function 
if __name__ == "__main__":
    main()
