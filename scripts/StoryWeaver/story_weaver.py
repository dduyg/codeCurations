import random
import re
from collections import defaultdict

# Predefined themes with story elements
themes = {
    "space adventure": {
        "setting": ["a distant galaxy", "a space station orbiting Jupiter", "a mysterious alien planet"],
        "characters": ["Captain Nova", "Lieutenant Orion", "Android X9", "Alien Diplomat Zog"],
        "conflicts": ["a malfunction in the spaceship", "an alien attack", "a mysterious SOS signal"],
        "resolutions": ["fixing the ship just in time", "making peace with the aliens", "discovering an ancient artifact"]
    },
    "haunted house": {
        "setting": ["an abandoned mansion", "a forgotten graveyard", "a creepy attic"],
        "characters": ["Lucy the Ghost Hunter", "Detective Hollow", "The Mysterious Old Man", "A Mischievous Spirit"],
        "conflicts": ["strange noises at midnight", "a cursed mirror", "an old book that reveals dark secrets"],
        "resolutions": ["banishing the ghost", "breaking the curse", "unraveling the hidden mystery"]
    },
    "fantasy kingdom": {
        "setting": ["the enchanted forest", "a grand medieval castle", "a dragon's cave"],
        "characters": ["Prince Eldric", "The Wise Wizard", "Lady Seraphina", "The Cunning Goblin"],
        "conflicts": ["a dragon threatening the kingdom", "a missing magical artifact", "a betrayal within the court"],
        "resolutions": ["defeating the dragon", "restoring the lost artifact", "exposing the traitor"]
    },
    "cyberpunk": {
        "setting": ["a neon-lit cityscape", "a dark hacker's den", "a corporate skyscraper"],
        "characters": ["Rogue AI Zeta", "Hacker Zero", "Cyber-Detective Raine", "The Megacorp CEO"],
        "conflicts": ["a stolen data chip", "a rogue AI takeover", "a black market cyber-drug operation"],
        "resolutions": ["hacking the mainframe", "outsmarting the corporation", "escaping the digital prison"]
    },
    "pirate adventure": {
        "setting": ["a stormy sea", "a hidden treasure island", "a pirate stronghold"],
        "characters": ["Captain Blackbeard", "First Mate Morgan", "The Mysterious Castaway", "The Royal Navy Commander"],
        "conflicts": ["a mutiny on board", "a legendary treasure map", "a battle with the navy"],
        "resolutions": ["finding the treasure", "defeating the mutineers", "outsmarting the navy"]
    },
    "detective mystery": {
        "setting": ["a foggy London alley", "a grand manor house", "a locked room"],
        "characters": ["Detective Holmes", "The Secretive Butler", "The Femme Fatale", "Inspector Graves"],
        "conflicts": ["a missing heirloom", "a mysterious murder", "a forged will"],
        "resolutions": ["uncovering the truth", "trapping the real culprit", "solving the case"]
    }
}

# Function to allow user input for custom story elements
def get_custom_story_elements():
    print("\nLet's create a custom theme!")
    theme_name = input("Enter a name for your theme: ").strip().lower()
    
    settings = input("Enter possible settings (comma-separated): ").split(',')
    characters = input("Enter possible characters (comma-separated): ").split(',')
    conflicts = input("Enter possible conflicts (comma-separated): ").split(',')
    resolutions = input("Enter possible resolutions (comma-separated): ").split(',')
    
    themes[theme_name] = {
        "setting": [s.strip() for s in settings],
        "characters": [c.strip() for c in characters],
        "conflicts": [c.strip() for c in conflicts],
        "resolutions": [r.strip() for r in resolutions]
    }
    
    return theme_name

# Function to generate story using Markov Chains
def generate_markov_story(theme):
    """Generates a story using Markov Chains for a more natural feel."""
    if theme not in themes:
        return "Sorry, I don't have stories for that theme yet."

    # Select story elements
    setting = random.choice(themes[theme]["setting"])
    character1, character2 = random.sample(themes[theme]["characters"], 2)
    conflict = random.choice(themes[theme]["conflicts"])
    resolution = random.choice(themes[theme]["resolutions"])

    # Base sentences for Markov generation
    sentences = [
        f"In {setting}, {character1} and {character2} embarked on a dangerous adventure.",
        f"They soon faced {conflict}, which seemed almost impossible to overcome.",
        f"With quick thinking and courage, they managed to {resolution}.",
        f"Their story became a legend, told across the lands."
    ]

    # Build a Markov chain from the sentences
    words = " ".join(sentences).split()
    markov_dict = defaultdict(list)

    for i in range(len(words) - 1):
        markov_dict[words[i]].append(words[i + 1])

    # Generate new sentences using Markov Chains
    def generate_sentence(start_word, length=12):
        sentence = [start_word]
        for _ in range(length - 1):
            next_word = random.choice(markov_dict.get(sentence[-1], words))
            sentence.append(next_word)
        return " ".join(sentence) + "."

    # Create final story with Markov-generated variation
    story = f"{generate_sentence('In')} {generate_sentence('They')} {generate_sentence('With')} {generate_sentence('Their')}"
    return story

# Main menu
def main():
    print("Welcome to the Story Generator!")
    print("Available themes: " + ", ".join(themes.keys()) + ", or type 'custom' to create your own.")
    
    user_theme = input("Enter a theme: ").strip().lower()
    
    if user_theme == "custom":
        user_theme = get_custom_story_elements()
    
    print("\nHere's your story:\n")
    print(generate_markov_story(user_theme))

if __name__ == "__main__":
    main()
