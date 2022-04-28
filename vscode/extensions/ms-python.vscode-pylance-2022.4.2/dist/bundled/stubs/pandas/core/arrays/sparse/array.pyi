import numpy as np
from pandas._libs.sparse import BlockIndex as BlockIndex, IntIndex as IntIndex, SparseIndex as SparseIndex
from pandas._libs.tslibs import NaT as NaT
from pandas.core.arrays import ExtensionArray as ExtensionArray, ExtensionOpsMixin as ExtensionOpsMixin
from pandas.core.arrays.sparse.dtype import SparseDtype as SparseDtype
from pandas.core.base import PandasObject as PandasObject
from pandas.core.construction import sanitize_array as sanitize_array
from pandas.core.dtypes.cast import (
    astype_nansafe as astype_nansafe,
    construct_1d_arraylike_from_scalar as construct_1d_arraylike_from_scalar,
    find_common_type as find_common_type,
    infer_dtype_from_scalar as infer_dtype_from_scalar,
)
from pandas.core.dtypes.common import (
    is_array_like as is_array_like,
    is_bool_dtype as is_bool_dtype,
    is_datetime64_any_dtype as is_datetime64_any_dtype,
    is_dtype_equal as is_dtype_equal,
    is_integer as is_integer,
    is_object_dtype as is_object_dtype,
    is_scalar as is_scalar,
    is_string_dtype as is_string_dtype,
    pandas_dtype as pandas_dtype,
)
from pandas.core.dtypes.generic import ABCIndexClass as ABCIndexClass, ABCSeries as ABCSeries, ABCSparseArray as ABCSparseArray
from pandas.core.dtypes.missing import isna as isna, na_value_for_dtype as na_value_for_dtype, notna as notna
from pandas.core.indexers import check_array_indexer as check_array_indexer
from pandas.core.missing import interpolate_2d as interpolate_2d
from pandas.core.ops.common import unpack_zerodim_and_defer as unpack_zerodim_and_defer
from pandas.errors import PerformanceWarning as PerformanceWarning

class SparseArray(PandasObject, ExtensionArray, ExtensionOpsMixin):
    def __init__(
        self, data, sparse_index=..., index=..., fill_value=..., kind: str = ..., dtype=..., copy: bool = ...
    ) -> None: ...
    @classmethod
    def from_spmatrix(cls, data): ...
    def __array__(self, dtype=..., copy=...) -> np.ndarray: ...
    def __setitem__(self, key, value) -> None: ...
    @property
    def sp_index(self): ...
    @property
    def sp_values(self): ...
    @property
    def dtype(self): ...
    @property
    def fill_value(self): ...
    @fill_value.setter
    def fill_value(self, value) -> None: ...
    @property
    def kind(self) -> str: ...
    def __len__(self) -> int: ...
    @property
    def nbytes(self) -> int: ...
    @property
    def density(self): ...
    @property
    def npoints(self) -> int: ...
    def isna(self): ...
    def fillna(self, value=..., method=..., limit=...): ...
    def shift(self, periods: int = ..., fill_value=...): ...
    def unique(self): ...
    def factorize(self, na_sentinel: int = ...): ...
    def value_counts(self, dropna: bool = ...): ...
    def __getitem__(self, key): ...
    def take(self, indices, allow_fill: bool = ..., fill_value=...): ...
    def searchsorted(self, v, side: str = ..., sorter=...): ...
    def copy(self): ...
    def astype(self, dtype=..., copy: bool = ...): ...
    def map(self, mapper): ...
    def to_dense(self): ...
    def nonzero(self): ...
    def all(self, axis=..., *args, **kwargs): ...
    def any(self, axis: int = ..., *args, **kwargs): ...
    def sum(self, axis: int = ..., *args, **kwargs): ...
    def cumsum(self, axis: int = ..., *args, **kwargs): ...
    def mean(self, axis: int = ..., *args, **kwargs): ...
    def transpose(self, *axes): ...
    @property
    def T(self): ...
    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs): ...
    def __abs__(self): ...

def make_sparse(arr, kind: str = ..., fill_value=..., dtype=..., copy: bool = ...): ...
