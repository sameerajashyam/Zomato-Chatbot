import chainlit as cl

from src.llm import ask_order,messages

@cl.on_message
async def main(message:cl.Message):
    #your custom logic goes here....
    messages.append({'role':'user','content':message.content})
    ask_order(messages)
    response=ask_order(messages)
    messages.append({'role':'assistant','content':response})
    await cl.Message(
        content=response,
    ).send()