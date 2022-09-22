# WarmCom

## Start
### First time
1. clone & cd
2. 複製檔案 `.env.example` 為 `.env`，並修改內容
3. 打開 terminal
4. 輸入 `pip install -r requirements.txt`
5. 輸入 `python manage.py createsuperuser`
6. 輸入 `python manage.py makemigrations chatbot`

### Every time
1. pull
2. 打開 terminal
3. 輸入 `python manage.py makemigrations`
4. 輸入 `python manage.py migrate`
5. 輸入 `python manage.py runserver`
