import re
import collections
from collections import Counter
import pickle

# def normalizer(word):
#     word = word.replace('ي', 'ی')
#     word = word.replace('ك', 'ک')
#     word = word.replace('ٔ', '')
#     return word
#
# def train(features):
#     model = collections.defaultdict(lambda: 1)
#     for f in features:
#         model[f] += 1
#     return model
#
# with open('voa_fa_2003-2008_orig.txt') as fin:
#     Nwords = train(normalizer(word) for ln in fin for word in ln.split())

alphabet = 'ا آ ب پ ت ث ج چ ح خ د ذ ر ز س ش ص ض ط ظ ع غ ف ق ک گ ل م ن و ه ی ء'

def words(text): return re.findall(r'\w+', text.lower())

# WORDS = Counter(words(open('small_file_3000000.txt', encoding="UTF-8").read()))
# pickle.dump(WORDS, open('3.pkl', 'wb'))
# a = pickle.load(open('./1.pkl', 'rb'))
# b = pickle.load(open('./2.pkl', 'rb'))
# c = pickle.load(open('./3.pkl', 'rb'))
# WORDS = a + b + c
# pickle.dump(WORDS, open('F.pkl', 'wb'))
WORDS = pickle.load(open('../Dictionary/Database.pkl', 'rb'))
def P(word, N=sum(WORDS.values())):
    "Probability of `word`."
    return WORDS[word] / N

def correction(word):
    "Most probable spelling correction for word."
    word = normalizer(word)
    return max(candidates(word), key=P)

def candidates(word):
    "Generate possible spelling corrections for word."
    # return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])
    if known([word]) and WORDS[word] > 100:
        return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])
    else:
        return (known(edits1(word)) or known(edits2(word)) or [word])
def known(words):
    "The subset of `words` that appear in the dictionary of WORDS."
    return set(w for w in words if w in WORDS)

def normalizer(word):
    word = word.replace('ي', 'ی')
    word = word.replace('ك', 'ک')
    word = word.replace('ٔ', '')
    return word

def edits1(word):
    "All edits that are one edit away from `word`."
    letters    = 'ا آ ب پ ت ث ج چ ح خ د ذ ر ز ژ س ش ص ض ط ظ ع غ ف ق ک گ ل م ن و ه ی ء'
    # print(letters)
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    # print(set(deletes + transposes + replaces + inserts))
    return set(deletes + transposes + replaces + inserts)

def edits2(word):
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))

# print(correction("قزار"))
# print(list(WORDS.items())[:100])