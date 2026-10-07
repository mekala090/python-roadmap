def word_freq(text):
    freq = {}
    for w in text.lower().split():
        freq[w] = freq.get(w, 0) + 1
    return freq
