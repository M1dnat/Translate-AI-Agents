"""
智能翻译助手 - Gradio Web 版本（支持流式输出）
"""

#硅基流动https://cloud.siliconflow.cn/me/account/ak

import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, HumanMessage
import gradio as gr

load_dotenv()


class SmartTranslator:
    def __init__(self):
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("❌ 未找到 API_KEY！请确保 .env 文件存在且内容正确")

        print(f"✅ API Key 已加载: {api_key[:8]}...")

        self.model = init_chat_model(
            "Qwen/Qwen3-8B",
            model_provider='openai',
            base_url='https://api.siliconflow.cn/v1',
            api_key=api_key,
            temperature=0
        )

    def translate_stream(self, text: str, target_lang: str = '中文', style: str = '正式'):
        """流式翻译生成器"""
        system_prompt = f"""你是一个专业的翻译助手。

任务：
1. 自动检测输入文本语言
2. 翻译成 {target_lang}
3. 使用 {style} 风格
4. 如有专业术语，在翻译后用括号标注原文

输出格式:
【原语言】：xxx
【翻译】：xxx
【术语解释】：（如果有）
"""

        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=text)
        ]

        full_response = ""
        for chunk in self.model.stream(messages):
            if chunk.content:
                full_response += chunk.content
                yield full_response


translator = SmartTranslator()


# ==================== Gradio 调用函数 ====================
def translate(text, target_lang, style):
    """供 Gradio 调用的翻译函数 - 返回完整结果"""
    if not text or not text.strip():
        return "❌ 请输入要翻译的文本"
    
    # 消费生成器，返回最终完整结果
    result = ""
    for chunk in translator.translate_stream(text, target_lang, style):
        result = chunk  # 持续更新
    
    return result


# 创建 Gradio 界面
with gr.Blocks(title="智能翻译助手", theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🎉 智能翻译助手\n支持多语言 · 多种风格")

    with gr.Row():
        with gr.Column(scale=2):
            input_text = gr.Textbox(
                label="📝 输入文本",
                placeholder="在此输入你要翻译的内容...",
                lines=6
            )

            with gr.Row():
                target_lang = gr.Dropdown(
                    choices=["中文", "英文", "日文", "韩文", "法文", "德文", "西班牙文", "俄文"],
                    value="英文",
                    label="🌐 目标语言"
                )
                style = gr.Dropdown(
                    choices=["正式", "口语", "文学"],
                    value="口语",
                    label="🎨 翻译风格"
                )

            translate_btn = gr.Button("🚀 开始翻译", variant="primary", size="large")

        with gr.Column(scale=2):
            output_text = gr.Textbox(
                label="📄 翻译结果",
                lines=12
            )

    # 绑定翻译按钮
    translate_btn.click(
        fn=translate,
        inputs=[input_text, target_lang, style],
        outputs=output_text
    )

    # 示例
    gr.Examples(
        examples=[
            ["LangChain is a framework for developing applications.", "中文", "正式"],
            ["这个框架真的超级好用，强烈推荐！", "英文", "口语"],
            ["Artificial Intelligence is transforming the world.", "中文", "正式"],
        ],
        inputs=[input_text, target_lang, style]
    )

    gr.Markdown("---\n💡 提示：点击翻译按钮后请稍等片刻")

# 在你的 translator.py 文件中，找到启动部分，修改为：
if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=True,  # 这行设置为 True 即可生成公网链接
        debug=True
    )

#使用cpolar进行公网展示
#https://www.cpolar.com/

#步骤1：启动翻译程序（终端1）
#python 智能翻译助手.py

#步骤2：启动 cpolar 隧道（终端2）
#& "C:\Program Files\cpolar\cpolar.exe" http 7860