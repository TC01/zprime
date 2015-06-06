zprime
======

All the various things I am hacking together for the zprime analysis.

Stuff that I work on that *is* probably useful to other people will get spun off and publicized or whatever is necessary.

This is currently the *old* version of the zprime (formerly known as G*) analysis!
Now I am doing something different, but it's still a zprime analysis, so I'll
be reusing this repo. Current up-to-date stuff will be landing in the master branch.

Patches:
-------

To preserve the hot-swappable nature of Marc's code, any patches to it are
available here.

Run, from your working folder:

```
patch < patch/onecut.patch
patch < patch/sequencer.patch
```

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
