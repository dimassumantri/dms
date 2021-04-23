from flask import Flask,request,Response
from botbuilder.schema import Activity
from botbuilder.core import BotFrameworkAdapter,BotFrameworkAdapterSettings
import asyncio

from echobot import EchoBot

app = Flask(__name__)
loop = asyncio.get_event_loop()

botadaptersettings = BotFrameworkAdapterSettings("94d0f980-12c5-4c0c-a5b1-0444be6f51d8","I3Zof~6bVFD8ik.EuQ~k.di-CiVV56jzzK")
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
    app.run('localhost',3978 )

