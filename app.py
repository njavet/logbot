#!/usr/bin/env python3

import argparse
import logging
import json
import logbot
import pymongo

import telegram.ext as te


def create_parser():
    desc = ''
    ep = ''

    parser = argparse.ArgumentParser(description=desc, epilog=ep)
    parser.add_argument('--token', dest='token', required=True)
    parser.add_argument('--user_id', dest='user_id', type=int, required=True)
    parser.add_argument('--dbuser', dest='dbuser', required=True)
    parser.add_argument('--dbpasswd', dest='dbpasswd', required=True)

    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()

    # bot auth
    updater = te.Updater(token=args.token)
    dispatcher = updater.dispatcher

    # database
    client = pymongo.MongoClient('localhost',
                                 username=args.dbuser,
                                 password=args.dbpasswd,
                                 authSource='training',
                                 authMechanism='SCRAM-SHA-1')

    db = client.training

    # TODO one config file
    with open('keys.json', 'r') as f:
        keys = json.loads(f.read())

    with open('attributes.json', 'r') as f:
        attrs = json.loads(f.read())

    with open('collections.json', 'r') as f:
        collections = json.loads(f.read())

    gym_bot = logbot.LogBot(db=db,
                            keys=keys,
                            attrs=attrs,
                            collections=collections)

    # TODO better logging!
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # help_handler = te.CommandHandler('help', gym_bot.send_help)
    # dispatcher.add_handler(help_handler)
    stronglift_handler = te.CommandHandler('stronglift', gym_bot.stronglift)
    dispatcher.add_handler(stronglift_handler)

    # message handler
    msg_handler = te.MessageHandler(te.Filters.chat(args.user_id), gym_bot.analyze_msg)
    dispatcher.add_handler(msg_handler)


    # t0 = datetime.time(hour=0, minute=8)
    job_queue = dispatcher.job_queue
    # job_queue.run_repeating(callback=gym_bot.job, interval=30, first=0)

    updater.start_polling()


if __name__ == '__main__':
    main()