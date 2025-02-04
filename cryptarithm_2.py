from itertools import permutations

def solve_cryptarithm(input1: str, input2: str, result: str):
    # Gabungkan semua huruf unik dari input
    unique_chars = set(input1 + input2 + result)
    if len(unique_chars) > 10:
        print("Terlalu banyak karakter unik!")
        return

    # Buat pemetaan kemungkinan angka untuk huruf
    for perm in permutations(range(10), len(unique_chars)):
        char_to_digit = dict(zip(unique_chars, perm))

        # Pastikan tidak ada leading zero
        if char_to_digit[input1[0]] == 0 or char_to_digit[input2[0]] == 0:
            continue

        # Konversi huruf ke angka berdasarkan pemetaan
        num1 = int("".join(str(char_to_digit[c]) for c in input1))
        num2 = int("".join(str(char_to_digit[c]) for c in input2))
        sum_result = int("".join(str(char_to_digit[c]) for c in result))

        # Periksa apakah penjumlahan sesuai
        if num1 + num2 == sum_result:
            print(f"{num1} + {num2} = {sum_result}")


# Contoh penggunaan
input1 = input("Enter the first letter: ")
input2 = input("Enter the second letter: ")
result = input("Enter the result: ")
solve_cryptarithm(input1, input2, result)
