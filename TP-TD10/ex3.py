class Maliste(list):
    def __init__(self, *args):
        super().__init__(*args)

    def __str__(self):
        return "[" + ";".join(str(e) for e in self) + "]"

    def __add__(self, other):
        return Maliste(super().__add__(other))

    def __mul__(self, other):
        return Maliste(super().__mul__(other))

    def __sub__(self, other):
        return Maliste(super().__sub__(other))


l1 = Maliste([1, 2, 3])
print(l1)
l2 = Maliste([1, 2, 3])
print(l2)
print(l1 + l2)
