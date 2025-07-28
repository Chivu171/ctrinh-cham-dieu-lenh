from visitor import Visitor
from pose import Pose
class FirstActionVisitor(Visitor):
    """Lớp Visitor xử lý cử động 1 của động tác đi đều."""
    def __init__(self, step_length: float = 0.75, step_height: float = 0.1):
        self.step_length = step_length  # Độ dài bước (70-80 cm)
        self.step_height = step_height  # Chiều cao nâng chân

    def visit(self, pose: Pose):
        """Cập nhật tọa độ mặc định: giữ nguyên tọa độ."""
        return pose