import ast

def evaluate_set_expression(file_path):
    # Читаем файл
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    # Проверка на пустой файл
    if not lines:
        raise ValueError("Файл пуст")

    # Парсим выражение и заменяем операторы для оператора eval
    expression = lines[0]
    operators = {'∪': '|', '∆': '^', '\\': '-', '∩': '&'}
    for old, new in operators.items():
        expression = expression.replace(old, new)

    # Создаем словарь множеств
    sets = {}
    for line in lines[1:]:
        name, values = line.split('=', 1)
        # использем ast для преобразования строки в множество
        sets[name.strip()] = ast.literal_eval(values.strip())

    # Вычисляем результат
    try:
        return eval(expression, {}, sets)
    except NameError as e:
        raise ValueError(f"Неопределенное множество: {e}") from e

firstAns = evaluate_set_expression('A.txt')
secondAns = evaluate_set_expression('B.txt')

print(f"Ответ для выражения 1: {evaluate_set_expression('A.txt')}\n")
print(f"Ответ для выражения 2: {evaluate_set_expression('B.txt')}")