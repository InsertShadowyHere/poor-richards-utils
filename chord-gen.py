import random
from time import time

# generate random chord number and major/minor and decorations
DEGREES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
NOTES = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
DISTANCES = {2: (1, 2), 3: (3, 4), 4: (5, 6), 5: (7, 7), 6: (8, 9), 7: (10, 11), 8: (12, 12), 9: (13, 14),
             10: (15, 16), 11: (17, 18)}


class Node:
    def __init__(self, value, note):
        self.value = value
        self.note = note
        self.next = None

    def __repr__(self):
        return str(self.note)

    def __eq__(self, other):
        return self.note == other

    def next_node(self, ct=1):
        if ct > 1:
            return self.next.next_node(ct - 1)
        else:
            return self.next

    def degree(self, deg):
        """
        Returns a random version of the scale degree given.\n
        e.g. degree(3) on c returns either E or D#
        :param deg:
        :return:
        """
        return self.next_node(random.choice(DISTANCES[deg]))


linked_degrees = []

for degree in DEGREES:
    linked_degrees.append(Node(degree, NOTES[degree - 1]))
linked_degrees[-1].next = linked_degrees[0]

for i in range(len(linked_degrees) - 1):
    linked_degrees[i].next = linked_degrees[i + 1]


def generate_chord(invert=False):
    """
    First generates a root triad - DONE
    then modifies to add 7ths, accidentals, etc.
    :return:
    """

    # decorations that can be added:
    # extensions (7, 9, 11, 13)
    # quality variations (aug, major, minor, diminished) - dealt with by random degrees
    # inversions and note spacing
    # random other notes

    root = random.choice(linked_degrees)
    # decide between maj and min
    chord = [root, root.degree(3), root.degree(5)]

    # EXTENSIONS
    # 1/10 chance of 11th, 1/5 change of 9th, 1/2 chance of 7th
    if random.randint(0, 1):
        chord.append(root.degree(7))
    if random.random() >= 0.8:
        chord.append(root.degree(9))
    if random.random() >= 0.9:
        chord.append(root.degree(11))

    if invert:
        random.shuffle(chord)
    return chord


x = generate_chord(invert=True)
while len(x) == 3:
    x = generate_chord(invert=True)
print(x)
def test_for(chord, cases):
    """
    Prints data about how long/how many tries it takes to generate a given chord.
    :param chord: given chord to look for
    :param cases: number of test cases
    :return:
    """
    times = []
    counts = []
    test_chord = chord
    test_cases = cases
    for _ in range(test_cases):
        start = time.time()
        count = 0
        while True:
            chord = generate_chord()
            if chord == test_chord:
                break
            else:
                count += 1
        total = time.time() - start
        times.append(total)
        counts.append(count)
    print(f"The program ran {test_cases} times over the course of {round(sum(times), 2)} seconds.")
    print(f"On average, it took {sum(counts) / len(counts)} tries to get the chord {test_chord}.")
