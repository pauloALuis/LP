#!/usr/bin/env python3

#2.a)
def vocals_in_word(s : str, vocals : list):
    """
    method that counts the vocals in a word (string)
    """
    n = 0
    for letter in s:
        for vocal in vocals:
            if letter == vocal:
                n+=1
    return n

#2.b)
def pair_digits_to_a(digits :str):
    """
    function that transform all the pair number os a string to the letter "a"
    if string isn't all numeric, function returns "invalid word"
    """
    s = ""
    if digits.isnumeric():
        for digit in digits:
            if int(digit) % 2 == 0:
                s += "a"
            else:
                s += digit
    else:
        print("a palavra não contém apenas dígitos!")
        return "invalid word"
    return s


#2.c)
def digits_sum_in_word(s: str):
    """
    function that returns the sum of digits in a string
    """
    n = 0
    for letter in s:
        if letter.isnumeric():
            n += int(letter)
    return n

#2.d)
def repeated_word(s: str, n: int):
    """
    method that returns the string "s" "n" times
    """
    result = ""
    for _ in range(n):
        result += s
    return result

if __name__ == "__main__":
    vocals = ["a", "e", "i", "o", "u"]
    s = "abcdefghi"
    s2 = "1234567890"
    s3 = "12osfidhv5ifdu6idufh8"
    s4 = "abc"
    n = 3
    #2.a)
    print("contagem de vogais na palavra ", s, " = ", vocals_in_word(s, vocals))

    #2.b)
    print("passagem de numeros pares para a letra \"a\" da palavra : ", s2, " = ", pair_digits_to_a(s2))

    #2.c)
    print("soma dos digitos na palavra ", s3, " = ", digits_sum_in_word(s3))

    #2.d)
    print("palavra ", s4, "repetida ", n, " vezes:")
    print(repeated_word(s4, n))

pass
