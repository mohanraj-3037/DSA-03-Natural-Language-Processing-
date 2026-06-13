# Experiment 1: CFG Validation and Parse Tree Construction

# Grammar Rules
Det = ["the", "a"]
N = ["student", "teacher", "book"]
V = ["reads", "likes"]

def parse_cfg(sentence):
    words = sentence.split()

    # Expected structure:
    # Det N V Det N
    if len(words) != 5:
        return "Invalid Sentence"

    if (words[0] in Det and
        words[1] in N and
        words[2] in V and
        words[3] in Det and
        words[4] in N):

        parse_tree = {
            "S": {
                "NP": {
                    "Det": words[0],
                    "N": words[1]
                },
                "VP": {
                    "V": words[2],
                    "NP": {
                        "Det": words[3],
                        "N": words[4]
                    }
                }
            }
        }

        return parse_tree

    else:
        return "Invalid Sentence"


# Test Cases
sentences = [
    "the student reads a book",
    "a teacher likes the book",
    "student reads book",
    "the book likes a teacher",
    "reads the student book"
]

for s in sentences:
    print("\\nInput:", s)
    print("Output:", parse_cfg(s))
