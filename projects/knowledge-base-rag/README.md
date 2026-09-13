# 企业知识库智能问答系统

## 核心目标

掌握完整 RAG Pipeline，并把“文档 → 检索 → 生成 → 来源引用”做成可运行 Web Demo。

## 核心功能

1. 上传企业 PDF / Word 文档
2. 文档解析与清洗
3. Chunk 切分
4. Embedding 向量化
5. 向量数据库入库
6. Top-K 检索
7. Rerank
8. LLM 生成答案
9. 返回引用来源
10. 提供 Web/API 接口

## 推荐目录

```text
app/
├── main.py
├── config.py
├── loader.py
├── splitter.py
├── embedding.py
├── vector_store.py
├── retriever.py
├── reranker.py
└── rag.py
```

## 验收标准

- 可运行 Web Demo
- 支持文档上传和问答
- 回答带来源引用
- 有 Chunk / 检索 / Rerank 对比实验
- 完成 RAG 优化实验报告
