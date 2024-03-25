class Lattice:
    def __init__(self, basis: Matrix):
        self.dimension = basis.rows_num
        self.basis = basis
        self.spanned_elements = self.basis.span()
        self.minkowski_first_theorem_distance = self.basis.minkowski_first_theorem_distance()

