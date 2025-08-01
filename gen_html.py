import os

# Configuration
folder = "files"  # Folder where audio files are stored
output_html = "index.html"

# Supported audio types
audio_extensions = {
    ".m4a": "audio/mp4",
    ".mp3": "audio/mpeg"
}

# Find audio files
audio_files = sorted([
    f for f in os.listdir(folder)
    if os.path.splitext(f)[1].lower() in audio_extensions
])

# Start HTML
html = [
    "<!DOCTYPE html>",
    "<html lang='en'>",
    "<head>",
    "  <meta charset='UTF-8'>",
    "  <title>My Audio Collection</title>",
    "</head>",
    "<body>",
    "  <h1>Audio Library</h1>"
]

# Add entries for each file
for file in audio_files:
    title = os.path.splitext(file)[0].replace("_", " ").title()
    mime = audio_extensions[os.path.splitext(file)[1].lower()]
    html += [
        f"  <div>",
        f"    <h2>{title}</h2>",
        f"    <audio controls>",
        f"      <source src='{folder}/{file}' type='{mime}'>",
        f"      Your browser does not support the audio element.",
        f"    </audio>",
        f"  </div>"
    ]

# End HTML
html += ["</body>", "</html>"]

# Save to file
with open(output_html, "w", encoding="utf-8") as f:
    f.write("\n".join(html))

print(f"Generated {output_html} with {len(audio_files)} audio files.")

