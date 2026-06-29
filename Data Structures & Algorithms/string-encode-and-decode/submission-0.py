class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_strgs=""
        for s in strs:
            encoded_strgs=encoded_strgs+str(len(s))+"#"+s
        return encoded_strgs

    def decode(self, s: str) -> List[str]:
        decoded_strgs=[]
        ptr = 0
        while ptr < len(s):
            j = ptr

            while s[j] != "#":
                j +=1
            length = int(s[ptr:j])
            decoded_strgs.append(s[j + 1 : j + 1 + length])
            ptr = j + 1 + length
        return decoded_strgs
