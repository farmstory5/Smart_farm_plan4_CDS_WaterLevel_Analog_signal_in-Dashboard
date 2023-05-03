from abc import ABC, abstractmethod

class AbstractBackoff(ABC):
    def reset(self) -> None: ...
    @abstractmethod
    def compute(self, failures: int) -> float: ...

class ConstantBackoff(AbstractBackoff):
    def __init__(self, backoff: int) -> None: ...
    def compute(self, failures: int) -> float: ...

class NoBackoff(ConstantBackoff):
    def __init__(self) -> None: ...

class ExponentialBackoff(AbstractBackoff):
    def __init__(self, cap: float = 0.512, base: float = 0.008) -> None: ...
    def compute(self, failures: int) -> float: ...

class FullJitterBackoff(AbstractBackoff):
    def __init__(self, cap: float = 0.512, base: float = 0.008) -> None: ...
    def compute(self, failures: int) -> float: ...

class EqualJitterBackoff(AbstractBackoff):
    def __init__(self, cap: float = 0.512, base: float = 0.008) -> None: ...
    def compute(self, failures: int) -> float: ...

class DecorrelatedJitterBackoff(AbstractBackoff):
    def __init__(self, cap: float = 0.512, base: float = 0.008) -> None: ...
    def compute(self, failures: int) -> float: ...