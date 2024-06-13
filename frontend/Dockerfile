FROM node:16-alpine

WORKDIR /app

COPY package.json package-lock.json ./

RUN npm install -g serve

RUN npm install

COPY . ./

RUN npm run build

EXPOSE 5000

CMD ["serve", "-s", "build", "-l", "5000"]
