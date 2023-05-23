import discord

class CommitUrl(discord.ui.View):
    def __init__(self, query: str):
        super().__init__()
        self.add_item(discord.ui.Button(label="点击前往", url=query))