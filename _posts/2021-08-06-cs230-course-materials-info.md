---
title: 斯坦福CS230深度学习-课程学习资料
subtitle: 斯坦福CS230深度学习课程，内容覆盖卷积神经网络、循环神经网络、网络训练技巧与经验等
author: HanXinzi@ShowMeAI
author_url: https://github.com/HanXinzi-AI
categories: [AI课程]
tags: [cs229, machine learning, AI课程]
pin: false
---

<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link href='https://fonts.googleapis.com/css?family=Inconsolata:400,700' rel='stylesheet' type='text/css'>
<link rel="stylesheet" href="/assets/vendor/normalize-css/normalize.css">
<link rel="stylesheet" href="/css/main.css">
<link rel="stylesheet" href="/assets/vendor/highlight/styles/solarized_dark.css">
<link rel="stylesheet" href="/assets/vendor/font-awesome/css/font-awesome.css">
<link rel="shortcut icon" href="/favicon.ico"/>

## 课程介绍
课程主页：[CS230: Deep Learning](http://cs230.stanford.edu/)

深度学习是AI领域中最受欢迎的技能之一，斯坦福CS230深度学习课程由吴恩达教授和他的助教Kian Katanforoosh讲授。课程内容覆盖：深度学习的基础，理解如何构建神经网络，卷积神经网络（CNN）、循环神经网络（RNN）、长短期记忆网络（LSTM）、Adam 优化器、Dropout 方法、BatchNorm 方法、Xavier/He 初始化方法等。课程也涉及了深度学习在医疗、自动驾驶、手语识别、音乐生成和自然语言处理等领域的应用案例。

## 前置课程
学生应具有以下背景：

- 掌握计算机科学基本原理和技能，编程能力达到一个水平足以编写一个相对比较复杂的计算机程序 Python/Numpy （CS106A、CS106B、CS106X）。
- 熟悉概率理论（CS 109、MATH151 或 STAT116）。
- 熟悉多变量微积分和线性代数。包括但不限于 MATH51、MATH104、MATH113、CS205、CME100）。

<hr />
<h2 id="ShowMeAI课程解读">ShowMeAI课程解读：全套资料</h2>
<div align="center">
<img src="http://ww1.sinaimg.cn/large/0060yMmAly1gt813qif68j31kx0fuqia.jpg" referrerpolicy="no-referrer" width = "100%" />
</div>


## 课程速查表 | [【点击链接】](http://blog.showmeai.tech/cs230/cheatsheet-slides)
<div align="center">
<img src="http://ww1.sinaimg.cn/large/0060yMmAly1gt81bppeltg30mw0hbnpg.gif" referrerpolicy="no-referrer" width = "100%"/>
</div>


## 课程重点笔记 | 【点击板块】

<style>
#customers {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 80%;
}

#customers td, #customers th {
  border: 2px solid #ddd;
  padding: 8px;
}

#customers tr:nth-child(even){background-color: #f2f2f2;}

#customers tr:hover {background-color: #ddd;}

#customers th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #F5B041;
  color: white;
}
</style>

<table id="customers" align="center">
  <tr>
    <th>板块编号</th>
    <th>笔记链接</th>
  </tr>
  <tr>
    <td>板块1</td>
    <td><a href="/cs230/CNN">卷积神经网络</a></td>
</tr>
<tr>
    <td>板块2</td>
    <td><a href="/cs230/RNN">循环神经网络</a></td>
</tr>
<tr>
    <td>板块3</td>
    <td><a href="/cs230/DL-Tips-and-Tricks">深度学习技巧与经验</a></td>
</tr>
</table>


