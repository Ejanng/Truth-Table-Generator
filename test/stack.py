import copy

class Stack:
    def stack_list(self, stack):
        if len(stack) == 0:
            return None
        temp = copy.deepcopy(stack)
        stack.clear()
        operators = ['^', 'v', '=>', '<=>']
        par = []
        op = []
        op_count = 0
        i = 0
        while i < len(temp):
            if i > len(temp) - 1:
                break
            
            if temp[i] == '(':
                par.append(temp[i])
                if i > 0 and temp[i-1] == '~':
                    par.append(temp[i-1])
                if temp[i+1] == '(':
                    i += 1
                    continue
            elif temp[i] in operators:
                if i + 1 < len(temp) and temp[i + 1] == '(':
                    i += 1
                    continue
                if i + 2 < len(temp) and temp[i + 2] in operators:
                    stack.append(temp[i-1])
                    op.append(temp[i])
                    op_count += 1
                    i += 1
                    continue
                if i > 1 and temp[i-2] == '~':
                    stack.append(temp[i-1])
                    stack.append(temp[i-2])
                else:
                    stack.append(temp[i-1])
                if temp[i+1] == '~':
                    stack.append(temp[i+2])
                    stack.append(temp[i+1])
                else:
                    if temp[i+1] != '(':
                        stack.append(temp[i+1])
                    for i in range(op_count):
                        stack.append(op.pop())
                    op_count = 0
                stack.append(temp[i])
            elif temp[i] == ')':
                if par[-1] == '~':
                    stack.append(par.pop())
                par.pop()
            i += 1

        return stack