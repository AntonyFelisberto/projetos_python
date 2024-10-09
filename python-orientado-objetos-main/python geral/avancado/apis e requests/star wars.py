import requests
import json

def api():
    r = requests.get('https://swapi.dev/api/')
    print(r.json())

def take_result_api(link):
    response = requests.get(link)
    api_result = json.loads(response.content)
    for character in api_result['results']:
        if 'https://swapi.dev/api/films/7/' in character['films']:
            yield character['name'] #yeild is not allowed out of methods or iterations
    if 'next' in api_result and api_result['next'] is not None:
        next_page = take_result_api(api_result['next'])
        for page in next_page:
            yield page

def count_down(num):
    results = []
    while num > 0:
        results.append(num)
        num -= 1
    return results

launch_timer = count_down(5)
for val in launch_timer:
    print(val)

def count_down_better(num):
    while num > 0:
        yield num   #yield will stopp the loop and will only continue when the variable be called again, and will return the actual value in the variable
        num -= 1

launch_timer = count_down_better(5)
for val in launch_timer:
    print(val)

force = take_result_api('https://swapi.dev/api/people/')
for results in force:
    print(results)