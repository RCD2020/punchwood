'''
Criterion Class used for keeping track of criteria and its triggers and
conditions.

Robert C Davis
November 30, 2023
(2023.11.30)
'''


class Criterion:
    '''
    Used for handling criteria.

    name : str -- Unique Name of Criterion

    2023.11.29
    '''

    def __init__(
            self,
            name: str
        ) -> None:

        self.name = name