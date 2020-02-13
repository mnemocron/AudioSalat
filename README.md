# AudioSalat

<img src="logo.png" width="128px"></img>  

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

Tool that synchronizes the audio tracks of two video files of the same movie with different language audio.

---

### Usage

```bash
audio-salat --video-src "./GitS-SAC-S01E01-eng.mkv" --audio-src "./GitS-SAC-S01E01-ger.mp4" -o "GitS-SAC-S01E01-eng-ger.mkv"

[processing] ./GitS-SAC-S01E01-eng.mkv ...
[processing] ./GitS-SAC-S01E01-ger.mp4 ...
[processing] cross correlating video streams...
[success] found time delay of t=3.456s
[processing] encoding new file "GitS-SAC-S01E01-eng-ger.mkv" ...
[ffmpeg] ffmpeg some-comand -magic -t=3.456s
[success] done!
```


---

### Sources

- [map-time-difference-between-two-similar-videos](https://dsp.stackexchange.com/questions/18846/map-time-difference-between-two-similar-videos)


---

#### Attribution

Logo by [freepik](https://www.flaticon.com/authors/freepik)
