---
title: lec3 - 2023春夏实用技能拾遗
separator: <!--s-->
verticalSeparator: <!--v-->
theme: simple
highlightTheme: github
css: custom.css
revealOptions:
    transition: 'slide'
    transitionSpeed: fast
    center: false
    slideNumber: "c/t"
    width: 1000
---

<div class="middle center">
<div style="width: 100%">

<img src="logo.png" style="margin-bottom: 1em">

# lec3：Markdown 语法及应用

<hr/>

2023 年春夏学期计算机学院朋辈辅学「实用工具拾遗」课程

By [@TonyCrane](https://github.com/TonyCrane)

<div style="text-align: right; margin-top: 1em;">
<p>2023.4.16&emsp;&emsp;&emsp;</p>
</div>

</div>
</div>

<!--v-->

## 本节内容

- 什么是 Markdown？它的本质是什么？
- Markdown 语法概览
    - 基于 CommonMark 的语法标准概览
- 其它 MarkUp 语言的快速简介
    - reStructuredText
    - AsciiDoc
- 支持 Markdown 的实用工具介绍
    - 文档编写：vscode mpe 插件、Marktext...
    - 网站建设：mkdocs、hexo、sphinx...

（更多关于如何规范编写文档、如何美化 markdown 主题等内容，将在后续课程中讲解）

<!--v-->

## 我想让你 take-away 的内容

- Markdown 的本质？
- Markdown 的“标准”语法？
- Markdown != Typora！还有更多更好用的开源工具！
- 除此之外还有其它文本标记语言，速通了解一下
- 基于 Markdown 的更多好用网站建设工具

<!--v-->

## 如何自学本章节内容



<!--s-->

<div class="middle center">
<div style="width: 100%">

# Part.1 什么是 Markdown？

</div>
</div>

<!--v-->

## Markdown 诞生历史

> John Gruber:  
> &nbsp;&nbsp;Markdown is intended to be as easy-to-read and easy-to-write as is feasible.

- 2004 年 John Gruber 发布了第一个 markdown 语法手册和 perl 语言写的转换器
    - [daringfireball.net/projects/markdown](https://daringfireball.net/projects/markdown)
- 以易读易写为目标，成为了电子邮件标记格式惯例
- 2016 年正式注册了 CommonMark（标准化）、GFM（GitHub 风格）等变体

<!--v-->

## 什么是 Markdown

- 是一种轻量级文本标记语言（markup language）
- 可以通过纯文本来表示带有格式的文档，同时保证易读性
- 语法简单，易于学习，易于使用
- 可以轻松转换为 HTML（映射到 HTML 的子集）
    - markdown 的**本质**实际上是对 HTML 各种标签的一种简化

<div class="mul-cols">
<div class="col">

```markdown
# This is a heading
## This is a sub-heading

This is a paragraph. and:  

- *emphasis* 
- **strong importance**
- `code`
- [links](some/url)
```

</div>

<div class="col">

```html
<h1>This is a heading</h1>
<h2>This is a sub-heading</h2>
<p>This is a paragraph. and:</p>
<ul>
<li><em>emphasis</em></li>
<li><strong>strong importance</strong></li>
<li><code>code</code></li>
<li><a href="some/url">links</a></li>
</ul>
```

</div>

</div>

<!--v-->

## 各种语法标准……？

为什么会有人觉得 markdown 语法有些混乱？

- John Gruber 所规定的语法过于简单，具体实现都没有明确规定
- 因此诞生了很多不同的标准，甚至各个软件、解析器都会有自己的实现
- 试图统一？有些困难，但不是没有成果，比如 CommonMark 规范

常见的规范都有什么？在哪里能看到呢？

- John Gruber 的最初始语法：[daringfireball.net/projects/markdown](https://daringfireball.net/projects/markdown)
- CommonMark 标准，实现细节更明确：[spec.commonmark.org](https://spec.commonmark.org/0.30/)
- 各个软件/网站自己的规范文档：
    - GitHub GFM 规范：[github.github.com/gfm](https://github.github.com/gfm/)（改自 CommonMark）
    - Pandoc 规范：[pandoc.org/MANUAL.html#pandocs-markdown](https://pandoc.org/MANUAL.html#pandocs-markdown)
    - Typora 规范：[support.typora.io](https://support.typora.io/Markdown-Reference/)（效仿 GFM，但实际有些混乱）
    - ...

<!--v-->

## 学习用软件

（更多长期使用的软件推荐在后面章节再说）

- 裸的 markdown 解析器（如果你熟悉 HTML 语法）
    - [markdown-it](https://github.com/markdown-it/markdown-it)：完美支持 CommonMark 的解析器
    - [markdown-it-py](https://github.com/executablebooks/markdown-it-py)：Python 版本，带有命令行工具
    - [python-markdown](https://github.com/Python-Markdown/markdown/)：更传统的 Python 版本解析器（标准不清晰）
    - [pandoc](https://pandoc.org/)：支持多种格式的转换器，但有自己的一套标准
- 所见即所得的 markdown 编辑器
    - [vscode mpe extension](https://marketplace.visualstudio.com/items?itemName=shd101wyy.markdown-preview-enhanced)：VSCode 的插件，支持实时预览
    - [Mark Text](https://marktext.app/)：开源 markdown 编辑器
    - [obsidian](https://obsidian.md/) 等笔记软件也支持 markdown
    - ~~[Typora](https://typora.io/)~~：闭源付费编辑器，用户多但我不推荐

<!--s-->

<div class="middle center">
<div style="width: 100%">

# Part.2 Markdown 语法概览

基于 CommonMark 标准的语法概览

</div>
</div>

<!--v-->

## 标题语法

<div class="mul-cols">
<div class="col">

- 井号 # 开头，后接内容
- 井号与标题间至少一个空格
- 只有 1～6 级标题，7 及以上不会变成标题格式
- 转为 html 利用 h1 ~ h6 tag
- 内容后面可以接任意多 # 来 “闭合”
- 可以跨过某一级，但不推荐
    - 请明确好层级关系

</div>

<div class="col">

```markdown
# 一级标题
## 二级标题
### 三级标题
#### 四级标题
##### 五级标题
###### 六级标题
```
```html
<h1>一级标题</h1>
<h2>二级标题</h2>
<h3>三级标题</h3>
<h4>四级标题</h4>
<h5>五级标题</h5>
<h6>六级标题</h6>
```

</div>

</div>

<!--v-->

## *标题语法（Setext 式）

<div class="mul-cols">
<div class="col">

- 使用 # 的称为 ATX 样式
- markdown 支持另一种称为 Setext 样式的标题
- 文字下方加任意多 = 表示一级标题
- 文字下方加任意多 - 表示二级标题

</div>
<div class="col">

```markdown
一级标题
=======

二级标题
-------
```
```html
<h1>一级标题</h1>
<h2>二级标题</h2>
```

</div>

</div>

<!--v-->

## 段落语法

- 直接编写文本即为普通段落
- 段落间通过空行来分割（有空行就有新的段落）
- 段落内换行需要在行尾加两个空格（`<br/>`）
    - 没有空格则源码内两行内容会合并为一行（并加一个空格）
- 关于换行：
    - 要搞清楚不同段落和同一段落内不同行的区别
    - CommonMark 是如上要求
    - 有些软件的规范会认为段落内的换行不需要两个空格
- 关于空格：
    - 多个连续的空格会被解析为一个空格
    - 但是在代码块中，空格会被保留
    - 使用多个空格可以使用 `&nbsp; &emsp;` 等 HTML 语法

<!--v-->

## 引言

<div class="mul-cols">
<div class="col">

- 一个 > 加一个空格后接内容
- 内部可以嵌套使用 markdown 语法
    - 可以嵌套任意多层引言
- 连续的 > 行属于同一个引言块
- 需要一个空行来退出环境
- 软件里一般使用一次 enter 退出一层

</div>
<div class="col">

```markdown
> ## Quote
> 第二行
> > 第二层
> 
> 回到第一层

退出引言
```

</div>

</div>

<!--v-->

## 无序列表

<div class="mul-cols">
<div class="col">

- `- + *` 后接一个空格然后接内容
- 同一个层级的符号要相同
- 如果一个项中要包含内容，需要换一行然后加一次缩进
- 嵌套列表直接缩进一次即可

</div>
<div class="col">

```markdown
- node 1
- node 2

  content in node 2
- node 3

* 第一层
    + 第二层
        * 第三层
    + 第二层
* 第一层
```

</div>
</div>

<!--v-->

## 有序列表

<div class="mul-cols">
<div class="col">

- 数字加点 后接空格 再接内容
    - 也可以数字加 ) 后接空格 再接内容
- 标准的 md 完全无视数字内容，所有有序列表都从 1 开始计数
- 但一般软件都会处理起始数字
- 有序列表可以和无序列表互相嵌套

</div>
<div class="col">

```markdown
1. node 1
2. node 2
4. node 3
1. node 4

1. 有序 
    - 嵌套无序
    - 嵌套无序
2. 有序
```

</div>

</div>

<!--v-->

## 分割线

<div class="mul-cols">
<div class="col">

- 使用 `* - _` 中任意一个字符重复至少三次
- 可以有空格分隔，甚至组织成不同样式
- 被转换为 html 中的 \<hr/>
- 分割线上下最好都加空行
- 特别记住 - 分割线上方不要有文字（Setext 标题）

</div>
<div class="col">

```text
***

* * *
_  __  _  __

----------------
```

</div>

</div>

<!--v-->

## 代码块

<div class="mul-cols">
<div class="col">

- 缩进形式
    - 空行加一个缩进创建一个代码块
    - 内部被原样展现
    - 软件不会进行代码高亮
- 篱笆形式
    - 使用三个或以上 ` 或 ~ 围起来构成代码块
    - ` 或 ~ 后面可以加语言名称
        - 带有高亮支持的软件会对其进行高亮显示
        - 不加（或加 text）不进行高亮

</div>
<div class="col">

~~~markdown
code block:

    print("hello world")
    # line 2

out

```c
#include <stdio.h>

int main() {
    printf("hello world\n");
    return 0;
}
```
~~~

</div>

</div>

<!--v-->

## 行内标记

<div class="mul-cols">
<div class="col">

- 格式见右侧，* 和 _ 等效
- 下划线无 markdown 语法，可以直接使用 html 的 \<u> tag 来实现
- 行内标记都可以互相嵌套
    - 也可以嵌套在其它块中
    - 行内代码中不行
- 最好在标记左右均加空格
- 文字中使用 * 建议加上 \ 转义

</div>
<div class="col">

```markdown
*斜体* _也是斜体_ \*这不是斜体\*
**粗体** __也是粗体__
***粗斜体*** ___也是粗斜体___
`行内代码`
~~删除线~~
<u>下划线</u>
```
```html
<em>斜体</em>
<strong>粗体</strong>
<code>行内代码</code>
<del>删除线</del>
```

</div>

</div>

<!--v-->

## 插入图片

<div class="mul-cols">
<div class="col">

- 感叹号-方括号-圆括号结合的形式
- 图片名可以省略
- 位置可以是链接，也可以是本地文件路径
- 常规 md 语法插入图片无法调大小，使用 html img 的 style 可以调节
- 软件一般可以帮你保存图片到某一目录
- 记住图片不会嵌入 md 文件中，要交给别人 md 文件的话请附带上所有素材文件

</div>
<div class="col">

```markdown
![图片名](图片位置)

![](图片位置)

<img src="图片位置" alt="图片名" 
    style="..."/>
```

</div>

</div>

<!--v-->

## 插入链接

<div class="mul-cols">
<div class="col">

- 方括号-圆括号组合
- 文字是要显示的内容，链接附加在其上
- 文字中可以嵌套行内标记格式
- 链接左右加 <> 自动链接

</div>
<div class="col">

```markdown
[文字](链接)

<链接>
等价于 [链接](链接)
```
```html
<a href="链接">文字</a>
```

</div>

</div>

<!--v-->

## 内联 HTML 语法

- markdown 中一般可以直接使用 html 语法和 css 样式
- 解析器会原封不动的保留 html 内容
- 文本中使用 \<tag\> 这样的字样需要用 \ 转义
- GitHub（GFM）仅支持少量 html，且不支持 css 样式
- html 语法不赘述

<!--v-->

## 表格

<div class="mul-cols">
<div class="col">

- 不在标准中，但一般这样使用
- 每个单元格的内容用 | 分开
    - 内容中使用 | 要用 \ 转义
- 第二行一定要有，规定整列对齐方式
    - `|--|` 或 `|:--|` 左对齐
    - `|--:|` 右对齐
    - `|:--:|` 居中对齐
    - `-` 的个数随意
- 仅可以处理简单表格，复杂的用 html 插入
- 推荐 [tablesgenerator.com](https://www.tablesgenerator.com/)

</div>
<div class="col">

```markdown
|表头|表头|表头|
|:--|:--:|--:|
|居左|居中|居右|
|abcde|fghij|klmno|
|.......|.......|.......|
```

<style>
section > .mul-cols > .col > table {
  border: 1.5pt solid;
  text-align: center;
  page-break-inside: avoid;
}
section > .mul-cols > .col > table > tbody > tr > td {
  border: 0.75pt solid;
  padding: 7px;
}
section > .mul-cols > .col > table > tbody > tr {
  border: 0.75pt solid;
  padding: 7px;
}
section > .mul-cols > .col > table > thead {
  border: 0.75pt solid;
  font-size: 0.9em;
}
section > .mul-cols > .col > table th {
  border: 0.75px solid;
}
</style>

|表头|表头|表头|
|:--|:--:|--:|
|居左|居中|居右|
|abcde|fghij|klmno|
|.......|.......|.......|

</div>

</div>

<!--s-->

<div class="middle center">
<div style="width: 100%">

# Part.3 其它 MarkUp 语言简介

</div>
</div>

<!--v-->

## 什么是 MarkUp 语言？




<!--s-->

<div class="middle center">
<div style="width: 100%">

# Part.4 支持 Markdown 的实用工具

</div>
</div>

<!--v-->


<!--s-->

<div class="middle center">
<div style="width: 100%">

# 总结

</div>
</div>

<!--v-->

## take-away？



<!--v-->

<div class="middle center">
<div style="width: 100%">

# 谢谢大家

<hr/>

**Questions?**

</div>
</div>