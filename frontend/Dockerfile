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

# # build stage
# FROM node:lts-alpine as build-stage
# WORKDIR /app
# COPY package.json /app
# COPY package-lock.json /app
# RUN npm install

# COPY . /app
# RUN npm run build

# # production stage
# FROM nginx:stable-alpine as production-stage
# COPY --from=build-stage /app/dist /usr/share/nginx/html
# COPY nginx.conf /etc/nginx
# #USER root
# #RUN chmod 755 /usr/share/nginx/html
# #RUN chown -R nginx:nginx /usr/share/nginx/*
# EXPOSE 8080
# CMD ["nginx", "-g", "daemon off;"]

#######################################################################

#==================== Building Stage ================================================ 

# Create the image based on the official Node 8.9.0 image from Dockerhub
FROM node:8.9.0 as node

# Create a directory where our app will be placed. This might not be necessary
RUN mkdir -p /frontend

# Change directory so that our commands run inside this new directory
WORKDIR /frontend

# Copy dependency definitions
COPY package.json /frontend

# Install dependencies using npm
RUN npm install

# Get all the code needed to run the app
COPY . /frontend

# Expose the port the app runs in
EXPOSE 4200

#Build the app
RUN npm run build

#==================== Setting up stage ==================== 
# Create image based on the official nginx - Alpine image
FROM nginx:stable-alpine

COPY --from=node /frontend/dist/ /usr/share/nginx/html
COPY index.html /usr/share/nginx/html

COPY ./nginx-frontend.conf /etc/nginx/conf.d/default.conf

CMD ["nginx", "-g", "daemon off;"]

########################################################################

# FROM node:7.10.0
# # use changes to package.json to force Docker not to use the cache
# # when we change our application's nodejs dependencies:
# ADD package.json /tmp/package.json
# RUN cd /tmp && yarn install
# RUN mkdir -p /usr/src/app && cp -a /tmp/node_modules /usr/src/app
# # From here we load our application's code in, therefore the previous docker
# # "layer" thats been cached will be used if possible
# WORKDIR /usr/src/app
# ADD . /usr/src/app
# RUN npm run build
# RUN rm -rf ./build
# RUN rm -rf ./test
# RUN rm -rf ./src
# ENV PORT=80
# EXPOSE 80

# CMD [ "npm", "start" ]