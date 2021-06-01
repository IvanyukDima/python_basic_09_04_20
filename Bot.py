#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  PigaDevelopment 31/05/21
  Планирование Google calendar через API c помощью телеграм
  Если отправлено сообщение типа '%d%m%y %H:%M' то будет запланировано событие в календаре
  На все другие сообщения будет отправлено 10 ближайших событий
"""

# [Google calendar]
from __future__ import print_function
import datetime
import googleapiclient
from google.oauth2 import service_account
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
# Telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# API google calendar
SCOPES = ['https://www.googleapis.com/auth/calendar.events']
SERVICE_ACCOUNT_FILE = 'token_bot.json'
calendarId = '6p7ni3epn0vmlj44t65smt7fkc@group.calendar.google.com'

credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = googleapiclient.discovery.build('calendar', 'v3', credentials=credentials)


class GoogleCalendar(object):

    def __init__(self):
        credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        self.service = googleapiclient.discovery.build('calendar', 'v3', credentials=credentials)

    # создание словаря с информацией о событии
    def create_event_dict(self, ev_dict):
        event_dct_t = ev_dict
        summary_t = event_dct_t.get('summary')
        datetime_t = event_dct_t.get('dateTime_st')
        datetime_e_t = event_dct_t.get('dateTime_e')

        event = {
            'summary': summary_t,
            'description': '',
            'start': {
                'dateTime': datetime_t,
            },
            'end': {
                'dateTime': datetime_e_t,
            }
        }
        return event

    # создание события в календаре
    def create_event(self, event):
        e = self.service.events().insert(calendarId=calendarId,
                                         body=event).execute()
        print('Event created: %s' % (e.get('id')))

    # вывод списка из десяти предстоящих событий
    def get_events_list(self):
        now = datetime.datetime.utcnow().isoformat() + 'Z'
        print('Getting the upcoming 10 events')
        events_result = self.service.events().list(calendarId=calendarId,
                                                   timeMin=now,
                                                   maxResults=10, singleEvents=True,
                                                   orderBy='startTime').execute()
        events = events_result.get('items', [])

        event_list = []

        if not events:
            print('Мистер свободен')
            event_mess = 'Мистер свободен.'
            event_list.append(event_mess)
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])
            event_mess = event['start'].get('dateTime', event['start'].get('date')) + " " + event['summary']
            event_list.append(event_mess)
        return event_list


calendar = GoogleCalendar()


# Телеграмм
def on_start(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="Привет, я Мистер №1")


def on_message(update, context):
    chat = update.effective_chat
    text = update.message.text
    datetime_str = text[:12]
    event = {'summary': '', '': 'some info', 'start': {'dateTime': '', }, 'end': {'dateTime': '', }}

    # Планирование события в календарь или вывод ближайших 10 мероприятий
    try:
        date_time_obj = datetime.datetime.strptime(datetime_str, '%d%m%y %H:%M')
        evn_dict = text_prepare(text)
        event = calendar.create_event_dict(evn_dict)
        calendar.create_event(event)
        context.bot.send_message(chat_id=chat.id, text="Внесено в календарь")
    except:
        message_list = calendar.get_events_list()
        for message in message_list:
            try:
                context.bot.send_message(chat_id=chat.id, text=message)
            except:
                context.bot.send_message(chat_id=chat.id, text="Мистер №1 к вашим услугам")


# Обратботка входящего сообщения для записи в календарь
def text_prepare(msg):
    txt = msg
    dt_tm = datetime.datetime.strptime(txt[:12], '%d%m%y %H:%M')
    dt_tm_e = dt_tm + datetime.timedelta(minutes=30)
    dt_tm = dt_tm.isoformat() + '+03:00'
    dt_tm_e = dt_tm_e.isoformat() + '+03:00'
    evn_d = {'dateTime_st': dt_tm, 'dateTime_e': dt_tm_e, 'summary': txt[13:]}
    return evn_d


token = "1798330301:AAFqFhTiW2CopygSgqFFAbrDrRy8jDy8UfQ"

updater = Updater(token, use_context=True)

dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", on_start))
dispatcher.add_handler(MessageHandler(Filters.all, on_message))

updater.start_polling()
updater.idle()

print("Бот запущен...")
