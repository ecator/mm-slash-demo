"""
处理slash相关
"""


from enum import Enum
import json


class SlashRequst:
    """
    处理Slash请求
    """

    def __init__(self, token: str, data: dict):
        pass
        self.token = token
        dataKeys = data.keys()
        if "channel_id" in dataKeys:
            self.channelId = data["channel_id"][0]
        else:
            self.channelId = None
        if "channel_name" in dataKeys:
            self.channelName = data["channel_name"][0]
        else:
            self.channelName = None
        if "command" in dataKeys:
            self.command = data["command"][0]
        else:
            self.command = None
        if "response_url" in dataKeys:
            self.responseUrl = data["response_url"][0]
        else:
            self.responseUrl = None
        if "team_domain" in dataKeys:
            self.teamDomain = data["team_domain"][0]
        else:
            self.teamDomain = None
        if "team_id" in dataKeys:
            self.teamId = data["team_id"][0]
        else:
            self.teamId = None
        if "text" in dataKeys:
            self.text = data["text"][0]
        else:
            self.text = None
        if "trigger_id" in dataKeys:
            self.triggerId = data["trigger_id"][0]
        else:
            self.triggerId = None
        if "user_id" in dataKeys:
            self.userId = data["user_id"][0]
        else:
            self.userId = None
        if "user_name" in dataKeys:
            self.userName = data["user_name"][0]
        else:
            self.userName = None


class ResponseType(Enum):
    EPHEMERAL = "ephemeral"
    IN_CHANNEL = "in_channel"


class SlashResponse:
    """
    处理Slash响应
    """

    def __init__(self, text: str = None, responseType: ResponseType = None, username: str = None, channelId: str = None, iconUrl: str = None, gotoLocation: str = None):
        pass
        data = {}
        if text:
            data["text"] = text
        if responseType:
            data["response_type"] = responseType.value
        if username:
            data["username"] = username
        if channelId:
            data["channel_id"] = channelId
        if iconUrl:
            data["icon_url"] = iconUrl
        if gotoLocation:
            data["goto_location"] = gotoLocation

        self.data = data

    def json(self) -> str:
        """
        序列化为json字符串
        """
        return json.dumps(self.data, ensure_ascii=False)
