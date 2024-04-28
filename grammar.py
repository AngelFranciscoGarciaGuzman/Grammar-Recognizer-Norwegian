import nltk
from nltk import CFG
nltk.download('punkt')

# Define a context-free grammar
custom_grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N | N | Det Adj N
    Det -> 'en' | 'et' | 'solen' | 'jorden' | 'regnet'
    N -> 'bil' | 'bok' | 'hus' | 'hund' | 'katt' | 'mat' | 'vann' | 'fjell' | 'skog' | 'blomst' | 'sol' | 'måne' | 'stjerne' | 'fugl' | 'fisk' | 'sjø' | 'elv' | 'snø' | 'is' | 'varme' | 'kald' | 'varm' | 'regn' | 'vind' | 'vær' | 'jord' | 'himmel' | 'natt' | 'dag' | 'tid' | 'fuglene'
    VP -> V NP | V Adj | V Adv
    V -> 'er' | 'spiser' | 'bor' | 'løper' | 'flyr' | 'fryser' | 'varmer' | 'regner' | 'blåser' | 'faller' | 'flyr'
    Adv -> 'fort' | 'langsamt' | 'raskt' | 'mye'
    Adj -> 'stort' | 'interessant' | 'høyt' | 'kald'
""")


# Create a parser with the defined grammar
custom_parser = nltk.ChartParser(custom_grammar)

# Define a custom tokenizer
def custom_tokenize(sentence):
    # Tokenize the sentence using nltk's word_tokenize
    tokens = nltk.word_tokenize(sentence)
    # Remove punctuation tokens
    tokens = [token.lower() for token in tokens if token.isalnum()]
    return tokens

# Input sentences to be parsed
sentences = [
    "En hund spiser mat.",
    "Et hus er stort.",
    "En katt løper raskt.",
    "En hund løper raskt.",
    "En bok er interessant.",
    "Et fjell er høyt.",
]

# Tokenize and parse each sentence using the custom tokenizer
for sentence in sentences:
    tokens = custom_tokenize(sentence)
    trees = list(custom_parser.parse(tokens))
    if trees:
        print(f"Parse tree for '{sentence}':")
        for tree in trees:
            tree.pretty_print()
    else:
        print(f"No parse tree found for '{sentence}'")
