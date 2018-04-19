class Printer:
    def __init__(self, _str):
        self.str = _str

    def print(self):
        for i in self.str:
            b = 2 +3
            print(i)


if __name__ == "__main__":
    p = Printer("Printer vasily number 112.3")
    p.print()
