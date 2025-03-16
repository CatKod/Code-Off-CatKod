import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Tạo dữ liệu ngẫu nhiên: Diện tích (m2), Số phòng ngủ, Số tầng -> Giá nhà (triệu VND)
np.random.seed(42)  # Đặt seed để tái tạo kết quả
X_area = np.random.randint(50, 300, size=100)  # Diện tích từ 50 đến 300 m2
X_rooms = np.random.randint(1, 7, size=100)  # Số phòng ngủ từ 1 đến 6
X_floors = np.random.randint(1, 4, size=100)  # Số tầng từ 1 đến 3
X = np.column_stack((X_area, X_rooms, X_floors))  # Kết hợp diện tích, số phòng ngủ và số tầng

# Giá nhà được tính dựa trên diện tích, số phòng ngủ, số tầng với một chút nhiễu
y = 50 * X_area + 200 * X_rooms + 300 * X_floors + np.random.randint(-500, 500, size=100)  # Giá nhà (triệu VND)

# Chia dữ liệu thành tập huấn luyện và kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Tạo Polynomial Features (đa thức bậc 2)
poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

# Huấn luyện mô hình Linear Regression trên dữ liệu đa thức
model = LinearRegression()
model.fit(X_train_poly, y_train)

# Dự đoán trên tập kiểm tra
y_pred = model.predict(X_test_poly)

# Đánh giá mô hình
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Hiển thị kết quả dự đoán
print("Thực tế vs Dự đoán:")
for actual, predicted in zip(y_test, y_pred):
    print(f"Thực tế: {actual} triệu, Dự đoán: {predicted:.2f} triệu")

# Vẽ biểu đồ minh họa (chỉ với diện tích để dễ hình dung)
plt.scatter(X[:, 0], y, color='blue', label='Dữ liệu thực tế')
plt.scatter(X_test[:, 0], y_pred, color='red', label='Dự đoán')
plt.xlabel('Diện tích (m2)')
plt.ylabel('Giá nhà (triệu VND)')
plt.legend()
plt.title('Dự đoán giá nhà với Polynomial Regression')
plt.show()