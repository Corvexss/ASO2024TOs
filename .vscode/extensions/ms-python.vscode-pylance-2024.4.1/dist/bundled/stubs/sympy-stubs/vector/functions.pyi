from typing import Any, Literal
from sympy import Equality, Ne
from sympy.core.add import Add
from sympy.core.relational import Relational
from sympy.vector.dyadic import DyadicZero
from sympy.vector.operators import Divergence
from sympy.vector.vector import VectorZero
def express(expr, system, system2=..., variables=...) -> VectorZero | DyadicZero:
    ...

def directional_derivative(field, direction_vector) -> VectorZero | Literal[0]:
    ...

def laplacian(expr) -> Divergence | Add:
    ...

def is_conservative(field) -> Literal[True]:
    ...

def is_solenoidal(field) -> bool:
    ...

def scalar_potential(field, coord_sys) -> Equality | Relational | Ne:
    ...

def scalar_potential_difference(field, coord_sys, point1, point2):
    ...

def matrix_to_vector(matrix, system) -> VectorZero:
    ...

def orthogonalize(*vlist, orthonormal=...) -> list[Any]:
    ...

