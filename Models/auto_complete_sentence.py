# Auto-complete sentence model

"""
Build a simple n-gram model from the training sentences.

For every prefix of a sentence, we learn a distribution
over the remaining part of the sentence.

Example (sentence = ['I', 'am', 'a', 'boy']):
    prefix ('I',)     -> 'am', 'a', 'boy'
    prefix ('I','am') -> 'a', 'boy'
    prefix ('I','am','a') -> 'boy'
"""

from collections import defaultdict, Counter
from typing import List, Tuple, Dict, Optional


class SentenceCompletionModel:
    def __init__(self, sentences: List[List[str]]):
        """
        Build an index that maps any contiguous fragment of a sentence
        (prefix, case-insensitive) to the remaining part of that sentence
        (in original casing).
        """
        # mapping: normalized prefix (tuple of lower-case tokens)
        #       -> list of possible completions (each completion is a list[str] in original form)
        self.completions: Dict[Tuple[str, ...], List[List[str]]] = defaultdict(list)

        for sentence in sentences:
            n = len(sentence)
            for start in range(n):
                for end in range(start + 1, n + 1):
                    # prefix tokens in original case
                    prefix_tokens = sentence[start:end]
                    remaining = sentence[end:]
                    if not remaining:
                        continue  # nothing to complete

                    # normalized prefix for case-insensitive matching
                    normalized_prefix = tuple(token.lower() for token in prefix_tokens)

                    # store the remaining part with original casing
                    self.completions[normalized_prefix].append(remaining)

    def _get_matches(self, prefix_words: List[str]) -> List[List[str]]:
        """Internal helper: case-insensitive lookup of completions."""
        normalized_prefix = tuple(word.lower() for word in prefix_words)
        return self.completions.get(normalized_prefix, [])

    def complete(
        self,
        prefix_words: List[str],
        return_as_strings: bool = True
    ) -> List[str] | List[List[str]]:
        """
        Return *all* possible completions for the given prefix (case-insensitive).

        If return_as_strings=True:
            -> ["a boy", "a Machine Expert", "through to the finals"]
        Else:
            -> [["a", "boy"], ["a", "Machine", "Expert"], ["through", "to", "the", "finals"]]
        """
        matches = self._get_matches(prefix_words)

        if not matches:
            return []

        # deduplicate while preserving order
        unique_set = set()
        unique_matches: List[List[str]] = []
        for completion in matches:
            tupled_completion = tuple(completion)
            if tupled_completion not in unique_set:
                unique_set.add(tupled_completion)
                unique_matches.append(completion)

        if return_as_strings:
            return [" ".join(words) for words in unique_matches]
        else:
            return unique_matches

    def complete_best(self, prefix_words: List[str]) -> Optional[str]:
        """
        Return the *single best* (most frequent) completion for the given prefix,
        using case-insensitive matching.

        If there are multiple completions with the same max frequency,
        tie-break using alphabetical order of the joined string.

        Returns:
            - A string like "a Machine Expert" or "through to the finals"
            - None if no completion exists for this prefix
        """
        matches = self._get_matches(prefix_words)
        if not matches:
            print("Model found no completion for this prefix")
            return None

        # Count how often each completion appears
        counts = Counter(tuple(match) for match in matches)

        # Choose completion with:
        # 1) highest frequency
        # 2) lexicographically smallest joined string as tie-break
        best_tuple, _ = max(
            counts.items(),
            key=lambda item: (item[1], " ".join(item[0]))
        )

        return " ".join(best_tuple)


training_set = [ 
    ['I', 'am', 'surprisingly', 'estactic'],
    ['I', 'like', 'pizza'],
    ['What', 'did', 'you', 'just', 'say'],
    ['I ', 'love', 'coding'],
    ['Where', 'do', 'you', 'live?'],
    ['I', 'am', 'a', 'school', 'boy'],
    ['You', 'said', 'I', 'like', 'donuts'],
    ['You', 'look', 'sober'],
    ['You', 'are', 'a', 'beast'],
    ['I','am', 'a', 'Machine', 'Learning', 'Expert'],
    ['You', 'said', 'good', 'things', 'about', 'me'],
    ['I', 'am', 'through', 'to', 'the', 'finals'],
    ['who', 'are', 'you', 'talking', 'about?'],
]

if __name__ == "__main__":
    model = SentenceCompletionModel(training_set)

    # 1. Inputs 1
    input_1 = input("Enter word 1: ")
    input_1 = input_1.split(" ") if input_1 else []
    print(f"All completions for {input_1}:", model.complete(input_1))
    print(f"Best completion for {input_1}:", model.complete_best(input_1))
    print('\t')

    # 2. Inputs 2
    input_2 = input("Enter word 2: ")
    input_2 = input_2.split(" ") if input_1 else []
    print(f"All completions for {input_2}:", model.complete(input_2))
    print(f"Best completion for {input_2}:", model.complete_best(input_2))
