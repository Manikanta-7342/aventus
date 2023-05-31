import cv2
from collections import Counter
# from html2text import html2text

# Function to get the most common element in the list
def most_common_element(lst):
    counter = Counter(lst)
    most_common = counter.most_common(1)
    return most_common[0][0] if most_common else None

# Function to scan QR codes in the frame
def scan_qrcodes(frame):
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Create a QRCodeDetector object
    qr_detector = cv2.QRCodeDetector()

    # Detect and decode QR codes
    retval, decoded_info, points, straight_qrcode = qr_detector.detectAndDecodeMulti(gray)

    # Loop over the decoded information
    if retval:
        p=points[0]
            # Draw a rectangle around the QR code
        x, w = p[0], p[2]
        cv2.rectangle(frame, (int(x[0]), int(x[1])), (int(w[0]), int(w[1])), (0, 255, 0), 2)

        # Extract the QR code data as a string
        qr_data = decoded_info

        # Draw the QR code data on the image
        text = f"{qr_data}"
        cv2.putText(frame, text, (int(w[0]), int(w[1]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Print the QR code data to the console
        t=qr_data
        final_value=t[0]
        if final_value!='':
            return str(final_value)
        else:
            return None
            # print("QR Code Data:", qr_data)

def open_camera():
    # Open the camera
    cap = cv2.VideoCapture(0)

    # Check if the camera was successfully opened
    if not cap.isOpened():
        print("Failed to open camera.")
        exit()

    data = []

    # Loop over frames from the camera
    while True:
        # Read a frame from the camera
        ret, frame = cap.read()

        # Check if a frame was successfully read
        if not ret:
            print("Failed to capture frame.")
            break

        # Scan for QR codes in the frame
        item = scan_qrcodes(frame)
        
        if item is None:
            # Display the frame with detected QR codes
            cv2.imshow("QR Code Scanner", frame)

        else:
            cv2.imshow("QR Code Scanner", frame)
            data.append(item)
            # Display the frame with detected QR codes

        # Wait for the 'q' key to exit or when 10 QR codes are detected
        if cv2.waitKey(1) & 0xFF == ord('q') or len(data) >= 10:
            break

    # Release the camera and close the OpenCV window
    cap.release()
    cv2.destroyAllWindows()

    most_common = most_common_element(data)
    return most_common

# Call the function to start scanning QR codes from the camera
# print(open_camera())
def main_value_small():
    temp=open_camera()
    ans=temp.split('=')[1].strip()
    return (ans)
# print(main_value_small())
# print(ans[-9:])
