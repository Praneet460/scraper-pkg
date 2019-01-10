from request_setup import simple_get

def get_links(url: str):
    content = simple_get(url)
    links = {}
    for link in content.find_all('a'):
        links[link.text] = link['href']

    return links



if __name__ == '__main__':
    print(get_links('https://www.google.com'))