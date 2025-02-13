import json
from src.tools.openrouter_config import get_chat_completion

def translate_to_chinese(text: str) -> str:
    # 将文本翻译为中文
    system_message = {
        "role": "system",
        "content": "以金融领域专家的身份做翻译"
    }
    user_message = {
        "role": "user",
        "content": f"将以下一段文字翻译成中文：\n\n{text}"
    }
    return get_chat_completion([system_message, user_message])

if __name__ == "__main__":
    translate_to_chinese("Risk Management's hold signal is a hard constraint.  Considering the weighted average of other signals, Valuation (0%), Fundamentals (bearish, 30%), Technicals (neutral, 25%), and Sentiment (bullish, 10%), there is not enough conviction to deviate from the hold recommendation. The high risk score from Risk Management further supports this decision.")