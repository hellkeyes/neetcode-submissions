class Solution:
    # strs = [ 'hello', 'world' ]

    def encode(self, strs: List[str]) -> str:
        
        encode_string = ''
        for i in strs:
            #findin the lenght of string
            encode_string += '#'
            length = len(i)
            encode_string += str(length)
            encode_string += '#'

            # encodin the string
            i = i[::-1]  # we reverse it

            for ch in i:   #move all character 3 steps forward
                encode_string += chr(ord(ch) + 3)

        return encode_string

    def decode(self, s: str) -> List[str]:
        # #5#roohk#5#gourz
        n = len(s)
        i = 0
        decoded = [] 

        while i < n:      
            length = ''
            my_str = ''
            decode_string = ''
            
            if s[i] == '#':     # we encounter first #
                i += 1
                
            while s[i] != '#':           #find the length of our string till we encounter another #
                    length += s[i]
                    i += 1
            length = int(length)

            while length > 0:        # move forward the length we found ignoring any symbol or integer
                i += 1
                my_str += s[i]  # our string
                length -= 1

            for ch in my_str:       # we move 3 steps back in our string
                decode_string += chr((ord(ch) - 3))      

            decode_string = decode_string[::-1]      #we reverse it
            decoded.append(decode_string) 

            i += 1

        return decoded