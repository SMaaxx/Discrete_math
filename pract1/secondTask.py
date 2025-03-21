from math import comb

def get_winning_probability(N, K, M):
    # Общее количество способов выбрать K карточек
    total_combinations = comb(N, K)

    # Расчёт благоприятных исходов
    winning_combinations = 0
    for m in range(M, K + 1):
        # Использую comb() для расчета сочетаний
        match = comb(K, m)  # Совпадения
        non_match = comb(N - K, K - m)  # Несовпадения
        winning_combinations += match * non_match

    # Считаем и возвращаем вероятность в процентах c округлением до 4 цифр после запятой
    return round((winning_combinations / total_combinations) * 100, 4)

print(f"Вероятность выигрыша: {get_winning_probability(28, 10, 7)}%")