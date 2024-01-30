
from pkg.eventGetter.EventsGetter import get_events

def testEvent():
    data = get_events()
    for e in data:
        print(e)

def testJson():
    ...

if __name__=="__main__" :
    data = get_events()
    for e in data:
        print(e)
