import urllib.request
from bs4 import BeautifulSoup

BASE_URL = 'https://maps.clarkcountynv.gov/assessor/assessorparceldetail/parceldetail.aspx?hdnParcel={}&hdnInstance=pcl7'

def get_parcel_details(parcel_num):
    url = BASE_URL.format(parcel_num)
    with urllib.request.urlopen(url) as response:
        webpage = response.read()

        soup = BeautifulSoup(webpage, 'html.parser')

        quote_span_1 = soup.find('span', {'id': 'lblDesc3'})
        if quote_span_1:
            print(f'"{quote_span_1.text}"')

        quote_span_2 = soup.find('span', {'id': 'lblLocation'})
        if quote_span_2:
            print(f'"{quote_span_2.text}"')

def main():
     while True:
          parcel_number = str(input("Enter Parcel Number (or 'quit' to exit): ")).strip()
          if parcel_number.lower() == 'quit':
               break
          parcel_num = parcel_number.replace("-", "").strip()
          get_parcel_details(parcel_num)

if __name__ == "__main__":
    main()








        quote_span_1 = soup.find('span', {'id': 'lblDesc3'})
        if quote_span_1:
            results.append(quote_span_1.text)

        quote_span_2 = soup.find('span', {'id': 'lblLocation'})
        if quote_span_2:
            results.append(quote_span_2.text)
        
        quote_span_3 = soup.find('span', {'id': 'lblAddr2'})
        if quote_span_3:
            results.append(quote_span_3.text)
        
        quote_span_4 = soup.find('span', {'id': 'lblAddr3'})
        if quote_span_4:
            results.append(quote_span_4.text)
