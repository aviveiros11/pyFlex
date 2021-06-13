import requests


class Credentials(object):

    def __init__(self):
        self.host = 'https://nrel.powerflex.com:9443'
        self.username = 'nrel'
        self.password = '5r28k68QFtKg'
        self.auth_header = "Bearer" + self.get_token()

    @property
    def set_password(self, password):
        self.password = password

    def get_token(self):
        data = {
            'username': self.username,
            'password': self.password
        }
        headers = {'Content-type': 'application/json', 'cache-control': 'no-cache'}

        try:
            response = requests.post(self.host + '/login', json=data, headers=headers)
            data = response.json()
            token = data['access_token']
            return token

        except BaseException:
            print("error with credentials")

    def get_measurement_data(self):
        data = {
            "measurment": "ct_response"
        }
        headers = {'Content-type': 'application/json', 'data': data, 'cache-control': 'no-cache',
                   'Authorization': self.auth_header}

        return headers


def main():
    c = Credentials()
    token = c.get_token()
    print(token)


if __name__ == "__main__":
    main()
