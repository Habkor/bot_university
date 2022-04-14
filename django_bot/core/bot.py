from telegram.ext import Updater
import os
import redis


TOKEN = os.getenv('TOKEN_BOT', '5101126561:AAHRV6ZkBMLpWJLFsY-iqFM4voQ7DPmiaFA')
redis = redis.Redis(host='localhost', port=6379, db=0)

updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher
