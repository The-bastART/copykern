# copykern
This little python script copies all the kerning information from one font to another.
It needs python-fontforge installed and works from command-line like this:

`./copykern.py source.ttf target.ttf outfile.ttf`

It is inspired by the [transpacing](https://github.com/ManufacturaInd/tinytypetools/tree/master/transpacing) script by  [ManufacturaInd](https://github.com/ManufacturaInd) which didn't work for me. They also use the `font.importLookups` which seems to only copy the table and subtable structure but not the actual entries. My script just cycles through all glyphs and copies the entries manually.
I'm not sure how well it works with more tables/subtables since I have no experience with / need for those at the moment.
