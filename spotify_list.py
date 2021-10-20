
play_List = [{
    "name": "Patagonia Bus",
    "created_by": "Colt Steel",
    "duration": "50 min",
    "songs": [{
        "title": "Turn it Off",
        "artists": ["Culture Abuse"],
        "album": "Peach",
        "created_date": "2020-09-04",
        "duration": "3:73"
    }, {
        "title": "Nights Off",
        "artists": ["Siruismo"],
        "album": "Mosaik",
        "created_date": "2020-03-04",
        "duration": "3:73"
    }, {
        "title": "Don't Stop",
        "artists": ["Knightlife"],
        "album": "Oceans Apart",
        "created_date": "2020-03-04",
        "duration": "3:73"
    }, {
        "title": "Tilted - Paradis Remix",
        "artists": ["Christina and The Queens", "Paradis"],
        "album": "Tilted (Paradis Remix)",
        "created_date": "2020-03-04",
        "duration": "3:73"
    }, {
        "title": "Wasted Days",
        "artists": ["Cloud Nothing"],
        "album": "Attack on Memory",
        "created_date": "2020-03-04",
        "duration": "3:73"
    }, {
        "title": "Sad Saturdays",
        "artists": ["JOBA"],
        "album": "Sad Saturdays",
        "created_date": "2020-03-04",
        "duration": "3:73"
    }]
}]


for play in play_List[0]["songs"]:
    print(play["title"])
