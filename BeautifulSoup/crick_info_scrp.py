from bs4 import BeautifulSoup

import urllib.request

from PyQt5 import Qt

import sys

url = "http://www.cricbuzz.com/live-cricket-scores/16871/ind-vs-eng-4th-test-england-tour-of-india-2016-17"

req = urllib.request.urlopen(url)

print(req.getcode())

soup = BeautifulSoup(req, "html.parser")

scores_container = soup.find(
    "div", class_="cb-col cb-col-100 cb-font-12 cb-text-gray cb-min-rcnt")

score_tray = scores_container.find_all('span')

score = score_tray[1].text

app = Qt.QApplication(sys.argv)
systemtray_icon = Qt.QSystemTrayIcon()
systemtray_icon.show()
systemtray_icon.showMessage('Recent Runs', score)
