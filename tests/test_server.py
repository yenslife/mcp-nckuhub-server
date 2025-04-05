import pytest

from nckuhub_mcp.server import (
    get_all_course,
    get_course,
    get_all_dpmt,
    get_all_course_prev,
)


@pytest.mark.asyncio
async def test_get_all_course():
    """測試 get_all_course 函數的返回格式"""
    # 直接調用函數
    result = await get_all_course()

    # 驗證結果格式
    assert isinstance(result, list), "返回值應該是一個 list"
    if result:  # 如果 list不為空
        course = result[0]
        assert isinstance(course, dict), "list 中的每個項目應該是字典"
        # 檢查必要的鍵是否存在
        expected_keys = ["id", "課程名稱", "老師", "時間", "學分"]
        for key in expected_keys:
            assert key in course, f"課程字典中應該包含 '{key}' 鍵"


@pytest.mark.asyncio
async def test_get_course():
    """測試 get_course 函數的返回格式"""
    # 使用一個已知存在的課程 ID
    course_id = "1722"  # 演算法課程

    # 直接調用函數
    result = await get_course(course_id)

    # 驗證結果格式
    assert isinstance(result, dict), "返回值應該是一個字典"
    # 檢查必要的鍵是否存在
    expected_top_keys = ["courseInfo", "comment"]
    for key in expected_top_keys:
        assert key in result, f"返回字典中應該包含 '{key}' 鍵"

    # 檢查 courseInfo 的格式
    if "courseInfo" in result:
        course_info = result["courseInfo"]
        assert isinstance(course_info, dict), "courseInfo 應該是一個字典"
        expected_info_keys = ["id", "課程名稱", "老師"]
        for key in expected_info_keys:
            assert key in course_info, f"courseInfo 字典中應該包含 '{key}' 鍵"

    # 檢查 comment 的格式
    if "comment" in result and result["comment"]:
        comment = result["comment"][0]
        assert isinstance(comment, dict), "comment list中的每個項目應該是字典"
        expected_comment_keys = ["id", "comment", "semester"]
        for key in expected_comment_keys:
            assert key in comment, f"comment 字典中應該包含 '{key}' 鍵"


@pytest.mark.asyncio
async def test_get_all_dpmt():
    """測試 get_all_dpmt 函數的返回格式"""
    # 直接調用函數
    result = await get_all_dpmt()

    # 驗證結果格式
    assert isinstance(result, list), "返回值應該是一個 list"
    if result:  # 如果 list不為空
        dpmt = result[0]
        assert isinstance(dpmt, dict), "list中的每個項目應該是字典"
        # 檢查必要的鍵是否存在
        expected_keys = ["DepPrefix", "DepName"]
        for key in expected_keys:
            assert key in dpmt, f"系所字典中應該包含 '{key}' 鍵"


@pytest.mark.asyncio
async def test_get_all_course_prev():
    """測試 get_all_course_prev 函數的返回格式"""
    # 直接調用函數
    result = await get_all_course_prev()

    # 驗證結果格式
    assert isinstance(result, list), "返回值應該是一個 list"
    if result:  # 如果 list不為空
        course_prev = result[0]
        assert isinstance(course_prev, dict), "list 中的每個項目應該是字典"
        # 檢查必要的鍵是否存在
        expected_keys = ["id", "課程名稱"]
        for key in expected_keys:
            assert key in course_prev, f"課程前況字典中應該包含 '{key}' 鍵"
