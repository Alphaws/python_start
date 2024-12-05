def main():
    number = int(input("Adj meg egy egész számot: "))
    print(f"A szám hossza: {len(str(number))}")

def number_length_without_len(number):
    count = 0
    while number > 0:
        number //= 10
        count += 1
    return count

if __name__ == "__main__":
    main()
    print(number_length_without_len(1234567890))
