from mastodon import Mastodon
import datetime
import time
import os

root = os.path.dirname(os.path.realpath(__file__))
credentials = root + "\\credentials\\"

if not os.path.exists(credentials):
    os.makedirs(credentials)
else:
    print(f"\"{credentials}\" exists.")

if not os.path.exists(f"{credentials}server.txt"):
    server = input("Enter Mastodon instance:\n")
    open(f"{credentials}server.txt", "w", encoding = "utf-8").write(server)

else:
    print("Server already provided.")

server = open(f"{credentials}server.txt", "r", encoding = "utf-8").readlines(0)

list = []

for item in server:
    list.append(item)

server = list[0]

if not os.path.exists(f"{credentials}email.txt"):
    email = input("Enter Mastodon email:\n")
    open(f"{credentials}email.txt", "w", encoding = "utf-8").write(email)

else:
    print("email already provided.")

email = open(f"{credentials}email.txt", "r", encoding = "utf-8").readlines(0)

list = []

for item in email:
    list.append(item)

email = list[0]

if not os.path.exists(f"{credentials}password.txt"):
    pwd = input("Enter Mastodon password:\n")
    open(f"{credentials}password.txt", "w", encoding = "utf-8").write(pwd)

else:
    print("password already provided.")

password = open(f"{credentials}password.txt", "r", encoding = "utf-8").readlines(0)

list = []

for item in password:
    list.append(item)

password = list[0]

Mastodon_API = f"{server}"

if not os.path.exists(f"{credentials}bot_credentials.txt"):
    Mastodon.create_app(
        "New Year Celebrations!",
        api_base_url = f"{server}",
        to_file = f"{credentials}bot_credentials.txt"
    )
else:
    pass

mastodon = Mastodon(client_id = f"{credentials}bot_credentials.txt")
mastodon.log_in(
    f"{email}",
    f"{password}",
    to_file = f"{credentials}user_credentials.txt"
)

while True:
    time.sleep(1)
    today = datetime.datetime.today()
    year = int(today.strftime("%Y"))
    current = datetime.datetime.today().strftime("%d/%m/%Y, %H:%M:%S")
    New_Year = f"01/01/{year}, 00:00:00"

    if current == New_Year:
        mastodon.status_post(f"Happy New Year! #HappyNewYear{year}")
        break
    else:
        print(f"Not yet, it's {current}")
