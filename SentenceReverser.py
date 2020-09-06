def sentenceReverser(sentence):
    newSentence = sentence.split(" ")
    newSentence = newSentence[::-1]
    return(newSentence)

sentenceReverser("Why hello there general kenobi")