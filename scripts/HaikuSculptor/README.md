## `haiku_sculptor.py`
This Python script generates **Haikus** — a traditional form of Japanese poetry —with dynamic word selection using the [Datamuse API](https://www.datamuse.com/api/) to fetch relevant words based on the randomly selected themes. The word bank is designed to reflect traditional Haiku themes, with words related to nature, seasons, elements, colors, objects, and places. The script generates each line of the Haiku with a syllable-counting algorithm using the `syllapy` library, adhering to the traditional 5-7-5 syllable structure of a Haiku. It allows you to generate multiple Haikus, choose how many you want, and save them in a JSON file for future use.

## Installation Dependencies
You can install the required dependencies using `pip`:
```bash
pip install requests syllapy
```

## How to Use
1. **Download the script**: Clone or download this repository to your local machine.
2. **Run the script**: Open a terminal/command prompt, navigate to the folder containing the script, and run the script using Python:   
    ```bash
    python haiku_sculptor.py
    ```
    
3. **Choose the number of Haikus**: When prompted, enter how many Haikus you would like to generate. The script will then generate that many Haikus based on random themes.
4. **View Output**: Once the Haikus are generated, they will be displayed in the terminal. The script will automatically save the generated Haikus to a **JSON file** with the default name `haikus.json`. Each Haiku will be saved as an object containing the title and the content:    
    ```json
    [
        {
            "title": "Haiku 1",
            "content": "autumn moonlight\nwhispers gently through cold winds\nthe crisp leaves flutter"
        },
        {
            "title": "Haiku 2",
            "content": "flowers bloom bright\nsoft winds carry the fragrance\nsunrise paints the sky"
        }
    ]
    ```
    

### <samp>Example Output (Console)</samp>
```
🌸 How many Haikus would you like to generate? 3

🌸 Generating Haiku based on the theme: autumn
🌸 Generating Haiku based on the theme: cherry blossom
🌸 Generating Haiku based on the theme: morning

Generated Haikus:

Haiku 1:
autumn moonlight
whispers gently through cold winds
the crisp leaves flutter

Haiku 2:
flowers bloom bright
soft winds carry the fragrance
sunrise paints the sky

Haiku 3:
morning sun rises
over misty hills it shines
birds sing in the dawn

✅ Haikus have been saved to haikus.json
```

The above command generates *3 Haikus* based on randomly selected themes and save them to a JSON file.

## Customization
The list of predefined themes can be modified in the script to add or remove themes. Each Haiku is generated based on a random selection from this list. The script pulls related words from the *Datamuse API* to create varied and creative Haikus based on the selected theme.

If you want to add a new theme like "mountain" and associated words, you can extend the lists in the script:
```python
themes = ["moon", "stars", "clouds", "mountains", "rain", "wind", "sea", "forest", "spring", "summer"]
```
