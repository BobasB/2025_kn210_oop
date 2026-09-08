def main():
    print("Hello, World!")

def check_passed_parameter(p: str = None):
    if p is None:
        return 0
    return 1


def count_passed_parameters(*args):
    return len(args)


if __name__ == "__main__":
    main()