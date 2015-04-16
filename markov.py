import sys
from random import choice


class SimpleMarkovGenerator(object):

    def read_files(self, filenames):
        """Given a list of files, make chains from them."""

        openfiles = ''

        for filename in filenames:
            openfiles += open(filename).read()

        for input_text in openfiles:
            input_text = openfiles.rstrip().split()

        return input_text


    def make_chains(self, corpus):
        """Takes input text as string; stores chains."""

        chains = {}

        words = corpus

        for i in range(len(words) - 2):
            key = (words[i], words[i + 1])
            value = words[i + 2]

            chains.setdefault(key, []).append(value)

        return chains


    def make_text(self, chains):
        """Takes dictionary of markov chains; returns random text."""

        key = choice(chains.keys())
        # words = [key[0], key[1]]
        words = ''

        counter = 0
        # while len(words) <= 250 :
        while counter <= 100:
            # Keep looping until we have a key that isn't in the chains
            # (which would mean it was the end of our original text)
            #
            # Note that for long texts (like a full book), this might mean
            # it would run for a very long time.
            # 
            # Note: with counter, final output is 3 more than counter max
            if key in chains:
                word = choice(chains[key])
                words = words + word + ' '
                key = (key[1], word)
            counter += 1

        # return " ".join(words)
        return words

if __name__ == "__main__":

    # we should get list of filenames from sys.argv
    # we should make an instance of the class
    # we should call the read_files method with the list of filenames
    # we should call the make_text method 5x

    filenames = [sys.argv[1], sys.argv[2]]
    # filenames = sys.argv[1]

    instance1 = SimpleMarkovGenerator()
    input_text = instance1.read_files(filenames)
    chains = instance1.make_chains(input_text)
    random_text = instance1.make_text(chains) 

    print random_text