import itertools

def is_isomorphic(matrix1, matrix2):
    matrix_len = len(matrix1)

    if matrix_len != len(matrix2):
        return False

    # Функция для получения отсортированных списков степеней вершин
    def get_degrees(matrix):
        return sorted(sum(row) for row in matrix)

    # Проверка на соответствие степеней вершин
    if get_degrees(matrix1) != get_degrees(matrix2):
        return False

    # Перебор перестановок
    for perm in itertools.permutations(range(matrix_len)):
        # Перестановка строк
        permuted_rows = [matrix1[i] for i in perm]
        # Перестановка столбцов в каждой строке
        permuted_matrix = [[row[j] for j in perm] for row in permuted_rows]

        # Проверка совпадения матриц
        if permuted_matrix == matrix2:
            return True

    return False


def check_isomorphism(file_path):
    # Считываем и парсим файл
    with open(file_path, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    n = int(lines[0])
    matrix1 = [list(map(int, line.split())) for line in lines[1:n + 1]]
    matrix2 = [list(map(int, line.split())) for line in lines[n + 1:2 * n + 1]]

    return is_isomorphic(matrix1, matrix2)


result = check_isomorphism('25_2.txt')
print(f"{'Да' if result else 'Нет'}")
