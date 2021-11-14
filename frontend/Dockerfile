FROM node:14.5.0-alpine

RUN npm install -g http-server

WORKDIR /app

COPY package*.json ./
RUN npm install
COPY . .

RUN npm run build

CMD [ "http-server", "dist" ]