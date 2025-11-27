import sys
from fastmcp import FastMCP
import os
import httpx

# 强制使用 UTF-8 输出，防止 Windows 下中文乱码导致 MCP 协议解析错误
sys.stdout.reconfigure(encoding='utf-8')

# 1. 定义工头：给你的服务起个名
# logLevel 参数在初始化时已废弃，改为在 run() 中指定或使用全局设置
mcp = FastMCP("WeatherStation")

# 2. 定义工具：这就是给 AI 的“菜单”
# 只要加上 @mcp.tool()，AI 就能看见这个函数
@mcp.tool()
async def get_weather(city: str) -> str: # <-- 核心变化：必须是 async def
    """
    查询指定城市的天气状况，数据来自 OpenWeatherMap 实时 API。
    """
    # 🚨 从环境变量读取密钥
    API_KEY = os.environ.get("OPENWEATHER_API_KEY")
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    if not API_KEY:
        return "【错误】: OPENWEATHER_API_KEY 未设置，无法联网！"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric", # 使用摄氏度
        "lang": "zh_cn"   # 返回中文描述
    }

    try:
        # 使用 httpx 异步请求，并等待结果
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(BASE_URL, params=params)
            response.raise_for_status() # 如果状态码是 4xx/5xx，抛出异常

            data = response.json()
            
            # 简化解析结果
            temp = data["main"]["temp"]
            description = data["weather"][0]["description"]
            
            return f"【实时天气】{city}：{description}，温度 {temp}°C。数据来源：OpenWeatherMap"
            
    except httpx.HTTPStatusError as e:
        return f"【API 错误】: 无法找到 {city} 的天气信息或 API 密钥错误。状态码: {e.response.status_code}"
    except Exception as e:
        return f"【网络错误】: 联网失败。错误信息: {e}"

# 3. 开工！
if __name__ == "__main__":
 
    mcp.run(log_level="ERROR")
