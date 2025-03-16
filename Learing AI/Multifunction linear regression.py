import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Dữ liệu mẫu về giá nhà
data = {
    'Area': [1500, 1600, 1700, 1800, 1900],
    'Bedrooms': [3, 3, 4, 4, 5],
    'Age': [10, 15, 20, 25, 30],
    'Price': [300000, 320000, 340000, 360000, 380000]
}

# Chuyển dữ liệu thành DataFrame
df = pd.DataFrame(data)

# Chia dữ liệu thành đầu vào (X) và đầu ra (y)
X = df[['Area', 'Bedrooms', 'Age']]
y = df['Price']

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Tạo và huấn luyện mô hình hồi quy tuyến tính
model = LinearRegression()
model.fit(X_train, y_train)

# Dự đoán giá nhà trên tập kiểm tra
y_pred = model.predict(X_test)

# Đánh giá mô hình
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Dự đoán giá nhà mới
new_house = pd.DataFrame([[2000, 4, 15]], columns=['Area', 'Bedrooms', 'Age'])  # Thêm tên cột
predicted_price = model.predict(new_house)
print("Predicted Price for new house:", predicted_price[0])
