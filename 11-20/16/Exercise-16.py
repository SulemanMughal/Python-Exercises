class Matrix:
    """Simple Matrix class."""
    
    def __init__(self, string):
        self.matrix = [
            [int(i) for i in row.split()]
            for row in string.splitlines()
        ]