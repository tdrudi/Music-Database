"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""

    # ADD THE NECESSARY CODE HERE
    __tablename__ = "playlists"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String, nullable = False)
    description = db.Column(db.Text, nullable = True)
    song = db.relationship("Song", secondary = "playlistSongs", backref = "playlists")



class Song(db.Model):
    """Song."""

    # ADD THE NECESSARY CODE HERE
    __tablename__ = "songs"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    title = db.Column(db.String, nullable = False)
    artist = db.Column(db.String, nullable = False)
    playlist = db.relationship("Playlist", secondary = "playlistSongs", backref = "songs")



class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    # ADD THE NECESSARY CODE HERE
    __tablename__ = "playlistSongs"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    playlist_id = db.Column(db.Integer, db.ForeignKey("playlists.id"), primary_key = True)
    song_id = db.Column(db.Integer, db.ForeignKey("songs.id"), primary_key = True)
    


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""
    with app.app_context():
        db.app = app
        db.init_app(app)
