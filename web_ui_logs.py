import os
import datetime
import gossip
from flask import render_template_string
from bson.json_util import dumps
from eva import conf
from eva import log

dir_path = os.path.dirname(os.path.realpath(__file__))
logs_markup = open(dir_path + '/templates/logs.html').read()

@gossip.register('eva.web_ui.start', provides=['web_ui_logs'])
def web_ui_start(app):
    app.add_url_rule('/logs', 'logs', logs)
    app.add_url_rule('/logs/more/<timestamp>', 'more_logs', more_logs)

@gossip.register('eva.web_ui.menu_items', provides=['web_ui_logs'])
def web_ui_menu_items():
    menu_item = {'path': '/logs', 'title': 'Logs'}
    conf['plugins']['web_ui']['config']['menu_items'].append(menu_item)

def logs():
    menu_items = conf['plugins']['web_ui']['module'].ready_menu_items()
    return render_template_string(logs_markup, menu_items=menu_items)

def more_logs(timestamp):
    date = datetime.datetime.utcfromtimestamp(float(timestamp) / 1000)
    mod = conf['plugins']['mongodb_logging']['module']
    cursor = mod.logs.find({'timestamp': {'$gt': date}})
    data = []
    for entry in cursor[:]:
        data.append(entry)
    return dumps(data)
