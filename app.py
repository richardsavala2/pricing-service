from models.item import Item


# "https://www.johnlewis.com/2020-apple-ipad-pro-12-9-inch-a12z-bionic-ios-wi-fi-256gb/silver/p4949087"
url = "https://www.johnlewis.com/2020-apple-ipad-pro-12-9-inch-a12z-bionic-ios-wi-fi-256gb/silver/p4949087"
tag_name = "p"
query = {"class": "price price--large"}

ipad = Item(url, tag_name, query)
ipad.save_to_mongo()

items_loaded = Item.all()
print(items_loaded)
print(items_loaded[0].load_price())

