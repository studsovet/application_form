import telegram
from notion.client import NotionClient
import configparser

config = configparser.ConfigParser()
config.read('config.ini')


def get_config(key, section='default'):
    return config[section][key]


def send_tg_message(chat_id, text):
    bot = telegram.Bot(token=get_config('TG_TOKEN'))
    bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)


def add_notion_row(url, data):
    # TODO: add candidate to notion
    pass
    # notion = NotionClient(token_v2=get_config('NOTION_TOKEN'))
    # cv = notion.get_collection_view(url)
    # row = cv.collection.add_row()
    # row.name = data['name']
