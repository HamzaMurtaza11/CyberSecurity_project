from http.client import responses
from urllib import response
import requests
import hashlib
import sys

def request_api_data(query_char):
    url= 'https://api.pwnedpasswords.com/range/'+query_char
    res= requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code},get api and try again')
        return res

def get_password_leak_count(hashes, hash_to_check):
    hashes= (line.split(':')for line in hashes.text.splitlines())
    for h,count in hashes:
        print(h,count)
        if h== hash_to_check:
         return count
    return 0


def pwned_api_check(password):
    sha1password= hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char= sha1password[:5]
    tail= sha1password[5:]
    print(tail)
    print(first5_char)
    response= request_api_data(first5_char)
    return get_password_leak_count(response, tail)

def main(args):
    for password in args:
        count= pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times .... you should change your password')
        else:
            print(f'{password} was NOT found. Carry on!')
    return 'done!'



if __name__=='__main__':

  sys.exit(main (sys.argv[1:]))




   

pwned_api_check("123")







