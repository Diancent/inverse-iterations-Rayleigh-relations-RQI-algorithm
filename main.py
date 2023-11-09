import numpy as np

def make_symmetric(matrix):
    return 0.5 * (matrix + matrix.T)

def power_rayleigh(a, mu, b, number_itr, tolerance=1e-6):
    I = np.eye(len(a[0]))

    for k in range(number_itr):
        t = a - mu * I
        try:
            b = np.linalg.solve(t, b)
        except np.linalg.LinAlgError:
            print("Матриця сингулярна, збіжність до:")
            return mu, b

        b /= np.linalg.norm(b)

        s = np.dot(a, b)
        mu = np.dot(s, b) / np.dot(b, b)

        # Перевірка на збіжність
        if np.abs(np.linalg.norm(mu) - np.linalg.norm(mu)) > 1e5:
            break

    print("Зійшовся до:")
    return np.abs(mu), b


def read_matrix_from_file(filename):
    matrix = np.loadtxt(filename)
    return matrix


if __name__ == "__main__":
    filename = "matrix_input.txt"

    matrix = read_matrix_from_file(filename)
    symmetric_matrix = make_symmetric(matrix)

    # Ініціалізація початкового вектора
    initial_vector = np.random.rand(len(matrix[0]))

    # Визначення параметрів для методу зворотніх ітерацій
    mu = 0.0  # Початкове наближене власне число
    number_of_iterations = 1000  # Кількість ітерацій

    # Запуск методу зворотніх ітерацій
    eigenvalue, eigenvector = power_rayleigh(symmetric_matrix, mu, initial_vector, number_of_iterations)

    eigenvalue_np, eigenvector_np = np.linalg.eig(matrix)

    print("Найменше за модулем власне число np:", eigenvalue_np)
    print("Відповідний власний вектор np:", eigenvector_np)
    print("Найменше за модулем власне число:", eigenvalue)
    print("Відповідний власний вектор:", eigenvector)
