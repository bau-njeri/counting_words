def words(line):
    word = {}
    for w in line.split():
        word[w] = word.get(w,0) + 1
    for w, c in word.items():
        
        return word
