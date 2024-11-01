# 파일에 내용 추가
def create_file(filename):
    with open(filename, "a", encoding="utf8") as file:
        while True:
            data = input("내용을 입력하시오: ")
            file.write("%s\n" % data)

            answer = input("내용을 추가하시겠습니까? 네 또는 아니요를 입력하십시오: ")
            if answer.lower() != "네":
                break

# 파일 내용 표시
def display_file(filename):
    with open(filename, "r", encoding="utf8") as file:
        lines = file.readlines()
        print("\n현재 파일 내용:")
        for index, line in enumerate(lines, start=1):
            print(f"{index}: {line.strip()}")
    return lines

# 파일 특정 줄 수정
def edit_line(filename, line_number, new_content):
    lines = display_file(filename)
    if 1 <= line_number <= len(lines):
        lines[line_number - 1] = new_content + '\n'
        with open(filename, "w", encoding="utf8") as file:
            file.writelines(lines)
        print(f"{line_number}번째 줄이 수정되었습니다.")
    else:
        print("해당 줄 번호가 유효하지 않습니다.")

# 파일 특정 줄 삭제
def delete_line(filename, line_number):
    lines = display_file(filename)
    if 1 <= line_number <= len(lines):
        del lines[line_number - 1]
        with open(filename, "w", encoding="utf8") as file:
            file.writelines(lines)
        print(f"{line_number}번째 줄이 삭제되었습니다.")
    else:
        print("해당 줄 번호가 유효하지 않습니다.")
        
def file_edi_del (filename):
    choice = input("\n수정하려면 '수정', 삭제하려면 '삭제', 종료하려면 '종료'를 입력하십시오: ").strip()
    if choice == "수정":
        line_number = int(input("수정할 줄 번호를 입력하세요: "))
        new_content = input("새로운 내용을 입력하세요: ")
        edit_line(filename, line_number, new_content)
    elif choice == "삭제":
        line_number = int(input("삭제할 줄 번호를 입력하세요: "))
        delete_line(filename, line_number)
    elif choice == "종료":
        print("프로그램을 종료합니다.")
    else:
        print("올바른 명령어를 입력해 주세요.")

# 프로그램 실행
while True:
    select = input(
        '''[기능]
        1. 파일 생성
        2. 파일 수정 및 삭제
        3. 파일 내용 확인
        4. 종료
        원하는 기능의 번호를 입력하시오: ''')
    filename = input("파일 이름을 입력해 주십시오: ")
    if select == "1":
        create_file(filename)
        display_file(filename)
    elif select == "2":
        display_file(filename)
        file_edi_del(filename)
    elif select == "3":
        display_file(filename)
    else:
        break