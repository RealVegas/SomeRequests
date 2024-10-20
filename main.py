import requests
from pprint import pprint


def github_info(find_request: dict) -> None:

    github_url = 'https://api.github.com/search/repositories'
    response = requests.get(url=github_url, params=find_request)

    print(f'Код ответа: {response.status_code}')
    pprint(response.json())


def placeholder_get(user_data: dict) -> None:

    get_url = ' https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url=get_url, data=user_data)

    print(f'Код ответа: {response.status_code}')
    print(f'Заголовки: {response.headers}')
    print(f'Ответ: {response.json()}')


def placeholder_post(new_data: dict) -> None:

    post_url = ' https://jsonplaceholder.typicode.com/posts'
    response = requests.post(url=post_url, data=new_data)

    print(f'Код ответа: {response.status_code}')
    print(f'Ответ: {response.json()}')


# Программа
print('Информация о репозиториях содержащих html с GitHub')
github_info({'q': 'html'})

print('\nОтвет с jsonplaceholder на get-запрос')
placeholder_get({'userId': 1})

print('\nОтвет с jsonplaceholder на post-запрос')
placeholder_post({'title': 'task_01', 'body': 'task_body', 'userId': 1})