from django.conf import settings
import json
import requests

class SlackClient:
    def __init__(self, url="", channel=""):
        self.url = url or settings.SLACK_CONFIG["webhook_url"]
        self.channel = channel or settings.SLACK_CONFIG["default_channel"]

    def post(self, text):
        payload = json.dumps({ "text": text, "channel": self.channel })
        return requests.post(self.url, payload)

