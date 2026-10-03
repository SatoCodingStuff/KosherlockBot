import psycopg2
import api
import os
from dotenv import load_dotenv

load_dotenv()

try:
    # Connects to DB
    connection = psycopg2.connect(
        host=os.getenv('IP'),
        database=os.getenv('DB'),
        user=os.getenv('USER'),
        password=os.getenv('PASS'),
        port=os.getenv('PORT'),
    )

    cursor = connection.cursor()
    
    print("Successfully connected to the database!")

except Exception as error:
    print(f"Error while connecting to PostgreSQL: {error}")


def addUser(discord_id, deadlock_id):
    cursor.execute(f"INSERT INTO users (discord_id, deadlock_id, rankscore) VALUES ({discord_id}, {deadlock_id}, {api.getRankedScore(api.getRank(deadlock_id), api.getSubrank(deadlock_id))})")
    connection.commit()

def getDeadlockId(discord_id):
    cursor.execute(f"SELECT deadlock_id FROM users WHERE discord_id = '{discord_id}'")
    results = cursor.fetchone()
    connection.commit()
    return results[0]

def getAllUsers():
    cursor.execute(f"SELECT * FROM users")
    results = cursor.fetchall()
    connection.commit()
    return results

# Gets the top 10 players in ranked
def getTopTen():
    cursor.execute("SELECT discord_id, deadlock_id, rankscore FROM users ORDER BY rankscore DESC LIMIT 10")
    results = cursor.fetchall()
    connection.commit()
    return results

def updateAllRankedScore():
    users = getAllUsers()

    i = 0
    while(i < len(users)):
        cursor.execute(f"UPDATE users SET rankscore = {api.getRankedScore(api.getRank(users[i][2]), api.getSubrank(users[i][2]))} WHERE discord_id = '{users[i][1]}' ")
        i += 1
    connection.commit()