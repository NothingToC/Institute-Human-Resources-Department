import sqlite3 as sq


def get_cursor() -> sq.Cursor:
    """
    Получаем cursor для работы с нашей базой данных
    """
    connection = sq.connect("DataBase.db")
    cursor = connection.cursor()

    return cursor


class CreateDataBase:
    """
    Этот класс предназначен для создания базы данных
    """

    def __init__(self) -> None:
        """
        Конструктор класса CreateDataBase
        """

        # Вызываем функцию, которая создает базу данных
        self.__create_db()

    def __create_db(self) -> None:
        """
        Функция для создания базы данных
        """

        # Пробуем подключиться(или создать) к базе данных
        try:
            self.connection = sq.connect("DataBase.db")
            self.cursor = self.connection.cursor()

        # Если что-то пошло не так, выведется ошибка
        except sq.Error as error:
            print(error)

        # Если блок try не выдал исключений
        else:
            self.__create_tables()
            self.__create_super_user()

    def __create_super_user(self) -> None:
        """
        Функция для добавления супер пользователя
        """

        # Добавляем супер пользователя в нашу базу данных
        self.cursor.execute(
            """

            INSERT OR IGNORE INTO employees (name, second_name, surname, login, password, role, age, date_birth, status_vacation, status_retirement, status_pre_retirement, status_childless, status_many_children, status_veteran)
            VALUES ('David', 'Gabriel', 'Davis', 'admin', '1234', 'admin', 21, '01.01.2003', 'нет', 'нет', 'нет', 'нет', 'нет', 'нет')

        """
        )

        # Сохраняем изменения
        self.connection.commit()

    def __create_tables(self) -> None:
        """
        Функция для создания таблиц в базе данных
        """

        # Пробуем создать таблицы
        try:
            # Создаем таблицу с должностями
            self.cursor.execute(
                """

                                CREATE TABLE IF NOT EXISTS job_title(
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name TEXT NOT NULL UNIQUE,
                                    salary INTEGER NOT NULL
                                )

                                """
            )

            self.cursor.execute(
                """
                                INSERT OR IGNORE INTO job_title (name, salary)
                                VALUES ('Учитель истории', 30000);
                                """
            )

            self.cursor.execute(
                """
                                INSERT OR IGNORE INTO job_title (name, salary)
                                VALUES ('Уборщик', 20000);
                                """
            )

            self.cursor.execute(
                """
                                INSERT OR IGNORE INTO job_title (name, salary)
                                VALUES ('Системный администратор', 30000);
                                """
            )

            self.cursor.execute(
                """
                                INSERT OR IGNORE INTO job_title (name, salary)
                                VALUES ('Физрук', 100000);
                                """
            )

            self.cursor.execute(
                """

                                CREATE TABLE IF NOT EXISTS department(
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name TEXT NOT NULL UNIQUE
                                )

                                """
            )

            self.cursor.execute(
                """
                                INSERT OR IGNORE INTO department (name)
                                VALUES ('гумунитарный');
                                """
            )

            self.cursor.execute(
                """
                                INSERT OR IGNORE INTO department (name)
                                VALUES ('технический');
                                """
            )

            # Создаем таблицу с сотрудниками
            self.cursor.execute(
                """

                                CREATE TABLE IF NOT EXISTS employees(
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name TEXT NOT NULL,
                                    second_name TEXT NOT NULL,
                                    surname TEXT NOT NULL,
                                    login TEXT NOT NULL UNIQUE,
                                    password TEXT NOT NULL,
                                    role TEXT NOT NULL,
                                    age INTEGER NOT NULL,
                                    date_birth TEXT NOT NULL,
                                    status_vacation TEXT NOT NULL,
                                    status_retirement TEXT NOT NULL,
                                    status_pre_retirement TEXT NOT NULL,
                                    status_childless TEXT NOT NULL,
                                    status_many_children TEXT NOT NULL,
                                    status_veteran TEXT NOT NULL
                                )

                                """
            )

            # Создаем таблицу с вакансиями
            self.cursor.execute(
                """

                                CREATE TABLE IF NOT EXISTS job_vacancy(
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    id_job_title INTEGER NOT NULL,
                                    id_department INTEGER NOT NULL,
                                    vacancy_opening_date TEXT NOT NULL,
                                    vacancy_closing_date TEXT,

                                    FOREIGN KEY (id_job_title) REFERENCES job_title (id) ON DELETE CASCADE,
                                    FOREIGN KEY (id_department) REFERENCES department (id) ON DELETE CASCADE
                                )
                                
                                """
            )

            self.cursor.execute(
                """
                                INSERT OR IGNORE INTO job_vacancy(id_job_title, id_department, vacancy_opening_date, vacancy_closing_date)
                                VALUES (2, 1, "07.01.2024", NULL),
                                       (1, 2, "07.01.2024", "01.01.2025"),
                                       (4, 2, "01.01.2024", NULL),
                                       (3, 1, "05.03.2024", "01.01.2026");
                                """
            )

            # Создаем таблицу с сотрудниками и их должностями
            self.cursor.execute(
                """

                                CREATE TABLE IF NOT EXISTS employees_and_positions(
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    id_employee INTEGER NOT NULL,
                                    id_job_title TEXT NOT NULL,
                                    id_department INTEGER,
                                
                                    FOREIGN KEY (id_employee) REFERENCES employees (id) ON DELETE CASCADE,
                                    FOREIGN KEY (id_job_title) REFERENCES job_title (id) ON DELETE CASCADE,
                                    FOREIGN KEY (id_department) REFERENCES department (id) ON DELETE CASCADE
                                )

                                """
            )

            # Сохраняем таблицы
            self.connection.commit()

        # Выводим исключение, если оно есть
        except sq.Error as error:
            print(error)

    def __del__(self) -> None:
        """
        Деструктор класса CreateDataBase.\n
        Отрабатывает тогда, когда данный класс удаляется из кэша сборщиком мусора
        """

        # Закрываем все подключения
        self.connection.close()


if __name__ == "__main__":
    CreateDataBase()
