#  2)მომხარებელს შემოატანინე რიცხვი, და თუ ეს რიცხვი  მეტია 15 ზე, 1 დან ან რიცხვამდე ყველა რიცხვი დაპრინტეთ  ფორ ლუპით 
number = input('enter number:')
if int(number) > 15:
    for i in range (1, int(number)):
        print(i)