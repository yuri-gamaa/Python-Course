import requests as rqs

dict_ = {
    "amount": 20,
    "type": "boolean"
}

resp = rqs.get(url="https://opentdb.com/api.php?", params=dict_)
resp.raise_for_status()

questions = [resp.json()['results'][index]['question'] for index in range(0, 20)]
answers = [resp.json()['results'][index]['correct_answer'] for index in range(0, 20)]
