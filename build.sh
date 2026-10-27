#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
# Tự động nạp dữ liệu mẫu ban đầu nếu cần
# python seed_data.py