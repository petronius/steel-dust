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
]

if __name__ == "__main__":
    import random
    for _ in range(100):
        print("%s the %s" % (random.choice(books), random.choice(schools)))
