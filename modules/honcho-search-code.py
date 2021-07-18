import pandas as pd
from yt_stats import YTstats
from tqdm import tqdm

API_KEY = 'AIzaSyAVY1UNekoQN1gpQIx0Jvce2LBRl5JrqQI'

df = pd.read_excel("..\csv\youtube_video_channel_ID.xlsx")
Views =[]

for x,y in tqdm(zip(df["Video ID"],df["Channel ID"])):
    channel_id = y
    video_id = x
    part = 'statistics'
    yt = YTstats(API_KEY, channel_id)
    a = yt._get_single_video_data(video_id,part)
    Views.append(a['viewCount'])

df["views"] = Views
df.to_excel("..\csv\output.xlsx")