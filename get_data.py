import pandas as pd
import os
import wget
import json
import ast
import urllib.request
def download_images_from_df(df=None,target_folder='./output/images/',limit=None):
    df = df
    counter=0
    stop_flag=False
    source_path='https://hammoq-assets.storage.googleapis.com/assets/'
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    for images_ids in df['images']:
        if not stop_flag:
            try:
                images_ids = ast.literal_eval(images_ids)
            except:
                pass            
            for img_id in images_ids:
                try:
                    wget.download(source_path+img_id,target_folder+'/'+img_id.split('blob')[0]+'.jpg')
                    print(f'{img_id} downloaded to {target_folder} successfully')
                    counter+=1
                    if limit is not None and counter >=limit:
                        stop_flag=True
                        break
                except:
                    print(f'{img_id} skipped')
    print(f'{counter} images downloaded')

df = pd.read_csv('./output/women_shorts_to_get.csv')
download_images_from_df(df,'./output/images/shorts/',limit=1000)
