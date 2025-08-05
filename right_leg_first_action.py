import math
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D # Import cho vẽ 3D

# Các hằng số về tỷ lệ cơ thể
hip_width = 0.191
hip_to_knee = 0.245 # Chiều dài đùi (Knee-Hip)
knee_to_heel_height = 0.285 # Chiều cao từ gót chân đến đầu gối
hip_to_heel_height = hip_to_knee + knee_to_heel_height # Chiều cao từ gót chân đến hông
knee_to_ankle = 0.246 # Chiều dài cẳng chân (Ankle-Knee)
ankle_to_heel_height = 0.039 # Chiều dài từ gót chân đến mắt cá chân
foot_length = 0.152 # Chiều dài bàn chân (Toe-Heel)

# Giả định một class Pose cơ bản để lưu trữ tọa độ
class Pose:
    def __init__(self, x, y, z, name):
        self.x = x
        self.y = y
        self.z = z
        self.name = name

# --- TÍNH TOÁN TỌA ĐỘ BAN ĐẦU VÀ CUỐI ---

# Tư thế ban đầu (đứng thẳng) - Định nghĩa dựa trên gót chân (Heel) ở y=0
# Để bàn chân nằm ngang: Toe ở Z dương, Heel ở Z âm
initial_x = 0 # Tất cả các khớp của chân này sẽ có X = 0

initial_heel_y = 0
initial_heel_z = -0.05

initial_toe_y = 0
initial_toe_z = foot_length # Toe ở 0.152

initial_ankle_y = ankle_to_heel_height # Ankle nằm trên heel
initial_ankle_z = 0 # Ankle thẳng hàng với gót chân ban đầu

initial_knee_y = knee_to_heel_height # Knee nằm trên ankle
initial_knee_z = 0 # Knee thẳng hàng với ankle ban đầu

initial_hip_y = hip_to_heel_height # Hip nằm trên knee
initial_hip_z = 0 # Hip thẳng hàng với knee ban đầu


# Định nghĩa các thông số cho Cử động 1
right_leg_lean_angle_deg = 39 # Góc nghiêng tối đa của cẳng chân/đùi so với phương thẳng đứng
final_lean_angle_rad = math.radians(right_leg_lean_angle_deg)
initial_lean_angle_rad = 0

# Góc nghiêng riêng cho bàn chân: từ 0 độ (ngang) đến 90 độ (vuông góc OZ)
final_foot_angle_rad = math.radians(90) # Mũi chân - Gót chân sẽ vuông góc với OZ
initial_foot_angle_rad = 0


# --- VỊ TRÍ TƯƠNG ĐỐI BAN ĐẦU GIỮA CÁC KHỚP (để áp dụng xoay) ---
# Tọa độ tương đối của Heel so với Toe
initial_heel_rel_toe_z = initial_heel_z - initial_toe_z
initial_heel_rel_toe_y = initial_heel_y - initial_toe_y

# Tọa độ tương đối của Ankle so với Toe (để xoay toàn bộ bàn chân)
initial_ankle_rel_toe_z = initial_ankle_z - initial_toe_z
initial_ankle_rel_toe_y = initial_ankle_y - initial_toe_y

# Tọa độ tương đối của Knee so với Ankle
initial_knee_rel_ankle_z = initial_knee_z - initial_ankle_z
initial_knee_rel_ankle_y = initial_knee_y - initial_ankle_y

# Tọa độ tương đối của Hip so với Knee
initial_hip_rel_knee_z = initial_hip_z - initial_knee_z
initial_hip_rel_knee_y = initial_hip_y - initial_knee_y


# --- VẼ BIỂU ĐỒ MÔ PHỎNG CHUYỂN ĐỘ ---

fig = plt.figure(figsize=(8, 8)) # Tạo figure
ax = fig.add_subplot(111, projection='3d') # Thêm subplot 3D

ax.set_title(f"Mô phỏng chân phải (Chân thẳng, bàn chân xoay) - 3D")
ax.set_xlabel("Trục X (Ngang)")
ax.set_ylabel("Trục Y (Chiều cao)")
ax.set_zlabel("Trục Z (Độ sâu - Tiến/Lùi)") # Thêm nhãn cho trục Z
ax.grid(True)
ax.set_ylim(-0.05, initial_hip_y + 0.1) 
ax.set_zlim(-0.3, 0.3) # Giới hạn lại Z cho 3D
ax.set_xlim(-0.1, 0.1) # Giới hạn X nhỏ vì chân này có X=0

plt.ion()
num_frames = 10

