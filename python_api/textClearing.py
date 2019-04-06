from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def clear_text(str, debug = 0):

    words = str.split()

    adj_words_to_check = 2
    for ind, word in enumerate(words):
        if ind < len(words)-adj_words_to_check:
            for i in range(1, adj_words_to_check):
                if debug:
                    print('words: ' + words[i] + ' ' + words[ind+i])
                    print(similar(words[ind], words[ind+i]))
                if similar(words[ind], words[ind+i]) >= 0.8:
                    del words[ind]

    str = ''
    for word in words:
        str += word
    return words

print(clear_text("Some tes test text with emm emm some some repeat repeated words"))
