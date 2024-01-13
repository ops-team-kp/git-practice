# 1. Import the requests library
import requests
URL = "https://transcripts.gotomeeting.com/#/s/db3e20674772c4558a107266e242e37c85a9d77897396a28ed11394663b60c97"
# 2. download the data behind the URL
response = requests.get(URL)
# 3. Open the response into a new file called instagram.ico
open("AWS", "wb").write(response.content)