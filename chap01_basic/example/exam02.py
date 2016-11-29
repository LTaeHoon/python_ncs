'''
step3, step4 수업후 문제 

문2) 지방(fat), 탄수화물(carbohydrate), 단백질(protein)            
      칼로리의 합계를 계산하는 프로그램을 작성하시오.
      조건1> 지방, 탄수화물, 단백질의 그램을 키보드로 입력받음 
      조건2> dict 자료구조 형식으로 3개의 데이터 저장 
      조건3> dict에 저장된 3개 데이터 이용 총 칼로리 계산
                총 칼로리 = 지방 * 9 + 단백질 * 4 + 탄수화물 * 4 
      조건4> 지방, 탄수화문, 단백질 데이터 입력 오류 예외 처리              

   <<화면출력 결과>>
  지방의 그램을 입력하세요 : 25
  탄수화물의 그램을 입력하세요 : 520
  단백질의 그램을 입력하세요 : 45
  총칼로리 : 2,485 cal
'''

import locale # 다국어 처리 모듈
locale.setlocale(locale.LC_ALL,locale='') #다국어 설정
print(locale.getlocale()) #('Korean_Korea', '949') #다국어 확인

try: 
    fat = float(input('지방의 그램을 입력하세요:'))
    carbohydrate = float(input('탄수화물의 그램을 입력하세요:'))
    protein = float(input('단백질의 그램을 입력하세요:'))
    
    data = {'fat':fat,'carbohydrate':carbohydrate,'protein':protein}
    tot = data['fat']*9 + data['carbohydrate']*4 +data['protein']*4

    ftot = locale.format('%d',tot,True)
    print('총칼로리 :{} cal'.format(ftot))
except Exception as e:
    print('오류정보:',e)
finally:
    print('프로그램 종료')


    








