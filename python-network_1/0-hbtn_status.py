#!/usr/bin/python3
"""A script that
- fetches https://alx-intranet.hbtn.io/status.
- uses urlib package
"""


if __name__ == '__main__':
    import urllib.request

    url = 'https://intranet.hbtn.io/status'
    if url.startswith('https://'):
        url = 'https://alu-intranet.hbtn.io/status'

    with urllib.request.urlopen(url) as res:
        content = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
