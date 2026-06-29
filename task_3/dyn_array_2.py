import ctypes
from typing import Any, List, Tuple
from itertools import product
from dyn_array import DynArray

"""
Задание 3, задача 5: динамический массив на основе банковского метода.
"""
class BankDynArray:
    def __init__(self) -> None:
        self.count: int = 0
        self.capacity: int = 1
        self.balance: int = 0
        self.array: ctypes.Array = self.make_array(self.capacity)

    def __len__(self) -> int:
        return self.count

    def make_array(self, new_capacity: int) -> ctypes.Array:
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i: int) -> Any:
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity: int) -> None:
        new_array: ctypes.Array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    """
    Сложность алгоритма:
    - временная (амортизированная): O(1)
    - пространственная: O(1).
    """
    def append(self, itm: Any) -> None:
        if self.balance >= self.capacity:
            self.resize(self.capacity * 2)
            self.balance -= self.count
        self.array[self.count] = itm
        self.count += 1
        self.balance += 2

    def insert(self, i: int, itm: Any) -> None:
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        for j in range(self.count - 1, i - 1, -1):
            self.array[j + 1] = self.array[j]
        self.array[i] = itm
        self.count += 1

    def delete(self, i: int) -> None:
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        for j in range(i, self.count - 1):
            self.array[j] = self.array[j + 1]
        self.array[self.count - 1] = None
        self.count -= 1
        new_capacity: int = max(16, int(self.capacity / 1.5))
        if self.count < (self.capacity + 1) / 2 and not (self.capacity == new_capacity):
            self.resize(new_capacity)


"""
Задание 3, задача 6: многомерный динамический массив.
"""
class MultyDynArray:

    def __init__(self, num_dims: int) -> None:
        self.num_dims: int = num_dims
        self.sizes: List[int] = [0] * num_dims
        self.capacities: List[int] = [16] * num_dims
        total: int = 16 ** num_dims
        self.array: DynArray = DynArray()
        self.array.resize(total)
        self.array.count = total
        for i in range(total):
            self.array.array[i] = None

    def _get_koeffs(self) -> List[int]:
        koeffs: List[int] = [1] * self.num_dims
        for k in range(self.num_dims - 2, -1, -1):
            koeffs[k] = koeffs[k + 1] * self.capacities[k + 1]
        return koeffs

    def _get_idx(self, coords: Tuple[int, ...]) -> int:
        koeffs: List[int] = self._get_koeffs()
        return sum(c * s for c, s in zip(coords, koeffs))

    def _row_start(self, prefix: Tuple[int, ...]) -> int:
        return self._get_idx(prefix + (0,))

    def _validate(self, coords: Tuple[int, ...]) -> Tuple[int, ...]:
        if len(coords) != self.num_dims:
            raise IndexError(f'Expected {self.num_dims} coords, got {len(coords)}')
        return coords

    def _resize(self, new_capacities: List[int]) -> None:
        old_get_koeffs: List[int] = self._get_koeffs()
        new_get_koeffs: List[int] = [1] * self.num_dims
        for k in range(self.num_dims - 2, -1, -1):
            new_get_koeffs[k] = new_get_koeffs[k + 1] * new_capacities[k + 1]
        total: int = 1
        for cap in new_capacities:
            total *= cap
        new_array: DynArray = DynArray()
        new_array.resize(total)
        new_array.count = total
        for i in range(total):
            new_array.array[i] = None
        for coords in product(*(range(s) for s in self.sizes)):
            old_idx: int = sum(c * st for c, st in zip(coords, old_get_koeffs))
            new_idx: int = sum(c * st for c, st in zip(coords, new_get_koeffs))
            new_array.array[new_idx] = self.array[old_idx]
        self.array = new_array
        self.capacities = new_capacities

    def __getitem__(self, coords: Tuple[int, ...]) -> Any:
        coords = self._validate(coords)
        for d, c in enumerate(coords):
            if c < 0 or c >= self.sizes[d]:
                raise IndexError('Index is out of bounds')
        return self.array.array[self._get_idx(coords)]

    """
    Сложность алгоритма:
    - временная: без _resize - O(N), где N - размер последнего измерения; 
        с _resize - O(X * Y * ...), где X, Y, ... - размерности измерений
    - пространственная: без _resize - O(1),
        с _resize - O(X * Y * ...), где X, Y, ... - размерности измерений
    """
    def insert(self, coords: Tuple[int, ...], itm: Any) -> None:
        coords = self._validate(coords)
        for d, c in enumerate(coords):
            if c < 0 or c >= self.sizes[d]:
                raise IndexError('Index is out of bounds')
        if self.sizes[-1] == self.capacities[-1]:
            new_capacities: List[int] = list(self.capacities)
            new_capacities[-1] = self.capacities[-1] * 2
            self._resize(new_capacities)
        start: int = self._row_start(coords[:-1])
        pos: int = self._get_idx(coords)
        last_new: int = start + self.sizes[-1]
        for j in range(last_new, pos, -1):
            self.array.array[j] = self.array.array[j - 1]
        self.array.array[pos] = itm
        self.sizes[-1] += 1

    """
    Сложность алгоритма:
    - временная: без _resize - O(N), где N - размер последнего измерения; 
        с _resize - O(X * Y * ...), где X, Y, ... - размерности измерений
    - пространственная: без _resize - O(1),
        с _resize - O(X * Y * ...), где X, Y, ... - размерности измерений
    """
    def delete(self, coords: Tuple[int, ...]) -> None:
        coords = self._validate(coords)
        for d, c in enumerate(coords):
            if c < 0 or c >= self.sizes[d]:
                raise IndexError('Index is out of bounds')
        start: int = self._row_start(coords[:-1])
        pos: int = self._get_idx(coords)
        last: int = start + self.sizes[-1] - 1
        for j in range(pos, last):
            self.array.array[j] = self.array.array[j + 1]
        self.array.array[last] = None
        self.sizes[-1] -= 1
        new_cap: int = max(16, int(self.capacities[-1] / 1.5))
        if self.sizes[-1] < (self.capacities[-1] + 1) / 2 and new_cap != self.capacities[-1]:
            new_capacities: List[int] = list(self.capacities)
            new_capacities[-1] = new_cap
            self._resize(new_capacities)

"""
рефлексия:
  - Задание 1, задача 8: решение совпадает с рекомендуемым. Но если задуматься, то элементы 
  связного списка могут быть произвольного типа, и просто так сложить их через '+' в реальной 
  жизни не получится.
"""    


