import requests as req

res = req.get('https://api.ipify.org/', headers={"fast":"campus"})
print(res.status_code)
print(res.text)
print(res.request.method)
print(res.request.headers)
print(res.elapsed)
print(res.raw)



