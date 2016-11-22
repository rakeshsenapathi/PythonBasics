import urllib.parse


def read_txt():
    text = open(r"F:\Projects\PythonBasics\Udacity Python\textFile\221baker.txt")
    contents_of_file = text.read()
    print(contents_of_file)
    text.close()
    check_profanity(contents_of_file)


def check_profanity(text_to_check):
    url = 'http://www.wdylike.appspot.com'
    values = {'q' : text_to_check}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8') # data should be bytes
    req = urllib.request.Request(url, data)
    resp = urllib.request.urlopen(req)
    respData = resp.read()
    
read_txt()
