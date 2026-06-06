# 📧 AI Email

AI邮件工具，支持邮件模板、营销、自动化。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 📝 邮件模板生成
- 📣 营销邮件生成
- ⚙️ SMTP配置生成
- 📊 效果分析
- 🔄 自动化序列
- 📰 新闻通讯

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from ai_email import create_tools

tools = create_tools()

# 邮件模板
template = tools.generate_template("欢迎邮件", "友好")

# 营销邮件
campaign = tools.generate_campaign("新产品", "潜在客户", "提升转化")

# SMTP配置
smtp = tools.generate_smtp_config("Gmail")

# 效果分析
analysis = tools.analyze_performance(metrics)

# 自动化序列
drip = tools.generate_drip_campaign(["注册", "激活", "留存"])

# 新闻通讯
newsletter = tools.generate_newsletter("AI技术", "每周")
```

## 📁 项目结构

```
ai-email/
├── tools.py       # 邮件工具核心
└── README.md
```

## 📄 许可证

MIT License
