def is_pangram(sentence):
    alphabet = []
    for i in sentence.replace(' ', '').lower():
        if i not in alphabet and i.isalpha():
            alphabet.append(i)

    if len(alphabet) == 26: return True
    else: return False
