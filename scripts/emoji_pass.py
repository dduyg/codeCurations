import random

emojis = [
    "😀", "😂", "🤣", "😎", "😍", "🤩", "🥳", "😜", "🧐", "🤖", "👽", "🎃", "🐍", "🦄", "🐉", "🐱", "🐶", "🦊", "🐼", "🐻", "🐸", "🐧", "🐦", "🦅", "🐢",  
    "🐠", "🐙", "🦑", "🦞", "🦀", "🐬", "🐳", "🐋", "🦈", "🦖", "🦕", "🌵", "🎄", "🌴", "🌺", "🌻", "🌹", "🌼", "🍄", "🍁", "☘️", "🍕", "🍔", "🌭", "🍿",  
    "🍩", "🎂", "🍫", "🍉", "🍎", "🍇", "🥭", "🍍", "🥝", "🥑", "🥕", "🥔", "🧀", "🥓", "🍗", "🍖", "🥩", "🍣", "🍤", "🍛", "🍜", "🥡", "🥤", "🍾", "🍷",  
    "🍺", "🍻", "🥂", "☕", "🍼", "🚀", "🚁", "🚂", "🚲", "🏎️", "🚜", "🛴", "🏍️", "🚢", "🛸", "⚽", "🏀", "🏈", "⚾", "🎾", "🏓", "🏸", "🥊", "🥋", "🎣",  
    "🎸", "🎻", "🥁", "🎤", "🎮", "🎲", "🃏", "🎯", "🏆", "💎", "🔑", "🔮", "🎩", "🧙‍♂️", "🧛‍♀️", "🎭", "🎨", "📸", "📚", "📖", "🔬", "💡", "⚡", "🔥",  
    "🌈", "☃️", "🌎", "🌙", "🪐", "⭐", "💰", "🛡️", "🏹", "🗡️", "🎷", "🎺", "🎵", "🎶", "🎤", "🛶", "🗿", "💣", "❤️", "💀", "🧠", "🕹️", "🔔", "📡", "💥"
]

password = "".join(random.choices(emojis, k=8))  # Generates an 8-character emoji password

print("Your emoji password:", password)
