# Archipelago Musoc Video

This project is for creating a music video using by editing AI generated images.

## FFmpeg commands

### 1. Create video from images
```
ffmpeg -r 30 -i frame-dir/%03d.png -pix_fmt yuv420p video-name.mp4
```
### 2. Extract frames from video
```
ffmpeg -i video.mp4 frames/video-%03d.jpg
```