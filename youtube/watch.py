import streamlit as st
import yt_dlp
import os

def video_download(URL):
    file_keep = "watch.py"
    files = os.listdir('./')
    for file in files:
        if file != file_keep:
            os.remove(file)

    # カスタマイズしたオプションを設定
    ydl_opts = {
        'outtmpl': './video.mp4',  # ファイル名と保存場所を指定
        'format' :"bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]",
        'progress_hooks': [progress_hook],
    }

        # YoutubeDLインスタンスを作成してダウンロード
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([URL])
        except Exception as e:
            print("Error")

def progress_hook(d):
    progress = float()
    if d['status'] == 'downloading':
        progress = (f"ダウンロード: {d['filename']} - {d['_percent_str']}")

st.title("YouTubeを見る")
URL = st.text_input("URLを入力")
if st.button("処理開始"):
    video_download(URL)
    
    file_select = "watch.py"
    files = os.listdir('.')
    
    for file in files:
        if file != file_select:
            with open('video.mp4', 'rb') as video_file:
                video_bytes = video_file.read()
                st.video(video_bytes)
