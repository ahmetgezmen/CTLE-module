def wordlist():
    global firstlist,secondlist,numbers,thirdlist,fourthlist,numbers2,fifthlist,sixthlist,numbers3
    firstlist = ['s', 'q', 'i', 'u', 'v', 'j', 'f', 'n', 't', 'l', 'w', 'z', 'a']
    secondlist = ['p', 'c', 'd', 'x', 'r', 'y', 'h', 'e', 'o', 'k', 'g', 'b', 'm']
    numbers = ['7', '$', '3', '4', ',', '6', '5', '2', '.', '1', '%', '9', '8']
    thirdlist = ['i', 'f', 'w', 'l', 'q', 'v', 's', 'j', 'u', 'z', 'n', 't', 'a']
    fourthlist = ['e', 'd', 'h', 'r', 'g', 'm', 'x', 'b', 'k', 'p', 'y', 'o', 'c']
    numbers2 = ['6', '4', '1', '.', '5', '2', '8', '$', '3', '%', ',', '9', '7']
    fifthlist = ['p', 'q', 'j', 'h', 'b', 'r', 'k', 'm', 'f', 'z', 'o', 'c', 'w']
    sixthlist = ['i', 'a', 'd', 'n', 'g', 'e', 'l', 't', '6', 'x', 's', 'v', 'u']
    numbers3 = ['=', '8', ']', '?', '5', '[', '/', 'y', '^', '_', '.', '*', '{']
wordlist()

def codepassword(todaycodepassword):
    firstrandom = int(todaycodepassword[-1])
    secondrandom = int(todaycodepassword[-2])
    thirdrandom = int(todaycodepassword[-3])
    fourthrandom = int(todaycodepassword[-4])
    fifthrandom = int(todaycodepassword[-5])
    sixthrandom = int(todaycodepassword[-6])
    seventhrandom = int(todaycodepassword[-7])
    eighthrandom= int(todaycodepassword[-8])
    ninthrandom = int(todaycodepassword[-9])
    tenthrandom =int(todaycodepassword[-10])
    one_one = int(todaycodepassword[-11])
    one_two = int(todaycodepassword[-12])
    one_tree= int(todaycodepassword[-13])
    one_four =int(todaycodepassword[-14])
    one_five=int(todaycodepassword[-15])
    one_six=int(todaycodepassword[-16])
    one_seven=int(todaycodepassword[-17])
    one_eight=int(todaycodepassword[-18])
    one_nine=int(todaycodepassword[-19])
    one_ten=int(todaycodepassword[-20])
    global oneone_list,oneone_listreverse,randomlist,randomlistreverse
    oneone_list=[one_one,one_two,one_tree,one_four,one_five,one_six,one_seven,one_eight,one_nine,one_ten]
    oneone_listreverse=[one_one,one_two,one_tree,one_four,one_five,one_six,one_seven,one_eight,one_nine,one_ten]
    oneone_listreverse.reverse()
    randomlist=[firstrandom,secondrandom,thirdrandom,fourthrandom,fifthrandom,sixthrandom,seventhrandom,eighthrandom,ninthrandom,tenthrandom]
    randomlistreverse=[firstrandom,secondrandom,thirdrandom,fourthrandom,fifthrandom,sixthrandom,seventhrandom,eighthrandom,ninthrandom,tenthrandom]
    randomlistreverse.reverse()
def slide(sayı,liste):
    for ssss in range(sayı):
        ekleme = liste[-1]
        liste.pop(-1)
        liste.insert(0,ekleme)
def reslide(sayı,liste):
    for ssss in range(sayı):
        ekleme = liste[0]
        liste.pop(0)
        liste.append(ekleme)
def firstcylinder(message,number):
    outtext = ""
    for x in message:
        if x in firstlist:
            place=firstlist.index(x)
            slide(number, secondlist)
            outtext = outtext+secondlist[place]
            reslide(number,secondlist)

        elif x in secondlist:
            place=secondlist.index(x)
            slide(number,firstlist)
            outtext = outtext+firstlist[place]
            reslide(number,firstlist)
        else :
            outtext = outtext+x
    wordlist()
    return outtext
