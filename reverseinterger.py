#Write a program that takes an integer as input and returns an integer with reversed digit  ordering.
def reverse_integer(n):
    reversed_num = 0
    while n > 0:
        remainder = n % 10
        reversed_num = reversed_num * 10 + remainder
        n = n // 10
    return reversed_num

def main():
    user_integer = int(input("Enter an integer: "))
    reversed_integer = reverse_integer(user_integer)
    print("Reversed integer:", reversed_integer)


if __name__ == "__main__":
    main()
#writes the reverse of the interger one inputs
