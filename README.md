# WarmCom

## Start
### First time
1. clone & cd
2. 複製檔案 `.env.example` 為 `.env`，並修改內容
3. 打開 terminal
4. 輸入 `pip install -r requirements.txt`
5. 輸入 `python manage.py createsuperuser`
6. 輸入 `python manage.py makemigrations chatbot`
7. 建立 `team_info.py` 在根目錄底下，並填入相關資訊
8. 在 terminal 輸入 `python manage.py shell`，並把 `seed.py` 所有內容貼入

### Every time
1. pull
2. 打開 terminal
3. 輸入 `python manage.py makemigrations`
4. 輸入 `python manage.py migrate`
5. 輸入 `python manage.py runserver`
