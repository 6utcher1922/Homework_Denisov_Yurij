# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

# Моё решение A:
def remove_exclamation_marks(s):
    a = s.replace("!", "")
    print(a)

remove_exclamation_marks("Oh, no!!!")



# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

# Моё решение B:
def remove_last_em(s):
    if s[-1] == "!":
        s = s[0:-1]
    print(s)

remove_last_em("Hi!")


# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

# Моё решение C:
def remove_word_with_one_em(s):
    return " ".join([w for w in s.split(" ") if w.count("!")!=1])

print(remove_word_with_one_em("Hi! Hi!! Hi!"))