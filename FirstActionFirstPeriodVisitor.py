# first_action_first_period.py
from pose import Pose, Side, LeftKnee, RightKnee, LeftWrist, RightWrist, LeftAnkle, RightAnkle
from visitor import FirstActionVisitor
from constant import *
import math

class FirstActionFirstPeriod(FirstActionVisitor):
    """Visitor cho cử động 1 của động tác đi đều."""
    def __init__(self, duration=1.0):
        self.duration = duration

    def visit_left_knee(self, left_knee: LeftKnee):
        pass

    def visit_right_knee(self, right_knee: RightKnee):
        pass

    def visit_left_wrist(self, left_wrist: LeftWrist):
        pass

    def visit_right_wrist(self, right_wrist: RightWrist):
        pass

    def visit_left_ankle(self, left_ankle: LeftAnkle):
        pass

    def visit_right_ankle(self, right_ankle: RightAnkle):
        pass

    def visit_left_hip(self, left_hip):
        pass

    def visit_right_hip(self, right_hip):
        pass

    def visit_left_shoulder(self, left_shoulder):
        pass

    def visit_right_shoulder(self, right_shoulder):
        pass

    def visit_left_elbow(self, left_elbow):
        pass

    def visit_right_elbow(self, right_elbow):
        pass

    def visit_left_heel(self, left_heel):
        pass

    def visit_right_heel(self, right_heel):
        pass

    def visit_neck(self, neck):
        pass

    def visit_head(self, head):
        pass

    def visit(self, pose: Pose):
        """Phương thức chung: gọi phương thức cụ thể dựa trên loại pose."""
        if isinstance(pose, LeftKnee):
            return self.visit_left_knee(pose)
        elif isinstance(pose, RightKnee):
            return self.visit_right_knee(pose)
        elif isinstance(pose, LeftWrist):
            return self.visit_left_wrist(pose)
        elif isinstance(pose, RightWrist):
            return self.visit_right_wrist(pose)
        elif isinstance(pose, LeftAnkle):
            return self.visit_left_ankle(pose)
        elif isinstance(pose, RightAnkle):
            return self.visit_right_ankle(pose)
        return pose  # Mặc định: giữ nguyên tọa độ