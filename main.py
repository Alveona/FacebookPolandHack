from video_converter import video_to_audio
from parse_audio_to_text import extract_text
from extract_cartoons_from_video import get_images_from_given_seconds

def make_cartoons_from_video(video_name):  
    video_to_audio(video_name)
    track_name = video_name.split('.')[0]
    print(track_name)
    answer = extract_text(track_name + '.wav')
    timelist = []
    print(answer)
    for e in answer:
        timelist.append((int(e[1]) + int(e[2]))/2)
    #print(timelist)
    get_images_from_given_seconds(video_name, timelist, "./rubbish/")
	
make_cartoons_from_video('IMG_3844.MOV')