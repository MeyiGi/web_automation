from playwright.sync_api import Playwright, sync_playwright, expect
import time

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.facebook.com/register")
    page.get_by_label("Имя").click()
    page.get_by_label("Имя").fill("Даниэл")
    page.get_by_label("Фамилия").click()
    page.get_by_label("Фамилия").press("CapsLock")
    page.get_by_label("Фамилия").fill("К")
    page.get_by_label("Фамилия").press("CapsLock")
    page.get_by_label("Фамилия").fill("Каныбеков")
    page.get_by_label("Номер мобильного телефона или эл. адрес").click()
    page.get_by_label("Номер мобильного телефона или эл. адрес").fill("kanybekovdaniel6@gmail.com")
    time.sleep(1)
    page.get_by_label("Повторно введите ваш эл. адрес").click()
    page.get_by_label("Повторно введите ваш эл. адрес").fill("kanybekovdaniel6@gmail.com")
    page.get_by_label("Новый пароль").click()
    page.get_by_label("Новый пароль").fill("Samat.2004")
    page.get_by_label("Год").select_option("2004")
    page.get_by_label("Месяц").select_option("4")
    page.get_by_label("День").select_option("23")
    page.get_by_label("Мужчина").check()
    page.get_by_role("button", name="Регистрация").click()
    page.goto("https://www.facebook.com/")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)