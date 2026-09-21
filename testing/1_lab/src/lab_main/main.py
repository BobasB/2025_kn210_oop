def check_passed_parameter(p: str = None):
    if p is None:
        return 0
    return 1


def get_input_from_user():
    user_input = input("Введіть будь-що: ")
    return user_input

def doing_api_call_to_external_system():
    """
    Імітуємо виклик до зовнішньої системи.
    """
    # Тут можна додати код для виклику API, наприклад, використовуючи requests або іншу бібліотеку.
    # Для прикладу, просто повернемо фіктивний результат.
    return {"status": "success", "data": "Результат від зовнішньої системи"}


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

def main():
    print("Hello, World!")
    print(get_input_from_user())

if __name__ == "__main__":
    main()
