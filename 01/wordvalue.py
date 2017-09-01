from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    # word_list =[]
    # for words in open(DICTIONARY,'r'):
    #     word_list.append(words.strip())
    # return word_list
    return [x.strip() for x in open(DICTIONARY,'r')]

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    # total = 0
    # for letter in list(word):
    #     total += LETTER_SCORES.get(letter.upper(),0)
    # return total
    return sum(LETTER_SCORES.get(letter.upper(),0) for letter in list(word))

def max_word_value(words_list=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    # max_word=''
    # max_word_val = 0
    # for word in words_list:
    #     word_value = calc_word_value(word)
    #     if word_value > max_word_val:
    #         max_word_val = word_value
    #         max_word=word
    # return max_word
    return max(words_list, key=calc_word_value)

if __name__ == "__main__":
    pass # run unittests to validate
    # calc_word_value('hello')
    # load_words()
