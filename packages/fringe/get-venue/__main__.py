import requests
from bs4 import BeautifulSoup
from datetime import datetime as dt


def main(args):
    show = args["show"]

    if not show:
        return {"body": "Please provide a show"}

    r = requests.get("https://tickets.edfringe.com/whats-on/" + show)

    soup = BeautifulSoup(r.text, "html.parser")
    venueNodes = soup.findAll("span", {"class": "venue-link__name"})
    venues = list(map(lambda x: x.get_text(), venueNodes))

    if not venues:
        return {"body": "No venue found...?"}

    venuesDescription = (
        " ".join(venues).strip().replace("\n", "").replace("\t", "").replace("-", ",")
    )
    venuesDescription = " ".join(venuesDescription.split())
    return {"body": venuesDescription}
