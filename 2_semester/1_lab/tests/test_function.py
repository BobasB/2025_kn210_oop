from lab_main import check_passed_parameter

print(f"{'='*10} Тестування функції check_passed_parameter() =======")

if check_passed_parameter() == 0:
    print("Функція check_passed_parameter() повертає 0, коли параметр не переданий")
elif check_passed_parameter("pass") == 1:
    print("Функція check_passed_parameter() повертає 1, коли параметр переданий")
else:
    raise AssertionError("Функція check_passed_parameter() повертає неправильне значення")