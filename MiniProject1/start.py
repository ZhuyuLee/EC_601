import sys
import twicture
import pic2video
import analyse_video

twicture.get_pics_urls(sys.argv[1])
twicture.download_pics()

pic2video.convert()

analyse_video.analyse()

