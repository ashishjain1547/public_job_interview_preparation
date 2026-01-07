from bs4 import BeautifulSoup
import os

with open(os.path.join(os.getcwd(), 'writeup.html'), 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')

# Now you can use soup to parse the HTML file

# Sort the div > a based on href attribute value and write to a new output html
div_elements = soup.find_all('div', {'class': 'separator'})
div_elements = sorted(div_elements, key=lambda x: x.a['href'].split("%")[-1])

with open(os.path.join(os.getcwd(), 'output.html'), 'w') as f:
    for div_element in div_elements:
        f.write(str(div_element))
