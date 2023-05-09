from SpacePyTraders import client

USERNAME = "tsudonymn"
TOKEN = "YOUR TOKEN"

api = client.Api(USERNAME,TOKEN)

def register():


def display_account_info():
    print(api.account.info())


def play():


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    display_account_info()
    play()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
