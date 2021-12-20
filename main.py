import requests


def get_from_instapaper():
    pass


def add_to_instapaper(article_url):
    request_url = 'https://www.instapaper.com/api/add'
    parameters = {'username': 'navid.ahmadian@gmail.com', 'password': '91929394', 'url': article_url}

    x = requests.post(request_url, data=parameters)

    print(x.text)


if __name__ == '__main__':
    urls = ['https://www.kojaro.com/2018/4/19/141888/%D8%B9%D8%B1%D8%A8%D8%B3%D8%AA%D8%A7%D9%86-%D8%B5%D8%B9%D9%88%D8'
            '%AF%DB%8C-%D9%87%D8%AA%D9%84/', 'https://codepaz.com/advice/',
            'https://amanjacademy.com/what-is-lcp-and-how-to-improve-this-for-seo/',
            'https://www.farjadp.com/website-optimization-consultancy-seo/']

    for url in urls:
        add_to_instapaper(url)
