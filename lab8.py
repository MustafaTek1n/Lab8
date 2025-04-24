

class ArchiveItem:  
    def __init__(self, uid, title, year):  
        self.uid = uid
        self.title = title 
        self.year = int(year)

    def __str__(self):  
        return f"{self._class_._name_} -> UID: {self.uid}, Title:{self.title}, Year : {self.year}"  

    def __eq__(self,other):
        return isinstance(other,ArchiveItem) and self.uid == other.uid
        
    def is_recent(self,n):
        return self.year >= (2025-n)
        
    
class Book(ArchiveItem):
    def __init__(self,uid,title,author,pages):
        super().__init__(uid,title,year)
        self.author=author
        self.pages=int(pages)
        
    def __str__(self):
        return f"Book -> UID: {self.uid}, Title: {self.title}, Year: {self.year}, Author: {self.Author}, Pages: {self.pages}"
        

class Artricle(ArchiveItem):
    def __init__(self,uid,title,year,journal,doi):
        super().__init__(uid,title,year)
        self.journal=journal
        self.doi=doi
        
    def __str__(self):
        return f"Artricle -> UID: {self.uid}, Title: {self.title}, Year: {self.year}, Journal: {self.Journal}, DOI: {self.doi}"
        
class Podcast(ArchiveItem):
    def __init__(self,uid,title,year,host,duration):
        super().__init__(uid,title,year)
        self.host=host
        self.duration=duration
        
    def __str__(self):
        return f"Podcast -> UID: {self.uid}, Title: {self.title}, Year: {self.year}, Host: {self.host}, Duration: {self.duration}"
    


def save_to_file(items, filename):
    with open(filename,'w') as f:
        for item in items:
            if isinstance(item,Book):
                f.write(f"Book,{item.uid},{item.title},{item.year},{item.author},{item.pages}\n)
            elif isinstance(item,Artricle):
                f.write(f"Article,{item.uid},{item.title},{item.year},{item.journal},{item.doi}\n)
            elif isinstance(item,Podcast):
                f.write(f"Podcast,{item.uid},{item.title},{item.year},{item.host},{item.duration}\n)
                

def load_from_file(filename):
    