def defusefirstcylinder(message,number):
    outtext = ""
    for x in message:
        slide(number,secondlist)
        slide(number,firstlist)
        if x in secondlist:
            reslide(number,firstlist)
            place = secondlist.index(x)
            outtext = outtext + firstlist[place]
            slide(number,firstlist)
        elif x in firstlist:
            reslide(number,secondlist)
            place = firstlist.index(x)
            outtext = outtext + secondlist[place]
            slide(number,secondlist)

        else:
            outtext = outtext + x

    wordlist()
    return outtext
def secondcylinder(message,number):
    outtext = ""
    for x in message:
        if x in firstlist:
            place=firstlist.index(x)
            slide(number, numbers)
            outtext = outtext+numbers[place]
            reslide(number,numbers)

        elif x in numbers:
            place=numbers.index(x)
            slide(number,firstlist)
            outtext = outtext+firstlist[place]
            reslide(number,firstlist)
        else :
            outtext = outtext+x
    wordlist()
    return outtext
def defusesecondcylinder(message,number):
    outtext = ""
    for x in message:
        slide(number,numbers)
        slide(number,firstlist)
        if x in numbers:
            reslide(number,firstlist)
            place = numbers.index(x)
            outtext = outtext + firstlist[place]
            slide(number,firstlist)
        elif x in firstlist:
            reslide(number,numbers)
            place = firstlist.index(x)
            outtext = outtext + numbers[place]
            slide(number,numbers)
        else:
            outtext = outtext + x
    wordlist()
    return outtext
def thirdcylinder(message,number):
    outtext = ""
    for x in message:
        if x in numbers:
            place=numbers.index(x)
            slide(number, secondlist)
            outtext = outtext+secondlist[place]
            reslide(number,secondlist)

        elif x in secondlist:
            place=secondlist.index(x)
            slide(number,numbers)
            outtext = outtext+str(numbers[place])
            reslide(number,numbers)
        else :
            outtext = outtext+x
    wordlist()
    return outtext
def defusethirdcylinder(message,number):
    outtext = ""
    for x in message:
        slide(number, secondlist)
        slide(number, numbers)
        if x in secondlist:
            reslide(number, numbers)
            place = secondlist.index(x)
            outtext = outtext + numbers[place]
            slide(number, numbers)
        elif x in numbers:
            reslide(number, secondlist)
            place = numbers.index(x)
            outtext = outtext + secondlist[place]
            slide(number, secondlist)
        else:
            outtext = outtext + x
    wordlist()
    return outtext
def fifthcylinder(message,number):
    outtext = ""
    for x in message:
        if x in thirdlist:
            place=thirdlist.index(x)
            slide(number, fourthlist)
            outtext = outtext+fourthlist[place]
            reslide(number,fourthlist)

        elif x in fourthlist:
            place=fourthlist.index(x)
            slide(number,thirdlist)
            outtext = outtext+thirdlist[place]
            reslide(number,thirdlist)
        else :
            outtext = outtext+x
    wordlist()
    return outtext
def defusefifthcylinder(message,number):
    outtext = ""
    for x in message:
        slide(number,fourthlist)
        slide(number,thirdlist)
        if x in fourthlist:
            reslide(number,thirdlist)
            place = fourthlist.index(x)
            outtext = outtext + thirdlist[place]
            slide(number,thirdlist)
        elif x in thirdlist:
            reslide(number,fourthlist)
            place = thirdlist.index(x)
            outtext = outtext + fourthlist[place]
            slide(number,fourthlist)
        else:
            outtext = outtext + x
    wordlist()
    return outtext
