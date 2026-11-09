import sys, unicodedata
from PIL import Image, ImageDraw, ImageFont
LANG=sys.argv[1]; OUT=sys.argv[2]
if LANG=='en':
    CW,CH=10,22; COLS=104
    mono=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf',16)
    monob=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf',16)
    cjk=mono; YOFF=2
else:
    CW,CH=9,22; COLS=115
    mono=ImageFont.truetype('/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc',18,index=7)
    monob=ImageFont.truetype('/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc',18,index=7)
    cjk=mono; YOFF=-2
ROWS=27; PX,PY=24,22
W,H=COLS*CW+2*PX, ROWS*CH+2*PY
BG=(14,16,20); FG=(214,217,222); DIM=(110,118,130); AMBER=(242,165,65); BLUE=(124,196,255); GREY=(139,147,161); FREE=(36,40,48); LINE=(40,44,52)
def wide(c): return unicodedata.east_asian_width(c) in 'WF'
def put(d,col,row,text,color=FG,bold=False):
    x=col
    for c in text:
        px,py=PX+x*CW,PY+row*CH
        if c in '░▓█':
            fill={'░':FREE,'▓':GREY,'█':AMBER}[c]
            d.rectangle([px+1,py+4,px+CW-1,py+CH-4],fill=fill); x+=1; continue
        if wide(c):
            d.text((px,py+YOFF),c,font=cjk,fill=color); x+=2
        else:
            d.text((px,py+YOFF),c,font=monob if bold else mono,fill=color); x+=1
    return x
if LANG=='en':
    T=dict(head='7:00 AM · daily brief', date='Wed 11/11', legend=' ▓ fixed  █ on your planner  ░ free',
      win='Open windows', you='You', cl='Claude',
      rows=[('07','░░','Wake · Breakfast'),('08','░░',''),('09','░░','Leave 9:15'),('10','▓▓','Econ 101 · Hall 210'),('11','▓░',''),('12','░░','Lunch'),('13','░░',''),('14','░░',''),('15','░░',''),('16','░░',''),('17','██','Run'),('18','░░',''),('19','░░','Dinner'),('20','░░',''),('21','░░',''),('22','░░','Sleep 22:30')],
      wins=[' A 08:00–09:00  home  ██ 1h',' B 13:00–16:30  home  ███████ 3h30',' C 19:45–22:30  home  █████ 2h45'],
      wins2=[' A 08:00–09:00  home  ██ 1h',' B 19:45–22:30  home  █████ 2h45'],
      msg1='stats problem set due Friday, about 2 hours',
      cand=['Stats problem set · due Fri · plan 3h12','(2h + 60% buffer)','','★A Wed 13:00–16:30  home  ███████ 3h30  fits in one go',' B Thu 19:00–21:00  home  ████    2h    pair with C',' C Fri 08:00–09:15  home  ██      1h15  finishing only','','A is the only window that fits it in one go.','Reply with letters, e.g. "A" or "B C"'],
      msg2='A', done=['Added to your planner.',"If it doesn't suit, drag it in Google Calendar."],
      block='Stats problem set · Solve', foot='nothing goes on your calendar until you pick')
