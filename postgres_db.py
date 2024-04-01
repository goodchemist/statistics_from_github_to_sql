import psycopg2


class PostgresDB:

    def __init__(self, db_name, params) -> None:
        """
        Создание экземпляра класса PostgresDB.
        :param db_name: имя базы данных
        """
        self.db_name = db_name
        self.params = params
        self.params.update({'dbname': self.db_name})

    def create_table(self) -> None:
        """
        Создает таблицу statistics для хранения статистики по репозиториям.
        :return: None
        """
        try:
            with psycopg2.connect(**self.params) as conn:
                with conn.cursor() as cur:

                    cur.execute("""CREATE TABLE IF NOT EXISTS statistics (
                        repository_id SERIAL PRIMARY KEY,
                        username VARCHAR(255) NOT NULL,
                        url TEXT NOT NULL,
                        description TEXT NOT NULL,
                        language VARCHAR(255) NOT NULL,
                        watchers INTEGER,
                        forks_count INTEGER
                        )
                        """)

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        finally:
            if conn is not None:
                conn.close()

    def insert_to_table(self):
        pass

    def get_to_json(self):
        pass

    def __repr__(self):
        pass

    def __str__(self):
        pass
