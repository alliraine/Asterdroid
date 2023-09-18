import os
import time

import schedule
from signalbot import SignalBot
import logging
from actions import BeepCommand, QotdCommand, AsterCommand
from tasks.send_qotd import send_qotd

logging.getLogger().setLevel(logging.INFO)
logging.getLogger("apscheduler").setLevel(logging.WARNING)


def main():
    signal_service = os.environ["SIGNAL_SERVICE"]
    phone_number = os.environ["PHONE_NUMBER"]
    group_id = os.environ["GROUP_ID"]
    internal_id = os.environ["GROUP_INTERNAL_ID"]

    config = {
        "signal_service": signal_service,
        "phone_number": phone_number
    }
    bot = SignalBot(config)

    bot.register(BeepCommand())
    bot.register(QotdCommand())
    bot.register(AsterCommand())
    bot.start()

    bot.send(group_id, "I am aliveeeee")

    schedule.every(5).minutes.do(send_qotd, bot=bot)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
