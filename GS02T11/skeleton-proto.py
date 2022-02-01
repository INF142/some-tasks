# It is possible to do the task from scratch, without using this file.

"""
Protocol
========

Order
-----
Only one message

Format
------
String

Request:

Command[3] | Number |
---------------------
Body                |
---------------------

Response:

Code                |
---------------------
Payload             |
---------------------


Rules
-----
Request (From client to server):
Method         Action
GET            Retrieve the content of file N
TODO: Add the commands and their description

Response (From server to client):
Code
200            Success
400            Bad request
404            File not found
"""


def get(file_number: int) -> str:
    with open(f"file{file_number}.txt", "r") as file:
        return file.read()

command_to_method = {
    "GET": get # TODO: Add other commands 
}


def on_receipt_reply(request: str) -> str:
    # TODO
    pass


if __name__ == "__main__":
    while text:=input("> "):
        text += "\n"+input("> ")
        print("--- Response "+"-"*12)
        print(on_receipt_reply(text))
        print("-"*25)
