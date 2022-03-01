from random import choice

#use words.txt
class WordFinder:
    """Word Finder: finds random words from a dictionary.
    
    >>> wordfinder = WordFinder('test.txt')
    3 words read
    >>> wordfinder.random() in ['cat', 'rabbit', 'dog']
    True
    """
    def __init__(self, path):
        """Creates list of words from path; prints a word count"""
        self.words = self.get_words(open(path))
        # with open(path, 'r') as file:
        #     word_count =  sum(1 for line in file)
        #     print(f"{word_count} words read")
        print(f"{len(self.words)} words read")

    def get_words(self, file):
        """Adds each word from the file to the words list to access randomly later"""
        return [word.strip() for word in file]

    def random(self):
        """Chooses a randomly selected word from the words list and returns it"""
        return choice(self.words)

#use complex_words.txt
class SpecialWordFinder(WordFinder):
    """Finds random words in file that has blank lines, as well as lines that start with a '#' to make a comment
    >>> specialWF = SpecialWordFinder('complex_words.txt')
    4 words read
    >>> specialWF.random() in ['kale', 'parsnips', 'apple', 'mango']
    True
    """
    def get_words(self, file):
        """Adds each word from the file to the words list to access randomly later IF that word does not start with a #"""
        return [word.strip() for word in file if word.strip() and word[0] != '#']



