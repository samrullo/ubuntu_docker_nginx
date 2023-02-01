FROM samrullo/ubuntu_2204_nginx_pyenv_python-3.9.14
COPY data/mysimplewsgi/mysimplewsgi.service /etc/systemd/system/
COPY data/mysimplewsgi/nginx/mysimplewsgi.conf /etc/nginx/sites-available
RUN ln -s /etc/nginx/sites-available/mysimplewsgi.conf /etc/nginx/sites-enabled/