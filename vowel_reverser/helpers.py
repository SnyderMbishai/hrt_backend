def reverse(message):
    """ Reverse vowels of a word/sentence """
    vowels = list("aeiouAEIOU")
    msg = list(message)
    msg_vowels = [i for i in message if i in vowels][::-1]
    count = 0
    for i in range(len(message)):
        if msg[i] in vowels:
            msg[i] = msg_vowels[count]
            count += 1
    return " ".join(msg)
