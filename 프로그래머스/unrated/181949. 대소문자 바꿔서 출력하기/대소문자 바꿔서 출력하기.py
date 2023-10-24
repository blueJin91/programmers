# 문자열 입력 받기
str = input()

# 대소문자 변환 후 출력
result = ""
for char in str:
    if char.isupper():
        result += char.lower()
    elif char.islower():
        result += char.upper()
    else:
        result += char  # 다른 문자(공백, 기호 등)는 그대로 유지

print(result)