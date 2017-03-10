def words(string):
    string = string.split()
    count = {}
    for word in string:
        if word.isdigit():
            word = int(word)
        if word in count:
            count[word] = count[word] + 1
        else:
            count[word] = 1

    return count

