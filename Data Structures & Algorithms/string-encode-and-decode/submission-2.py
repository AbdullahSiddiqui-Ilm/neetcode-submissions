class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            holder = str(len(word)) + "#" + word
            encoded += holder
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j]) # '3#cat'
            res.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return res

"""
Pattern: Encoding / Serialization

When multiple pieces of variable-length data must be combined into a single representation and later reconstructed exactly, you need a way to encode the boundaries/length of each piece.

Ask: "When decoding, how will I know where one piece ends and the next begins?"

We will need a prefix length + delimiter which acts as a seperation between the words, allowing us to 
always know the length of the next word and where it starts, being after the delimiter

the length prefix tells you how many characters belong to the word, while the delimiter separates the length from the word.

Encoding pattern: Use a length prefix + delimiter to encode each string. The length tells the decoder exactly how many characters to read, while the delimiter separates the length from the actual word. This allows the original strings to be reconstructed unambiguously.
"""

            


