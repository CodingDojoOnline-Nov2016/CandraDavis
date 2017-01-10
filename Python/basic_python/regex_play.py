# Starting with the code snippet below, write a regex that will match:
import re

def get_matching_words(regex):
    words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]

    return [word for word in words if re.search(regex, word)]

# All words that contain a v
print get_matching_words(r'([v])')

# All words that contain a double-s
print get_matching_words(r'([s]+[s])')
# All words that end with an e
print get_matching_words(r'([a-z]+)')
# # All words that contain an b, any character, then another b
get_matching_words(r'([b]+[a-z]+[b])')
# # All words that contain an b, at least one character, then another b
# get_matching_words()
# # All words that contain an b, any number of characters (including zero), then another b
# get_matching_words()
# # All words that include all five vowels in order
# get_matching_words()
# # All words that only use the letters in (regular expression) (each letter can appear any number of times)
# get_matching_words()
# # All words that contain a double letter
# get_matching_words()