else:
    T=dict(head='早上 7:00 · 今日安排', date='周三 11/11', legend=' ▓ 固定  █ 已在日历  ░ 空',
      win='还能用的窗口', you='你', cl='Claude',
      rows=[('07','░░','起 · 早饭'),('08','░░',''),('09','░░','出发 9:15'),('10','▓▓','经济学原理 · Hall 210'),('11','▓░',''),('12','░░','午饭'),('13','░░',''),('14','░░',''),('15','░░',''),('16','░░',''),('17','██','跑步'),('18','░░',''),('19','░░','晚饭'),('20','░░',''),('21','░░',''),('22','░░','22:30 睡')],
      wins=[' A 08:00–09:00  在家  ██ 1h',' B 13:00–16:30  在家  ███████ 3h30',' C 19:45–22:30  在家  █████ 2h45'],
      wins2=[' A 08:00–09:00  在家  ██ 1h',' B 19:45–22:30  在家  █████ 2h45'],
      msg1='统计作业周五交，大概 2 小时',
      cand=['统计作业 · 周五截止 · 需 3h12','（估2h + 60% 余量）','','★A 周三 13:00–16:30  在家  ███████ 3h30  一次做完',' B 周四 19:00–21:00  在家  ████    2h    要配 C',' C 周五 08:00–09:15  在家  ██      1h15  只够收尾','','推荐 A：唯一能一次装下的窗口。','挑哪个？回字母，多选写一起（"B C"）'],
      msg2='A', done=['已写进日历。','不合适直接在 Google Calendar 里拖。'],
      block='统计作业 · 做题', foot='你不点头，什么都不会写进日历')
RC=62 if LANG=='en' else 69
def frame(nrows=16, chat=[], booked=False, flash=False):
    im=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(im)
    x=PX+(RC-2)*CW; d.line([x,PY,x,H-PY],fill=LINE,width=1)
    put(d,RC,0,T['head'],DIM); put(d,RC,1,T['date'],FG,True)
    for i,(h,c,l) in enumerate(T['rows'][:nrows]):
        r=3+i
        if booked and h in ('13','14','15'):
            c='██'; l=T['block'] if h=='13' else ''
        put(d,RC,r,h+' ',DIM); put(d,RC+3,r,c)
        if l: put(d,RC+6,r,l,AMBER if (booked and h=='13') else FG)
        if flash and booked and h in ('13','14','15'):
            px=PX+(RC+2)*CW; py=PY+r*CH; d.rectangle([px,py+2,px+CW*4,py+CH-2],outline=AMBER)
    if nrows>=16:
        put(d,RC,20,T['legend'],DIM); put(d,RC,22,T['win'],FG,True)
        for i,w in enumerate(T['wins2'] if booked else T['wins']): put(d,RC,23+i,w)
    row=0
    for who,lines in chat:
        put(d,0,row,(T['you'] if who=='you' else T['cl'])+' ›',BLUE if who=='you' else AMBER,True); row+=1
        for ln in lines:
            if ln.startswith('★'):
                put(d,2 if LANG=='en' else 1,row,'★',AMBER,True); put(d,3,row,ln[1:])
            else: put(d,2,row,ln, FG if who!='sys' else DIM)
            row+=1
        row+=1
    put(d,0,ROWS-1,T['foot'],DIM)
    return im
frames=[];durs=[]
def add(im,ms): frames.append(im); durs.append(ms)
for n in range(1,17): add(frame(n),70)
add(frame(16),1600)
s=T['msg1']
for k in range(1,len(s)+1,2 if LANG=='en' else 1): add(frame(16,[('you',[s[:k]+'▏'])]),45 if LANG=='en' else 80)
add(frame(16,[('you',[s])]),500)
for k in range(1,len(T['cand'])+1): add(frame(16,[('you',[s]),('cl',T['cand'][:k])]),110)
add(frame(16,[('you',[s]),('cl',T['cand'])]),2400)
chat=[('you',[s]),('cl',T['cand']),('you',['A'])]
add(frame(16,chat),700)
chat2=chat+[('cl',T['done'])]
for f in range(3): add(frame(16,chat2,booked=True,flash=(f%2==0)),250)
add(frame(16,chat2,booked=True),3500)
pal=[im.convert('P',palette=Image.ADAPTIVE,colors=64) for im in frames]
pal[0].save(OUT,save_all=True,append_images=pal[1:],duration=durs,loop=0,optimize=True,disposal=1)
frames[len(frames)-1].save(OUT.replace('.gif','-last.png'))
frames[30].save(OUT.replace('.gif','-mid.png'))
print(len(frames), W,H)
