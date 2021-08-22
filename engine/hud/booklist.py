books = [
    "Tome",
    "Volume",
    "Book",
    "Opus",
    "Treatise",
    "Ledger",
    "Paperback",
    "Handbook",
    "Scroll",
    "Dictionary",
    "Compendium",
    "Manuscript",
    "Manual",
    "Chronicle",
    "Folio",
    "Incunabulum",
    "Thesaurus",
    "Herbarium",
    "Saga",
    "Catalogue",
    "Cyclopaedia",
    "Testamentum",
    "Grimoire",
    "Liber",
    "Lesser Key",
    "Daemonarium",
    "Idiot's Guide",
]

schools = [
    "Power",
    "Might",
    "Mystery",
    "Befuddlement",
    "Ice Magic",
    "Must",
    "Smells",
    "Magic",
    "Sorcery",
    "Hexes",
    "Charms",
    "Jargon",
    "Spells",
    "Nonsense",
    "Old Languages",
    "Damnation",
    "Wisdom",
    "Secrets",
    "Chaos",
    "Witchcraft",
    "Necromancy",
    "Slutty Magic",
    "the Occult",
    "Enchantment",
    "Binding",
    "Incantation",
    "Esoterica",
    "the Eldritch",
    "the Dead",
    "the Karcist",
    "Summoning",
    "Angelology",
    "Transformation",
    "Unusual Beasts",
    "the Wonders of the East",
    "Cryptography",
    "Fortran",
    "Witchery",
    "Wizzardy",
    "Brainfuck",
    "Poisons",
    "Alchemy",
    "Most Wickedde Magicke",
    "Madjgycke",
    "Unholy Arts",
    "Illiberal Arts",
    "Fireballs for Dummies",
    "Lycanthropy",
    "Haruspicy",
    "Prophecy",
    "Discord",
    "Alectromancy",
    "Ceromancy",
    "Cleromancy",
    "Chronomancy",
    "Gastromancy",
    "Numerology",
    "Oneiromancy",
    "Tasseomancy",
    "Cartomancy",
    "Rhabdomancy",
    "Pyromancy",
    "Flim-Flam",
    "Con Artistry",
    "Frauds and Swindles",
    "Rude Latin Poetry",
    "Awkwardly Out of Date Orientalism",
    "Mistranslated Egyptian Funerary Texts",
    "Malarky",
    "Thaumaturgy",
    "Philology",
    "Horse Training",
    "Abyssal Sudoku",
    "Old Babylonian Crossword Puzzles",
    "Diophantane Approximation",
    "Card Tricks",
    "Exorcism",
    "Inexplicable Woodcuts",
    "Doodles",
    "Erotic Vampire Fiction",
    "Postmodern Theory",
    "Some Harry Potter Bullshit",
]

if __name__ == "__main__":
    import random
    for _ in range(100):
        print("%s of %s" % (random.choice(books), random.choice(schools)))
