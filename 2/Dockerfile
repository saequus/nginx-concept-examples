
FROM ubuntu:18.04
 

RUN apt-get -y update
RUN apt-get install -y nginx
 
# Set environment variables.
ENV HOME /root

# Define working directory.
WORKDIR /root

RUN rm /etc/nginx/nginx.conf

COPY ["nginx.conf", "/etc/nginx/nginx.conf"]

# Указываем Nginx запускаться на переднем плане (daemon off)
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
# В индексном файле меняем первое вхождение nginx на docker-nginx
RUN sed -i "0,/nginx/s/nginx/docker-nginx/i" /usr/share/nginx/html/index.html
# Запускаем Nginx. CMD указывает, какую команду необходимо запустить, когда контейнер запущен.
CMD [ "nginx" ]



