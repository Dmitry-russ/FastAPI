# Api для хранения информации о сказочных существах.
По умолчанияю создано три класса существ: Dragon, Chimera, Basilisk. 
Api разработано с помощью FastAPI. Докуемнтация к проекту сформирована по умолчанию.
Api разработана без использования подключения к базе данных.
Возможность подключения в будущем предусмотрена проектом.

* Установка, настройка:

Клонируйте репозиторий, установите и активируйте виртуальное окружение:

Win:
```
python -m venv venv
venv/Scripts/activate
```
Mac:
```
python3 -m venv venv
source venv/bin/activate
```
Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
```
Запустите файл main
```
uvicorn main:app --reload
```
