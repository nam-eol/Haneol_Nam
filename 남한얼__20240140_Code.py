## 전역 변수 선언 부분 ##
swidth, sheight = 1000, 600
inStr=''

## 함수 불러오기 ##
from tkinter.simpledialog import *

from information import 북마케도니아 as A
from information import 남아프리카_공화국 as B
from information import 튀니지 as C
from information import 우즈베키스탄 as D
from information import 앤티가_바부다 as E
from information import 조선민주주의_인민공화국 as F
from information import 이스라엘 as G
from information import 영국 as H
from information import 세인트_빈센트_그레나딘 as I
from information import 대한민국 as J

from flag import draw_북마케도니아 as a
from flag import draw_남아프리카공화국 as b
from flag import draw_튀니지 as c
from flag import draw_우즈베키스탄 as d
from flag import draw_앤티가바부다 as e
from flag import draw_조선민주주의인민공화국 as f
from flag import draw_이스라엘 as g
from flag import draw_영국 as h
from flag import draw_세인트빈센트그레나딘 as i
from flag import draw_대한민국 as j
from flag import draw_로고 as k

## 터틀 창 설정 ##
import turtle as t

t.title('파이썬 국기 그리기')
t.shape('turtle')
t.setup(width = swidth + 100, height = sheight + 100)
t.screensize(swidth, sheight)

## 메인 코드 부분 ##
while True :
    print('')
    print("나라 이름 또는 번호를 입력해주세요.")
    print('')
    print("제작 정보를 알고 싶으면 '13.정보 더보기'를 선택하세요.")
    print('')
    
    select = input("어떤 나라의 국기를 그리시겠습니까? (1.북마케도니아 2.남아프리카 공화국 3.튀니지 4.우즈베키스탄 5.앤티가 바부다 6.조선민주주의 인민공화국 7.이스라엘 8.영국 9.세인트빈센트 그레나딘 10.대한민국 11.나만의 로고 12.모든 국기 그리기 13.정보 더보기 14.그만 그리기) : ")

    if select == "1" or select == "북마케도니아" :
        a()
    elif select == "2" or select == "남아프리카 공화국" :
        b()
    elif select == "3" or select == "튀니지" :
        c()
    elif select == "4" or select == "우즈베키스탄" :
        d()
    elif select == "5" or select == "앤티가 바부다" :
        e()
    elif select == "6" or select == "조선민주주의 인민공화국" :
        f()
    elif select == "7" or select == "이스라엘" :
        g()
    elif select == "8" or select == "영국" :
        h()
    elif select == "9" or select == "세인트빈센트 그레나딘" :
        i()
    elif select == "10" or select =="대한민국" :
        j()
    elif select == "11" or select == "나만의 로고" :
        k()
    elif select == "12" or select == "모든 국기 그리기" :
        a(), b(), c(), d(), e(), f(), g(), h(), i(), j(), k()
    elif select == "13" or select == "정보 더보기" :
        inStr = askstring('국기 정보 더보기', '정보가 알고 싶은 국기')
        if inStr == "북마케도니아":
            A()
        elif inStr == "남아프리카 공화국":
            B()
        elif inStr == "튀니지":
            C()
        elif inStr == "우즈베키스탄":
            D()
        elif inStr == "앤티가 바부다":
            E()
        elif inStr == "조선민주주의 인민공화국":
            F()
        elif inStr == "이스라엘":
            G()
        elif inStr == "영국":
            H()
        elif inStr == "세인트빈센트 그레나딘":
            I()
        elif inStr == "대한민국":
            J()
        else:
            print("해당 국기가 없습니다. 다시 입력해주세요.")
    elif select == "14" or select == "그만 그리기" :
        break
    else:
        print("해당 국기가 없습니다. 다시 입력해주세요.")

