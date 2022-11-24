import urllib.request
import json

def main():
    response = urllib.request.urlopen('http://jsonip.com/')
    raw = response.read()
    print(type(raw))
    txt = raw.decode('utf-8')
    print(txt)
    print(type(txt))
    d = json.loads(txt)
    print(d['ip'])

if __name__ == "__main__":
    main()