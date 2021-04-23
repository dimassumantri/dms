from flask import Flask,request,Response
from botbuilder.schema import Activity
from botbuilder.core import BotFrameworkAdapter,BotFrameworkAdapterSettings
import asyncio

from echobot import EchoBot

app = Flask(__name__)
loop = asyncio.get_event_loop()

botadaptersettings = BotFrameworkAdapterSettings("7d07150e-1682-4c90-ba5f-575f5569a06a","yy8qj.BOKJRZVe6.r8QUI.1_6OEb9~6SO4")
botadapter = BotFrameworkAdapter(botadaptersettings)

ebot = EchoBot()

@app.route("/api/messages",methods=["POST"])
def messages():
    if "application/json" in request.headers["content-type"]:
      jsonmessage = request.json
    else:
      return Response(status=415)

    activity = Activity().deserialize(jsonmessage)

    async def turn_call(turn_context):
        await ebot.on_turn(turn_context)

    task = loop.create_task(botadapter.process_activity(activity,"",turn_call))
    loop.run_until_complete(task)

if __name__ == '__main__':
    app.run('localhost',3978)

