import telegram
from notion.client import NotionClient
import configparser

config = configparser.ConfigParser()
config.read('config.ini')


def get_config(key: str, section: str = 'default'):
    return config[section].get(key, None)


def send_tg_message(chat_id: int | str, text: str):
    bot = telegram.Bot(token=get_config('TG_TOKEN'))
    bot.send_message(chat_id=chat_id, text=text,
                     parse_mode=telegram.ParseMode.HTML)


def add_notion_row(url, data):
    # TODO: add candidate to notion
    raise NotImplementedError('Notion integration is not implemented yet')
    # notion = NotionClient(token_v2=get_config('NOTION_TOKEN'))
    # cv = notion.get_collection_view(url)
    # row = cv.collection.add_row()
    # row.name = data['name']
