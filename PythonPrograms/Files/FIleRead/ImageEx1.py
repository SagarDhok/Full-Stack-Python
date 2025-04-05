def imgcopy():
 try:
   with open("C:\\Users\\sdhok\\Downloads\\mahadev.jpg","rb") as rp:
        with open("image.png","wb") as fp:
             img = rp.read()
             fp.write(img)
        print("Image copied successfully - verify")
 except FileNotFoundError:
    print(" Image does not exist ")
imgcopy()