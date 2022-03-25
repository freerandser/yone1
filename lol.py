
import random

top = ['가렌', '갱플랭크', '그웬', '나르', '나서스', '다리우스', '럼블', '레넥톤', '렝가', '리븐', '마오카이', '말파이트',
       '모데카이저', '문도박사', '사이온', '세트', '쉔', '신지드', '아칼리', '아트록스', '오공', '오른', '요릭', '우르곳',
       '이렐리아', '일라오이', '요네', '잭스', '제이스', '초가스', '카밀', '트린다미어', '티모', '피오라', '하이머딩거']
jungle = ['그라가스', '그레이브즈', '녹턴', '누누', '니달리', '다이애나', '람머스', '렉사이', '리신', '릴리아', '마스터이',
          '바이', '샤코', '쉬바나', '신짜오', '아무무', '아이번', '엘리스', '올라프', '우디르', '워윅', '이블린', '자르반4세',
          '자크', '카서스', '카직스', '케인', '킨드레드', '탈리아', '피들스틱', '헤카림', '트런들']
mid = ['갈리오', '니코', '라이즈', '르블랑', '리산드라', '말자하', '베이가', '벡스', '벨코즈', '블라디미르', '빅토르', '사일러스',
       '신드라', '아리', '아지르', '아크샨', '애니', '애니비아', '야스오', '조이', '오리아나', '제라스', '제드', '직스', '카사딘',
       '카타리나', '코르키', '트위스티드 페이트', '피즈', '카시오페아']
ad = ['제리', '사미라', '징크스', '루시안', '진', '베인', '이즈리얼', '카이사', '자야', '트위치', '케이틀린', '드레이븐',
      '트리스타나', '아펠리오스', '시비르', '코그모', '칼리스타', '바루스', '세나']
sup = ['블리츠크랭크', '노틸러스', '레오나', '카르마', '레나타 글라스크', '룰루', '파이크', '알리스타', '렐', '모르가나',
       '럭스', '쓰레쉬', '질리언', '소라카', '나미', '자이라', '잔나', '라칸', '브라움', '바드', '스웨인', '타릭']


def getresult(text):
    words = text.split()

    result = {"● 탑": '', "● 정글": '', "● 미드": '', "● 원딜": '', "● 서폿": ''}

    for word in words:
        if word == "1팀":
            index = random.randrange(0, len(top))
            result["탑"] = top[index]
            index = random.randrange(0, len(jungle))
            result["정글"] = jungle[index]
            index = random.randrange(0, len(mid))
            result["미드"] = mid[index]
            index = random.randrange(0, len(ad))
            result["원딜"] = ad[index]
            index = random.randrange(0, len(sup))
            result["서폿"] = sup[index]
        elif word == "2팀":
            index = random.randrange(0, len(top))
            result["탑"] = top[index]
            index = random.randrange(0, len(jungle))
            result["정글"] = jungle[index]
            index = random.randrange(0, len(mid))
            result["미드"] = mid[index]
            index = random.randrange(0, len(ad))
            result["원딜"] = ad[index]
            index = random.randrange(0, len(sup))
            result["서폿"] = sup[index]

        return result