### If else basic ii

# * Checking if a itemList is empty or not
# itemList = []
# if itemList:
#     for item in itemList:
#         print(item)
# else:
#     print("Sorry, the itemList is empty :(")


item = []
requestedItem = [1 ]# list(range(3, 11))

if item and requestedItem:
    for tempRequestedItem in requestedItem:
        if tempRequestedItem in item:
            print(f"It's available, item no. {tempRequestedItem}")
        else:
            print(f"Sorry, this item is not available. Item no. {tempRequestedItem}")
elif requestedItem:
    print("Sorry, no item is currently available")
else:
    print("Sorry, you didn't make any request for any item")