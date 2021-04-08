def separate(text):
    output=[]
    if len(text)%2==1:
        length = len(text)+1
        lengthHalf = int(length / 2)
        outStringLeft = text[0:lengthHalf]
        outStringRight = text[lengthHalf:]
        output.append(outStringLeft)
        output.append(outStringRight)
    elif len(text)%2==0:
        length=len(text)
        lengthHalf=int(length/2)
        outStringLeft=text[0:lengthHalf]
        outStringRight=text[lengthHalf:]
        output.append(outStringLeft)
        output.append(outStringRight)
    return output