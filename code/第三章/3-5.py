def replaceWords(dict, sentence):
    """
    :type dict: List[str]
    :type sentence: str
    :rtype: str
    """
    d = collections.defaultdict(set)
    s = collections.defaultdict(int)
    sentence = sentence.split()
    for w in dict:
        print(w[0])
        d[w[0]].add(w)
        s[w[0]] = max(s[w[0]], len(w))
    for i, w in enumerate(sentence):
        for j in range(s[w[0]]):
            if w[:j+1] in d[w[0]]:
                sentence[i] = w[:j+1]
                break
    return ' '.join(sentence)