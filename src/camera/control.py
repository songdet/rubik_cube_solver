import requests

def take_photo(ip_address, port, img_file):

    # Synthesize the url to take photo from
    image_url = "http://" + str(ip_address) + ":" + str(port) + "/capture"

    # Need to request image twice to refresh new photo for some reason
    image_data = requests.get(image_url).content
    image_data = requests.get(image_url).content

    # Write image data to image_file location
    with open(img_file, 'wb') as handler:
        handler.write(image_data)
        