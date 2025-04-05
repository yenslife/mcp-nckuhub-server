import time


def convert_ad_to_roc(year: str) -> str:
    return str(int(year) - 1911)


def parse_semester_from_query_impl(query: str) -> str:
    """
    將使用者的自然語言查詢轉換為學期格式
    """
    timestamp = time.time()
    current_year = int(time.strftime("%Y", time.localtime(timestamp)))
    current_month = int(time.strftime("%m", time.localtime(timestamp)))
    current_year_roc = current_year - 1911

    prompt = f"""你是一個工具，用來將使用者輸入的查詢字串（可能包含年份、學期、描述）轉換為成功大學的「學期代碼」，格式為「民國年-學期」（例如 113-2）。

請依照以下規則進行轉換：
1. 學期 1：約每年 8 月 1 日到隔年 1 月 31 日。
2. 學期 2：約每年 2 月 1 日到 7 月 31 日。
3. 西元年份需轉換為民國年（民國 = 西元 - 1911）。
4. 僅回傳學期代碼，例如：112-1、113-2，不需要說明文字。

範例：
- 使用者輸入 "2023-2024 2學期" → 回傳 "113-2"
- 使用者輸入 "112年第二學期" → 回傳 "112-2"

現在時間：{current_year_roc} 年 {current_month} 月  
使用者查詢：{query}  
請回傳對應的學期代碼（格式為 112-1 或 113-2）：
"""

    return prompt


if __name__ == "__main__":
    print(parse_semester_from_query_impl("2024-2025 2學期"))
