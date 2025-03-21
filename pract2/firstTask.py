def find_infinite_depressed(file_path):
    with open(file_path, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    n = int(lines[0])
    matrix = [list(map(int, line.split())) for line in lines[1:n + 1]]

    # Определяем вложенную функцию dfs для поиска в глубину
    def dfs(vertex, start, visited, path, teacher_mood):
        # Проверяем, что текущий путь замкнут (начальная и конечная вершины совпадают)
        if len(path) > 1 and vertex == start:
            # Проверяем, что настроение убывает и все вершины в пути уникальны
            return teacher_mood < 0 and len(path) - 1 == len(set(path)) # - 1 т.к. в пути повторяется 1-ый элемент 

        # Перебираем варианты следующих вершин
        for next_vertex in range(n):
            # Проверяем, что следующая вершина еще не посещена или что она является начальной вершиной и путь замкнут
            if next_vertex not in visited or (len(path) > 1 and next_vertex == start):
                # Добавляем следующую вершину в посещенные и в путь
                path.append(next_vertex)
                visited.add(next_vertex)

                # Рекурсивно вызываем dfs для следующей вершины, обновляя сумму весов ребер
                if dfs(next_vertex, start, visited, path, teacher_mood + matrix[vertex][next_vertex]):
                    return True  # Если найдена бесконечно унылая последовательность

                path.pop()  # Удаляем последнюю вершину из пути (возврат)
                visited.remove(next_vertex)  # Удаляем последнюю вершину из множества посещенных (возврат)

        return False  # Если замкнутый путь с убывающей суммой весов не найден, возвращаем False

    # Перебираем все возможные начальные вершины
    for item in range(n):
        # Добавляем первую вершину в мн-во посещенных вершин и путь
        visited = {item}
        path = [item]

        # Вызываем dfs для начальной вершины
        if dfs(item, item, visited, path, 0):
            # Если найден замкнутый путь с убывающей суммой весов, выводим его длину и вершины (с индексацией, начиная с 1)
            print(f"Длина найденного пути = {len(path)} \nСписок вершин в найденном пути = {[item + 1 for item in path]}")
            return

    print("Пути, удовлетворяющего условиям не найдено") # Если не нашли последовательность

find_infinite_depressed("25_1.txt")
