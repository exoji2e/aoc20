import os, glob, time
import progressbar
from datetime import datetime
def log(s):
    print('Fetch: {}'.format(s))

def submit_real(year, day, level, answer): 
    import requests, bs4
    from secret import session
    jar = requests.cookies.RequestsCookieJar()
    jar.set('session', session)
    url = 'https://adventofcode.com/{}/day/{}/answer'.format(year, day)
    byte_ans = str(answer).encode('utf-8')
    assert level == 1 or level == 2
    byte_level = b'1' if level == 1 else b'2'
    data = {
        b'answer' : byte_ans,
        b'level' : byte_level
    }
    r = requests.post(url, data=data, cookies=jar)
    
    Correct = "That's the correct answer"
    if not r.status_code == 200:
        return 'StatusCode: {}\n{}'.format(r.status_code, r.text)
    
    html = bs4.BeautifulSoup(r.text, 'html.parser')
    return html.find('article').text
    

def submit(year, day, level, answer):
    print('About to submit: "{}" on {}-{} part {}'.format(answer, year, day, level))
    print('Confirm submit? y/N')
    ans = input()
    if ans.lower() == 'y':
        print('Submitting {}'.format(answer))
        text = submit_real(year, day, level, answer)
        if "That's the correct answer" in text:
            print('AC!')
        print('>> ' + text)
        return text
    else:
        print('Skipping submit')



def dl(fname, day, year):
    import requests
    from secret import session
    jar = requests.cookies.RequestsCookieJar()
    jar.set('session', session)
    url = 'https://adventofcode.com/{}/day/{}/input'.format(year, day)
    r = requests.get(url, cookies=jar)
    if 'Puzzle inputs' in r.text:
        log('Session cookie expired?')
        return r.text
    if "Please don't repeatedly request this endpoint before it unlocks!" in r.text:
        log('Output not available yet')
        return r.text
    if r.status_code != 200:
        log('Not 200 as status code')
        return r.text
    with open(fname,'w') as f:
        f.write(r.text)
    return 0

def mkdirs(f):
    try:
        os.makedirs(f)
    except: pass

def wait_until(date_time):
    now = datetime.now()
    tE = date_time.timestamp()
    t0 = now.timestamp()
    M = int(tE-t0) + 1
    if M <= 0: return
    widgets=[
        ' [', progressbar.CurrentTime(), '] ',
        progressbar.Bar(),
        ' (', progressbar.ETA(), ') ',
    ]
    print(f'waiting from {now} until {date_time}')
    bar = progressbar.ProgressBar(max_value=int(tE-t0), widgets=widgets)
    while time.time() < tE:
        cT = time.time()
        bar.update(min(M, int(cT - t0)))
        time.sleep(1)
    bar.finish()

def get_input_file_name(year, day):
    return 'cache/{}-{}.in'.format(year, day)


def fetch(year, day, log, force=False, wait_until_date=-1):
    filename = get_input_file_name(year, day)
    mkdirs('cache')
    exists = os.path.isfile(filename)
    if not exists or force:
        if wait_until_date != -1:
            wait_until(wait_until_date)

        out = dl(filename, day, year)
        if out != 0:
            return out
    return open(filename, 'r').read().strip('\n')


def get_samples(year, day):
    d = 'samples/{}_{}'.format(year,day)
    mkdirs('samples')
    mkdirs(d)
    samples = []
    for fname in glob.glob('{}/*.in'.format(d)):
        inp = open(fname, 'r').read().strip('\n')
        samples.append((fname, inp))
    return samples

