from signalbot import Command, Context


class BeepCommand(Command):
    def describe(self) -> str:
        return "🏓 Beep Command: Listen for a beep"

    async def handle(self, c: Context):
        command = c.message.text

        if "beep" in command.lower():
            await c.react('🤖')
            response = "boop"
            for x in range(command.lower().count("beep") - 1):
                response += " boop"
            await c.send(response)
            return
