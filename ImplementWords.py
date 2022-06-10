# coding=utf-8
import Listener
from PIL import Image, ImageDraw, ImageFont
import time

path = "/Users/DoDoBird/Desktop/APP/%s.png"
words = str(Listener.listen()).split()
print(words)
timeframes = ['good', 'morning', 'afternoon', 'night', 'tomorrow', 'yesterday', 'end','evening',
              'every week', 'month', 'last', 'next', 'one o’clock', 'January', 'February', 'March',
              'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
topics = ['I','animal', 'Animal', 'zebra', 'Zebra', 'you', 'world', 'women', 'wife', 'man', 'person',
        'children', 'baby', 'family', 'dog', 'cat', 'bird', 'art', 'shop', 'student', 'road', 'car', 'colleague',
          'pregnant', 'friend', 'waiter', 'school', 'teacher', 'police', 'sea', 'factory’, ‘You',
          'World',"Women", "Wife", "Man", "Person", "Children", "Baby", "Family", "Dog","Cat", "Bird",
          "Art", "Shop", "Student", "Road", "Car", "Colleague", "Pregnant", "Friend",
          "Waiter", "School","Teacher", "Police","Sea", 'Factory']
actions = ['goodbye', 'how are you', 'hello', 'talk', 'eat', 'drink', 'walk', 'run', 'arrest', 'speak', 'live',
           'work', 'learn', 'think', 'do', 'come', 'go', 'dead', 'want', 'look', 'break', 'need', 'like', 'love',
           'choke', 'said', 'keep fit', 'help', 'fly', 'try', 'broken', 'know', 'promise', 'ask', 'remember',
           'leave', 'shower', 'read', 'start', 'finish', 'repeat', 'meet', 'hide', 'have', 'hearing', 'charge', 'lock',
           'choose', 'allow', 'hope', 'exercise', 'rest', 'lend', 'bike']
timeFrame = []
topic = []
action = []
final = []
f = 0
g = 0
h = 0
j = 0
i = 0
howareyou = ['how', 'are', 'you']
oneoclock = ['1', "o'clock"]
keepfit = ['keep', 'fit']
everyweek = ['every', 'week']
goodbye = ['good', 'bye']

kk = ['allow', 'arrest', 'ask', 'broken', 'charge', 'children', 'choke', 'choose', 'colleague', 'dead', 'do', 'evening',
      'every week', 'factory', 'finish', 'fly', 'go', 'have', 'hearing', 'hide', 'keep fit', 'know',
      'leave', 'lend', 'like', 'lock', 'like', 'lock', 'look', "one o'clock", 'person', 'pregnant',
      'road', 'said', 'shop', 'shower', 'speak', 'start', 'student', 'talk', 'tomorrow', 'try', 'waiter']
twos = ['arrest', 'ask', 'broken', 'charge', 'choke', 'choose', 'dead', 'do', 'evening', 'go', 'have', 'hearing',
        'hide', 'keep fit', 'know', 'leave', 'lend', 'lock', 'look', 'road', 'said', 'start', 'tomorrow', 'try', 'person']
threes = ['allow', 'factory', 'pregnant', 'waiter']
fours = ['children', 'colleague', 'every week', 'finish', 'fly', 'like', "one o'clock", 'shop', 'shower', 'speak',
         'student', 'talk']

for word in words:
    if word in howareyou:
        f += 1
for word in words:
    if word in oneoclock:
        g += 1
for word in words:
    if word in keepfit:
        h += 1
for word in words:
    if word in everyweek:
        j += 1
for word in words:
    if word in goodbye:
        i += 1
for word in words:
    if word in timeframes:
        timeFrame.append(word)
for word in words:
    if word in topics:
        topic.append(word)
for word in words:
    if word in actions:
        action.append(word)

for variables in timeFrame:
    final.append(variables)
if j == 2:
    final.append('every week')
if g == 2:
    final.append("one o'clock")
for variables in topic:
    final.append(variables)
if f == 3:
    final.append('how are you')
    final.remove('you')
if h == 2:
    final.append('keep fit')
if i == 2:
    final.append('goodbye')
for variables in action:
    final.append(variables)
for word in final:
    for letters in word:
        if letters.isupper() == True:
            letters = letters.lower()

print('Here is your text:  (British Sign Language, n.d.)')
print(final)

if len(final) == 0:
    w = Image.new("RGB", (2000, 1000), "white")
    x = ImageDraw.Draw(w)
    font = ImageFont.truetype('Arial.ttf', 45)
    x.text((830, 10), "Try again from phrase list", font=font, fill=(100, 149, 237))
    w.show()
    time.sleep(2)
else:
    w = Image.new("RGB", (2000, 1000), "white")
    x = ImageDraw.Draw(w)
    font = ImageFont.truetype('Arial.ttf', 45)
    x.text((830, 10), "Here is your text:  (British Sign Language, n.d.)", font=font, fill=(100,149,237))
    w.show()
    time.sleep(2)

for word in final:
    if word in kk:
        if word in twos:
            for x in range(1, 3):
                wordchange = word + str(x)
                Image.open(path % wordchange).show()
                time.sleep(1)
        elif word in threes:
            for x in range(1, 4):
                wordchange = word + str(x)
                Image.open(path % wordchange).show()
                time.sleep(1)
        elif word in fours:
            for x in range(1, 5):
                wordchange = word + str(x)
                Image.open(path % wordchange).show()
                time.sleep(1)
        else:
            break
    else:
        Image.open(path % word).show()
        time.sleep(2)
