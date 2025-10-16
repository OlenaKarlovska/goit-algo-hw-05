import timeit

# Алгоритм Боєра–Мура

def boyer_moore_search(text, pattern):
    m = len(pattern)
    n = len(text)
    if m == 0:
        return 0
    skip = {}
    for k in range(m - 1):
        skip[pattern[k]] = m - k - 1
    i = m - 1
    while i < n:
        j = m - 1
        k = i
        while j >= 0 and text[k] == pattern[j]:
            j -= 1
            k -= 1
        if j == -1:
            return k + 1
        i += skip.get(text[i], m)
    return -1

# Алгоритм Кнута–Морріса–Пратта

def kmp_search(text, pattern):
    n, m = len(text), len(pattern)
    if m == 0:
        return 0
    lps = [0] * m
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    i = j = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return i - j
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

# Алгоритм Рабіна–Карпа

def rabin_karp_search(text, pattern, d=256, q=101): 
    n = len(text)
    m = len(pattern)
    if m == 0:
        return 0
    h = pow(d, m - 1) % q
    p = 0 
    t = 0 
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    for s in range(n - m + 1):
        if p == t:
            if text[s:s + m] == pattern:
                return s
        if s < n - m:
            t = (d * (t - ord(text[s]) * h) + ord(text[s + m])) % q
            if t < 0:
                t += q
    return -1

# Тестування та порівняння часу

def measure_algorithms(text, pattern):
    algorithms = {
        "Боєр–Мур": lambda: boyer_moore_search(text, pattern),
        "Кнут–Морріс–Пратт": lambda: kmp_search(text, pattern),
        "Рабін–Карп": lambda: rabin_karp_search(text, pattern)}
    results = {}
    for name, func in algorithms.items():
        t = timeit.timeit(func, number=10)
        results[name] = t
    return results

# Bикористання
def read_file(filename, code='UTF-8'):
    with open(filename, 'r', code) as f:
        return f.read()

if __name__ == "__main__":
    # Завантаження текстів з файлів
    text1 = read_file(r"C:\Users\Rui\Desktop\Basic Algorithms and Data Structures\tema5\statia1.txt", code="cp1251")
    print(text1)
    text2 = read_file(r"C:\Users\Rui\Desktop\Basic Algorithms and Data Structures\tema5\statia2.txt", code = "utf-8-sig")
    print(text2)
    print(text2)

    existing_substring = "наука"
    non_existing_substring = "jriugsffwepso"

    print("****** Стаття 1 *****")
    print("Існуючий підрядок:")
    print(measure_algorithms(text1, existing_substring))
    print("Вигаданий підрядок:")
    print(measure_algorithms(text1, non_existing_substring))

    print("\n****** Стаття 2 *****")
    print("Існуючий підрядок:")
    print(measure_algorithms(text2, existing_substring))
    print("Вигаданий підрядок:")
    print(measure_algorithms(text2, non_existing_substring))

