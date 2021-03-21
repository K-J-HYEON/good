# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit"

# import re
# re.sub('[^\w]', ' ', paragraph)

# banned = 'hit'
# word_list = re.sub('[^\w]', ' ', paragraph).lower().split()
# words = [word for word in word_list if word not in banned]
# print(words)

# import collections
# counts = collections.Counter(words)
# print(counts)

# print(counts.most_common()[0][0])

#Counter()에 대한 정리
# import collections
# data = [1, 2, 3, 3, 4, 5, 6, 6, 6, 7, 8]
# dic_data = collections.Counter(data)
# print(dic_data)

# print(type(dic_data))

# print(dic_data.most_common())

# print(dic_data.most_common(2))

# Bow(Bag-of-Words)
from collections import Counter
sentences = [['barber', 'person'], ['barber', 'good', 'person'], ['barber', 'huge', 'person'], ['knew', 'secret'], ['secret', 'kept', 'huge', 'secret'], ['huge', 'secret'], ['barber', 'kept', 'word'], ['barber', 'kept', 'word'], ['barber', 'kept', 'secret'], ['keeping', 'keeping', 'huge', 'secret', 'driving', 'barber', 'crazy'], ['barber', 'went', 'huge', 'mountain']]

words = sum(sentences, [])
print(words)

vocab = Counter(words)
print(vocab)
print(vocab["barber"])

vocab_size = 5
vocab = vocab.most_common(vocab_size)
vocab

word_to_index = {}
i = 0
for (word, frequency) in vocab:
    i = i + 1
    word_to_index[word] = i
print(word_to_index)