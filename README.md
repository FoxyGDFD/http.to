# Запуск приложения:


## Windows:
---
### 1. Создаем виртуальное окружение
```bash
python -m venv venv
```

### 2. Активируем виртуальное окрудение
```bash
.\venv\Scripts\activate
```

### 3. Устанавливаем зависимости
```bash
pip install -r requirements.txt
```

### 4. Переходим в рабочую директорию проекта
```bash
 cd .\web
```

### 5. Применяем миграции 
```bash
python manage.py migrate
```

### 6. Запускаем сервер разработки
```bash
python manage.py runserver
```


## MacOS/Linux:
---
### 1. Создаем виртуальное окружение
```bash
python3 -m venv venv
```

### 2. Активируем виртуальное окрудение
```bash
source venv/bin/activate
```

### 3. Устанавливаем зависимости
```bash
pip install -r requirements.txt
```

### 4. Переходим в рабочую директорию проекта
```bash
 cd ./web
```

### 5. Применяем миграции 
```bash
python3 manage.py migrate
```

### 6. Запускаем сервер разработки
```bash
python3 manage.py runserver
```

# Запуск приложения с docker
---
## 1. Установите docker: `https://docs.docker.com/engine/install/`
## 2. В директории проекта выполните команду 
```bash
docker compose -f ./compose-dev.yml up
```