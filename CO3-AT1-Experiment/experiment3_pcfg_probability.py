# Experiment 3: PCFG Sentence Probability

# Grammar Probabilities
NP = {
    "John": 0.6,
    "Mary": 0.4
}

VP = {
    "runs": 0.5,
    "walks": 0.5
}

S_prob = 1.0

def sentence_probability(sentence):

    words = sentence.split()

    # Sentence must contain exactly 2 words
    if len(words) != 2:
        return 0.00

    noun = words[0]
    verb = words[1]

    if noun in NP and verb in VP:
        probability = S_prob * NP[noun] * VP[verb]
        return round(probability, 2)

    return 0.00


# Test Cases
sentences = [
    "John runs",
    "John walks",
    "Mary runs",
    "Mary walks",
    "Peter runs"
]

for s in sentences:
    print(f"{s} -> {sentence_probability(s)}")
