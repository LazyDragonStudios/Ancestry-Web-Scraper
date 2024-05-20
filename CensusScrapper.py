from bs4 import BeautifulSoup
import requests
import pandas as PD


def scrape_page(url,neighbourhood):
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"html.parser")
    table = soup.find('table', attrs={'class':'subs noBorders evenRows'})

    persons = []
    for row in table.find_all('tr'):
        row_dict = {}
        cells = row.find_all('td')
        if len(cells)==8:
            row_dict["Name"] = cells[0].text.strip()
            row_dict["Sex"] = cells[1].text.strip()
            row_dict["Age"] = cells[2].text.strip()
            row_dict["Birth Year Estimated"] = cells[3].text.strip()
            row_dict["Birthplace"] = cells[4].text.strip()
            row_dict["Race"] = cells[5].text.strip()
            row_dict["House Number"] = cells[6].text.strip()
            row_dict["Schedule Type"] = cells[7].text.strip()
            row_dict["Neighbourhood"] = neighbourhood
            persons.append(row_dict)




    return persons



data = []
user_input=""
while not user_input == "END":
    user_input = input("Please enter UR followed by -- and The name of the neighbood:")
    url, neighbourhood = [part.strip() for part in user_input.split("--")]
    print("URL: ", url)
    print("Neighbourhood: ", neighbourhood)
    data.append(scrape_page(url,neighbourhood))


df = PD.DataFrame(data)
df.to_excel("research_data.xlsx", index = False)
