from signalbot import Command, Context
import openai
import os
openai.organization = "org-39lwdYbHwZNWOWJ9k9IrCctR"
openai.api_key = os.getenv("OPENAI_API_KEY")

class AsterCommand(Command):
    def describe(self) -> str:
        return "OpenAI Trigger"

    async def handle(self, c: Context):
        command = c.message.text
        if "aster" in command.lower():
            await c.start_typing()
            await c.react('🤖')
            response = openai.ChatCompletion.create(
              model="gpt-3.5-turbo",
              messages=[
                {"role": "system", "content": "You are a chat bot called Asterbot. You are here to assisted The Constellation which consists of Alli, Jen, Ellie, and Sae. They are a queer polycule"},
                {"role": "user", "content": command}
              ]
            )
            await c.reply(response.choices[0].message)
            await c.stop_typing()
            return
