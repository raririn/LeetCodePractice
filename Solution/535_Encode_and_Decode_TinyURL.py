class Codec:
    def __init__(self):
        self.data = []  # Use a list to store urls

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        self.data.append(longUrl)
        return 'http://tinyurl.com/' + str(len(self.data) - 1)
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        todecode = shortUrl.split('/')[-1]
        return self.data[int(todecode)]
        

# A simple but NOT applicable solution.