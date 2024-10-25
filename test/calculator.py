import os  # Import the os module
import sys  # Import the sys module

class Calculator:
    def operator_and(self, row, a, b):
        solve_value = [0] * row
        for i in range(row):
            solve_value[i] = a[i] and b[i]
        return solve_value

    def operator_or(self, row, a, b):
        solve_value = [0] * row
        for i in range(row):
            solve_value[i] = a[i] or b[i]
        return solve_value

    def operator_implies(self, row, a, b):
        solve_value = [0] * row
        for i in range(row):
            solve_value[i] = int(not a[i]) or b[i]
        return solve_value

    def operator_equivalent(self, row, a, b):
        solve_value = [0] * row
        for i in range(row):
            solve_value[i] = int(a[i] == b[i])
        return solve_value

    def calculate_dimensions(self, variable_used):
        if variable_used < 1:
            os.system('cls')  # Clear the console
            print("Error: There is no variable used!")
            print("Note: Variable must be p, q, r, s only!")
            sys.exit(1)

        holder = 2
        for i in range(variable_used - 1):
            holder *= 2
        
        row = holder
        col = variable_used
        return row, col
