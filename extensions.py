originalmsg=input("File name: ")
loweredmsg=originalmsg.lower()

if ".gif" in loweredmsg:
    print("image/gif")
elif ".jpg" in loweredmsg:
    print("image/jpg")
elif ".jpeg" in loweredmsg:
    print("image/jpeg")
elif ".png" in loweredmsg:
    print("image/png")
elif ".pdf" in loweredmsg:
    print("application/pdf")
elif ".txt" in loweredmsg:
    print("text/plain")
elif ".zip" in loweredmsg:
    print("application/zip")
else:
    print("application/octet-stream")