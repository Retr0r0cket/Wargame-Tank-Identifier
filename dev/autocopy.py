from PIL import ImageGrab
from subprocess import call

for faction in ['NATO', 'PACT']:
    if faction == 'NATO':
        countries = ['United States', 'France', 'United Kingdom', 'FRG', 'Canada', 'Denmark', 'Norway', 'Sweden']
    else:
        countries = ['Soviet Union', 'GDR', 'Poland', 'Czechoslovakia']
    for country in countries:
        for tank in range(int(input("Number of tanks for " + country + ": "))):
            tankName = input("Tank model: ")
            #source: https://stackoverflow.com/questions/3730964/python-script-execute-commands-in-terminal
            call(['mkdir -p', '../Images/' + faction + '/' + country + '/' + tankName])
            # source: https://stackoverflow.com/questions/7045264/how-do-i-read-a-jpg-or-png-from-the-windows-clipboard-in-python-and-vice-versa
            img = ImageGrab.grabclipboard()
            for image in int(input("Number of images: ")):
                # source: https://stackoverflow.com/questions/1662161/is-there-a-do-until-in-python
                while True:
                    newImg = ImageGrab.grabclipboard()
                    if newImg != img:
                        img = newImg
                        break
                # source: https://www.geeksforgeeks.org/python-pil-image-save-method/
                img.save('../Images/' + faction + '/' + country + '/' + tankName)