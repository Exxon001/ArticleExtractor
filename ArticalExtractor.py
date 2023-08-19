from bs4 import BeautifulSoup
import requests


def extract(url):
    response = requests.get(url)

    html_content = response.content
    content = ''
    soup = BeautifulSoup(html_content, 'html.parser')
    common_tags = ['article', 'p']
    class_names = ['main-content', 'section-content', 'article', 'wrapper', 'text', 'content']
    num = 0
    try:
        for tag in common_tags:
            tex = soup.find(tag)
            if len(tex.get_text()) > 400:
               for i in tex:
                   content += i.get_text()
            else:
                for classes in class_names:
                    tex = soup.select(f'[class*="{classes}"]')
                    for texts in tex:
                       content += texts.get_text() + "\n"
            break
    except:
        return "Error"
    return content

