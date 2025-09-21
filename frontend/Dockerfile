# frontend/Dockerfile
FROM node:20

WORKDIR /app

# 依存関係をキャッシュするために package.json だけ先にコピー
COPY package*.json ./

RUN npm install

# プロジェクトコードをコピー
COPY . .

EXPOSE 3000

CMD ["npm", "start"]
