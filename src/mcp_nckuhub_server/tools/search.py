from thefuzz import process
from mcp_nckuhub_server.tools import fetch_all_dpmt_impl, fetch_all_course_impl


async def search_department_id_by_name_impl(DepName: str) -> str:
    """用系所名稱進行模糊搜尋系所代碼"""
    dpmt = await fetch_all_dpmt_impl()
    department_names = [item["DepName"] for item in dpmt]

    # 使用模糊搜尋找出最接近的系所名稱
    best_match, score = process.extractOne(DepName, department_names)

    # 如果相似度太低，返回未找到
    if score < 50:
        return "未找到系所代碼，請輸入正確的系所名稱"

    # 找出對應的系所代碼
    for item in dpmt:
        if item["DepName"] == best_match:
            return item["DepPrefix"]

    return "未找到系所代碼"


async def search_courses_by_department_id_impl(DepPrefix: str = "") -> list[dict]:
    course = await fetch_all_course_impl()
    result = []
    for item in course:
        if item["系號"] == DepPrefix:
            result.append(item)
    return result
