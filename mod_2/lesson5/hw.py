def intr(word):
    return len(word.lower()) == len(set(word.lower()))    
words = input().split()
intresting_words = list(filter(intr, words))
print(len(intresting_words))
# print(len(list(filter(lambda words: len(set(words)) == len(words), input().lower().split()))))
