def main():
    print("Hello, World!")

def check_passed_parameter(p: str = None):
    if p is None:
        return 0
    return 1


def count_passed_parameters(*args):
    return len(args)

class MainLab:
    """Клас MainLab є idempotent, тобто його методи не мають побічних ефектів."""
    GLOBALS = [1, 2, 3, 4, 5]
    def __init__(self):
        self.name = "Main Lab"

    def return_numbers(self):
        for number in self.GLOBALS:
            yield number


if __name__ == "__main__":
    main()
