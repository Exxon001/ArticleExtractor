from bs4 import BeautifulSoup
import requests


def extract():
    user_url = input("Url: ")
    response = requests.get(user_url)

    html_content = response.content
    content = ''
    soup = BeautifulSoup(html_content, 'html.parser')
    common_tags = ['div']
    class_names = ['main-content', 'section-content', 'maincontent', 'sectioncontent', 'article']
    num = 0
    for classes in class_names:
        tex = soup.select(f'[class*="{classes}"]')
        for texts in tex:
            content += texts.get_text(strip=True)
            print(f"{classes}: {content}")
    return content
    '''
    for tag in common_tags:
        article = soup.find_all(tag)
        for i in article:
            print(tag + " " + str(num))
            if len(i) > 5:
               content += i.get_text() + '\n'
    return content
    '''

print(extract())