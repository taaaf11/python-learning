import pyshorteners

def shorten_url(url):
    shortener = pyshorteners.Shortener()
    return shortener.tinyurl.short(url)

url_to_shorten = "https://www.codewars.com/kata/53ea07c9247bc3fcaa00084d/train/python"

shortened_url = shorten_url(url_to_shorten)
shortener = pyshorteners.Shortener()
original_url = shortener.tinyurl.expand(shortened_url)

print(f"Original URL: {original_url}, Shortened URL: {shortened_url}")