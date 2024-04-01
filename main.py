from config import config
from functions import get_repos_stats
from postgres_db import PostgresDB


def main():
    # Получаем статистику по репозиториям пользователя через API GitHub
    data = get_repos_stats('goodchemist')

    # Параметры для подключения к БД берем из конфигурационного файла
    params = config()

    # Создаём экземпляр класса PostgresDB
    postgres_db = PostgresDB('github', params)

    # Создаём таблицу для хранения информации
    postgres_db.create_table('statistics')

    # Записываем данные в таблицу
    postgres_db.insert_to_table('statistics', data)

    # Получаем данные из таблицы
    data_from_table = postgres_db.get_data_from_postgres('statistics')

    # Записываем данные в JSON-файл
    postgres_db.save_to_json(data_from_table, 'github_stats')


if __name__ == '__main__':
    main()
