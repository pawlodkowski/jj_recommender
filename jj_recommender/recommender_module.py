"""Module Docstring goes here"""

import random

class Recommender:

    """Class for grouping all my related functions (i.e. methods).
       A paragraph for all my structured sentences.
    """

    def __init__(self, items):
        self.items = items

    def recommend_random(self, num:str)->list:
        """
        Given a list of items, return n results randomly.

        Parameters:
        --------------------

        - items (list)
        - num (integer)

        Returns:
        --------------------
        - results (list)

        """
        results = random.sample(self.items, k = num)
        results = [i.lower() for i in results]
        return results

    def recommend_nmf():
        """Coming in version 2.0"""
        pass

    def recommend_cosim():
        """Coming in version 3.0"""
        pass


if __name__ == '__main__':
    #Whatever code is in this block will ONLY be executed if I run this module
    #directly, i.e. python recommender_module.py
    #If stuff from this module is imported from somewhere else, then this code
    #will NOT be run.

    ITEMS = ['Toy Story 1',
             'Life of Pi',
             'La La Land',
             'Shawshank Redemption',
             'Something else',
             'Some other thing',
             'basil is not a spice',
             'thyme is a herb goddamit',
             'jasmine? Not a spice!',
             'Forest Gamp',
             'Bohemian Rapsody',
             'Mr. Nobody',
             'The Tree of Life',
             'Portrait of Dorian Gray',
             'Parasite']
    rec = Recommender(ITEMS)
    result = rec.recommend_random(3)
    print(result)


class Random:
    """
    Just a random class to annoy
    """
    pass
