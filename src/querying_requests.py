import requests

class Query:
    """
    Creates an object for receiving responses

    Args:
        query_url (string): url string
        params (dictionary): parameters to pass to requests
        timeout (float): time to wait before returning TimeOut error
        retry (int): number of retries in case of timeout
    
    """

    def __init__(self,
    query_url,
    params,
    timeout,
    retry):

        self.query_url = query_url
        self.query_param = params
        self.timeout = timeout
        self.retry = retry

    
    def response_fn(self):

        try:

            response = requests.get(self.query_url,
            params=self.query_param, timeout=self.timeout)
            # returns name of the object class and status code of the returned request
            response.raise_for_status()
            # for all 4xx and 5xx error codes
            # response.status_code: contains the status code of the response
            return response

        except requests.exceptions.HTTPError as error:
            # response = None if error is raised
            print(error)

        except requests.exceptions.ConnectionError as error:
            print(error)

        except requests.exceptions.TooManyRedirects as error:
            print(error)

        except requests.exceptions.RequestException as error:
            print(error)

        except requests.exceptions.Timeout as error:
            # can set a retry loop here
            for count in range(self.retry):
                try:
                    response = requests.get(self.query_url,
            params=self.query_param, timeout=self.timeout)
                    
                except:
                    continue

            print(error)

       


if __name__ == '__main__':

    url = "http://api.open-notify.org/astros.jso"
    queries = {'latitude':'45', 'longitude':'180'}
    timeout = 1
    no_tmout_retries = 3
    
    query = Query(url,
    params=queries,
    timeout=timeout,
    retry=no_tmout_retries)

    response = query.response_fn()
    if response != None:
        print(response)
        print('\n')

        print('Content or raw bytes of the data payload: ', response.content)
        print('\n')
        print('Text or string representation of the data payload: ', response.text)
        print('\n')
        print('If API returns JSON: ', response.json())
        print('\n')
        print('Header info: ', response.headers)
        # tst = requests.get(url, params=queries)
        # print(tst.json())