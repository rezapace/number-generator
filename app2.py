import concurrent.futures

def generate_number(current_number, text_after):
    if current_number.is_integer():
        return f"{int(current_number)}{text_after}"
    else:
        return f"{current_number}{text_after}"

def generate_numbers():
    first_number = float(input("Enter the first number: "))
    last_number = float(input("Enter the last number: "))
    step = float(input("Enter the step (difference between consecutive numbers): "))
    text_after = input("Enter the text to add after each number: ")

    numbers = []
    current_number = first_number
    while current_number <= last_number:
        numbers.append(current_number)
        current_number += step

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(generate_number, numbers, [text_after]*len(numbers))

    return list(results)

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