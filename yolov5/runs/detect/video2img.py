import cv2
import os

def extract_frames(video_path, output_dir, interval_seconds):
    """
    从视频中按时间间隔提取图片并保存到指定文件夹。

    Args:
        video_path (str): 视频文件路径。
        output_dir (str): 图片保存的文件夹路径。
        interval_seconds (float): 图片提取的时间间隔，单位为秒。
    """

    # 创建输出文件夹
    os.makedirs(output_dir, exist_ok=True)

    # 打开视频文件
    cap = cv2.VideoCapture(video_path)

    # 获取视频帧率
    fps = cap.get(cv2.CAP_PROP_FPS)

    # 获取视频总帧数
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # 计算图片提取的帧数间隔
    frame_interval = int(fps * interval_seconds)

    # 计数器
    frame_count = 0

    # 循环读取视频帧
    sum = 0
    while True:
        # 读取一帧
        ret, frame = cap.read()

        # 如果读取失败，退出循环
        if not ret:
            break

        # 判断是否需要提取图片
        if frame_count % frame_interval == 0:
            # 保存图片
            cv2.imwrite(os.path.join(output_dir, f"frame_{frame_count}.jpg"), frame)

            sum += 1
            print(sum)

        # 计数器加1
        frame_count += 1
        # print(frame_count)

    # 释放视频文件
    cap.release()
    # print(sum)

# 示例用法
video_path = "/home/camsense/yao/Data/DATA/data8/out2.mp4"  # 替换为你的视频文件路径
output_dir = "/home/camsense/yao/Data/DATA/data8/out2/"  # 替换为你的输出文件夹路径
interval_seconds = 0.2 # 替换为你的时间间隔，单位为秒

extract_frames(video_path, output_dir, interval_seconds)
