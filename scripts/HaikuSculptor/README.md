## `haiku_sculptor.py`
This Python script generates **Haikus** — a traditional form of Japanese poetry — using dynamic word selection from an extensive word bank. The script randomly selects words based on syllable counts using the `pyphen` library to construct lines, adhering to the traditional 5-7-5 syllable structure of a Haiku. The script uses a dictionary of words categorized by their syllable count. The word bank is designed to reflect traditional Haiku themes, with words related to nature, seasons, elements, colors, objects, and places. For each line of the Haiku, the script randomly selects words from the word bank that match the required syllable count.

## How to Use
1. Clone this repository or download the script file.
2. Install the required Python package (if you haven't already) by running:  
    ```bash
    pip install pyphen
    ```    
3. Run the script to generate a Haiku.     
    ```bash
    python haiku_sculptor.py
    ```    
4. Each time you run the script, a new Haiku will be randomly generated.

### <samp>Example Output:</samp>
```
autumn leaves whisper,
crystal sky, a distant hill,
tender moon rises.
```

## Customization
You can easily customize the word bank or tweak the script for specific needs:
- You can easily modify the word bank to add more words or adjust the existing ones. The word bank is organized into syllable counts (1, 2, 3, etc.), and you can expand each syllable category with additional words related to seasons, nature, or anything you like.
    
    To modify the word bank, simply update the `word_dict` in the script:    
    ```python
    word_dict = {
        1: ["sun", "moon", "sky", "star", "tree", ...],
        2: ["whisper", "autumn", "gentle", "breeze", ...],
        ...
    }
    ```    
- **Adjust Syllable Counting**: You can change the syllable rules or even use a different syllable counting library if needed.
