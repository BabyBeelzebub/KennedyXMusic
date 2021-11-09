from pyrogram import Client
from pytgcalls.types import Update
from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import InputStream
from pytgcalls.types.input_stream import InputAudioStream
from KennedyMusic.callsmusic.queues import queues
from KennedyMusic.config import API_HASH, API_ID, SESSION_NAME


client = Client(SESSION_NAME, API_ID, API_HASH)
pytgcalls = PyTgCalls(client)


@pytgcalls.on_stream_end()
async def on_stream_end(client: PyTgCalls, update: Update) -> None:
    chat_id = update.chat_id
    queues.task_done(chat_id)

    if queues.is_empty(chat_id):
        await pytgcalls.leave_group_call(chat_id)
    else:
        await pytgcalls.change_stream(
            chat_id,
            InputStream(
                InputAudioStream(
                    file_path,
                ),
            ),
        )

run = pytgcalls.start
