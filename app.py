from typing import Optional

import requests
from requests.exceptions import HTTPError


URL_API = 'https://api.airtable.com/v0/app1eknKRmKc4fwjm/MainTable?api_key=keytgAQ1CpPeOmuNU'

def get_json_response(url: str) -> Optional[dict]:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}') 
    except Exception as err:
        print(f'Other error occurred: {err}')

def get_list_of_sort_title() -> Optional[list]:
    json_response = get_json_response(URL_API)

    if json_response:
        list_fields = [record['fields'] for record in json_response['records']]
        sorted_list_fields = sorted(list_fields, key=lambda k: k['ID'])
        return [ field['title'] for field in sorted_list_fields ]


class CircularBuffer:
    def __init__(self, size) -> None:
        self.max = size
        self.data = []
        
    def __len__(self) -> int:
        return self.data.__len__()

    def append(self, el) -> None:
        self.data.append(el)

        if len(self.data) == self.max:
            self.cur = 0

            #  Permanently change self's class from non-full to full
            self.__class__ = self.__Full
    
    def get(self) -> list:
        return self.data

    class __Full:
        """ Class that implements a full buffer """
        def __len__(self) -> int:
            return self.data.__len__()

        def append(self, el) -> None:
            self.data[self.cur] = el
            self.cur = (self.cur + 1) % self.max

        def get(self) -> list:
            return self.data[self.cur:] + self.data[:self.cur]
            


def main() -> None:
    titles = get_list_of_sort_title()
    print(titles)


if __name__ == '__main__':
    main()
