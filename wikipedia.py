import requests
# testing

SPORT_KEYWORDS = ['season', 'series', 'US Open', 'football', 'baseball', 'soccer', 'NCAA', 'NHL', 'NFL', "FIFA", 'championship', 'world cup', 'tournament', 'rugby']


def is_election(title):
    if "election" in title.lower():
        return True
    return False

def is_sport(title):
    for keyword in SPORT_KEYWORDS:
        if keyword in title:
            return True
    return False


def find_articles(count, filename, filesize=400, faster_update=False):
    """
    Generate a list of wikipedia pages of a certain file size (in KB) using https://en.wikipedia.org/wiki/Special:Random\n
    WARNING: If function is killed before it's finished, the articles will not save.
    :param count:
    :param filename:
    :return:
    """

    f = open(f'{filename}', 'a')
    while count:
        r = requests.get("https://en.wikipedia.org/wiki/Special:Random")
        if len(r.text) > filesize * 1000:
            # OPTIONAL: check if sports or election
            title = r.text[r.text.index("<title>") + 7:r.text.index(" - Wikipedia")]
            if is_election(title):
                continue
            if is_sport(title):
                continue
            f.write(r.url + "\n")
            count -= 1
            print(f"Appending {title}, size {len(r.text)}.")
            if faster_update:
                f.close()
                f = open(f'{filename}', 'a')
    f.close()

find_articles(20, "pages1.txt", faster_update=True)
