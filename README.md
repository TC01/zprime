zprime
======

All the various things I am hacking together for the zprime analysis.

Physics isn't quite like normal software development in the sense that the tools you write (unless you're very good) are
generally not used by other people. That's because you're not developing *software*, exactly. Your finished product is not
the tools to perform an analysis but the analysis itself.

The scripts and so on you write along the way are probably not terribly relevant later.

I don't think that's any excuse to do a bad job on them, though, because better tools = easier analysis. Hence this repo.
It'll probably stay private for now.

Stuff that I work on that *is* probably useful to other people will get spun off and publicized or whatever is necessary.

Patches:
-------

To preserve the hot-swappable nature of Marc's code, any patches to it are
available here.

Run, from your working folder:

patch < patch/onecut.patch
patch < patch/sequencer.patch

Once I write the tool to automatically fix from x import * imports, that will be ran too.

Analysis-in-a-box:
------------------

This is really cool, but probably not practical!

Just run "make". That will *automatically* apply all the cuts in the right
sequence, bringing the analysis up to speed to however far I've gotten!

Useful in case I accidentally rm -rf something.

All output from the analyzer is logged, and all trees and plots are stored.

Sidebands, etc, are not currently being generated. I feel like they should be.

Credits:
--------
Ben Rosser <bjr@pha.jhu.edu>
