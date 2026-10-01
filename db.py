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
    cursor.execute(f"INSERT INTO users (discord_id, deadlock_id, rank, subrank) VALUES ({discord_id}, {deadlock_id}, {api.getRank(deadlock_id)}, {api.getSubrank(deadlock_id)})")
    connection.commit()