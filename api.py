import http.client
import json

# Accesses the API
HOST = "api.deadlock-api.com"

# Takes a rank (as an integer) and a division and returns the rank emoji, rank and division.
def stylizedRank(rank, subrank):
    match rank:
        case 11:
            rank = "<:Rank_Initiate_Badge:1555622479823642734>  Initiate"
        case 10:
            rank = "<:Rank_Seeker_Badge:1555622801539473438>  Seeker"
        case 9:
            rank = "<:Rank_Acolyte_Badge:1555622393370902590>  Acolyte"
        case 8: 
            rank = "<:Rank_Sentinel_Badge:1555622821672128622>  Sentinel"
        case 7:
            rank = "<:Rank_Mystic_Badge:1555622496156516383>  Mystic"
        case 6:
            rank = "<:Rank_Ritualist_Badge:1555622780521812149>  Ritualist"
        case 5:
            rank = "<:Rank_Emissary_Badge:1555622445623414784>  Emissary"
        case 4:
            rank = "<:Rank_Oracle_Badge:1555622536425775235>  Oracle"
        case 3:
            rank = "<:Rank_Phantom_Badge:1555622633507131584>  Phantom"
        case 2:
            rank = "<:Rank_Ascendant_Badge:1555622424173875241>  Ascendant"
        case 1:
            rank = "<:Rank_Eternus_Badge:1555622587428634624>  Eternus"
        case _:
            rank = "<:Rank_Obscurus_Badge:1555635920781443083> Obscurus"

    return rank + " " + str(subrank)


def fetchPlayerData(id, request):
    conn = http.client.HTTPSConnection(HOST, timeout=10)
    try:
        conn.request("GET", request)
        response = conn.getresponse()
        if response.status == 200:
            return json.loads(response.read().decode())
        return {}
    finally:
        conn.close()

def getRank(id):
    data = fetchPlayerData(id, f"/v1/players/{id}/rank")
    return data["rank"]

def getSubrank(id):
    data = fetchPlayerData(id, f"/v1/players/{id}/rank")
    return data["subrank"]

# returns a "ranked score" to sort player's as per their rank.
def getRankedScore(rank, subrank):
    # I lowkey have no idea how this works
    # but seems like it works so ill keep it like this
    return (12 - rank) * 10 + subrank