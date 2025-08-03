search = "TA_TO_"

with open("scrabble-words-dict.txt", "r") as dic:
    words = list(map(lambda x: x.strip(), dic.readlines()))
    possible = []
    for i in words:
        print(i)
        if len(i) == len(search):
            print(i)
            for n in range(len(i)):
                if search[n] != "_" and search[n] != i[n]:
                    skip = True
                    break
            if skip:
                skip = False
                continue
            possible.append(i)
        else:
            continue
    print(possible)
