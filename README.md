<h1>Интернет - магазин</h1>
<br>
запуск redis
<br>
brew services start redis
запуск celery 
<br>
celery -A myshop worker --loglevel=info 
<br>
celery -A myshop beat -l info
<br>
запуск Flower
celery -A myshop flower
<br>
url
http://localhost:5555/dashboard
