import http.client
import json

conn = http.client.HTTPSConnection("api.deadlock-api.com")
'''
def getRank(id):
    conn.request("GET", f"/v1/players/{id}/rank")
    response = conn.getresponse().read().decode()
    data = json.loads(response)
    conn.close()
    rank = data["rank"]

    match rank:
        case 11:
            rank = "Initiate "
        case 10:
            rank = "Seeker "
        case 9:
            rank = "Acolyte "
        case 8: 
            rank = "Sentinel "
        case 7:
            rank = "Mystic "
        case 6:
            rank = "Ritualist "
        case 5:
            rank = "Emissary "
        case 4:
            rank = "Oracle "
        case 3:
            rank = "Phantom "
        case 2:
            rank = "Ascendant "
        case 1:
            rank = "Eternus "
        case _:
            rank = "Obscurus "

    rank += str(data["subrank"])

    return rank
    '''

def getRank(id):
    conn.request("GET", f"/v1/players/{id}/rank")
    response = conn.getresponse().read().decode()
    data = json.loads(response)
    conn.close()
    return data["rank"]

def getSubrank(id):
    conn.request("GET", f"/v1/players/{id}/rank")
    response = conn.getresponse().read().decode()
    data = json.loads(response)
    conn.close()
    return data["subrank"]