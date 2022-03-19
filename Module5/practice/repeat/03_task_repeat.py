# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.

a = 11
b = 33

def palindrome(number):
    return str(number)[::-1] == str(number)

list_of_palindromes = []
for number in range (a, b+1):
    if palindrome(number):
        list_of_palindromes.append(number)

print(list_of_palindromes)
print(len(list_of_palindromes))
