FROM node:18

# Устанавливаем директорию приложения внутри контейнера
WORKDIR /app

# Копируем зависимости и устанавливаем их
COPY package.json .
COPY package-lock.json .
RUN npm install

# Копируем остальные файлы приложения
COPY . .

# Собираем приложение
RUN npm run build

# Команда, которая будет выполнена при запуске контейнера
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
