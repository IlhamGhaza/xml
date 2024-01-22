import xml.etree.ElementTree as ET

# Open the XML file
tree = ET.parse("books.xml")

# Get the root element
root = tree.getroot()

# Extract data from each book
categories = set()
category_books = {}

for book in root.findall("book"):
    category = book.get("category")
    categories.add(category)
    
    title = book.find("title").text
    author = book.find("author").text
    year = int(book.find("year").text)
    price = float(book.find("price").text)
    language = book.find("language").text
    publisher = {}
    
    if book.find("publiser"):
        publisher["name"] = book.find("publiser").find("name").text
        publisher["location"] = book.find("publiser").find("location").text
    
    if category not in category_books:
        category_books[category] = []
    
    category_books[category].append({
        "title": title,
        "author": author,
        "year": year,
        "price": price,
        "language": language,
        "publisher": publisher,
    })

# Print the extracted data by category in the order of appearance in the XML file
for category in sorted(categories):
    print(f"\nCategory: {category}")
    
    for book in category_books[category]:
        print("\tTitle:", book['title'])
        print("\tAuthor:", book['author'])
        print("\tYear:", book['year'])
        print("\tPrice:", book['price'])
        print("\tLanguage:", book['language'])
        if book["publisher"]:
            print("\tPublisher:", book["publisher"])
        print("---")
