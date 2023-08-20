from bs4 import BeautifulSoup
import requests


def extract(url):
    response = requests.get(url)

    html_content = response.content
    content = ''
    soup = BeautifulSoup(html_content, 'html.parser')
    common_tags = ['article', 'p']
    class_names = ['main-content', 'section-content', 'article', 'wrapper', 'text', 'content', 'comments', 'commentswrapper', 'news', 'container']
    id = ['post-content', 'content', 'main', 'container', 'comments', 'COMMENTS', 'news']
    num = 0
    try:
        for tag in common_tags:
            tex = soup.find(tag)
            if len(tex.get_text()) > 400:
               for i in tex:
                   content += "<b>" + "Tag Content: </b>" + i.get_text() + "<br><br>"
            else:
                for classes in class_names:
                    tex = soup.select(f'[class*="{classes}"]')
                    for texts in tex:
                       content += "<b>" + "Class Content: </b>" + texts.get_text() + "<br><br>"
            
            for ids in id:
                print(ids)
                te = soup.select(f'[id*="{ids}"]')
                for t in te:
                    content += "<br><br> <b>" + "ID Content: </b>" + t.get_text() + "<br><br>"
                    print(ids + "1")
            break
    except:
        return "Error, couldn't find any content!"
    return content

