import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
# from sklearn.linear_model import PassiveAggressiveRegressor

# ---------------------------
# 1. Sinh dữ liệu giả lập
# ---------------------------
np.random.seed(0)  # Đặt seed để kết quả có thể tái tạo

# Sinh 100 điểm dữ liệu cho biến X trong khoảng [0, 10]
X = 10 * np.random.rand(100, 1)
# Hàm mục tiêu: y = 2 + 3*x, cộng thêm nhiễu ngẫu nhiên (noise ~ N(0,1))
y = 2 + 3 * X+ np.random.randn(100, 1)

# Vẽ dữ liệu ban đầu
plt.figure(figsize=(8, 6))
plt.scatter(X, y, color='blue', label='Dữ liệu quan sát')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Dữ liệu Hồi Quy Tuyến Tính')
plt.legend()
plt.show()

# ---------------------------
# 2. Huấn luyện mô hình Linear Regression
# ---------------------------
model = LinearRegression()
model.fit(X, y)

# Lấy hệ số của mô hình
intercept = model.intercept_[0]
coef = model.coef_[0][0]
print("Hệ số chặn (Intercept):", intercept)
print("Hệ số góc (Coefficient):", coef)

# ---------------------------
# 3. Dự đoán và vẽ đường hồi quy
# ---------------------------
# Tạo một mảng các giá trị X mới để vẽ đường hồi quy
X_new = np.linspace(0, 10, 100).reshape(100, 1)
y_pred = model.predict(X_new)

plt.figure(figsize=(8, 6))
plt.scatter(X, y, color='blue', label='Dữ liệu quan sát')
plt.plot(X_new, y_pred, color='red', linewidth=2, label='Đường hồi quy')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Kết quả Hồi Quy Tuyến Tính')
plt.legend()
plt.show()
