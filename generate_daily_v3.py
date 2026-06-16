"""
V3 自动更新器（预留真实数据接口）
运行：
python generate_daily_v3.py
"""

import json
from datetime import datetime
from random import uniform

def fetch_market_data():
    # TODO:
    # 替换成真实来源：
    # 中证指数 / 东方财富 / 公开API
    return {
        "price": round(uniform(1.08,1.20),3),
        "change": round(uniform(-2.5,2.5),2),
        "rsi": round(uniform(25,65),1),
        "dy": round(uniform(4.1,5.4),2),
        "score": round(uniform(72,97))
    }

def calc(data):
    return {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "price": str(data["price"]),
        "change": f'{data["change"]:+.2f}%',
        "rsi": str(data["rsi"]),
        "dy": f'{data["dy"]:.2f}%',
        "score": str(data["score"])
    }

daily = calc(fetch_market_data())

with open("daily.json","w",encoding="utf-8") as f:
    json.dump(daily,f,ensure_ascii=False,indent=2)

print("完成：daily.json")
