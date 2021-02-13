def count_letters(word_list):
    """ See question description """
    
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"

    letter_count = {}
    for letter in ALPHABET:
        letter_count[letter] = 0
    for word in word_list:
        for letter in word:
            if letter == ' ':
                pass
            else: 
                letter_count[letter] += 1
    
    max_value = max(letter_count.values())
    for key in letter_count:
        if letter_count[key] == max_value:
            return key         

print(count_letters(["hello", "world"]))
monty_quote = "listen strange women lying in ponds distributing swords is no basis for a system of government supreme executive power derives from a mandate from the masses not from some farcical aquatic ceremony"
monty_words = monty_quote.split(" ")
print(count_letters(monty_words))
