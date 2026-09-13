# 企业数据分析 Agent

## 核心目标

将自然语言问题转为安全 SQL，再执行数据分析和结果生成。

## 核心流程

自然语言 → Schema 理解 → SQL 生成 → SQL 安全检查 → PostgreSQL 查询 → 指标计算 → 图表/报告 → 自然语言结论

## 核心功能

- Text-to-SQL
- PostgreSQL 查询
- 只读权限
- SQL LIMIT
- SQL 超时
- SQL 安全检查
- Pandas 数据分析
- Matplotlib/前端图表
- 自动生成业务分析报告

## 验收标准

- 完成 NL2SQL Demo
- 完成安全版 NL2SQL
- 至少 30 条评测问题
- 统计准确率与执行成功率
