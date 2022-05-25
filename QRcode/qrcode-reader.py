from pyzbar.pyzbar import decode
import cv2



cap = cv2.VideoCapture(0)

while True:

    _, frame = cap.read()

    decode_data= decode(frame)
    try:
        print(decode_data[0][0])
        for qrcode in decode_data:
            x, y, w, h = qrcode.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    except:
        pass



    cv2.imshow("QRcode scanner", frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
