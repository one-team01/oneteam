from . import add, minus, multiplication, division

def main():
    print("덧셈:", add(10, 2))
    print("뺄셈:", minus(10, 2))
    print("곱셈:", multiplication(10, 2))
    print("나눗셈:", division(10, 2))

if __name__ == "__main__":
    main()