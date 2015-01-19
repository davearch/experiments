#!/usr/bin/env python
"""
Main entry point. Invoke as `webScrap' or `python -m webScrap'.

"""
import sys
from .webScrap import main
from .webScrap import __version__ as webScrap_version, TreeFlow

if __name__ == '__main__':
    sys.exit(main())
