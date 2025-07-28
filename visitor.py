from abc import ABC, abstractmethod
from pose import Pose

class Visitor(ABC):
    """Lớp trừu tượng gốc cho Visitor."""
    @abstractmethod
    def visit(self, pose: Pose):
        pass