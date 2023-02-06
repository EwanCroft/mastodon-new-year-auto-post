from mastodon import Mastodon
import datetime
import time
import os
import configparser

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

if not os.path.exists(rf'{ROOT_DIR}\config.ini'):
    url = input("Enter the URL of your Mastodon instance:\n")
    email = input("Enter your email address:\n")
    password = input("Enter your password:\n")
    
    app_info = Mastodon.create_app(
        "New Year Message Poster",
        api_base_url = f"{url}"
    )
    client_id, client_secret = app_info

    mastodon = Mastodon(client_id=client_id, client_secret=client_secret, api_base_url=url)
    access_token = mastodon.log_in(email, password)

    config = configparser.ConfigParser()
    config['MASTODON'] = {'url': url,
                          'email': email,
                          'password': password,
                          'client_id': client_id,
                          'client_secret': client_secret,
                          'access_token': access_token}
    
    with open(rf'{ROOT_DIR}\config.ini', 'w') as configfile:
        config.write(configfile)

config = configparser.ConfigParser()
config.read(rf'{ROOT_DIR}\config.ini')
url = config['MASTODON']['url']
email = config['MASTODON']['email']
password = config['MASTODON']['password']
client_id_str = config['MASTODON']['client_id']
client_secret_str = config['MASTODON']['client_secret']
access_token_str = config['MASTODON']['access_token']

mastodon = Mastodon(client_id=client_id_str, client_secret=client_secret_str, access_token=access_token_str, api_base_url=url)


while True:
    time.sleep(1)
    today = datetime.datetime.today()
    year = int(today.strftime("%Y"))
    current = datetime.datetime.today().strftime("%d/%m/%Y, %H:%M:%S")
    New_Year = f"01/01/{year}, 00:00:00"

    if current == New_Year:
        try:
            mastodon.status_post(status = f"Happy New Year! #HappyNewYear #HappyNewYear{year}")
            break
        except Exception as e:
            print(e)