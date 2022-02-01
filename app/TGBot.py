import requests

from config import BASE_API_URL, WEBHOOK_URL


class Bot:
    """ Simple class, represents Telegram API. """
    def __init__(self, api_token):
        self.token = api_token
        self.base_url = BASE_API_URL
        self.handlers = {}
        print("=== BOT STARTED ===")

        if not self.__is_webhook_set():
            print(self.set_webhook(WEBHOOK_URL))


    def send_message(self, chat_id, text):
        """ Sends message to user.

        Keyword arguments:
        chat_id -- the ID of user
        text    -- message for user

        """
        args = {"chat_id": chat_id, "text": text}
        r = requests.get(self.base_url + "sendMessage", json=args)
        return r.json()


    def get_updates(self):
        """ Gets updates received by the bot. """
        r = requests.get(self.base_url + "getUpdates")
        return r.json()


    def set_webhook(self, url):
        """ Sets the webhook for getting POST requests by Telegram.

        Keyword arguments:
        url -- URL for receiving POST requests by Telegram

        """
        args = {"url": url}
        r = requests.get(self.base_url + "setWebhook", json=args)
        return r.json()


    def delete_webhook(self):
        """ Deletes the webhook for gettings requests. """
        r = requests.get(self.base_url + "deleteWebhook")
        return r.json()


    def get_webhook_info(self):
        """ Returns inforamtion about the webhook (URL, IP Address, etc.). """
        r = requests.get(self.base_url + "getWebhookInfo")
        return r.json()


    def __is_webhook_set(self):
        """ Returns True if the URLs from config and setted webhook match. """
        info = self.get_webhook_info()
        return info["result"]["url"] == WEBHOOK_URL


    def add_handler(self, command, callback):
        """ Add new command for bot.

        Keyword arguments:
        command -- command which user should to write
        callback -- handler for command

        """
        self.handlers.update({command: callback})


    def handle_message(self, data):
        """ This function reatcs for user's message.
        Invokes function from self.handlers by key (user's message).

        Keyword arguments:
        data -- JSON object from Telegram's POST requests

        """
        chat_id = data["message"]["from"]["id"]
        content = data["message"]["text"]

        try: # Was command bind before?
            response = self.handlers[content]()
        except KeyError: # If it wasn't
            response = "I don't know what to say :'("

        self.send_message(chat_id, response)
