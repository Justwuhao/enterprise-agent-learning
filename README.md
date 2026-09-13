# Enterprise Agent Learning

> 研究生一年级企业智能体（Enterprise Agent）学习、实验、项目实践与科研积累仓库。

## 1. 仓库定位

本仓库围绕“模型理解 → 大模型应用 → RAG → Agent → 企业系统 → 工程部署 → 评测与科研”的完整能力链建设。

目标不是单纯学习某一个模型或框架，而是持续形成：

- 可复用的学习笔记
- 可运行的技术 Demo
- 可演示的完整项目
- 可复现的实验记录
- 可用于科研和作品集的技术文档

## 2. 学习路线

### 阶段一：AI 基础与大模型应用（第 1-8 周）
Python、Git、Linux、HTTP、FastAPI、LLM API、Prompt、Token、Embedding、Transformer、结构化输出、Tool Calling、LangChain、LangGraph。

阶段产出：FastAPI Demo、LLM Chat、Prompt 实验平台、Workflow Demo。

### 阶段二：RAG 与企业知识库（第 9-16 周）
文档解析、Chunk、Embedding、向量数据库、Retriever、RAG、Chunk 优化、Hybrid Search、Rerank、Query Rewrite、RAG 评测。

阶段产出：企业知识库智能问答系统。

### 阶段三：Agent 与企业流程自动化（第 17-28 周）
ReAct、Tool Calling、Workflow、企业制度知识库、审批流程、Text-to-SQL、SQL 安全、数据分析 Agent、图表与报告、评测。

阶段产出：企业流程自动化 Agent、企业数据分析 Agent。

### 阶段四：企业级部署与综合项目（第 29-40 周）
Multi-Agent、Memory、企业级约束、Docker、PostgreSQL、Redis、模型服务、日志监控、Trace、Token/成本统计、综合平台。

阶段产出：多智能体企业助手、企业智能体综合平台、年度成果包。

## 3. 仓库结构

```text
enterprise-agent-learning/
├── README.md
├── .gitignore
├── docs/                       # 学习笔记
│   ├── 01-基础阶段/
│   ├── 02-RAG技术/
│   ├── 03-智能体开发/
│   └── 04-企业智能体/
├── projects/                   # 完整练手项目
│   ├── knowledge-base-rag/
│   ├── ticket-agent/
│   ├── multi-agent-office/
│   ├── enterprise-data-agent/
│   └── enterprise-agent-platform/
├── code-demos/                 # 单技术点最小实验
├── research/                   # 论文、实验与技术报告
└── weekly/                     # 40 周周报
```

## 4. 五个核心项目

| 项目 | 周期 | 核心目标 | 核心功能 |
|---|---|---|---|
| 企业知识库智能问答 | 7-16 周 | 掌握完整 RAG Pipeline | PDF/Word → 解析 → 切分 → Embedding → 检索 → Rerank → LLM → 来源引用 |
| 企业流程自动化 Agent | 17-22 周 | 掌握 Tool Calling + Workflow | 意图识别、制度查询、参数收集、工具调用、流程状态管理、Trace |
| 企业数据分析 Agent | 23-28 周 | 掌握 Text-to-SQL + 数据分析 | 自然语言 → SQL → 查询 → 指标 → 图表/报告 → SQL 安全 |
| 多智能体企业助手 | 29-34 周 | 掌握 Multi-Agent + Memory | 市场/销售/财务/技术 Agent 协作、任务拆解、消息传递、汇总 |
| 企业智能体综合平台 | 35-40 周 | 形成可复用平台雏形 | 知识库、Agent、工具、会话、日志、Workflow、Docker、部署 |

## 5. 每周执行闭环

周一：理论学习，记录 5-10 条关键笔记。

周二-周三：围绕一个最小 Demo 编码。

周四：改变一个变量做可复现实验。

周五：把本周能力接入主项目。

周末：写周报、整理 README、提交 Git。

## 6. Git 提交约定

- `docs:` 学习笔记
- `demo:` 技术实验
- `feat:` 新功能
- `fix:` 修复问题
- `refactor:` 重构
- `test:` 测试
- `research:` 论文/实验/科研记录

## 7. 当前阶段

> 当前目标：完成第 1-8 周基础阶段，优先打通 Python + FastAPI + LLM API + Prompt + Embedding + Tool Calling + LangGraph。
