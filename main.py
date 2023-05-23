# fastapi 相关
from fastapi import FastAPI, Request, Header
import uvicorn

# discord 相关
import discord

# 其他
import globals
import asyncio
import model
import json
from view import CommitUrl


app = FastAPI() # 创建 api 对象

bot = discord.Client(intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('Logged on as {0}!'.format(bot.user))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content.startswith('$hello'):
        await send_github_commit_message()
        
async def send_github_commit_message(root: model.Root):
    channel = bot.get_channel(globals.DISCROD_BOT_DEV_CHANNEL_ID)
    await channel.send(f"""
    收到一个新的提交喵！
    提交人：{root.head_commit.committer.name}
    提交信息：{root.head_commit.message}
    以下文件发生了修改：{root.head_commit.modified}
    以下文件添加了: {root.head_commit.added}
    以下文件被删除了：{root.head_commit.removed}""", view=CommitUrl(root.head_commit.url))

@app.post("/webhook")
async def webhook(request: Request):
    # send_github_commit_message()
    payload = await request.json()
    root = model.Root.parse_raw(json.dumps(payload))
    await send_github_commit_message(root)
    return {"message": "Unable to process action"}

@app.on_event("startup")
async def startup_event():
    # 开启 discord 机器人
    asyncio.create_task(bot.start(globals.DISCROD_BOT_TOKEN))
    await asyncio.sleep(4) #optional sleep for established connection with discord
    print(f"{bot.user} has connected to Discord!")

if __name__ == "__main__":
    print("Starting FastAPI")
    uvicorn.run(app=app, port=7860, host="0.0.0.0")