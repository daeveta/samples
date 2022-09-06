def shortener(sentence):
    while '(' in sentence or ')' in sentence:
        left = sentence.rfind('(')
        right = sentence.find(')', left)
        sentence = sentence.replace(sentence[left:right+1], '')
        return (sentence)
print(shortener('Кто-то решил, что текст в скобках (как этот) читать не нужно'))