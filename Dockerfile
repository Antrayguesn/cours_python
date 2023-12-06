FROM nginx

COPY *.html /usr/share/nginx/html/
COPY images  /usr/share/nginx/html/images/
COPY TP/*.py /usr/share/nginx/html/codes/
