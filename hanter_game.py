import curses
import random
import time
scren = curses.initscr()
curses.curs_set(0)
scren_hight, scren_width = scren.getmaxyx()
window = curses.newwin(scren_hight, scren_width, 0,0)
window.keypad(1)
window.timeout(100)

#جسم الهانتر
hanter_x = scren_width//4 
hanter_y = scren_hight//2
hanter = [[hanter_y , hanter_x],
          [hanter_y , hanter_x - 1]]

#جسم الهدف
enemy_x = scren_width//2
enemy_y = scren_hight//2
enemy = [[enemy_y , enemy_x]]
window.addch(enemy[0][0], enemy[0][1], curses.ACS_PI)
key = curses.KEY_RIGHT

while True :
    #تحديد اتجاه الحركة
    next_key = window.getch()
    #تحديد المفتاح التالي
    key = key if next_key == -1 else next_key
    #هل الرأس وصل الى الحافة او الى جسم الحية
    if hanter[0][0] in [0, scren_hight] or hanter[0][1] in [0, scren_width] or hanter[0] in hanter[1:]:

        #إنهاء الشاشة
        curses.endwin()
        quit()
    while True:
        alfark_x=abs(hanter[0][1] - enemy[0][1])
        alfark_y = abs (hanter[0][0] - enemy[0][0])
        if alfark_x < 5 and alfark_y <5 :
                # move enemy one step toward the hanter when close
                if enemy[0][1] < hanter[0][1]:
                    enemy[0][1] += 1
                elif enemy[0][1] > hanter[0][1]:
                    enemy[0][1] -= 1
                if enemy[0][0] < hanter[0][0]:
                    enemy[0][0] += 1
                elif enemy[0][0] > hanter[0][0]:
                    enemy[0][0] -= 1
        new_hanter = [hanter[0][0], hanter[0][1]]
        if key == curses.KEY_UP :
             new_hanter[0] -= 1
        if key == curses.KEY_DOWN : 
             new_hanter[0] += 1
        if key == curses.KEY_RIGHT : 
             new_hanter[1] += 1 
        if key == curses.KEY_LEFT :
             new_hanter[1] -= 1
