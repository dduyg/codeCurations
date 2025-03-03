import syllapy
import random
import requests
import json

# Expanded list of predefined themes
themes = [
    "moon", "stars", "clouds", "mountains", "rain", "wind", "sea", "forest", 
    "rivers", "snow", "flowers", "trees", "lakes", "birds", "animals", "grass", 
    "insects", "rock", "spring", "summer", "autumn", "winter", "cherry blossom", 
    "new year", "harvest", "evening", "morning", "fog", "sunrise", "sunset", 
    "twilight", "midnight", "noon", "early morning", "evening", "late night", 
    "dusk", "dawn", "thunderstorm", "lightning", "breeze", "hail", "dew", "drizzle", 
    "blizzard", "heatwave", "rainbow", "clear sky", "love", "loneliness", "happiness", 
    "sadness", "peace", "tranquility", "hope", "memory", "dreams", "longing", "silence", 
    "struggle", "birth", "growth", "change", "decay", "blooming", "harvest", "rebirth", 
    "regeneration", "new beginnings", "zen", "meditation", "enlightenment", "death", 
    "spirit", "journey", "transience", "impermanence", "nature’s cycles", "mountain peak", 
    "waterfall", "beach", "rainy window", "mist over a lake", "storm clouds", "flowers blooming", 
    "bird in flight", "snow-covered landscape", "haiku", "tea ceremony", "bamboo", "pagoda", 
    "Japanese garden", "lanterns", "chrysanthemums", "koi fish", "bamboo forest", "deer in the forest", 
    "fox in the snow", "owl in the night", "swan on a pond", "butterfly in a field", "fireflies", 
    "crickets at night", "turtles in the river", "wolf howling at the moon", "fish swimming in the pond"
]

# Function to interact with Datamuse API and fetch related words
def fetch_words_from_datamuse(query, max_results=10):
    url = f"https://api.datamuse.com/words?rel_jja={query}&max={max_results}"  # Adjective relation
    response = requests.get(url)
    
    if response.status_code == 200:
        words = [word['word'] for word in response.json()]
        return words
    else:
        print("Failed to fetch data from Datamuse API.")
        return []

# Load a list of basic words or retrieve them from the API
def load_word_lists():
    nouns = ["autumn", "moon", "mountain", "wind", "rain", "cherry", "blossom", "cloud", "bird", "storm"]
    verbs = ["whispers", "falls", "rises", "flies", "drifts", "shines", "howls", "grows", "breaks", "melts"]
    adjectives = []
    
    for noun in nouns[:3]:  # Only fetch adjectives for a few nouns to limit API calls
        adjectives.extend(fetch_words_from_datamuse(noun))
    
    return {
        "nouns": nouns,
        "verbs": verbs,
        "adjectives": adjectives
    }

# Function to create Haiku lines based on syllables
def create_line(syllables, word_lists):
    line = ""
    remaining_syllables = syllables
    while remaining_syllables > 0:
        word_category = random.choice(["nouns", "verbs", "adjectives"])
        word = random.choice(word_lists[word_category])
        
        if syllapy.count(word) <= remaining_syllables:
            line += word + " "
            remaining_syllables -= syllapy.count(word)
    
    return line.strip()

# Function to generate a single Haiku with a random theme
def generate_haiku():
    theme = random.choice(themes)
    print(f"🌸 Generating Haiku based on the theme: {theme}")
    
    word_lists = load_word_lists()
    
    # Fetch theme-specific adjectives from Datamuse
    theme_adjectives = fetch_words_from_datamuse(theme, max_results=5)
    word_lists["adjectives"].extend(theme_adjectives)
    
    # Generate Haiku lines
    haiku = []
    haiku.append(create_line(5, word_lists))  # First line (5 syllables)
    haiku.append(create_line(7, word_lists))  # Second line (7 syllables)
    haiku.append(create_line(5, word_lists))  # Third line (5 syllables)
    
    return "\n".join(haiku)

# Validate Haiku syllable structure
def validate_haiku(haiku):
    lines = haiku.split("\n")
    syllable_counts = [sum(syllapy.count(word) for word in line.split()) for line in lines]
    return syllable_counts == [5, 7, 5]

# Function to generate multiple Haikus
def generate_multiple_haikus(num_haikus):
    haikus = []
    for _ in range(num_haikus):
        generated_haiku = generate_haiku()
        haikus.append({
            "title": f"Haiku {_+1}",
            "content": generated_haiku
        })
    return haikus

# Function to save the Haikus collection as a JSON file
def save_haikus_to_json(haikus, filename="haikus.json"):
    with open(filename, "w") as f:
        json.dump(haikus, f, ensure_ascii=False, indent=4)
    print(f"✅ Haikus have been saved to {filename}")

# Example usage
num_haikus = int(input("🌸🌿 How many Haikus would you like to generate? "))
haikus = generate_multiple_haikus(num_haikus)

# Display generated Haikus
print("\nGenerated Haikus:")
for haiku in haikus:
    print(f"\n{haiku['title']}:\n{haiku['content']}")

# Save Haikus to JSON file
save_haikus_to_json(haikus)
