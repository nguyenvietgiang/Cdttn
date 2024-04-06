FROM python:3.10.4

# Thiết lập thư mục làm việc của ứng dụng
WORKDIR /app

# Sao chép mã nguồn của ứng dụng vào container
COPY . /app

# Cài đặt các phụ thuộc Python từ tệp requirements.txt
RUN pip install -r requirements.txt

# Mở cổng cho Django chạy trên container
EXPOSE 8000

# Lệnh khởi động máy chủ Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]