"""
Convert Numbers Program: Mariana Gonzalez Bravo A01630948
"""
import sys
import time

def convert_binary(number):
    """Converts from decimal to binary with 10 bits"""
    if number == 0:
        return '0' * 10

    is_negative = False
    if number < 0:
        is_negative = True
        number = abs(number)

    binary_result = ''
    while number > 0:
        remainder = number % 2
        binary_result = str(remainder) + binary_result
        number = number // 2

    # Ensure the binary result has exactly 10 bits
    binary_result = binary_result.zfill(10)

    if is_negative:
        # Calculate 2's complement
        binary_result = ''.join('1' if bit == '0' else '0' for bit in binary_result)
        binary_result = bin_add(binary_result, '1')

    return binary_result

def bin_add(a, b):
    """Binary addition"""
    result = ''
    carry = 0

    a = list(a)
    b = list(b)

    while a or b or carry:
        bit_a = int(a.pop()) if a else 0
        bit_b = int(b.pop()) if b else 0

        total = bit_a + bit_b + carry
        result = str(total % 2) + result
        carry = total // 2

    return result

def convert_hex(number):
    """Converts from decimal to hexadecimal with 10 characters"""
    hex_chars = "0123456789ABCDEF"

    if number == 0:
        return '0' * 10
    is_negative = False
    if number < 0:
        is_negative = True
        number = abs(number)
    hex_result = ''
    while number > 0:
        remainder = number % 16
        hex_result = hex_chars[remainder] + hex_result
        number = number // 16

    # Ensure the hex result has exactly 10 characters
    hex_result = hex_result.zfill(9)[:10].upper()

    if is_negative:
        # Calculate 2's complement
        hex_result = ''.join(hex_chars[15 - hex_chars.index(char)] for char in hex_result)
        hex_result = hex_add(hex_result, '1')

    return hex_result

def hex_add(a, b):
    """Hexadecimal addition"""
    hex_chars = "0123456789ABCDEF"
    result = ''
    carry = 0
    a = list(a)
    b = list(b)
    while a or b or carry:
        char_a = int(a.pop(), 16) if a else 0
        char_b = int(b.pop(), 16) if b else 0
        total = char_a + char_b + carry
        result = hex_chars[total % 16] + result
        carry = total // 16
    return result.upper()

def process_file(file_path):
    """Process file and delivers the results"""
    binary_hex_results = []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    number = int(line.strip())
                    binary = convert_binary(number)
                    hexa = convert_hex(number)
                    binary_hex_results.append((number, binary, hexa))
                except ValueError:
                    print(f"Valor invalido: {line.strip()}")

    except FileNotFoundError:
        print("Error: No se encuentra el archivo")
        sys.exit(1)

    return binary_hex_results

def main():
    """Main function"""
    if len(sys.argv) != 2:
        sys.exit(1)

    file_path = sys.argv[1]

    file_name_without_extension = file_path.split('.')[0]

    start_time = time.time()

    results = process_file(file_path)

    end_time = time.time()
    elapsed_time = end_time - start_time

    output_file_path = f"{file_name_without_extension}Results.txt"

    with open(output_file_path, 'w', encoding='utf-8') as results_file:
        for result in results:
            decimal_str = f"Decimal: {result[0]:<20}"
            binary_str = f"Binary: {result[1]:<30}"
            hex_str = f"Hexadecimal: {result[2]:<10}"

            print(decimal_str, binary_str, hex_str)
            results_file.write(decimal_str + binary_str + hex_str + "\n")

        print(f"Execution time: {elapsed_time} seconds")
        results_file.write(f"Execution time: {elapsed_time} seconds\n")

if __name__ == "__main__":
    main()
