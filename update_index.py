import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace pinks with blues
replacements = {
    "#ff9a9e": "#9ae5ff",
    "#ffb6c1": "#b6e1ff",
    "#ff7eb3": "#7eb3ff",
    "#ff758c": "#758cff",
    "#fecfef": "#cffeff",
    "#ff0844": "#0844ff",
    "#ffb199": "#b199ff",
    "#f76baf": "#6baaff",
    "#ee5286": "#4b9fff" # signature color
}

for old_color, new_color in replacements.items():
    html = html.replace(old_color, new_color)

new_letter = """<div class="letter">
                <p>Oii meu amor,minha nega,minha princesa e minha gostosa,queira lhe entregar um buquê de flores pessoalmente mas infelizmente não posso mas tem esse que vai surgir pra você💟❤️💖❣️💕.</p>
                <div class="photos">
                    <img src="./assets/WhatsApp Image 2026-06-21 at 10.45.04 (1).jpeg" alt="foto">
                    <img src="./assets/WhatsApp Image 2026-06-21 at 10.45.04.jpeg" alt="foto">
                    <img src="./assets/WhatsApp Image 2026-06-21 at 10.45.05 (1).jpeg" alt="foto">
                    <img src="./assets/WhatsApp Image 2026-06-21 at 10.45.05 (2).jpeg" alt="foto">
                    <img src="./assets/WhatsApp Image 2026-06-21 at 10.45.05.jpeg" alt="foto">
                </div>
                <div class="audio-player">
                    <p>Dê play na nossa música ❤️</p>
                    <audio src="./assets/music.webm" controls loop></audio>
                </div>
            </div>"""

html = re.sub(r'<div class="letter">.*?</div>', new_letter, html, flags=re.DOTALL)

# Add CSS for photos
css_addition = """
.photos {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    justify-content: center;
    margin-top: 15px;
}
.photos img {
    width: 100px;
    height: 100px;
    object-fit: cover;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
}
.audio-player {
    margin-top: 20px;
}
.audio-player p {
    font-size: 0.9rem;
    font-weight: bold;
    color: #4b9fff;
    margin-bottom: 5px;
}
"""

html = html.replace("</style>", css_addition + "\n</style>")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
