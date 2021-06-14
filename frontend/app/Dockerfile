FROM node:lts-alpine

RUN npm install -g http-server

RUN npm install -g @quasar/cli

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN quasar build -m pwa

EXPOSE 8080

CMD [ "http-server", "dist/pwa" ]