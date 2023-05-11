from selenium.webdriver.chrome.options import Options
from signalbot import Command, Context
from bs4 import BeautifulSoup
import requests
from selenium import webdriver


def get_qotd():
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get('https://randomwordgenerator.com/question.php')
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    s = soup.find('ol', id='result')
    driver.quit()
    return s.find('span', class_='support-sentence').text


class QotdCommand(Command):
    def describe(self) -> str:
        return "🏓 Beep Command: Listen for a beep"

    async def handle(self, c: Context):
        command = c.message.text

        if command == "qotd":
            print("command qotd triggered")
            await c.react('🤖')
            qotd = get_qotd()
            await c.send(f"❓QOTD: {qotd}")
            return
