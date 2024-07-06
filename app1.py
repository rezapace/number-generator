def generate_numbers():
    first_number = float(input("Enter the first number: "))
    last_number = float(input("Enter the last number: "))
    step = float(input("Enter the step (difference between consecutive numbers): "))
    text_after = input("Enter the text to add after each number: ")

    numbers = []
    current_number = first_number
    while current_number <= last_number:
        # Check if the number is an integer, and format accordingly
        if current_number.is_integer():
            numbers.append(f"{int(current_number)}{text_after}")
        else:
            numbers.append(f"{current_number}{text_after}")
        current_number += step

    return numbers

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
