import requests

# URL to the data file
data_url = "https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/misc/2020/5/7d3576d97e7560ae85135cc214ffe2b3412c51d7.csv"

# Function to download the data file
def download_data_file(url, save_path):
    response = requests.get(url)
    with open(save_path, "wb") as file:
        file.write(response.content)

# Save the data file in the current directory
save_path = "Popular_Baby_Names.csv"
download_data_file(data_url, save_path)

