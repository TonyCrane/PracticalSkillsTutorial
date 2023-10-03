# 朋辈辅学「实用技能拾遗」课程仓库

## 课程介绍

> 大学里的计算机课程通常专注于讲授从操作系统到机器学习这些学院派的课程或主题，而对于如何精通工具这一主题则往往会留给学生自行探索。在这个系列课程中，我们讲授命令行、强大的文本编辑器的使用、使用版本控制系统提供的多种特性等等。学生在他们受教育阶段就会和这些工具朝夕相处（在他们的职业生涯中更是这样）。
> 
> 因此，花时间打磨使用这些工具的能力并能够最终熟练地、流畅地使用它们是非常有必要的。
> 
> 精通这些工具不仅可以帮助您更快的使用工具完成任务，并且可以帮助您解决在之前看来似乎无比复杂的问题。
>
> <right>—— [The Missing Semester of Your CS Education](https://missing-semester-cn.github.io/)</right>

课程内容和目标类似 the missing semester，即讲授一些基础、实用但学校课程中并不会教的技能，内容难度和深度相比 the missing semester 都会有所降低，~~致力于做更适合刚入门计算机的中国宝宝的技能拾遗课程~~。

### 课程安排

课程主页：<https://slides.tonycrane.cc/PracticalSkillsTutorial/>

- 2023 年春夏学期
    - 浙江大学计算机学院朋辈辅学课程「实用技能拾遗」单周周日下午班
    - 课程材料：[`2023-spring-cs`](https://github.com/TonyCrane/PracticalSkillsTutorial/tree/2023-spring-cs) 分支
    - 课程网站：<https://slides.tonycrane.cc/PracticalSkillsTutorial/2023-spring-cs/>
    - 课程内容：(all by [@TonyCrane](https://github.com/TonyCrane/))
        - [lec1：Shell 基础及 CLI 工具推荐](https://slides.tonycrane.cc/PracticalSkillsTutorial/2023-spring-cs/lec1/)
        - [lec2：Git/GitHub 基础介绍](https://slides.tonycrane.cc/PracticalSkillsTutorial/2023-spring-cs/lec2/)
        - [lec3：Markdown 语法及应用](https://slides.tonycrane.cc/PracticalSkillsTutorial/2023-spring-cs/lec3/)
        - [lec4：LaTeX 排版简要介绍](https://slides.tonycrane.cc/PracticalSkillsTutorial/2023-spring-cs/lec4/)
- 2023 年秋冬学期
    - 浙江大学竺可桢学院学指辅学计划 程序设计精品课「实用技能拾遗」课程
    - 课程材料：[`master`](https://github.com/TonyCrane/PracticalSkillsTutorial/tree/master) 分支（当前）
    - 课程网站：<https://slides.tonycrane.cc/PracticalSkillsTutorial/2023-fall-ckc/>
    - 课程内容：
        - [lec0：前瞻：通往 Pro 的第一步](https://slides.tonycrane.cc/PracticalSkillsTutorial/2023-fall-ckc/lec0/) by [@TonyCrane](https://github.com/TonyCrane)
        - [lec1：Shell 基础及 CLI 工具推荐](https://slides.tonycrane.cc/PracticalSkillsTutorial/2023-fall-ckc/lec1/) by [@45gfg9](https://github.com/45gfg9)
        - [lec2：Git/GitHub 基础介绍](https://slides.tonycrane.cc/PracticalSkillsTutorial/2023-fall-ckc/lec2/) by [@TonyCrane](https://github.com/TonyCrane)
        - [lec3：Markdown 语法及应用](https://slides.tonycrane.cc/PracticalSkillsTutorial/2023-fall-ckc/lec3/) by [@TonyCrane](https://github.com/TonyCrane)
        - [lec4：LaTeX 排版简要介绍](https://slides.tonycrane.cc/PracticalSkillsTutorial/2023-fall-ckc/lec4/) by [@45gfg9](https://github.com/45gfg9)
        - [lec5：如何排出规范、美观的文档](https://slides.tonycrane.cc/PracticalSkillsTutorial/2023-fall-ckc/lec5/) by [@TonyCrane](https://github.com/TonyCrane)
        - [lec6：网络/网站基础知识概述](https://slides.tonycrane.cc/PracticalSkillsTutorial/2023-fall-ckc/lec6/) by [@45gfg9](https://github.com/45gfg9)

## 关于 slides
### 构建与部署

<details>
<summary>原版指南</summary>

1. 安装 reveal-md
    ```sh 
    $ npm install -g reveal-md
    ```
2. 在浏览器中实时预览
    ```sh 
    $ reveal-md main.md -w
    ```
3. 构建静态文件
    ```sh 
    $ reveal-md main.md --static site --assets-dir assets
    ```
    - 生成 pdf 版：在 url 后面加上 `?print-pdf` 使用浏览器打印
4. 部署
    - 很蠢的一个实现，总之就是用 Action 把 site 文件夹中的内容复制到我的另一个私有 repo 中，然后在那个 repo 里部署 GitHub Pages
    - 构建出 site 文件夹后 commit & push，message 需要以 `[deploy]` 开头

</details>

本课程所有 slides 都使用 reveal-md，源码都在 slides/src/ 目录中，同时包含了一个简单的 Makefile 用来更方便地预览和构建。

- 实时预览
    ```sh 
    $ make         # 仅 lec0
    $ make LECNO=1 # lec1
    ```
- 单个 slides 构建
    ```sh
    $ make build         # 仅 lec0
    $ make LECNO=1 build # lec1
    ```
- 构建全部 slides
    ```sh
    $ make all
    ``` 
- 清除全部 slides
    ```sh
    $ make clean
    ```

### 用法

和 reveal-js 的快捷键一致，在页面中按下 `?` 可以查看所有快捷键。常用的：

- N / SPACE：下一页
- P / Shift SPACE：上一页
- ← / H：翻到左边页面
- → / L：翻到右边页面
- ↑ / K：翻到上边页面
- ↓ / J：翻到下边页面
- B / .：暂停（黑屏）
- F：全屏
- ESC / O：显示概览
- S：打开演讲者窗口
