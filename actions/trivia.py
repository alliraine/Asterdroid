from signalbot import Command, Context
from trivia import trivia

curr = None

class Trivia:
  def __init__(self, category, type, difficulty, question, correct_answer):
    self.category = category
    self.type = type
    self.difficulty = difficulty
    self.question = question
    self. correct_answer = correct_answer


class TriviaCommand(Command):
    def describe(self) -> str:
        return "🏓 Beep Command: Listen for a beep"

    async def handle(self, c: Context):
        command = c.message.text
        global curr

        if command == "trivia":
            await c.start_typing()
            print("command trivia triggered")
            await c.react('🤖')
            question = await trivia.question(amount=1, category=0, difficulty='easy', quizType='multiple')
            q = question[0]
            curr = Trivia(q.get("category"), q.get("type"), q.get("difficulty"), q.get("question"), q.get("correct_answer"))
            res = f"🧠Today's trivia is in the {curr.category} category! \n❓Question: {curr.question}"
            await c.reply(f"{res}")
            await c.stop_typing()
            return

        if command == "trivia answer":
            await c.start_typing()
            print("command trivia triggered")
            await c.react('🤖')
            await c.reply(f"The answer is: {curr.correct_answer}")
            await c.stop_typing()
            return
