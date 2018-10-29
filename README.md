# bearybot
just a chatbot for beary  
### 使用说明:
1.逻辑后端(backend)  
#### 创建数据库
数据库名 hubot_backend  
#### 装虚拟环境
pip install -r req.txt
#### 初始化数据库,启动后端
cd backend  
python manage.py migrate  
python manage.py runserver   0.0.0.0:6789
#### 启动用户端
cd user_side  
python rtm.py  


### 后端管理后台
0.0.0.0:6789/admin    
可以用python manage.py createsuperuser 创建后台管理用户
