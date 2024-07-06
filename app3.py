import cupy as cp

def generate_numbers():
    first_number = float(input("Enter the first number: "))
    last_number = float(input("Enter the last number: "))
    step = float(input("Enter the step (difference between consecutive numbers): "))
    text_after = input("Enter the text to add after each number: ")

    # Create an array of numbers using CuPy
    num_elements = int((last_number - first_number) / step) + 1
    numbers = cp.arange(first_number, first_number + num_elements * step, step)
    
    # Format the numbers
    formatted_numbers = []
    for number in cp.asnumpy(numbers):
        if number.is_integer():
            formatted_numbers.append(f"{int(number)}{text_after}")
        else:
            formatted_numbers.append(f"{number}{text_after}")

    return formatted_numbers

def save_to_file(numbers):
    with open("output.txt", "w") as file:
        for number in numbers:
            file.write(number + "\n")

def main():
    generated_numbers = generate_numbers()
    save_to_file(generated_numbers)
    print("The numbers have been saved to output.txt")

if __name__ == "__main__":
    main()
