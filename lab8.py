

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
    items = []
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split(',')
            item_type = parts[0]
            if item_type == "Book":
                items.append(Book(*parts[1:]))
            elif item_type == "Article":
                items.append(Article(*parts[1:]))
            elif item_type == "Podcast":
                items.append(Podcast(*parts[1:]))
    return items

if _name_ == "_main_":
    # 6 Archive Items
    items = [
        Book("B001", "Deep Learning", 2018, "Ian Goodfellow", 775),
        Book("B002", "Clean Code", 2020, "Robert C. Martin", 464),
        Article("A101", "Quantum Computing", 2022, "Nature", "10.1234/qc567"),
        Article("A102", "AI Ethics", 2021, "AI Journal", "10.5678/ai2021"),
        Podcast("P301", "TechTalk AI", 2023, "Jane Doe", 45),
        Podcast("P302", "History Now", 2016, "Mark Smith", 30)
    ]

    save_to_file(items, "archive.txt")

    loaded_items = load_from_file("archive.txt")

    print("All Items:")
    for item in loaded_items:
        print(item)

    print("\nRecent Items (Last 5 Years):")
    for item in loaded_items:
        if item.is_recent(5):
            print(item)
            
    print("\nArticles with DOI starting '10.1234':")
    for item in loaded_items:
        if isinstance(item, Article) and item.doi.startswith("10.1234"):
            print(item)
