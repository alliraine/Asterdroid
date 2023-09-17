import os

from actions.qotd import get_qotd


def send_qotd(bot):
    print("triggered send_qotd")
    bot.send(os.environ["GROUP_ID"], f"❓QOTD: {get_qotd()}")
