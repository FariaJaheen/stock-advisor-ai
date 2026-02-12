from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import os
import requests


class PushNotificationArgs(BaseModel):
    argument: str = Field(..., description="The message to be sent to the user/investor")


class PushNotificationTool(BaseTool):
    name: str = "send_push_notification"
    description: str = "Send a push notification to the user/investor via Pushover."
    args_schema: Type[BaseModel] = PushNotificationArgs

    def _run(self, argument: str) -> str:
        pushover_user = os.getenv("PUSHOVER_USER")
        pushover_token = os.getenv("PUSHOVER_TOKEN")

        if not pushover_user or not pushover_token:
            return "Missing PUSHOVER_USER or PUSHOVER_TOKEN in environment."

        url = "https://api.pushover.net/1/messages.json"
        payload = {"user": pushover_user, "token": pushover_token, "message": argument}

        resp = requests.post(url, data=payload, timeout=15)
        if resp.status_code != 200:
            return f"Failed to send notification: {resp.status_code} {resp.text}"

        return "ok"