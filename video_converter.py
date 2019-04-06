import os
import pipes
def video_to_audio(fileName):
    try:
        print("convertion started")
        file, file_extension = os.path.splitext(fileName)
        file = pipes.quote(file)
        video_to_wav = 'ffmpeg -i ' + file + file_extension + ' -ac 1 ' + file + '.wav'
        final_audio = 'lame '+ file + '.wav' + ' ' + file + '.mp3'
        os.system(video_to_wav)
        os.system(final_audio)
        #file=pipes.quote(file)
        #os.remove(file + '.wav')
        print("sucessfully converted ", fileName, " into audio!")
    except OSError as err:
        print(err.reason)
        exit(1)