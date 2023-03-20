import cx_Oracle
import config


class Oracle:
    def __init__(self):
        self.cursor = None
        self.connect = None

    def connect_node(self, user=config.db_config["user"], password=config.db_config["password"],
                     dsn=config.db_config["dsn"]):
        """Подключение к БД"""
        try:
            self.connect = cx_Oracle.connect(user=user, password=password, dsn=dsn, encoding='utf8')
            print('SQL: ', 'Connection to MySQL DB successful')
            self.cursor = self.connect.cursor()
        except cx_Oracle.DatabaseError:
            raise

    def disconnect_node(self):
        """Отключение от БД"""
        try:
            self.cursor.close()
            self.connect.close()
            print('SQL: ', 'Connection to MySQL DB closed')
        except cx_Oracle.DatabaseError:
            raise

    def fetchall_node(self, sql):
        """Запрос в SQL"""
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def execute_node(self, sql, commit=False):
        """Выполнение SQL"""
        self.cursor.execute(sql)
        if commit:
            self.connect.commit()


def bd_read(sql):
    bd = None
    try:
        bd = Oracle()
        bd.connect_node()
        yield bd.fetchall_node(sql)
    except Exception:
        raise
    finally:
        bd.disconnect_node()


def bd_write(sql):
    bd = None
    try:
        bd = Oracle()
        bd.connect_node()
        yield bd.execute_node(sql)
    except Exception:
        raise
    finally:
        bd.disconnect_node()
