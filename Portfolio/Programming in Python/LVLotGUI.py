import urllib.request
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser

BASE_URL = 'https://maps.clarkcountynv.gov/assessor/assessorparceldetail/parceldetail.aspx?hdnParcel={}&hdnInstance=pcl7'

link_url = None

def get_parcel_details(parcel_num):
    results = []
    url = BASE_URL.format(parcel_num)
    with urllib.request.urlopen(url) as response:
        webpage = response.read()
        soup = BeautifulSoup(webpage, 'html.parser')

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
            results.append('\n')

        link_a = soup.find('a', {'id': 'parcelLink2'})
        if link_a:
            link = link_a['href']
            results.append("Link to associate neighborhood map: ")
            results.append(link)

        aerial_link_a = soup.find('a', {'id': 'linkAerialView'})
        if aerial_link_a:
            aerial_link = aerial_link_a['href']
            results.append("Aerial View: ")
            results.append(aerial_link)
            
    return results

def open_link(event):
    if link_url: 
        webbrowser.open(link_url)

def get_details():
    global link_url
    parcel_number = parcel_entry.get().replace("-", "").strip()
    if not parcel_number:
        messagebox.showinfo("Info", "Please enter a parcel number.")
        return
    details = get_parcel_details(parcel_number)
    details_text.delete(1.0, tk.END)
    for detail in details:
        if "http" in detail:
            details_text.insert(tk.END, detail + '\n', 'hyperlink')
            link_url = detail
        else:
            details_text.insert(tk.END, detail + '\n')
    adjust_textbox_height(details_text)

def adjust_textbox_height(text_widget):
    num_lines = int(text_widget.index(tk.END).split('.')[0])
    text_widget.config(height=num_lines)

# GUI

app = tk.Tk()
app.title("Parcel Details Grabber")

frame = ttk.Frame(app, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(frame, text="Enter Parcel Number:").grid(column=0, row=0, sticky=tk.W, pady=5)
parcel_entry = ttk.Entry(frame, width=25)
parcel_entry.grid(column=1, row=0, pady=5)

get_button = ttk.Button(frame, text="Get Details", command=get_details)
get_button.grid(column=1, row=1, columnspan=2, pady=10)

details_text = tk.Text(frame, wrap=tk.WORD, width=50)
details_text.grid(column=0, row=2, columnspan=2, pady=5)

details_text.tag_configure('hyperlink', foreground='blue', underline=1)
details_text.tag_bind('hyperlink', '<Button-1>', open_link)

app.mainloop()
