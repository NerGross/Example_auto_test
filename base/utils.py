from selenium.webdriver.remote.webelement import WebElement
import cx_Oracle
import config


class Utils:
    """
       Описывает общие методы работы.
       """

    # получаем строковый список -> возвращаем строку с разделителем
    @staticmethod
    def join_strings(str_list: list[str]) -> str:
        return ";".join(str_list)

    # получаем список WebElement -> возвращаем строковый список
    @staticmethod
    def get_text_from_webelements(elements) -> list[str]:
        return [element.text for element in elements]

    # получаем список WebElement, искомое название -> возвращаем WebElement
    @staticmethod
    def get_element_by_name(elements: list[WebElement], name: str) -> WebElement:
        name = name.lower()
        for element in elements:
            if element.text.lower().__contains__(name):  # если текстовое представление элемента содержит name
                return element

    # получаем словарь WebElement, искомое название -> возвращаем WebElement
    @staticmethod
    def get_dict_element_by_name(elements: dict[WebElement], name: str) -> WebElement:
        name = name.lower()
        for key, value in elements.items():
            if key.text.lower() == name:
                return value

    @staticmethod
    def sql_clear(sql):
        try:
            with cx_Oracle.connect(user=config.db_config["user"], password=config.db_config["password"],
                                   dsn=config.db_config["dsn"], encoding='utf8') as connection:
                print('SQL: ', sql)
                print("Connection to MySQL DB successful")
                with connection.cursor() as cursor:
                    cursor.execute(sql)
                    connection.commit()
                    cursor.close()
                    connection.close()
                    print("Connection to MySQL DB closed")

        except cx_Oracle.Error as e:
            print(e)

    @staticmethod
    def sql_script(sql: str):
        try:
            with cx_Oracle.connect(user=config.db_config["user"], password=config.db_config["password"],
                                   dsn=config.db_config["dsn"], encoding='utf8') as connection:
                print('SQL: ', sql)
                print("Connection to MySQL DB successful")
                with connection.cursor() as cursor:
                    cursor.execute(sql)
                    result = cursor.fetchall()
                    cursor.close()
                    connection.close()
                    print("Connection to MySQL DB closed")
                    print(result)
                    return 'sql = ', result

        except cx_Oracle.Error as error:
            print(error)
