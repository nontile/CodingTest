# 주어진 문자열(공백 없이 쉼표로 구분되어 있음)을 가지고 아래 문제에 대한 프로그램을 작성하세요.
# 이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌

str_name = "유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌"
names = str_name.split(",")

# 1.김씨와 이씨는 각각 몇 명 인가요?
kim = len([name for name in names if name.startswith("김")])
lee = len([name for name in names if name.startswith("이")])
print(f"김씨는 {kim} 명이고 이씨는 {lee} 명 입니다.")


# 2."이재영"이란 이름이 몇 번 반복되나요?
ljy = len([name for name in names if name == "이재영"])    
print(f"이재영이란 이름은 {ljy} 번 반복 됩니다.")


# 3.중복을 제거한 이름을 출력하세요.
print(set(names))


# 4.중복을 제거한 이름을 오름차순으로 정렬하여 출력하세요.
print(sorted(set(names)))