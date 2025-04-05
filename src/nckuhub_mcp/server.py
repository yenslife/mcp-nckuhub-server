from mcp.server import FastMCP
from nckuhub_mcp.utils import (
    fetch_all_course,
    fetch_course,
    fetch_all_dpmt,
    fetch_all_course_prev,
)

# Initialize the server
mcp = FastMCP("nckuhub-mcp")


@mcp.tool()
async def get_all_course() -> list[dict]:
    """
    取得所有課程資訊
    e.g.
    ```json
    [
        {
            "id": 487,
            "系號": "A9",
            "選課序號": "046",
            "課程名稱": "音樂舞蹈戲劇",
            "老師": "林怡薇",
            "時間": "[2]3~4 ",
            "學分": 2,
            "選必修": "必修",
            "系所名稱": "通識中心 "
        }
    ]
    ```
    """
    return await fetch_all_course()


@mcp.tool()
async def get_course(course_id: str) -> dict:
    """
        取得指定課程的評價
        e.g.
        ```json
        {
        "got": 8.25,
        "cold": 6,
        "sweet": 8.25,
        "rate_count": 4,
        "courseInfo": {
            "id": "1722",
            "系所名稱": "資訊系 CSIE",
            "系號": "F7",
            "選課序號": "F7053",
            "課程碼": "F721300",
            "分班碼": "1",
            "班別": "甲",
            "年級": "2",
            "類別": "講義",
            "組別": null,
            "英語授課": "N",
            "課程名稱": "演算法",
            "選必修": "必修",
            "學分": 3,
            "老師": "謝孫源",
            "已選課人數": 92,
            "餘額": 68,
            "時間": "[2]2~4 ",
            "教室": "共同教室 A1302",
            "備註": "",
            "限選條件": "",
            "業界參與": "否",
            "屬性碼": "CSIE3003",
            "跨領域學分學程": "",
            "Moocs": "否",
            "updateTime": null,
            "comment_num": 3,
            "remain_update_time": "2025-01-26T11:10:30.000Z",
            "count": 51,
            "admit": null,
            "created_time": "2025-01-14T00:59:05.000Z",
            "comment": 4,
            "course_style": 0,
            "report_hw": 0,
            "score_style": 0,
            "semester": null
        },
        "comment": [
            {
            "id": 10101,
            "comment": "演算法這門課可以深入教授困難的內容，也可以簡單帶過，而這堂課偏向後者。只要抓住上課重點，就一定能拿到A。\n100：1\n90+：138\n80+：98\n70+：18\n60+：6\n其他：3",
            "semester": "112-2"
            },
            {
            "id": 5752,
            "comment": "簡單來說就是超級棒!!!\n老師雖然常常有事情會缺席\n但是只要老師來上的話\n都很有趣\n作業很簡單\n考試也很簡單\n只要你前幾天好好用功看ppt\n都會拿到好成績\n阿點名不定時\n所以盡量不要缺席\n",
            "semester": "107-2"
            },
            {
            "id": 5251,
            "comment": "作業：每個chapter都會有作業，要花點功夫。\n\n出席：偶爾突擊點名，老師有時候沒來，會由博士生代上。\n\n考試:基本上考古題上的應用、數學證明都會考，不過讀透PPT足以應付。\n\n心得:老師講話有點搞笑，喜歡叫大家\"喊一遍\"來提神。講解的速度也偏快，上課進度也蠻快的，必須要好好把握自己學習的進度。",
            "semester": "107-2"
            },
            {
            "id": 3700,
            "comment": "我愛老師!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n老師講解觀念十分清楚(雖然是有點快)，上課很有活力對學生也很好~",
            "semester": "106-2"
            }
        ],
        "rates": [
            {
            "id": 1119,
            "got": 10,
            "sweet": 7,
            "cold": 2,
            "user_id": 1986,
            "post_id": 3700,
            "course_name": "演算法",
            "teacher": "謝孫源 ",
            "like": 0,
            "dislike": 0,
            "give": 1,
            "recommand": 1,
            "hard": 1
            },
            {
            "id": 2622,
            "got": 7,
            "sweet": 7,
            "cold": 7,
            "user_id": 2784,
            "post_id": 5251,
            "course_name": "演算法",
            "teacher": "謝孫源",
            "like": 0,
            "dislike": 0,
            "give": 1,
            "recommand": 1,
            "hard": 1
            },
            {
            "id": 3123,
            "got": 9,
            "sweet": 9,
            "cold": 9,
            "user_id": 1947,
            "post_id": 5752,
            "course_name": "演算法",
            "teacher": "謝孫源",
            "like": 0,
            "dislike": 0,
            "give": 1,
            "recommand": 1,
            "hard": 1
            },
            {
            "id": 7314,
            "got": 7,
            "sweet": 10,
            "cold": 6,
            "user_id": 11252,
            "post_id": 10101,
            "course_name": "演算法",
            "teacher": "謝孫源",
            "like": 0,
            "dislike": 0,
            "give": 1,
            "recommand": 1,
            "hard": 1
            }
        ],
        "courserate_id": 0
        }
    ```
    """
    return await fetch_course(course_id)


@mcp.tool()
async def get_all_dpmt() -> list[dict]:
    """
    取得所有系所資訊
    e.g.
    ```json
    [
        {
            "id": 1,
            "name": "資訊系 CSIE"
        }
    ]
    ```
    """
    return await fetch_all_dpmt()


@mcp.tool()
async def get_all_course_prev() -> list[dict]:
    """
    取得所有課程現況資訊
    """
    return await fetch_all_course_prev()


def main():
    print("正在啟動 NCKUHub MCP 服務器...")
    mcp.run()


if __name__ == "__main__":
    main()
