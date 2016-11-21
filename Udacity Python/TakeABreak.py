import webbrowser
import time
count = 0;
while( count < 3) :
    time.sleep(3)
    webbrowser.open("https://www.youtube.com/")
    count = count + 1;
if( count == 3) :
    webbrowser.open("https://www.facebook.com/")

