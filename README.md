# Magic: The Gathering CLI Tools

I *really* love [Magic: The Gathering](https://en.wikipedia.org/wiki/Magic:_The_Gathering) and wanted to make a set of tools for me to use to create an inventory of my collection, download the card images or art crops of my collection, and create a wallpaper from those images.

# Creation
In the [Creation Directory](Creation/), we have an EDH deck creation tool that takes a Commander's name and looks on EDHRec through the Archidekt section, pulls the UUID and quanities of the cards, parses the UUID's on Scryfall for the card's name, then outputs it into a text file that's setup for use on Moxfield (or any other site that utilizes the same deck list style).

# Imagery
If you're more into images of your inventory, the tools inside [Imagery](Imagery/) will be more up your alley. These tools will allow you to input your cards using the [interactive_cards_with_dl.py](Imagery/interactive_cards_with_dl.py) script which will output the cards into a CSV file. The [image_dl.py](Imagery/image_dl.py) and [art_image_dl.py](Imagery/art_image_dl.py) will download the card imagery from Scryfall and place them into their correct folders.

Once you've completed that, if you want to make a wallpaper out of those images, you can use [create_wallpaper.py](Imagery/create_wallpaper.py) to create a wallpaper with your downloaded card images.

# Inventory
The age old question, "How can I inventory my cards?" These tools will allow you to do so. With [cli_cards.py](Inventory/cli_cards.py), you can do it completely by hand. An example input would be:

How the CLI is laid out: `Card_Name Set_Code Collector_Number Quantity Foil`

CLI Example: `"Evercoat Ursine" blc 64 1 False`

[interactive_cards.py](Inventory/interactive_cards.py) does similar, but walks through each section interactively. A full example is found in the [Inventory](Inventory/README.md) section.