for i in range(num_frames + 1):
    t = i / num_frames

    # Nội suy góc xoay cho từng đoạn
    current_leg_angle_rad = (1 - t) * initial_lean_angle_rad + t * final_lean_angle_rad
    current_foot_angle_rad = (1 - t) * initial_foot_angle_rad + t * final_foot_angle_rad
    
    # --- CÔNG THỨC XOAY (XOAY THEO CHIỀU KIM ĐỒNG HỒ TRONG MẶT PHẲNG YZ, TỨC QUANH TRỤC X) ---
    # new_rel_z = old_rel_z * cos(angle) + old_rel_y * sin(angle)
    # new_rel_y = old_rel_y * cos(angle) - old_rel_z * sin(angle)
    
    # Mũi chân (Toe) - Vị trí cố định (là điểm xoay chính)
    current_toe_x = initial_x
    current_toe_z = initial_toe_z
    current_toe_y = initial_toe_y

    # Gót chân (Heel) - Xoay quanh Toe
    current_heel_rel_z = initial_heel_rel_toe_z * math.cos(current_foot_angle_rad) + initial_heel_rel_toe_y * math.sin(current_foot_angle_rad)
    current_heel_rel_y = initial_heel_rel_toe_y * math.cos(current_foot_angle_rad) - initial_heel_rel_toe_z * math.sin(current_foot_angle_rad)
    current_heel_x = initial_x # X không đổi
    current_heel_z = current_toe_z + current_heel_rel_z
    current_heel_y = current_toe_y + current_heel_rel_y
    
    # Mắt cá chân (Ankle) - Xoay quanh Toe (cùng với bàn chân)
    current_ankle_rel_z_from_toe = initial_ankle_rel_toe_z * math.cos(current_foot_angle_rad) + initial_ankle_rel_toe_y * math.sin(current_foot_angle_rad)
    current_ankle_rel_y_from_toe = initial_ankle_rel_toe_y * math.cos(current_foot_angle_rad) - initial_ankle_rel_toe_z * math.sin(current_foot_angle_rad)
    current_ankle_x = initial_x # X không đổi
    current_ankle_z = current_toe_z + current_ankle_rel_z_from_toe
    current_ankle_y = current_toe_y + current_ankle_rel_y_from_toe

    # Đầu gối (Knee) - Xoay quanh Ankle
    current_knee_rel_ankle_z = initial_knee_rel_ankle_z * math.cos(current_leg_angle_rad) + initial_knee_rel_ankle_y * math.sin(current_leg_angle_rad)
    current_knee_rel_ankle_y = initial_knee_rel_ankle_y * math.cos(current_leg_angle_rad) - initial_knee_rel_ankle_z * math.sin(current_leg_angle_rad)
    current_knee_x = initial_x # X không đổi
    current_knee_z = current_ankle_z + current_knee_rel_ankle_z
    current_knee_y = current_ankle_y + current_knee_rel_ankle_y
    
    # Hông (Hip) - Xoay quanh Knee
    current_hip_rel_knee_z = initial_hip_rel_knee_z * math.cos(current_leg_angle_rad) + initial_hip_rel_knee_y * math.sin(current_leg_angle_rad)
    current_hip_rel_knee_y = initial_hip_rel_knee_y * math.cos(current_leg_angle_rad) - initial_hip_rel_knee_z * math.sin(current_leg_angle_rad)
    current_hip_x = initial_x # X không đổi
    current_hip_z = current_knee_z + current_hip_rel_knee_z
    current_hip_y = current_knee_y + current_hip_rel_knee_y


    ax.clear()
    ax.set_title(f"Mô phỏng chân phải - Tiến độ: {t*100:.0f}%")
    ax.set_xlabel("Trục X (Ngang)")
    ax.set_ylabel("Trục Y (Chiều cao)")
    ax.set_zlabel("Trục Z (Độ sâu - Tiến/Lùi)") # Thêm nhãn cho trục Z
    ax.set_ylim(-0.05, initial_hip_y + 0.1)
    ax.set_zlim(-0.3, 0.3)
    ax.set_xlim(-0.1, 0.1)
    ax.grid(True)
    # ax.set_aspect('equal', adjustable='box') # adjustable='box' không hoạt động với 3D

    # Vẽ tư thế ban đầu (để làm mốc so sánh) - Toàn bộ chân
    ax.plot(
        [initial_x, initial_x, initial_x, initial_x, initial_x], # Dùng initial_x cho tất cả X
        [initial_hip_y, initial_knee_y, initial_ankle_y, initial_heel_y, initial_toe_y],
        [initial_hip_z, initial_knee_z, initial_ankle_z, initial_heel_z, initial_toe_z],
        'o-', color='gray', label='Tư thế ban đầu', markersize=6
    )

    # Vẽ tư thế hiện tại (trong animation)
    # Vẽ từng đoạn riêng biệt để kiểm soát tốt hơn và hiển thị đầy đủ
    ax.plot(
        [current_hip_x, current_knee_x],
        [current_hip_y, current_knee_y],
        [current_hip_z, current_knee_z],
        'o--', color='red', label='Chân phải hiện tại', markersize=8
    )
    ax.plot(
        [current_knee_x, current_ankle_x],
        [current_knee_y, current_ankle_y],
        [current_knee_z, current_ankle_z],
        'o--', color='red', markersize=8
    )
    ax.plot(
        [current_ankle_x, current_heel_x], # Ankle nối với Heel
        [current_ankle_y, current_heel_y],
        [current_ankle_z, current_heel_z],
        'o--', color='red', markersize=8
    )
    ax.plot(
        [current_heel_x, current_toe_x], # Heel nối với Toe (bàn chân)
        [current_heel_y, current_toe_y],
        [current_heel_z, current_toe_z],
        'o--', color='red', markersize=8
    )
    ax.plot(
        [current_ankle_x, current_toe_x], # Ankle nối với Heel
        [current_ankle_y, current_toe_y],
        [current_ankle_z, current_toe_z],
        'o--', color='red', markersize=8
    )

    # Đoạn này vẽ lại Ankle-Toe, có thể không cần thiết nếu coi Heel-Toe-Ankle là khối cứng
    # ax.plot(
    #     [current_ankle_x, current_toe_x],
    #     [current_ankle_y, current_toe_y],
    #     [current_ankle_z, current_toe_z],
    #     'o--', color='red', markersize=8
    # )


    ax.text(current_hip_x, current_hip_y, current_hip_z, '  Hip', color='red')
    ax.text(current_knee_x, current_knee_y, current_knee_z, '  Knee', color='red')
    ax.text(current_ankle_x, current_ankle_y, current_ankle_z, '  Ankle', color='red')
    ax.text(current_heel_x, current_heel_y, current_heel_z, '  Heel', color='red')
    ax.text(current_toe_x, current_toe_y, current_toe_z, '  Toe', color='red')
    ax.legend()
    plt.draw()
    plt.pause(0.05)

plt.ioff()
plt.show()