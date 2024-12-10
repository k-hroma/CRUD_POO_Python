# create books class to be able to create book type objects

class Book():

    def __init__(self, title, autor, gender):
        # protected attributes
        self._title = title
        self._autor = autor
        self._gender = gender

    @property
    def title(self):
        return self._title

    @property
    def autor(self):
        return self._autor

    @property
    def gender(self):
        return self._gender
