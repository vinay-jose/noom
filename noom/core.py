"""Noom class definition - arithmetic and comparison operations"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_core.ipynb.

# %% auto 0
__all__ = ['Noom']

# %% ../nbs/00_core.ipynb 4
from fastcore.foundation import patch

# %% ../nbs/00_core.ipynb 5
class Noom:
    """Noom is a number datatype alternative with limited capabilities."""
    def __init__(self, val):
        assert isinstance(val, (int, float))
        self.val = val
    
    def __repr__(self):
        return str(self.val)
    
    __str__ = __repr__
    
    def __add__(self, oth):
        return Noom(self.val + oth.val)
    
    def __sub__(self, oth):
        return Noom(self.val - oth.val)
    
    def __mul__(self, oth):
        return Noom(self.val * oth.val)
    
    def __truediv__(self, oth):
        return Noom(self.val / oth.val)
    
    def __floordiv__(self, oth):
        return Noom(self.val // oth.val)


# %% ../nbs/00_core.ipynb 14
@patch
def __eq__(self: Noom, oth):
    return self.val == oth.val

# %% ../nbs/00_core.ipynb 26
@patch
def __lt__(self: Noom, oth):
    return self.val < oth.val

# %% ../nbs/00_core.ipynb 31
@patch
def __le__(self: Noom, oth):
    return self.val <= oth.val
