import hashlib

input_data = input()
encoded_data = input_data.encode()  # 문자열의 바이트 객체를 만들어 줍니다. 
result = hashlib.sha256(encoded_data).hexdigest() # 해시 결과 문자열이 반환이 됩니다. 
print(result)

