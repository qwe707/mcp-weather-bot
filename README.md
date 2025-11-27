# My Weather MCP Server 

这是一个基于 FastMCP 的 AI 工具服务，可以让 Claude/Cursor 具备以下能力（我没有claude，然后cursor没money，antigarvity好像得是github的mcp才可以，最后是在vscode里下载了cline进行操作的，一把辛酸泪）：
1. **查天气**：通过 OpenWeatherMap API 查询全球实时天气。
2. **读文档**：读取本地的项目笔记。（这个不稳定我给删了）

## 如何运行

1. 安装依赖：
   ```bash
   pip install -r requirements.txt
   设置 API 密钥 (Windows PowerShell):

2.设置密钥

$env:OPENWEATHER_API_KEY="你的密钥"



3.运行，查查把，为你心爱的人看看对方城市的天气
python weather.py
非常简单，做这个只是为了让自己能熟悉mcp了解一下，明天看看再进阶一下，再学习一下sse
