import requests

class API:

    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()


    def get(self, endpoint):
        url = f"{self.base_url}/ {endpoint}"
        try:
            response = self.session.get(url)
            return response.json()
        except requests.exceptions.ConnectionError as e:
            print(e)
            return None

    def post(self, endpoint, data):
        url = f"{self.base_url}/ {endpoint}"
        try:
            response = self.session.post(url, json=data)
            return response.json()
        except requests.exceptions.ConnectionError as e:
            print(e)
            return None

    def delete(self, endpoint):
        url = f"{self.base_url}/ {endpoint}"
        response = self.session.delete(url)
        return  response.status_code

if __name__ == "__main__":
    client = API("url")


    users = client.get("users")

#
#
import functools

def reverse_string(func):
    @functools.wraps(func)
    def wrapper(s, *args, **kwargs):
        reversed_s = s[::-1]
        return func(s, reversed_s, *args, **kwargs)
    return wrapper

@reverse_string
def palindrome2(s, reversed_s):
    return s == reversed_s

print(palindrome2('malayalam'))


def palindrome(n):
    return n == n[::-1]

def is_palindrome(n):
    lower_n = n.lower().strip()
    left, right = 0, len(lower_n) - 1
    while left < right:
        if lower_n[left] != lower_n[right]:
            return False
        left += 1
        right -= 1
    return True


print(is_palindrome("Madam"))


