FROM python:3.6.0

ENV PYTHONUNBUFFERED 1

#Chạy lệnh tạo thư mục mới trong container
RUN mkdir /sourcecode

WORKDIR /sourcecode

# Cập nhật pip của container
RUN pip install --upgrade pip

COPY docker-entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh
