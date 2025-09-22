```mermaid
erDiagram
    regions ||--o{ tours : "регион тура"
    tour_categories ||--o{ tours : "категория тура"
    tours ||--o{ tour_photos : "фотографии тура"
    tours ||--o{ tour_schedules : "расписание тура"
    tour_schedules ||--o{ bookings : "бронирования"
    users ||--o{ bookings : "брони клиента"
    users ||--o{ audit_log : "изменения пользователя"
    users }o--o{ roles : "роли пользователя" via user_roles

    regions {
        integer id PK
        varchar(100) name "название (напр., 'Кавказ')"
        text description "описание региона"
    }

    tour_categories {
        integer id PK
        varchar(100) name "название (напр., 'Экскурсионный')"
        text description "описание категории"
    }

    tours {
        integer id PK
        varchar(200) title "название тура"
        text short_description "краткое описание"
        integer duration_days "длительность (дней)"
        decimal(10,2) price "цена"
        boolean is_active "активен (по умолч. TRUE)"
        timestamp created_at "дата создания"
        integer region_id FK "ссылка на регион"
        integer category_id FK "ссылка на категорию"
    }

    tour_photos {
        integer id PK
        varchar(200) photo_url "URL фотографии"
        varchar(255) description "описание фото"
        integer tour_id FK "ссылка на тур"
    }

    tour_schedules {
        integer id PK
        date start_date "дата начала"
        date end_date "дата окончания"
        integer available_seats "доступные места"
        integer tour_id FK "ссылка на тур"
    }

    bookings {
        integer id PK
        varchar(100) customer_name "имя клиента"
        varchar(100) email
        varchar(20) phone "телефон"
        integer seats "кол-во мест"
        timestamp booking_date "дата брони"
        boolean is_confirmed "подтверждено"
        integer schedule_id FK "ссылка на расписание"
        integer user_id FK "ссылка на пользователя (опц.)"
    }

    users {
        integer id PK
        varchar(50) username "логин"
        varchar(128) password "хэш пароля"
        varchar(50) first_name "имя"
        varchar(100) email
        varchar(20) phone "телефон"
        timestamp created_at "дата регистрации"
        jsonb settings "настройки (тема, формат даты)"
    }

    roles {
        integer id PK
        varchar(50) name "роль (Администратор, Пользователь, Аналитик)"
    }

    user_roles {
        integer id PK
        integer user_id FK "ссылка на пользователя"
        integer role_id FK "ссылка на роль"
    }

    audit_log {
        integer id PK
        varchar(100) table_name "название таблицы"
        char(1) operation "операция (I, U, D)"
        jsonb old_data "данные до изменения"
        jsonb new_data "данные после изменения"
        integer changed_by FK "ссылка на пользователя"
        timestamp change_time "время изменения"
    }
```
