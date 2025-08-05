import math
import matplotlib.pyplot as plt
import numpy as np

# Các hằng số về tỷ lệ cơ thể
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

hip_to_ankle = knee_to_ankle + hip_to_knee

# Giả định một class Pose cơ bản để lưu trữ tọa độ
class Pose:
    def __init__(self, x, y, z, name):
        self.x = x
        self.y = y
        self.z = z
        self.name = name

# --- TÍNH TOÁN TỌA ĐỘ BAN ĐẦU VÀ CUỐI CÙNG ---

# Đặt gót chân phải làm gốc tọa độ (0, 0, 0)
right_heel = Pose(0, 0, -0.05, "Right Heel")
right_hip = Pose(-hip_width, hip_to_heel_height, 0, "Right Hip")
right_knee = Pose(right_hip.x, right_hip.y - hip_to_knee, right_hip.z, "Right Knee")
right_ankle = Pose(right_hip.x, ankle_to_heel_height, right_hip.z, "Right Ankle")
right_toe = Pose(right_hip.x, 0, foot_length - 0.05, "Right Toe")

# Chân trái (chân giơ lên)
left_hip = Pose(hip_width, hip_to_heel_height, 0, "Left Hip")

# Định nghĩa các thông số cho Cử động 1
left_leg_hip_angle_deg = 82.65
initial_left_leg_angle_rad = math.radians(0)
final_left_leg_angle_rad = math.radians(left_leg_hip_angle_deg)
foot_angle_deg = 20
foot_angle_rad = math.radians(foot_angle_deg)

# --- TẠO CÁC ĐIỂM TƯ THẾ BAN ĐẦU VÀ CUỐI CÙNG ---
# Tư thế ban đầu của chân trái
initial_left_heel = Pose(hip_width/2, 0, -0.05, "Left Heel")
initial_left_toe = Pose(hip_width/2, 0, foot_length - 0.05, "Left Toe")
initial_left_ankle = Pose(hip_width/2, ankle_to_heel_height, 0, "Left Ankle")
initial_left_knee = Pose(hip_width/2, knee_to_heel_height, 0, "Left Knee")
initial_left_hip = Pose(hip_width/2, hip_to_heel_height, 0, "Left Hip")

# --- VẼ BIỂU ĐỒ MÔ PHỎNG CHUYỂN ĐỘ ---

fig, ax = plt.subplots(figsize=(6, 8))
ax.set_title(f"Mô phỏng chân trái giơ lên (góc {left_leg_hip_angle_deg}°) so với chân phải")
ax.set_xlabel("Trục Z (Độ sâu - Tiến/Lùi)")
ax.set_ylabel("Trục Y (Chiều cao)")
ax.grid(True)
ax.set_ylim(-0.05, 0.9)
ax.set_xlim(-0.1, 0.9)
ax.set_aspect('equal', adjustable='box')
plt.ion()

num_frames = 50
for i in range(num_frames + 1):
    t = i / num_frames
    
    

    # Nội suy góc nghiêng cho chân trái
    current_left_leg_angle_rad = (1 - t) * initial_left_leg_angle_rad + t * final_left_leg_angle_rad
    
    # Chiều dài các đoạn xương từ khớp hông trái
    length_hip_to_knee_left = hip_to_knee
    length_hip_to_ankle_left = hip_to_knee + knee_to_ankle
    length_hip_to_heel_left = hip_to_knee + knee_to_ankle + ankle_to_heel_height
    length_hip_to_toe_left = length_hip_to_ankle_left + foot_length # Khoảng cách từ hông đến ngón chân

    # Tính tọa độ của các khớp trên chân trái
    current_left_knee_y = initial_left_hip.y - (length_hip_to_knee_left * math.cos(current_left_leg_angle_rad))
    current_left_knee_z = initial_left_hip.z + (length_hip_to_knee_left * math.sin(current_left_leg_angle_rad))
    
    current_left_ankle_y = initial_left_hip.y - (length_hip_to_ankle_left * math.cos(current_left_leg_angle_rad))
    current_left_ankle_z = initial_left_hip.z + (length_hip_to_ankle_left * math.sin(current_left_leg_angle_rad))

    # Tính tọa độ bàn chân cuối cùng
    current_left_toe_y = initial_left_hip.y - ((length_hip_to_toe_left-0.1) * math.cos(current_left_leg_angle_rad +math.radians(11)))
    current_left_toe_z = initial_left_hip.z + ((length_hip_to_toe_left-0.1) * math.sin(current_left_leg_angle_rad +math.radians(11)))
    
    current_left_heel_y = initial_left_hip.y - (length_hip_to_heel_left * math.cos(current_left_leg_angle_rad - math.radians(5)))
    current_left_heel_z = initial_left_hip.z + (length_hip_to_heel_left * math.sin(current_left_leg_angle_rad -math.radians(5) ))


    ax.clear()
    ax.set_title(f"Mô phỏng chân trái giơ lên - Góc hiện tại: {math.degrees(current_left_leg_angle_rad):.1f}°")
    ax.set_xlabel("Trục Z (Độ sâu - Tiến/Lùi)")
    ax.set_ylabel("Trục Y (Chiều cao)")
    ax.set_ylim(-0.05, 0.9)
    ax.set_xlim(-0.1, 0.9)
    ax.grid(True)
    ax.set_aspect('equal', adjustable='box')
    
    # Vẽ chân phải (chân trụ)
    ax.plot(
        [right_toe.z, right_heel.z, right_ankle.z, right_knee.z, right_hip.z],
        [right_toe.y, right_heel.y, right_ankle.y, right_knee.y, right_hip.y],
        'o-', color='gray', label='Chân phải (trụ)', markersize=6
    )

    # Vẽ chân phải tạo thành tam giác nhỏ
    ax.plot(
        [right_toe.z, right_heel.z, right_ankle.z, right_toe.z],
        [right_toe.y, right_heel.y, right_ankle.y, right_toe.y],
        '--', color='gray', linewidth=1
    )

    # Vẽ chân trái (chuyển động)
    ax.plot(
        [current_left_heel_z, current_left_toe_z, current_left_ankle_z, current_left_knee_z, initial_left_hip.z],
        [current_left_heel_y, current_left_toe_y, current_left_ankle_y, current_left_knee_y, initial_left_hip.y],
        'o--', color='red', label='Chân trái', markersize=8
    )

    # Vẽ bàn chân trái tạo thành tam giác
    ax.plot(
        [current_left_toe_z, current_left_heel_z, current_left_ankle_z, current_left_toe_z],
        [current_left_toe_y, current_left_heel_y, current_left_ankle_y, current_left_toe_y],
        '--', color='red', linewidth=1
    )

    ax.text(right_hip.z, right_hip.y, ' Right Hip', color='gray')
    ax.text(initial_left_hip.z, initial_left_hip.y, ' Left Hip', color='red')
    ax.text(right_toe.z, right_toe.y, ' Right Toe', color='gray')
    ax.text(right_heel.z, right_heel.y, ' Right Heel', color='gray')
    ax.text(right_ankle.z, right_ankle.y, ' Right Ankle', color='gray')
    ax.text(right_knee.z, right_knee.y, ' Right Knee', color='gray')
    ax.legend()
    plt.draw()
    plt.pause(0.05)

plt.ioff()
plt.show()
