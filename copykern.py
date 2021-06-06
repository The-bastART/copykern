#!/usr/bin/env python
import fontforge, os, sys

src=os.path.abspath(sys.argv[1])
tgt=os.path.abspath(sys.argv[2])
out=os.path.abspath(sys.argv[3])

src_font=fontforge.open(src)
tgt_font=fontforge.open(tgt)

tgt_font.importLookups(src_font, src_font.gpos_lookups)

for tbl in tgt_font.gpos_lookups:
    for subtbl in tgt_font.getLookupSubtables(tbl):
        for gly in src_font:
            if src_font[gly].getPosSub("*"):
                for p in src_font[gly].getPosSub("*"):
                    print(gly,p[2],p[5])
                    tgt_font[gly].addPosSub(subtbl,p[2],p[5])

if out.endswith('sfd'):
    tgt_font.save(out)
else:
    tgt_font.generate(out)