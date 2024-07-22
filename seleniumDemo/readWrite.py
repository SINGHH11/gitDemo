with open('text.txt', 'r') as reader:
    content = reader.readlines()
    content.reverse()
    print(content)
    with open('text.txt', 'w') as writer:
        for i in range (0,len(content)):
            writer.write(content[i])






