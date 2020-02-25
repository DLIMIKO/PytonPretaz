# Objekty

class Kruh:
    def __intit__(self, pol):
        self.polomer = pol

    def __str__(self):
        return "Kruh ma polomer {}".format(self.polomer)

    """def __mul__ (self, other):
        return Kruh (self.polomer*other.polomer)"""

    def obsah(self):
        return self.polomer ** 2 * 3.14

    @property
    def polomer(self):
        return self.polomer

Prvy = Kruh(10)
print(Prvy.obsah())

Druhy=Kruh(20)

