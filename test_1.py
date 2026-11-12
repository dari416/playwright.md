# ФИО: Алеександрова Дарья
# Дата: 2026-12-11
# Время: 14:30
# Описание: этот код представляет собой два автоматических тестов с использованием библиотеки Playwright.они проверяют работу офицального сайта Playwright
import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # Ожидать, что заголовок содержит подстроку
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Кликнуть по ссылке "Get Started" (начать работу)
    page.get_by_role("link", name="Get started").click()

    # ожидать, что на странице есть заголовок с названием "installation" установка
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()
    