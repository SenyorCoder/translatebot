def uzbcha(matn):
    import requests
    import json

    url = "https://translo.p.rapidapi.com/api/v3/translate"

    payload = f"from=uz&to=en&text={matn}"
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": "2052bc373bmsh90938c82770c07fp1d3eadjsne5840c836aa5",
        "X-RapidAPI-Host": "translo.p.rapidapi.com"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    rest = json.loads(response.text)
    return rest['translated_text']
