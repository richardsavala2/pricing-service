from models.item import Item


url = "https://www.johnlewis.com/2020-apple-ipad-pro-11-inch-a12z-bionic-ios-wi-fi-128gb/space-grey/p4949052"
tag_name = "p"
query = {"class": "price price--large"}

item = Item(url, tag_name, query)
item2 = Item(url, tag_name, query)
print(item.load_price())
