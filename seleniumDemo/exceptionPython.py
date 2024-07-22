"""with open('textn.txt','r') as reader:
   reader.read()"""


"""try:
    with open('textn.txt', 'r') as reader:
        reader.read()
except:
    print("There is some error Buddy ")"""


try:
    with open('textn.txt', 'r') as reader:
        reader.read()
except Exception as e:
    print(e)