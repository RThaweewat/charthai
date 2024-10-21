from abc import ABC, abstractmethod
from typing import List

class BaseTokenizer(ABC):
    @abstractmethod
    def tokenize(self, text: str) -> List[str]:
        pass

# TODO: Implement the BaseTokenizer class
