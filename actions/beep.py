from signalbot import Command, Context

class BeepCommand(Command):
    def describe(self) -> str:
        return "🏓 Beep Command: Listen for a beep"

    async def handle(self, c: Context):
        command = c.message.text

        if command == "beep":
            await c.send("boop")
            return