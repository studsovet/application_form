import os
import telegram
from notion.client import NotionClient


def send_tg_message(chat_id: int | str, text: str):
    bot = telegram.Bot(token=os.environ.get("TG_TOKEN"))
    bot.send_message(chat_id=chat_id, text=text,
                     parse_mode=telegram.ParseMode.HTML)


def add_notion_row(url, data):
    # TODO: add candidate to notion
    raise NotImplementedError('Notion integration is not implemented yet')
    # notion = NotionClient(token_v2=get_config('NOTION_TOKEN'))
    # cv = notion.get_collection_view(url)
    # row = cv.collection.add_row()
    # row.name = data['name']
