---
title: lec2 - 2023春夏实用技能拾遗
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

# lec2：Git&hairsp;&hairsp;/&hairsp;&hairsp;GitHub 基础介绍

<hr/>

2023 年春夏学期计算机学院朋辈辅学「实用工具拾遗」课程

By [@TonyCrane](https://github.com/TonyCrane)

<div style="text-align: right; margin-top: 1em;">
<p>2023.4.2&emsp;&emsp;&emsp;</p>
</div>

</div>
</div>

<!--v-->

## 本节内容

- Git
    - Git 基础：文件管理、提交 commit、分支 branch、合并 merge
    - Git 进阶：修改历史、变基 rebase、远程版本库
    - *略讲内容：钩子 hook、子模块 submodule
- GitHub
    - GitHub 基本操作概述
    - issue 与 pull request
    - *略讲内容：GitHub Pages、GitHub Actions

（不会讲解 Git 安装、稳定访问 GitHub 等内容）

<!--v-->

## 如何自学本章节内容

<img style="float: right" width="25%" src="lec2/gitbook.jpg"/>

- 《Git 版本控制管理》[ISBN 978-7-115-38243-6](http://oreilly.com.cn/index.php?func=book&isbn=978-7-115-38243-6)
    - [*Version Control with Git*](https://www.oreilly.com/library/view/version-control-with/9780596158187/), Jon Loeliger
- *Pro Git (2nd Edition)*, Scott Chacon, et al.
    - https://git-scm.com/book/zh/v2
    - https://git-scm.com/book/en/v2
- Git Reference: https://git-scm.com/docs
- [git-flight-rules](https://github.com/k88hudson/git-flight-rules/blob/master/README_zh-CN.md)
- 实操❗️实操❗️一定要实操❗️❗️
    - [Learning Git Branching](https://learngitbranching.js.org/?locale=zh_CN)
    - [Gazler/githug](https://github.com/Gazler/githug)

<!--s-->

<div class="middle center">
<div style="width: 100%">

# Part.1 什么是 Git？

</div>
</div>

<!--v-->

## 什么是 Git？

- 分布式版本控制系统（DVCS，Distributed Version Control System）
    - 分布式：不需要联网，在自己的机器上就可以使用
    - 版本控制：记录、管理、回溯文件的修改历史
- 官网：https://git-scm.com/
- 和其他版本控制系统相比的优点：开源、快速、分布式、基于内容、分支管理……

<!--v-->

## Git 模型



<!--v-->

## Git 基础配置

- git init
- git config

<!--s-->

<div class="middle center">
<div style="width: 100%">

# Part.2 Git 基础用法

</div>
</div>

<!--v-->

## 文件暂存

- git add
- git rm
- git mv
- git status
- Tracked / Ignored / Untracked
    - .gitignore

<!--v-->

## 提交更改

- git commit
    - commit message
- git log
- sha1 / ref / ^~
- git checkout
    - detached HEAD

<!--v-->

## 分支

- git branch
    - git show-branch
- git checkout
- git diff

<!--v-->

## 合并

- git merge
- merge conflict
- git merge-base (?)
- merge commit
    - fast-forward / already up-to-date (?)
- squash merge
- -> GitHub

<!--s-->

<div class="middle center">
<div style="width: 100%">

# Part.3 Git 进阶用法

</div>
</div>

<!--v-->

## 修改提交历史

- git reset (soft/mixed/hard)
- git revert
- git commit --amend

<!--v-->

## rebase 变基

- git rebase -i
    - pick edit squash drop

<!--v-->

## 远程版本库

- 远程版本库概念/模型
- 裸版本库/权威版本库
- git remote 设置
- git push
- git fetch / git pull
- non-fast-forward
- -> GitHub

<!--v-->

## *hooks 钩子

- .git/hooks
- pre-commit prepare-commit-msg commit-msg post-commit
- pre-receive update post-receive post-update
- git help hooks

<!--v-->

## *submodule 子模块

- git submodule add
- git submodule update
- git submodule status

<!--s-->

<div class="middle center">
<div style="width: 100%">

# Part.4 GitHub 基本操作与项目协作

</div>
</div>

<!--v-->

## GitHub 基本操作

- 用户、邮箱配置，与 git config 配合的必要性
- repo
    - 创建
    - star watch fork
    - public / private
    - 权限管理
    - 分支
    - release

<!--v-->

## GitHub 项目协作

- issue / discussion
- pull request
    - 如何开？都有什么规范，什么注意事项？
    - 什么是 review？
    - 如何 merge？

<!--s-->

<div class="middle center">
<div style="width: 100%">

# Part.5 GitHub 进阶用法

</div>
</div>

<!--v-->

## *GitHub Pages

- Pages 原理
- Pages 设置，自定义域名

<!--v-->

## *GitHub Actions

- 什么是 Actions，什么是 CI，有什么用？
- workflow 怎么编写
- 看文档 / 在尝试中学习

<!--v-->

## *签署 commit

- 使用 GPG 签署 commit
- 为什么推荐签署 commit

<!--s-->

<div class="middle center">
<div style="width: 100%">

# Part.6 Git 相关工具/资源

</div>
</div>

<!--v-->

## Git 相关工具/资源

Git 相关工具

- gitui
- lazygit
- gitoxide

Git 学习资源

- 《Git 版本控制管理》[ISBN 978-7-115-38243-6](http://oreilly.com.cn/index.php?func=book&isbn=978-7-115-38243-6)
    - [*Version Control with Git*](https://www.oreilly.com/library/view/version-control-with/9780596158187/), Jon Loeliger, et al.
- *Pro Git (2nd Edition)*, Scott Chacon, et al.
    - https://git-scm.com/book/zh/v2
- [git-flight-rules](https://github.com/k88hudson/git-flight-rules/blob/master/README_zh-CN.md)
- [Learning Git Branching](https://learngitbranching.js.org/?locale=zh_CN)
- [Gazler/githug](https://github.com/Gazler/githug)

<!--s-->

<div class="middle center">
<div style="width: 100%">

# 谢谢大家

<hr/>

**Questions?**

</div>
</div>