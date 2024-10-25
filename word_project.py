from graphics import *

# 파일에서 단어 데이터 읽기
with open('word.txt', encoding='utf-8') as file:
    words_str = file.read()
words_list = words_str.split()

# 중복 없는 단어 리스트와 빈도 계산
unique_words = list(set(words_list))
word_counts = {word: words_list.count(word) for word in unique_words}

# 단어 수에 따라 그래프 창 크기 및 막대 간격 설정
num_words = len(unique_words)
win_width = max(400, num_words * 50)  # 최소 폭 400, 단어 수에 따라 크기 조정
win_height = 400

win = GraphWin('단어 차트', win_width, win_height)
win.setCoords(0, 0, num_words * 50, 100)  # 좌표 설정

win.setBackground('white')

# 최대 빈도수 계산
max_count = max(word_counts.values())

# 막대 너비 및 간격 설정
bar_width = max(30, 40 - num_words)  # 단어 수에 따라 막대 너비 감소
gap = bar_width / 2  # 막대 사이의 간격

for i, (word, count) in enumerate(word_counts.items()):
    bar_height = count * (80 / max_count)  # 높이는 최대 빈도에 따라 정규화

    # 바 그리기
    x_start = i * (bar_width + gap) + gap
    rect = Rectangle(Point(x_start, 10), Point(x_start + bar_width, 10 + bar_height))
    rect.setFill("green")
    rect.draw(win)

    # 바 위에 개수(count) 텍스트 표시하기
    count_label = Text(Point(x_start + bar_width / 2, 10 + bar_height + 5), str(count))
    count_label.setSize(8)
    count_label.draw(win)

    # 단어 레이블 표시
    label = Text(Point(x_start + bar_width / 2, 5), word)
    label.setSize(7)
    label.draw(win)

win.getMouse()  # 마우스 클릭 대기
win.close()  # 창 닫기

