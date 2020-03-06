# Color Palette
Sometimes, you just wanna see how a bunch of colors look together. [Coolors](https://coolors.co/) can generate palettes, but is limited to how many colors.

## Dependencies
* `flask`

## Running
1. Clone the repository.
2. Copy/paste your Coolors links into `links.txt` (don't worry about duplicates)
3. Run `app.py` and go to http://localhost:5000/

## Configuration
(Top of `app.py`)
* `LINK_FILE` (string): path to file holding links, relative to `app.py`
* `SHUFFLE` (boolean): whether or not to shuffle the colors around
* `NUM_BLOCKS` (integer): number of blocks of each color

## To Do
* Make blocks draggable
* Separate config file
* Add block size, blocks per row to config

---
_____onsite, maintained_____
