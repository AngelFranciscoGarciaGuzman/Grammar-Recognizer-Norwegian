# Grammar-Recognizer-Norwegian
Evidence 2 of the course Implementation of Computational methods

# Norwegian Language Context and CFG Parser

## Language Context

The Norwegian language is a Germanic language primarily spoken in Norway, with significant communities in neighboring countries and worldwide. It belongs to the North Germanic language family and shares close linguistic ties with Danish and Swedish. Norwegian has two official written forms: Bokmål and Nynorsk, with Bokmål being more prevalent, especially in urban areas. The language's vocabulary and grammar reflect its historical evolution and interactions with other languages, notably Danish due to the extended union between Norway and Denmark. Additionally, Norwegian has seen influences from English, particularly in recent years due to globalization and English's dominance in various domains.

## Language Structure

Norwegian sentence structure generally follows the subject-verb-object (SVO) pattern, akin to English. However, Norwegian relies heavily on inflection to convey grammatical roles and relationships within sentences. Nouns, adjectives, and articles in Norwegian are inflected for gender, number, and case. Verbs are conjugated based on tense, mood, aspect, and person. While Norwegian distinguishes between singular and plural, it does not have specific markers for dual or trial numbers like Na'vi.

## Context-Free Grammar (CFG)

To model Norwegian's grammar, we define a context-free grammar (CFG) using Backus-Naur Form (BNF) notation. The grammar includes productions for sentences (S), noun phrases (NP), verb phrases (VP), determiners (Det), nouns (N), verbs (V), adjectives (Adj), and adverbs (Adv). Additionally, we provide a lexicon of Norwegian words to populate the grammar.

## Example Sentences

To test our CFG parser for Norwegian, we utilize six example sentences:

1. "En hund spiser mat." - "A dog eats food."
2. "Et hus er stort." - "A house is big."
3. "En katt løper raskt." - "A cat runs quickly."
4. "Solen varmer jorden." - "The sun warms the earth."
5. "En bok er interessant." - "A book is interesting."
6. "Et fjell er høyt." - "A mountain is tall"

## Code Implementation

We implement the CFG parser using NLTK (Natural Language Toolkit) in Python. The code defines the CFG, creates a parser, and tokenizes and parses each example sentence. If a parse tree is found, it is printed to the console.

```python
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
    tokens = nltk.word_tokenize(sentence)
    tokens = [token.lower() for token in tokens if token.isalnum()]
    return tokens

# Input sentences to be parsed
sentences = [
    "En hund spiser mat.",
    "Et hus er stort.",
    "En katt løper raskt.",
    "Solen varmer jorden.",
    "En bok er interessant.",
    "Regnet faller fort."
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
```
## Implementation Steps

1. **Import NLTK and CFG Class**: First, we import the necessary components from NLTK. We'll utilize the CFG class to create a grammar framework that captures the structure of our language.

    ```python
    from nltk import CFG
    ```

2. **Define Context-Free Grammar**: We define a CFG that represents the structure of our language. This CFG includes productions for sentences (S), noun phrases (NP), verb phrases (VP), determiners (Det), nouns (N), verbs (V), adjectives (Adj), and adverbs (Adv). We also provide a lexicon of words to populate the grammar.

    ```python
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
    ```

3. **Create Parser**: We generate a parser using the defined CFG. This parser dissects sentences into individual words and determines whether they adhere to the rules established in our grammar.

    ```python
    custom_parser = nltk.ChartParser(custom_grammar)
    ```

4. **Tokenize and Parse Sentences**: Finally, we tokenize and parse each sentence using the custom tokenizer. If a parse tree is found, it is printed to the console; otherwise, a message indicating that no parse tree was found is displayed.

    ```python
    for sentence in sentences:
        tokens = custom_tokenize(sentence)
        trees = list(custom_parser.parse(tokens))
        if trees:
            print(f"Parse tree for '{sentence}':")
            for tree in trees:
                tree.pretty_print()
        else:
            print(f"No parse tree found for '{sentence}'")
    ```
## Testing
As mentioned earlier, after processing the program with the 6 provided sentences, we would obtain corresponding tree structures as outputs.

```

Parse tree for 'En hund spiser mat.':
              S                
      ________|__________       
     |                   VP    
     |              _____|___   
     NP            |         NP
  ___|___          |         |  
Det      N         V         N 
 |       |         |         |  
 en     hund     spiser     mat

Parse tree for 'Et hus er stort.':
             S               
      _______|_______         
     NP              VP      
  ___|___         ___|____    
Det      N       V       Adj 
 |       |       |        |   
 et     hus      er     stort

Parse tree for 'En katt l�per raskt.':
              S                 
      ________|_________         
     NP                 VP      
  ___|___           ____|____    
Det      N         V        Adv 
 |       |         |         |   
 en     katt     l�per     raskt

Parse tree for 'En hund l�per raskt.':
              S                 
      ________|_________         
     NP                 VP      
  ___|___           ____|____    
Det      N         V        Adv 
 |       |         |         |   
 en     hund     l�per     raskt

Parse tree for 'En bok er interessant.':
             S                     
      _______|_______               
     NP              VP            
  ___|___         ___|_______       
Det      N       V          Adj    
 |       |       |           |      
 en     bok      er     interessant

Parse tree for 'Et fjell er h�yt.':
               S              
      _________|_______        
     NP                VP     
  ___|____          ___|___    
Det       N        V      Adj 
 |        |        |       |   
 et     fjell      er     h�yt
```
