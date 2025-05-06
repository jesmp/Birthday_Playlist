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
  <ol>
    <li><strong>Clone the repo</strong>
      <pre><code>git clone https://github.com/yourusername/birthday-playlist-generator.git cd birthday-playlist-generator</code></pre>
    </li>
    <li><strong>Create and activate a virtual environment (optional but recommended)</strong>
      <pre><code>python -m venv venv  source venv/bin/activate  # On Windows use `venv\Scripts\activate`</code></pre>
    </li>
    <li><strong>Install dependencies</strong>
      <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li><strong>Create a <code>.env</code> file</strong>
      <p>Create a <code>.env</code> file in the root directory with the following content:</p>
      <pre><code>CLIENT_ID=your_spotify_client_id
CLIENT_SECRET=your_spotify_client_secret
SPOTIFY_USERID=your_spotify_user_id</code></pre>
    </li>
    <li><strong>Run the app</strong>
      <pre><code>python main.py</code></pre>
    </li>
  </ol>

  <h2>🧠 How It Works</h2>
  <ol>
    <li>You’ll be prompted to enter a <strong>birth date</strong>, playlist <strong>name</strong>, and <strong>description</strong>.</li>
    <li>The app scrapes the #1 song from Billboard for that date across each year.</li>
    <li>Each song is searched on Spotify.</li>
    <li>A new <strong>private playlist</strong> is created in your Spotify account and populated with the found songs.</li>
  </ol>

  <h2>⚠️ Notes</h2>
  <ul>
    <li>Some songs may not exist on Spotify — the app will skip those with a warning.</li>
    <li>Make sure your Spotify Developer app has the correct <strong>redirect URI</strong> (<code>https://example.com</code> by default; adjust as needed).</li>
    <li>The app creates a private playlist by default. Modify <code>spotify_data["public"]</code> to <code>True</code> if you want it to be public.</li>
  </ul>

  <h2>📄 License</h2>
  <p>This project is open-source and free to use under the <a href="#">MIT License</a>.</p>
