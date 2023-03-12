import allure
import config
from TestEnter.pom.enterLocator import EnterLocator


class EnterFixtureTrue(EnterLocator):
    def __init__(self, driver):
        super().__init__(driver)

    def enter(self):
        enter = EnterLocator(self.driver)
        with allure.step("Загрузки страницы ввода логина и пароля"):
            enter.get_button("Войти")
        with allure.step('Вход в ЛК'):
            enter.get_auth("Логин").send_keys(config.enter["l_curator"])
            enter.get_auth("Пароль").send_keys(config.enter["p_curator"])
            enter.get_button("Войти").click()
        with allure.step("Загрузки страницы выбор компании"):
            enter.get_not_button("Войти")
            assert enter.get_drop_down_meaning("Страхование ТС")
        with allure.step('Переход по меню'):
            enter.get_menu("Объекты страхования").click()
            enter.get_menu("Транспортные средства").click()
        with allure.step("Транспортные средства"):
            enter.get_not_drop_down_meaning("Страхование ТС")
