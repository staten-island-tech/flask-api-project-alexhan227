from flask import Flask, render_template
import requests

app = Flask(__name__)

# Route for the home page
@app.route("/")
def index():
    # We ask the Pokémon API for the first 150 Pokémon.
    response = requests.get("https://db.ygoprodeck.com/api/v7/cardinfo.php")
    data = response.json()
    card_list= data['results']
    
    # We create a list to store details for each .
    cards = []
    
    for card in card_list:
        # Each Pokémon has a URL like "https://pokeapi.co/api/v2/pokemon/1/"
        url = cards['url']
        parts = url.strip("/").split("/")
        id = parts[-1]  # The last part of the URL is the Pokémon's ID
        
        # We use the ID to build an image URL.
        image_url = f""
        
        cards.append({
            'name': card['name'].capitalize(),
            'id': id,
            'image': image_url
        })
    
    # We tell Flask to show the 'index.html' page and pass the list of Pokémon.
    return render_template("index.html", card=cards)

# Route for the Pokémon details page
@app.route("/pokemon/<int:id>")
def card_detail(id):
    # We get detailed info for a specific Pokémon using its id.
    response = requests.get(f"https://db.ygoprodeck.com/api/v7/cardinfo.php/{id}")
    data = response.json()
    
    # We extract extra details like types, height, weight, and stats.
    card_sets = data.get('cards_sets').capitalize()
    name = data.get('name').capitalize()
    type = [t['type']['name'] for t in data['types']]
    desc = data.get('desc')
    humanReadableCardType = data.get('humanReadableCardType')
    race = data.get('race')
    archtype = data.get('archtype')
    set_rarity = data.get('set_rarity')
    image_url = f""
    
    
    # We tell Flask to show the 'pokemon.html' page with all these details.
    return render_template("yugioh.html", cards={
        'card_sets': card_sets,
        'name': name,
        'id': id,
        'image': image_url,
        'type': type,
        'humanReadableCardType': humanReadableCardType,
        'race': race,
        'archtype': archtype,
        'set_rarity': set_rarity,
        'desc': desc,

    })

if __name__ == '__main__':
    app.run(debug=True)