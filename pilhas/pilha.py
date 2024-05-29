class Pilha:
    def __init__(self) -> None:
        self.pilha = []

    def __str__(self) -> str:
        return f"{self.pilha}"

    def push(self, value):
        self.pilha.append(value)

    def pop(self):
        if not self.empty():
            self.pilha.pop()
        else:
            raise Exception("Pilha vazia!")

    def top(self):
        if not self.empty():
            return self.pilha[-1]
        raise Exception("Pilha vazia!")

    def empty(self):
        return False if self.pilha else True

    def lenght(self):
        return len(self.pilha)

    def delete(self):
        self.pilha = []


if __name__ == "__main__":
    stack = Pilha()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack)
    assert stack.empty() == False
    assert stack.lenght() == 3
    stack.pop()
    assert stack.lenght() == 2
    stack.delete()
    assert stack.empty() == True
