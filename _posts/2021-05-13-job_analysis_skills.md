---
title: 算法招聘_技能与要求分析
---



<html>
<head>
    <meta charset="UTF-8">
    <title>Awesome-pyecharts</title>
            <script type="text/javascript" src="https://assets.pyecharts.org/assets/echarts.min.js"></script>
        <script type="text/javascript" src="https://assets.pyecharts.org/assets/echarts-wordcloud.min.js"></script>

    

<style>
.button {
  display: inline-block;
  border-radius: 5px;
  border: 1px solid pink;
  background-color: #f4511e;
  color: #FFFFFF;
  text-align: center;
  font-size: 18px;
  padding: 16px;
  transition: all 0.1s;
  cursor: pointer;
  float: left;
}


.button:hover {
    background-color: #3e8e41;
}
</style>
</head>
<body>

<h2>（2021-05-31更新）</h2>

<h2>点击按钮查看招聘数据分析详情</h2>
    
<a href="https://showmeai-hub.github.io/2021/05/13/job_data_analysis.html">
    <button class="button">看薪资</button>
</a>
<a href="https://showmeai-hub.github.io/2021/05/13/job_analysis_company.html">
    <button class="button">看公司</button>
</a>
<a href="https://showmeai-hub.github.io/2021/05/13/job_analysis_skills.html">
    <button class="button">看要求</button>
</a>
<a href="https://showmeai-hub.github.io/2021/05/13/recent_jds.html">
    <button class="button">典型JD</button>
</a>

<p style="clear:both"><br></p>


</body>


