class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        left  = 0
        token_length = len(tokens)
        prev = 0
        operators = {"+", "-", "*", "/"}
        evalStack = []
        while left < token_length:
            if tokens[left] not in operators:
                evalStack.append(float(tokens[left]))
                prev = tokens[left]
            else:
                a = evalStack.pop()
                b = evalStack.pop()
                match tokens[left]:
                    case "+":
                        prev = b + a
                    case "-":
                        prev = b - a
                    case "*":
                        prev = b * a
                    case "/":
                        prev = int(b / a)
                evalStack.append(prev)
                print(evalStack)
            left +=1
        return int(prev)
