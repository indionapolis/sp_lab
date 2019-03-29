FROM node:latest
WORKDIR /home
COPY package.json ./

RUN npm install
COPY . ./
CMD ["npm", "test"]
