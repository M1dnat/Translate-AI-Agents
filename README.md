# 🌐 智能翻译助手

一个基于 Gradio 和 LangChain 构建的智能翻译 Web 应用，支持多种语言翻译和多种翻译风格。

## ✨ 功能特点

- 🤖 AI驱动：基于通义千问 Qwen3-8B 模型
- 🌍 多语言支持：中文、英文、日文、韩文、法文、德文、西班牙文、俄文
- 🎨 多种风格：正式、口语、文学
- 📝 自动检测源语言
- 📖 专业术语自动解释
- 🔗 支持公网访问

## 🛠️ 技术栈

- Python 3.8+
- Gradio - Web界面
- LangChain - LLM框架
- 通义千问 Qwen3-8B - 翻译模型
- SiliconFlow API - API服务

## 📦 安装步骤

### 1. 克隆项目
git clone https://github.com/yourusername/smart-translator.git
cd smart-translator

### 2. 安装依赖
pip install gradio langchain langchain-core python-dotenv

### 3. 配置API密钥
创建 .env 文件，添加：
API_KEY=your_siliconflow_api_key_here

### 4. 运行应用
python app.py

## 🚀 使用方法

### 本地访问
浏览器打开：http://localhost:7860

### 公网访问（cpolar方式）
终端1：python app.py
终端2：& "C:\Program Files\cpolar\cpolar.exe" http 7860

## 📝 翻译示例

输入：Hello, how are you?
目标语言：中文
输出：
【原语言】：英文
【翻译】：你好吗？

输入：这个框架真的超级好用
目标语言：英文
输出：
【原语言】：中文
【翻译】：This framework is really easy to use!

## ⚠️ 注意事项

1. API调用会产生费用
2. 公网链接有时间限制
3. 关闭终端后服务停止

## 📄 许可证

MIT License
