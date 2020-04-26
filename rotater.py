from PIL import Image
import os
from pathlib import Path
import requests

class ImageRotate:
    def __init__(self):
        self.images = []

    def __del__(self):
        for path in self.images:
            os.remove(path)
    
    # returns path of the rotated image
    def _img_rotate(self, filepath: str, degrees: int) -> str:
        img : Image = Image.open(filepath)
        os.remove(filepath)

        out : Image = img.rotate(degrees, expand=True)

        file_name = filepath.split("/")[-1] 

        Path("./Images").mkdir(parents=True, exist_ok=True)

        out_path = "./Images/" + file_name
        out.save(out_path, img.format)
        return out_path

    # returns path of the downloaded image
    def _img_save(self, url: str) -> str:
        Path("./Images/Downloads").mkdir(parents=True, exist_ok=True)

        out_path : str = "./Images/Downloads/" + str(hash(url)) + ".jpg"
        f = open(out_path, "wb")
        f.write(requests.get(url).content)
        f.close()
        return out_path

    # Returns the path of the downloaded and converted image
    def img_convert(self, url: str, degrees: int) -> str:
        img_path = self._img_save(url)
        return self._img_rotate(img_path, degrees)

    # Deletes the image from the path
    def img_delete(self, filepath: str):
        os.remove(filepath)
        self.images.remove(filepath)

    

if __name__ == '__main__':
    # name : str = img_rotate("_fub.jpg", 90)
    # assert name == "_fub.jpg" , "filename is wrong: {}".format(name) 
    # f = open("01.jpg", "wb")
    # f.write(requests.get("https://cdn.discordapp.com/attachments/698416591099920394/703183203728490586/fub.jpg").content)
    # f.close()
    img_rotater = ImageRotate()
    print(img_rotater.img_convert("https://cdn.discordapp.com/attachments/698416591099920394/703183203728490586/fub.jpg", -90))

    