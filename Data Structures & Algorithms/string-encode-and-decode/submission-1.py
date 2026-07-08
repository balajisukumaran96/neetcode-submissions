class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        result = []

        for word in strs:
            result.append(str(len(word)))
            result.append("#")
            result.append(word)

        return "".join(result)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            current_len = int(s[i:j])

            i = j + 1
            result.append(s[i:i + current_len])
            i += current_len

        return result