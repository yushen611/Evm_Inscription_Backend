
from pkg.eventGetter.EventsGetter import get_events
from pkg.token_getter.tokens import *
def testEvent():
    data = get_events()
    for e in data:
        print(e)

def testJson():
    ntf_list, deployFT_map, ft_account_map  = get_valid_tokens()
    print(deployFT_map)

if __name__=="__main__" :
    testEvent()
