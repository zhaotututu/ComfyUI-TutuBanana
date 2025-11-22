<div align="center">

![AI LAB Tutu Logo](image/logo.png)

# 🍌 ComfyUI-TutuBanana

**ComfyUI的专业Gemini图像生成节点套装**

[![GitHub stars](https://img.shields.io/github/stars/zhaotututu/ComfyUI-TutuBanana?style=social)](https://github.com/zhaotututu/ComfyUI-TutuBanana)
[![GitHub issues](https://img.shields.io/github/issues/zhaotututu/ComfyUI-TutuBanana)](https://github.com/zhaotututu/ComfyUI-TutuBanana/issues)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)

[中文文档](README.md) | [English](README_EN.md)

</div>

---

## 中文文档

### 📖 项目简介

ComfyUI-TutuBanana 是一个功能强大的ComfyUI自定义节点套装，专为Google Gemini系列模型的图像生成而设计。该项目提供了三个核心节点，涵盖从提示词模板管理到多平台API调用的完整工作流程。

**核心特性：**

- 🎨 **三大核心节点**：提示词模板管理器 + 双API平台支持 + Google官方API专业版
- 📚 **333个专业模板**：涵盖10大类别的高质量提示词模板，中英文双语支持
- 🖼️ **多图像处理**：最多支持14张图像同时输入，适用于复杂的图像编辑任务
- 🌐 **多平台兼容**：支持 OpenRouter、ai.comfly.chat、Google官方API 和 T8Star
- 🔄 **智能索引映射**：自动处理端口号与API图片索引的对应关系
- ⚡ **随机变化控制**：通过种子实现可控的随机性，支持"抽卡"式生成

---

### 🎯 三大核心节点

#### 1️⃣ 提示词模板管理器

**节点名称：** `🎨 Tutu 图图香蕉模型提示词模板管理器`

![提示词模板管理器](image/QQ20251123-003425.png)

**功能特点：**

- 📚 内置333个精选提示词模板
- 🗂️ 10大类别分类（摄影、自然、品牌、交通工具、风景、角色等）
- 🌍 中英文双语模板支持
- 🔍 可视化模板浏览器，支持搜索和预览
- 💾 一键加载和应用模板

![模板浏览器界面](image/QQ20251123-003541.png)

**使用场景：**

- 快速获取专业级提示词灵感
- 标准化提示词风格
- 学习高质量提示词的写作方法

---

#### 2️⃣ 香蕉模型（OpenRouter / Comfly）

**节点名称：** `🍌 Tutu 图图的香蕉模型(OpenRouter / Comfly)`

![香蕉模型节点](image/QQ20251123-003640.png)

**核心功能：**

- 🌐 **双平台支持**：OpenRouter 和 ai.comfly.chat
- 🎯 **智能模型选择**：根据API提供商自动匹配模型
  - OpenRouter: `google/gemini-2.5-flash-image-preview`
  - Comfly: `gemini-2.5-flash-image-preview`
- 🖼️ **5路图像输入**：支持最多5张参考图像
- 🔢 **自动索引映射**：将端口号自动转换为API图片编号
- 🎲 **随机种子控制**：可重现的随机性，支持"抽卡"功能

**技术特性：**

- Base64图像编码
- 自动提示词增强（区分文生图/图生图模式）
- 智能图片标注（`[这是图1]`、`[这是图2]`等）
- 非流式API调用，更稳定可靠

**输入端口：**

- `prompt` (强制输入)：提示词文本
- `input_image_1~5` (可选)：参考图像
- `api_provider`：API提供商选择
- `seed`：随机种子（0为完全随机）
- `comfly_api_key` / `openrouter_api_key`：API密钥

**输出端口：**

- `generated_images`：生成的图像张量
- `response`：详细的生成信息

---

#### 3️⃣ 香蕉模型专业版（Google官方 / T8Star）

**节点名称：** `🍌 Tutu 图图的香蕉模型专业版/香蕉2 (Google官方 / T8Star)`

![香蕉模型专业版](image/QQ20251123-003650.png)

**专业特性：**

- 🏢 **Google官方API直连**：使用官方Gemini 3 Pro API
- 🎯 **T8Star API支持**：国内优化的API服务
- 🖼️ **14路图像输入**：专业级多图处理能力
- 📐 **精确尺寸控制**：
  - 宽高比：1:1, 2:3, 3:2, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9
  - 分辨率：1K, 2K, 4K
- 🔍 **Google搜索增强**：启用联网搜索功能（仅Google官方）
- 🎲 **智能图片选择**：自动选择最高分辨率输出

**输入端口：**

- `prompt` (强制输入)：提示词文本
- `input_image_1~14` (可选)：参考图像
- `api_provider`：Google官方 / T8Star
- `aspect_ratio`：宽高比选择
- `image_size`：分辨率级别
- `seed`：随机种子
- `enable_google_search`：启用搜索增强（仅Google，就是可以获得即时信息，比如绘制一张图，包含明天的天气情况和日期，模型就会自主去查找，从而获得当下最准确的信息。）
- `google_api_key` / `t8star_api_key`：API密钥

**输出端口：**

- `generated_image`：最高质量生成图像
- `response`：详细的生成报告

---

### 🚀 快速开始

#### 安装方式

**方法一：通过ComfyUI Manager安装（推荐）**

1. 打开ComfyUI Manager
2. 搜索 `TutuBanana`
3. 点击安装并重启ComfyUI

**方法二：Git克隆安装**

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/zhaotututu/ComfyUI-TutuBanana.git
cd ComfyUI-TutuBanana
pip install -r requirements.txt
```

**方法三：手动下载安装**

1. 下载ZIP：[GitHub Releases](https://github.com/zhaotututu/ComfyUI-TutuBanana/releases)
2. 解压到 `ComfyUI/custom_nodes/ComfyUI-TutuBanana`
3. 安装依赖：`pip install -r requirements.txt`
4. 重启ComfyUI

---

#### 配置API密钥

**方式一：在节点中直接输入（推荐）**

- 在节点的对应API密钥输入框中填写
- 自动保存到配置文件

**方式二：编辑配置文件**

创建或编辑 `Tutuapi.json`：

```json
{
  "comfly_api_key": "your_comfly_api_key_here",
  "openrouter_api_key": "your_openrouter_api_key_here",
  "google_api_key": "your_google_api_key_here",
  "t8star_api_key": "your_t8star_api_key_here"
}
```

**获取API密钥：**

- **OpenRouter**: [https://openrouter.ai](https://openrouter.ai)
- **ai.comfly.chat**: [https://ai.comfly.chat](https://ai.comfly.chat)
- **Google官方**: [https://aistudio.google.com/apikey](https://aistudio.google.com/apikey)
- **T8Star**: [https://ai.t8star.cn](https://ai.t8star.cn)

---

### 📊 使用场景与工作流

#### 场景1：纯文本生成图像

```
[提示词模板管理器] → [香蕉模型] → 生成图像
```

1. 在模板管理器中选择合适的模板
2. 将模板输出连接到香蕉模型的prompt输入
3. 不连接任何图像输入
4. 运行生成

#### 场景2：单图编辑/风格转换

```
[加载图像] → input_image_1
[提示词] → prompt
[香蕉模型] → 生成编辑后的图像
```

#### 场景3：多图合成创作

```
[图像1] → input_image_1
[图像2] → input_image_2
[图像3] → input_image_3
[提示词：将图1的人物放在图2的背景中，使用图3的风格] → prompt
[香蕉模型] → 生成合成图像
```

#### 场景4：专业高清输出

```
[提示词模板管理器] → [香蕉模型专业版]
选择：
- 分辨率：4K
- 宽高比：16:9
- Google官方API
→ 生成超高清图像
```

---

### 🎯 高级技巧

#### 1. 图片索引自动映射

**问题场景：**
假设你只连接了 `input_image_2` 和 `input_image_5`

**✅你可以这样写：**

```
将图2中的猫和图5中的狗合成在一起
```

**✅ 也可以这样写：**

```
将图1中的猫和图2中的狗合成在一起
```

**原因：** 节点会自动将已连接的端口映射为连续的图片编号。系统会自动转换：

- `input_image_2` (端口2) → `图1`（API中的第1张图）
- `input_image_5` (端口5) → `图2`（API中的第2张图）

**💡 最佳实践：**

- 使用从1开始的连续编号：`图1`, `图2`, `图3`...
- 支持多种表达：`图X`, `图片X`, `第X张图`, `第X个图`
- 系统会自动处理端口号与实际图片位置的对应关系

---

#### 2. 随机种子的使用

**`seed = 0`（默认）**

- 每次运行生成完全不同的结果
- 适合"抽卡"式探索
- 每次会在提示词末尾添加随机标识符

**`seed = 固定值（如12345）`**

- 使用相同提示词和种子会生成相似（但不完全相同）的结果
- 适合微调和迭代
- 基于种子生成确定性的随机变化

**示例：**

```
seed = 0  → variation-53921
seed = 0  → variation-78432  (完全不同)
seed = 42 → variation-67834
seed = 42 → variation-67834  (每次相同)
```

---

#### 3. 模板系统使用技巧

**浏览和搜索：**

- 点击节点的"浏览模板"按钮打开模板管理器
- 左侧分类栏筛选类别
- 右上角搜索框快速定位
- 查看示例图片了解效果

**应用模板：**

1. 选择模板后，提示词会自动加载到输入框
2. 可以直接使用或进一步编辑
3. 模板中的 `{prompt}` 占位符会被替换为实际内容

**自定义模板：**

- 点击"创建新模板"
- 输入名称、分类、提示词内容
- 保存后即可在"我的模板"中找到

---

### 🔧 系统要求

**运行环境：**

- **ComfyUI**: 最新版本
- **Python**: 3.8+ (推荐 3.10+)
- **操作系统**: Windows / macOS / Linux

**核心依赖：**

```
aiohttp              # 异步HTTP客户端
aiohttp-cors         # CORS支持
GitPython           # Git集成
numpy               # 数值计算
Pillow              # 图像处理
requests            # HTTP请求
torch               # PyTorch框架
transformers        # Hugging Face库
huggingface-hub     # Hub集成
psutil              # 系统监控
matrix-client       # Matrix协议
```

---

### ❓ 常见问题

#### Q1: 为什么我的图片没有生成？

**A:** 检查以下几点：

1. API密钥是否正确
2. 网络连接是否正常
3. API余额是否充足
4. 提示词是否明确包含生成图片的指令
5. 查看控制台日志获取详细错误信息

#### Q2: 如何获得更好的生成质量？

**A:** 建议：

1. 使用香蕉模型专业版（支持更高分辨率）
2. 选择4K分辨率
3. 使用提示词模板管理器中的专业模板
4. 提供清晰、具体的描述
5. 如需真实感，添加"photorealistic"、"高清"等关键词

#### Q3: 提示词中的图片编号如何使用？

**A:**

- **始终从1开始编号**：`图1`, `图2`, `图3`...
- **不要使用端口号**：即使你连接的是 `input_image_3`，也应该写"图1"
- 系统会自动映射端口号到连续的图片编号

#### Q4: OpenRouter和Comfly有什么区别？

**A:**

- **OpenRouter**: 国际服务，支持多种模型路由，标准OpenAI格式
- **Comfly**: 国内优化，访问速度快，界面友好

### 📚 教程与资源

**视频教程：**

- 📺 **Bilibili**: [@zhaotutu](https://space.bilibili.com/431046154) - 详细使用教程、工作流演示
- 📺 **YouTube**: [@zhaotutu](https://www.youtube.com/@zhaotutu) - 英文教程和案例分享

**工作流下载：**

- 🔗 [RunningHub](https://www.runninghub.ai/user-center/1936823199386537986/webapp?inviteCode=rh-v0990) - 下载配套工作流和案例

**社区支持：**

- 💬 [GitHub Issues](https://github.com/zhaotututu/ComfyUI-TutuBanana/issues) - 问题反馈和功能建议
- 📖 [GitHub Wiki](https://github.com/zhaotututu/ComfyUI-TutuBanana/wiki) - 详细文档和教程

---

### 📝 更新日志

#### v2.0 (当前版本 - 重大更新)

- ✨ 新增提示词模板管理器（333个专业模板）
- ✨ 新增香蕉模型专业版（支持Google官方API和T8Star）
- 🔄 重构图片索引映射系统（自动端口转换）
- 🎲 新增随机种子控制（可重现的随机性）
- 🖼️ 扩展图像输入（5路→14路）
- 📐 新增精确尺寸控制（宽高比+分辨率级别）
- 🔍 支持Google搜索增强功能
- 🌐 优化多平台API兼容性

#### v1.1

- 🔧 修复节点名称冲突
- 🖼️ 统一base64图像处理
- 🎨 消除图片白边问题
- ⚡ 改进OpenRouter兼容性

#### v1.0

- 🎉 初始版本发布
- 🌐 多平台API支持
- 📦 基础预设系统
- 📡 流式响应支持

---

### 🤝 贡献与致谢

**参考项目：**

- [Comfyui_Comfly](https://github.com/ainewsto/Comfyui_Comfly) - 感谢原作者的优秀工作

---

### 📄 许可证

本项目基于 Apache-2.0 许可证开源。详见 [LICENSE](LICENSE) 文件。

---

### 📞 联系方式

- **GitHub**: [@zhaotututu](https://github.com/zhaotututu)
- **Bilibili**: [@zhaotutu](https://space.bilibili.com/431046154)
- **YouTube**: [@zhaotutu](https://www.youtube.com/@zhaotutu)

---

<div align="center">

**如果觉得这个项目有帮助，请给个⭐️支持一下！**

Made with ❤️ by AI LAB Tutu

</div>

