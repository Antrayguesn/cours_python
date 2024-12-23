FROM nginx

<<<<<<< HEAD
COPY build/* /usr/share/nginx/html/
COPY build/reveal.js/ /usr/share/nginx/html/reveal.js/
COPY images  /usr/share/nginx/html/images/
COPY TP/*.py /usr/share/nginx/html/codes/
COPY TP/TP_0/* /usr/share/nginx/html/codes/
=======
COPY *.html /usr/share/nginx/html/
COPY images /usr/share/nginx/html/
>>>>>>> 465d731 (Modif)
