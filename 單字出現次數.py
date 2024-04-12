def replaceblank(string):
    for char in string:
        if char in "!>,<.?":
            string = string.replace(char, ' ')
    return string


def counts(string):
    result = {}
    wordslidt = string.split()
    for word in wordslidt:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result


song = "I have a pen.I have an apple,Apple pen.I have a pen.I have pinapple.pinapple pen,Apple pen,Pinapple pen,Pen pinapple,apple pen."

x = replaceblank(song.lower())
result = counts(x)
print(result)
