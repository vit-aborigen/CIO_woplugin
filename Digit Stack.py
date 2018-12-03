class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        return 0

    def peek(self):
        if self.stack:
            return self.stack[-1]
        return 0

def digit_stack(commands):
    stack = Stack()
    result = 0
    for command in commands:
        if command == 'POP':
            result += stack.pop()
        elif command == 'PEEK':
            result += stack.peek()
        elif command.startswith('PUSH'):
            stack.push(int(command.split()[1]))
    return result


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK",
                        "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]) == 8, "Example"
    assert digit_stack(["POP", "POP"]) == 0, "pop, pop, zero"
    assert digit_stack(["PUSH 9", "PUSH 9", "POP"]) == 9, "Push the button"
    assert digit_stack([]) == 0, "Nothing"