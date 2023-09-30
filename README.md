# Indent Headers in Markdown files
我们在石墨文档中记录每个人的论文阅读记录。
对于同一篇论文，我们以每个人的名字作为一级标题，导致自己的Md文档中不可以出现一级标题。
(这种方式确实有些拉胯，而且石墨文档并不完全支持Markdown，哈人)

## 使用方法
```
python indent.py file_path
```

## Tips
石墨文档会把'>'后面所有的行都转换成markdown的阅读模式的开头有'>'的样子。
所以indent.py会在每一行以'>'开头且下一行不以'>'开头的行后面添加一个空行来避免这一点。
