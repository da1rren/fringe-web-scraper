import requests
import re
from bs4 import BeautifulSoup
from datetime import datetime as dt


def main(args):
    show = args["show"]

    if not show:
        return {"body": "Please provide a show"}

    r = requests.get("https://tickets.edfringe.com/whats-on/" + show)

    soup = BeautifulSoup(r.text, "html.parser")

    timeNodes = soup.findAll("li", {"title": "Time"})
    venueNodes = soup.findAll("span", {"class": "venue-link__name"})
    venues = list(map(lambda x: x.get_text(), venueNodes))
    time = list(map(lambda x: x.get_text(), timeNodes))

    if not venues:
        return {"body": "No venue found...?"}

    venuesDescription = (
        " ".join(venues).strip().replace("\n", "").replace("\t", "").replace(",", "-")
    )

    timeDescription = " ".join(time).strip().replace("\n", "").replace("\t", "")

    venuesDescription = " ".join(venuesDescription.split()).strip()
    timeDescription = " ".join(timeDescription.split()).strip()

    venuesDescription=re.sub(r'[^A-Za-z0-9 ]+', '', venuesDescription)
    timeDescription=re.sub(r'[^A-Za-z0-9 ]+', '', timeDescription)
    resp = timeDescription + " @ " + venuesDescription

    print(resp)
    return {"body": resp}



if __name__ == "__main__":
    main({"show": "foil-arms-and-hog-hogwash"})
