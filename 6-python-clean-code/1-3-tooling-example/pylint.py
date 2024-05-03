import os
"""
Docstring module
"""

"""
Run the command
pylint ./1-3-tooling-example/pylint.py

Links:
docs.pylint.org
youtube.com/watch?v=P7Rzlu8LrAE
pylint.readthedocs.io/en/stable/
youtube.com/watch?v=fY5103p5-c
"""

class StringManager:
    """ Docstring class """

    def __init__(self, word ):
        """ Docstring method """
        self.word = word

    def revert(self ):
        """ Docstring method """
        return self._upper(self.word)

    def _upper(self, word ):
        """ Docstring method """
        return word.upper()


os.system('ls')
