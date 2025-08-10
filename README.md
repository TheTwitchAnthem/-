# Process Scanner - Security Tool


Простой инструмент для мониторинга процессов в Windows, который:
- Проверяет запущенные и приостановленные процессы
- Сравнивает с базой опасных и безопасных процессов
- Ищет информацию о неизвестных процессах через браузер

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/yourusername/process-scanner.git
cd process-scanner
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

## Использование

Запустите главное приложение:
```bash
python main.py
```

### Функционал:
- Вкладка "Active" - активные процессы
- Вкладка "Suspended" - приостановленные процессы
- Кнопка "Scan All" - запускает проверку
- Кнопка "Research Unknown" - ищет информацию о неизвестных процессах

## Структура проекта

```
process-scanner/
├── main.py              # Основное приложение
├── process_checker.py   # Проверка процессов
├── process_researcher.py# Поиск информации
├── danger.json          # База опасных процессов
├── save.json            # База безопасных процессов
├── requirements.txt     # Зависимости
└── README.md            # Этот файл
```
