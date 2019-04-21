import cv2
import time
import os
import move
import sys
def cam_start(path, wxid):
    # 定义摄像头对象，其参数0表示第一个摄像头
    camera = cv2.VideoCapture(0)
    # 判断视频是否打开
    if (camera.isOpened()):
        print('Open')
    else:
        print('摄像头未打开')
        camera.release()
        #destroyAllWindows()关闭所有图像窗口
        cv2.destroyAllWindows()
        sys.exit(0)
 
    # 测试用,查看视频size
    size = (int(camera.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    print('size:'+repr(size))

    # //move.move_det(camera, path, wxid)
    # release()释放摄像头
    camera.release()
    #destroyAllWindows()关闭所有图像窗口
    cv2.destroyAllWindows()
cam_start('s', '12')