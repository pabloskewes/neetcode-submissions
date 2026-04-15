SEP = "#"

class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}{SEP}{s}" for s in strs)

    def decode(self, encoded_str: str) -> List[str]:
        decoded_strs = []
        word_begin = 0
        sep_position = encoded_str.find(SEP)
        while sep_position != -1:
            word_length = int(encoded_str[word_begin:sep_position])
            next_word_pos = sep_position + word_length + 1
            word = encoded_str[sep_position + 1:next_word_pos]
            decoded_strs.append(word)

            word_begin = next_word_pos
            sep_position = encoded_str.find(SEP, word_begin)

        return decoded_strs


        