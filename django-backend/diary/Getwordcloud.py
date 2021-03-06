
import numpy as np
import random   # numpy와 random, palettable은 font 색 설정
from PIL import Image   # mask 이미지를 처리
from wordcloud import WordCloud, STOPWORDS  # wordcloud는 이 모든 것을 이용해서 word cloud를 그릴 때 이용
from palettable.cartocolors.sequential import BluGrn_7
import NLP
# https://jiffyclub.github.io/palettable/
# from palettable.colorbrewer.qualitative import Dark2_8 # random color

def color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return tuple(BluGrn_7.colors[random.randint(0,6)])
    # return tuple(Dark2_8.colors[random.randint(0,7)])


def Get_wordcloud(sentence):
    pre_sent = NLP.Preprocessing(sentence)         # 전처리
    freq_list = NLP.frequent_list(pre_sent, 500)   # 빈도 수 높은 단어 추출


    font = "BMHANNA_11yrs_ttf"
    font_path = "%s.ttf" % font

    # https://pixlr.com/kr/editor/ - Translate Transparent(alpha) Image
    # https://dramahdg.tistory.com/1 - Search Transparent(alpha) Image
    icon = "Tree"
    icon_path = "%s.png" % icon

    # 불용어 제거
    stopwords = []
    with open("./StopWord.txt", 'rt', encoding='UTF8') as f:
        while True:
            line = f.readline().rstrip('n')
            if not line: break
            stopwords.append(line)

    icon = Image.open(icon_path)
    mask = Image.new("RGB", icon.size, (255, 255, 255))  # backgraound: white(255,255,255)
    mask.paste(icon, icon)
    mask = np.array(mask)

    # wordcloud 생성
    wc = WordCloud(font_path=font_path, background_color="rgba(255, 255, 255, 0)", mode="RGBA", max_words=2000,
                   mask=mask,
                   max_font_size=250, random_state=42, stopwords=stopwords)
    #wc.generate_from_text(message) # 문자열로 생성
    wc.generate_from_frequencies(dict(freq_list))
    wc.recolor(color_func=color_func, random_state=3)
    wc.to_file("static/WordCloud_Tree.png")    # 이미지 저장




if __name__ == '__main__':
    #sent = "작년 크리스마스 선물로 받은 컨버스 척테일러 후기를 이제서야 남긴다..! 계속 블로그에 글 써야지 했는데 이제 쓰게 됐습니다 후기를 남길려면 최소 2개월정도 사용해 본 후에 써야하지 않겠습니까!! 지금 바로 후기 쓰도록 할게욧 저는 카카오톡 컨버스 스토어에서 구입했습니다! 왜냐면 7000원 정도? 할인하고 있었기 때문입니다 원가는 79,000원 입니다 ㅎㅎ컨버스 척테일러 1970s 블랙으로 구입 :) ++ 아직도 세일 중인가 싶어서 카카오톡 스토어 들어가봤는데 세일중입니다! 이왕 사는거 세일해서 더 저렴하게 사면 기분 좋겠죠 원래 발 사이즈가 240이기 때문에 그냥 240으로 샀어요! + 저는 발볼이 넓은 편인데, 240으로 사니까 발볼은 맞는데 뒷꿈치가 조금 헐렁거렸어요 ㅠㅠ 그래도 스니커즈는 조금 크게 신어야 하니까! ++ 발볼 좁으신 분들은 5 사이즈 정도 작게 하시는게 좋을 것 같아요! 엄마가 신발 보고는 왜이렇게 싼티(...) 나냐고 뭐라고 하셨습니다 ㅠㅠ아마 흰 부분이 고무 재질인것 같은데 반짝반짝 빛나서 그런 것 같아요 그래도 영롱한거 보면... 왜 국민신발인지 알겠구요 아마 사진 수십개는 찍은 것 같아요!! ㅋㅋ 사실 컨버스 올스타 랑 1970s 둘 중에 뭘 살까.. 고민을 하고있었는데 1970s 이 더 예쁜 것 같아요 (물론 조금 더 비싸지만...) 참고로 제가 고민했다던 두 상품! 왼쪽 제품은 정확한 상품명을 모르겠네요 암튼 왼쪽은 앞코 (흰색) 부분이 더 넓었던 것 같아요 약간... 슈펜 스니커즈 느낌?! (작년 여름에 포스팅 했던!) 아하하 슈펜 컨버스 (....) 를 샀는데 후기를 남겨보도록 하겠습니다 일단 신었을때는 되게 예뻤슴니다 발 ... 착용감은 일단 제 기준으로 반스보다는 훨씬 불편한 것 같아요,, 왜냐면 신발이 무거워서 다닐때도 약간 불편한 감이 조금 있는데 그래도 아예 막 못신고 다니겠다-- 이정도는 아니구요! 근데 전 앞에서 말했듯이 발볼이 넓은편이라서 발볼쪽이 처음에 아팠고 ㅠㅠ그냥 신고 다닐때는 뒷꿈치가 들리는 참사가 발생했습니다.... 무슨일인지 지금은 또 괜찮아요 반스>>>>>> 컨버스 이정도로 봐주시면 되겠습니다 하핫 기본템이라서 옷을 아무렇게나 입어도 잘어울리고 좋아요 특히 전 아직 학생이기 때문에 교복을 주로 입는데 교복에도 잘 어울리고 넵! 전체 점수를 매긴다면 전 별 세개 반..? 정도! 이걸 끝으로 후기를 마치도록 하겠습니당! 뭐 주관적인 후기니까 구매에 참고가 되었으면 좋겠네요 크하하 핫"

    # 텍스트를 파일로 읽어올 경우
    with open("diary1.txt", encoding='UTF-8') as f:
        sent = f.read()
        f.close()
    with open("diary2.txt", encoding='UTF-8') as f:
        sent += f.read()
        f.close()

    Get_wordcloud(sent)

