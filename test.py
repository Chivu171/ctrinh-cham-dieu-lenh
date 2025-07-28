import math
import matplotlib.pyplot as plt
import numpy as np

# Các hằng số về tỷ lệ cơ thể
hip_width = 0.191
hip_to_knee = 0.245
knee_to_heel_height = 0.285
hip_to_heel_height = hip_to_knee + knee_to_heel_height
knee_to_ankle = 0.246
ankle_to_heel_height = 0.039
foot_length = 0.152

# Giả định một class Pose cơ bản để lưu trữ tọa độ
class Pose:
    def __init__(self, x, y, z, name):
        self.x = x
        self.y = y
        self.z = z
        self.name = name

# --- TÍNH TOÁN TỌA ĐỘ BAN ĐẦU VÀ CUỐI ---

# Tư thế ban đầu (đứng thẳng)
initial_hip_y = hip_to_heel_height
initial_hip_z = 0

initial_knee_y = knee_to_heel_height
initial_knee_z = 0

initial_ankle_y = ankle_to_heel_height
initial_ankle_z = 0

initial_heel_y = 0
initial_heel_z = 0

initial_toe_y = 0
initial_toe_z = foot_length

# Định nghĩa các thông số cho Cử động 1
right_leg_lean_angle_deg =39
final_lean_angle_rad = math.radians(right_leg_lean_angle_deg)
initial_lean_angle_rad = 0

# Góc nghiêng riêng cho bàn chân: từ 0 độ (song song OZ) đến 90 độ (vuông góc OZ)
final_foot_angle_rad = math.radians(90)
initial_foot_angle_rad = 0
final_ankle_angle_rad  = math.radians (100)


# Vị trí cố định của mũi chân (điểm xoay)
pivot_z = initial_toe_z
pivot_y = initial_toe_y

# Vị trí ban đầu của các khớp so với điểm xoay (mũi chân)
initial_heel_rel_z = initial_heel_z - pivot_z
initial_heel_rel_y = initial_heel_y - pivot_y

initial_ankle_rel_z = initial_ankle_z - pivot_z
initial_ankle_rel_y = initial_ankle_y - pivot_y

initial_knee_rel_z = initial_knee_z - pivot_z
initial_knee_rel_y = initial_knee_y - pivot_y

initial_hip_rel_z = initial_hip_z - pivot_z
initial_hip_rel_y = initial_hip_y - pivot_y

# --- VẼ BIỂU ĐỒ MÔ PHỎNG CHUYỂN ĐỘ ---

fig, ax = plt.subplots(figsize=(6, 8))
ax.set_title(f"Mô phỏng chân phải (Mũi chân cố định)")
ax.set_xlabel("Trục Z (Độ sâu - Tiến/Lùi)")
ax.set_ylabel("Trục Y (Chiều cao)")
ax.grid(True)
ax.set_ylim(-0.05, 0.9)
ax.set_xlim(-0.9, 0.9)
ax.set_aspect('equal', adjustable='box')

plt.ion()
num_frames = 20

for i in range(num_frames + 1):
    t = i / num_frames

    current_leg_angle_rad = (1 - t) * initial_lean_angle_rad + t * final_lean_angle_rad
    current_foot_angle_rad = (1 - t) * initial_foot_angle_rad + t * final_foot_angle_rad
    
    # --- CÔNG THỨC XOAY CHÍNH XÁC (XOAY THEO CHIỀU KIM ĐỒNG HỒ) ---
    
    # Gót chân (Heel) - Sử dụng góc xoay của bàn chân
    current_heel_z = pivot_z + initial_heel_rel_z * math.cos(current_foot_angle_rad) + initial_heel_rel_y * math.sin(current_foot_angle_rad)
    current_heel_y = pivot_y + initial_heel_rel_y * math.cos(current_foot_angle_rad) - initial_heel_rel_z * math.sin(current_foot_angle_rad)
    
    # Mắt cá chân (Ankle) - Sử dụng góc xoay của chân
    current_ankle_z = pivot_z + initial_ankle_rel_z * math.cos(current_leg_angle_rad) + initial_ankle_rel_y * math.sin(current_leg_angle_rad)
    current_ankle_y = pivot_y + initial_ankle_rel_y * math.cos(current_leg_angle_rad) - initial_ankle_rel_z * math.sin(current_leg_angle_rad)

    # Đầu gối (Knee) - Sử dụng góc xoay của chân
    current_knee_z = pivot_z + initial_knee_rel_z * math.cos(current_leg_angle_rad) + initial_knee_rel_y * math.sin(current_leg_angle_rad)
    current_knee_y = pivot_y + initial_knee_rel_y * math.cos(current_leg_angle_rad) - initial_knee_rel_z * math.sin(current_leg_angle_rad)
    
    # Hông (Hip) - Sử dụng góc xoay của chân
    current_hip_z = pivot_z + initial_hip_rel_z * math.cos(current_leg_angle_rad) + initial_hip_rel_y * math.sin(current_leg_angle_rad)
    current_hip_y = pivot_y + initial_hip_rel_y * math.cos(current_leg_angle_rad) - initial_hip_rel_z * math.sin(current_leg_angle_rad)

    # Mũi chân (Toe) - Vị trí cố định
    current_toe_z = initial_toe_z
    current_toe_y = initial_toe_y

    ax.clear()
    ax.set_title(f"Mô phỏng chân phải - Tiến độ: {t*100:.0f}%")
    ax.set_xlabel("Trục Z (Độ sâu - Tiến/Lùi)")
    ax.set_ylabel("Trục Y (Chiều cao)")
    ax.set_ylim(-0.05, 0.9)
    ax.set_xlim(-0.9, 0.9)
    ax.grid(True)
    ax.set_aspect('equal', adjustable='box')
    
    # Vẽ tư thế ban đầu (để làm mốc so sánh)
    ax.plot(
        [initial_hip_z, initial_knee_z, initial_ankle_z, initial_heel_z, initial_toe_z],
        [initial_hip_y, initial_knee_y, initial_ankle_y, initial_heel_y, initial_toe_y],
        'o-', color='gray', label='Tư thế ban đầu', markersize=6
    )

    # Vẽ tư thế hiện tại (trong animation)
    ax.plot(
        [current_hip_z, current_knee_z, current_ankle_z, current_toe_z],
        [current_hip_y, current_knee_y, current_ankle_y, current_toe_y],
        'o--', color='red', label='Chân phải hiện tại', markersize=8
    )
    # Vẽ phần bàn chân (Toe - Heel)
    ax.plot(
        [current_toe_z, current_heel_z],
        [current_toe_y, current_heel_y],
        'o--', color='red', markersize=8
    )

    ax.text(current_hip_z, current_hip_y, '  Hip', color='red')
    ax.text(current_knee_z, current_knee_y, '  Knee', color='red')
    ax.text(current_ankle_z, current_ankle_y, '  Ankle', color='red')
    ax.text(current_heel_z, current_heel_y, '  Heel', color='red')
    ax.text(current_toe_z, current_toe_y, '  Toe', color='red')
    ax.legend()
    plt.draw()
    plt.pause(0.05)

plt.ioff()
plt.show()