def fourthcylinder(message,number):
    outtext = ""
    for x in message:
        if x in thirdlist:
            place=thirdlist.index(x)
            slide(number, numbers2)
            outtext = outtext+numbers2[place]
            reslide(number,numbers2)

        elif x in numbers2:
            place=numbers2.index(x)
            slide(number,thirdlist)
            outtext = outtext+thirdlist[place]
            reslide(number,thirdlist)
        else :
            outtext = outtext+x
    wordlist()
    return outtext
def defusefourthcylinder(message,number):
    outtext = ""
    for x in message:
        slide(number,numbers2)
        slide(number,thirdlist)
        if x in numbers2:
            reslide(number,thirdlist)
            place = numbers2.index(x)
            outtext = outtext + thirdlist[place]
            slide(number,thirdlist)
        elif x in thirdlist:
            reslide(number,numbers2)
            place = thirdlist.index(x)
            outtext = outtext + numbers2[place]
            slide(number,numbers2)
        else:
            outtext = outtext + x
    wordlist()
    return outtext
def sixthcylinder(message,number):
    outtext = ""
    for x in message:
        if x in numbers2:
            place=numbers2.index(x)
            slide(number, fourthlist)
            outtext = outtext+fourthlist[place]
            reslide(number,fourthlist)

        elif x in fourthlist:
            place=fourthlist.index(x)
            slide(number,numbers2)
            outtext = outtext+str(numbers2[place])
            reslide(number,numbers2)
        else :
            outtext = outtext+x
    wordlist()
    return outtext
def defusesixthcylinder(message,number):
    outtext = ""
    for x in message:
        slide(number, fourthlist)
        slide(number, numbers2)
        if x in fourthlist:
            reslide(number, numbers2)
            place = fourthlist.index(x)
            outtext = outtext + numbers2[place]
            slide(number, numbers2)
        elif x in numbers2:
            reslide(number, fourthlist)
            place = numbers2.index(x)
            outtext = outtext + fourthlist[place]
            slide(number, fourthlist)
        else:
            outtext = outtext + x

    wordlist()
    return outtext
def seventhcylinder(message,number):
    outtext = ""
    for x in message:
        if x in fifthlist:
            place=fifthlist.index(x)
            slide(number, sixthlist)
            outtext = outtext+sixthlist[place]
            reslide(number,sixthlist)

        elif x in sixthlist:
            place=sixthlist.index(x)
            slide(number,fifthlist)
            outtext = outtext+fifthlist[place]
            reslide(number,fifthlist)
        else :
            outtext = outtext+x
    wordlist()
    return outtext
def defuseseventhcylinder(message,number):
    outtext = ""
    for x in message:
        slide(number,sixthlist)
        slide(number,fifthlist)
        if x in sixthlist:
            reslide(number,fifthlist)
            place = sixthlist.index(x)
            outtext = outtext + fifthlist[place]
            slide(number,fifthlist)
        elif x in fifthlist:
            reslide(number,sixthlist)
            place = fifthlist.index(x)
            outtext = outtext + sixthlist[place]
            slide(number,sixthlist)
        else:
            outtext = outtext + x

    wordlist()
    return outtext
def eigthcylinder(message,number):
    outtext = ""
    for x in message:
        if x in fifthlist:
            place=fifthlist.index(x)
            slide(number, numbers3)
            outtext = outtext+numbers3[place]
            reslide(number,numbers3)

        elif x in numbers3:
            place=numbers3.index(x)
            slide(number,fifthlist)
            outtext = outtext+fifthlist[place]
            reslide(number,fifthlist)
        else :
            outtext = outtext+x
    wordlist()
    return outtext
def defuseeigthcylinder(message,number):
    outtext = ""
    for x in message:
        slide(number,numbers3)
        slide(number,fifthlist)
        if x in numbers3:
            reslide(number,fifthlist)
            place = numbers3.index(x)
            outtext = outtext + fifthlist[place]
            slide(number,fifthlist)
        elif x in fifthlist:
            reslide(number,numbers3)
            place = fifthlist.index(x)
            outtext = outtext + numbers3[place]
            slide(number,numbers3)
        else:
            outtext = outtext + x
    wordlist()
    return outtext
