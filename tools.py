"""
AI Email - AI邮件工具
支持邮件模板、营销、自动化
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class AIEmailTools:
    """
    AI邮件工具
    支持：模板、营销、自动化
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def generate_template(self, purpose: str, style: str = "professional") -> str:
        """生成邮件模板"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请生成{purpose}邮件模板：

风格：{style}

要求：
1. HTML格式
2. 响应式设计
3. 包含占位符"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def generate_campaign(self, product: str, audience: str, goal: str) -> Dict:
        """生成营销邮件"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请为{product}设计邮件营销：

目标人群：{audience}
目标：{goal}

请返回JSON格式：
{{
    "subject_lines": ["标题"],
    "content": "内容",
    "cta": "行动号召",
    "send_time": "发送时间"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"campaign": content}

    def generate_smtp_config(self, provider: str) -> str:
        """生成SMTP配置"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请生成{provider}的SMTP配置：

请生成Python代码，包含：
1. SMTP配置
2. 发送函数
3. 错误处理"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1500
        )

        return response.choices[0].message.content

    def analyze_performance(self, metrics: Dict) -> Dict:
        """分析邮件效果"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        metrics_text = json.dumps(metrics, ensure_ascii=False)

        prompt = f"""请分析邮件营销效果：

{metrics_text}

请返回JSON格式：
{{
    "performance": "表现",
    "strengths": ["亮点"],
    "weaknesses": ["不足"],
    "improvements": ["改进建议"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"analysis": content}

    def generate_drip_campaign(self, stages: List[str]) -> List[Dict]:
        """生成自动化邮件序列"""
        if not self.client:
            return [{"error": "LLM客户端未配置"}]

        stages_text = "\n".join(f"- {s}" for s in stages)

        prompt = f"""请生成自动化邮件序列：

阶段：
{stages_text}

请返回JSON格式：
[
    {{"stage": "阶段", "delay": "延迟", "subject": "标题", "content": "内容摘要"}}
]"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\[.*\]', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return [{"sequence": content}]

    def generate_newsletter(self, topic: str, frequency: str) -> Dict:
        """生成新闻通讯"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请生成{frequency}的{topic}新闻通讯：

请返回JSON格式：
{{
    "sections": [
        {{"title": "标题", "content": "内容"}}
    ],
    "design": "设计建议",
    "subject_lines": ["标题建议"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"newsletter": content}


def create_tools(**kwargs) -> AIEmailTools:
    """创建邮件工具"""
    return AIEmailTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("AI Email Tools")
    print()

    # 测试
    template = tools.generate_template("欢迎邮件", "友好")
    print(template[:300] + "...")
