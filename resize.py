#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cv2 import (
    CAP_PROP_FPS,
    CAP_PROP_FRAME_COUNT,
    CAP_PROP_FRAME_HEIGHT,
    CAP_PROP_FRAME_WIDTH,
    VideoCapture,
    VideoWriter,
    VideoWriter_fourcc,
    imshow,
    waitKey,
)
from video import video

_F = 0  # frame counter
show_video = True

cap = VideoCapture(f"{video.path_o}{video.name}.{video.format}")  # Open video
fps, frames = cap.get(CAP_PROP_FPS), cap.get(CAP_PROP_FRAME_COUNT)

# Aspect ratio of original video
w_frame = int(cap.get(CAP_PROP_FRAME_WIDTH))
h_frame = int(cap.get(CAP_PROP_FRAME_HEIGHT))

new_width, new_height = 520, 1080  # for vertical video

x, y = int(w_frame / 2), int(h_frame / 2)  # Center of new cropped video

# output
fourcc = VideoWriter_fourcc(*"XVID")
out = VideoWriter(
    f"{video.path_c}c_{video.name}.{video.format}", fourcc, fps, (new_height, new_width)
)

while cap.isOpened():
    ret, frame = cap.read()
    _F += 1  # Counting frames

    # Avoid problems when video finish
    if ret:
        crop_frame = frame[y : y + h_frame, x : x + new_width]

        if video.show_progress:
            print(f"{int(_F * 100 / frames)} %")  # frames cropped

        out.write(crop_frame)  # Save video

        if show_video:
            imshow("frame", frame)
            imshow("cropped", crop_frame)

        if waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
out.release()
