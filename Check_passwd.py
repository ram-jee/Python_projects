import requests
import hashlib
import sys

#This function connects to API and returns all the entries which matches the given string
def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error Fetching: {res.status_code} check api and try again')
    return res


#This function accepts initial characters as input in hashes and splits aa the responses line by line into resp and count
def get_password_leak_count(hashes,hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())

    for h,count in hashes:
        if h == hash_to_check:
            return count
    return 0

#This function accepts all the passwords to be checked and then invokes get_password_leak_count for each password
def pwned_api_check(password):

    sha1password = (hashlib.sha1(password.encode('utf-8')).hexdigest().upper())

    first5_char, tail = sha1password[:5],sha1password[5:]
    response = request_api_data(first5_char)
    #print(first5_char,tail)
    #print(response)

    return get_password_leak_count(response,tail)

#request_api_data('123')
#pwned_api_check('123')

# This function allows users to enter passwords from command line and invokes pwned_api_check
def main(args):
    for password in args:
        count = pwned_api_check(password)

        if count:
            print(f'{password} was found {count} times...... You are in danger')
        else:
            print(f'{password} was not found. You are safe')

    return 'done'



main(sys.argv[1:])