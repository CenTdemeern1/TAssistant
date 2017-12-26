from test import *
from google import search
from time import sleep

t = hear()

def r(tr, ra, a=t):
    if tr == a: return ra
    else: return None
def m(tr, ra, a=t.split()):
    try:
        for l in range(len(tr)):
            trv = tr[l]
            if trv in a:
                pass
            else: raise BaseException
        return ra
    except BaseException:
        return None
def google(searchq):
    urls = []
    for url in search(searchq, stop=5):
        urls.append(url)
    return urls

#if t == 'test':
#    say('loud and clear!')
if t == 'Google search':
    urls = google(hear())
    print('top result is ' + urls[0])

    print('second result is ' + urls[1])

    print('third result is ' + urls[2])

    print('fourth result is ' + urls[3])

    print('fifth result is ' + urls[4])


    say('top result is ' + urls[0])
    sleep(15)
    say('second result is ' + urls[1])
    sleep(15)
    say('third result is ' + urls[2])
    sleep(15)
    say('fourth result is ' + urls[3])
    sleep(15)
    say('fifth result is ' + urls[4])
elif m(['music'], True):
    say('media playing isn\'t implemented yet.')
else:
    say(r('test','loud and clear!') or r('boom','kapow') or r('hello', 'how\'s it going?'))
