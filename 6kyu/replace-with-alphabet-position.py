def alphabet_position(text):
    numbers = []
    for letter in text:
        if(letter.isalpha()):
            if(letter.isupper()):
                numbers.append(str(ord(letter) - 64))
            else:
                numbers.append(str(ord(letter) - 96))
    return ' '.join(numbers)


first = alphabet_position("The sunset sets at twelve o' clock.")
first_solution = "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"

second = alphabet_position("The narwhal bacons at midnight.")
second_solution = "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20"

print(first == first_solution)  # true
print(second == second_solution)  # true
