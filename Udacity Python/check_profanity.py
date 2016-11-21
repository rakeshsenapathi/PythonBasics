import urllib


def read_txt():
    text = open(r"F:\Projects\PythonBasics\Udacity Python\textFile\221baker.txt")
    contents_of_file = text.read()
    print(contents_of_file)
    text.close()
    check_profanity(contents_of_file)


def check_profanity(text_to_check):
    connection = urllib.request.OpenerDirector("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    print(output)
    connection.close()

read_txt()
