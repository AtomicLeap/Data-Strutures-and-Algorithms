# Auto-complete next word model

"""
Build a simple n-gram model from the training sentences.

For every prefix of a sentence, we learn a distribution
over the next word.

Example (sentence = ['I', 'am', 'a', 'boy']):
    prefix ()         -> 'I'
    prefix ('I',)     -> 'am'
    prefix ('I','am') -> 'a'
    prefix ('I','am','a') -> 'boy'
"""

from collections import defaultdict, Counter
from typing import List, Optional, Tuple


class AutoCompleteModel:
    def __init__(self, sentences: List[List[str]]):
        # mapping: prefix (tuple of tokens) -> Counter(next_word)
        self.model: dict[Tuple[str, ...], Counter] = defaultdict(Counter)

        for sentence in sentences:
            for i in range(len(sentence)):
                prefix = tuple(sentence[:i])   # words before position i
                next_word = sentence[i]        # word at position i
                self.model[prefix][next_word] += 1

    def predict_next(
        self, prefix_words: List[str], top_k: int = 1
    ) -> Optional[str | List[str]]:
        """
        Given a (possibly multi-word) prefix, predict the next word.
        
        Uses longest-prefix backoff:
          - Try full prefix
          - If unseen, drop the first word and try again
          - Continue until we find something or give up
        
        top_k = 1  -> return single best word (or None)
        top_k > 1  -> return list of best candidates
        """
        if not prefix_words:
            prefix = ()
        else:
            prefix = tuple(prefix_words)

        # Backoff: shorten prefix from the left until we find a match
        while prefix and prefix not in self.model:
            prefix = prefix[1:]

        # If still no match, try empty prefix (start-of-sentence stats)
        if prefix_words and not prefix:
            print('Model found no completion for this prefix')
            return None

        counter = self.model[prefix]

        # Sort by frequency (descending), then lexicographically for stability
        candidates = sorted(counter.items(), key=lambda x: (-x[1], x[0]))

        if top_k == 1:
            return candidates[0][0]  # best single prediction (word)
        else:
            return [w for (w, _) in candidates[:top_k]]

training_set = [ 
    ['I', 'am', 'surprisingly', 'estactic'],
    ['I', 'like', 'pizza'],
    ['What', 'did', 'you', 'just', 'said'],
    ['I ', 'love', 'coding'],
    ['Where', 'do', 'you', 'live', '?'],
    ['I', 'am', 'a', 'school', 'boy'],
    ['You', 'said', 'I', 'like', 'donuts'],
    ['You', 'look', 'sober'],
    ['You', 'are', 'a', 'beast'],
    ['I','am', 'a', 'Machine', 'Learning', 'Expert'],
    ['You', 'said', 'good', 'things', 'about', 'me'],
    ['I', 'am', 'through', 'to', 'the', 'finals'],
    ['who', 'are', 'you', '?'],
]

if __name__ == "__main__":
    model = AutoCompleteModel(training_set)

    # Some example queries:

    # 1. Inputs 1
    input_1 = input("Enter word 1: ")
    input_1 = input_1.split(" ") if input_1 else []
    print(f"After {input_1}:", model.predict_next(input_1))

    # 2. Inputs 2
    input_2 = input("Enter word 2: ")
    input_2 = input_2.split(" ") if input_1 else []
    print(f"After {input_2}:", model.predict_next(input_2))
