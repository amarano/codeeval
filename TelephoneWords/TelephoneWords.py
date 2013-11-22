import sys

#Not very pythonic. I wanted to do it without list comprehensions just to prove to myself I could.
# I'll rewrite with list comp for another revision

def TelephoneWords(number):
    key_letters = {'0': '0', '1': '1', '2': "abc", '3': "def", '4': "ghi", '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    words = ['']
    for num in str(number):
        temp_words = []
        for letter in key_letters[num]:
            for word in words:
                temp_words.append(word + letter)
        words = temp_words
    return words


def main():
    lines = map(lambda x: x.rstrip(), open(sys.argv[1]).readlines())
    for line in lines:
        print ','.join(sorted(TelephoneWords(line)))

main()