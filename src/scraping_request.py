import requests
from bs4 import BeautifulSoup

# Requete vers l'URL d'un projet Mantis et scraping avec BeautifulSoup.
# L'idéal serait d'avoir une API pour faire ça
def scrape_project(php_session_id: str, mantis_string_cookie: str, project_id: str):
    cookies = {
        'PHPSESSID': php_session_id,
        'MANTIS_secure_session': '0',
        'MANTIS_STRING_COOKIE': mantis_string_cookie,
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'connection': 'keep-alive',
        'host': 'mantis.elosi.com',
        'referer': 'https://mantis.elosi.com/my_view_page.php',
        'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
    }

    params = {
        'id': project_id,
    }

    response = requests.get('https://mantis.elosi.com/view.php', params=params, cookies=cookies, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    bugnotes = soup.find('div', id='bugnotes')
    
    if bugnotes:
        return bugnotes.get_text(strip=True)
    return None