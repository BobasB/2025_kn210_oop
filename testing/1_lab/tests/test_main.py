from lab_main import main

print(f"{'='*10} Тестування функції main() =======")
assert main() is None, "Функція main() повинна повертати None"
assert callable(main), "main має бути викликабельним"
print("Тестування функції main() завершено успішно!")
