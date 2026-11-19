# use this whenever you need to update the databases.

import sqlite3
import json

conn = sqlite3.connect("database/data_source.db")
conn.row_factory = sqlite3.Row

cursor = conn.cursor()

# get everything
cursor.execute("SELECT * FROM game")
game = [dict(row) for row in cursor.fetchall()]
cursor.execute("SELECT * FROM developer")
developer = [dict(row) for row in cursor.fetchall()]
cursor.execute("SELECT * FROM console")
console = [dict(row) for row in cursor.fetchall()]
cursor.execute("SELECT * FROM subseries")
subseries = [dict(row) for row in cursor.fetchall()]
cursor.execute("SELECT * FROM character")
character = [dict(row) for row in cursor.fetchall()]
cursor.execute("SELECT * FROM species")
species = [dict(row) for row in cursor.fetchall()]
# combine into one
data = {
    "game": game,
    "developer": developer,
    "console": console,
    "subseries": subseries,
    "character": character,
    "species": species,
}
# Export data to JSON file
with open("games.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

conn.close()

print("Database successfully converted to JSON!")
