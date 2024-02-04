"""
Compute Statistics Program: Mariana Gonzalez Bravo A01630948
"""
import sys
import time

def read_file(file_path):
    """
    Lee un archivo, muestra si los archivos tienen errores, y regresa una lista de números.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = [float(line.strip()) for line in file if line.strip()]
            if not data:
                print("Error: El archivo esta vacio")
                return None
        return data
    except FileNotFoundError as e:
        print(f"Error: No se puede encontrar el archivo '{file_path}'  {e}")
        return None
    except ValueError as e:
        print(f"Error: El archivo contiene valores no validos:\n{e}")
        return None

def mean_func(data):
    """
    Calcula la media de la lista de datos.
    """
    mean = sum(data) / len(data)
    return mean

def median_func(data):
    """
    Calcula la mediana de la lista de datos.
    """
    if not data:
        return 'La lista está vacía'

    sorted_data = sorted(data)
    mid = len(sorted_data) // 2
    # Si el Número de datos es par, obtener el promedio de los dos números medios
    if len(sorted_data) % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    return sorted_data[mid]

def mode_func(data):
    """
    Calcula la moda de la lista de datos.
    """
    counter = {}
    for num in data:
        if num in counter:
            counter[num] += 1
        else:
            counter[num] = 1

    # Encontrar los números con la frecuencia máxima
    counter_max = max(counter.values())

    #Verificar si no hay moda
    if counter_max == 1:
        return "No hay moda, todos los números son diferentes."

    mode_numbers = [num for num, freq in counter.items() if freq == counter_max]

    return mode_numbers

def standard_deviation_func(data, mean):
    """
    Calcula la desviacion estandar de la lista de datos.
    """
    n = len(data)
    deviation = [(x - mean) ** 2 for x in data]
    variance = sum(deviation) / n
    return variance ** 0.5

def variance_func(data, mean):
    """
    Calcula la varianza de la lista de datos.
    """
    n = len(data)
    deviation = [(x - mean) ** 2 for x in data]
    return sum(deviation) / n

def main():
    """
    Ejecuta el programa
    """
    if len(sys.argv) != 2:
        print("Uso: python computeStatistics.py fileWithData.txt")
        sys.exit(1)

    file_path = sys.argv[1]

    # Obtén el nombre del archivo sin la extensión
    file_name_without_extension = file_path.split('.')[0]

    start_time = time.time()

    data = read_file(file_path)

    if data is not None:
        mean = mean_func(data)
        median = median_func(data)
        mode = mode_func(data)
        std_deviation = standard_deviation_func(data, mean)
        variance = variance_func(data, mean)

        if isinstance(mode, list):  # Verifica si mode es una lista
            formatted_mode = ", ".join([f"{round(value, 2)}" for value in mode])
        else:
            formatted_mode = mode

        print(f"Mean: {mean:.2f}")
        print(f"Median: {median:.2f}")
        print(f"Mode: {formatted_mode}")
        print(f"Standard Deviation: {std_deviation:.2f}")
        print(f"Variance: {variance:.2f}")

        output_file_path = f"{file_name_without_extension}Result.txt"

        with open(output_file_path, 'w', encoding='utf-8') as result_file:
            result_file.write(f"Mean: {mean:.2f}\n")
            result_file.write(f"Median: {median:.2f}\n")
            result_file.write(f"Mode: {formatted_mode}\n")
            result_file.write(f"Standard Deviation: {std_deviation:.2f}\n")
            result_file.write(f"Variance: {variance:.2f}\n")

        end_time = time.time()
        elapsed_time = end_time - start_time

        print(f"Time elapsed: {elapsed_time} seconds")

        with open(output_file_path, 'a', encoding='utf-8') as result_file:
            result_file.write(f"Time elapsed: {elapsed_time} seconds\n")

if __name__ == "__main__":
    main()
