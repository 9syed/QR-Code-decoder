import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

def decode(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    barcodes = pyzbar.decode(gray)

    for barcode in barcodes:
        barcode_data = barcode.data.decode("utf-8")
        print("QR Code data: ", barcode_data)

        points = barcode.polygon
        if len(points) == 4:
            pts = np.array([(pt.x, pt.y) for pt in points], dtype=int)
            cv2.polylines(frame, [pts], isClosed=True, color=(0, 255, 0), thickness=3)
    
    return frame

def main():
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        result_frame = decode(frame)
        cv2.imshow("QR Code Scanner", result_frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()