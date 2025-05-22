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
        image_url = f"https://www.dnd5eapi.co/api/images/monsters/aboleth.png"  # Placeholder, not an actual image
        monster_url = f"https://www.dnd5eapi.co/api/monsters/{index}"
        monsters.append({
            'name': name,
            'index': index,
            'image': image_url,
            'monster_url': monster_url
        })


    return render_template("index.html", monsters_list=monsters)

@app.route("/details/<string:monster>")
def details(monster):
    monster_url = f'https://www.dnd5eapi.co/api/monsters/{index}'
    response = requests.get(monster_url, headers=headers)
    headers = {'Accept': 'application/json'}
    data2 = response.json
    monster_details = data2.get('resulst', [])


    for monster_detail in monster_details:
        strength = monster_detail['strength']
        dexterity = monster_detail['dexterity']
        constitution = monster_detail['constitution']
        intelligence = monster_detail['intelligence']
        wisdom = monster_detail['wisdom']
        charisma = monster_detail['charisma']
        special_abilities = monster_detail['special_abilities']
        monster_detail.append({
        "strength": strength,
        "dexterity": dexterity,
        "constitution": constitution,
        "intelligence": intelligence,
        "wisdom": wisdom,
        "charisma": charisma,
        "special_abilities": special_abilities
        })


    return render_template("Monsters.html", monster_details=monster)

if __name__ == '__main__':
    app.run(debug=True)