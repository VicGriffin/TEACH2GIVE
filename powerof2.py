#Write a program that takes an integer as input and returns true if the input is a power of two.
def is_power_of_two(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0

def main():
    user_integer = int(input("Enter an integer: "))
    if is_power_of_two(user_integer):
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    main()
