class MainLab:
    """Клас MainLab є idempotent, тобто його методи не мають побічних ефектів."""
    GLOBALS = [1, 2, 3, 4, 5]
    def __init__(self):
        self.name = "Main Lab"

    def return_numbers(self):
        for number in self.GLOBALS:
            yield number

    def get_exeptions(self, i: int):
        """Метод для демонстрації обробки виключень."""
        if i < 0:
            raise ValueError("i must be non-negative")
        return self.GLOBALS[i]

def main():
    obj = MainLab()

if __name__ == "__main__":
    main()
