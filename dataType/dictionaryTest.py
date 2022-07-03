d = {}
urls = {"google":"google.com",18:"unesco.org"}
urls["x"] = 2560
print(urls)

print(len(urls))
print(urls.keys())
print(urls.values())
#딕셔너리.items() : 키와 값을 쌍으로 묶어 dict_items 객체로 리턴
print(urls.items()) #dict_items([('google','google.com'),(18, 'unesco.org'),..])