# WEBCRAWLER EXTRACTING LINKS

page = "Moses ouma <a href='www.google.com'>MY WEB</a>"

start_link = page.find("<a href=")
link = page[start_link:]

start_url = link.find("'")
end_url = link.find("'", start_url + 1)

print(link[start_url + 1:end_url])

