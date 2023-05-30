class Dictionary():
    def __init__(self):
        self.d = {}
        
    def newentry(self, word, definition):
        self.d[word] = definition
        
    def look(self, key):
        if key in self.d:
            return self.d[key]
        else: return f"Can't find entry for {key}"
