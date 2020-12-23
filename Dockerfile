FROM python:3.6.0

ENV PYTHONUNBUFFERED 1

#Chạy lệnh tạo thư mục mới trong image
RUN mkdir /demo-server

WORKDIR /demo-server

# Cập nhật pip của image
RUN pip install --upgrade pip

#Copy source code vào image
COPY . .

# Set quyền run cho file .sh
RUN chmod +x docker-entrypoint.sh
