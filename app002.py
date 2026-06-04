import cv2
'''
# OpenCV 모듈 가져오기

# 버전 확인
print(cv2.__version__)   # 4.13.0

## 이미지 불러와서 출력하기 - (https://www.pexels.com/ko-kr/)
cityImg = cv2.imread('./res/img/city.jpg')       # 이미지 읽기
print(f'cityImg shape: {cityImg.shape}')         # 이미지 크기  --> (4096, 3276, 3(BGR))
cityImg = cv2.resize(cityImg, (800, 600))        # 이미지 크기 변경 --> (가로, 세로), 3))

cv2.imshow('title-cityImg', cityImg)             # 이미지 출력
cv2.waitKey(0)                                   # 어떤 키를 누룰때까지 기다려라 
cv2.destroyAllWindows()                          # 모든 창 닫기
'''

## 읽기 옵션
# cityImgColor = cv2.imread('./res/img/city.jpg', cv2.IMREAD_COLOR)       # BGR 유지
# cityImgColor = cv2.resize(cityImgColor, (800, 600))

# cityImgGray = cv2.imread('./res/img/city.jpg', cv2.IMREAD_GRAYSCALE)    # GRAYSCALE
# cityImgGray = cv2.resize(cityImgGray, (800, 600))

# cityImgUnchanged = cv2.imread('./res/img/city.jpg', cv2.IMREAD_UNCHANGED) # ALPHA 유지
# cityImgUnchanged = cv2.resize(cityImgUnchanged, (800, 600))

# cv2.imshow('title-cityImgColor', cityImgColor)
# cv2.imshow('title-cityImgGray', cityImgGray)
# cv2.imshow('title-cityImgUnchanged', cityImgUnchanged)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

## 동영상 불러와서 출력하기 - (https://www.pexels.com/ko-kr/)
# OpenCV에서 동영상을 불러온다는 것은 '동영상 -> 프레임(frame) 추출 -> 이미지화 -> 출력'

cityMov = cv2.VideoCapture('./res/mov/city.mp4')
while cityMov.isOpened():  # 동영상 파일이 연결되어 있다면...
    result, frame = cityMov.read()     # result: read 성공 여부, frame: 받아온 이미지(프레임)
    if not result:
        print('END FRAME')
        break

    # 사이즈 조정
    frame = cv2.resize(frame, (800, 600))

    print(f'frame: {frame}')
    cv2.imshow('title-cityFrame', frame)      # 매우 빠르게 frame(이미지)가 출력 된다.

    if cv2.waitKey(1) == ord('q'):  # 1ms 동안 기다린다. 사용자가 'q'를 입력하면 중단한다.
        break

cityMov.release()        # 외부 자원 해제
cv2.destroyAllWindows()  # 윈도우 창 닫기


'''
# 캠에서 동영상 실시간으로 불러오기
cityMov = cv2.VideoCapture(0)
while cityMov.isOpened():  # 동영상 파일이 연결되어 있다면...
    result, frame = cityMov.read()     # result: read 성공 여부, frame: 받아온 이미지(프레임)
    if not result:
        print('END FRAME')
        break

    # 사이즈 조정
    frame = cv2.resize(frame, (800, 600))

    print(f'frame: {frame}')
    cv2.imshow('title-cityFrame', frame)      # 매우 빠르게 frame(이미지)가 출력 된다.

    if cv2.waitKey(1) == ord('q'):  # 1ms 동안 기다린다. 사용자가 'q'를 입력하면 중단한다.
        break

cityMov.release()        # 외부 자원 해제
cv2.destroyAllWindows()  # 윈도우 창 닫기
'''