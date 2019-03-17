from bs4 import BeautifulSoup
import requests

link = 'https://archive.org/stream/DopeInc.BritainOpiumWarAgainstTheUs1978.pdfVersion2/DopeInc.BritainOpiumWarAgainstTheUs1978_djvu.txt'

def simple_parser(link):
    pure_text = ''
    html = requests.get(link)
    soup = BeautifulSoup(html.text, 'lxml')
    content = soup.find(id='maincontent')
    title = content.h1.text
    dirt_text = content.pre.text
    pure_text += str(title) + '\n' + dirt_text
    with open('draft.txt', 'w', encoding='utf-8') as draft:
        draft.write(pure_text)
    return pure_text

simple_parser(link)


