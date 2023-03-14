---
title: lec1 - 2023春夏实用技能拾遗
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

# lec1：Shell 及部分命令行工具推荐

<hr/>

2023 年春夏学期计算机学院朋辈辅学「实用工具拾遗」课程

By [@TonyCrane](https://github.com/TonyCrane)

</div>
</div>

<!--v-->

## 本节内容

- 清楚认识什么是 Shell，什么是 Terminal
- 学会 Shell 基础命令，包括目录操作、文本编辑、重定向、管道等
- 了解 vim 编辑器的基本用法
- 了解一些常用的命令行工具
- 了解 GNU make 的基本用法

<!--s-->

<div class="middle center">
<div style="width: 100%">

# Part.1 什么是 Shell？

</div>
</div>

<!--v-->

## 什么是 Shell

- 一个黑黑的窗口？
- 一个输入奇怪命令的地方？
- 一个看起来很高级很黑客的界面？

<div class="fragment">

❌ 这些都不是 Shell ❌

</div>

<div class="fragment">

这些描述的窗口其实是 Terminal

</div>

<!--v-->

## 什么是 Terminal

- 也叫 Terminal Emulator，模拟传统终端的行为
- 一个应用程序，提供了一个窗口，和输入输出交互的功能
- 内部运行的是 Shell，Shell 才是执行命令得到输出的东西

<div class="fragment">

都有哪些常用的 Terminal 呢？

</div>

<div class="fragment">

- Windows 下：Windows Terminal（强烈推荐）
- Linux 下：Gnome Terminal、Konsole、iTerm2 等
- macOS 下：原生 Terminal、iTerm2（推荐）等
- 跨平台：
    - Warp: <https://warp.dev/>，基于 Rust
    - Hyper: <https://hyper.is/>，基于 Electron
    - ...

</div>

<!--v-->

## 那什么才是 Shell

- “壳层”，是用户与系统内核交互的界面
- 也是一个程序，负责接收命令，处理要做的工作然后交给内核来执行，并处理返回输出
    - 如何让内核执行工作？系统调用

<div class="fragment">

都有什么常用的 Shell 呢？

</div>  

<div class="fragment">

- Windows 下：cmd.exe、PowerShell（图形化 Shell）
- *nix 下：
    - **sh**：Bourne Shell，最早、最经典的 shell
    - **bash**：Bourne Again Shell，最常用的 shell，绝大部分 Linux 发行版的默认 shell
    - **zsh**：Z Shell，功能强大、可高度自定义的 shell（个人推荐）
        - 自 macOS Catalina 开始的默认 shell
    - **fish**：Friendly Interactive Shell，易用、全平台的 shell

</div>

<!--v-->

## Shell 与 Terminal

- Terminal 的任务是从用户获取输入，然后传递给 Shell，等待 Shell 执行完后，将结果再传递回用户（显示出来）
- Shell 的任务是从 Terminal 拿到输入指令，解析后交给内核执行，然后将结果返回给 Terminal

一些例子：

- macOS 下 Terminal 可以随意更换 Shell
- Ctrl-C 到底是复制还是中断程序？
    - 和 Shell 无关，是 Terminal 的行为
    - 比如 macOS 上 iTerm 就可以随意更改按键的这些行为
    - 如果定义了 ^C 应该复制，那么 Terminal 就会直接复制内容到剪贴板
    - 如果定义了 ^C 应该中断程序，那么 Terminal 就告诉 Shell，Shell 再通过 SIGINT 信号通知内核中断程序

<!--v-->

## 为什么要用命令行？它能做什么？

- 命令行就是一种操作计算机的方式，理论上可以做任何事情
- 可以让你手在键盘上就能控制电脑，而不需要鼠标拖拽等
- 在没有显示器的服务器上（例如通过 ssh 连接），只能通过命令行操作

一个夸张的例子：你甚至可以在命令行中查看网页！[fathyb/carbonyl](https://github.com/fathyb/carbonyl)

<div style="text-align: center;">
<img src="img1.png" width="65%" style="margin: 0 auto;">
</div>

<!--v-->

## *关于 zsh 的一些推荐配置

- oh-my-zsh：<https://ohmyz.sh/>，一个 zsh 的配置框架，支持主题、插件等配置
- powerlevel10k（p10k）：一个 oh-my-zsh 的主题，配置简单，好看
- 插件：
    - git：oh-my-zsh 自带插件，提供 git 相关的提示
    - zsh-autosuggestions：自动提示输入过的历史命令
    - zsh-syntax-highlighting：命令语法高亮
    - autojump：快速跳转到曾经跳转过的目录
    - ...

具体安装方法等请见：<https://note.tonycrane.cc/cs/tools/shell/>

<!--s-->

<div class="middle center">
<div style="width: 100%">

# Part.2 基础 Shell 命令

以 bash/zsh 为例

</div>
</div>

<!--v-->

## Prompt 与路径意识

- Prompt 即命令提示符，用来等待输入并给你提供一些信息
- 其中最重要的信息就是**当前路径**，也称工作路径，是当前 Shell 所处的“位置”
    - 一定要时时刻刻知道自己“在哪里”
    - 因为基本所有命令的行为都和当前路径有关
- 通常还要有的信息是当前正在操作的**用户**
    - 和权限有关，比如普通用户还是 root 等

<br/>

<div class="fragment">

- 向其中输入命令然后回车，就可以执行命令
- 输入 pwd，这个命令用来获取当前路径
    - 可见 ~ 代表的就是当前用户的 “home” 目录
- *nix 下的路径分隔符是 /，Windows 下是 \
- 而且 Windows 下有多个“根目录”，即不同“盘符”，比如 C:\、D:\ 等

</div>

<!--v-->

## 路径相关命令

- pwd：获取当前路径
- cd *path*：切换路径
    - *path* 可以是“相对路径”或者“绝对路径”
    - *path* 中 ~ 代表 home，. 代表当前路径，.. 代表上一级路径

<!--v-->

## 文件/目录操作命令

- ls：列出当前路径下的文件和目录
    - -a：列出所有文件和目录，包括隐藏文件
    - -l：列出详细信息
- touch *file*：创建一个文件
- mkdir *dir*：创建一个目录
- rm *file*：删除一个文件
    - -r：递归删除目录；-f：强制删除
- rmdir *dir*：删除一个空目录（rm -r *dir* 删除目录及其下全部内容）
- cp *src* *dst*：复制文件或目录
    - -r：递归复制目录
- mv *src* *dst*：移动文件或目录（重命名）
- find *path* -name *pattern*：在 *path* 下查找文件名匹配 *pattern* 的文件

<!--v-->

## 文件内容查看命令

- cat *file*：输出文件内容
    - -n：输出行号
- head -n *lines* *file*：输出文件前 *lines* 行
- tail -n *lines* *file*：输出文件后 *lines* 行
- more/less *file*：分页输出文件内容
    - 空格翻页，回车下一行，q 退出
    - less 的功能更多，比如查找，更好的翻页等，用法见 less --help

<!--v-->

## 其他命令

- echo：输出字符串（常配合重定向/管道使用）
- whoami：获取当前用户
- date：获取当前时间
- clear：清屏
- ps：显示进程信息
- kill：杀死进程
- man：查看 man 文档
- grep：查找文件内容（常配合重定向/管道使用）
- diff：比较文件/目录内容
- ln：创建链接
- whereis/which：查找命令所在位置
- ...

<!--v-->

## 重定向

- 即文件流重定向
- shell 中三种流：stdin 标准输入，stdout 标准输出，stderr 标准错误
- 如何更便捷地将输出存入文件/将文件内容作为程序输入？通过重定向
- 通过 > *file* 将 stdout 重定向到文件，通过 < *file* 将文件重定向到 stdin
- 通过 2> *file* 将 stderr 重定向到文件
- 两个右箭头（大于号）>> 表示追加模式，即不覆盖原文件，而是追加到文件末尾
- 通过 &> *file* 将 stdout 和 stderr 重定向到文件

<div class="fragment">

常见用法：

- echo "hello" > *file*：将字符串 hello 写入文件
- cat *file* > *file2*：将文件内容复制到另一个文件
- diff *file1* *file2* > *file3*：将 diff 的输出写入文件
- ./a.out < *file*：将文件作为程序的输入

</div>

<!--v-->

## 管道

- 通过管道（pipe）可以将一个命令的输出作为另一个命令的输入
- 使用 | 操作符，将左侧 stdout 重定向到右侧 stdin
- 通过管道可以将多个命令连接起来，形成一个命令序列，可以通过一行命令来完成相对复杂的操作（e.g. [SadServers](https://sadservers.com/) Saskatoon）
    ```bash
    $ cat /home/admin/access.log | cut -d ' ' -f 1 | sort | uniq -c | sort | tail -n 1
    482 66.249.73.135
    ```

常用搭配：

- *some command* | tail -n *lines*：只输出最后 *lines* 行
- *some command* | less：分页输出
- *some command* | grep *pattern*：在输出中查找匹配 *pattern* 的行
- 与 cut / sort / uniq / awk 等命令搭配，处理文本数据
- ...

<!--v-->

## *环境变量

TODO

<!--s-->

<div class="middle center">
<div style="width: 100%">

# Part.3 vim 基础用法

</div>
</div>

<!--v-->

## 

<!--s-->

<div class="middle center">
<div style="width: 100%">

# Part.4 GNU make

</div>
</div>

<!--v-->

##

<!--s-->

<div class="middle center">
<div style="width: 100%">

# Part.5 其他命令行工具推荐

</div>
</div>

<!--v-->

## 