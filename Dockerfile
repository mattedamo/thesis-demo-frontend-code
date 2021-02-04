# Stage 1
FROM node:12-alpine AS build 
WORKDIR /frontend 
COPY . .
RUN npm i
RUN npm run build --prod

# Stage 2
FROM nginx:1.17.1
COPY ./nginx.conf /etc/nginx/conf.d/default.conf 
COPY --from=build /frontend/dist/thesis-microservices-app-frontend /usr/share/nginx/html/
