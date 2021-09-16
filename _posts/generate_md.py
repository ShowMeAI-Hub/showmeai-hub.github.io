#conding=utf8  
import os,sys

for line in open(sys.argv[1]):
    fname, img, title, keywords, des = line.strip().split("\t")
    out = open(fname, 'w')
    subtitle = title.strip("-学习资料")+"课程，内容覆盖"+keywords.replace(",","、")+"等"
    tags = "[" + keywords.replace(",", ", ") + "]"

    content = '''---
title: {name}
subtitle: {subname}
author: 韩信子
author_url: https://github.com/HanXinzi-AI
categories: [AI课程]
tags: {tag}
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

'''.format(name=title, subname=subtitle, tag = tags)
    out.write(content)

    content = '''## 课程介绍

<div align="center">
<img src="http://image.showmeai.tech/course/{image}-1.png" width = "100%" />
</div>

{description}

'''.format(description=des, image=img)

    out.write(content)

    content = '''<hr />
<h2 id="ShowMeAI课程解读">ShowMeAI课程解读：全套资料</h2>
<div align="center">
<img src="http://image.showmeai.tech/course/{image}-2.png" width = "100%" />
</div>'''.format(image=img)+'''
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
        <td rowspan="5">计算机数学基础</td>
        <td><a href="/mit-6.042j">MIT-计算机科学的数学基础</a></td>
    </tr>
    <tr>
        <td><a href="/uc-math100">辛辛那提大学-微积分I</a></td>
    </tr>
    <tr>
        <td><a href="/uc-math101">辛辛那提大学-微积分II</a></td>
    </tr>
    <tr>
        <td><a href="/uc-math1071">辛辛那提大学-离散数学</a></td>
    </tr>
    <tr>
        <td><a href="/stanford-engr108">斯坦福-线性代数与矩阵方法导论</a></td>
    </tr>
    <tr>
        <td rowspan="3">计算机科学导论</td>
        <td><a href="/stanford-cs105">斯坦福-计算机科学导论</a></td>
    </tr>
    <tr>
        <td><a href="/harvard-cs50-cs">哈佛-计算机科学导论</a></td>
    </tr>
    <tr>
        <td><a href="/mit-6.0001">MIT-计算机科学与Python编程导论</a></td>
    </tr>
    <tr>
        <td rowspan="2">数据结构与算法</td>
        <td><a href="/mit-6.046j">MIT-数据结构与算法设计</a></td>
    </tr>
    <tr>
        <td><a href="/umd-cmsc420-0101">马里兰大学-数据结构</a></td>
    </tr>
    <tr>
        <td rowspan="2">数据库</td>
        <td><a href="/cmu-14-455">CMU-数据库系统导论</a></td>
    </tr>
    <tr>
        <td><a href="/cmu-15-721">CMU-数据库系统进阶</a></td>
    </tr>
    <tr>
        <td rowspan="2">机器学习及应用</td>
        <td><a href="/cs229">斯坦福CS229</a></td>
    </tr>
    <tr>
        <td><a href="/mit-6.036">MIT-机器学习导论</a></td>
    </tr>
    <tr>
        <td rowspan="8">深度学习及应用</td>
        <td><a href="/cs230">斯坦福CS230</a></td>
    </tr>
    <tr>
        <td><a href="/harvard-cs50-ai">哈佛-Python人工智能入门</a></td>
    </tr>
    <tr>
        <td><a href="/mit-6.s191">MIT-深度学习导论</a></td>
    </tr>
    <tr>
        <td><a href="/ntu-hylee-ml">李宏毅-机器学习(&深度学习)</a></td>
    </tr>
    <tr>
        <td><a href="/tech-adl">应用深度学习(全知识点覆盖)</a></td>
    </tr>
    <tr>
        <td><a href="/berkeley-csw182">UC Berkeley-深度神经网络设计、可视化与理解</a></td>
    </tr>
    <tr>
        <td><a href="/wisc-stat453">威斯康星-深度学习和生成模型导论</a></td>
    </tr>
    <tr>
        <td><a href="/berkeley-fsdl">UC Berkeley-全栈深度学习训练营</a></td>
    </tr>
    <tr>
        <td rowspan="4">自然语言处理</td>
        <td><a href="/cs224n">斯坦福CS224n（深度学习与NLP）</a></td>
    </tr>
    <tr>
        <td><a href="/cs124">斯坦福CS124（从语言到信息）</a></td>
    </tr>
    <tr>
        <td><a href="/cs520">斯坦福CS520（知识图谱）</a></td>
    </tr>
    <tr>
        <td><a href="/umass-cs685">马萨诸塞-自然语言处理进阶</a></td>
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
        <td >多模态</td>
        <td><a href="/cmu-11-777">CMU-多模态机器学习</a></td>
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
        <td >无监督学习</td>
        <td><a href="/cs294-158">伯克利CS294-158（深度无监督学习）</a></td>
    </tr>
    <tr>
        <td rowspan="3">AI与生物医疗</td>
        <td><a href="/mit-6.874">MIT-面向生命科学的深度学习</a></td>
    </tr>
    <tr>
        <td><a href="/mit-6.047">MIT-基因组学机器学习</a></td>
    </tr>
    <tr>
        <td><a href="/mit-6.s897">MIT-医疗机器学习</a></td>
    </tr>
    <tr>
        <td rowspan="2">图形学与几何</td>
        <td><a href="/cmu-15-462">CMU-计算机图形学</a></td>
    </tr>
    <tr>
        <td><a href="/ammi-gml">AMMI-几何深度学习</a></td>
    </tr>
    <tr>
        <td rowspan="2">其他课程</td>
        <td><a href="/harvard-cs50-web">哈佛-基于Python/JavaScript的web编程</a></td>
    </tr>
    <tr>
        <td><a href="/mit-18.s191">MIT-计算思维导论(Julia)</a></td>
    </tr>
</table>

<div align="center">'''+'''
<img src="http://image.showmeai.tech/course/{image}-3.png" width = "100%" alt="end" align=center />
</div>
'''.format(image=img)

    out.write(content)
    out.close()