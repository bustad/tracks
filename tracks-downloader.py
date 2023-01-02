# All charts are on
# https://sverigesradio.se/tracks
# https://sverigesradio.se/topplista.aspx?programid=2696&date=2010-12-11

import urllib.request
import html
import datetime
import time


def g(instring):
  if len(instring) == 1:
    return " " + instring
  else:
    return instring


def downloaddate(date):
  website = "https://sverigesradio.se/topplista.aspx?programid=2696&date="

  try:
    with urllib.request.urlopen(website + date) as fp:
      mybytes = fp.read()
  except urllib.error.HTTPError as e:
    #print('Error code: ', e.code)
    return ""

  #with urllib.request.urlopen(website) as fp:
  #  mybytes = fp.read()

  mystr = mybytes.decode("utf8")
  mystr = html.unescape(mystr)
  mystr = mystr.split("\r\n")
  mystr = [l.strip() for l in mystr]

  result = ""
  for k in range(len(mystr)):
    if mystr[k] == '<li class="track">':
      result += date + ", "
      if mystr[k + 3] == '<div class="track__ranking-current">':
        result += g(mystr[k + 4].split()[0]) + ", "
        result += mystr[k +
                        8][len('<span class="track__title">'):-len('</span>')]
        result += "\n"
      else:
        result += " B, " + mystr[
          k + 3][len('<span class="track-title">'):-len('</span>')] + "\n"

  return result


start_date = datetime.date(1984, 1, 1)
end_date = datetime.date(2011, 1, 1)
delta = datetime.timedelta(days=1)
current_date = start_date

while (current_date < end_date):
  print(current_date, end="\n")
  with open("tracks-db.txt", "a") as myfile:
    myfile.write(downloaddate(str(current_date)))
  time.sleep(0.5)
  current_date += delta

