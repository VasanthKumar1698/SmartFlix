FROM nginx:alpine

RUN rm -rf /usr/share/nginx/html/*

COPY ./app/templates/ /usr/share/nginx/html/

RUN chmod -R 755 /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]

# Trigger build
