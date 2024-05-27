from login import Login


class MainApp:
    """
    Основной класс для взаимодействия дочерних модулей
    """

    def __init__(self) -> None:
        self.run_app()

    def run_app(self):
        """
        Основной метод для добавления разных модулей
        """

        self.login = Login()
        role: str = self.login.get_role()
        
        if role is not None:
            self.__redirect_to_page(role)
            

    def __redirect_to_page(self, role: str):
        """
        Метод для перенаправления на страницы по роли
        """
        if role == 'admin':
            print(f"Ваша роль: {role}")
            # Перенаправить на страницу с ролью admin
            self.login.destroy()
            

        elif role == 'teacher':
            print(f"Ваша роль: {role}")
            # Перенаправить на страницу с ролью teacher
            self.login.destroy()
            

        elif role == 'staff':
            print(f"Ваша роль: {role}")
            # Перенаправить на страницу с ролью staff
            self.login.destroy()
            


if __name__ == "__main__":
    MainApp()
