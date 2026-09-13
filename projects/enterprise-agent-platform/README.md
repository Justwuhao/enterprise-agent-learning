# 企业智能体综合平台

## 核心目标

把前面项目中的能力统一到一个可复用的企业智能体平台 MVP。

## 核心模块

- 知识库管理
- Agent 管理
- Tool 管理
- Workflow 管理
- 会话管理
- 用户与权限
- 日志与 Trace
- 评测
- Docker 部署

## 推荐架构

```text
Web UI
  ↓
FastAPI
  ↓
Agent Workflow
  ├── Knowledge Base / RAG
  ├── Tools
  ├── Memory
  └── Multi-Agent
  ↓
PostgreSQL + Redis
  ↓
LLM / Model Service
```

## 验收标准

- 企业智能体平台 MVP
- 完整 README
- 系统架构图
- 技术报告
- 可部署演示版本
