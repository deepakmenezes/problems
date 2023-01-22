class Solution:

    def isvalid(self, num: int):
        return chr(num).isalpha() or num == 32

    def decode(self, encodedstring: str) -> str:
        """
        decodes the given encoded string
        :param encodedstring: str
        :return: decoded string
        """
        result = []
        revstr = encodedstring[::-1]

        while (len(revstr) >= 2):

            if self.isvalid(int(revstr[0:2])):
                result.append(chr(int(revstr[0:2])))
                revstr = revstr[2:]
            else:
                result.append(chr(int(revstr[0:3])))
                revstr = revstr[3:]

        return ''.join(result)


if __name__ == "__main__":
    Sol = Solution()

    print(Sol.decode("101411797877682311117"))
    print(Sol.decode("7010117928411101701997927"))
