# grubhub_giftcard_script
Script to use to purchase GrubHub giftcards in bulk

## Requirements
Need to install selenium for python:
```
pip3 install selenium
```

Need to have ChromeDriver. 
https://chromedriver.chromium.org/downloads

It needs to be the same version of chrome you currently have. To check, go to `chrome://version` in your Google Chrome browser.

Also, don't have any devtools of any type running - could interfere with selenium interacting with the browser.

## NOTES:

Max of $1999 in total gift cards per transaction. (Any more, you need to register for a GrubHub corporate account).

Max of 15 unique recipeints per transaction.

If you run into issues where the browser can't find the element, try and add a wait between. 
```
import time

time.sleep(1) # 1 second wait
```
