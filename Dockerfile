FROM nginx

COPY build/* /usr/share/nginx/html/
COPY build/reveal.js/ /usr/share/nginx/html/reveal.js/
COPY images  /usr/share/nginx/html/images/
COPY TP/*.py /usr/share/nginx/html/codes/
