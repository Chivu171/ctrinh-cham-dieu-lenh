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
initial_toe_z = -foot_length

# Định nghĩa các thông số cho Cử động 1
right_leg_lean_angle_deg = 39
right_leg_lean_angle_deg_heel = 90
initial_lean_angle_rad = 0  # Góc ban đầu là 0 độ (đứng thẳng)
final_lean_angle_rad = math.radians(right_leg_lean_angle_deg)
final_lean_angle_rad_heel = math.radians(right_leg_lean_angle_deg_heel)

# --- VẼ BIỂU ĐỒ MÔ PHỎNG CHUYỂN ĐỘNG ---

fig, ax = plt.subplots(figsize=(6, 8))
ax.set_title(f"Mô phỏng chuyển động của chân phải (Nội suy góc nghiêng)")
ax.set_xlabel("Trục Z (Độ sâu - Tiến/Lùi)")
ax.set_ylabel("Trục Y (Chiều cao)")
ax.grid(True)
ax.set_ylim(-0.05, 0.9)
ax.set_xlim(-0.9, 0.9)
ax.set_aspect('equal', adjustable='box')

plt.ion()
num_frames = 20
for i in range(num_frames + 1):
    # Tính toán tiến độ của animation (t từ 0.0 đến 1.0)
    t = i / num_frames

    # --- NỘI SUY GÓC NGHIÊNG ---
    # Nội suy tuyến tính cho góc nghiêng của toàn bộ chân
    current_lean_angle_rad = (1 - t) * initial_lean_angle_rad + t * final_lean_angle_rad
    current_angle_heel = (1 - t) * initial_lean_angle_rad + t * final_lean_angle_rad_heel
    # Sử dụng góc nghiêng hiện tại để tính tọa độ Y và Z
    # của tất cả các khớp. Chân luôn thẳng tắp.
    
    total_leg_length = hip_to_knee + knee_to_ankle + ankle_to_heel_height
    length_heel_to_knee = knee_to_ankle + ankle_to_heel_height
    length_heel_to_ankle = ankle_to_heel_height

    # Tính toán tọa độ hiện tại
    current_hip_y = total_leg_length * math.cos(current_lean_angle_rad)
    current_hip_z = 0 - (total_leg_length * math.sin(current_lean_angle_rad))
    
    current_knee_y = length_heel_to_knee * math.cos(current_lean_angle_rad)
    current_knee_z = 0 - (length_heel_to_knee * math.sin(current_lean_angle_rad))

    current_ankle_y = length_heel_to_ankle * math.cos(current_lean_angle_rad)
    current_ankle_z = 0 - (length_heel_to_ankle * math.sin(current_lean_angle_rad))
    
    # Tọa độ gót chân luôn cố định
    current_heel_y = foot_length * math.cos(right_leg_lean_angle_deg_heel)
    current_heel_z = initial_heel_z * math.cos(right_leg_lean_angle_deg_heel)

    current_toe_z = initial_toe_z
    current_toe_y = initial_toe_y

    


    ax.clear()
    ax.set_title(f"Mô phỏng chân phải (Nội suy góc nghiêng) - Tiến độ: {t*100:.0f}%")
    ax.set_xlabel("Trục Z (Độ sâu - Tiến/Lùi)")
    ax.set_ylabel("Trục Y (Chiều cao)")
    ax.set_ylim(-0.2, 0.9)
    ax.set_xlim(-0.9, 0.9)
    ax.grid(True)
    ax.set_aspect('equal', adjustable='box')
    
    # Vẽ tư thế ban đầu (để làm mốc so sánh)
    ax.plot(
        [initial_heel_z, initial_ankle_z, initial_knee_z, initial_hip_z],
        [initial_heel_y, initial_ankle_y, initial_knee_y, initial_hip_y],
        'o-', color='gray', label='Tư thế ban đầu', markersize=6
    )

    # Vẽ tư thế hiện tại (trong animation)
    ax.plot(
        [current_heel_z, current_ankle_z, current_knee_z, current_hip_z],
        [current_heel_y, current_ankle_y, current_knee_y, current_hip_y],
        'o--', color='red', label='Chân phải hiện tại', markersize=8
    )

    ax.text(current_hip_z, current_hip_y, '  Hip', color='red')
    ax.text(current_knee_z, current_knee_y, '  Knee', color='red')
    ax.text(current_ankle_z, current_ankle_y, '  Ankle', color='red')
    ax.text(current_heel_z, current_heel_y, '  Heel', color='red')
    ax.text(current_toe_z,current_toe_y, ' Toe', color = 'red')
    ax.legend()
    plt.draw()
    plt.pause(0.05)

plt.ioff()
plt.show()