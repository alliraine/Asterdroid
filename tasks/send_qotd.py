from actions.qotd import get_qotd
def send_qotd(bot):
    bot.send(get_qotd())