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
    print(monster_url)
    headers = {'Accept': 'application/json'}
    response = requests.get(monster_url, headers=headers)
    data2 = response.json()
    print("test",response)
    monster_details = data2

    for monster in monster_details:
        strength = monster['strength']
        monster_details.append({
            'strength': strength,
        })


    return render_template("Monsters.html", monster=monster_details)

if __name__ == '__main__':
    app.run(debug=True)