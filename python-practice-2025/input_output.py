def main():
    n = int(input("How many numbers you want to enter: "))
    print(f"Please enter {n} numbers")

    arr = []
    for i in range(1, n + 1):
        enter_number = int(input("Please enter number: "))
        arr.append(enter_number)

    print(arr)

if __name__ == "__main__":
    main()
