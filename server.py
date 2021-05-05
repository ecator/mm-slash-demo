#!/usr/bin/env python3

import http.server as HTTPServer
from re import split
from urllib.parse import parse_qs
import slash

import sys
import argparse


class SlashHandler(HTTPServer.BaseHTTPRequestHandler):
    def do_slash(self):
        '''process slash'''

        contentLength=self.headers["Content-Length"]
        length=0
        if contentLength:
            length=int(contentLength)
        authorization = self.headers["Authorization"]
        token = ""
        if authorization:
            token = split(" ", authorization)[1]
        requestData = parse_qs(self.rfile.read(length).decode("utf-8"))
        slashRequst = slash.SlashRequst(token,requestData)

        self.send_response(200)

        text=f"""
key|value
---|---
token|{slashRequst.token}
command|{slashRequst.command}
text|{slashRequst.text}
channel_id|{slashRequst.channelId}
channel_name|{slashRequst.channelName}
response_url|{slashRequst.responseUrl}
team_domain|{slashRequst.teamDomain}
team_id|{slashRequst.teamId}
trigger_id|{slashRequst.triggerId}
user_id|{slashRequst.userId}
user_name|{slashRequst.userName}
"""
        slashResponse=slash.SlashResponse(text=text,responseType=slash.ResponseType.IN_CHANNEL)
        responseJson = slashResponse.json().encode("utf-8")

        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", len(responseJson))

        self.end_headers()
        self.wfile.write(responseJson)

    def do_GET(self):
        self.do_slash()

    def do_POST(self):
        self.do_slash()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A simple slash server for Mattermost")
    parser.add_argument("-p", "--port", type=int, default=5050, help="The port to bind, default is 5050")
    parser.add_argument("-a", "--address", type=str, default="127.0.0.1", help="The address to listen, default is 127.0.0.1")
    args = parser.parse_args()
    addr = args.address
    port = args.port
    httpd = HTTPServer.HTTPServer((addr, port), SlashHandler)
    print(f"Serving HTTP on {addr} port {port} ")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nKeyboard interrupt received, exiting.")
        sys.exit(0)
