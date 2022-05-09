import string

english_alphabet = list(string.ascii_lowercase) + [str(num) for num in range(1, 11)]
morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
        "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", ".----",
        "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----.", "-----"]

iter_num = max(len(english_alphabet), len(morse))

morse_text = {english_alphabet[i]:morse[i] for i in range(iter_num)}
text_morse = {value:key for (key, value) in morse_text.items()}



