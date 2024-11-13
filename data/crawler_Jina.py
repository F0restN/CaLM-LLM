import requests
import utils.output_file as output_file
import json

url = "https://r.jina.ai/https://pmc.ncbi.nlm.nih.gov/articles/PMC11320145/"
headers = {
    'Authorization': 'Bearer jina_84941d4f49324915a81d2d61c2ab1255MMHqnl8Usv2mEC1TbkSONxxf_kal',
}

response = requests.get(url, headers=headers)

# print("Hello World")