## 课程作业 |【作业代码解析】|【点击编号】
<div align="center">
<img src="http://ww1.sinaimg.cn/large/0060yMmAly1gsvjfay0q5g313m0hmk1z.gif" referrerpolicy="no-referrer" width = "100%" />
</div>
<table id="customers" align="center">
  <tr>
    <th>作业编号</th>
    <th>solution地址</th>
  </tr>
  <tr>
      <td>第1门-作业1</td>
      <td><a href="https://github.com/ShowMeAI-Hub/awesome-AI-courses-notes-cheatsheets/tree/main/CS230-Deep-Learning/assignment-solutions/Assignment1">无作业</a></td>
  </tr>
  <tr>
      <td>第1门-作业2</td>
      <td><a href="https://github.com/ShowMeAI-Hub/awesome-AI-courses-notes-cheatsheets/tree/main/CS230-Deep-Learning/assignment-solutions/Assignment1">神经网络基础</a></td>
  </tr>
  <tr>
      <td>第1门-作业3</td>
      <td><a href="https://github.com/ShowMeAI-Hub/awesome-AI-courses-notes-cheatsheets/tree/main/CS230-Deep-Learning/assignment-solutions/Assignment1">浅层神经网络</a></td>
  </tr>
  <tr>
      <td>第1门-作业4</td>
      <td><a href="https://github.com/ShowMeAI-Hub/awesome-AI-courses-notes-cheatsheets/tree/main/CS230-Deep-Learning/assignment-solutions/Assignment1">深层神经网络</a></td>
  </tr>
  <tr>
      <td>第2门-作业1</td>
      <td><a href="https://github.com/ShowMeAI-Hub/awesome-AI-courses-notes-cheatsheets/tree/main/CS230-Deep-Learning/assignment-solutions/Assignment2">神经网络实践(初始化、正则化、梯度检查)</a></td>
  </tr>
  <tr>
      <td>第2门-作业2</td>
      <td><a href="https://github.com/ShowMeAI-Hub/awesome-AI-courses-notes-cheatsheets/tree/main/CS230-Deep-Learning/assignment-solutions/Assignment2">神经网络优化算法</a></td>
  </tr>
  <tr>
      <td>第2门-作业3</td>
      <td><a href="https://github.com/ShowMeAI-Hub/awesome-AI-courses-notes-cheatsheets/tree/main/CS230-Deep-Learning/assignment-solutions/Assignment2">超参数调优、BN与Tensorflow实践</a></td>
  </tr>
  <tr>
      <td>第3门-作业</td>
      <td><a href="https://github.com/ShowMeAI-Hub/awesome-AI-courses-notes-cheatsheets/tree/main/CS230-Deep-Learning/assignment-solutions/Assignment3">无作业</a></td>
  </tr>
  <tr>
      <td>第4门-作业1</td>
      <td><a href="https://github.com/ShowMeAI-Hub/awesome-AI-courses-notes-cheatsheets/tree/main/CS230-Deep-Learning/assignment-solutions/Assignment4">卷积神经网络基础</a></td>
  </tr>
  <tr>
      <td>第4门-作业2</td>
      <td><a href="https://github.com/ShowMeAI-Hub/awesome-AI-courses-notes-cheatsheets/tree/main/CS230-Deep-Learning/assignment-solutions/Assignment4">深度卷积神经网络</a></td>
  </tr>
  <tr>
      <td>第4门-作业3</td>
      <td><a href="https://github.com/ShowMeAI-Hub/awesome-AI-courses-notes-cheatsheets/tree/main/CS230-Deep-Learning/assignment-solutions/Assignment4">目标检测实现</a></td>
  </tr>
  <tr>
      <td>第4门-作业4</td>
      <td><a href="https://github.com/ShowMeAI-Hub/awesome-AI-courses-notes-cheatsheets/tree/main/CS230-Deep-Learning/assignment-solutions/Assignment4">图像风格转换与人脸识别</a></td>
  </tr>
  <tr>
      <td>第4门-作业1</td>
      <td><a href="https://github.com/ShowMeAI-Hub/awesome-AI-courses-notes-cheatsheets/tree/main/CS230-Deep-Learning/assignment-solutions/Assignment5">循环神经网络与LSTM</a></td>
  </tr>
  <tr>
      <td>第4门-作业2</td>
      <td><a href="https://github.com/ShowMeAI-Hub/awesome-AI-courses-notes-cheatsheets/tree/main/CS230-Deep-Learning/assignment-solutions/Assignment5">自然语言处理与词嵌入</a></td>
  </tr>
  <tr>
      <td>第4门-作业3</td>
      <td><a href="https://github.com/ShowMeAI-Hub/awesome-AI-courses-notes-cheatsheets/tree/main/CS230-Deep-Learning/assignment-solutions/Assignment5">序列模型与注意力机制</a></td>
  </tr>
</table>


<div align="center">
<img src="http://ww1.sinaimg.cn/large/0060yMmAly1gt813qbj1mj31kx0fugtn.jpg" referrerpolicy="no-referrer" width = "100%" alt="end" align=center />
</div>

## 更多技术与课程清单 | 点击查看详细课程
<style>
#customers {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 80%;
}

#customers td, #customers th {
  border: 2px solid #ddd;
  padding: 8px;
}

#customers tr:hover {background-color: #ddd;}

#customers th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #F5B041;
  color: white;
}

</style>

<table id="customers" align="center">
  <tr>
      <th>技术方向</th>
      <th>课程及链接</th>
    </tr>
    <tr>
        <td >机器学习</td>
        <td><a href="/cs229">斯坦福CS229</a></td>
    </tr>
    <tr>
        <td >深度学习</td>
        <td><a href="/cs230">斯坦福CS230</a></td>
    </tr>
    <tr>
        <td rowspan="3">自然语言处理</td>
        <td><a href="/cs224n">斯坦福CS224n（深度学习与NLP）</a></td>
    </tr>
    <tr>
        <td><a href="/cs520">斯坦福CS520（知识图谱）</a></td>
    </tr>
    <tr>
        <td><a href="/cs124">斯坦福CS124（从语言到信息）</a></td>
    </tr>
    <tr>
        <td rowspan="3">计算机视觉</td>
        <td><a href="/cs231n">斯坦福CS231n（深度学习与CV）</a></td>
    </tr>
    <tr>
        <td><a href="/eecs498">密歇根eecs498（CS231n进阶课）</a></td>
    </tr>
    <tr>
        <td><a href="/adl4cv">慕尼黑工大adl4cv（深度学习与CV高阶课）</a></td>
    </tr>
    <tr>
      <td >图机器学习</td>
        <td><a href="/cs224w">斯坦福CS224w</a></td>
    </tr>
    <tr>
        <td rowspan="2">强化学习</td>
        <td><a href="/cs234">斯坦福CS234（强化学习）</a></td>
    </tr>
    <tr>
        <td><a href="/cs285">伯克利CS285（深度强化学习）</a></td>
    </tr>
    <tr>
      <td>无监督学习</td>
        <td><a href="/cs294-158">伯克利CS294-158（深度无监督学习）</a></td>
    </tr>
</table>

<div align="center">
<img src="http://ww1.sinaimg.cn/large/0060yMmAly1gt813qqfpvj31kx0funp9.jpg" referrerpolicy="no-referrer" width = "100%" alt="end" align=center />
</div>