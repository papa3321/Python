from bs4 import BeautifulSoup
soup = BeautifulSoup(open('avustest.html'))
print soup.prettify()
