from selenium.webdriver.chrome.options import Options
from signalbot import Command, Context
from bs4 import BeautifulSoup
import requests
from selenium import webdriver

class QotdCommand(Command):
    def describe(self) -> str:
        return "🏓 Beep Command: Listen for a beep"

    async def handle(self, c: Context):
        command = c.message.text

        if command == "qotd":
            print("command qotd triggered")
            await c.react('🤖')
            options = Options()
            options.headless = True
            driver = webdriver.Chrome(options=options)
            driver.get('https://randomwordgenerator.com/question.php')
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            s = soup.find('ol', id='result')
            qotd = s.find('span', class_='support-sentence')
            await c.send(f"❓QOTD: {qotd.text}")
            driver.quit()
            return