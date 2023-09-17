from signalbot import Command, Context


class BeepCommand(Command):
    def describe(self) -> str:
        return "🏓 Beep Command: Listen for a beep"

    async def handle(self, c: Context):
        command = c.message.text
        print(command)
        if "beep" in command.lower():
            await c.start_typing()
            await c.react('🤖')
            response = "boop"
            for x in range(command.lower().count("beep") - 1):
                response += " boop"
            await c.reply(response)
            await c.stop_typing()
            return
