import cv2
import subprocess
import os
from datetime import datetime, timedelta
# get the current datetime
now = datetime.now()
url = "https://svs.itworkscdn.net/rudawlive/rudawlive.smil/rudawtv_chunks.m3u8"  # replace with your URL
duration = 10  # recording duration in seconds
# create output file name based on current datetime and recording duration
start_time_str = now.strftime("%d %B %Y %H.%M.%S")
end_time = now + timedelta(seconds=duration)
end_time_str = end_time.strftime("%H.%M.%S")
output_file = f"output_{start_time_str}_to_{end_time_str}.mp4"
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


# Commit 
