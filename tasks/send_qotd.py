from actions.qotd import get_qotd


def send_qotd(bot):
    print("triggered send_qotd")
    bot.send(f"❓QOTD: {get_qotd()}")
