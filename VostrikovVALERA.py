alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
#второй алфавит если буду фишровать последнюю букву алфавита
encrypt = input("ЯвижуденьгрядущийкакполебранинакоторомсражаютсянизачтоКтотогибнетактотопродолжаетбессмысленнуювознюрадисомнительнойпобедыВосторгэтойпобедыпомеркнетпосколькупобедительнеизбежнобудетповерженСмертью ИягдетовцентревсегоэтоговареваПосредимандецаистинныйсмыслкоторогоускользаетотменяГоворюобэтомкак уловившийпроблескпониманияноВосприятиепеленаетменяпростыняминастоящегоТугокутаетобязательствамивсплескамиэмоцийпривязанностямЗакручиваетподлинногоменявтугиеузлытряпичныхистинСкомканныйвскладкахэтихтряпокизвиваяськаксервьявыползучтобылишьнамгновениеузретьиллюминаторстиральноймашинывкоторойизакончитсямоёокончательноеочищениеКембытынибылнезадаваймнебольшетакихвопросовЯнезнаюкакнанихотвечатьВсетвоивопросыужесодержатвсебеответЯвсеголишьслушаютвойголосоннравитсямнеАвопросыпростопредлодСампосебетынеразговорчивЗаткнисьМолчуТолькопротризеркалоТвойжаркийпротестскрикамииспачкалегослюнойАмнепомимотвоегоголосапонравуитвоявнешность"
key = int(input("6")
encpypt = encrypt.lower() #превращение верхний регистр в нижний
encpypted = ""
#использую цикл for
for letter in encrypt:
 position = alphabet.find(letter) 
 #функция find() обращение к переменной алфавита для поиска совпадения и возвращения к порядковому номеру
 newPosition = position + key 
 #к индексу буквы прибвляется ключ
 if letter in alphabet:
 encrypted = encrypted + alphabet[newPosition]
 else:
 encrypted = encrypted + letter
 print("", encrypted)
