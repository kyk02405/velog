import feedparser, datetime, os

# ✅ Velog RSS URL
RSS_URL = "https://v2.velog.io/rss/@kyk02405"

# ✅ 저장 폴더
POSTS_DIR = "velog-posts"
os.makedirs(POSTS_DIR, exist_ok=True)

# ✅ RSS 파싱
feed = feedparser.parse(RSS_URL)

valid_entries = []

for entry in feed.entries:
    # 🔥 1) 발행일 없는 글(초안/자동저장)은 제외
    if not hasattr(entry, "published") or entry.published.strip() == "":
        continue
    
    # 🔥 2) description이 너무 짧으면(임시저장일 확률 높음) 제외
    if len(entry.description.strip()) < 80:  
        continue

    valid_entries.append(entry)

# 🔥 유효한 최근 10개만 저장
for entry in valid_entries[:10]:
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

# 🔥 불필요한 grass 폭발을 막기 위해 sync-log 자동 기록 제거
# → 자동저장으로 인한 잔디 폭발 방지막
# (원한다면 다시 On 가능)
# with open("sync-log.txt", "a", encoding="utf-8") as log:
#     log.write(f"Synced at {datetime.datetime.now()}\n")

print("✅ Velog posts synced without autosave drafts!")
