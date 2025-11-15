# 📝 QA Service

Сервис вопросов и ответов на **FastAPI** с базой данных **PostgreSQL** и миграциями через **Alembic**.

---

## 🚀 Функционал

- CRUD для вопросов и ответов  
- Автоматическое управление датами создания (`created_at`)  
- Каскадное удаление ответов при удалении вопроса  
- Асинхронная работа с базой через **SQLAlchemy Async**  

---

## 🛠️ Технологии

- Python 3.12  
- FastAPI  
- SQLAlchemy (Async + ORM)  
- PostgreSQL 
- Alembic для миграций  
- Docker & Docker Compose  

---

## ⚡ Быстрый старт с Docker

### 1️⃣ Клонируем репозиторий

```bash
git clone <your_repo_url>
cd <repo_folder>
```

### 2️⃣ Создаем .env на основе .example.env

```bash
cp .example.env .env
```
и заполните реальные значения

### 3️⃣ Запускаем контейнеры

```bash
docker-compose up --build
```

### 4️⃣ Применяем миграции

```bash
docker-compose exec web alembic upgrade head
```
### 🌐 Доступ к сервису

После запуска FastAPI будет доступен:
```
Swagger UI: http://localhost:8000/docs
Redoc: http://localhost:8000/redoc
```

### 🏗️ Структура проекта

<pre>
  qa_service/
├── alembic/
│   ├── versions/                  # Файлы миграций
│   ├── env.py                     # Конфиг Alembic
│   └── script.py.mako             # Шаблон Alembic
├── src/
│   ├── apps/
│   │   ├── common/
│   │   │   ├── __init__.py 
│   │   │   └── models.py          # Mixin модели
│   │   ├── questions/
│   │   │   ├── __init__.py  
│   │   │   ├── schemas.py         # Pydantic схемы
│   │   │   ├── mapper.py          # DTO маппер
│   │   │   ├── models.py          # Модели
│   │   │   ├── repository.py      # Репозиторий с crud
│   │   │   └── routers.py         # Роуты
│   │   └── answers/
│   │   │   ├── __init__.py
│   │   │   ├── schemas.py         # Pydantic схемы
│   │   │   ├── mapper.py          # DTO маппер
│   │   │   ├── models.py          # Модели
│   │   │   ├── repository.py      # Репозиторий с crud
│   │   │   └── routers.py         # Роуты
│   ├── database.py                # Настройки базы данных
│   └── main.py                    # FastAPI приложение
├── tests/
│   ├── conftest.py                # Фикстуры для тестов
│   ├── test_questions.py
│   └── test_answers.py
├── .env.example                   # Пример переменных окружения
├── requirements.txt               # Python зависимости
├── docker-compose.yml
├── Dockerfile
└── README.md
</pre>
