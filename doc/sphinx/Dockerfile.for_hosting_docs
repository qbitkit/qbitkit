FROM nginx:latest
ENV ContentDirectory=/usr/share/nginx/html/*
RUN rm -rf $ContentDirectory
COPY ./_build/html/* $ContentDirectory
