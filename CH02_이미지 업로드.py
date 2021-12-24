import requests as req

# webhook.site 에 접속

# res = req.get("https://webhook.site/e2d543b8-5038-4a43-97d9-810f19523603?name=hi",headers={
#     "User-Agent":"fastcampus/401"
# })
# print(res.text)

url = "https://webhook.site/e2d543b8-5038-4a43-97d9-810f19523603"
res = req.post(url,data={
    "nane":"hi"
})
print(res.text)