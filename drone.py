from djitellopy import Tello
import cv2
import time

width = 320  # WIDTH OF THE IMAGE
height = 240  # HEIGHT OF THE IMAGE
startCounter =0   #  0 FOR FIGHT 1 FOR TESTING

tello = Tello()

tello.connect()

tello.for_back_velocity = 0
tello.left_right_velocity = 0
tello.up_down_velocity = 0
tello.yaw_velocity = 0
tello.speed = 0


tello.streamoff()
tello.streamon()


while True:

    # GET THE IMGAE FROM TELLO
    frame_read = tello.get_frame_read()
    myFrame = frame_read.frame
    img = cv2.resize(myFrame, (width, height))

    # TO GO UP IN THE BEGINNING
    if startCounter == 0:
        tello.takeoff()
        time.sleep(8)
        tello.rotate_clockwise(90)
        time.sleep(3)
        tello.move_left(35)
        time.sleep(3)
        tello.land()
        startCounter = 1

    # # SEND VELOCITY VALUES TO TELLO
    # if me.send_rc_control:
    #     me.send_rc_control(me.left_right_velocity, me.for_back_velocity, me.up_down_velocity, me.yaw_velocity)

    # DISPLAY IMAGE
    cv2.imshow("MyResult", img)

    # WAIT FOR THE 'Q' BUTTON TO STOP
    if cv2.waitKey(1) & 0xFF == ord('q'):
        tello.land()
        break