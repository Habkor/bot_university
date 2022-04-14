from telegram.ext import CallbackContext, run_async
from telegram import ParseMode, Message
from typing import Optional


@run_async
def send_async_message(
    context: CallbackContext,
    message: str,
    chat_id: Optional[int] = None,
    parse_mode: ParseMode = ParseMode.HTML,
    **kwargs,
) -> Message:
    return context.bot.send_message(
        chat_id=chat_id,
        text=message,
        parse_mode=parse_mode,
        **kwargs,
    )

