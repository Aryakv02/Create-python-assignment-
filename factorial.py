def factorial_recursive(n):
  if n == 0:
    return 1
  else:
    return n * factorial_recursive(n - 1)

def factorial_iterative(n):
  if n == 0:
    return 1
  else:
    result = 1
    for i in range(1, n + 1):
      result *= i
    return result

def main():
  num = int(input("Enter an integer: "))

  if num < 0:
    print("Factorial is not defined for negative numbers.")
  else:
    recursive_result = factorial_recursive(num)
    iterative_result = factorial_iterative(num)

    print(f"Factorial of {num} using recursion: {recursive_result}")
    print(f"Factorial of {num} using iteration: {iterative_result}")

if __name__ == "__main__":
  main() 