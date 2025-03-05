import requests
import re
import json

# Google 포토 공유 앨범 링크 (여기에 본인 링크 추가)
album_urls = [
    "https://photos.app.goo.gl/VoN3YiE4zFwZERkG9",
    "https://photos.app.goo.gl/Daid3aaurbLgDFNd7"
]

def get_google_photos_images(album_url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(album_url, headers=headers)
    
    if response.status_code == 200:
        image_urls = re.findall(r'https://lh3.googleusercontent.com/[^"]+', response.text)
        return image_urls
    else:
        return []

# 모든 앨범의 이미지 수집
all_images = []
for url in album_urls:
    all_images.extend(get_google_photos_images(url))

# JSON 파일로 저장
json_data = {"images": all_images}
with open("photos.json", "w") as json_file:
    json.dump(json_data, json_file, indent=4)

print("✅ photos.json 업데이트 완료!")
