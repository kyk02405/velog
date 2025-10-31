import feedparser, datetime, os

# ✅ 올바른 Velog RSS URL
RSS_URL = "https://v2.velog.io/rss/@kyk02405"

# ✅ 저장 폴더
POSTS_DIR = "velog-posts"
os.makedirs(POSTS_DIR, exist_ok=True)

# ✅ RSS 파싱
feed = feedparser.parse(RSS_URL)

# ✅ 최근 10개 글 덮어쓰기 (수정글도 반영됨)
for entry in feed.entries[:10]:
    title = entry.title.replace('/', '-').replace('\\', '-').strip()
    link = entry.link
    pub_date = entry.published
    desc = entry.description.strip()

    file_path = os.path.join(POSTS_DIR, f"{title}.md")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n")
        f.write(f"- 📅 Published: {pub_date}\n")
        f.write(f"- 🔗 [Read on Velog]({link})\n\n")
        f.write(desc)

# ✅ 강제 변경 감지를 위한 로그 기록 (항상 커밋되게)
with open("sync-log.txt", "a", encoding="utf-8") as log:
    log.write(f"Synced at {datetime.datetime.now()}\n")

print("✅ Velog posts synced successfully!")
