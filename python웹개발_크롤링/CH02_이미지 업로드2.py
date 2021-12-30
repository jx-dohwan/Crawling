import requests as req

url = "https://imgur.com/a/m2DZajl"

# image.png
with open("image2.png","rb") as f:
    img = f.read()


res = req.post(url, files={
    "image":img,
    "type": "file",
    "name" : "image2.png",
})
print(res.status_code)
print(res.text)

# 200 -> 성공
# 400 -> 보내는 사람 잘 못
# 500 -> 받는 사람 잘 못