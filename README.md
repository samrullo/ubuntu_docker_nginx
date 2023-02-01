# Introduction

We are spinning up an ubuntu docker that comes with nginx and pyenv pre-installed

# Docker commands

```
docker commit -m "message" -a "author" <container> <image name>:<tag>
```


# How I installed tesseract on ubuntu docker

First ```apt-get update```

Then 

```
apt install tesseract-ocr libtesseract-dev
```

Then installed specific language

```
apt install tesseract-ocr-uzb
```
