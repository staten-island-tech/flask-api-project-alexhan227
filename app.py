from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    url = "https://www.dnd5eapi.co/api/monsters"
    headers = {'Accept': 'application/json'}
    response = requests.get(url, headers=headers)
    data = response.json()
    monsters_list = data.get('results', [])

    monsters = []
    for monster in monsters_list:
        name = monster['name']
        index = monster['index']
        image_url = f"https://www.dnd5eapi.co/api/images/monsters/{index}.png"  # Placeholder, not an actual image
        monster_url = f"https://www.dnd5eapi.co/api/monsters/{index}"
        monsters.append({
            'name': name,
            'index': index,
            'image_url': image_url,
            'monster_url': monster_url
        })


    return render_template("index.html", monsters_list=monsters)

@app.route("/details/<string:monster>")
def details(monster):

    monster_url = f'https://www.dnd5eapi.co/api/monsters/{monster}'
    headers = {'Accept': 'application/json'}
    response = requests.get(monster_url, headers=headers)
    data2 = response.json()
    monster_details = data2

    return render_template("Monsters.html", monster=monster_details)

if __name__ == '__main__':
    app.run(debug=True)