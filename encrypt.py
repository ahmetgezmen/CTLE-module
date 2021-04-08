import datetime
from templates import mainleft, mainright, textedit
def codeControl(code):
    try:
        code=int(code)
        return "true"
    except:
        return "false"
def coder(toDayCode):
    datetimenow = datetime.datetime.now()
    day = datetimenow.day
    month = datetimenow.month
    year = datetimenow.year
    todaycodepassword = str((day + month + year) * int(toDayCode))
    return  todaycodepassword

def encrypt(text,code):
    if (codeControl(code)=="true"):
        textList = textedit.separate(text)
        outputleft = mainleft.encrypt(textList[0], code)
        outputright = mainright.encrypt(textList[1], code)
        output = outputleft + outputright
        return output
    else:
        return "Please use numbers only "


def defuse(text,code):
    if (codeControl(code)=="true"):
        textList = textedit.separate(text)
        outputleft = mainleft.defuse(textList[0], code)
        outputright = mainright.defuse(textList[1], code)
        output = outputleft + outputright
        return output
    else:
        return "Please use numbers only "


def dailyChangingEncrypt(text,codex):
    if (codeControl(codex)=="true"):
        code=coder(codex)
        textList = textedit.separate(text)
        outputleft = mainleft.encrypt(textList[0], code)
        outputright = mainright.encrypt(textList[1], code)
        output = outputleft + outputright
        return output
    else:
        return "Please use numbers only "
def dailyChangingDefuse(text,codex):
    if (codeControl(codex)=="true"):
        code=coder(codex)
        textList = textedit.separate(text)
        outputleft = mainleft.defuse(textList[0], code)
        outputright = mainright.defuse(textList[1], code)
        output = outputleft + outputright
        return output
    else:
        return "Please use numbers only "

