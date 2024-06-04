# Python Web Spider

- [x] 抓取 http://tw-nba.udn.com/nba/index 中的焦點新聞。
- [x] 使用 [Django](https://www.djangoproject.com/) 設計恰當的 Model，並將所抓取新聞存儲至 DB。
- [x] 使用 [Django REST Framework](http://www.django-rest-framework.org/) 配合 AJAX 實現以下頁面：
	 * 焦點新聞列表
	 * 新聞詳情頁面
- [x] 以 Pull-Request 的方式將代碼提交。
	
## 進階要求
- [x] 使用 Scrapy。
- [x] 實現爬蟲自動定時抓取。
- [ ] 使用 Websocket 服務，抓取到新的新聞時立即通知前端頁面。
- [x] 將本 demo 部署到伺服器並可正確運行。
- [ ] 所實現新聞列表 API 可承受 100 QPS 的壓力測試。

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
