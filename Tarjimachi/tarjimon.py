def tar(matn):
    import requests
    import json

    url = "https://translo.p.rapidapi.com/api/v3/translate"

    payload = f"from=en&to=uz&text={matn}"
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": "2052bc373bmsh90938c82770c07fp1d3eadjsne5840c836aa5",
        "X-RapidAPI-Host": "translo.p.rapidapi.com"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    result = json.loads(response.text)
    return result['translated_text']


## ARABCHA

def ara(bic):
    import requests
    import json

    url = "https://translo.p.rapidapi.com/api/v3/translate"

    payload = f"from=uz&to=ar&text={bic}"
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": "2052bc373bmsh90938c82770c07fp1d3eadjsne5840c836aa5",
        "X-RapidAPI-Host": "translo.p.rapidapi.com"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    result = json.loads(response.text)
    return result['translated_text']

## Uz Korean

def arauz(bicuz):
    import requests
    import json

    url = "https://translo.p.rapidapi.com/api/v3/translate"

    payload = f"from=uz&to=ko&text={bicuz}"
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": "2052bc373bmsh90938c82770c07fp1d3eadjsne5840c836aa5",
        "X-RapidAPI-Host": "translo.p.rapidapi.com"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    result = json.loads(response.text)
    return result['translated_text']


## Uzb To rus

def uzrus(uzru):
    import requests
    import json

    url = "https://translo.p.rapidapi.com/api/v3/translate"

    payload = f"from=uz&to=ru&text={uzru}"
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": "2052bc373bmsh90938c82770c07fp1d3eadjsne5840c836aa5",
        "X-RapidAPI-Host": "translo.p.rapidapi.com"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    result = json.loads(response.text)
    return result['translated_text']


## Rus to uz

def rusuz(ruuz):
    import requests
    import json

    url = "https://translo.p.rapidapi.com/api/v3/translate"

    payload = f"from=ru&to=uz&text={ruuz}"
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": "2052bc373bmsh90938c82770c07fp1d3eadjsne5840c836aa5",
        "X-RapidAPI-Host": "translo.p.rapidapi.com"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    result = json.loads(response.text)
    return result['translated_text']