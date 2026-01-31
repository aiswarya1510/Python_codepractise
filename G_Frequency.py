def freq(words):
    visitlist=[]
    for i in range(0,len(words)):
        freq=1
        if words[i] in visitlist:
            continue
        for j in range(i+1,len(words)):
            if words[i]==words[j]:
                freq=freq+1
        visitlist.append(words[i])
        print(f"frequency of {words[i]} is {freq}")

freq("abbnbnb")


def freq2(words):
    wordlist=[]
    for c in words:
        if c in wordlist:
            continue
        val=words.count(c)
        print(f"count of {c} is {val}")
        wordlist.append(c)

freq2("abbbb")