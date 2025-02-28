import random
import pyphen

# Initialize the Pyphen syllable counting object
pyphen_obj = pyphen.Pyphen(lang='en')

# A much larger dictionary of words categorized by syllable count, including locations and subjects
word_dict = {
    1: [
        "wind", "leaf", "sky", "tree", "sun", "cloud", "rain", "moon", "star", "bird",
        "rock", "stone", "snow", "light", "fire", "ice", "path", "rose", "earth", "sea",
        "lake", "hill", "wood", "dawn", "shade", "snow", "dew", "mist", "wave", "grass",
        "night", "day", "star", "heat", "fire", "rain", "cloud", "storm", "flower", "snow",
        "earth", "shore", "mist", "leaf", "stone", "creek", "river", "dream", "sky", "beach",
        "gold", "blue", "red", "green", "black", "white", "gray", "pink", "purple", "teal",
        "orange", "yellow", "beach", "snow", "dawn", "petal", "shell", "city", "forest",
        "mountain", "desert", "ocean", "village", "field", "path", "pond", "river"
    ],
    2: [
        "whisper", "gentle", "autumn", "breeze", "flowing", "ripple", "silent", "twilight",
        "echo", "shadow", "branch", "storm", "gather", "waking", "crystal", "rainbow", 
        "shining", "dreamer", "forest", "flame", "shiver", "frost", "blossom", "feather", 
        "horizon", "glimmer", "glow", "glimpse", "flutter", "wither", "murmur", "sunset",
        "crystal", "silent", "harmony", "tremor", "whistle", "glisten", "twilight", "brisk",
        "glance", "fragrant", "sizzle", "whistle", "flame", "shiver", "river", "bloom", "brush",
        "whirling", "shudder", "laughter", "winding", "hunger", "balance", "frosty", "swimming",
        "glistening", "twinkling", "amber", "violet", "sapphire", "tangerine", "emerald", "canyon",
        "temple", "valley", "meadow", "desert", "pyramid", "harbor", "beach"
    ],
    3: [
        "beautiful", "radiant", "peaceful", "majestic", "mysterious", "delicate", "fragile", 
        "harmonious", "twinkling", "glorious", "majestic", "melancholy", "serenity", "invisible", 
        "inspired", "adventure", "journey", "whistling", "reflective", "inspiration", "wonderful", 
        "magnificent", "elation", "celebration", "mysterious", "elusive", "reverence", "discovery",
        "rippled", "blooming", "trembling", "soothing", "forever", "tenderness", "glistening", "tapping", 
        "passion", "glittering", "overflowing", "screaming", "ecstatic", "ascending", "enlightening", 
        "surrender", "surprising", "delightful", "loneliness", "staggering", "resilience", "shimmering",
        "crimson", "turquoise", "rosewood", "charcoal", "emerald", "lavender", "amber", "sunset", "azure",
        "desert", "mountain", "island", "valley", "forest", "pond", "field", "river", "cloud"
    ],
    4: [
        "meditation", "reflection", "elation", "inspiration", "contemplation", "sensation", 
        "celebration", "illumination", "rejuvenation", "expectation", "realization", "awakening", 
        "enlightenment", "revelation", "wonderment", "imagination", "compassion", "liberation", 
        "innovation", "dedication", "understanding", "appreciation", "surrendering", "astonishing",
        "restoration", "illumination", "transformation", "concentration", "involvement", "reparation",
        "reverence", "elevation", "revelation", "invention", "adoration", "hesitation", "realization",
        "communication", "meditative", "wonderment", "resurrection", "acclamation", "absolution",
        "violet", "scarlet", "indigo", "turquoise", "alabaster", "onyx", "cerulean", "sapphire",
        "desert", "field", "cliff", "island", "tundra", "harbor", "village", "highland", "coastline"
    ],
    5: [
        "magnificence", "inspiration", "illumination", "reflection", "contemplation", "serenity",
        "delightfulness", "rejuvenation", "exhilaration", "unexpectedly", "whispering", "satisfaction", 
        "benevolence", "proclamation", "contribution", "celebration", "accommodation", "hesitation", 
        "wonderment", "frustration", "stimulation", "insurrection", "elevation", "connection", 
        "penetration", "appreciation", "realization", "apprehension", "realization", "solitude", 
        "meditation", "harmony", "exploration", "liberation", "transformation", "reformation", "elation",
        "lavender", "goldenrod", "amethyst", "peacock", "cinnamon", "topaz", "fuchsia", "crimson", "chartreuse",
        "coast", "mountain", "village", "temple", "harbor", "canyon", "ocean", "cliff", "desert"
    ],
    6: [
        "synchronization", "restoration", "magnification", "unfolding", "proclamation", "illumination", 
        "transformation", "integration", "coordination", "rejuvenation", "reinterpretation", "consolidation",
        "reconfiguration", "renovation", "organization", "complication", "combination", "revolution", 
        "reconstruction", "constellation", "appreciation", "justification", "subjugation", "emancipation", 
        "reparations", "separation", "realignment", "visualization", "affirmation", "identification",
        "pearl", "ruby", "onyx", "topaz", "sapphire", "jade", "emerald", "diamond", "turquoise", "ivory",
        "village", "temple", "palace", "mountain", "meadow", "canyon", "river", "desert", "oasis", "ocean"
    ]
}

# Function to count syllables in a word
def count_syllables(word):
    return len(pyphen_obj.inserted(word).split('-'))

# Function to dynamically create a line with a specified syllable count
def generate_line(syllable_count):
    line = []
    while syllable_count > 0:
        # Randomly choose a word with the remaining syllable count
        available_words = [word for word in word_dict[syllable_count] if count_syllables(word) == syllable_count]
        word = random.choice(available_words)
        line.append(word)
        syllable_count -= count_syllables(word)
    return " ".join(line)

# Function to generate a haiku (5-7-5 syllable structure)
def generate_haiku():
    line1 = generate_line(5)
    line2 = generate_line(7)
    line3 = generate_line(5)

    haiku = f"{line1}\n{line2}\n{line3}"
    return haiku

# Generate and print a haiku
print(generate_haiku())
