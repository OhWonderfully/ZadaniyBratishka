import string
from pprint import pprint
 
symbols = string.ascii_letters #перечесление букв(все регистры)Вверх низ!
step = int(len(symbols) ** .5) #len возвращение кол-ва элементов в списке(ВОПРОС RETURN НУЖЕН ИЛИ НЕТ?)
 
if len(symbols) > step * step:
    step += 1
 
n = step * step - len(symbols)
if n > 0:
    symbols += "-" * n
matrix = [symbols[i:i+step].ljust(step, "-") for i in range(0, len(symbols), step)]
last = len(matrix) - 2 if n > 0 else 1
 
 
def encode(text):
    result = []
    for ch in text:
        for i, line in enumerate(matrix):
            if ch in line:
                j = line.index(ch)
                i = 0 if i == last or matrix[i + 1][j] == "-" else i + 1
                result.append(matrix[i][j])
                break
    return "".join(result)
 
 
def decode(text):
    result = []
    for ch in text:
        for i, line in enumerate(matrix):
            if ch in line:
                j = line.index(ch)
                i = last if i == 0 else i - 1
                ch = matrix[i][j]
                result.append(matrix[i - 1][j] if ch == "-" else ch)
                break
    return "".join(result)
 
pprint(matrix)
result = encode("WhyisreadingnotpopulartodayTeenagerstrytospendtheirfreetimewiththeircellphonesTheycanchatplaytextbuttheydontreadWecanalwayshearthatourministersofeducationattributethecrisisofreadingtomethodsofteachingIntheirspeeches theycallteachingtooarchaicortoomodernInmyopinionthesemethodshavenothingtodowiththeteenagersdisaffectionofthbookReadingisanactivitythatcanonlybe practicedinsilenceandsolitudeIthinkitisthereasonwhytherearereadingproblems amongteenagerstodayEverythingthatwecanseeintheworldisfullofnoisenowIfwecanlistentomusictogetherwecantreadtogetherWecanreadonlyaloneItisevenagreatpleasurewhenwediscoveredthebookthatwecanthinkoverbeingaloneAndonly afterthatwewillbereadytoshareourthoughtswiththeothersifweliketodothatBut solitudeandsilencearenowluxuriousgoodsinourhecticworldThatiswhyreadingcantbecomeahobbyforteenagersunfortunately")
print(result)
print(decode(result))
