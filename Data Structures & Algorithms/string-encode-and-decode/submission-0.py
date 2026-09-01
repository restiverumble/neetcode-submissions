class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            length = len(s)
            encoded_string = encoded_string + str(length) 
            encoded_string = encoded_string + "#"
            encoded_string = encoded_string + s
            
        return encoded_string
    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        end_of_string = False

        while not end_of_string:
            if s != "":
                x = 0
                while s[x] != "#":
                    x += 1
                num_letters = int(s[0:x])
                string = s[x+1: x+1 + num_letters]
                s = s[x+1 + num_letters:]
                decoded_strs.append(string)
            else:
                end_of_string = True

        return(decoded_strs)