Web UI Logs
===========

An Eva plugin that adds a way of viewing logs from the Web UI.

You will only see log messages from AFTER the [MongoDB Logging](https://github.com/edouardpoitras/eva-mongodb-logging) plugin has been enabled during the boot process.

The logs may not reveal issues with parsing the plugins directories or the config files, and may not catch any plugin errors that occur before the [MongoDB Logging](https://github.com/edouardpoitras/eva-mongodb-logging) plugin's instantiation.

## Installation

Can be easily installed through the Web UI by using [Web UI Plugins](https://github.com/edouardpoitras/eva-web-ui-plugins).

Alternatively, add `web_ui_logs` to your `eva.conf` file in the `enabled_plugins` option list and restart Eva.

## Usage

Enable the plugin, go the the Web UI, and click on the new menu item titled `Logs`.

You should be taken to the bottom of the page and log messages should start streaming in as they occur. Try starting a new interaction with Eva while watching the `Logs` page.

## Configuration

None
