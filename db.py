import psycopg2
import api
import os
from dotenv import load_dotenv

load_dotenv()

try:
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

def getTopTen():
    cursor.execute("SELECT discord_id, deadlock_id, rankscore FROM users ORDER BY rankscore DESC LIMIT 10")
    results = cursor.fetchall()
    connection.commit()
    return results
