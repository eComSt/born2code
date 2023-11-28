def count_vowels(string):
    vowels = "aeiou"
    count = 0
    for char in string.lower():
        if char in vowels:
            count += 1
    return count

# Пример использования функции
input_string = input("Введите строку: ")
vowel_count = count_vowels(input_string)
print(vowel_count)