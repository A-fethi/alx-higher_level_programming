#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return (len(sentence), None)
    for i in range(len(sentence)):
        return (len(sentence), sentence[i])
