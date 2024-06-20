from typing import Optional

from fastapi import FastAPI

import random  # randomライブラリを追加

from fastapi.responses import HTMLResponse #インポート

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "soccer!!⚽"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/omikuji")
def omikuji():
    omikuji_list = [
        "大吉",
        "中吉",
        "小吉",
        "吉",
        "半吉",
        "末吉",
        "末小吉",
        "凶",
        "小凶",
        "大凶"
    ]

    return omikuji_list[random.randrange(10)]

@app.get("/index")
def index():
    html_content = """
    <html lang="ja">
        <head>
        <meta charset="UTF-8">
    </head>
    <body>
        <h2 style="color: #ffffff; background-color: #00ff00;">好きな歌手</h2>
        <p style="color: #ff0000">藤井風</p>
        <h2 style="color: #ffffff; background-color: #00ff00;">はまっている曲</h2>
        <p style="color: #ff0000">藤井風‐花</p>
        <a href="https://www.google.co.jp/" title="検索">ググる</a>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


@app.post("/present")
async def new_naming(present):
   colors_list = [
        "赤色",
        "青色",
        "黄色",
        "緑色",
        "オレンジ",
        "ピンク",
        "紫色",
        "水色",
        "朱色",
        "黒色"
    ]
     luckyColor_result = colors_list[random.randrange(10)]
    return {
        "response": f"メッセージ {present}ありがとう。今日のあなたのラッキーカラーは",
        "omikuji": omikuji_result
    }