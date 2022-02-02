from db.run_sql import run_sql

from models.artist import Artist

# def select_all():
#     artists = []
#     sql = "SELECT * FROM artists"
#     result = run_sql(sql)

#     for row in artists:


def save(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING *"
    values = [artist.name]
    result = run_sql(sql, values)
    artist.id = result[0]['id']
    return artist

def select_all():
    artists = []

    sql = "SELECT * FROM artists"
    results = run_sql(sql)
    
    for row in results:
        artist = Artist(row['name'], row['id'])
        artists.append(artist)
    return artists

def select(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        artist = Artist(result['name'], result['id'])
    return artist

def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)