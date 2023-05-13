import cv2
import subprocess
import os
from datetime import datetime, timedelta
import schedule
import time

def record_video():
    # get the current datetime
    now = datetime.now()
    url = "https://svs.itworkscdn.net/rudawlive/rudawlive.smil/rudawtv_chunks.m3u8"  # replace with your URL
    duration = 30  # recording duration in seconds
    # create output file name based on current datetime and recording duration
    start_time_str = now.strftime("%d %B %Y %H.%M.%S")
    end_time = now + timedelta(seconds=duration)
    end_time_str = end_time.strftime("%H.%M.%S")
    output_file = f"rudaw_{start_time_str}_to_{end_time_str}.mp4"
    # set up capture from URL
    cap = cv2.VideoCapture(url)
    # get the video dimensions
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # set up FFmpeg command to record for a specific duration
    ffmpeg_cmd = [
        "C:/ffmpeg/bin/ffmpeg.exe",
        "-y",
        "-t", str(duration),
        "-f", "hls",
        "-i", url,
        "-c", "copy",
        output_file
    ]
    # start the FFmpeg process to record the video
    subprocess.call(ffmpeg_cmd)
    # release the video capture
    cap.release()

# schedule the recording to run every day at 7:45 pm
schedule.every().day.at("17:46").do(record_video)

while True:
    # run the scheduled tasks
    schedule.run_pending()
    # wait for 1 second before checking again
    time.sleep(1)

import  schedule    
import  time    
# get the current datetime
def record_video():
    now = datetime.now()
    url = "https://svs.itworkscdn.net/rudawlive/rudawlive.smil/rudawtv_chunks.m3u8"  # replace with your URL
    duration = 30  # recording duration in seconds
    # create output file name based on current datetime and recording duration
    start_time_str = now.strftime("%d %B %Y %H.%M.%S")
    end_time = now + timedelta(seconds=duration)
    end_time_str = end_time.strftime("%H.%M.%S")
    output_file = f"rudaw_{start_time_str}_to_{end_time_str}.mp4"
    # set up capture from URL
    cap = cv2.VideoCapture(url)
    # get the video dimensions
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # set up FFmpeg command to record for a specific duration
    ffmpeg_cmd = [
        "C:/ffmpeg/bin/ffmpeg.exe",
        "-y",
        "-t", str(duration),
        "-f", "hls",
        "-i", url,
        "-c", "copy",
        output_file
    ]
    # start the FFmpeg process to record the video
    subprocess.call(ffmpeg_cmd)
    # release the video capture
    cap.release()

#now we schedule it using the schedule library 
schedule.every().day.at("11:08").do(record_video)

while   True:
    schedule.run_pending()
    time.sleep(1)

