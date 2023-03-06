---
title: Slide 模板
separator: <!--s-->
verticalSeparator: <!--v-->
theme: simple
highlightTheme: monokai-sublime
css: 
    - custom.css
    - dark.css
revealOptions:
    transition: 'slide'
    transitionSpeed: fast
    center: false
    slideNumber: "c/t"
    width: 1000
---

<div class="middle center">
<div style="width: 100%">

# Slide 模版

<hr/>

By [@TonyCrane](https://github.com/TonyCrane)



</div>
</div>

<!--s-->

<div class="middle center">
<div style="width: 100%">

# Part.1 大标题

一些 markdown

</div>
</div>


<!--v-->

## 标题

> test

<hr/>

```rust [1|2-3]
fn main() {
    println!("Hello World!")
}
```

...

- list 1
- list 2
    - list 2.1

1. 有序

<!--v-->

## 标题

<div class="three-line">

|表头 a|表头 b|表头 c|
|:--:|:--:|:--:|
|这是一个|一些内容|...|
|三线表|...|...|

</div>

|表头 a|表头 b|表头 c|
|:--:|:--:|:--:|
|这是一个|一些内容|...|
|普通表格|...|...|

<!--s-->

<div class="middle center">
<div style="width: 100%">

# Part.2 布局

</div>
</div>

<!--v-->

## 多列布局

<div class="mul-cols">
<div class="col">

第一列

- list
- list

</div>
<div class="col">

第二列

```python
class MyClass:
    def __init__(self, ...):
        ...
    def method(self, ...):
        ...
```

</div>
</div>

<div class="mul-cols">
<div class="col">

第一列

- list
- list

</div>
<div class="col">

第二列

1. list 
2. list 
    - list

</div>
<div class="col">

第三列

```python
class MyClass:
    def __init__(self, ...):
        ...
    def method(self, ...):
        ...
```

</div>
</div>