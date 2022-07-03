pocket = ['paper','cellphone','money','card']
#주머니에 돈이 있으면 택시, 주머니에 돈이 없지만 카드가 있으면 택시, 돈x,card x 걸어가
if 'money' or 'card'in pocket:
    print('taxi')
else:
    print('just walk')

saying = "Life is too short, you need python"
if "wife" in saying : print('wife')
elif "python" in saying and "you" not in saying : print("python")
elif "shirt" not in saying : print("shirt")
elif "need" in saying : print('need')
else: print('none')