def ninthcylinder(message,number):
    outtext = ""
    for x in message:
        if x in numbers3:
            place=numbers3.index(x)
            slide(number, sixthlist)
            outtext = outtext+sixthlist[place]
            reslide(number,sixthlist)

        elif x in sixthlist:
            place=sixthlist.index(x)
            slide(number,numbers3)
            outtext = outtext+str(numbers3[place])
            reslide(number,numbers3)
        else :
            outtext = outtext+x
    wordlist()
    return outtext
def defuseninthcylinder(message,number):
    outtext = ""
    for x in message:
        slide(number, sixthlist)
        slide(number, numbers3)
        if x in sixthlist:
            reslide(number, numbers3)
            place = sixthlist.index(x)
            outtext = outtext + numbers3[place]
            slide(number, numbers3)
        elif x in numbers3:
            reslide(number, sixthlist)
            place = numbers3.index(x)
            outtext = outtext + sixthlist[place]
            slide(number, sixthlist)
        else:
            outtext = outtext + x
    wordlist()
    return outtext
def tenthcylinder(message,number):
    outtext = ""
    for x in message:
        if x in numbers3:
            place = numbers3.index(x)
            slide(number, firstlist)
            outtext = outtext + firstlist[place]
            reslide(number, firstlist)

        elif x in firstlist:
            place = firstlist.index(x)
            slide(number, numbers3)
            outtext = outtext + str(numbers3[place])
            reslide(number, numbers3)
        else:
            outtext = outtext + x
    wordlist()
    return outtext
def defusetenthcylinder(message,number):
    outtext = ""
    for x in message:
        slide(number, firstlist)
        slide(number, numbers3)
        if x in firstlist:
            reslide(number, numbers3)
            place = firstlist.index(x)
            outtext = outtext + numbers3[place]
            slide(number, numbers3)
        elif x in numbers3:
            reslide(number, firstlist)
            place = numbers3.index(x)
            outtext = outtext + firstlist[place]
            slide(number, firstlist)
        else:
            outtext = outtext + x

    wordlist()
    return outtext

def cylinderMathc(text,number,number2):
    if number==1:
        return firstcylinder(text,number2)
    elif number ==2 :
        return secondcylinder(text,number2)
    elif number ==3 :
        return thirdcylinder(text,number2)
    elif number ==4:
        return fourthcylinder(text,number2)
    elif number ==5:
        return fifthcylinder(text,number2)
    elif number ==6:
        return sixthcylinder(text,number2)
    elif number == 7:
        return seventhcylinder(text,number2)
    elif number == 8:
        return eigthcylinder(text,number2)
    elif number ==9 :
        return ninthcylinder(text,number2)
    elif number == 0:
        return tenthcylinder(text,number2)
def cylinderDefuseMathc(text,number,number2):
    if number==1:
        return defusefirstcylinder(text,number2)
    elif number ==2 :
        return defusesecondcylinder(text,number2)
    elif number ==3 :
        return defusethirdcylinder(text,number2)
    elif number ==4:
        return defusefourthcylinder(text,number2)
    elif number ==5:
        return defusefifthcylinder(text,number2)
    elif number ==6:
        return defusesixthcylinder(text,number2)
    elif number == 7:
        return defuseseventhcylinder(text,number2)
    elif number == 8:
        return defuseeigthcylinder(text,number2)
    elif number ==9 :
        return defuseninthcylinder(text,number2)
    elif number == 0:
        return defusetenthcylinder(text,number2)

def encrypt(text,number):
    codepassword(number)
    y=0
    for x in randomlist:
        text = cylinderMathc(text,x,oneone_list[y])
        y+=1
    return text

def defuse(text,number):
    codepassword(number)
    y=0
    for x in randomlistreverse:
        text = cylinderDefuseMathc(text,x,oneone_listreverse[y])
        y+=1
    return text
