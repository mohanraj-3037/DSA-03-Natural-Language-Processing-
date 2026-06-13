# Experiment 2: Subject-Verb Agreement Checking

# Feature Structures
subjects = {
    "he": ("singular", "third"),
    "she": ("singular", "third"),
    "it": ("singular", "third"),
    "they": ("plural", "third")
}

verbs = {
    "runs": "singular",
    "writes": "singular",
    "run": "plural",
    "write": "plural"
}

def check_agreement(subject, verb):

    if subject not in subjects or verb not in verbs:
        return False

    subject_number = subjects[subject][0]
    verb_number = verbs[verb]

    return subject_number == verb_number


# Test Cases
test_cases = [
    ("he", "runs"),
    ("he", "run"),
    ("they", "run"),
    ("they", "writes"),
    ("she", "writes")
]

for subject, verb in test_cases:
    print(f"{subject} {verb} -> {check_agreement(subject, verb)}")
