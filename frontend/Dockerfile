# FROM node:lts-alpine

# # install simple http server for serving static content
# RUN npm install -g http-server

# # make the 'app' folder the current working directory
# WORKDIR /app

# # copy both 'package.json' and 'package-lock.json' (if available)
# COPY package.json /app
# COPY package-lock.json /app

# # install project dependencies
# RUN npm install

# # copy project files and folders to the current working directory (i.e. 'app' folder)
# COPY . /app

# # build app for production with minification
# RUN npm run build

# EXPOSE 8080
# CMD [ "http-server", "dist" , "-p", "8080" ]

# build stage
FROM node:lts-alpine as build-stage
WORKDIR /app
COPY package.json /app
COPY package-lock.json /app
RUN npm install

COPY . /app
RUN npm run build

# production stage
FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx
#USER root
#RUN chmod 755 /usr/share/nginx/html
#RUN chown -R nginx:nginx /usr/share/nginx/*
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]