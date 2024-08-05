from flask import Flask, render_template, request, abort
import mysql.connector
from flask_sitemap import Sitemap

# Establishing the connection to the MySQL database
conn = mysql.connector.connect(
    user='root', password='root', host='127.0.0.1', database='anime'
)

# Creating a cursor object to interact with the database
cursor = conn.cursor()

app = Flask(__name__)
ext = Sitemap(app=app)

@app.route('/')
def index():
    """Render the index page."""
    return render_template("index.html")

@ext.register_generator
def index():
    """Generate the sitemap."""
    yield 'index', {}

@app.route("/<name>")
def home(name):
    """
    Render the home page for a specific show.
    
    :param name: The name of the show.
    """
    try:
        # Fetch show details from the database
        cursor.execute(f"SELECT * FROM {name}")
        namer = cursor.fetchone()
        if namer:
            nameshow, genre, sypnosis, rating, year = namer
            return render_template(
                "home.html", 
                nameshow=nameshow, genre=genre, year=year, 
                sypnosis=sypnosis, rating=rating, name=name
            )
        else:
            abort(404)
    except mysql.connector.Error as err:
        abort(404)

@app.route("/player_<name>")
def player(name):
    """
    Render the player page for a specific episode.
    
    :param name: The name of the show and episode number in the format 'show-episode'.
    """
    try:
        print(name)
        namer, episode = name.split("-")
        print(namer)
        episode = int(episode)

        # Connect to the database for the specific show
        conn2 = mysql.connector.connect(
            user='animezone', password='c2cx7tp9tk', host='127.0.0.1', database=f'{namer}'
        )
        cursor2 = conn2.cursor()

        # Fetch show name
        cursor.execute(f"SELECT name FROM {namer}")
        nameshow = cursor.fetchone()[0]

        # Format episode number
        if episode < 10:
            episode = f'0{episode}'

        # Fetch video link for the episode
        cursor2.execute(f"SELECT * FROM links WHERE links LIKE '%{episode}_Dubbed_%'")
        link = cursor2.fetchone()[0]

        # Prepare next and previous episode numbers
        next_episode = f'0{int(episode) + 1}' if int(episode) + 1 < 10 else str(int(episode) + 1)
        prev_episode = f'0{int(episode) - 1}' if int(episode) - 1 < 10 else str(int(episode) - 1)

        # Fetch the total number of episodes
        cursor2.execute("SELECT COUNT(*) FROM links")
        result = cursor2.fetchall()[0][0]

        return render_template('player.html', nameshow=nameshow, link=link, namer=namer, result=result, next=next_episode, prev=prev_episode, episode=episode)
    except mysql.connector.Error as err:
        abort(404)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
