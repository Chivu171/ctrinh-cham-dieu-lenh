# pose.py
from enum import Enum
from abc import ABC, abstractmethod
from constant import *

class Side(Enum):
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    NONE = "NONE"

class Pose(ABC):
    """Lớp trừu tượng đại diện cho một điểm pose."""
    def __init__(self, x: float, y: float, z: float, name: str, side: Side):
        self.x = x
        self.y = y
        self.z = z
        self.name = name
        self.side = side

    @abstractmethod
    def accept(self, visitor):
        pass

    def __str__(self):
        return f"Pose(name={self.name}, side={self.side.value}, x={self.x:.4f}, y={self.y:.4f}, z={self.z:.4f})"

class LeftKnee(Pose):
    def __init__(self):
        super().__init__(
            x=hip_width / 2,  # 0.0955
            y=knee_to_heel_height,  # 0.285
            z=0.0,
            name="left_knee",
            side=Side.LEFT
        )

    def accept(self, visitor):
        return visitor.visit_left_knee(self)

class RightKnee(Pose):
    def __init__(self):
        super().__init__(
            x=-hip_width / 2,  # -0.0955
            y=knee_to_heel_height,  # 0.285
            z=0.0,
            name="right_knee",
            side=Side.RIGHT
        )

    def accept(self, visitor):
        return visitor.visit_right_knee(self)

class LeftWrist(Pose):
    def __init__(self):
        super().__init__(
            x=shoulder_width / 2,  # 0.1295
            y=wrist_to_heel_height,  # 0.485
            z=0.0,
            name="left_wrist",
            side=Side.LEFT
        )

    def accept(self, visitor):
        return visitor.visit_left_wrist(self)

class RightWrist(Pose):
    def __init__(self):
        super().__init__(
            x=-shoulder_width / 2,  # -0.1295
            y=wrist_to_heel_height,  # 0.485
            z=0.0,
            name="right_wrist",
            side=Side.RIGHT
        )

    def accept(self, visitor):
        return visitor.visit_right_wrist(self)

# Thêm các lớp con khác nếu cần, ví dụ:
class LeftAnkle(Pose):
    def __init__(self):
        super().__init__(
            x=hip_width / 2,  # 0.0955
            y=ankle_to_heel_height,  # 0.039
            z=0.0,
            name="left_ankle",
            side=Side.LEFT
        )

    def accept(self, visitor):
        return visitor.visit_left_ankle(self)

class RightAnkle(Pose):
    def __init__(self):
        super().__init__(
            x=-hip_width / 2,  # -0.0955
            y=ankle_to_heel_height,  # 0.039
            z=0.0,
            name="right_ankle",
            side=Side.RIGHT
        )

    def accept(self, visitor):
        return visitor.visit_right_ankle(self)

# Có thể thêm các lớp khác như LeftHeel, RightHeel, Neck, Head, v.v.

class LeftHip(Pose):
    def __init__(self):
        super().__init__(
            x=hip_width / 2,
            y=hip_to_heel_height,
            z=0.0,
            name="left_hip",
            side=Side.LEFT
        )
    def accept(self, visitor):
        return visitor.visit_left_hip(self)

class RightHip(Pose):
    def __init__(self):
        super().__init__(
            x=-hip_width / 2,
            y=hip_to_heel_height,
            z=0.0,
            name="right_hip",
            side=Side.RIGHT
        )
    def accept(self, visitor):
        return visitor.visit_right_hip(self)

class LeftShoulder(Pose):
    def __init__(self):
        super().__init__(
            x=shoulder_width / 2,
            y=shoulder_to_heel_height,
            z=0.0,
            name="left_shoulder",
            side=Side.LEFT
        )
    def accept(self, visitor):
        return visitor.visit_left_shoulder(self)

class RightShoulder(Pose):
    def __init__(self):
        super().__init__(
            x=-shoulder_width / 2,
            y=shoulder_to_heel_height,
            z=0.0,
            name="right_shoulder",
            side=Side.RIGHT
        )
    def accept(self, visitor):
        return visitor.visit_right_shoulder(self)

class LeftElbow(Pose):
    def __init__(self):
        super().__init__(
            x=shoulder_width / 2,
            y=shoulder_to_heel_height - shoulder_to_elbow,
            z=0.0,
            name="left_elbow",
            side=Side.LEFT
        )
    def accept(self, visitor):
        return visitor.visit_left_elbow(self)

class RightElbow(Pose):
    def __init__(self):
        super().__init__(
            x=-shoulder_width / 2,
            y=shoulder_to_heel_height - shoulder_to_elbow,
            z=0.0,
            name="right_elbow",
            side=Side.RIGHT
        )
    def accept(self, visitor):
        return visitor.visit_right_elbow(self)

class LeftHeel(Pose):
    def __init__(self):
        super().__init__(
            x=hip_width / 2,
            y=0.0,
            z=0.0,
            name="left_heel",
            side=Side.LEFT
        )
    def accept(self, visitor):
        return visitor.visit_left_heel(self)

class RightHeel(Pose):
    def __init__(self):
        super().__init__(
            x=-hip_width / 2,
            y=0.0,
            z=0.0,
            name="right_heel",
            side=Side.RIGHT
        )
    def accept(self, visitor):
        return visitor.visit_right_heel(self)

class Neck(Pose):
    def __init__(self):
        super().__init__(
            x=0.0,
            y=shoulder_to_heel_height + neck_length,
            z=0.0,
            name="neck",
            side=Side.NONE
        )
    def accept(self, visitor):
        return visitor.visit_neck(self)

class Head(Pose):
    def __init__(self):
        super().__init__(
            x=0.0,
            y=shoulder_to_heel_height + neck_length + head_height,
            z=0.0,
            name="head",
            side=Side.NONE
        )
    def accept(self, visitor):
        return visitor.visit_head(self)