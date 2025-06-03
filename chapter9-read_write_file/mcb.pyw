#! python
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
#        py.exe mcb.pyw delete <keyword> - Deletes keyword from the shelf.
#        py.exe mcb.pyw delete - Deletes all keywords from the shelf.

import shelve, pyperclip, sys

mcb_shelf = shelve.open('mcb')

if len(sys.argv) == 3:
  if sys.argv[1].lower() == 'save':
    mcb_shelf[sys.argv[2]] = pyperclip.paste()
  elif sys.argv[1].lower() == 'delete':
    if sys.argv[2] in mcb_shelf:
      del mcb_shelf[sys.argv[2]]
    else:
      print(f"Keyword '{sys.argv[2]}' not found.")
elif len(sys.argv) == 2:
  if sys.argv[1].lower() == 'list':
    pyperclip.copy(str(list(mcb_shelf.keys())))
  if sys.argv[1].lower() == 'delete':
    mcb_shelf.clear()
    print("All keywords deleted.")
  elif sys.argv[1] in mcb_shelf:
    pyperclip.copy(mcb_shelf[sys.argv[1]])


mcb_shelf.close()
