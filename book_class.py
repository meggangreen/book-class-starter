class Book(object):

    def __init__(self, title=None):
        self.title = title
        self.word_counts = {}
        # other properties like author, publisher, etc

    def __repr__(self):
        return ('<Book "{}" | Words counted: {}>'
                ).format(self.title, str(len(self.word_counts) > 0))

    def fill_word_counts(self, text):  # text as string
        words = text.split()
        for word in words:
            # correct capitalization
            # correct punctuation
            self.word_counts[word] = self.word_counts.get(word, 0) + 1

    def get_word_counts(self, word):  # word as string
        return self.word_counts.get(word, 0)