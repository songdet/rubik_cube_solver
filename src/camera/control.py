import requests

def take_photo(ip_address, img_file, port="80"):
    camera = Camera(ip_address, port)
    camera.take_photo(img_file)
        
class Camera:

    def __init__(self, ip_address, port="80"):
        self._ip_address = ip_address
        self._port = port

    def take_photo(self, img_file):
        
        # Synthesize the url to take photo from
        image_url = "http://" + str(self._ip_address) + ":" + str(self._port) + "/capture"

        # Need to request image twice to refresh new photo for some reason
        image_data = requests.get(image_url).content
        image_data = requests.get(image_url).content

        # Write image data to image_file location
        with open(img_file, 'wb') as handler:
            handler.write(image_data)
