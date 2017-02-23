# A Random Paragraph Generator

This Python program randomly generates paragraphs using a Context
Free Grammar (CFG). It takes two JSON files as inputs: a rule
dictionary containing phrase structure rules and a lexical
dictionary containing words grouped by parts of speech. It outputs
the file `generated_paragraphs.txt`, which contains the randomly
generated sentences split between one or more paragraphs.

By having the dictionaries separate from the program, the hope is
to eventually allow for the generation of paragraphs in a variety
of languages. However, this is a long-term goal, as the program is
still being developed to handle a wide range of English sentence
generation possibilities.

## The Rule Dictionary
The rule dictionary contains phrase structure rules and weights
for the outputs. These weights are arbitrarily chosen as their
purpose is not to mimic the distribution of various constructions
in English sentences, but to ensure that sentences do not expand
infinitely.

The format of the entries looks like the following:  
```JSON
{"NP":
    {"outputs":
        ["AdjP N", "N PP", "N Conj N", "N"],
    "weights":
        [15, 30, 40, 90]
    }
}
```

## The Lexical Dictionary
The lexical dictionary contains lists of words organized by parts
of speech. Currently the set of words is small for testing purposes.

The format of the entries looks like the following:
```JSON
{"P":
    ["in", "with", "to", "for", "on", "by"]
}
```

## Current Tasks
- [x] Re-write dictionary files from XML into JSON
- [x] Re-write current version of program from C# into Python
- [] Develop a system for tracking agreement
- [] Develop a system for handling multiple tenses
- [] Develop a system for handling verb complements
- [] Develop a system for question inversion
- [] Investigate HPSGs to see if those would work better