<body>
        <style>
        .tab {
            overflow: hidden;
            border: 1px solid #ccc;
            background-color: #f1f1f1;
        }

        .tab button {
            background-color: inherit;
            float: left;
            border: none;
            outline: none;
            cursor: pointer;
            padding: 12px 16px;
            transition: 0.3s;
        }

        .tab button:hover {
            background-color: #ddd;
        }

        .tab button.active {
            background-color: #ccc;
        }

        .chart-container {
            display: none;
            padding: 6px 12px;
            border-top: none;
        }
    </style>
    <div class="tab">
            <button class="tablinks" onclick="showChart(event, '542ca9020b3e4d499fd3f9a04bb67226')">关键词</button>
            <button class="tablinks" onclick="showChart(event, 'd31f4cdb30a0420a8863e33743f1788d')">关键词分布</button>
            <button class="tablinks" onclick="showChart(event, '8b44b2d05d5940c3940a5290bcf49a06')">学历要求</button>
            <button class="tablinks" onclick="showChart(event, '1d57d57562114e00b5e6519e532349a3')">经验要求</button>
            <button class="tablinks" onclick="showChart(event, '1b34c75d07b546cc8a21f302c114bb52')">NLP岗位职责</button>
            <button class="tablinks" onclick="showChart(event, '6889adb6cb1a40aa8beeed533e1722b4')">NLP任职要求</button>
            <button class="tablinks" onclick="showChart(event, 'bcbd103e05e549c3ac4d2fbcb8639ad1')">CV岗位职责</button>
            <button class="tablinks" onclick="showChart(event, '4f4bdabde7c6463daf9313c70d1a8e73')">CV任职要求</button>
            <button class="tablinks" onclick="showChart(event, 'c90670413a9441b48ad004799a71e6e9')">推荐算法岗位职责</button>
            <button class="tablinks" onclick="showChart(event, '20c3bc576c1d4da49b2d2d2441118c2a')">推荐算法任职要求</button>
    </div>

    <div class="box">
                <div id="542ca9020b3e4d499fd3f9a04bb67226" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_542ca9020b3e4d499fd3f9a04bb67226 = echarts.init(
            document.getElementById('542ca9020b3e4d499fd3f9a04bb67226'), 'white', {renderer: 'canvas'});
            
    var waterMarkText = 'ShowMeAI';
    var canvas = document.createElement('canvas');
    var ctx = canvas.getContext('2d');
    canvas.width = canvas.height = 300;
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.globalAlpha = 0.03;
    ctx.font = '50px Microsoft Yahei';
    ctx.translate(100, 100);
    ctx.rotate(-Math.PI / 4);
    ctx.fillText(waterMarkText, 0, 0);
    img = canvas;
    
        var option_542ca9020b3e4d499fd3f9a04bb67226 = {
    "backgroundColor": {
        "type": "pattern",
        "image": img,
        "repeat": "repeat"
    },
    "animation": true,
    "animationThreshold": 2000,
    "animationDuration": 1000,
    "animationEasing": "cubicOut",
    "animationDelay": 0,
    "animationDurationUpdate": 300,
    "animationEasingUpdate": "cubicOut",
    "animationDelayUpdate": 0,
    "color": [
        "#c23531",
        "#2f4554",
        "#61a0a8",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3",
        "#f05b72",
        "#ef5b9c",
        "#f47920",
        "#905a3d",
        "#fab27b",
        "#2a5caa",
        "#444693",
        "#726930",
        "#b2d235",
        "#6d8346",
        "#ac6767",
        "#1d953f",
        "#6950a1",
        "#918597"
    ],
    "series": [
        {
            "type": "bar",
            "xAxisIndex": 0,
            "yAxisIndex": 0,
            "legendHoverLink": true,
            "data": [
                447,
                286,
                191,
                134,
                124,
                114,
                110
            ],
            "showBackground": false,
            "barMinHeight": 0,
            "barCategoryGap": "20%",
            "barGap": "30%",
            "large": false,
            "largeThreshold": 400,
            "seriesLayoutBy": "column",
            "datasetIndex": 0,
            "clip": true,
            "zlevel": 0,
            "z": 2,
            "label": {
                "show": true,
                "position": "top",
                "margin": 8
            }
        },
        {
            "type": "wordCloud",
            "name": "\u804c\u4f4d\u5173\u952e\u8bcd",
            "shape": "circle",
            "rotationRange": [
                -90,
                90
            ],
            "rotationStep": 45,
            "girdSize": 20,
            "sizeRange": [
                25,
                68
            ],
            "data": [
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60",
                    "value": 447,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,0,115)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u670d\u52a1",
                    "value": 286,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,1,44)"
                        }
                    }
                },
                {
                    "name": "Python",
                    "value": 191,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,104,42)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6316\u6398",
                    "value": 134,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,106,138)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u7b97\u6cd5",
                    "value": 124,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,95,89)"
                        }
                    }
                },
                {
                    "name": "C/C++",
                    "value": 114,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,95,53)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u5b66\u4e60",
                    "value": 110,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,77,90)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u7247\u8bc6\u522b",
                    "value": 108,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,101,20)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u7b97\u6cd5",
                    "value": 93,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,87,134)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7136\u8bed\u8a00\u5904\u7406",
                    "value": 75,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,87,24)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u8138\u8bc6\u522b",
                    "value": 72,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,6,160)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,48,158)"
                        }
                    }
                },
                {
                    "name": "\u7ee9\u6548\u5956\u91d1",
                    "value": 59,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,53,21)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e",
                    "value": 58,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,58,128)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546\u5e73\u53f0",
                    "value": 56,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,11,91)"
                        }
                    }
                },
                {
                    "name": "C++",
                    "value": 52,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,37,68)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u786c\u4ef6",
                    "value": 51,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,156,30)"
                        }
                    }
                },
                {
                    "name": "\u6280\u80fd\u57f9\u8bad",
                    "value": 51,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,56,63)"
                        }
                    }
                },
                {
                    "name": "Java",
                    "value": 50,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,156,102)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u670d\u52a1\uff5c\u54a8\u8be2",
                    "value": 48,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,33,6)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u5f0f\u8bc6\u522b",
                    "value": 47,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,159,41)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u5e74\u5047",
                    "value": 47,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,144,85)"
                        }
                    }
                },
                {
                    "name": "\u8f6f\u4ef6\u670d\u52a1\uff5c\u54a8\u8be2",
                    "value": 47,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,54,82)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u7b97\u6cd5",
                    "value": 42,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,21,82)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u8bc6\u522b",
                    "value": 42,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,47,121)"
                        }
                    }
                },
                {
                    "name": "\u79fb\u52a8\u4e92\u8054\u7f51",
                    "value": 39,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,71,23)"
                        }
                    }
                },
                {
                    "name": "\u5c97\u4f4d\u664b\u5347",
                    "value": 38,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,29,111)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5904\u7406",
                    "value": 36,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,42,47)"
                        }
                    }
                },
                {
                    "name": "\u7269\u8054\u7f51",
                    "value": 34,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,150,160)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u5de5\u4f5c",
                    "value": 33,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,67,157)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u6280\u91d1\u878d",
                    "value": 33,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,139,76)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u7ba1\u7406",
                    "value": 33,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,14,20)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u56fe\u50cf\u89c6\u89c9",
                    "value": 32,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,90,147)"
                        }
                    }
                },
                {
                    "name": "TensoFlow",
                    "value": 32,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,39,12)"
                        }
                    }
                },
                {
                    "name": "\u9886\u5bfc\u597d",
                    "value": 32,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,138,151)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u5206\u7c7b",
                    "value": 31,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,46,93)"
                        }
                    }
                },
                {
                    "name": "NLP",
                    "value": 30,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,146,28)"
                        }
                    }
                },
                {
                    "name": "OpenCV",
                    "value": 29,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,44,70)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u673a\u89c6\u89c9",
                    "value": 28,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,139,74)"
                        }
                    }
                },
                {
                    "name": "\u76ee\u6807\u68c0\u6d4b",
                    "value": 28,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,81,136)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1",
                    "value": 27,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,2,62)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u5065\u5eb7",
                    "value": 27,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,144,113)"
                        }
                    }
                },
                {
                    "name": "PyTorch",
                    "value": 27,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,30,91)"
                        }
                    }
                },
                {
                    "name": "IT\u6280\u672f\u670d\u52a1\uff5c\u54a8\u8be2",
                    "value": 25,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,53,77)"
                        }
                    }
                },
                {
                    "name": "\u6587\u5b57\u8bc6\u522b",
                    "value": 25,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,7,115)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u7cfb\u7edf",
                    "value": 24,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,102,112)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4ea4\u5e73\u53f0",
                    "value": 24,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,26,100)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d",
                    "value": 23,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,141,35)"
                        }
                    }
                },
                {
                    "name": "\u540e\u7aef\u5f00\u53d1",
                    "value": 23,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,18,141)"
                        }
                    }
                },
                {
                    "name": "nan",
                    "value": 23,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,88,144)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76",
                    "value": 22,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,87,149)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u96f6\u552e",
                    "value": 22,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,74,27)"
                        }
                    }
                },
                {
                    "name": "\u6e38\u620f",
                    "value": 21,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,90,106)"
                        }
                    }
                },
                {
                    "name": "\u80a1\u7968\u671f\u6743",
                    "value": 21,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,122,98)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,66,100)"
                        }
                    }
                },
                {
                    "name": "\u8282\u65e5\u793c\u7269",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,64,150)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u89c6\u89c9\u68c0\u6d4b",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,14,74)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5e95\u53cc\u85aa",
                    "value": 18,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,57,31)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u5177\u7c7b\u4ea7\u54c1",
                    "value": 18,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,119,51)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,157,63)"
                        }
                    }
                },
                {
                    "name": "\u516d\u9669\u4e00\u91d1",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,132,132)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u671f\u4f53\u68c0",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,102,23)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u5408\u6210",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,129,111)"
                        }
                    }
                },
                {
                    "name": "\u5c31\u8fd1\u79df\u623f\u8865\u8d34",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,14,19)"
                        }
                    }
                },
                {
                    "name": "\u5728\u7ebf\u6559\u80b2",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,120,33)"
                        }
                    }
                },
                {
                    "name": "Hadoop",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,104,8)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u9891\uff5c\u89c6\u9891\u5a92\u4f53",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,132,151)"
                        }
                    }
                },
                {
                    "name": "\u6559\u80b2",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,54,113)"
                        }
                    }
                },
                {
                    "name": "CNN",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,10,61)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u670d\u52a1",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,143,82)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u8ba1\u7b97",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,150,151)"
                        }
                    }
                },
                {
                    "name": "C",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,156,82)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u73ed\u8f66",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,148,8)"
                        }
                    }
                },
                {
                    "name": "\u4f01\u4e1a\u670d\u52a1",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,142,118)"
                        }
                    }
                },
                {
                    "name": "\u610f\u56fe\u8bc6\u522b",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,125,75)"
                        }
                    }
                },
                {
                    "name": "\u670d\u52a1\u673a\u5668\u4eba",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,17,90)"
                        }
                    }
                },
                {
                    "name": "\u6d88\u8d39\u751f\u6d3b",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,85,127)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u751f\u6210",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,156,103)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5206\u6790",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,147,148)"
                        }
                    }
                },
                {
                    "name": "MATLAB",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,20,138)"
                        }
                    }
                },
                {
                    "name": "\u5efa\u6a21",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,94,50)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u5f71\u50cf\u8bca\u65ad",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,68,98)"
                        }
                    }
                },
                {
                    "name": "\u5728\u7ebf\u533b\u7597",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,44,33)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u8425\u9500",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,5,32)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u5b89\u5168",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,136,116)"
                        }
                    }
                },
                {
                    "name": "XGBoost",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,93,122)"
                        }
                    }
                },
                {
                    "name": "\u6570\u4ed3\u5efa\u6a21",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,83,64)"
                        }
                    }
                },
                {
                    "name": "\u8f85\u52a9/\u667a\u80fd\u9a7e\u9a76",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,66,41)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4ea4",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,140,2)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u670d\u52a1",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,103,6)"
                        }
                    }
                },
                {
                    "name": "SLAM",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,74,144)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u6e38\uff5c\u51fa\u884c",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,40,105)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891/\u76d1\u63a7\u5206\u6790",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,91,142)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u7edc\u901a\u4fe1",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,101,151)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\uff5c\u4fdd\u5065\uff5c\u7f8e\u5bb9",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,30,89)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u7b97\u6cd5",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,107,123)"
                        }
                    }
                },
                {
                    "name": "\u8425\u9500\u670d\u52a1\uff5c\u54a8\u8be2",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,34,65)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u9891\u7b97\u6cd5",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,46,24)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u9879\u5956\u91d1",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,91,11)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u4e50",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,11,33)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u8d44\u8baf",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,87,23)"
                        }
                    }
                },
                {
                    "name": "\u7ba1\u7406\u89c4\u8303",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,152,139)"
                        }
                    }
                },
                {
                    "name": "\u95ee\u7b54\u7cfb\u7edf",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,111,84)"
                        }
                    }
                },
                {
                    "name": "Spark",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,118,118)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u80fd\u6e90\u6c7d\u8f66\u5236\u9020",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,74,153)"
                        }
                    }
                },
                {
                    "name": "AI",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,66,125)"
                        }
                    }
                },
                {
                    "name": "\u77ed\u89c6\u9891",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,136,85)"
                        }
                    }
                },
                {
                    "name": "\u7269\u6d41\uff5c\u8fd0\u8f93",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,35,155)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u793e\u533a",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,29,76)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,27,21)"
                        }
                    }
                },
                {
                    "name": "RNN",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,49,53)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u62bd\u53d6",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,113,17)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u8865\u52a9",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,140,62)"
                        }
                    }
                },
                {
                    "name": "Shell",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,71,11)"
                        }
                    }
                },
                {
                    "name": "Scala",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,10,34)"
                        }
                    }
                },
                {
                    "name": "Caffe",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,101,20)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u5177\u8f6f\u4ef6",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,109,64)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79\u4f18\u5316",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,50,125)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u6587\u5206\u8bcd",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,118,117)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4ea4\u5a92\u4f53",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,101,95)"
                        }
                    }
                },
                {
                    "name": "\u8def\u5f84\u89c4\u5212",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,117,88)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u5904\u7406",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,156,54)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,86,113)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u8bc6\u56fe\u8c31",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,40,112)"
                        }
                    }
                },
                {
                    "name": "\u529e\u516c\u903c\u683c\u9ad8",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,6,48)"
                        }
                    }
                },
                {
                    "name": "\u671f\u6743\u4e30\u539a",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,8,86)"
                        }
                    }
                },
                {
                    "name": "\u6ef4\u6ef4",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,130,98)"
                        }
                    }
                },
                {
                    "name": "\u7269\u6d41",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,157,109)"
                        }
                    }
                },
                {
                    "name": "\u5782\u76f4\u641c\u7d22",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,34,95)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u56e2\u961f",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,62,68)"
                        }
                    }
                },
                {
                    "name": "python",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,141,31)"
                        }
                    }
                },
                {
                    "name": "linux",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,159,83)"
                        }
                    }
                },
                {
                    "name": "SQL",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,110,126)"
                        }
                    }
                },
                {
                    "name": "\u8bcd\u6027\u6807\u6ce8",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,103,66)"
                        }
                    }
                },
                {
                    "name": "GAN",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,105,3)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u5de5\u7a0b\u5e08",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,60,58)"
                        }
                    }
                },
                {
                    "name": "Keras",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,34,36)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u5973\u591a",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,75,158)"
                        }
                    }
                },
                {
                    "name": "TensorFlow",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,118,113)"
                        }
                    }
                },
                {
                    "name": "\u6559\u80b2\uff5c\u57f9\u8bad",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,124,100)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u753b\u50cf",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,6,154)"
                        }
                    }
                },
                {
                    "name": "\u751f\u6d3b\u670d\u52a1",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,153,5)"
                        }
                    }
                },
                {
                    "name": "spark",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,129,106)"
                        }
                    }
                },
                {
                    "name": "ARM",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,13,16)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51\u91d1\u878d",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,54,0)"
                        }
                    }
                },
                {
                    "name": "Linux",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,18,52)"
                        }
                    }
                },
                {
                    "name": "\u533a\u5757\u94fe",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,3,86)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u7ed3\u6784",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,32,55)"
                        }
                    }
                },
                {
                    "name": "\u5f3a\u5316\u5b66\u4e60",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,69,101)"
                        }
                    }
                },
                {
                    "name": "\u901a\u8baf\u6d25\u8d34",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,10,48)"
                        }
                    }
                },
                {
                    "name": "nlp\u7b97\u6cd5\u5de5\u7a0b\u5e08",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,45,16)"
                        }
                    }
                },
                {
                    "name": "\u53e5\u6cd5\u5206\u6790",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,20,10)"
                        }
                    }
                },
                {
                    "name": "HALCON",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,59,130)"
                        }
                    }
                },
                {
                    "name": "Hive",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,110,104)"
                        }
                    }
                },
                {
                    "name": "\u7cbe\u82f1\u56e2\u961f",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,22,160)"
                        }
                    }
                },
                {
                    "name": "MCN\uff5c\u76f4\u64ad\u5e73\u53f0",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,88,49)"
                        }
                    }
                },
                {
                    "name": "\u94f6\u884c",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,76,70)"
                        }
                    }
                },
                {
                    "name": "MySQL",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,96,149)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u7ffb\u8bd1",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,63,15)"
                        }
                    }
                },
                {
                    "name": "\u6587\u5316\u4f20\u5a92",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,145,17)"
                        }
                    }
                },
                {
                    "name": "CV",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,74,94)"
                        }
                    }
                },
                {
                    "name": "CTR\u9884\u4f30",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,13,121)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u89c6\u89c9",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,27,142)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,79,39)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,51,90)"
                        }
                    }
                },
                {
                    "name": "opencv",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,32,23)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u4e1a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,99,120)"
                        }
                    }
                },
                {
                    "name": "c++",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,156,17)"
                        }
                    }
                },
                {
                    "name": "\u6c7d\u8f66",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,113,55)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,65,87)"
                        }
                    }
                },
                {
                    "name": "kaggle",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,3,67)"
                        }
                    }
                },
                {
                    "name": "Tensorflow",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,113,18)"
                        }
                    }
                },
                {
                    "name": "Golang",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,117,141)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u5316\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,35,54)"
                        }
                    }
                },
                {
                    "name": "opengl",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,50,104)"
                        }
                    }
                },
                {
                    "name": "OCR",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,126,10)"
                        }
                    }
                },
                {
                    "name": "\u6c7d\u8f66\u4ea4\u6613\u5e73\u53f0",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,55,68)"
                        }
                    }
                },
                {
                    "name": "\u5d4c\u5165\u5f0f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,11,99)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,66,21)"
                        }
                    }
                },
                {
                    "name": "ROS",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,1,43)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u68c0\u7d22",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,105,74)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u641c\u7d22",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,67,120)"
                        }
                    }
                },
                {
                    "name": "\u76f4\u64ad",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,33,101)"
                        }
                    }
                },
                {
                    "name": "\u8fea\u58eb\u5c3c",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,96,8)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u4e92\u8054\u7f51",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,43,12)"
                        }
                    }
                },
                {
                    "name": "\u8ffd\u6c42\u6781\u81f4",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,103,160)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u4eba\u8f66",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,20,140)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u5bb6\u5c45",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,54,87)"
                        }
                    }
                },
                {
                    "name": "ROS\u7cfb\u7edf",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,135,10)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,116,59)"
                        }
                    }
                },
                {
                    "name": "GPU",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,50,31)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u5668\u68b0",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,106,126)"
                        }
                    }
                },
                {
                    "name": "\u6d41\u5a92\u4f53",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,66,40)"
                        }
                    }
                },
                {
                    "name": "tensorflow",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,9,10)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79\u5b66",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,44,10)"
                        }
                    }
                },
                {
                    "name": "\u7acb\u4f53\u89c6\u89c9",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,34,49)"
                        }
                    }
                },
                {
                    "name": "\u6559\u80b2\u8f85\u5bfc",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,98,120)"
                        }
                    }
                },
                {
                    "name": "\u8f6f\u4ef6\u5f00\u53d1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,124,127)"
                        }
                    }
                },
                {
                    "name": "\u540e\u7aef",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,49,17)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u8bbe\u8ba1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,56,76)"
                        }
                    }
                },
                {
                    "name": "\u5c45\u4f4f\u670d\u52a1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,72,12)"
                        }
                    }
                },
                {
                    "name": "slam",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,118,2)"
                        }
                    }
                },
                {
                    "name": "\u70b9\u4e91",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,88,42)"
                        }
                    }
                },
                {
                    "name": "\u672c\u5206",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,105,150)"
                        }
                    }
                },
                {
                    "name": "ETA",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,105,138)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u8bc6\u522b",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,117,39)"
                        }
                    }
                },
                {
                    "name": "\u5730\u56fe",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,149,29)"
                        }
                    }
                },
                {
                    "name": "\u7269\u6d41\u5e73\u53f0",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,61,70)"
                        }
                    }
                },
                {
                    "name": "\u795e\u7ecf\u7f51\u7edc",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,69,158)"
                        }
                    }
                },
                {
                    "name": "\u5236\u9020\u4e1a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,31,71)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,23,34)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5ea6\u65c5\u6e38",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,77,37)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u539a\u5e74\u7ec8",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,8,96)"
                        }
                    }
                },
                {
                    "name": "nlp",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,67,50)"
                        }
                    }
                },
                {
                    "name": "\u53cd\u4f5c\u5f0a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,133,137)"
                        }
                    }
                },
                {
                    "name": "\u4f20\u611f\u5668",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,89,47)"
                        }
                    }
                },
                {
                    "name": "\u6027\u80fd\u6d4b\u8bd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,47,119)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u8bbe\u8ba1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,129,153)"
                        }
                    }
                },
                {
                    "name": "Lucene",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,9,137)"
                        }
                    }
                },
                {
                    "name": "\u5546\u4e1a\u822a\u5929",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,144,41)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u52a8\u63a7\u5236",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,116,47)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u89c6\u9891",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,62,13)"
                        }
                    }
                },
                {
                    "name": "\u786c\u4ef6\u5236\u9020",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,134,18)"
                        }
                    }
                },
                {
                    "name": "\u7c7b\u8111\u8ba1\u7b97",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,77,113)"
                        }
                    }
                },
                {
                    "name": "OpenCL",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,134,0)"
                        }
                    }
                },
                {
                    "name": "\u7248\u9762\u5206\u6790",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,8,93)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5206\u7ea2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,139,75)"
                        }
                    }
                },
                {
                    "name": "\u5168\u7403\u5316",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,106,119)"
                        }
                    }
                },
                {
                    "name": "\u51fa\u56fd\u65c5\u6e38",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,129,108)"
                        }
                    }
                },
                {
                    "name": "\u5348\u9910\u8865\u52a9",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,6,4)"
                        }
                    }
                },
                {
                    "name": "GBDT",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,66,155)"
                        }
                    }
                },
                {
                    "name": "hadoop",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,56,49)"
                        }
                    }
                },
                {
                    "name": "\u5206\u5e03\u5f0f\u641c\u7d22",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,78,37)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u7ba1\u7406",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,56,4)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u5339\u914d\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,21,46)"
                        }
                    }
                },
                {
                    "name": "\u6570\u4ed3\u67b6\u6784",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,128,43)"
                        }
                    }
                },
                {
                    "name": "PaddlePddle",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,65,34)"
                        }
                    }
                },
                {
                    "name": "\u7cfb\u7edf\u67b6\u6784",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,141,141)"
                        }
                    }
                },
                {
                    "name": "\u9700\u6c42\u5206\u6790",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,160,141)"
                        }
                    }
                },
                {
                    "name": "\u8f66\u8054\u7f51",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,144,150)"
                        }
                    }
                },
                {
                    "name": "\u805a\u7c7b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,33,95)"
                        }
                    }
                },
                {
                    "name": "SNN",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,69,131)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6167\u57ce\u5e02",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,7,9)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u8138\u751f\u6210",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,47,62)"
                        }
                    }
                },
                {
                    "name": "\u901a\u4fe1/\u7f51\u7edc\u8bbe\u5907",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,117,3)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u68c0\u6d4b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,39,116)"
                        }
                    }
                },
                {
                    "name": "C#",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,157,40)"
                        }
                    }
                },
                {
                    "name": "matlab",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,22,97)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4ea4\u5a92\u4f53\u5e73\u53f0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,88,15)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u589e\u957f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,106,37)"
                        }
                    }
                },
                {
                    "name": "\u8111\u673a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,155,14)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u8574\u6db5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,90,115)"
                        }
                    }
                },
                {
                    "name": "Pytorch",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,76,65)"
                        }
                    }
                },
                {
                    "name": "\u7535\u673a\u63a7\u5236",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,139,141)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5e93",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,104,126)"
                        }
                    }
                },
                {
                    "name": "DSP",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,73,94)"
                        }
                    }
                },
                {
                    "name": "JAVA",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,78,79)"
                        }
                    }
                },
                {
                    "name": "Node.js",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,107,51)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u91d1\u878d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,42,96)"
                        }
                    }
                },
                {
                    "name": "\u6e38\u620fAI\u7814\u53d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,137,45)"
                        }
                    }
                },
                {
                    "name": "ACM",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,70,0)"
                        }
                    }
                },
                {
                    "name": "\u4e03\u9669\u4e00\u91d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,49,55)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,139,149)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u673a\u56fe\u5f62\u5b66",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,83,26)"
                        }
                    }
                },
                {
                    "name": "CAD",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,8,119)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,55,124)"
                        }
                    }
                },
                {
                    "name": "Flink",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,43,111)"
                        }
                    }
                },
                {
                    "name": "RTK",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,149,21)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u4f4d\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,3,21)"
                        }
                    }
                },
                {
                    "name": "3D",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,75,62)"
                        }
                    }
                },
                {
                    "name": "LR",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,62,109)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5206\u5272",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,54,64)"
                        }
                    }
                },
                {
                    "name": "\u5e05\u54e5\u591a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,70,148)"
                        }
                    }
                },
                {
                    "name": "\u5206\u7c7b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,11,44)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u4ed3\u5e93",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,133,4)"
                        }
                    }
                },
                {
                    "name": "ElasticSearch",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,131,57)"
                        }
                    }
                },
                {
                    "name": "OpenGL",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,34,77)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,68,135)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u76ee",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,73,112)"
                        }
                    }
                },
                {
                    "name": "VIO",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,89,3)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u98ce\u63a7",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,51,63)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7406\u89e3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,24,29)"
                        }
                    }
                },
                {
                    "name": "\u5206\u7c7b\u4fe1\u606f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,3,71)"
                        }
                    }
                },
                {
                    "name": "AR",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,76,107)"
                        }
                    }
                },
                {
                    "name": "\u7ade\u54c1\u5206\u6790",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,122,76)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,49,36)"
                        }
                    }
                },
                {
                    "name": "OpenMesh",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,133,107)"
                        }
                    }
                },
                {
                    "name": "MCU",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,90,144)"
                        }
                    }
                },
                {
                    "name": "\u5206\u5e03\u5f0f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,29,132)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u7a0b\u80fd\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,22,59)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u7406\u89e3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,25,9)"
                        }
                    }
                },
                {
                    "name": "\u5956\u91d1\u591a\u591a\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,148,54)"
                        }
                    }
                },
                {
                    "name": "R",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,121,109)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u4e49\u7406\u89e3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,14,158)"
                        }
                    }
                },
                {
                    "name": "\u964d\u566a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,127,74)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,122,65)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,10,49)"
                        }
                    }
                },
                {
                    "name": "\u5305\u5348\u9910\u665a\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,82,133)"
                        }
                    }
                },
                {
                    "name": "\u52a8\u4f5c\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,134,30)"
                        }
                    }
                },
                {
                    "name": "\u5b8c\u6210E\u8f6e\u878d\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,27,112)"
                        }
                    }
                },
                {
                    "name": "\u63a7\u5236\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,105,146)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u5b66\u4e60\u6a21\u578b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,82,125)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u4e49\u5206\u6790",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,82,121)"
                        }
                    }
                },
                {
                    "name": "\u5b9e\u4f53\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,88,23)"
                        }
                    }
                },
                {
                    "name": "AI\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,107,21)"
                        }
                    }
                },
                {
                    "name": "rtk\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,104,80)"
                        }
                    }
                },
                {
                    "name": "salm",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,43,126)"
                        }
                    }
                },
                {
                    "name": "\u4e70\u624b\u6218\u7565",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,57,11)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u6a21\u578b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,155,122)"
                        }
                    }
                },
                {
                    "name": "XGB",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,56,35)"
                        }
                    }
                },
                {
                    "name": "\u5d4c\u5165\u5f0f\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,133,96)"
                        }
                    }
                },
                {
                    "name": "libvpx",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,109,43)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u4eba\u9a7e\u9a76",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,16,119)"
                        }
                    }
                },
                {
                    "name": "ACC/AEB/LKA",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,8,37)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u9891\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,68,61)"
                        }
                    }
                },
                {
                    "name": "AutoML",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,152,17)"
                        }
                    }
                },
                {
                    "name": "\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,120,92)"
                        }
                    }
                },
                {
                    "name": "PCL",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,15,65)"
                        }
                    }
                },
                {
                    "name": "3dmm",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,154,33)"
                        }
                    }
                },
                {
                    "name": "3D\u5f15\u64ce",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,56,112)"
                        }
                    }
                },
                {
                    "name": "\u6392\u5e8f\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,113,120)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,140,107)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u725b\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,21,66)"
                        }
                    }
                },
                {
                    "name": "\u878d\u5408IMU",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,107,78)"
                        }
                    }
                },
                {
                    "name": "X264",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,91,41)"
                        }
                    }
                },
                {
                    "name": "\u907f\u969c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,142,9)"
                        }
                    }
                },
                {
                    "name": "\u6d4b\u8bd5\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,74,141)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u53ec\u56de",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,102,68)"
                        }
                    }
                },
                {
                    "name": "SOA",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,92,133)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5a92\u4f53",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,118,27)"
                        }
                    }
                },
                {
                    "name": "\u8425\u9500\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,148,20)"
                        }
                    }
                },
                {
                    "name": "\u56de\u58f0\u6d88\u9664",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,3,113)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,3,35)"
                        }
                    }
                },
                {
                    "name": "VTK",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,87,98)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u4e1a\u670d\u52a1\uff5c\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,73,136)"
                        }
                    }
                },
                {
                    "name": "\u51e0\u4f55\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,83,56)"
                        }
                    }
                },
                {
                    "name": "\u6df7\u54cd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,30,42)"
                        }
                    }
                },
                {
                    "name": "\u5168\u94fe\u8defSaaS\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,86,78)"
                        }
                    }
                },
                {
                    "name": "3D\u59ff\u6001\u91cd\u5efa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,119,12)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u4e49\u5206\u5272",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,107,28)"
                        }
                    }
                },
                {
                    "name": "3D\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,71,158)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u52a8\u63a7\u5236\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,136,134)"
                        }
                    }
                },
                {
                    "name": "3DGIS",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,47,102)"
                        }
                    }
                },
                {
                    "name": "CAD\u56fe\u7eb8\u5206\u6790",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,153,107)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9slam",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,127,10)"
                        }
                    }
                },
                {
                    "name": "\u5e95\u5c42\u89c6\u89c9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,38,98)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u524d\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,141,124)"
                        }
                    }
                },
                {
                    "name": "\u4e0b\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,58,26)"
                        }
                    }
                },
                {
                    "name": "NLP/CV",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,2,146)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,130,93)"
                        }
                    }
                },
                {
                    "name": "\u4eff\u771f\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,31,93)"
                        }
                    }
                },
                {
                    "name": "DSP\u7f16\u7a0b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,33,153)"
                        }
                    }
                },
                {
                    "name": "\u4eff\u771f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,25,85)"
                        }
                    }
                },
                {
                    "name": "\u9ed1\u76d2\u6d4b\u8bd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,102,35)"
                        }
                    }
                },
                {
                    "name": "AIOPS",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,128,78)"
                        }
                    }
                },
                {
                    "name": "\u65f6\u5e8f\u6570\u636e\u5e93",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,34,132)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u6280\u5927\u725b\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,134,111)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u89c6\u89c9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,124,72)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u5238\u5546",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,51,8)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u56fe\u50cf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,153,27)"
                        }
                    }
                },
                {
                    "name": "\u5206\u5e03\u5f0f\u8bad\u7ec3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,113,135)"
                        }
                    }
                },
                {
                    "name": "ESMM",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,112,81)"
                        }
                    }
                },
                {
                    "name": "\u7279\u6548",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,5,2)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u7814\u7a76",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,75,17)"
                        }
                    }
                },
                {
                    "name": "rgbd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,108,59)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u4f30\u8ba1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,40,85)"
                        }
                    }
                },
                {
                    "name": "\u534f\u540c\u8fc7\u6ee4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,53,85)"
                        }
                    }
                },
                {
                    "name": "SSD\u3001Faster",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,90,42)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u4eff\u771f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,125,128)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u5f15\u64ce",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,40,95)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u589e\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,28,124)"
                        }
                    }
                },
                {
                    "name": "\u5065\u5eb7\u7761\u7720",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,109,79)"
                        }
                    }
                },
                {
                    "name": "3D\u89c6\u89c9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,119,6)"
                        }
                    }
                },
                {
                    "name": "KALDI",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,138,41)"
                        }
                    }
                },
                {
                    "name": "h264\uff0ch265\uff0cav1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,25,26)"
                        }
                    }
                },
                {
                    "name": "Pulp",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,82,160)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,108,127)"
                        }
                    }
                },
                {
                    "name": "CPU",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,60,159)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6e05\u6d17",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,4,151)"
                        }
                    }
                },
                {
                    "name": "\u5f3a\u608d\u7684\u521b\u59cb\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,101,113)"
                        }
                    }
                },
                {
                    "name": "HBase",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,83,85)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,135,26)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a9\u4e09\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,4,72)"
                        }
                    }
                },
                {
                    "name": "\u8f66\u8f86\u8fd0\u52a8\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,15,0)"
                        }
                    }
                },
                {
                    "name": "\u6e32\u67d3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,113,111)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u6280\u672f\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,83,152)"
                        }
                    }
                },
                {
                    "name": "LTE",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,84,105)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u63a8\u8350",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,111,17)"
                        }
                    }
                },
                {
                    "name": "MatLab",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,155,50)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u9884\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,141,85)"
                        }
                    }
                },
                {
                    "name": "CTR",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,44,129)"
                        }
                    }
                },
                {
                    "name": "cuda",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,36,65)"
                        }
                    }
                },
                {
                    "name": "\u9065\u611f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,119,160)"
                        }
                    }
                },
                {
                    "name": "\u8f66\u8f86\u52a8\u529b\u5b66\u5efa\u6a21",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,146,50)"
                        }
                    }
                },
                {
                    "name": "\u5546\u54c1\u6a21\u578b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,47,36)"
                        }
                    }
                },
                {
                    "name": "ISP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,106,21)"
                        }
                    }
                },
                {
                    "name": "flv\uff0cmp3\uff0cmp4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,136,158)"
                        }
                    }
                },
                {
                    "name": "\u5bfc\u822a\u5b9a\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,19,56)"
                        }
                    }
                },
                {
                    "name": "\u6ee4\u955c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,104,10)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u6587\u5206\u6790",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,24,107)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,42,31)"
                        }
                    }
                },
                {
                    "name": "Tensor",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,21,14)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u6392\u5e8f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,43,147)"
                        }
                    }
                },
                {
                    "name": "\u57fa\u7840\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,151,72)"
                        }
                    }
                },
                {
                    "name": "Go",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,138,50)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u5206\u6790",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,15,106)"
                        }
                    }
                },
                {
                    "name": "hybrid/end2end",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,22,135)"
                        }
                    }
                },
                {
                    "name": "openGL",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,10,15)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5e02\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,72,103)"
                        }
                    }
                },
                {
                    "name": "\u540d\u6821\u540d\u4f01\u80cc\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,36,73)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7136\u8bed\u8a00",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,26,11)"
                        }
                    }
                },
                {
                    "name": "\u9aa8\u79d1\u673a\u5668\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,114,83)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u7edc\u4f20\u8f93\u534f\u8bae",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,123,0)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,34,84)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u53ec\u56de",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,25,125)"
                        }
                    }
                },
                {
                    "name": "asr",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,130,139)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,4,31)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u8f6f\u4ef6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,90,149)"
                        }
                    }
                },
                {
                    "name": "ADAS",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,109,59)"
                        }
                    }
                },
                {
                    "name": "Cplex",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,13,69)"
                        }
                    }
                },
                {
                    "name": "\u5348\u9910\u4ea4\u901a\u8865\u52a9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,106,156)"
                        }
                    }
                },
                {
                    "name": "GO",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,94,79)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u6d4b\u8bc4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,3,133)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u538b\u7f29",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,22,27)"
                        }
                    }
                },
                {
                    "name": "/",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,21,61)"
                        }
                    }
                },
                {
                    "name": "\u751f\u7406\u53c2\u6570",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,41,53)"
                        }
                    }
                },
                {
                    "name": "\u6392\u5e8f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,2,109)"
                        }
                    }
                },
                {
                    "name": "react",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,24,94)"
                        }
                    }
                },
                {
                    "name": "\u67b6\u6784\u5e08",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,143,146)"
                        }
                    }
                },
                {
                    "name": "\u591a\u4f20\u611f\u5668\u878d\u5408",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,72,73)"
                        }
                    }
                },
                {
                    "name": "SSL/TLS",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,153,145)"
                        }
                    }
                },
                {
                    "name": "pandas",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,157,125)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u6392\u7a0b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,35,40)"
                        }
                    }
                },
                {
                    "name": "h264",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,147,47)"
                        }
                    }
                },
                {
                    "name": "\u5730\u56fe\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,17,127)"
                        }
                    }
                },
                {
                    "name": "\u78c1\u529b\u8ba1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,83,146)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u8ba1\u7b97",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,144,25)"
                        }
                    }
                },
                {
                    "name": "\u5168\u5458\u51fa\u56fd\u6e38",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,127,95)"
                        }
                    }
                },
                {
                    "name": "\u751f\u4ea7\u8c03\u5ea6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,77,95)"
                        }
                    }
                },
                {
                    "name": "\u6570\u5b57\u56fe\u50cf\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,132,100)"
                        }
                    }
                },
                {
                    "name": "BIM+3D",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,90,154)"
                        }
                    }
                },
                {
                    "name": "\u58f0\u7eb9\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,122,5)"
                        }
                    }
                },
                {
                    "name": "Gurobi",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,62,142)"
                        }
                    }
                },
                {
                    "name": "\u901a\u4fe1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,108,83)"
                        }
                    }
                },
                {
                    "name": "PPP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,14,93)"
                        }
                    }
                },
                {
                    "name": "CGAL",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,90,0)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u5904\u7406\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,36,128)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u591a\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,13,39)"
                        }
                    }
                },
                {
                    "name": "AI\u4ea7\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,97,82)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u843d\u5730",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,7,78)"
                        }
                    }
                },
                {
                    "name": "\u5f02\u5e38\u8bca\u65ad",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,94,53)"
                        }
                    }
                },
                {
                    "name": "LSTM",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,94,121)"
                        }
                    }
                },
                {
                    "name": "\u5173\u7cfb\u6316\u6398",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,36,65)"
                        }
                    }
                },
                {
                    "name": "\u70b9\u4e91\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,68,1)"
                        }
                    }
                },
                {
                    "name": "\u5149\u5b66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,110,119)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,115,22)"
                        }
                    }
                },
                {
                    "name": "\u9009\u578b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,65,135)"
                        }
                    }
                },
                {
                    "name": "docker",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,28,141)"
                        }
                    }
                },
                {
                    "name": "VINS",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,142,154)"
                        }
                    }
                },
                {
                    "name": "\u5355\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,160,153)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,83,20)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u5177\u793e\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,154,86)"
                        }
                    }
                },
                {
                    "name": "java",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,46,57)"
                        }
                    }
                },
                {
                    "name": "nlp\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,38,24)"
                        }
                    }
                },
                {
                    "name": "\u8c03\u62e8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,125,98)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,29,90)"
                        }
                    }
                },
                {
                    "name": "PID\u63a7\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,50,143)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,136,20)"
                        }
                    }
                },
                {
                    "name": "\u786c\u4ef6\u52a0\u901f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,47,20)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u91cd\u5efa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,151,61)"
                        }
                    }
                },
                {
                    "name": "Matlab",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,93,44)"
                        }
                    }
                },
                {
                    "name": "\u5bfc\u822a\u5f15\u64ce",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,71,108)"
                        }
                    }
                },
                {
                    "name": "python/go",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,7,72)"
                        }
                    }
                },
                {
                    "name": "\u9a6c\u5c14\u514b\u592b\u968f\u673a\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,87,28)"
                        }
                    }
                },
                {
                    "name": "ppp-rtk",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,86,24)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,18,15)"
                        }
                    }
                },
                {
                    "name": "\u901a\u4fe1\u539f\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,7,46)"
                        }
                    }
                },
                {
                    "name": "SaaS",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,133,94)"
                        }
                    }
                },
                {
                    "name": "GNSS\u5b9a\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,52,0)"
                        }
                    }
                },
                {
                    "name": "TF",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,29,13)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5348\u9910\u665a\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,4,11)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u5b9a\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,141,102)"
                        }
                    }
                },
                {
                    "name": "3D\u6253\u5370",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,133,128)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u9891\u7f16\u89e3\u7801",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,41,27)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u91cd\u6784",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,121,103)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u63a8\u8350",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,26,113)"
                        }
                    }
                },
                {
                    "name": "Linux\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,160,79)"
                        }
                    }
                },
                {
                    "name": "Attention",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,50,98)"
                        }
                    }
                },
                {
                    "name": "\u5bfc\u822a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,5,95)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7cbe\u5ea6\u5730\u56fe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,5,44)"
                        }
                    }
                },
                {
                    "name": "SVC",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,76,127)"
                        }
                    }
                },
                {
                    "name": "\u8fde\u7eed\u521b\u4e1a\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,61,94)"
                        }
                    }
                },
                {
                    "name": "kaldi",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,100,76)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u81ea\u52a8\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,63,29)"
                        }
                    }
                },
                {
                    "name": "\u52a8\u4f5c\u6355\u6349",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,106,78)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6316\u6398\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,137,99)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5730\u6d4b\u91cf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,48,124)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u8f6c\u6362",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,136,27)"
                        }
                    }
                },
                {
                    "name": "C++/python",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,6,74)"
                        }
                    }
                },
                {
                    "name": "\u5373\u65f6\u901a\u8baf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,149,54)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u77e5\u8bc6\u8bc1\u660e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,33,61)"
                        }
                    }
                },
                {
                    "name": "\u6709\u524d\u9014",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,1,21)"
                        }
                    }
                },
                {
                    "name": "ECC",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,64,42)"
                        }
                    }
                },
                {
                    "name": "Rust",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,10,48)"
                        }
                    }
                },
                {
                    "name": "\u7279\u5f81\u5de5\u7a0b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,128,87)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u62df\u9000\u706b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,122,71)"
                        }
                    }
                },
                {
                    "name": "GIS",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,17,87)"
                        }
                    }
                },
                {
                    "name": "\u7acb\u4f53\u5339\u914d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,79,128)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544aCTR/CVR",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,9,142)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b\u79fb\u690d\u4f18\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,28,106)"
                        }
                    }
                },
                {
                    "name": "\u8def\u5f84\u4f18\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,123,102)"
                        }
                    }
                },
                {
                    "name": "MXNet",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,132,1)"
                        }
                    }
                },
                {
                    "name": "ADAS\u7cfb\u7edf\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,54,36)"
                        }
                    }
                },
                {
                    "name": "webGL",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,67,59)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51+",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,40,154)"
                        }
                    }
                },
                {
                    "name": "\u5730\u56fe\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,2,10)"
                        }
                    }
                },
                {
                    "name": "AILab",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,150,59)"
                        }
                    }
                },
                {
                    "name": "3DCAD",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,156,28)"
                        }
                    }
                },
                {
                    "name": "\u6570\u5b57\u4fe1\u53f7\u5904\u7406\u6570",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,15,107)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u57fa\u7840",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,39,89)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,34,129)"
                        }
                    }
                },
                {
                    "name": "\u4f20\u611f\u5668\u878d\u5408",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,148,101)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u4f533D\u91cd\u5efa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,97,31)"
                        }
                    }
                },
                {
                    "name": "\u4f4f\u798f\u8ba1\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,57,92)"
                        }
                    }
                },
                {
                    "name": "\u4e50\u7406\u8f6c\u6362",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,115,155)"
                        }
                    }
                },
                {
                    "name": "\u8def\u51b5\u8ba1\u7b97",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,154,108)"
                        }
                    }
                },
                {
                    "name": "pytorch",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,129,96)"
                        }
                    }
                },
                {
                    "name": "\u4f11\u95f2\uff5c\u5a31\u4e50",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,123,116)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u5148\u4e0a\u6d77\u843d\u6237",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,89,148)"
                        }
                    }
                },
                {
                    "name": "/Pytorch",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,10,131)"
                        }
                    }
                },
                {
                    "name": "\u9886\u519b\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,42,66)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u7b56\u7565",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,69,73)"
                        }
                    }
                },
                {
                    "name": "\u7279\u5f81\u6316\u6398",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,99,49)"
                        }
                    }
                },
                {
                    "name": "\u5bc6\u7801\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,58,24)"
                        }
                    }
                },
                {
                    "name": "\u6392\u7a0b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,16,156)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u4e3b\u664b\u5347\u8ba1\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,92,9)"
                        }
                    }
                },
                {
                    "name": "NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,110,76)"
                        }
                    }
                },
                {
                    "name": "\u53ec\u56de\u7b56\u7565",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,102,41)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u56fe\u5f62",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,143,157)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u9886\u57df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,120,152)"
                        }
                    }
                },
                {
                    "name": "\u5b9e\u65f6\u8def\u51b5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,88,126)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7136\u8bed\u8a00\u5904",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,130,81)"
                        }
                    }
                },
                {
                    "name": "ETL",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,98,71)"
                        }
                    }
                },
                {
                    "name": "B2B",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,155,152)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u5316\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,123,71)"
                        }
                    }
                },
                {
                    "name": "RCN",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,154,133)"
                        }
                    }
                },
                {
                    "name": "\u516c\u94a5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,44,127)"
                        }
                    }
                },
                {
                    "name": "\u89c4\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,99,57)"
                        }
                    }
                },
                {
                    "name": "\u8f68\u8ff9\u89c4\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,123,102)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u89c6\u9891\u7f16\u89e3\u7801",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,48,83)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9SLAM",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,62,73)"
                        }
                    }
                },
                {
                    "name": "AEB",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,96,57)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7ef4\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,121,34)"
                        }
                    }
                },
                {
                    "name": "\u672c\u5730\u751f\u6d3b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,21,17)"
                        }
                    }
                },
                {
                    "name": "\u4e2a\u6027\u5316\u63a8\u8350",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,33,0)"
                        }
                    }
                },
                {
                    "name": "\u591a\u4f20\u611f\u5668",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,10,82)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u7f51\u683c/\u70b9\u4e91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,32,54)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5065\u5eb7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,100,145)"
                        }
                    }
                },
                {
                    "name": "\u9057\u4f20\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,132,58)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u6e38",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,107,122)"
                        }
                    }
                },
                {
                    "name": "\u8fd1\u7ea2\u5916",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,73,84)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,5,87)"
                        }
                    }
                },
                {
                    "name": "\u878d\u5408\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,92,87)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u90e8\u7f72",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,77,25)"
                        }
                    }
                },
                {
                    "name": "DeepFM",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,34,72)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u65b9\u5411\u7b97\u6cd5\u5de5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,113,150)"
                        }
                    }
                },
                {
                    "name": "\u5468\u672b\u53cc\u4f11",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,46,39)"
                        }
                    }
                },
                {
                    "name": "\u6570\u5b57\u97f3\u9891\u6c34\u5370",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,91,96)"
                        }
                    }
                },
                {
                    "name": "\u4f20\u611f\u5668\u6216\u70b9\u4e91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,34,10)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,111,109)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51\u51fa\u884c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,64,117)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u80fd\u6e90",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,148,61)"
                        }
                    }
                },
                {
                    "name": "neon",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,119,136)"
                        }
                    }
                },
                {
                    "name": "Windows",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,143,57)"
                        }
                    }
                },
                {
                    "name": "\u611f\u77e5\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,45,49)"
                        }
                    }
                },
                {
                    "name": "\u5bfc\u822a\u89c4\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,118,25)"
                        }
                    }
                },
                {
                    "name": "\u5f71\u89c6\uff5c\u52a8\u6f2b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,11,134)"
                        }
                    }
                },
                {
                    "name": "\u8bad\u7ec3\u52a0\u901f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,155,141)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546\u641c\u7d22",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,5,57)"
                        }
                    }
                },
                {
                    "name": "\u5730\u7406\u8f68\u8ff9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,69,160)"
                        }
                    }
                },
                {
                    "name": "\u533b\u5b66\u5f71\u50cf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,1,75)"
                        }
                    }
                },
                {
                    "name": "\u51e0\u4f55\u5b66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,111,9)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b\u538b\u7f29",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,147,21)"
                        }
                    }
                },
                {
                    "name": "HADOOP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,5,123)"
                        }
                    }
                },
                {
                    "name": "FLINK",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,152,116)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6293\u53d6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,73,27)"
                        }
                    }
                },
                {
                    "name": "\u539f\u578b\u8bbe\u8ba1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,134,13)"
                        }
                    }
                },
                {
                    "name": "\u5a92\u4f53",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,125,47)"
                        }
                    }
                },
                {
                    "name": "\u865a\u5047\u6d41\u91cf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,139,71)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u5b89\u5168",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,37,12)"
                        }
                    }
                },
                {
                    "name": "\u53ec\u56de",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,84,125)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u8f6c\u6362",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,66,94)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u5bfc\u822a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,74,116)"
                        }
                    }
                },
                {
                    "name": "\u4e34\u5e8a\u79d1\u7814",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,160,121)"
                        }
                    }
                },
                {
                    "name": "\u8def\u51b5\u4f18\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,88,91)"
                        }
                    }
                },
                {
                    "name": "Caffe\u3001Pytorch\u3001",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,101,42)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,74,139)"
                        }
                    }
                },
                {
                    "name": "UWB",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,139,134)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u8baf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,142,74)"
                        }
                    }
                },
                {
                    "name": "\u3001Spark",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,8,24)"
                        }
                    }
                },
                {
                    "name": "GPS",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,33,139)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u89c6\u9891\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,128,132)"
                        }
                    }
                },
                {
                    "name": "ERP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,91,126)"
                        }
                    }
                },
                {
                    "name": "AR/VR/MR",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,64,110)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u7cca\u63a7\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,148,22)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u76d1\u7763\u5b66\u4e60",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,91,65)"
                        }
                    }
                },
                {
                    "name": "KF/EKF",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,91,79)"
                        }
                    }
                },
                {
                    "name": "\u53bb\u6df7\u54cd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,11,92)"
                        }
                    }
                },
                {
                    "name": "Database",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,12,15)"
                        }
                    }
                },
                {
                    "name": "numpy",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,51,118)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u68c0\u6d4b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,119,76)"
                        }
                    }
                },
                {
                    "name": "\u773c\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,93,77)"
                        }
                    }
                },
                {
                    "name": "\u6295\u8d44/\u878d\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,52,104)"
                        }
                    }
                },
                {
                    "name": "\u591c\u62cd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,108,61)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u7b56\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,18,120)"
                        }
                    }
                },
                {
                    "name": "c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,78,63)"
                        }
                    }
                },
                {
                    "name": "NLP\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,126,118)"
                        }
                    }
                },
                {
                    "name": "PID",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,49,122)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u7b56\u7565",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,96,36)"
                        }
                    }
                },
                {
                    "name": "\u77e9\u9635\u5206\u6790",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,6,68)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,132,68)"
                        }
                    }
                },
                {
                    "name": "\u542f\u53d1\u5f0f\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,18,92)"
                        }
                    }
                },
                {
                    "name": "\u7cbe\u5bc6\u5355\u70b9\u5b9a\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,26,15)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,14,140)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u957f\u5e26\u85aa\u5047\u671f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,106,109)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,119,142)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62\u56fe\u50cf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,36,117)"
                        }
                    }
                },
                {
                    "name": "Transformer",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,92,94)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u725b\u4f17\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,140,27)"
                        }
                    }
                },
                {
                    "name": "x265",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,40,133)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62\u5b66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,157,157)"
                        }
                    }
                },
                {
                    "name": "\u65f6\u95f4\u5e8f\u5217",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,80,49)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7cbe\u5730\u56fe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,124,72)"
                        }
                    }
                },
                {
                    "name": "AGV",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,107,76)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u5b66\u4e60\u7b97\u6cd5\u673a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,149,131)"
                        }
                    }
                },
                {
                    "name": "query",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,69,27)"
                        }
                    }
                },
                {
                    "name": "\u626b\u5730\u673a\u5668\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,74,125)"
                        }
                    }
                },
                {
                    "name": "PHM",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,86,81)"
                        }
                    }
                },
                {
                    "name": "JitterBuffer",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,89,96)"
                        }
                    }
                },
                {
                    "name": "NPL",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,52,28)"
                        }
                    }
                },
                {
                    "name": "NPU",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,87,92)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5206\u6790",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,46,158)"
                        }
                    }
                },
                {
                    "name": "android",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,139,108)"
                        }
                    }
                },
                {
                    "name": "\u542f\u53d1\u5f0f\u89c4\u5219\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,80,37)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u5316\u6d4b\u8bd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,123,159)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u7814",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,21,136)"
                        }
                    }
                },
                {
                    "name": "\u7f16\u7a0b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,69,34)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u6295\u653e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,57,41)"
                        }
                    }
                },
                {
                    "name": "\u4e50\u5668",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,21,76)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u98ce\u63a7AI",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,24,19)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u5206\u7c7b\uff0c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,37,62)"
                        }
                    }
                },
                {
                    "name": "\u6574\u6570\u89c4\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,88,160)"
                        }
                    }
                },
                {
                    "name": "\u73af\u5883\u611f\u77e5\u4e0e\u878d\u5408",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,113,128)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u4f18\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,88,110)"
                        }
                    }
                },
                {
                    "name": "\u79fb\u52a8\u7aef",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,61,159)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u91c7\u96c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,141,112)"
                        }
                    }
                },
                {
                    "name": "flow",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,148,99)"
                        }
                    }
                },
                {
                    "name": "\u519c\u6797\u7267\u6e14",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,150,110)"
                        }
                    }
                },
                {
                    "name": "\u91cf\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,85,105)"
                        }
                    }
                },
                {
                    "name": "Javascript",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,144,108)"
                        }
                    }
                },
                {
                    "name": "\u4e16\u754c500\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,152,0)"
                        }
                    }
                },
                {
                    "name": "\u8054\u90a6\u5b66\u4e60",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,128,113)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,91,135)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u98df\u4e0b\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,10,82)"
                        }
                    }
                },
                {
                    "name": "ORBSLAM",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,119,19)"
                        }
                    }
                },
                {
                    "name": "\u89c4\u5219\u5f15\u64ce",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,152,14)"
                        }
                    }
                },
                {
                    "name": "\u692d\u5706\u66f2\u7ebf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,113,100)"
                        }
                    }
                },
                {
                    "name": "\u80a2\u4f53\u68c0\u6d4b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,78,133)"
                        }
                    }
                },
                {
                    "name": "\u6570\u5b66\u5e93",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,112,35)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7f16\u8f91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,153,88)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u8c03\u7814",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,106,109)"
                        }
                    }
                },
                {
                    "name": "\u624b\u52bf\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,66,39)"
                        }
                    }
                },
                {
                    "name": "\u8282\u65e5\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,56,40)"
                        }
                    }
                },
                {
                    "name": "CPLEX",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,32,87)"
                        }
                    }
                },
                {
                    "name": "\u4f53\u80b2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,112,100)"
                        }
                    }
                },
                {
                    "name": "DNN",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,7,78)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u5173\u952e\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,41,25)"
                        }
                    }
                },
                {
                    "name": "SFM",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,29,8)"
                        }
                    }
                },
                {
                    "name": "CCF",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,58,64)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u611f\u77e5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,128,32)"
                        }
                    }
                },
                {
                    "name": "\u6279\u53d1\uff5c\u96f6\u552e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,39,107)"
                        }
                    }
                },
                {
                    "name": "kalman",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,160,33)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u5bbd\u63a7\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,42,108)"
                        }
                    }
                },
                {
                    "name": "pil",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,100,128)"
                        }
                    }
                },
                {
                    "name": "\u9690\u79d8\u8ba1\u7b97\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,105,113)"
                        }
                    }
                },
                {
                    "name": "C/C++/Python",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,14,91)"
                        }
                    }
                },
                {
                    "name": "H.264/265",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,98,118)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,119,128)"
                        }
                    }
                },
                {
                    "name": "\u6216",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,149,154)"
                        }
                    }
                },
                {
                    "name": "\u5e95\u76d8\u63a7\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,107,131)"
                        }
                    }
                }
            ],
            "top": "10%",
            "height": "400px",
            "drawOutOfBound": false,
            "textStyle": {
                "emphasis": {}
            },
            "xAxisIndex": 1,
            "yAxisIndex": 1
        }
    ],
    "legend": [
        {
            "data": [
                ""
            ],
            "selected": {
                "": true
            },
            "show": true,
            "padding": 5,
            "itemGap": 10,
            "itemWidth": 25,
            "itemHeight": 14
        },
        {
            "data": [],
            "selected": {},
            "show": true,
            "padding": 5,
            "itemGap": 10,
            "itemWidth": 25,
            "itemHeight": 14
        }
    ],
    "tooltip": {
        "show": true,
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "showContent": true,
        "alwaysShowContent": false,
        "showDelay": 0,
        "hideDelay": 100,
        "textStyle": {
            "fontSize": 14
        },
        "borderWidth": 0,
        "padding": 5
    },
    "xAxis": [
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "axisLabel": {
                "rotate": 35
            },
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "show": true,
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            },
            "data": [
                "\u6df1\u5ea6\u5b66\u4e60",
                "\u4eba\u5de5\u667a\u80fd\u670d\u52a1",
                "Python",
                "\u6570\u636e\u6316\u6398",
                "\u56fe\u50cf\u7b97\u6cd5",
                "C/C++",
                "\u673a\u5668\u5b66\u4e60"
            ]
        }
    ],
    "yAxis": [
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "show": true,
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            }
        }
    ],
    "title": [
        {
            "padding": 5,
            "itemGap": 10
        },
        {
            "text": "\u804c\u4f4d\u5173\u952e\u8bcd",
            "padding": 5,
            "itemGap": 10,
            "textStyle": {
                "fontSize": 23
            }
        }
    ],
    "grid": [
        {
            "show": false,
            "zlevel": 0,
            "z": 2,
            "top": "60%",
            "containLabel": false,
            "backgroundColor": "transparent",
            "borderColor": "#ccc",
            "borderWidth": 1
        },
        {
            "show": false,
            "zlevel": 0,
            "z": 2,
            "bottom": "50%",
            "containLabel": false,
            "backgroundColor": "transparent",
            "borderColor": "#ccc",
            "borderWidth": 1
        }
    ]
};
        chart_542ca9020b3e4d499fd3f9a04bb67226.setOption(option_542ca9020b3e4d499fd3f9a04bb67226);
    </script>
                <div id="d31f4cdb30a0420a8863e33743f1788d" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_d31f4cdb30a0420a8863e33743f1788d = echarts.init(
            document.getElementById('d31f4cdb30a0420a8863e33743f1788d'), 'white', {renderer: 'canvas'});
        var option_d31f4cdb30a0420a8863e33743f1788d = {
    "animation": true,
    "animationThreshold": 2000,
    "animationDuration": 1000,
    "animationEasing": "cubicOut",
    "animationDelay": 0,
    "animationDurationUpdate": 300,
    "animationEasingUpdate": "cubicOut",
    "animationDelayUpdate": 0,
    "color": [
        "#c23531",
        "#2f4554",
        "#61a0a8",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3",
        "#f05b72",
        "#ef5b9c",
        "#f47920",
        "#905a3d",
        "#fab27b",
        "#2a5caa",
        "#444693",
        "#726930",
        "#b2d235",
        "#6d8346",
        "#ac6767",
        "#1d953f",
        "#6950a1",
        "#918597"
    ],
    "series": [
        {
            "type": "treemap",
            "name": "\u5173\u952e\u8bcd\u5206\u5e03\u6811\u72b6\u56fe",
            "data": [
                {
                    "value": 447,
                    "name": "\u6df1\u5ea6\u5b66\u4e60"
                },
                {
                    "value": 286,
                    "name": "\u4eba\u5de5\u667a\u80fd\u670d\u52a1"
                },
                {
                    "value": 191,
                    "name": "Python"
                },
                {
                    "value": 134,
                    "name": "\u6570\u636e\u6316\u6398"
                },
                {
                    "value": 124,
                    "name": "\u56fe\u50cf\u7b97\u6cd5"
                },
                {
                    "value": 114,
                    "name": "C/C++"
                },
                {
                    "value": 110,
                    "name": "\u673a\u5668\u5b66\u4e60"
                },
                {
                    "value": 108,
                    "name": "\u56fe\u7247\u8bc6\u522b"
                },
                {
                    "value": 93,
                    "name": "\u63a8\u8350\u7b97\u6cd5"
                },
                {
                    "value": 75,
                    "name": "\u81ea\u7136\u8bed\u8a00\u5904\u7406"
                },
                {
                    "value": 72,
                    "name": "\u4eba\u8138\u8bc6\u522b"
                },
                {
                    "value": 64,
                    "name": "\u4eba\u5de5\u667a\u80fd"
                },
                {
                    "value": 59,
                    "name": "\u7ee9\u6548\u5956\u91d1"
                },
                {
                    "value": 58,
                    "name": "\u5927\u6570\u636e"
                },
                {
                    "value": 56,
                    "name": "\u7535\u5546\u5e73\u53f0"
                },
                {
                    "value": 52,
                    "name": "C++"
                },
                {
                    "value": 51,
                    "name": "\u667a\u80fd\u786c\u4ef6"
                },
                {
                    "value": 51,
                    "name": "\u6280\u80fd\u57f9\u8bad"
                },
                {
                    "value": 50,
                    "name": "Java"
                },
                {
                    "value": 48,
                    "name": "\u6570\u636e\u670d\u52a1\uff5c\u54a8\u8be2"
                },
                {
                    "value": 47,
                    "name": "\u6a21\u5f0f\u8bc6\u522b"
                },
                {
                    "value": 47,
                    "name": "\u5e26\u85aa\u5e74\u5047"
                },
                {
                    "value": 47,
                    "name": "\u8f6f\u4ef6\u670d\u52a1\uff5c\u54a8\u8be2"
                },
                {
                    "value": 42,
                    "name": "\u641c\u7d22\u7b97\u6cd5"
                },
                {
                    "value": 42,
                    "name": "\u8bed\u97f3\u8bc6\u522b"
                },
                {
                    "value": 39,
                    "name": "\u79fb\u52a8\u4e92\u8054\u7f51"
                },
                {
                    "value": 38,
                    "name": "\u5c97\u4f4d\u664b\u5347"
                },
                {
                    "value": 36,
                    "name": "\u56fe\u50cf\u5904\u7406"
                },
                {
                    "value": 34,
                    "name": "\u7269\u8054\u7f51"
                },
                {
                    "value": 33,
                    "name": "\u5f39\u6027\u5de5\u4f5c"
                },
                {
                    "value": 33,
                    "name": "\u79d1\u6280\u91d1\u878d"
                },
                {
                    "value": 33,
                    "name": "\u6241\u5e73\u7ba1\u7406"
                },
                {
                    "value": 32,
                    "name": "\u4e09\u7ef4\u56fe\u50cf\u89c6\u89c9"
                },
                {
                    "value": 32,
                    "name": "TensoFlow"
                },
                {
                    "value": 32,
                    "name": "\u9886\u5bfc\u597d"
                },
                {
                    "value": 31,
                    "name": "\u6587\u672c\u5206\u7c7b"
                },
                {
                    "value": 30,
                    "name": "NLP"
                },
                {
                    "value": 29,
                    "name": "OpenCV"
                },
                {
                    "value": 28,
                    "name": "\u8ba1\u7b97\u673a\u89c6\u89c9"
                },
                {
                    "value": 28,
                    "name": "\u76ee\u6807\u68c0\u6d4b"
                },
                {
                    "value": 27,
                    "name": "\u4e94\u9669\u4e00\u91d1"
                },
                {
                    "value": 27,
                    "name": "\u533b\u7597\u5065\u5eb7"
                },
                {
                    "value": 27,
                    "name": "PyTorch"
                },
                {
                    "value": 25,
                    "name": "IT\u6280\u672f\u670d\u52a1\uff5c\u54a8\u8be2"
                },
                {
                    "value": 25,
                    "name": "\u6587\u5b57\u8bc6\u522b"
                },
                {
                    "value": 24,
                    "name": "\u63a8\u8350\u7cfb\u7edf"
                },
                {
                    "value": 24,
                    "name": "\u793e\u4ea4\u5e73\u53f0"
                },
                {
                    "value": 23,
                    "name": "\u91d1\u878d"
                },
                {
                    "value": 23,
                    "name": "\u540e\u7aef\u5f00\u53d1"
                },
                {
                    "value": 23,
                    "name": "nan"
                },
                {
                    "value": 22,
                    "name": "\u81ea\u52a8\u9a7e\u9a76"
                },
                {
                    "value": 22,
                    "name": "\u65b0\u96f6\u552e"
                },
                {
                    "value": 21,
                    "name": "\u6e38\u620f"
                },
                {
                    "value": 21,
                    "name": "\u80a1\u7968\u671f\u6743"
                },
                {
                    "value": 19,
                    "name": "\u7535\u5546"
                },
                {
                    "value": 19,
                    "name": "\u8282\u65e5\u793c\u7269"
                },
                {
                    "value": 19,
                    "name": "\u5de5\u4e1a\u89c6\u89c9\u68c0\u6d4b"
                },
                {
                    "value": 18,
                    "name": "\u5e74\u5e95\u53cc\u85aa"
                },
                {
                    "value": 18,
                    "name": "\u5de5\u5177\u7c7b\u4ea7\u54c1"
                },
                {
                    "value": 17,
                    "name": "\u641c\u7d22"
                },
                {
                    "value": 17,
                    "name": "\u516d\u9669\u4e00\u91d1"
                },
                {
                    "value": 17,
                    "name": "\u5b9a\u671f\u4f53\u68c0"
                },
                {
                    "value": 17,
                    "name": "\u8bed\u97f3\u5408\u6210"
                },
                {
                    "value": 16,
                    "name": "\u5c31\u8fd1\u79df\u623f\u8865\u8d34"
                },
                {
                    "value": 16,
                    "name": "\u5728\u7ebf\u6559\u80b2"
                },
                {
                    "value": 16,
                    "name": "Hadoop"
                },
                {
                    "value": 16,
                    "name": "\u97f3\u9891\uff5c\u89c6\u9891\u5a92\u4f53"
                },
                {
                    "value": 16,
                    "name": "\u6559\u80b2"
                },
                {
                    "value": 15,
                    "name": "CNN"
                },
                {
                    "value": 15,
                    "name": "\u6570\u636e\u670d\u52a1"
                },
                {
                    "value": 14,
                    "name": "\u4e91\u8ba1\u7b97"
                },
                {
                    "value": 14,
                    "name": "C"
                },
                {
                    "value": 13,
                    "name": "\u514d\u8d39\u73ed\u8f66"
                },
                {
                    "value": 13,
                    "name": "\u4f01\u4e1a\u670d\u52a1"
                },
                {
                    "value": 13,
                    "name": "\u610f\u56fe\u8bc6\u522b"
                },
                {
                    "value": 13,
                    "name": "\u670d\u52a1\u673a\u5668\u4eba"
                },
                {
                    "value": 13,
                    "name": "\u6d88\u8d39\u751f\u6d3b"
                },
                {
                    "value": 13,
                    "name": "\u6587\u672c\u751f\u6210"
                },
                {
                    "value": 12,
                    "name": "\u6570\u636e\u5206\u6790"
                },
                {
                    "value": 12,
                    "name": "MATLAB"
                },
                {
                    "value": 12,
                    "name": "\u5efa\u6a21"
                },
                {
                    "value": 12,
                    "name": "\u533b\u7597\u5f71\u50cf\u8bca\u65ad"
                },
                {
                    "value": 12,
                    "name": "\u5728\u7ebf\u533b\u7597"
                },
                {
                    "value": 11,
                    "name": "\u5e7f\u544a\u8425\u9500"
                },
                {
                    "value": 11,
                    "name": "\u4fe1\u606f\u5b89\u5168"
                },
                {
                    "value": 11,
                    "name": "XGBoost"
                },
                {
                    "value": 11,
                    "name": "\u6570\u4ed3\u5efa\u6a21"
                },
                {
                    "value": 11,
                    "name": "\u8f85\u52a9/\u667a\u80fd\u9a7e\u9a76"
                },
                {
                    "value": 11,
                    "name": "\u793e\u4ea4"
                },
                {
                    "value": 11,
                    "name": "\u5e7f\u544a\u670d\u52a1"
                },
                {
                    "value": 11,
                    "name": "SLAM"
                },
                {
                    "value": 11,
                    "name": "\u65c5\u6e38\uff5c\u51fa\u884c"
                },
                {
                    "value": 10,
                    "name": "\u89c6\u9891/\u76d1\u63a7\u5206\u6790"
                },
                {
                    "value": 10,
                    "name": "\u7f51\u7edc\u901a\u4fe1"
                },
                {
                    "value": 10,
                    "name": "\u533b\u7597\uff5c\u4fdd\u5065\uff5c\u7f8e\u5bb9"
                },
                {
                    "value": 10,
                    "name": "\u5e7f\u544a\u7b97\u6cd5"
                },
                {
                    "value": 10,
                    "name": "\u8425\u9500\u670d\u52a1\uff5c\u54a8\u8be2"
                },
                {
                    "value": 10,
                    "name": "\u97f3\u9891\u7b97\u6cd5"
                },
                {
                    "value": 10,
                    "name": "\u4e13\u9879\u5956\u91d1"
                },
                {
                    "value": 10,
                    "name": "\u97f3\u4e50"
                },
                {
                    "value": 9,
                    "name": "\u5185\u5bb9\u8d44\u8baf"
                },
                {
                    "value": 9,
                    "name": "\u7ba1\u7406\u89c4\u8303"
                },
                {
                    "value": 9,
                    "name": "\u95ee\u7b54\u7cfb\u7edf"
                },
                {
                    "value": 9,
                    "name": "Spark"
                },
                {
                    "value": 9,
                    "name": "\u65b0\u80fd\u6e90\u6c7d\u8f66\u5236\u9020"
                },
                {
                    "value": 9,
                    "name": "AI"
                },
                {
                    "value": 8,
                    "name": "\u77ed\u89c6\u9891"
                },
                {
                    "value": 8,
                    "name": "\u7269\u6d41\uff5c\u8fd0\u8f93"
                },
                {
                    "value": 8,
                    "name": "\u5185\u5bb9\u793e\u533a"
                },
                {
                    "value": 8,
                    "name": "\u63a8\u8350"
                },
                {
                    "value": 8,
                    "name": "RNN"
                },
                {
                    "value": 7,
                    "name": "\u4fe1\u606f\u62bd\u53d6"
                },
                {
                    "value": 7,
                    "name": "\u4ea4\u901a\u8865\u52a9"
                },
                {
                    "value": 7,
                    "name": "Shell"
                },
                {
                    "value": 7,
                    "name": "Scala"
                },
                {
                    "value": 7,
                    "name": "Caffe"
                },
                {
                    "value": 7,
                    "name": "\u5de5\u5177\u8f6f\u4ef6"
                },
                {
                    "value": 7,
                    "name": "\u8fd0\u7b79\u4f18\u5316"
                },
                {
                    "value": 7,
                    "name": "\u4e2d\u6587\u5206\u8bcd"
                },
                {
                    "value": 6,
                    "name": "\u793e\u4ea4\u5a92\u4f53"
                },
                {
                    "value": 6,
                    "name": "\u8def\u5f84\u89c4\u5212"
                },
                {
                    "value": 6,
                    "name": "\u8bed\u97f3\u5904\u7406"
                },
                {
                    "value": 6,
                    "name": "\u673a\u5668\u4eba"
                },
                {
                    "value": 6,
                    "name": "\u77e5\u8bc6\u56fe\u8c31"
                },
                {
                    "value": 6,
                    "name": "\u529e\u516c\u903c\u683c\u9ad8"
                },
                {
                    "value": 6,
                    "name": "\u671f\u6743\u4e30\u539a"
                },
                {
                    "value": 6,
                    "name": "\u6ef4\u6ef4"
                },
                {
                    "value": 6,
                    "name": "\u7269\u6d41"
                },
                {
                    "value": 6,
                    "name": "\u5782\u76f4\u641c\u7d22"
                },
                {
                    "value": 6,
                    "name": "\u5927\u725b\u56e2\u961f"
                },
                {
                    "value": 6,
                    "name": "python"
                },
                {
                    "value": 6,
                    "name": "linux"
                },
                {
                    "value": 6,
                    "name": "SQL"
                },
                {
                    "value": 6,
                    "name": "\u8bcd\u6027\u6807\u6ce8"
                },
                {
                    "value": 5,
                    "name": "GAN"
                },
                {
                    "value": 5,
                    "name": "\u7b97\u6cd5\u5de5\u7a0b\u5e08"
                },
                {
                    "value": 5,
                    "name": "Keras"
                },
                {
                    "value": 5,
                    "name": "\u7f8e\u5973\u591a"
                },
                {
                    "value": 5,
                    "name": "TensorFlow"
                },
                {
                    "value": 5,
                    "name": "\u6559\u80b2\uff5c\u57f9\u8bad"
                },
                {
                    "value": 5,
                    "name": "\u7528\u6237\u753b\u50cf"
                },
                {
                    "value": 5,
                    "name": "\u751f\u6d3b\u670d\u52a1"
                },
                {
                    "value": 5,
                    "name": "spark"
                },
                {
                    "value": 5,
                    "name": "ARM"
                },
                {
                    "value": 5,
                    "name": "\u4e92\u8054\u7f51\u91d1\u878d"
                },
                {
                    "value": 5,
                    "name": "Linux"
                },
                {
                    "value": 5,
                    "name": "\u533a\u5757\u94fe"
                },
                {
                    "value": 5,
                    "name": "\u6570\u636e\u7ed3\u6784"
                },
                {
                    "value": 4,
                    "name": "\u5f3a\u5316\u5b66\u4e60"
                },
                {
                    "value": 4,
                    "name": "\u901a\u8baf\u6d25\u8d34"
                },
                {
                    "value": 4,
                    "name": "nlp\u7b97\u6cd5\u5de5\u7a0b\u5e08"
                },
                {
                    "value": 4,
                    "name": "\u53e5\u6cd5\u5206\u6790"
                },
                {
                    "value": 4,
                    "name": "HALCON"
                },
                {
                    "value": 4,
                    "name": "Hive"
                },
                {
                    "value": 4,
                    "name": "\u7cbe\u82f1\u56e2\u961f"
                },
                {
                    "value": 4,
                    "name": "MCN\uff5c\u76f4\u64ad\u5e73\u53f0"
                },
                {
                    "value": 4,
                    "name": "\u94f6\u884c"
                },
                {
                    "value": 4,
                    "name": "MySQL"
                },
                {
                    "value": 4,
                    "name": "\u673a\u5668\u7ffb\u8bd1"
                },
                {
                    "value": 4,
                    "name": "\u6587\u5316\u4f20\u5a92"
                },
                {
                    "value": 4,
                    "name": "CV"
                },
                {
                    "value": 4,
                    "name": "CTR\u9884\u4f30"
                },
                {
                    "value": 4,
                    "name": "\u673a\u5668\u89c6\u89c9"
                },
                {
                    "value": 4,
                    "name": "\u4e92\u8054\u7f51"
                },
                {
                    "value": 4,
                    "name": "\u56fe\u5f62"
                },
                {
                    "value": 4,
                    "name": "opencv"
                },
                {
                    "value": 4,
                    "name": "\u91d1\u878d\u4e1a"
                },
                {
                    "value": 4,
                    "name": "c++"
                },
                {
                    "value": 4,
                    "name": "\u6c7d\u8f66"
                },
                {
                    "value": 4,
                    "name": "\u8bed\u97f3\u7b97\u6cd5"
                },
                {
                    "value": 4,
                    "name": "kaggle"
                },
                {
                    "value": 4,
                    "name": "Tensorflow"
                },
                {
                    "value": 4,
                    "name": "Golang"
                },
                {
                    "value": 3,
                    "name": "\u4f18\u5316\u7b97\u6cd5"
                },
                {
                    "value": 3,
                    "name": "opengl"
                },
                {
                    "value": 3,
                    "name": "OCR"
                },
                {
                    "value": 3,
                    "name": "\u6c7d\u8f66\u4ea4\u6613\u5e73\u53f0"
                },
                {
                    "value": 3,
                    "name": "\u5d4c\u5165\u5f0f"
                },
                {
                    "value": 3,
                    "name": "\u89c6\u89c9"
                },
                {
                    "value": 3,
                    "name": "ROS"
                },
                {
                    "value": 3,
                    "name": "\u4fe1\u606f\u68c0\u7d22"
                },
                {
                    "value": 3,
                    "name": "\u89c6\u9891\u641c\u7d22"
                },
                {
                    "value": 3,
                    "name": "\u76f4\u64ad"
                },
                {
                    "value": 3,
                    "name": "\u8fea\u58eb\u5c3c"
                },
                {
                    "value": 3,
                    "name": "\u5de5\u4e1a\u4e92\u8054\u7f51"
                },
                {
                    "value": 3,
                    "name": "\u8ffd\u6c42\u6781\u81f4"
                },
                {
                    "value": 3,
                    "name": "\u65e0\u4eba\u8f66"
                },
                {
                    "value": 3,
                    "name": "\u667a\u80fd\u5bb6\u5c45"
                },
                {
                    "value": 3,
                    "name": "ROS\u7cfb\u7edf"
                },
                {
                    "value": 3,
                    "name": "\u89c6\u89c9\u7b97\u6cd5"
                },
                {
                    "value": 3,
                    "name": "GPU"
                },
                {
                    "value": 3,
                    "name": "\u533b\u7597\u5668\u68b0"
                },
                {
                    "value": 3,
                    "name": "\u6d41\u5a92\u4f53"
                },
                {
                    "value": 3,
                    "name": "tensorflow"
                },
                {
                    "value": 3,
                    "name": "\u8fd0\u7b79\u5b66"
                },
                {
                    "value": 3,
                    "name": "\u7acb\u4f53\u89c6\u89c9"
                },
                {
                    "value": 3,
                    "name": "\u6559\u80b2\u8f85\u5bfc"
                },
                {
                    "value": 3,
                    "name": "\u8f6f\u4ef6\u5f00\u53d1"
                },
                {
                    "value": 3,
                    "name": "\u540e\u7aef"
                },
                {
                    "value": 3,
                    "name": "\u7b97\u6cd5\u8bbe\u8ba1"
                },
                {
                    "value": 3,
                    "name": "\u5c45\u4f4f\u670d\u52a1"
                },
                {
                    "value": 3,
                    "name": "slam"
                },
                {
                    "value": 3,
                    "name": "\u70b9\u4e91"
                },
                {
                    "value": 3,
                    "name": "\u672c\u5206"
                },
                {
                    "value": 3,
                    "name": "ETA"
                },
                {
                    "value": 3,
                    "name": "\u56fe\u50cf\u8bc6\u522b"
                },
                {
                    "value": 3,
                    "name": "\u5730\u56fe"
                },
                {
                    "value": 3,
                    "name": "\u7269\u6d41\u5e73\u53f0"
                },
                {
                    "value": 3,
                    "name": "\u795e\u7ecf\u7f51\u7edc"
                },
                {
                    "value": 3,
                    "name": "\u5236\u9020\u4e1a"
                },
                {
                    "value": 3,
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5"
                },
                {
                    "value": 3,
                    "name": "\u5e74\u5ea6\u65c5\u6e38"
                },
                {
                    "value": 3,
                    "name": "\u4e30\u539a\u5e74\u7ec8"
                },
                {
                    "value": 3,
                    "name": "nlp"
                },
                {
                    "value": 2,
                    "name": "\u53cd\u4f5c\u5f0a"
                },
                {
                    "value": 2,
                    "name": "\u4f20\u611f\u5668"
                },
                {
                    "value": 2,
                    "name": "\u6027\u80fd\u6d4b\u8bd5"
                },
                {
                    "value": 2,
                    "name": "\u4ea7\u54c1\u8bbe\u8ba1"
                },
                {
                    "value": 2,
                    "name": "Lucene"
                },
                {
                    "value": 2,
                    "name": "\u5546\u4e1a\u822a\u5929"
                },
                {
                    "value": 2,
                    "name": "\u8fd0\u52a8\u63a7\u5236"
                },
                {
                    "value": 2,
                    "name": "\u97f3\u89c6\u9891"
                },
                {
                    "value": 2,
                    "name": "\u786c\u4ef6\u5236\u9020"
                },
                {
                    "value": 2,
                    "name": "\u7c7b\u8111\u8ba1\u7b97"
                },
                {
                    "value": 2,
                    "name": "OpenCL"
                },
                {
                    "value": 2,
                    "name": "\u7248\u9762\u5206\u6790"
                },
                {
                    "value": 2,
                    "name": "\u5e74\u7ec8\u5206\u7ea2"
                },
                {
                    "value": 2,
                    "name": "\u5168\u7403\u5316"
                },
                {
                    "value": 2,
                    "name": "\u51fa\u56fd\u65c5\u6e38"
                },
                {
                    "value": 2,
                    "name": "\u5348\u9910\u8865\u52a9"
                },
                {
                    "value": 2,
                    "name": "GBDT"
                },
                {
                    "value": 2,
                    "name": "hadoop"
                },
                {
                    "value": 2,
                    "name": "\u5206\u5e03\u5f0f\u641c\u7d22"
                },
                {
                    "value": 2,
                    "name": "\u6280\u672f\u7ba1\u7406"
                },
                {
                    "value": 2,
                    "name": "\u7528\u6237\u5339\u914d\u7b97\u6cd5"
                },
                {
                    "value": 2,
                    "name": "\u6570\u4ed3\u67b6\u6784"
                },
                {
                    "value": 2,
                    "name": "PaddlePddle"
                },
                {
                    "value": 2,
                    "name": "\u7cfb\u7edf\u67b6\u6784"
                },
                {
                    "value": 2,
                    "name": "\u9700\u6c42\u5206\u6790"
                },
                {
                    "value": 2,
                    "name": "\u8f66\u8054\u7f51"
                },
                {
                    "value": 2,
                    "name": "\u805a\u7c7b"
                },
                {
                    "value": 2,
                    "name": "SNN"
                },
                {
                    "value": 2,
                    "name": "\u667a\u6167\u57ce\u5e02"
                },
                {
                    "value": 2,
                    "name": "\u4eba\u8138\u751f\u6210"
                },
                {
                    "value": 2,
                    "name": "\u901a\u4fe1/\u7f51\u7edc\u8bbe\u5907"
                },
                {
                    "value": 2,
                    "name": "\u5de5\u4e1a\u68c0\u6d4b"
                },
                {
                    "value": 2,
                    "name": "C#"
                },
                {
                    "value": 2,
                    "name": "matlab"
                },
                {
                    "value": 2,
                    "name": "\u793e\u4ea4\u5a92\u4f53\u5e73\u53f0"
                },
                {
                    "value": 2,
                    "name": "\u7528\u6237\u589e\u957f"
                },
                {
                    "value": 2,
                    "name": "\u8111\u673a"
                },
                {
                    "value": 2,
                    "name": "\u6587\u672c\u8574\u6db5"
                },
                {
                    "value": 2,
                    "name": "Pytorch"
                },
                {
                    "value": 2,
                    "name": "\u7535\u673a\u63a7\u5236"
                },
                {
                    "value": 2,
                    "name": "\u6570\u636e\u5e93"
                },
                {
                    "value": 2,
                    "name": "DSP"
                },
                {
                    "value": 2,
                    "name": "JAVA"
                },
                {
                    "value": 2,
                    "name": "Node.js"
                },
                {
                    "value": 2,
                    "name": "\u667a\u80fd\u91d1\u878d"
                },
                {
                    "value": 2,
                    "name": "\u6e38\u620fAI\u7814\u53d1"
                },
                {
                    "value": 2,
                    "name": "ACM"
                },
                {
                    "value": 2,
                    "name": "\u4e03\u9669\u4e00\u91d1"
                },
                {
                    "value": 2,
                    "name": "\u89c6\u9891\u7b97\u6cd5"
                },
                {
                    "value": 2,
                    "name": "\u8ba1\u7b97\u673a\u56fe\u5f62\u5b66"
                },
                {
                    "value": 2,
                    "name": "CAD"
                },
                {
                    "value": 2,
                    "name": "\u533b\u7597"
                },
                {
                    "value": 2,
                    "name": "Flink"
                },
                {
                    "value": 2,
                    "name": "RTK"
                },
                {
                    "value": 2,
                    "name": "\u5b9a\u4f4d\u7b97\u6cd5"
                },
                {
                    "value": 2,
                    "name": "3D"
                },
                {
                    "value": 2,
                    "name": "LR"
                },
                {
                    "value": 2,
                    "name": "\u56fe\u50cf\u5206\u5272"
                },
                {
                    "value": 2,
                    "name": "\u5e05\u54e5\u591a"
                },
                {
                    "value": 2,
                    "name": "\u5206\u7c7b"
                },
                {
                    "value": 2,
                    "name": "\u6570\u636e\u4ed3\u5e93"
                },
                {
                    "value": 2,
                    "name": "ElasticSearch"
                },
                {
                    "value": 2,
                    "name": "OpenGL"
                },
                {
                    "value": 2,
                    "name": "\u89c6\u9891"
                },
                {
                    "value": 2,
                    "name": "\u53cc\u76ee"
                },
                {
                    "value": 2,
                    "name": "VIO"
                },
                {
                    "value": 2,
                    "name": "\u91d1\u878d\u98ce\u63a7"
                },
                {
                    "value": 2,
                    "name": "\u89c6\u9891\u7406\u89e3"
                },
                {
                    "value": 2,
                    "name": "\u5206\u7c7b\u4fe1\u606f"
                },
                {
                    "value": 2,
                    "name": "AR"
                },
                {
                    "value": 2,
                    "name": "\u7ade\u54c1\u5206\u6790"
                },
                {
                    "value": 1,
                    "name": "\u4e09\u7ef4"
                },
                {
                    "value": 1,
                    "name": "OpenMesh"
                },
                {
                    "value": 1,
                    "name": "MCU"
                },
                {
                    "value": 1,
                    "name": "\u5206\u5e03\u5f0f"
                },
                {
                    "value": 1,
                    "name": "\u5de5\u7a0b\u80fd\u529b"
                },
                {
                    "value": 1,
                    "name": "\u5185\u5bb9\u7406\u89e3"
                },
                {
                    "value": 1,
                    "name": "\u5956\u91d1\u591a\u591a\u591a"
                },
                {
                    "value": 1,
                    "name": "R"
                },
                {
                    "value": 1,
                    "name": "\u8bed\u4e49\u7406\u89e3"
                },
                {
                    "value": 1,
                    "name": "\u964d\u566a"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u8fd0\u7b79\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u5305\u5348\u9910\u665a\u9910"
                },
                {
                    "value": 1,
                    "name": "\u52a8\u4f5c\u8bc6\u522b"
                },
                {
                    "value": 1,
                    "name": "\u5b8c\u6210E\u8f6e\u878d\u8d44"
                },
                {
                    "value": 1,
                    "name": "\u63a7\u5236\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u673a\u5668\u5b66\u4e60\u6a21\u578b"
                },
                {
                    "value": 1,
                    "name": "\u8bed\u4e49\u5206\u6790"
                },
                {
                    "value": 1,
                    "name": "\u5b9e\u4f53\u8bc6\u522b"
                },
                {
                    "value": 1,
                    "name": "AI\u56fe\u50cf\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "rtk\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "salm"
                },
                {
                    "value": 1,
                    "name": "\u4e70\u624b\u6218\u7565"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u6a21\u578b"
                },
                {
                    "value": 1,
                    "name": "XGB"
                },
                {
                    "value": 1,
                    "name": "\u5d4c\u5165\u5f0f\u6280\u672f"
                },
                {
                    "value": 1,
                    "name": "libvpx"
                },
                {
                    "value": 1,
                    "name": "\u65e0\u4eba\u9a7e\u9a76"
                },
                {
                    "value": 1,
                    "name": "ACC/AEB/LKA"
                },
                {
                    "value": 1,
                    "name": "\u97f3\u9891\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "AutoML"
                },
                {
                    "value": 1,
                    "name": "\u5f00\u53d1"
                },
                {
                    "value": 1,
                    "name": "PCL"
                },
                {
                    "value": 1,
                    "name": "3dmm"
                },
                {
                    "value": 1,
                    "name": "3D\u5f15\u64ce"
                },
                {
                    "value": 1,
                    "name": "\u6392\u5e8f\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u6570\u636e\u5f00\u53d1"
                },
                {
                    "value": 1,
                    "name": "\u6280\u672f\u5927\u725b\u591a"
                },
                {
                    "value": 1,
                    "name": "\u878d\u5408IMU"
                },
                {
                    "value": 1,
                    "name": "X264"
                },
                {
                    "value": 1,
                    "name": "\u907f\u969c"
                },
                {
                    "value": 1,
                    "name": "\u6d4b\u8bd5\u5f00\u53d1"
                },
                {
                    "value": 1,
                    "name": "\u5e7f\u544a\u53ec\u56de"
                },
                {
                    "value": 1,
                    "name": "SOA"
                },
                {
                    "value": 1,
                    "name": "\u65b0\u5a92\u4f53"
                },
                {
                    "value": 1,
                    "name": "\u8425\u9500\u4e1a\u52a1"
                },
                {
                    "value": 1,
                    "name": "\u56de\u58f0\u6d88\u9664"
                },
                {
                    "value": 1,
                    "name": "\u5e74\u7ec8\u5956\u91d1"
                },
                {
                    "value": 1,
                    "name": "VTK"
                },
                {
                    "value": 1,
                    "name": "\u4e13\u4e1a\u670d\u52a1\uff5c\u54a8\u8be2"
                },
                {
                    "value": 1,
                    "name": "\u51e0\u4f55\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u6df7\u54cd"
                },
                {
                    "value": 1,
                    "name": "\u5168\u94fe\u8defSaaS\u5e73\u53f0"
                },
                {
                    "value": 1,
                    "name": "3D\u59ff\u6001\u91cd\u5efa"
                },
                {
                    "value": 1,
                    "name": "\u8bed\u4e49\u5206\u5272"
                },
                {
                    "value": 1,
                    "name": "3D\u89c6\u89c9\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u8fd0\u52a8\u63a7\u5236\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "3DGIS"
                },
                {
                    "value": 1,
                    "name": "CAD\u56fe\u7eb8\u5206\u6790"
                },
                {
                    "value": 1,
                    "name": "\u89c6\u89c9slam"
                },
                {
                    "value": 1,
                    "name": "\u5e95\u5c42\u89c6\u89c9"
                },
                {
                    "value": 1,
                    "name": "\u8bed\u97f3\u524d\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "\u4e0b\u5348\u8336"
                },
                {
                    "value": 1,
                    "name": "NLP/CV"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u52a8\u5316"
                },
                {
                    "value": 1,
                    "name": "\u4eff\u771f\u4eba"
                },
                {
                    "value": 1,
                    "name": "DSP\u7f16\u7a0b"
                },
                {
                    "value": 1,
                    "name": "\u4eff\u771f"
                },
                {
                    "value": 1,
                    "name": "\u9ed1\u76d2\u6d4b\u8bd5"
                },
                {
                    "value": 1,
                    "name": "AIOPS"
                },
                {
                    "value": 1,
                    "name": "\u65f6\u5e8f\u6570\u636e\u5e93"
                },
                {
                    "value": 1,
                    "name": "\u79d1\u6280\u5927\u725b\u516c\u53f8"
                },
                {
                    "value": 1,
                    "name": "\u673a\u5668\u4eba\u89c6\u89c9"
                },
                {
                    "value": 1,
                    "name": "\u91d1\u878d\u5238\u5546"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u56fe\u50cf"
                },
                {
                    "value": 1,
                    "name": "\u5206\u5e03\u5f0f\u8bad\u7ec3"
                },
                {
                    "value": 1,
                    "name": "ESMM"
                },
                {
                    "value": 1,
                    "name": "\u7279\u6548"
                },
                {
                    "value": 1,
                    "name": "\u7528\u6237\u7814\u7a76"
                },
                {
                    "value": 1,
                    "name": "rgbd"
                },
                {
                    "value": 1,
                    "name": "\u6df1\u5ea6\u4f30\u8ba1\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u534f\u540c\u8fc7\u6ee4"
                },
                {
                    "value": 1,
                    "name": "SSD\u3001Faster"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u4eff\u771f"
                },
                {
                    "value": 1,
                    "name": "\u641c\u7d22\u5f15\u64ce"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u50cf\u589e\u5f3a"
                },
                {
                    "value": 1,
                    "name": "\u5065\u5eb7\u7761\u7720"
                },
                {
                    "value": 1,
                    "name": "3D\u89c6\u89c9"
                },
                {
                    "value": 1,
                    "name": "KALDI"
                },
                {
                    "value": 1,
                    "name": "h264\uff0ch265\uff0cav1"
                },
                {
                    "value": 1,
                    "name": "Pulp"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u50cf"
                },
                {
                    "value": 1,
                    "name": "CPU"
                },
                {
                    "value": 1,
                    "name": "\u6570\u636e\u6e05\u6d17"
                },
                {
                    "value": 1,
                    "name": "\u5f3a\u608d\u7684\u521b\u59cb\u4eba"
                },
                {
                    "value": 1,
                    "name": "HBase"
                },
                {
                    "value": 1,
                    "name": "\u6a21\u578b"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u52a9\u4e09\u9910"
                },
                {
                    "value": 1,
                    "name": "\u8f66\u8f86\u8fd0\u52a8\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u6e32\u67d3"
                },
                {
                    "value": 1,
                    "name": "\u9ad8\u7ea7\u6280\u672f\u7ba1\u7406"
                },
                {
                    "value": 1,
                    "name": "LTE"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u63a8\u8350"
                },
                {
                    "value": 1,
                    "name": "MatLab"
                },
                {
                    "value": 1,
                    "name": "\u89c6\u9891\u9884\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "CTR"
                },
                {
                    "value": 1,
                    "name": "cuda"
                },
                {
                    "value": 1,
                    "name": "\u9065\u611f"
                },
                {
                    "value": 1,
                    "name": "\u8f66\u8f86\u52a8\u529b\u5b66\u5efa\u6a21"
                },
                {
                    "value": 1,
                    "name": "\u5546\u54c1\u6a21\u578b"
                },
                {
                    "value": 1,
                    "name": "ISP"
                },
                {
                    "value": 1,
                    "name": "flv\uff0cmp3\uff0cmp4"
                },
                {
                    "value": 1,
                    "name": "\u5bfc\u822a\u5b9a\u4f4d"
                },
                {
                    "value": 1,
                    "name": "\u6ee4\u955c"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u6587\u5206\u6790"
                },
                {
                    "value": 1,
                    "name": "\u6570\u636e\u7ba1\u7406"
                },
                {
                    "value": 1,
                    "name": "Tensor"
                },
                {
                    "value": 1,
                    "name": "\u641c\u7d22\u6392\u5e8f"
                },
                {
                    "value": 1,
                    "name": "\u57fa\u7840\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "Go"
                },
                {
                    "value": 1,
                    "name": "\u89c6\u9891\u5206\u6790"
                },
                {
                    "value": 1,
                    "name": "hybrid/end2end"
                },
                {
                    "value": 1,
                    "name": "openGL"
                },
                {
                    "value": 1,
                    "name": "\u4e0a\u5e02\u516c\u53f8"
                },
                {
                    "value": 1,
                    "name": "\u540d\u6821\u540d\u4f01\u80cc\u666f"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u7136\u8bed\u8a00"
                },
                {
                    "value": 1,
                    "name": "\u9aa8\u79d1\u673a\u5668\u4eba"
                },
                {
                    "value": 1,
                    "name": "\u7f51\u7edc\u4f20\u8f93\u534f\u8bae"
                },
                {
                    "value": 1,
                    "name": "\u6570\u636e\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "\u641c\u7d22\u53ec\u56de"
                },
                {
                    "value": 1,
                    "name": "asr"
                },
                {
                    "value": 1,
                    "name": "\u8fd0\u7b79"
                },
                {
                    "value": 1,
                    "name": "\u5927\u6570\u636e\u8f6f\u4ef6"
                },
                {
                    "value": 1,
                    "name": "ADAS"
                },
                {
                    "value": 1,
                    "name": "Cplex"
                },
                {
                    "value": 1,
                    "name": "\u5348\u9910\u4ea4\u901a\u8865\u52a9"
                },
                {
                    "value": 1,
                    "name": "GO"
                },
                {
                    "value": 1,
                    "name": "\u8bed\u97f3\u6d4b\u8bc4"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u50cf\u538b\u7f29"
                },
                {
                    "value": 1,
                    "name": "/"
                },
                {
                    "value": 1,
                    "name": "\u751f\u7406\u53c2\u6570"
                },
                {
                    "value": 1,
                    "name": "\u6392\u5e8f"
                },
                {
                    "value": 1,
                    "name": "react"
                },
                {
                    "value": 1,
                    "name": "\u67b6\u6784\u5e08"
                },
                {
                    "value": 1,
                    "name": "\u591a\u4f20\u611f\u5668\u878d\u5408"
                },
                {
                    "value": 1,
                    "name": "SSL/TLS"
                },
                {
                    "value": 1,
                    "name": "pandas"
                },
                {
                    "value": 1,
                    "name": "\u5de5\u4e1a\u6392\u7a0b"
                },
                {
                    "value": 1,
                    "name": "h264"
                },
                {
                    "value": 1,
                    "name": "\u5730\u56fe\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u78c1\u529b\u8ba1"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u8ba1\u7b97"
                },
                {
                    "value": 1,
                    "name": "\u5168\u5458\u51fa\u56fd\u6e38"
                },
                {
                    "value": 1,
                    "name": "\u751f\u4ea7\u8c03\u5ea6"
                },
                {
                    "value": 1,
                    "name": "\u6570\u5b57\u56fe\u50cf\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "BIM+3D"
                },
                {
                    "value": 1,
                    "name": "\u58f0\u7eb9\u8bc6\u522b"
                },
                {
                    "value": 1,
                    "name": "Gurobi"
                },
                {
                    "value": 1,
                    "name": "\u901a\u4fe1"
                },
                {
                    "value": 1,
                    "name": "PPP"
                },
                {
                    "value": 1,
                    "name": "CGAL"
                },
                {
                    "value": 1,
                    "name": "\u5927\u6570\u636e\u5904\u7406\u6280\u672f"
                },
                {
                    "value": 1,
                    "name": "\u5e74\u7ec8\u591a\u85aa"
                },
                {
                    "value": 1,
                    "name": "AI\u4ea7\u54c1"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u843d\u5730"
                },
                {
                    "value": 1,
                    "name": "\u5f02\u5e38\u8bca\u65ad"
                },
                {
                    "value": 1,
                    "name": "LSTM"
                },
                {
                    "value": 1,
                    "name": "\u5173\u7cfb\u6316\u6398"
                },
                {
                    "value": 1,
                    "name": "\u70b9\u4e91\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u5149\u5b66"
                },
                {
                    "value": 1,
                    "name": "\u98ce\u63a7\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u9009\u578b"
                },
                {
                    "value": 1,
                    "name": "docker"
                },
                {
                    "value": 1,
                    "name": "VINS"
                },
                {
                    "value": 1,
                    "name": "\u5355\u76ee"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u5f62\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "\u5de5\u5177\u793e\u533a"
                },
                {
                    "value": 1,
                    "name": "java"
                },
                {
                    "value": 1,
                    "name": "nlp\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u8c03\u62e8"
                },
                {
                    "value": 1,
                    "name": "\u5927\u5e73\u53f0"
                },
                {
                    "value": 1,
                    "name": "PID\u63a7\u5236"
                },
                {
                    "value": 1,
                    "name": "\u56e2\u961f\u7ba1\u7406"
                },
                {
                    "value": 1,
                    "name": "\u786c\u4ef6\u52a0\u901f"
                },
                {
                    "value": 1,
                    "name": "\u4e09\u7ef4\u91cd\u5efa"
                },
                {
                    "value": 1,
                    "name": "Matlab"
                },
                {
                    "value": 1,
                    "name": "\u5bfc\u822a\u5f15\u64ce"
                },
                {
                    "value": 1,
                    "name": "python/go"
                },
                {
                    "value": 1,
                    "name": "\u9a6c\u5c14\u514b\u592b\u968f\u673a\u52a8"
                },
                {
                    "value": 1,
                    "name": "ppp-rtk"
                },
                {
                    "value": 1,
                    "name": "\u5e7f\u544a\u5e73\u53f0"
                },
                {
                    "value": 1,
                    "name": "\u901a\u4fe1\u539f\u7406"
                },
                {
                    "value": 1,
                    "name": "SaaS"
                },
                {
                    "value": 1,
                    "name": "GNSS\u5b9a\u4f4d"
                },
                {
                    "value": 1,
                    "name": "TF"
                },
                {
                    "value": 1,
                    "name": "\u514d\u8d39\u5348\u9910\u665a\u9910"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u5b9a\u4f4d"
                },
                {
                    "value": 1,
                    "name": "3D\u6253\u5370"
                },
                {
                    "value": 1,
                    "name": "\u97f3\u9891\u7f16\u89e3\u7801"
                },
                {
                    "value": 1,
                    "name": "\u4e09\u7ef4\u91cd\u6784"
                },
                {
                    "value": 1,
                    "name": "\u641c\u7d22\u63a8\u8350"
                },
                {
                    "value": 1,
                    "name": "Linux\u5f00\u53d1"
                },
                {
                    "value": 1,
                    "name": "Attention"
                },
                {
                    "value": 1,
                    "name": "\u5bfc\u822a"
                },
                {
                    "value": 1,
                    "name": "\u9ad8\u7cbe\u5ea6\u5730\u56fe"
                },
                {
                    "value": 1,
                    "name": "SVC"
                },
                {
                    "value": 1,
                    "name": "\u8fde\u7eed\u521b\u4e1a\u56e2\u961f"
                },
                {
                    "value": 1,
                    "name": "kaldi"
                },
                {
                    "value": 1,
                    "name": "\u5de5\u4e1a\u81ea\u52a8\u5316"
                },
                {
                    "value": 1,
                    "name": "\u52a8\u4f5c\u6355\u6349"
                },
                {
                    "value": 1,
                    "name": "\u6570\u636e\u6316\u6398\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u5927\u5730\u6d4b\u91cf"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u50cf\u8f6c\u6362"
                },
                {
                    "value": 1,
                    "name": "C++/python"
                },
                {
                    "value": 1,
                    "name": "\u5373\u65f6\u901a\u8baf"
                },
                {
                    "value": 1,
                    "name": "\u96f6\u77e5\u8bc6\u8bc1\u660e"
                },
                {
                    "value": 1,
                    "name": "\u6709\u524d\u9014"
                },
                {
                    "value": 1,
                    "name": "ECC"
                },
                {
                    "value": 1,
                    "name": "Rust"
                },
                {
                    "value": 1,
                    "name": "\u7279\u5f81\u5de5\u7a0b"
                },
                {
                    "value": 1,
                    "name": "\u6a21\u62df\u9000\u706b\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "GIS"
                },
                {
                    "value": 1,
                    "name": "\u7acb\u4f53\u5339\u914d"
                },
                {
                    "value": 1,
                    "name": "\u5e7f\u544aCTR/CVR"
                },
                {
                    "value": 1,
                    "name": "\u6a21\u578b\u79fb\u690d\u4f18\u5316"
                },
                {
                    "value": 1,
                    "name": "\u8def\u5f84\u4f18\u5316"
                },
                {
                    "value": 1,
                    "name": "MXNet"
                },
                {
                    "value": 1,
                    "name": "ADAS\u7cfb\u7edf\u5f00\u53d1"
                },
                {
                    "value": 1,
                    "name": "webGL"
                },
                {
                    "value": 1,
                    "name": "\u4e92\u8054\u7f51+"
                },
                {
                    "value": 1,
                    "name": "\u5730\u56fe\u5f00\u53d1"
                },
                {
                    "value": 1,
                    "name": "AILab"
                },
                {
                    "value": 1,
                    "name": "3DCAD"
                },
                {
                    "value": 1,
                    "name": "\u6570\u5b57\u4fe1\u53f7\u5904\u7406\u6570"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u57fa\u7840"
                },
                {
                    "value": 1,
                    "name": "\u5e74\u7ec8\u5956"
                },
                {
                    "value": 1,
                    "name": "\u4f20\u611f\u5668\u878d\u5408"
                },
                {
                    "value": 1,
                    "name": "\u4eba\u4f533D\u91cd\u5efa"
                },
                {
                    "value": 1,
                    "name": "\u4f4f\u798f\u8ba1\u5212"
                },
                {
                    "value": 1,
                    "name": "\u4e50\u7406\u8f6c\u6362"
                },
                {
                    "value": 1,
                    "name": "\u8def\u51b5\u8ba1\u7b97"
                },
                {
                    "value": 1,
                    "name": "pytorch"
                },
                {
                    "value": 1,
                    "name": "\u4f11\u95f2\uff5c\u5a31\u4e50"
                },
                {
                    "value": 1,
                    "name": "\u4f18\u5148\u4e0a\u6d77\u843d\u6237"
                },
                {
                    "value": 1,
                    "name": "/Pytorch"
                },
                {
                    "value": 1,
                    "name": "\u9886\u519b\u4f01\u4e1a"
                },
                {
                    "value": 1,
                    "name": "\u5e7f\u544a\u7b56\u7565"
                },
                {
                    "value": 1,
                    "name": "\u7279\u5f81\u6316\u6398"
                },
                {
                    "value": 1,
                    "name": "\u5bc6\u7801\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u6392\u7a0b"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u4e3b\u664b\u5347\u8ba1\u5212"
                },
                {
                    "value": 1,
                    "name": "NLP\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u53ec\u56de\u7b56\u7565"
                },
                {
                    "value": 1,
                    "name": "\u4e09\u7ef4\u56fe\u5f62"
                },
                {
                    "value": 1,
                    "name": "\u5de5\u4e1a\u9886\u57df"
                },
                {
                    "value": 1,
                    "name": "\u5b9e\u65f6\u8def\u51b5"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u7136\u8bed\u8a00\u5904"
                },
                {
                    "value": 1,
                    "name": "ETL"
                },
                {
                    "value": 1,
                    "name": "B2B"
                },
                {
                    "value": 1,
                    "name": "\u6241\u5e73\u5316\u7ba1\u7406"
                },
                {
                    "value": 1,
                    "name": "RCN"
                },
                {
                    "value": 1,
                    "name": "\u516c\u94a5"
                },
                {
                    "value": 1,
                    "name": "\u89c4\u5212"
                },
                {
                    "value": 1,
                    "name": "\u8f68\u8ff9\u89c4\u5212"
                },
                {
                    "value": 1,
                    "name": "\u97f3\u89c6\u9891\u7f16\u89e3\u7801"
                },
                {
                    "value": 1,
                    "name": "\u89c6\u89c9SLAM"
                },
                {
                    "value": 1,
                    "name": "AEB"
                },
                {
                    "value": 1,
                    "name": "\u8fd0\u7ef4\u7ba1\u7406"
                },
                {
                    "value": 1,
                    "name": "\u672c\u5730\u751f\u6d3b"
                },
                {
                    "value": 1,
                    "name": "\u4e2a\u6027\u5316\u63a8\u8350"
                },
                {
                    "value": 1,
                    "name": "\u591a\u4f20\u611f\u5668"
                },
                {
                    "value": 1,
                    "name": "\u4e09\u7ef4\u7f51\u683c/\u70b9\u4e91"
                },
                {
                    "value": 1,
                    "name": "\u5927\u5065\u5eb7"
                },
                {
                    "value": 1,
                    "name": "\u9057\u4f20\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u65c5\u6e38"
                },
                {
                    "value": 1,
                    "name": "\u8fd1\u7ea2\u5916"
                },
                {
                    "value": 1,
                    "name": "\u533b\u7597\u884c\u4e1a"
                },
                {
                    "value": 1,
                    "name": "\u878d\u5408\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u90e8\u7f72"
                },
                {
                    "value": 1,
                    "name": "DeepFM"
                },
                {
                    "value": 1,
                    "name": "\u5e7f\u544a\u65b9\u5411\u7b97\u6cd5\u5de5"
                },
                {
                    "value": 1,
                    "name": "\u5468\u672b\u53cc\u4f11"
                },
                {
                    "value": 1,
                    "name": "\u6570\u5b57\u97f3\u9891\u6c34\u5370"
                },
                {
                    "value": 1,
                    "name": "\u4f20\u611f\u5668\u6216\u70b9\u4e91"
                },
                {
                    "value": 1,
                    "name": "\u9879\u76ee\u7ba1\u7406"
                },
                {
                    "value": 1,
                    "name": "\u4e92\u8054\u7f51\u51fa\u884c"
                },
                {
                    "value": 1,
                    "name": "\u65b0\u80fd\u6e90"
                },
                {
                    "value": 1,
                    "name": "neon"
                },
                {
                    "value": 1,
                    "name": "Windows"
                },
                {
                    "value": 1,
                    "name": "\u611f\u77e5\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u5bfc\u822a\u89c4\u5212"
                },
                {
                    "value": 1,
                    "name": "\u5f71\u89c6\uff5c\u52a8\u6f2b"
                },
                {
                    "value": 1,
                    "name": "\u8bad\u7ec3\u52a0\u901f"
                },
                {
                    "value": 1,
                    "name": "\u7535\u5546\u641c\u7d22"
                },
                {
                    "value": 1,
                    "name": "\u5730\u7406\u8f68\u8ff9"
                },
                {
                    "value": 1,
                    "name": "\u533b\u5b66\u5f71\u50cf"
                },
                {
                    "value": 1,
                    "name": "\u51e0\u4f55\u5b66"
                },
                {
                    "value": 1,
                    "name": "\u6a21\u578b\u538b\u7f29"
                },
                {
                    "value": 1,
                    "name": "HADOOP"
                },
                {
                    "value": 1,
                    "name": "FLINK"
                },
                {
                    "value": 1,
                    "name": "\u6570\u636e\u6293\u53d6"
                },
                {
                    "value": 1,
                    "name": "\u539f\u578b\u8bbe\u8ba1"
                },
                {
                    "value": 1,
                    "name": "\u5a92\u4f53"
                },
                {
                    "value": 1,
                    "name": "\u865a\u5047\u6d41\u91cf"
                },
                {
                    "value": 1,
                    "name": "\u4e91\u5b89\u5168"
                },
                {
                    "value": 1,
                    "name": "\u53ec\u56de"
                },
                {
                    "value": 1,
                    "name": "\u8bed\u97f3\u8f6c\u6362"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u5bfc\u822a"
                },
                {
                    "value": 1,
                    "name": "\u4e34\u5e8a\u79d1\u7814"
                },
                {
                    "value": 1,
                    "name": "\u8def\u51b5\u4f18\u5316"
                },
                {
                    "value": 1,
                    "name": "Caffe\u3001Pytorch\u3001"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u5f62\u56fe\u50cf\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "UWB"
                },
                {
                    "value": 1,
                    "name": "\u8d44\u8baf"
                },
                {
                    "value": 1,
                    "name": "\u3001Spark"
                },
                {
                    "value": 1,
                    "name": "GPS"
                },
                {
                    "value": 1,
                    "name": "\u97f3\u89c6\u9891\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "ERP"
                },
                {
                    "value": 1,
                    "name": "AR/VR/MR"
                },
                {
                    "value": 1,
                    "name": "\u6a21\u7cca\u63a7\u5236"
                },
                {
                    "value": 1,
                    "name": "\u65e0\u76d1\u7763\u5b66\u4e60"
                },
                {
                    "value": 1,
                    "name": "KF/EKF"
                },
                {
                    "value": 1,
                    "name": "\u53bb\u6df7\u54cd"
                },
                {
                    "value": 1,
                    "name": "Database"
                },
                {
                    "value": 1,
                    "name": "numpy"
                },
                {
                    "value": 1,
                    "name": "\u6587\u672c\u68c0\u6d4b"
                },
                {
                    "value": 1,
                    "name": "\u773c\u52a8"
                },
                {
                    "value": 1,
                    "name": "\u6295\u8d44/\u878d\u8d44"
                },
                {
                    "value": 1,
                    "name": "\u591c\u62cd"
                },
                {
                    "value": 1,
                    "name": "\u4ea7\u54c1\u7b56\u5212"
                },
                {
                    "value": 1,
                    "name": "c"
                },
                {
                    "value": 1,
                    "name": "NLP\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "PID"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u7b56\u7565"
                },
                {
                    "value": 1,
                    "name": "\u77e9\u9635\u5206\u6790"
                },
                {
                    "value": 1,
                    "name": "\u5de5\u4e1a\u89c6\u89c9\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u542f\u53d1\u5f0f\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u7cbe\u5bc6\u5355\u70b9\u5b9a\u4f4d"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u5e73\u53f0"
                },
                {
                    "value": 1,
                    "name": "\u8d85\u957f\u5e26\u85aa\u5047\u671f"
                },
                {
                    "value": 1,
                    "name": "\u91d1\u878d\u79d1\u6280"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u5f62\u56fe\u50cf"
                },
                {
                    "value": 1,
                    "name": "Transformer"
                },
                {
                    "value": 1,
                    "name": "\u6280\u672f\u5927\u725b\u4f17\u591a"
                },
                {
                    "value": 1,
                    "name": "x265"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u5f62\u5b66"
                },
                {
                    "value": 1,
                    "name": "\u65f6\u95f4\u5e8f\u5217"
                },
                {
                    "value": 1,
                    "name": "\u9ad8\u7cbe\u5730\u56fe"
                },
                {
                    "value": 1,
                    "name": "AGV"
                },
                {
                    "value": 1,
                    "name": "\u673a\u5668\u5b66\u4e60\u7b97\u6cd5\u673a"
                },
                {
                    "value": 1,
                    "name": "query"
                },
                {
                    "value": 1,
                    "name": "\u626b\u5730\u673a\u5668\u4eba"
                },
                {
                    "value": 1,
                    "name": "PHM"
                },
                {
                    "value": 1,
                    "name": "JitterBuffer"
                },
                {
                    "value": 1,
                    "name": "NPL"
                },
                {
                    "value": 1,
                    "name": "NPU"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u5206\u6790"
                },
                {
                    "value": 1,
                    "name": "android"
                },
                {
                    "value": 1,
                    "name": "\u542f\u53d1\u5f0f\u89c4\u5219\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u52a8\u5316\u6d4b\u8bd5"
                },
                {
                    "value": 1,
                    "name": "\u79d1\u7814"
                },
                {
                    "value": 1,
                    "name": "\u7f16\u7a0b"
                },
                {
                    "value": 1,
                    "name": "\u5e7f\u544a\u6295\u653e"
                },
                {
                    "value": 1,
                    "name": "\u4e50\u5668"
                },
                {
                    "value": 1,
                    "name": "\u91d1\u878d\u98ce\u63a7AI"
                },
                {
                    "value": 1,
                    "name": "\u6587\u672c\u5206\u7c7b\uff0c"
                },
                {
                    "value": 1,
                    "name": "\u6574\u6570\u89c4\u5212"
                },
                {
                    "value": 1,
                    "name": "\u73af\u5883\u611f\u77e5\u4e0e\u878d\u5408"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u4f18\u5316"
                },
                {
                    "value": 1,
                    "name": "\u79fb\u52a8\u7aef"
                },
                {
                    "value": 1,
                    "name": "\u6570\u636e\u91c7\u96c6"
                },
                {
                    "value": 1,
                    "name": "flow"
                },
                {
                    "value": 1,
                    "name": "\u519c\u6797\u7267\u6e14"
                },
                {
                    "value": 1,
                    "name": "\u91cf\u5316"
                },
                {
                    "value": 1,
                    "name": "Javascript"
                },
                {
                    "value": 1,
                    "name": "\u4e16\u754c500\u5f3a"
                },
                {
                    "value": 1,
                    "name": "\u8054\u90a6\u5b66\u4e60"
                },
                {
                    "value": 1,
                    "name": "\u5b9a\u4f4d"
                },
                {
                    "value": 1,
                    "name": "\u96f6\u98df\u4e0b\u5348\u8336"
                },
                {
                    "value": 1,
                    "name": "ORBSLAM"
                },
                {
                    "value": 1,
                    "name": "\u89c4\u5219\u5f15\u64ce"
                },
                {
                    "value": 1,
                    "name": "\u692d\u5706\u66f2\u7ebf"
                },
                {
                    "value": 1,
                    "name": "\u80a2\u4f53\u68c0\u6d4b"
                },
                {
                    "value": 1,
                    "name": "\u6570\u5b66\u5e93"
                },
                {
                    "value": 1,
                    "name": "\u89c6\u9891\u7f16\u8f91"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u8c03\u7814"
                },
                {
                    "value": 1,
                    "name": "\u624b\u52bf\u8bc6\u522b"
                },
                {
                    "value": 1,
                    "name": "\u8282\u65e5\u798f\u5229"
                },
                {
                    "value": 1,
                    "name": "CPLEX"
                },
                {
                    "value": 1,
                    "name": "\u4f53\u80b2"
                },
                {
                    "value": 1,
                    "name": "DNN"
                },
                {
                    "value": 1,
                    "name": "\u673a\u5668\u4eba\u5173\u952e\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "SFM"
                },
                {
                    "value": 1,
                    "name": "CCF"
                },
                {
                    "value": 1,
                    "name": "\u673a\u5668\u611f\u77e5"
                },
                {
                    "value": 1,
                    "name": "\u6279\u53d1\uff5c\u96f6\u552e"
                },
                {
                    "value": 1,
                    "name": "kalman"
                },
                {
                    "value": 1,
                    "name": "\u5e26\u5bbd\u63a7\u5236"
                },
                {
                    "value": 1,
                    "name": "pil"
                },
                {
                    "value": 1,
                    "name": "\u9690\u79d8\u8ba1\u7b97\u672f"
                },
                {
                    "value": 1,
                    "name": "C/C++/Python"
                },
                {
                    "value": 1,
                    "name": "H.264/265"
                },
                {
                    "value": 1,
                    "name": "\u98ce\u63a7"
                },
                {
                    "value": 1,
                    "name": "\u6216"
                },
                {
                    "value": 1,
                    "name": "\u5e95\u76d8\u63a7\u5236"
                }
            ],
            "width": "80%",
            "height": "80%",
            "label": {
                "show": true,
                "position": "inside",
                "margin": 8
            },
            "upperlabel": {
                "show": true,
                "position": "inside",
                "margin": 8
            },
            "drillDownIcon": "\u25b6",
            "roam": true,
            "nodeClick": "zoomToNode",
            "zoomToNodeRatio": 0.1024,
            "colorMappingBy": "index",
            "visibleMin": 10
        }
    ],
    "legend": [
        {
            "data": [
                "\u5173\u952e\u8bcd\u5206\u5e03\u6811\u72b6\u56fe"
            ],
            "selected": {
                "\u5173\u952e\u8bcd\u5206\u5e03\u6811\u72b6\u56fe": true
            },
            "show": true,
            "padding": 5,
            "itemGap": 10,
            "itemWidth": 25,
            "itemHeight": 14
        }
    ],
    "tooltip": {
        "show": true,
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "showContent": true,
        "alwaysShowContent": false,
        "showDelay": 0,
        "hideDelay": 100,
        "textStyle": {
            "fontSize": 14
        },
        "borderWidth": 0,
        "padding": 5
    },
    "title": [
        {
            "text": "\u5173\u952e\u8bcd\u5206\u5e03\u6811\u72b6\u56fe",
            "padding": 5,
            "itemGap": 10
        }
    ]
};
        chart_d31f4cdb30a0420a8863e33743f1788d.setOption(option_d31f4cdb30a0420a8863e33743f1788d);
    </script>
                <div id="8b44b2d05d5940c3940a5290bcf49a06" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_8b44b2d05d5940c3940a5290bcf49a06 = echarts.init(
            document.getElementById('8b44b2d05d5940c3940a5290bcf49a06'), 'white', {renderer: 'canvas'});
        var option_8b44b2d05d5940c3940a5290bcf49a06 = {
    "backgroundColor": {
        "type": "pattern",
        "image": img,
        "repeat": "repeat"
    },
    "animation": true,
    "animationThreshold": 2000,
    "animationDuration": 1000,
    "animationEasing": "cubicOut",
    "animationDelay": 0,
    "animationDurationUpdate": 300,
    "animationEasingUpdate": "cubicOut",
    "animationDelayUpdate": 0,
    "color": [
        "#c23531",
        "#2f4554",
        "#61a0a8",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3",
        "#f05b72",
        "#ef5b9c",
        "#f47920",
        "#905a3d",
        "#fab27b",
        "#2a5caa",
        "#444693",
        "#726930",
        "#b2d235",
        "#6d8346",
        "#ac6767",
        "#1d953f",
        "#6950a1",
        "#918597"
    ],
    "series": [
        {
            "type": "bar",
            "xAxisIndex": 0,
            "yAxisIndex": 0,
            "legendHoverLink": true,
            "data": [
                968,
                496,
                111,
                70,
                46,
                15,
                13,
                5
            ],
            "showBackground": false,
            "barMinHeight": 0,
            "barCategoryGap": "20%",
            "barGap": "30%",
            "large": false,
            "largeThreshold": 400,
            "seriesLayoutBy": "column",
            "datasetIndex": 0,
            "clip": true,
            "zlevel": 0,
            "z": 2,
            "label": {
                "show": true,
                "position": "top",
                "margin": 8
            }
        },
        {
            "type": "pie",
            "clockwise": true,
            "data": [
                {
                    "name": "\u672c\u79d1",
                    "value": 968
                },
                {
                    "name": "\u7855\u58eb",
                    "value": 496
                },
                {
                    "name": "\u5e94\u5c4a / \u672c\u79d1",
                    "value": 111
                },
                {
                    "name": "\u5e94\u5c4a / \u7855\u58eb",
                    "value": 70
                },
                {
                    "name": "\u4e0d\u9650",
                    "value": 46
                },
                {
                    "name": "\u535a\u58eb",
                    "value": 15
                },
                {
                    "name": "\u5e94\u5c4a / \u4e0d\u9650",
                    "value": 13
                },
                {
                    "name": "\u5927\u4e13",
                    "value": 5
                }
            ],
            "radius": [
                "10%",
                "35%"
            ],
            "center": [
                "70%",
                "28%"
            ],
            "roseType": "radius",
            "label": {
                "show": true,
                "position": "top",
                "margin": 8,
                "formatter": "{b}: {d}%"
            },
            "rippleEffect": {
                "show": true,
                "brushType": "stroke",
                "scale": 2.5,
                "period": 4
            },
            "xAxisIndex": 1,
            "yAxisIndex": 1
        },
        {
            "type": "pie",
            "clockwise": true,
            "data": [
                {
                    "name": "\u672c\u79d1",
                    "value": 968
                },
                {
                    "name": "\u7855\u58eb",
                    "value": 496
                },
                {
                    "name": "\u5e94\u5c4a / \u672c\u79d1",
                    "value": 111
                },
                {
                    "name": "\u5e94\u5c4a / \u7855\u58eb",
                    "value": 70
                },
                {
                    "name": "\u4e0d\u9650",
                    "value": 46
                },
                {
                    "name": "\u535a\u58eb",
                    "value": 15
                },
                {
                    "name": "\u5e94\u5c4a / \u4e0d\u9650",
                    "value": 13
                },
                {
                    "name": "\u5927\u4e13",
                    "value": 5
                }
            ],
            "radius": [
                "10%",
                "35%"
            ],
            "center": [
                "70%",
                "75%"
            ],
            "label": {
                "show": true,
                "position": "top",
                "margin": 8,
                "formatter": "{b}: {d}%"
            },
            "rippleEffect": {
                "show": true,
                "brushType": "stroke",
                "scale": 2.5,
                "period": 4
            },
            "xAxisIndex": 1,
            "yAxisIndex": 1
        }
    ],
    "legend": [
        {
            "data": [
                ""
            ],
            "selected": {
                "": true
            },
            "show": true,
            "padding": 5,
            "itemGap": 10,
            "itemWidth": 25,
            "itemHeight": 14
        },
        {
            "data": [
                "\u672c\u79d1",
                "\u7855\u58eb",
                "\u5e94\u5c4a / \u672c\u79d1",
                "\u5e94\u5c4a / \u7855\u58eb",
                "\u4e0d\u9650",
                "\u535a\u58eb",
                "\u5e94\u5c4a / \u4e0d\u9650",
                "\u5927\u4e13"
            ],
            "selected": {},
            "show": false,
            "padding": 5,
            "itemGap": 10,
            "itemWidth": 25,
            "itemHeight": 14
        }
    ],
    "tooltip": {
        "show": true,
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "showContent": true,
        "alwaysShowContent": false,
        "showDelay": 0,
        "hideDelay": 100,
        "textStyle": {
            "fontSize": 14
        },
        "borderWidth": 0,
        "padding": 5
    },
    "xAxis": [
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "axisLabel": {
                "rotate": 35
            },
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "show": true,
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            },
            "data": [
                "\u672c\u79d1",
                "\u7855\u58eb",
                "\u5e94\u5c4a / \u672c\u79d1",
                "\u5e94\u5c4a / \u7855\u58eb",
                "\u4e0d\u9650",
                "\u535a\u58eb",
                "\u5e94\u5c4a / \u4e0d\u9650",
                "\u5927\u4e13"
            ]
        }
    ],
    "yAxis": [
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "show": true,
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            }
        }
    ],
    "title": [
        {
            "text": "\u5b66\u5386\u8981\u6c42",
            "padding": 5,
            "itemGap": 10
        },
        {
            "text": " ",
            "padding": 5,
            "itemGap": 10
        }
    ],
    "grid": [
        {
            "show": false,
            "zlevel": 0,
            "z": 2,
            "right": "60%",
            "containLabel": false,
            "backgroundColor": "transparent",
            "borderColor": "#ccc",
            "borderWidth": 1
        },
        {
            "show": false,
            "zlevel": 0,
            "z": 2,
            "left": "40%",
            "containLabel": false,
            "backgroundColor": "transparent",
            "borderColor": "#ccc",
            "borderWidth": 1
        }
    ]
};
        chart_8b44b2d05d5940c3940a5290bcf49a06.setOption(option_8b44b2d05d5940c3940a5290bcf49a06);
    </script>
                <div id="1d57d57562114e00b5e6519e532349a3" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_1d57d57562114e00b5e6519e532349a3 = echarts.init(
            document.getElementById('1d57d57562114e00b5e6519e532349a3'), 'white', {renderer: 'canvas'});
        var option_1d57d57562114e00b5e6519e532349a3 = {
    "backgroundColor": {
        "type": "pattern",
        "image": img,
        "repeat": "repeat"
    },
    "animation": true,
    "animationThreshold": 2000,
    "animationDuration": 1000,
    "animationEasing": "cubicOut",
    "animationDelay": 0,
    "animationDurationUpdate": 300,
    "animationEasingUpdate": "cubicOut",
    "animationDelayUpdate": 0,
    "color": [
        "#c23531",
        "#2f4554",
        "#61a0a8",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3",
        "#f05b72",
        "#ef5b9c",
        "#f47920",
        "#905a3d",
        "#fab27b",
        "#2a5caa",
        "#444693",
        "#726930",
        "#b2d235",
        "#6d8346",
        "#ac6767",
        "#1d953f",
        "#6950a1",
        "#918597"
    ],
    "series": [
        {
            "type": "bar",
            "xAxisIndex": 0,
            "yAxisIndex": 0,
            "legendHoverLink": true,
            "data": [
                664,
                369,
                285,
                198,
                195,
                12,
                5
            ],
            "showBackground": false,
            "barMinHeight": 0,
            "barCategoryGap": "20%",
            "barGap": "30%",
            "large": false,
            "largeThreshold": 400,
            "seriesLayoutBy": "column",
            "datasetIndex": 0,
            "clip": true,
            "zlevel": 0,
            "z": 2,
            "label": {
                "show": true,
                "position": "top",
                "margin": 8
            }
        },
        {
            "type": "pie",
            "clockwise": true,
            "data": [
                {
                    "name": "\u7ecf\u9a8c3-5\u5e74",
                    "value": 664
                },
                {
                    "name": "\u7ecf\u9a8c1-3\u5e74",
                    "value": 369
                },
                {
                    "name": "\u7ecf\u9a8c\u4e0d\u9650",
                    "value": 285
                },
                {
                    "name": "\u7ecf\u9a8c\u5728\u6821",
                    "value": 198
                },
                {
                    "name": "\u7ecf\u9a8c5-10\u5e74",
                    "value": 195
                },
                {
                    "name": "\u7ecf\u9a8c1\u5e74\u4ee5\u4e0b",
                    "value": 12
                },
                {
                    "name": "\u7ecf\u9a8c10\u5e74\u4ee5\u4e0a",
                    "value": 5
                }
            ],
            "radius": [
                "10%",
                "35%"
            ],
            "center": [
                "70%",
                "28%"
            ],
            "roseType": "radius",
            "label": {
                "show": true,
                "position": "top",
                "margin": 8,
                "formatter": "{b}: {d}%"
            },
            "rippleEffect": {
                "show": true,
                "brushType": "stroke",
                "scale": 2.5,
                "period": 4
            },
            "xAxisIndex": 1,
            "yAxisIndex": 1
        },
        {
            "type": "pie",
            "clockwise": true,
            "data": [
                {
                    "name": "\u7ecf\u9a8c3-5\u5e74",
                    "value": 664
                },
                {
                    "name": "\u7ecf\u9a8c1-3\u5e74",
                    "value": 369
                },
                {
                    "name": "\u7ecf\u9a8c\u4e0d\u9650",
                    "value": 285
                },
                {
                    "name": "\u7ecf\u9a8c\u5728\u6821",
                    "value": 198
                },
                {
                    "name": "\u7ecf\u9a8c5-10\u5e74",
                    "value": 195
                },
                {
                    "name": "\u7ecf\u9a8c1\u5e74\u4ee5\u4e0b",
                    "value": 12
                },
                {
                    "name": "\u7ecf\u9a8c10\u5e74\u4ee5\u4e0a",
                    "value": 5
                }
            ],
            "radius": [
                "10%",
                "35%"
            ],
            "center": [
                "70%",
                "75%"
            ],
            "label": {
                "show": true,
                "position": "top",
                "margin": 8,
                "formatter": "{b}: {d}%"
            },
            "rippleEffect": {
                "show": true,
                "brushType": "stroke",
                "scale": 2.5,
                "period": 4
            },
            "xAxisIndex": 1,
            "yAxisIndex": 1
        }
    ],
    "legend": [
        {
            "data": [
                ""
            ],
            "selected": {
                "": true
            },
            "show": true,
            "padding": 5,
            "itemGap": 10,
            "itemWidth": 25,
            "itemHeight": 14
        },
        {
            "data": [
                "\u7ecf\u9a8c3-5\u5e74",
                "\u7ecf\u9a8c1-3\u5e74",
                "\u7ecf\u9a8c\u4e0d\u9650",
                "\u7ecf\u9a8c\u5728\u6821",
                "\u7ecf\u9a8c5-10\u5e74",
                "\u7ecf\u9a8c1\u5e74\u4ee5\u4e0b",
                "\u7ecf\u9a8c10\u5e74\u4ee5\u4e0a"
            ],
            "selected": {},
            "show": false,
            "padding": 5,
            "itemGap": 10,
            "itemWidth": 25,
            "itemHeight": 14
        }
    ],
    "tooltip": {
        "show": true,
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "showContent": true,
        "alwaysShowContent": false,
        "showDelay": 0,
        "hideDelay": 100,
        "textStyle": {
            "fontSize": 14
        },
        "borderWidth": 0,
        "padding": 5
    },
    "xAxis": [
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "axisLabel": {
                "rotate": 35
            },
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "show": true,
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            },
            "data": [
                "\u7ecf\u9a8c3-5\u5e74",
                "\u7ecf\u9a8c1-3\u5e74",
                "\u7ecf\u9a8c\u4e0d\u9650",
                "\u7ecf\u9a8c\u5728\u6821",
                "\u7ecf\u9a8c5-10\u5e74",
                "\u7ecf\u9a8c1\u5e74\u4ee5\u4e0b",
                "\u7ecf\u9a8c10\u5e74\u4ee5\u4e0a"
            ]
        }
    ],
    "yAxis": [
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "show": true,
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            }
        }
    ],
    "title": [
        {
            "text": "\u5de5\u4f5c\u7ecf\u9a8c\u8981\u6c42",
            "padding": 5,
            "itemGap": 10
        },
        {
            "text": " ",
            "padding": 5,
            "itemGap": 10
        }
    ],
    "grid": [
        {
            "show": false,
            "zlevel": 0,
            "z": 2,
            "right": "60%",
            "containLabel": false,
            "backgroundColor": "transparent",
            "borderColor": "#ccc",
            "borderWidth": 1
        },
        {
            "show": false,
            "zlevel": 0,
            "z": 2,
            "left": "40%",
            "containLabel": false,
            "backgroundColor": "transparent",
            "borderColor": "#ccc",
            "borderWidth": 1
        }
    ]
};
        chart_1d57d57562114e00b5e6519e532349a3.setOption(option_1d57d57562114e00b5e6519e532349a3);
    </script>
                <div id="1b34c75d07b546cc8a21f302c114bb52" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_1b34c75d07b546cc8a21f302c114bb52 = echarts.init(
            document.getElementById('1b34c75d07b546cc8a21f302c114bb52'), 'white', {renderer: 'canvas'});
            
    var waterMarkText = 'ShowMeAI';
    var canvas = document.createElement('canvas');
    var ctx = canvas.getContext('2d');
    canvas.width = canvas.height = 300;
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.globalAlpha = 0.03;
    ctx.font = '50px Microsoft Yahei';
    ctx.translate(100, 100);
    ctx.rotate(-Math.PI / 4);
    ctx.fillText(waterMarkText, 0, 0);
    img = canvas;
    
        var option_1b34c75d07b546cc8a21f302c114bb52 = {
    "backgroundColor": {
        "type": "pattern",
        "image": img,
        "repeat": "repeat"
    },
    "animation": true,
    "animationThreshold": 2000,
    "animationDuration": 1000,
    "animationEasing": "cubicOut",
    "animationDelay": 0,
    "animationDurationUpdate": 300,
    "animationEasingUpdate": "cubicOut",
    "animationDelayUpdate": 0,
    "color": [
        "#c23531",
        "#2f4554",
        "#61a0a8",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3",
        "#f05b72",
        "#ef5b9c",
        "#f47920",
        "#905a3d",
        "#fab27b",
        "#2a5caa",
        "#444693",
        "#726930",
        "#b2d235",
        "#6d8346",
        "#ac6767",
        "#1d953f",
        "#6950a1",
        "#918597"
    ],
    "series": [
        {
            "type": "wordCloud",
            "name": "NLP\u5de5\u4f5c\u804c\u8d23\u5173\u952e\u8bcd",
            "shape": "circle",
            "rotationRange": [
                -90,
                90
            ],
            "rotationStep": 45,
            "girdSize": 20,
            "sizeRange": [
                18,
                48
            ],
            "data": [
                {
                    "name": "NLP\u843d\u5730",
                    "value": 100,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,143,33)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u95ee\u7b54",
                    "value": 99,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,76,105)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u52a9\u7406",
                    "value": 98,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,27,145)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u5ba2\u670d",
                    "value": 97,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,134,155)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u8bc6\u56fe\u8c31",
                    "value": 96,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,31,50)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u8bc6\u63a8\u7406",
                    "value": 95,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,158,88)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u6e05\u6d17",
                    "value": 94,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,98,25)"
                        }
                    }
                },
                {
                    "name": "\u60c5\u611f\u5206\u6790",
                    "value": 93,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,20,23)"
                        }
                    }
                },
                {
                    "name": "\u8206\u60c5\u5206\u6790",
                    "value": 92,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,79,89)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u4e49\u7406\u89e3",
                    "value": 91,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,5,67)"
                        }
                    }
                },
                {
                    "name": "\u610f\u56fe\u7406\u89e3",
                    "value": 90,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,36,105)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u6458\u8981",
                    "value": 89,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,0,1)"
                        }
                    }
                },
                {
                    "name": "query\u5206\u6790",
                    "value": 88,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,129,94)"
                        }
                    }
                },
                {
                    "name": "query\u7406\u89e3",
                    "value": 87,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,68,94)"
                        }
                    }
                },
                {
                    "name": "\u62fc\u5199\u7ea0\u9519",
                    "value": 86,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,145,62)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u753b\u50cf",
                    "value": 85,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,84,26)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u95fb\u7279\u5f81",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,137,22)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u4e49\u53ec\u56de",
                    "value": 83,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,121,41)"
                        }
                    }
                },
                {
                    "name": "\u591a\u8f6e\u5bf9\u8bdd",
                    "value": 82,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,61,100)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u68c0\u7d22",
                    "value": 81,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,4,0)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u68c0\u7d22",
                    "value": 80,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,4,121)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u76f8\u5173\u6027",
                    "value": 79,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,20,108)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u8c31\u67e5\u8be2",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,46,82)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u8c31\u63a8\u7406",
                    "value": 77,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,17,109)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u6587\u672c",
                    "value": 76,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,158,129)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u6587\u672c",
                    "value": 75,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,110,88)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u5e7f\u544aNLP",
                    "value": 74,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,7,150)"
                        }
                    }
                },
                {
                    "name": "\u5bf9\u8bdd\u7406\u89e3",
                    "value": 73,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,93,61)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u5b89\u5168",
                    "value": 72,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,93,157)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u8baf\u63a8\u8350\u548c\u641c\u7d22",
                    "value": 71,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,27,2)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u884c\u4e3a\u5206\u6790",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,71,9)"
                        }
                    }
                },
                {
                    "name": "\u5bf9\u8bdd\u8f6c\u5199",
                    "value": 69,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,18,146)"
                        }
                    }
                },
                {
                    "name": "UGC\u6316\u6398",
                    "value": 68,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,41,39)"
                        }
                    }
                },
                {
                    "name": "\u6cd5\u5f8b\u95ee\u7b54",
                    "value": 67,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,29,142)"
                        }
                    }
                },
                {
                    "name": "\u9605\u8bfb\u7406\u89e3",
                    "value": 66,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,129,60)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u6807\u7b7e\u4f53\u7cfb",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,103,32)"
                        }
                    }
                },
                {
                    "name": "\u4efb\u52a1\u5f0f\u5bf9\u8bdd\u7cfb\u7edf",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,36,61)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672cspam\u8bc6\u522b",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,62,146)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u6559\u80b2\u9886\u57df",
                    "value": 62,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,120,26)"
                        }
                    }
                },
                {
                    "name": "\u50ac\u6536\u6587\u672c\u6316\u6398",
                    "value": 61,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,112,138)"
                        }
                    }
                }
            ],
            "drawOutOfBound": false,
            "textStyle": {
                "emphasis": {}
            }
        }
    ],
    "legend": [
        {
            "data": [],
            "selected": {},
            "show": true,
            "padding": 5,
            "itemGap": 10,
            "itemWidth": 25,
            "itemHeight": 14
        }
    ],
    "tooltip": {
        "show": true,
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "showContent": true,
        "alwaysShowContent": false,
        "showDelay": 0,
        "hideDelay": 100,
        "textStyle": {
            "fontSize": 14
        },
        "borderWidth": 0,
        "padding": 5
    },
    "title": [
        {
            "text": "NLP\u5de5\u4f5c\u804c\u8d23\u5173\u952e\u8bcd",
            "padding": 5,
            "itemGap": 10,
            "textStyle": {
                "fontSize": 23
            }
        }
    ]
};
        chart_1b34c75d07b546cc8a21f302c114bb52.setOption(option_1b34c75d07b546cc8a21f302c114bb52);
    </script>
                <div id="6889adb6cb1a40aa8beeed533e1722b4" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_6889adb6cb1a40aa8beeed533e1722b4 = echarts.init(
            document.getElementById('6889adb6cb1a40aa8beeed533e1722b4'), 'white', {renderer: 'canvas'});
            
    var waterMarkText = 'ShowMeAI';
    var canvas = document.createElement('canvas');
    var ctx = canvas.getContext('2d');
    canvas.width = canvas.height = 300;
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.globalAlpha = 0.03;
    ctx.font = '50px Microsoft Yahei';
    ctx.translate(100, 100);
    ctx.rotate(-Math.PI / 4);
    ctx.fillText(waterMarkText, 0, 0);
    img = canvas;
    
        var option_6889adb6cb1a40aa8beeed533e1722b4 = {
    "backgroundColor": {
        "type": "pattern",
        "image": img,
        "repeat": "repeat"
    },
    "animation": true,
    "animationThreshold": 2000,
    "animationDuration": 1000,
    "animationEasing": "cubicOut",
    "animationDelay": 0,
    "animationDurationUpdate": 300,
    "animationEasingUpdate": "cubicOut",
    "animationDelayUpdate": 0,
    "color": [
        "#c23531",
        "#2f4554",
        "#61a0a8",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3",
        "#f05b72",
        "#ef5b9c",
        "#f47920",
        "#905a3d",
        "#fab27b",
        "#2a5caa",
        "#444693",
        "#726930",
        "#b2d235",
        "#6d8346",
        "#ac6767",
        "#1d953f",
        "#6950a1",
        "#918597"
    ],
    "series": [
        {
            "type": "wordCloud",
            "name": "NLP\u4efb\u804c\u8981\u6c42\u5173\u952e\u8bcd",
            "shape": "circle",
            "rotationRange": [
                -90,
                90
            ],
            "rotationStep": 45,
            "girdSize": 20,
            "sizeRange": [
                15,
                48
            ],
            "data": [
                {
                    "name": "Python",
                    "value": 100,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,134,36)"
                        }
                    }
                },
                {
                    "name": "Java",
                    "value": 99,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,102,9)"
                        }
                    }
                },
                {
                    "name": "C++",
                    "value": 98,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,20,132)"
                        }
                    }
                },
                {
                    "name": "GO",
                    "value": 97,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,20,53)"
                        }
                    }
                },
                {
                    "name": "Linux",
                    "value": 96,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,157,0)"
                        }
                    }
                },
                {
                    "name": "TensorFlow",
                    "value": 95,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,142,111)"
                        }
                    }
                },
                {
                    "name": "Keras",
                    "value": 94,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,55,88)"
                        }
                    }
                },
                {
                    "name": "PyTorch",
                    "value": 93,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,39,99)"
                        }
                    }
                },
                {
                    "name": "\u6b63\u5219\u8868\u8fbe\u5f0f",
                    "value": 92,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,142,34)"
                        }
                    }
                },
                {
                    "name": "\u547d\u540d\u5b9e\u4f53\u8bc6\u522b",
                    "value": 91,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,0,30)"
                        }
                    }
                },
                {
                    "name": "\u5173\u7cfb\u62bd\u53d6",
                    "value": 90,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,147,8)"
                        }
                    }
                },
                {
                    "name": "\u5c5e\u6027\u62bd\u53d6",
                    "value": 89,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,111,160)"
                        }
                    }
                },
                {
                    "name": "\u4e8b\u4ef6\u62bd\u53d6",
                    "value": 88,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,22,91)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u5206\u7c7b",
                    "value": 87,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,67,1)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u76f8\u4f3c\u5ea6\u8ba1\u7b97",
                    "value": 86,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,72,104)"
                        }
                    }
                },
                {
                    "name": "\u5173\u7cfb\u62bd\u53d6",
                    "value": 85,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,156,130)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u7b97\u6cd5",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,15,116)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u4e49\u5339\u914d",
                    "value": 83,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,89,92)"
                        }
                    }
                },
                {
                    "name": "\u5e8f\u5217\u6807\u6ce8",
                    "value": 82,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,102,143)"
                        }
                    }
                },
                {
                    "name": "\u591a\u6a21\u6001\u5b66\u4e60",
                    "value": 81,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,44,140)"
                        }
                    }
                },
                {
                    "name": "\u591a\u6a21\u6001\u7406\u89e3",
                    "value": 80,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,133,70)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u8868\u793a",
                    "value": 79,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,120,20)"
                        }
                    }
                },
                {
                    "name": "\u76f8\u5173\u6027",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,118,120)"
                        }
                    }
                },
                {
                    "name": "\u5206\u8bcd",
                    "value": 77,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,49,134)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u68c0\u7d22",
                    "value": 76,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,157,73)"
                        }
                    }
                },
                {
                    "name": "\u5bf9\u8bdd\u751f\u6210",
                    "value": 75,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,17,96)"
                        }
                    }
                },
                {
                    "name": "Embedding",
                    "value": 74,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,41,3)"
                        }
                    }
                },
                {
                    "name": "Q&A",
                    "value": 73,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,76,144)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u7ffb\u8bd1",
                    "value": 72,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,72,62)"
                        }
                    }
                },
                {
                    "name": "SelfAttention",
                    "value": 71,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,120,9)"
                        }
                    }
                },
                {
                    "name": "lda",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,34,149)"
                        }
                    }
                },
                {
                    "name": "RNN",
                    "value": 69,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,31,23)"
                        }
                    }
                },
                {
                    "name": "CNN",
                    "value": 68,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,72,63)"
                        }
                    }
                },
                {
                    "name": "seq2seq",
                    "value": 67,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,43,103)"
                        }
                    }
                },
                {
                    "name": "Word2vec",
                    "value": 66,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,48,0)"
                        }
                    }
                },
                {
                    "name": "GPT2",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,61,90)"
                        }
                    }
                },
                {
                    "name": "Transformer",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,36,35)"
                        }
                    }
                },
                {
                    "name": "BERT",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,139,99)"
                        }
                    }
                },
                {
                    "name": "\u4e3b\u9898\u6a21\u578b",
                    "value": 62,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,117,149)"
                        }
                    }
                },
                {
                    "name": "KBQA",
                    "value": 61,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,33,91)"
                        }
                    }
                }
            ],
            "drawOutOfBound": false,
            "textStyle": {
                "emphasis": {}
            }
        }
    ],
    "legend": [
        {
            "data": [],
            "selected": {},
            "show": true,
            "padding": 5,
            "itemGap": 10,
            "itemWidth": 25,
            "itemHeight": 14
        }
    ],
    "tooltip": {
        "show": true,
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "showContent": true,
        "alwaysShowContent": false,
        "showDelay": 0,
        "hideDelay": 100,
        "textStyle": {
            "fontSize": 14
        },
        "borderWidth": 0,
        "padding": 5
    },
    "title": [
        {
            "text": "NLP\u4efb\u804c\u8981\u6c42\u5173\u952e\u8bcd",
            "padding": 5,
            "itemGap": 10,
            "textStyle": {
                "fontSize": 23
            }
        }
    ]
};
        chart_6889adb6cb1a40aa8beeed533e1722b4.setOption(option_6889adb6cb1a40aa8beeed533e1722b4);
    </script>
                <div id="bcbd103e05e549c3ac4d2fbcb8639ad1" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_bcbd103e05e549c3ac4d2fbcb8639ad1 = echarts.init(
            document.getElementById('bcbd103e05e549c3ac4d2fbcb8639ad1'), 'white', {renderer: 'canvas'});
            
    var waterMarkText = 'ShowMeAI';
    var canvas = document.createElement('canvas');
    var ctx = canvas.getContext('2d');
    canvas.width = canvas.height = 300;
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.globalAlpha = 0.03;
    ctx.font = '50px Microsoft Yahei';
    ctx.translate(100, 100);
    ctx.rotate(-Math.PI / 4);
    ctx.fillText(waterMarkText, 0, 0);
    img = canvas;
    
        var option_bcbd103e05e549c3ac4d2fbcb8639ad1 = {
    "backgroundColor": {
        "type": "pattern",
        "image": img,
        "repeat": "repeat"
    },
    "animation": true,
    "animationThreshold": 2000,
    "animationDuration": 1000,
    "animationEasing": "cubicOut",
    "animationDelay": 0,
    "animationDurationUpdate": 300,
    "animationEasingUpdate": "cubicOut",
    "animationDelayUpdate": 0,
    "color": [
        "#c23531",
        "#2f4554",
        "#61a0a8",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3",
        "#f05b72",
        "#ef5b9c",
        "#f47920",
        "#905a3d",
        "#fab27b",
        "#2a5caa",
        "#444693",
        "#726930",
        "#b2d235",
        "#6d8346",
        "#ac6767",
        "#1d953f",
        "#6950a1",
        "#918597"
    ],
    "series": [
        {
            "type": "wordCloud",
            "name": "CV\u5de5\u4f5c\u804c\u8d23\u5173\u952e\u8bcd",
            "shape": "circle",
            "rotationRange": [
                -90,
                90
            ],
            "rotationStep": 45,
            "girdSize": 20,
            "sizeRange": [
                14,
                48
            ],
            "data": [
                {
                    "name": "\u4eba\u8138\u8bc6\u522b",
                    "value": 100,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,35,99)"
                        }
                    }
                },
                {
                    "name": "OCR",
                    "value": 99,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,35,153)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u5206\u6790",
                    "value": 98,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,87,143)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u5f71\u50cf\u7406\u89e3",
                    "value": 97,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,135,3)"
                        }
                    }
                },
                {
                    "name": "\u76ee\u6807\u68c0\u6d4b\u548c\u8ddf\u8e2a",
                    "value": 96,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,40,145)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5206\u5272",
                    "value": 95,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,82,46)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u641c\u7d22",
                    "value": 94,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,143,42)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u7a0b\u5b9e\u73b0",
                    "value": 93,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,107,12)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5206\u6790",
                    "value": 92,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,35,119)"
                        }
                    }
                },
                {
                    "name": "\u6027\u80fd\u4f18\u5316",
                    "value": 91,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,71,23)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u89c6\u9891",
                    "value": 90,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,101,141)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u7247\u5185\u5bb9\u751f\u6210",
                    "value": 89,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,147,35)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u63a8\u8350",
                    "value": 88,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,63,82)"
                        }
                    }
                },
                {
                    "name": "\u5bf9\u8c61\u63d0\u53d6",
                    "value": 87,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,19,119)"
                        }
                    }
                },
                {
                    "name": "\u7269\u4f53\u611f\u77e5",
                    "value": 86,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,75,153)"
                        }
                    }
                },
                {
                    "name": "\u7269\u4f53\u5206\u7c7b",
                    "value": 85,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,69,83)"
                        }
                    }
                },
                {
                    "name": "\u7269\u4f53\u8ddf\u8e2a",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,29,120)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7ed3\u6784\u5316",
                    "value": 83,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,135,83)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6167\u57ce\u5e02",
                    "value": 82,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,33,42)"
                        }
                    }
                },
                {
                    "name": "\u9065\u611f\u89e3\u8bd1",
                    "value": 81,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,90,69)"
                        }
                    }
                },
                {
                    "name": "\u4e8b\u4ef6\u5206\u6790",
                    "value": 80,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,143,65)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b\u538b\u7f29\u8f7b\u91cf\u5316\u5e94\u7528",
                    "value": 79,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,111,29)"
                        }
                    }
                },
                {
                    "name": "\u591a\u4f20\u611f\u5668\u878d\u5408",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,99,28)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u4f4d\u548c\u5bfc\u822a",
                    "value": 77,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,11,143)"
                        }
                    }
                },
                {
                    "name": "\u6ee4\u955c\u521b\u4f5c\u5de5\u5177",
                    "value": 76,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,22,30)"
                        }
                    }
                },
                {
                    "name": "\u5173\u952e\u70b9\u68c0\u6d4b",
                    "value": 75,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,125,29)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u751f\u6210",
                    "value": 74,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,36,36)"
                        }
                    }
                },
                {
                    "name": "AR/MR",
                    "value": 73,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,150,116)"
                        }
                    }
                },
                {
                    "name": "3D\u91cd\u5efa",
                    "value": 72,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,6,22)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u6444\u5f71",
                    "value": 71,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,38,10)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u91cd\u5efa",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,43,159)"
                        }
                    }
                },
                {
                    "name": "\u6750\u8d28\u548c\u5916\u89c2\u91cd\u5efa",
                    "value": 69,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,24,25)"
                        }
                    }
                },
                {
                    "name": "\u5ea6\u91cf\u5b66\u4e60",
                    "value": 68,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,49,74)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u4e49/\u5b9e\u4f8b\u5206\u5272",
                    "value": 67,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,135,41)"
                        }
                    }
                },
                {
                    "name": "\u6587\u5b57\u68c0\u6d4b\u8bc6\u522b",
                    "value": 66,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,17,144)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u8138\u68c0\u6d4b\u8bc6\u522b",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,88,141)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u7f16\u8f91\u751f\u6210",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,55,100)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u683c\u8fc1\u79fb",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,99,90)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u56fe\u79c0\u79c0",
                    "value": 62,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,9,135)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u62cd",
                    "value": 61,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,0,54)"
                        }
                    }
                }
            ],
            "drawOutOfBound": false,
            "textStyle": {
                "emphasis": {}
            }
        }
    ],
    "legend": [
        {
            "data": [],
            "selected": {},
            "show": true,
            "padding": 5,
            "itemGap": 10,
            "itemWidth": 25,
            "itemHeight": 14
        }
    ],
    "tooltip": {
        "show": true,
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "showContent": true,
        "alwaysShowContent": false,
        "showDelay": 0,
        "hideDelay": 100,
        "textStyle": {
            "fontSize": 14
        },
        "borderWidth": 0,
        "padding": 5
    },
    "title": [
        {
            "text": "CV\u5de5\u4f5c\u804c\u8d23\u5173\u952e\u8bcd",
            "padding": 5,
            "itemGap": 10,
            "textStyle": {
                "fontSize": 23
            }
        }
    ]
};
        chart_bcbd103e05e549c3ac4d2fbcb8639ad1.setOption(option_bcbd103e05e549c3ac4d2fbcb8639ad1);
    </script>
                <div id="4f4bdabde7c6463daf9313c70d1a8e73" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_4f4bdabde7c6463daf9313c70d1a8e73 = echarts.init(
            document.getElementById('4f4bdabde7c6463daf9313c70d1a8e73'), 'white', {renderer: 'canvas'});
            
    var waterMarkText = 'ShowMeAI';
    var canvas = document.createElement('canvas');
    var ctx = canvas.getContext('2d');
    canvas.width = canvas.height = 300;
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.globalAlpha = 0.03;
    ctx.font = '50px Microsoft Yahei';
    ctx.translate(100, 100);
    ctx.rotate(-Math.PI / 4);
    ctx.fillText(waterMarkText, 0, 0);
    img = canvas;
    
        var option_4f4bdabde7c6463daf9313c70d1a8e73 = {
    "backgroundColor": {
        "type": "pattern",
        "image": img,
        "repeat": "repeat"
    },
    "animation": true,
    "animationThreshold": 2000,
    "animationDuration": 1000,
    "animationEasing": "cubicOut",
    "animationDelay": 0,
    "animationDurationUpdate": 300,
    "animationEasingUpdate": "cubicOut",
    "animationDelayUpdate": 0,
    "color": [
        "#c23531",
        "#2f4554",
        "#61a0a8",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3",
        "#f05b72",
        "#ef5b9c",
        "#f47920",
        "#905a3d",
        "#fab27b",
        "#2a5caa",
        "#444693",
        "#726930",
        "#b2d235",
        "#6d8346",
        "#ac6767",
        "#1d953f",
        "#6950a1",
        "#918597"
    ],
    "series": [
        {
            "type": "wordCloud",
            "name": "CV\u4efb\u804c\u8981\u6c42\u5173\u952e\u8bcd",
            "shape": "circle",
            "rotationRange": [
                -90,
                90
            ],
            "rotationStep": 45,
            "girdSize": 20,
            "sizeRange": [
                15,
                48
            ],
            "data": [
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60",
                    "value": 100,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,1,12)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u8bc6\u522b/\u5206\u7c7b",
                    "value": 99,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,105,12)"
                        }
                    }
                },
                {
                    "name": "\u7269\u4f53\u68c0\u6d4b",
                    "value": 98,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,16,100)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u5206\u6790",
                    "value": 97,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,1,150)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b\u538b\u7f29",
                    "value": 96,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,70,155)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5206\u5272",
                    "value": 95,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,68,39)"
                        }
                    }
                },
                {
                    "name": "GAN",
                    "value": 94,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,121,47)"
                        }
                    }
                },
                {
                    "name": "Linux",
                    "value": 93,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,23,118)"
                        }
                    }
                },
                {
                    "name": "tensorflow",
                    "value": 92,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,99,47)"
                        }
                    }
                },
                {
                    "name": "pytorch",
                    "value": 91,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,33,137)"
                        }
                    }
                },
                {
                    "name": "C++",
                    "value": 90,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,134,65)"
                        }
                    }
                },
                {
                    "name": "Python",
                    "value": 89,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,41,97)"
                        }
                    }
                },
                {
                    "name": "CVPR",
                    "value": 88,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,91,53)"
                        }
                    }
                },
                {
                    "name": "ECCV",
                    "value": 87,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,116,50)"
                        }
                    }
                },
                {
                    "name": "ICCV",
                    "value": 86,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,10,121)"
                        }
                    }
                },
                {
                    "name": "\u5206\u5e03\u5f0f\u8bad\u7ec3",
                    "value": 85,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,98,94)"
                        }
                    }
                },
                {
                    "name": "\u591a\u6a21\u6001",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,16,136)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u76d1\u7763/\u534a\u76d1\u7763\u5b66\u4e60",
                    "value": 83,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,123,28)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u89c6\u89c9",
                    "value": 82,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,49,73)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u751f\u6210",
                    "value": 81,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,39,28)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf/\u89c6\u9891\u8bc6\u522b",
                    "value": 80,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,18,31)"
                        }
                    }
                },
                {
                    "name": "OCR",
                    "value": 79,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,78,94)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b\u538b\u7f29",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,68,133)"
                        }
                    }
                },
                {
                    "name": "SLAM",
                    "value": 77,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,45,151)"
                        }
                    }
                },
                {
                    "name": "OpenCV",
                    "value": 76,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,51,80)"
                        }
                    }
                },
                {
                    "name": "PCL",
                    "value": 75,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,121,144)"
                        }
                    }
                },
                {
                    "name": "\u5355\u76ee/\u53cc\u76ee\u6df1\u5ea6\u4f30\u8ba1",
                    "value": 74,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,119,16)"
                        }
                    }
                },
                {
                    "name": "\u76f8\u673a\u6807\u5b9a/\u914d\u51c6",
                    "value": 73,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,86,142)"
                        }
                    }
                },
                {
                    "name": "3D\u7269\u4f53\u8bc6\u522b\u4e0e\u5206\u5272",
                    "value": 72,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,69,159)"
                        }
                    }
                },
                {
                    "name": "3D\u91cd\u5efa",
                    "value": 71,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,88,156)"
                        }
                    }
                },
                {
                    "name": "Visual SLAM",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,27,17)"
                        }
                    }
                },
                {
                    "name": "SfM\u3001MVS",
                    "value": 69,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,78,126)"
                        }
                    }
                },
                {
                    "name": "\u5206\u7c7b",
                    "value": 68,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,50,95)"
                        }
                    }
                },
                {
                    "name": "\u56de\u5f52",
                    "value": 67,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,44,22)"
                        }
                    }
                },
                {
                    "name": "\u805a\u7c7b",
                    "value": 66,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,37,45)"
                        }
                    }
                },
                {
                    "name": "\u6982\u7387\u6a21\u578b",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,8,19)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5904\u7406",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,131,55)"
                        }
                    }
                },
                {
                    "name": "\u6587\u732e\u9605\u8bfb",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,77,25)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u901f\u5b66\u4e60\u80fd\u529b",
                    "value": 62,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,42,47)"
                        }
                    }
                },
                {
                    "name": "CNN",
                    "value": 61,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,84,5)"
                        }
                    }
                }
            ],
            "drawOutOfBound": false,
            "textStyle": {
                "emphasis": {}
            }
        }
    ],
    "legend": [
        {
            "data": [],
            "selected": {},
            "show": true,
            "padding": 5,
            "itemGap": 10,
            "itemWidth": 25,
            "itemHeight": 14
        }
    ],
    "tooltip": {
        "show": true,
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "showContent": true,
        "alwaysShowContent": false,
        "showDelay": 0,
        "hideDelay": 100,
        "textStyle": {
            "fontSize": 14
        },
        "borderWidth": 0,
        "padding": 5
    },
    "title": [
        {
            "text": "CV\u4efb\u804c\u8981\u6c42\u5173\u952e\u8bcd",
            "padding": 5,
            "itemGap": 10,
            "textStyle": {
                "fontSize": 23
            }
        }
    ]
};
        chart_4f4bdabde7c6463daf9313c70d1a8e73.setOption(option_4f4bdabde7c6463daf9313c70d1a8e73);
    </script>
                <div id="c90670413a9441b48ad004799a71e6e9" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_c90670413a9441b48ad004799a71e6e9 = echarts.init(
            document.getElementById('c90670413a9441b48ad004799a71e6e9'), 'white', {renderer: 'canvas'});
            
    var waterMarkText = 'ShowMeAI';
    var canvas = document.createElement('canvas');
    var ctx = canvas.getContext('2d');
    canvas.width = canvas.height = 300;
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.globalAlpha = 0.03;
    ctx.font = '50px Microsoft Yahei';
    ctx.translate(100, 100);
    ctx.rotate(-Math.PI / 4);
    ctx.fillText(waterMarkText, 0, 0);
    img = canvas;
    
        var option_c90670413a9441b48ad004799a71e6e9 = {
    "backgroundColor": {
        "type": "pattern",
        "image": img,
        "repeat": "repeat"
    },
    "animation": true,
    "animationThreshold": 2000,
    "animationDuration": 1000,
    "animationEasing": "cubicOut",
    "animationDelay": 0,
    "animationDurationUpdate": 300,
    "animationEasingUpdate": "cubicOut",
    "animationDelayUpdate": 0,
    "color": [
        "#c23531",
        "#2f4554",
        "#61a0a8",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3",
        "#f05b72",
        "#ef5b9c",
        "#f47920",
        "#905a3d",
        "#fab27b",
        "#2a5caa",
        "#444693",
        "#726930",
        "#b2d235",
        "#6d8346",
        "#ac6767",
        "#1d953f",
        "#6950a1",
        "#918597"
    ],
    "series": [
        {
            "type": "wordCloud",
            "name": "\u63a8\u8350\u7b97\u6cd5\u5de5\u4f5c\u804c\u8d23\u5173\u952e\u8bcd",
            "shape": "circle",
            "rotationRange": [
                -90,
                90
            ],
            "rotationStep": 45,
            "girdSize": 20,
            "sizeRange": [
                14,
                48
            ],
            "data": [
                {
                    "name": "\u7528\u6237\u884c\u4e3a\u6a21\u578b",
                    "value": 100,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,77,41)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u7cfb\u7edf\u6838\u5fc3\u7b97\u6cd5\u7814\u53d1",
                    "value": 99,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,124,89)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u5174\u8da3\u5efa\u6a21",
                    "value": 98,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,92,19)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u5b9e\u65f6\u610f\u56fe\u5efa\u6a21",
                    "value": 97,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,158,34)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6316\u6398",
                    "value": 96,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,42,102)"
                        }
                    }
                },
                {
                    "name": "\u4e2a\u6027\u5316\u63a8\u8350",
                    "value": 95,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,137,141)"
                        }
                    }
                },
                {
                    "name": "\u4e2a\u6027\u5316\u63a8\u9001\u7b97\u6cd5",
                    "value": 94,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,11,74)"
                        }
                    }
                },
                {
                    "name": "\u53ec\u56de",
                    "value": 93,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,19,103)"
                        }
                    }
                },
                {
                    "name": "\u6392\u5e8f",
                    "value": 92,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,5,97)"
                        }
                    }
                },
                {
                    "name": "\u51b7\u542f\u52a8",
                    "value": 91,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,115,69)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u753b\u50cf\u4f18\u5316",
                    "value": 90,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,9,75)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u80fd\u529b\u6a21\u578b",
                    "value": 89,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,160,80)"
                        }
                    }
                },
                {
                    "name": "\u4f9b\u9700\u5173\u7cfb\u6a21\u578b",
                    "value": 88,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,53,153)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u7b56\u7565",
                    "value": 87,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,122,113)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u6d41\u63a8\u8350",
                    "value": 86,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,60,153)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350/\u641c\u7d22/\u5e7f\u544a",
                    "value": 85,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,144,31)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u63a8\u8350",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,133,0)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u8425\u9500",
                    "value": 83,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,109,36)"
                        }
                    }
                },
                {
                    "name": "feed\u6d41\u63a8\u8350\u3001\u76f8\u5173\u6027\u63a8\u8350",
                    "value": 82,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,159,80)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u8d28\u91cf\u4f53\u7cfb",
                    "value": 81,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,33,53)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u6807\u7b7e\u4f53\u7cfb",
                    "value": 80,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,133,56)"
                        }
                    }
                },
                {
                    "name": "\u4e0b\u5355\u9884\u4f30",
                    "value": 79,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,78,72)"
                        }
                    }
                },
                {
                    "name": "\u767e\u5ea6",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,20,61)"
                        }
                    }
                },
                {
                    "name": "\u6dd8\u5b9d",
                    "value": 77,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,112,158)"
                        }
                    }
                },
                {
                    "name": "\u5b57\u8282\u8df3\u52a8",
                    "value": 76,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,159,90)"
                        }
                    }
                },
                {
                    "name": "\u6296\u97f3",
                    "value": 75,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,93,83)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u624b",
                    "value": 74,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,41,81)"
                        }
                    }
                },
                {
                    "name": "\u4eac\u4e1c",
                    "value": 73,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,16,154)"
                        }
                    }
                },
                {
                    "name": "\u7ebf\u4e0a\u6392\u5e8f\u7cfb\u7edf",
                    "value": 72,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,41,86)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u95fb\u63a8\u8350",
                    "value": 71,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,121,52)"
                        }
                    }
                },
                {
                    "name": "\u957f\u77ed\u671f\u753b\u50cf",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,65,113)"
                        }
                    }
                },
                {
                    "name": "query\u7406\u89e3",
                    "value": 69,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,3,160)"
                        }
                    }
                },
                {
                    "name": "query\u76f8\u5173\u63a8\u8350",
                    "value": 68,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,91,91)"
                        }
                    }
                },
                {
                    "name": "\u6d41\u91cf\u4f18\u5316",
                    "value": 67,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,117,50)"
                        }
                    }
                },
                {
                    "name": "\u5546\u4e1a\u5316",
                    "value": 66,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,91,17)"
                        }
                    }
                },
                {
                    "name": "\u6d88\u8d39\u65f6\u957f",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,120,110)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u7559\u5b58",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,0,143)"
                        }
                    }
                },
                {
                    "name": "\u505c\u7559\u65f6\u957f\u4f18\u5316",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,82,92)"
                        }
                    }
                },
                {
                    "name": "\u70b9\u51fb\u7387\u4f18\u5316",
                    "value": 62,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,25,54)"
                        }
                    }
                },
                {
                    "name": "\u7559\u5b58\u7387\u4f18\u5316",
                    "value": 61,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,57,155)"
                        }
                    }
                }
            ],
            "drawOutOfBound": false,
            "textStyle": {
                "emphasis": {}
            }
        }
    ],
    "legend": [
        {
            "data": [],
            "selected": {},
            "show": true,
            "padding": 5,
            "itemGap": 10,
            "itemWidth": 25,
            "itemHeight": 14
        }
    ],
    "tooltip": {
        "show": true,
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "showContent": true,
        "alwaysShowContent": false,
        "showDelay": 0,
        "hideDelay": 100,
        "textStyle": {
            "fontSize": 14
        },
        "borderWidth": 0,
        "padding": 5
    },
    "title": [
        {
            "text": "\u63a8\u8350\u7b97\u6cd5\u5de5\u4f5c\u804c\u8d23\u5173\u952e\u8bcd",
            "padding": 5,
            "itemGap": 10,
            "textStyle": {
                "fontSize": 23
            }
        }
    ]
};
        chart_c90670413a9441b48ad004799a71e6e9.setOption(option_c90670413a9441b48ad004799a71e6e9);
    </script>
                <div id="20c3bc576c1d4da49b2d2d2441118c2a" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_20c3bc576c1d4da49b2d2d2441118c2a = echarts.init(
            document.getElementById('20c3bc576c1d4da49b2d2d2441118c2a'), 'white', {renderer: 'canvas'});
            
    var waterMarkText = 'ShowMeAI';
    var canvas = document.createElement('canvas');
    var ctx = canvas.getContext('2d');
    canvas.width = canvas.height = 300;
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.globalAlpha = 0.03;
    ctx.font = '50px Microsoft Yahei';
    ctx.translate(100, 100);
    ctx.rotate(-Math.PI / 4);
    ctx.fillText(waterMarkText, 0, 0);
    img = canvas;
    
        var option_20c3bc576c1d4da49b2d2d2441118c2a = {
    "backgroundColor": {
        "type": "pattern",
        "image": img,
        "repeat": "repeat"
    },
    "animation": true,
    "animationThreshold": 2000,
    "animationDuration": 1000,
    "animationEasing": "cubicOut",
    "animationDelay": 0,
    "animationDurationUpdate": 300,
    "animationEasingUpdate": "cubicOut",
    "animationDelayUpdate": 0,
    "color": [
        "#c23531",
        "#2f4554",
        "#61a0a8",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3",
        "#f05b72",
        "#ef5b9c",
        "#f47920",
        "#905a3d",
        "#fab27b",
        "#2a5caa",
        "#444693",
        "#726930",
        "#b2d235",
        "#6d8346",
        "#ac6767",
        "#1d953f",
        "#6950a1",
        "#918597"
    ],
    "series": [
        {
            "type": "wordCloud",
            "name": "\u63a8\u8350\u7b97\u6cd5\u4efb\u804c\u8981\u6c42\u5173\u952e\u8bcd",
            "shape": "circle",
            "rotationRange": [
                -90,
                90
            ],
            "rotationStep": 45,
            "girdSize": 20,
            "sizeRange": [
                15,
                48
            ],
            "data": [
                {
                    "name": "Keras",
                    "value": 100,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,46,5)"
                        }
                    }
                },
                {
                    "name": "Tensorflow",
                    "value": 99,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,51,107)"
                        }
                    }
                },
                {
                    "name": "PyTorch",
                    "value": 98,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,23,62)"
                        }
                    }
                },
                {
                    "name": "\u534f\u540c\u8fc7\u6ee4",
                    "value": 97,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,27,12)"
                        }
                    }
                },
                {
                    "name": "FM",
                    "value": 96,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,133,49)"
                        }
                    }
                },
                {
                    "name": "LR",
                    "value": 95,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,78,72)"
                        }
                    }
                },
                {
                    "name": "NN",
                    "value": 94,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,148,78)"
                        }
                    }
                },
                {
                    "name": "LSTM",
                    "value": 93,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,145,115)"
                        }
                    }
                },
                {
                    "name": "GBDT",
                    "value": 92,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,13,48)"
                        }
                    }
                },
                {
                    "name": "C/C++",
                    "value": 91,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,44,40)"
                        }
                    }
                },
                {
                    "name": "Python",
                    "value": 90,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,11,34)"
                        }
                    }
                },
                {
                    "name": "Java",
                    "value": 89,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,81,136)"
                        }
                    }
                },
                {
                    "name": "Hadoop",
                    "value": 88,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,47,52)"
                        }
                    }
                },
                {
                    "name": "Spark",
                    "value": 87,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,127,1)"
                        }
                    }
                },
                {
                    "name": "Storm",
                    "value": 86,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,96,39)"
                        }
                    }
                },
                {
                    "name": "CTR\u9884\u4f30",
                    "value": 85,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,126,87)"
                        }
                    }
                },
                {
                    "name": "xgboost",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,141,2)"
                        }
                    }
                },
                {
                    "name": "lightgbm",
                    "value": 83,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,92,7)"
                        }
                    }
                },
                {
                    "name": "catboost",
                    "value": 82,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,36,11)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u6216\u641c\u7d22\u76f8\u5173\u7ecf\u9a8c",
                    "value": 81,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,97,44)"
                        }
                    }
                },
                {
                    "name": "\u53ec\u56de/\u6392\u5e8f\u7b97\u6cd5",
                    "value": 80,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,115,92)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60",
                    "value": 79,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,57,24)"
                        }
                    }
                },
                {
                    "name": "\u5f3a\u5316\u5b66\u4e60",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,4,54)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u70b9\u51fb\u7387\u9884\u4f30",
                    "value": 77,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,50,19)"
                        }
                    }
                },
                {
                    "name": "\u4e2a\u6027\u5316\u63a8\u8350\u6a21\u578b",
                    "value": 76,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,3,139)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u6392\u5e8f",
                    "value": 75,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,50,89)"
                        }
                    }
                },
                {
                    "name": "LearningToRank",
                    "value": 74,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,158,33)"
                        }
                    }
                },
                {
                    "name": "word2vec",
                    "value": 73,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,153,84)"
                        }
                    }
                },
                {
                    "name": "RecSys",
                    "value": 72,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,117,45)"
                        }
                    }
                },
                {
                    "name": "SIGIR",
                    "value": 71,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,85,126)"
                        }
                    }
                },
                {
                    "name": "WWW",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,143,122)"
                        }
                    }
                },
                {
                    "name": "ICML",
                    "value": 69,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,146,122)"
                        }
                    }
                },
                {
                    "name": "NIPS",
                    "value": 68,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,156,89)"
                        }
                    }
                },
                {
                    "name": "\u70b9\u51fb\u7387\u9884\u4f30",
                    "value": 67,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,14,106)"
                        }
                    }
                },
                {
                    "name": "\u6295\u9012\u9884\u4f30",
                    "value": 66,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,64,32)"
                        }
                    }
                },
                {
                    "name": "\u9884\u7b97\u5efa\u8bae",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,22,8)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u4ef7\u673a\u5236",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,62,34)"
                        }
                    }
                },
                {
                    "name": "\u5206\u5e03\u5f0f\u8ba1\u7b97",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,153,2)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u5854\u6a21\u578b",
                    "value": 62,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,88,29)"
                        }
                    }
                },
                {
                    "name": "\u7279\u5f81\u5de5\u7a0b",
                    "value": 61,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,31,147)"
                        }
                    }
                }
            ],
            "drawOutOfBound": false,
            "textStyle": {
                "emphasis": {}
            }
        }
    ],
    "legend": [
        {
            "data": [],
            "selected": {},
            "show": true,
            "padding": 5,
            "itemGap": 10,
            "itemWidth": 25,
            "itemHeight": 14
        }
    ],
    "tooltip": {
        "show": true,
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "showContent": true,
        "alwaysShowContent": false,
        "showDelay": 0,
        "hideDelay": 100,
        "textStyle": {
            "fontSize": 14
        },
        "borderWidth": 0,
        "padding": 5
    },
    "title": [
        {
            "text": "\u63a8\u8350\u7b97\u6cd5\u4efb\u804c\u8981\u6c42\u5173\u952e\u8bcd",
            "padding": 5,
            "itemGap": 10,
            "textStyle": {
                "fontSize": 23
            }
        }
    ]
};
        chart_20c3bc576c1d4da49b2d2d2441118c2a.setOption(option_20c3bc576c1d4da49b2d2d2441118c2a);
    </script>
    </div>

    <script>
    </script>
    <script>
        (function() {
            containers = document.getElementsByClassName("chart-container");
            if(containers.length > 0) {
                containers[0].style.display = "block";
            }
        })()

        function showChart(evt, chartID) {
            let containers = document.getElementsByClassName("chart-container");
            for (let i = 0; i < containers.length; i++) {
                containers[i].style.display = "none";
            }

            let tablinks = document.getElementsByClassName("tablinks");
            for (let i = 0; i < tablinks.length; i++) {
                tablinks[i].className = "tablinks";
            }

            document.getElementById(chartID).style.display = "block";
            evt.currentTarget.className += " active";
        }
    </script>
</body>
</html>
