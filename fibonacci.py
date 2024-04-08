#Write a program to generate the Fibonacci sequence up to 100.
def generate_fibonacci_sequence(limit):
    fib_sequence = [0, 1]
    while fib_sequence[-1] + fib_sequence[-2] <= limit:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def main():
    limit = 100
    fibonacci_sequence = generate_fibonacci_sequence(limit)
    print("Fibonacci sequence up to 100:", fibonacci_sequence)

if __name__ == "__main__":
    main()

