import os
from yt_dlp import YoutubeDL

def download_video():
    print("--- برنامج تحميل مقاطع اليوتيوب ---")
    url = input("أدخل رابط مقطع اليوتيوب هنا: ").strip()
    
    if not url:
        print("الرابط فارغ! حاول مرة أخرى.")
        return

    # خيارات التحميل (تأكد من حفظه في مجلد التنزيلات أو مجلد الفيديو عندك)
    download_path = os.path.expanduser('~/Videos')
    os.makedirs(download_path, exist_ok=True)

    ydl_opts = {
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        # اختيار أفضل جودة فيديو مع الصوت
        'format': 'bestvideo+bestaudio/best',
    }

    print("جاري التحميل، انتظر قليلاً...")
    
    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"\n تم تحميل المقطع بنجاح وحفظه في مجلد: {download_path} 🚀")
    except Exception as e:
        print(f"حدث خطأ أثناء التحميل: {e}")

if __name__ == '__main__':
    download_video()
