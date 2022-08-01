import requests
from bs4 import BeautifulSoup
from datetime import datetime as dt

def suffix(d):
    print(d)
    return 'th' if 11<=d<=13 else {1:'st',2:'nd',3:'rd'}.get(d%10, 'th')

def main(args):
    show=args["show"]

    if not show:
        return {
            'body': 'Please provide a show'
        }

    r = requests.get("https://tickets.edfringe.com/whats-on/" + show,
                     headers={"X-Requested-With": "XMLHttpRequest"})

    soup = BeautifulSoup(r.text, 'html.parser')
    liAvailable = soup.findAll("span", {"class": "available"})
    liFree = soup.findAll("span", {"class": "tickets-free"})
    liPreview = soup.findAll("span", {"class": "tickets-preview"})
    li241 = soup.findAll("span", {"class": "two_for_one"})

    li=liAvailable + liFree + liPreview + li241
    dates = list(map(lambda x: x.get_text() + suffix(int(x.get_text())), li))

    if not dates:
        return {
            'body': 'No dates available :('
        }

    ' '.join(dates)
    return {
        'body': ' '.join(dates)
      }
