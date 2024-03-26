class ExpressionNode:
    def evaluate(self):
        pass

class OperandNode(ExpressionNode):
    def __init__(self, value):
        self.value = value

    def evaluate(self):
        return self.value

class OperatorNode(ExpressionNode):
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right

    def evaluate(self):
        if self.operator == '+':
            return self.left.evaluate() + self.right.evaluate()
        elif self.operator == '-':
            return self.left.evaluate() - self.right.evaluate()
        elif self.operator == '*':
            return self.left.evaluate() * self.right.evaluate()
        elif self.operator == '/':
            return self.left.evaluate() / self.right.evaluate()
        else:
            raise ValueError("unknown")

# (5 + 3) * (2 - 1)
leftF_operand = OperandNode(5)
rightF_operand = OperandNode(3)
addition = OperatorNode('+', leftF_operand, rightF_operand)

leftS_operand = OperandNode(2)
rightS_operand = OperandNode(1)
subtraction = OperatorNode('-', leftS_operand, rightS_operand)

res = OperatorNode('*', addition, subtraction)

print(res.evaluate())
