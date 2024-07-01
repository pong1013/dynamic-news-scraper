## Introduction

A Django-based web application to automatically scrape focal news from the UDN NBA website using Scrapy, store the data in a database with appropriate Django models, and display the news dynamically using Django REST Framework and AJAX. The application includes celery scheduled scraping and is deployed to a server on GCP for live operation.

## Start server

Run git project or docker image:

- Clone this project
    
    ```shell
    git clone https://github.com/pong1013/django-scrapy.git
    ```
    
    Run `start.sh`
    
    ```shell
    cd udn_nba
    ./start.sh
    ```
    
- Pull Image
    
    ```shell
    docker pull pong1013/udn-nba
    docker run -p 8000:8000 -p 6379:6379 pong1013/udn-nba
    ```
## Deploy on GCP
Go to cloud shell.
1. Pull Image
    ```shell
    sudo docker pull pong1013/udn-nba:hello_latest
    sudo docker run -d --platform linux/arm64 -p 8000:8000 -p 6379:6379 pong1013/udn-nba:hello_latest
    ```
2. List running container and check logs
    ```shell
    sudo docker ps
    sudo docker logs <container_id>
    ```
3. Access web
    ```shell
    http://[EXTERNAL_IP]:8000
    ```
    [Demo video](https://drive.google.com/file/d/1PwxEXjzfb9MtCpBypuNRhSzT1l_Mt8Xr/view?usp=drive_link)
