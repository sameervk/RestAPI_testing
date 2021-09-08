import requests

class Authenticate:

    def __init__(self,
    login_url,
    useremail,
    pw):

        self.login_url = login_url
        self.useremail = useremail
        self.pw = pw

    
    def get_token(self):
        print('Getting token...')

        data_get = {'email': self.useremail,
                    'password': self.pw,
                    'loginMode': 1}

        requst = requests.post(self.login_url+'/user',
                                data=data_get)
        if requst.ok:
            print("Headers: ", requst.headers)
            print('\n')
            # print("Cookies: ", requst.cookies)

        else:
            print("HTTP %i - %s, Message %s" % (requst.status_code,
                                                requst.reason, 
                                                requst.text))

    

if __name__ == '__main__':

    url = 'https://api.github.com'

    user = ''
    pw = ''

    authntcte = Authenticate(url, user, pw)

    authntcte.get_token()


