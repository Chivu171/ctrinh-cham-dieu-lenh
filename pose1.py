
from side import Side


class Pose:
    def __init__(self, x:float , y: float , z:float , name:str, side:Side):
        self.x = x
        self.y = y
        self.z = z
        self.name = name
        self.side = side
    def update_coordinates(self, x:float , y: float , z:float):
        self.x = x
        self.y = y
        self.z = z


head_height = 0.13
neck_length = 0.129
shoulder_to_elbow = 0.188
elbow_to_wrist = 0.145
wrist_to_fingertip = 0.108
shoulder_width = 0.259
shoulder_to_heel_height = 0.818
wrist_to_heel_height = 0.485
upper_torso_length = 0.174
hip_width = 0.191
hip_to_knee = 0.245
knee_to_heel_height = 0.285
hip_to_heel_height = 0.530
knee_to_ankle = 0.246
ankle_to_heel_height = 0.039
foot_width = 0.055
foot_length = 0.152

# hai cổ chân
left_ankle = Pose(hip_width/2, ankle_to_heel_height, 0, "left_ankle", Side.LEFT)
right_ankle = Pose(-hip_width/2, ankle_to_heel_height, 0, "right_ankle", Side.RIGHT)

# hai đầu gối
left_knee = Pose(hip_width/2, knee_to_heel_height, 0, "left_knee", Side.LEFT)
right_knee = Pose(-hip_width/2, knee_to_heel_height, 0, "right_knee", Side.RIGHT)

# hai hông 
left_hip = Pose(hip_width/2, hip_to_heel_height, 0, "left_hip", Side.LEFT)
right_hip = Pose(-hip_width/2, hip_to_heel_height, 0, "right_hip", Side.RIGHT)

# hai vai
left_shoulder = Pose(shoulder_width/2, shoulder_to_heel_height, 0, "left_shoulder", Side.LEFT)
right_shoulder = Pose(-shoulder_width/2, shoulder_to_heel_height, 0, "right_shoulder", Side.RIGHT)

# hai cùi trỏ
left_elbow = Pose(shoulder_width/2, shoulder_to_heel_height - shoulder_to_elbow, 0, "left_elbow", Side.LEFT)
right_elbow = Pose(-shoulder_width/2, shoulder_to_heel_height - shoulder_to_elbow, 0, "right_elbow", Side.RIGHT)

# hai gót chân
left_heel = Pose(hip_width/2, 0, 0, "left_heel",Side.LEFT )
right_heel = Pose (hip_width/2, 0, 0,"right_heel",Side.RIGHT)

#cai co
neck = Pose(0,shoulder_to_heel_height + neck_length ,0)

#cai dau
head = Pose(0, shoulder_to_heel_height + neck_length+head_height,0 )

#hai cổ tay:
left_wrist = Pose(shoulder_width/2, wrist_to_heel_height, 0, "left_wrist", Side.LEFT)
right_wrist = Pose(-shoulder_width/2, wrist_to_heel_height, 0, "right_wrist", Side.RIGHT)








