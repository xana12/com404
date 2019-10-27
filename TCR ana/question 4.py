def item_from_suitcase(item): 
    print("I wonder what is i my suitcase..")
response = input()

if (response == "toothbrush"):
    print("A toothbrush. Well, got to have clean teeth!")
elif (response == "spide"):
    print("My Spidey suit! I won't be needing this. I am on holiday.")
else:
    print("An unexpected item! It could be useful")



item_from_suitcase("toothbrush") 
item_from_suitcase("belt")
item_from_suitcase("spidey suit")
