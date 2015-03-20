# Write Python code that assigns to the 
# variable url a string that is the value 
# of the first URL that appears in a link 
# tag in the string page.
# Your code should print http://udacity.com
# Make sure that if page were changed to
# page = '<a href="http://udacity.com">Hello world</a>'
# that your code still prints the same thing.

# page = contents of a web page
page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')
start_link = page.find('<a href=')
urlBeginning = page[start_link:].find('"');
urlEnding = page[start_link + urlBeginning + 1:].find('"')

url = page[start_link + urlBeginning + 1: start_link + urlBeginning + urlEnding + 1]
print(url)