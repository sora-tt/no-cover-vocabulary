# backend/Dockerfile
FROM python:3.13-slim

# 環境変数
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# 依存関係を先にコピーしてインストール
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# プロジェクトコードをコピー
COPY . .

# ポート公開
EXPOSE 8000

# gunicorn 起動（compose の command で上書き可能）
CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:8000", "--reload"]
