# 企业流程自动化 Agent

> 文档规划中的“项目 2：企业流程自动化 Agent”。这里使用 ticket-agent 作为工程目录名，后续也可以改成更贴近具体业务的名称。

## 核心目标

掌握 LangGraph、Tool Calling 和企业 Workflow，把自然语言需求转成可执行的业务流程。

## 示例场景

以出差、报销、请假等企业流程为例。

## 核心功能

1. 意图识别
2. 制度查询
3. 参数收集与校验
4. 工具调用
5. 流程状态管理
6. 人工确认
7. 错误重试
8. Agent Trace

## 至少 3 个工具

- `query_policy`：查询企业制度
- `create_application`：创建申请
- `check_application`：查询申请状态

## 验收标准

- 至少 3 个可调用工具
- 能展示完整 Agent Trace
- 完成至少 10 个测试案例
- 有架构图和技术文档
