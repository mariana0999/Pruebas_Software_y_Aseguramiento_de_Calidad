"""
Word Count Program: Mariana Gonzalez Bravo A01630948
"""
import sys
import time

def process_file(file_path):
    """
    Cuenta cuantas veces se repite cada palabra
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            words = file.read().split()
    except FileNotFoundError:
        print("Error: No se encuentra el archivo")
        sys.exit(1)

    word_count = {}
    for word in words:
        clean_word = ''.join(char.lower() for char in word if char.isalnum())
        if clean_word:
            word_count[clean_word] = word_count.get(clean_word, 0) + 1

    return word_count

def main():
    """
    Funcion principal
    """
    if len(sys.argv) != 2:
        print("Usage: python wordCount.py fileWithData.txt")
        sys.exit(1)

    file_path = sys.argv[1]

    # Obtén el nombre del archivo sin la extensión
    file_name_without_extension = file_path.split('.')[0]

    start_time = time.time()

    word_count_results = process_file(file_path)

    end_time = time.time()
    elapsed_time = end_time - start_time

    output_file_path = f"{file_name_without_extension}Result.txt"

    with open(output_file_path, 'w', encoding='utf-8') as results_file:
        for word, count in word_count_results.items():
            print(f"Word: {word:<20} Frequency: {count}")
            results_file.write(f"Word: {word:<20} Frequency: {count}\n")

        print(f"Execution time: {elapsed_time:.4f} seconds")
        results_file.write(f"Execution time: {elapsed_time:.4f} seconds\n")

if __name__ == "__main__":
    main()
