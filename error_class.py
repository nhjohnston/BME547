a = "The sky is blue"
print(a)


def calc_square_root(n):
    from math import sqrt
    answer = sqrt(n)
    return answer


def main():
    try:
        calc_square_root(4)
    except ModuleNotFoundError:
        print("My_calculator module not available.  Using default")


if __name__ == "__main__":
    main()
