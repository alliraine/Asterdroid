from signalbot import Command, Context, triggered


def get_qotd():
    file = open("data/random_questions.csv", "r")
    questions = file.read()
    question_list = questions.split('\n')

    question = question_list[0]

    with open('data/random_questions.csv', 'w') as fp:
        fp.write('\n'.join(question_list[1:]))

    return question


class QotdCommand(Command):
    def describe(self) -> str:
        return "🏓 Beep Command: Listen for a beep"

    @triggered("qotd")
    async def handle(self, c: Context):
        await c.start_typing()
        print("command qotd triggered")
        await c.react('🤖')
        qotd = get_qotd()
        await c.reply(f"❓QOTD: {qotd}")
        await c.stop_typing()
        return
