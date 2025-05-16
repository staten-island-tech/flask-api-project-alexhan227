from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    url = "https://www.dnd5eapi.co/api/monsters"
    headers = {'Accept': 'application/json'}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return "Failed to retrieve monsters from API", 500

    data = response.json()
    monsters_list = data.get('results', [])

    monsters = []
    for monster in monsters_list:
        name = monster['name']
        index = monster['index']
        image_url = f"https://www.dnd5eapi.co/api/monsters/{index}"  # Placeholder, not an actual image
        monster_url = f"https://www.dnd5eapi.co/api/monsters/{index}"
        monsters.append({
            'name': name,
            'index': index,
            'image': image_url,
            'monster_url': monster_url
        })

    return render_template("index.html", monsters_list=monsters)

if __name__ == '__main__':
    app.run(debug=True)