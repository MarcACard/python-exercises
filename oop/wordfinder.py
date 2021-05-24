"""Word Finder: finds random words from a dictionary."""

from random import choice


class WordFinder:
    """A class to process and return random words from a file"""

    def __init__(self, file_path):
        f = open(file_path)
        self.words = self.parse_file(f)
        self.source = file_path

        print(f"{len(self.words)} words read")

    def __repr__(self):
        return f"<WordFinder word_count={len(self.words)} source={self.source}>"

    def parse_file(self, f):
        """Parse a file and return a list containing each line."""
        return [line.rstrip() for line in f]

    def random(self):
        """Return a random word from the words attribute"""
        return choice(self.words)


class SpecialWordFinder(WordFinder):
    """A special WordFinder that is able to process files with blank lines & comments"""

    def __init__(self, file_path):
        super().__init__(file_path)

    def __repr__(self):
        return f"<SpecialWordFinder word_count={len(self.words)} source={self.source}>"

    def parse_file(self, f):
        """Parse a file and return a list with each line.Ignore empty lines & \\n characters"""
        return [
            line.rstrip()
            for line in f
            if not line.startswith("#") and not line.startswith("\n")
        ]
