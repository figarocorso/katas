class WordsCounting():

    class FileNotFound(Exception):
        pass

    def __init__(self):
        self.words_counting = {}

    def count_file(self, source_file):
        self.source = ""

        try:
            self.source = open(source_file,'r')

            return self.count(self.source.read())

        except IOError:
            raise self.FileNotFound('File ' + source_file + ' not found')

    def count(self, words):
        for word in  words.split():
            try:
                self.words_counting[word] += 1
            except KeyError, e:
                self.words_counting[word] = 1

        return self.format_results()

    def format_results(self):
        self.result = ""
        for word, word_count in self.words_counting.iteritems():
            self.result += word + ':' + str(word_count) + '\n'

        return self.result
