import requests


def get_repos_stats(user_name) -> list[dict]:
    """
    Собирает статистику по репозиториям заданного пользователя на GitHub.
    :param user_name: никнекйм пользователя на GitHub
    :return: список словарей, содержащих статистику по каждому репозиторию
    """
    try:
        response = requests.get(f'https://api.github.com/users/{user_name}/repos')

        response_json = response.json()

        data = []

        for response in response_json:
            data_dict = {'username': response['name'], 'url': response['url'], 'description': response['description'],
                         'language': response['language'], 'watchers': response['watchers'],
                         'forks_count': response['forks_count']}
            data.append(data_dict)

        return data

    except requests.exceptions.HTTPError as exc:
        print(f"Ошибка: {exc}")

        return []
