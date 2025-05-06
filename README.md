<h1>🎵 Birthday #1 Song Playlist Generator</h1>
<p>This Python application creates a personalized Spotify playlist featuring the #1 Billboard Hot 100 song on your birthday for every year from your birth year to the current year. It's a nostalgic journey through music history tailored to your special day!</p>

<h2>🚀 Features</h2>
<ul>
<li>Scrapes Billboard's Hot 100 chart to find the #1 song on a given birth date across multiple years.</li>
<li>Searches Spotify for each #1 track and adds it to a new private playlist.</li>
<li>Customizable playlist name and description.</li>
<li>Uses Spotify’s API and OAuth for playlist creation and management.</li>
</ul>

<h2>🛠️ Requirements</h2>
<ul>
<li>Python 3.7+</li>
<li>Spotify account</li>
<li>Spotify Developer credentials (CLIENT_ID, CLIENT_SECRET, SPOTIFY_USERID)</li>
<li>A .env file with credentials (see below)</li>
</ul>

<h2>📦 Installation</h2>
Clone the repo

bash
Copy
Edit
git clone https://github.com/yourusername/birthday-playlist-generator.git
cd birthday-playlist-generator
Create and activate a virtual environment (optional but recommended)

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Create a .env file

Create a .env file in the root directory with the following keys:

env
Copy
Edit
CLIENT_ID=your_spotify_client_id
CLIENT_SECRET=your_spotify_client_secret
SPOTIFY_USERID=your_spotify_user_id
Run the app

bash
Copy
Edit
python main.py
🧠 How It Works
You'll be prompted to enter a birth date, playlist name, and description.

The app scrapes the #1 song from Billboard for that date across each year.

Each song is searched on Spotify.

A new private playlist is created in your Spotify account and populated with the found songs.

⚠️ Notes
Some songs may not exist on Spotify — the app will skip those with a warning.

Make sure your Spotify developer app has the correct redirect URI (https://example.com is used by default; adjust as needed).

The app creates a private playlist by default. Modify spotify_data["public"] to True if you want it public.

📄 License
This project is open-source and free to use under the MIT License.

