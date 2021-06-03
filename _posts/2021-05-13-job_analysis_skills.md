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

<h2>（2021-06-03更新）</h2>

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
            <button class="tablinks" onclick="showChart(event, '6ee0591be146426ba0d200687a0c520a')">关键词</button>
            <button class="tablinks" onclick="showChart(event, 'e6467948103948899914325ca2f0b8ed')">关键词分布</button>
            <button class="tablinks" onclick="showChart(event, 'd09a42159f8644faa96fdc3d480a70c6')">学历要求</button>
            <button class="tablinks" onclick="showChart(event, '885711c5885f40dfb2fd445d89d1cebb')">经验要求</button>
            <button class="tablinks" onclick="showChart(event, '4562f0b8363c426496fe107df707b020')">NLP岗位职责</button>
            <button class="tablinks" onclick="showChart(event, '86fe6d08f82149e1b07299818e413a24')">NLP任职要求</button>
            <button class="tablinks" onclick="showChart(event, '10ae9a71fc1b4f6f869e91d9d334d7a7')">CV岗位职责</button>
            <button class="tablinks" onclick="showChart(event, '068ef39b14de4f358941e7f1e4b60fa0')">CV任职要求</button>
            <button class="tablinks" onclick="showChart(event, '2a0eb8de6cc54bcd9eefdf765ff8141d')">推荐算法岗位职责</button>
            <button class="tablinks" onclick="showChart(event, 'bb90e206890840b09465eb5f6cabef04')">推荐算法任职要求</button>
    </div>

    <div class="box">
                <div id="6ee0591be146426ba0d200687a0c520a" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_6ee0591be146426ba0d200687a0c520a = echarts.init(
            document.getElementById('6ee0591be146426ba0d200687a0c520a'), 'white', {renderer: 'canvas'});
            
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
    
        var option_6ee0591be146426ba0d200687a0c520a = {
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
                451,
                286,
                184,
                144,
                124,
                119,
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
                    "value": 451,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,129,3)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u670d\u52a1",
                    "value": 286,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,7,85)"
                        }
                    }
                },
                {
                    "name": "Python",
                    "value": 184,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,98,70)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6316\u6398",
                    "value": 144,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,114,113)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u7b97\u6cd5",
                    "value": 124,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,88,96)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u5b66\u4e60",
                    "value": 119,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,102,33)"
                        }
                    }
                },
                {
                    "name": "C/C++",
                    "value": 110,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,53,49)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u7247\u8bc6\u522b",
                    "value": 103,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,57,135)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u7b97\u6cd5",
                    "value": 92,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,154,48)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u8138\u8bc6\u522b",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,88,57)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546\u5e73\u53f0",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,131,105)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7136\u8bed\u8a00\u5904\u7406",
                    "value": 69,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,160,8)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,154,64)"
                        }
                    }
                },
                {
                    "name": "\u7ee9\u6548\u5956\u91d1",
                    "value": 60,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,109,60)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u786c\u4ef6",
                    "value": 59,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,85,155)"
                        }
                    }
                },
                {
                    "name": "\u8f6f\u4ef6\u670d\u52a1\uff5c\u54a8\u8be2",
                    "value": 59,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,81,153)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u670d\u52a1\uff5c\u54a8\u8be2",
                    "value": 56,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,160,2)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e",
                    "value": 55,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,148,56)"
                        }
                    }
                },
                {
                    "name": "Java",
                    "value": 54,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,125,48)"
                        }
                    }
                },
                {
                    "name": "\u6280\u80fd\u57f9\u8bad",
                    "value": 50,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,106,116)"
                        }
                    }
                },
                {
                    "name": "C++",
                    "value": 50,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,14,127)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u5e74\u5047",
                    "value": 45,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,69,113)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u5f0f\u8bc6\u522b",
                    "value": 44,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,131,142)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u7b97\u6cd5",
                    "value": 42,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,141,64)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u8bc6\u522b",
                    "value": 40,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,78,142)"
                        }
                    }
                },
                {
                    "name": "\u79fb\u52a8\u4e92\u8054\u7f51",
                    "value": 38,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,0,60)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5904\u7406",
                    "value": 37,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,145,137)"
                        }
                    }
                },
                {
                    "name": "\u5c97\u4f4d\u664b\u5347",
                    "value": 36,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,3,56)"
                        }
                    }
                },
                {
                    "name": "\u7269\u8054\u7f51",
                    "value": 34,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,47,44)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u5de5\u4f5c",
                    "value": 33,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,104,43)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u56fe\u50cf\u89c6\u89c9",
                    "value": 32,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,72,77)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u7ba1\u7406",
                    "value": 31,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,43,25)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u673a\u89c6\u89c9",
                    "value": 31,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,33,12)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u6280\u91d1\u878d",
                    "value": 31,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,53,42)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u5065\u5eb7",
                    "value": 30,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,21,90)"
                        }
                    }
                },
                {
                    "name": "\u9886\u5bfc\u597d",
                    "value": 30,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,120,41)"
                        }
                    }
                },
                {
                    "name": "OpenCV",
                    "value": 30,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,67,76)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u7cfb\u7edf",
                    "value": 29,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,63,150)"
                        }
                    }
                },
                {
                    "name": "TensoFlow",
                    "value": 29,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,78,72)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u5206\u7c7b",
                    "value": 29,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,14,127)"
                        }
                    }
                },
                {
                    "name": "NLP",
                    "value": 28,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,10,65)"
                        }
                    }
                },
                {
                    "name": "\u6587\u5b57\u8bc6\u522b",
                    "value": 28,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,158,2)"
                        }
                    }
                },
                {
                    "name": "\u76ee\u6807\u68c0\u6d4b",
                    "value": 28,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,38,83)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1",
                    "value": 27,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,54,26)"
                        }
                    }
                },
                {
                    "name": "PyTorch",
                    "value": 26,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,110,140)"
                        }
                    }
                },
                {
                    "name": "IT\u6280\u672f\u670d\u52a1\uff5c\u54a8\u8be2",
                    "value": 25,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,49,3)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76",
                    "value": 25,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,79,89)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u96f6\u552e",
                    "value": 24,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,109,149)"
                        }
                    }
                },
                {
                    "name": "\u80a1\u7968\u671f\u6743",
                    "value": 24,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,92,108)"
                        }
                    }
                },
                {
                    "name": "\u8282\u65e5\u793c\u7269",
                    "value": 24,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,104,29)"
                        }
                    }
                },
                {
                    "name": "nan",
                    "value": 24,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,153,97)"
                        }
                    }
                },
                {
                    "name": "\u540e\u7aef\u5f00\u53d1",
                    "value": 23,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,33,85)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u5177\u7c7b\u4ea7\u54c1",
                    "value": 22,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,28,121)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4ea4\u5e73\u53f0",
                    "value": 22,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,53,149)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d",
                    "value": 21,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,106,75)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5e95\u53cc\u85aa",
                    "value": 21,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,19,69)"
                        }
                    }
                },
                {
                    "name": "\u5728\u7ebf\u6559\u80b2",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,68,26)"
                        }
                    }
                },
                {
                    "name": "\u6e38\u620f",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,127,70)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u671f\u4f53\u68c0",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,157,109)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u9891\uff5c\u89c6\u9891\u5a92\u4f53",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,155,55)"
                        }
                    }
                },
                {
                    "name": "\u610f\u56fe\u8bc6\u522b",
                    "value": 18,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,48,83)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22",
                    "value": 18,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,133,95)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u5408\u6210",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,36,134)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u670d\u52a1",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,44,144)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u89c6\u89c9\u68c0\u6d4b",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,50,48)"
                        }
                    }
                },
                {
                    "name": "\u516d\u9669\u4e00\u91d1",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,125,49)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,136,66)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u751f\u6210",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,144,138)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u73ed\u8f66",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,36,38)"
                        }
                    }
                },
                {
                    "name": "\u5c31\u8fd1\u79df\u623f\u8865\u8d34",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,8,41)"
                        }
                    }
                },
                {
                    "name": "Hadoop",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,13,116)"
                        }
                    }
                },
                {
                    "name": "\u6559\u80b2",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,49,155)"
                        }
                    }
                },
                {
                    "name": "MATLAB",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,124,125)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u670d\u52a1",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,123,50)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u9879\u5956\u91d1",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,150,10)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u9891\u7b97\u6cd5",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,145,116)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u8ba1\u7b97",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,31,114)"
                        }
                    }
                },
                {
                    "name": "\u6d88\u8d39\u751f\u6d3b",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,143,24)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u5f71\u50cf\u8bca\u65ad",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,117,42)"
                        }
                    }
                },
                {
                    "name": "C",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,158,156)"
                        }
                    }
                },
                {
                    "name": "CNN",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,119,94)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u7b97\u6cd5",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,53,120)"
                        }
                    }
                },
                {
                    "name": "\u8f85\u52a9/\u667a\u80fd\u9a7e\u9a76",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,8,128)"
                        }
                    }
                },
                {
                    "name": "\u5728\u7ebf\u533b\u7597",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,104,100)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5206\u6790",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,80,117)"
                        }
                    }
                },
                {
                    "name": "\u670d\u52a1\u673a\u5668\u4eba",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,85,99)"
                        }
                    }
                },
                {
                    "name": "\u5efa\u6a21",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,159,147)"
                        }
                    }
                },
                {
                    "name": "\u6570\u4ed3\u5efa\u6a21",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,107,34)"
                        }
                    }
                },
                {
                    "name": "XGBoost",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,158,114)"
                        }
                    }
                },
                {
                    "name": "\u4f01\u4e1a\u670d\u52a1",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,58,23)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u6e38\uff5c\u51fa\u884c",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,153,37)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u4e50",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,50,43)"
                        }
                    }
                },
                {
                    "name": "AI",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,22,119)"
                        }
                    }
                },
                {
                    "name": "\u7269\u6d41\uff5c\u8fd0\u8f93",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,146,47)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891/\u76d1\u63a7\u5206\u6790",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,140,78)"
                        }
                    }
                },
                {
                    "name": "\u8425\u9500\u670d\u52a1\uff5c\u54a8\u8be2",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,0,68)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u8d44\u8baf",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,12,37)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u7edc\u901a\u4fe1",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,144,27)"
                        }
                    }
                },
                {
                    "name": "\u7ba1\u7406\u89c4\u8303",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,52,39)"
                        }
                    }
                },
                {
                    "name": "SLAM",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,2,55)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\uff5c\u4fdd\u5065\uff5c\u7f8e\u5bb9",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,139,113)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,103,46)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u793e\u533a",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,26,120)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u5b89\u5168",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,159,133)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4ea4",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,10,69)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u8425\u9500",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,59,48)"
                        }
                    }
                },
                {
                    "name": "\u95ee\u7b54\u7cfb\u7edf",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,2,45)"
                        }
                    }
                },
                {
                    "name": "\u77ed\u89c6\u9891",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,52,140)"
                        }
                    }
                },
                {
                    "name": "Spark",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,105,121)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u80fd\u6e90\u6c7d\u8f66\u5236\u9020",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,108,14)"
                        }
                    }
                },
                {
                    "name": "\u8def\u5f84\u89c4\u5212",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,135,86)"
                        }
                    }
                },
                {
                    "name": "TensorFlow",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,60,43)"
                        }
                    }
                },
                {
                    "name": "RNN",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,140,49)"
                        }
                    }
                },
                {
                    "name": "Caffe",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,24,108)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79\u4f18\u5316",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,21,114)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u6587\u5206\u8bcd",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,52,94)"
                        }
                    }
                },
                {
                    "name": "Shell",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,58,94)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u8865\u52a9",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,18,112)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u5973\u591a",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,118,33)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u62bd\u53d6",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,109,139)"
                        }
                    }
                },
                {
                    "name": "Scala",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,153,113)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51\u91d1\u878d",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,2,101)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u8bc6\u56fe\u8c31",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,144,79)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,30,99)"
                        }
                    }
                },
                {
                    "name": "\u6ef4\u6ef4",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,30,139)"
                        }
                    }
                },
                {
                    "name": "python",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,121,145)"
                        }
                    }
                },
                {
                    "name": "\u671f\u6743\u4e30\u539a",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,104,68)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u56e2\u961f",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,85,33)"
                        }
                    }
                },
                {
                    "name": "\u7269\u6d41",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,78,50)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u7b97\u6cd5",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,153,50)"
                        }
                    }
                },
                {
                    "name": "\u529e\u516c\u903c\u683c\u9ad8",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,55,1)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u5177\u8f6f\u4ef6",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,19,36)"
                        }
                    }
                },
                {
                    "name": "\u53e5\u6cd5\u5206\u6790",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,120,52)"
                        }
                    }
                },
                {
                    "name": "Keras",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,75,112)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u5de5\u7a0b\u5e08",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,59,131)"
                        }
                    }
                },
                {
                    "name": "\u5782\u76f4\u641c\u7d22",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,53,142)"
                        }
                    }
                },
                {
                    "name": "MCN\uff5c\u76f4\u64ad\u5e73\u53f0",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,100,84)"
                        }
                    }
                },
                {
                    "name": "Linux",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,133,35)"
                        }
                    }
                },
                {
                    "name": "\u94f6\u884c",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,105,86)"
                        }
                    }
                },
                {
                    "name": "ARM",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,145,97)"
                        }
                    }
                },
                {
                    "name": "linux",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,103,51)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4ea4\u5a92\u4f53",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,132,157)"
                        }
                    }
                },
                {
                    "name": "\u901a\u8baf\u6d25\u8d34",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,150,10)"
                        }
                    }
                },
                {
                    "name": "nlp",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,75,95)"
                        }
                    }
                },
                {
                    "name": "GAN",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,159,42)"
                        }
                    }
                },
                {
                    "name": "\u533a\u5757\u94fe",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,135,88)"
                        }
                    }
                },
                {
                    "name": "Hive",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,36,101)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u91d1\u878d",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,109,130)"
                        }
                    }
                },
                {
                    "name": "spark",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,68,60)"
                        }
                    }
                },
                {
                    "name": "\u8bcd\u6027\u6807\u6ce8",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,18,134)"
                        }
                    }
                },
                {
                    "name": "\u6559\u80b2\uff5c\u57f9\u8bad",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,16,76)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u7ed3\u6784",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,106,73)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,66,36)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5ea6\u65c5\u6e38",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,0,48)"
                        }
                    }
                },
                {
                    "name": "tensorflow",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,132,91)"
                        }
                    }
                },
                {
                    "name": "RTK",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,67,9)"
                        }
                    }
                },
                {
                    "name": "CV",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,50,110)"
                        }
                    }
                },
                {
                    "name": "\u6c7d\u8f66",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,24,30)"
                        }
                    }
                },
                {
                    "name": "MySQL",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,57,159)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u753b\u50cf",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,46,59)"
                        }
                    }
                },
                {
                    "name": "c++",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,54,3)"
                        }
                    }
                },
                {
                    "name": "Golang",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,45,151)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u4e1a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,155,147)"
                        }
                    }
                },
                {
                    "name": "\u5c45\u4f4f\u670d\u52a1",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,51,52)"
                        }
                    }
                },
                {
                    "name": "opencv",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,69,72)"
                        }
                    }
                },
                {
                    "name": "Tensorflow",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,83,57)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u5904\u7406",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,157,65)"
                        }
                    }
                },
                {
                    "name": "CTR\u9884\u4f30",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,97,50)"
                        }
                    }
                },
                {
                    "name": "ROS",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,34,160)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,55,126)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,125,45)"
                        }
                    }
                },
                {
                    "name": "HALCON",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,89,151)"
                        }
                    }
                },
                {
                    "name": "\u6587\u5316\u4f20\u5a92",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,64,124)"
                        }
                    }
                },
                {
                    "name": "kaggle",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,69,146)"
                        }
                    }
                },
                {
                    "name": "SQL",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,47,64)"
                        }
                    }
                },
                {
                    "name": "nlp\u7b97\u6cd5\u5de5\u7a0b\u5e08",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,160,73)"
                        }
                    }
                },
                {
                    "name": "\u7cbe\u82f1\u56e2\u961f",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,67,131)"
                        }
                    }
                },
                {
                    "name": "\u751f\u6d3b\u670d\u52a1",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,124,69)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u89c6\u89c9",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,39,28)"
                        }
                    }
                },
                {
                    "name": "\u4f20\u611f\u5668",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,100,17)"
                        }
                    }
                },
                {
                    "name": "OCR",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,138,19)"
                        }
                    }
                },
                {
                    "name": "\u8fea\u58eb\u5c3c",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,95,122)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u68c0\u7d22",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,2,49)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u4e92\u8054\u7f51",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,109,5)"
                        }
                    }
                },
                {
                    "name": "GBDT",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,71,26)"
                        }
                    }
                },
                {
                    "name": "\u5546\u4e1a\u822a\u5929",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,126,106)"
                        }
                    }
                },
                {
                    "name": "\u5730\u56fe",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,117,20)"
                        }
                    }
                },
                {
                    "name": "\u8ffd\u6c42\u6781\u81f4",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,8,139)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u4eba\u8f66",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,60,59)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u8bc6\u522b",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,130,59)"
                        }
                    }
                },
                {
                    "name": "\u540e\u7aef",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,20,132)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u89c6\u9891",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,54,117)"
                        }
                    }
                },
                {
                    "name": "ROS\u7cfb\u7edf",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,140,116)"
                        }
                    }
                },
                {
                    "name": "\u795e\u7ecf\u7f51\u7edc",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,18,26)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u641c\u7d22",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,110,144)"
                        }
                    }
                },
                {
                    "name": "ETA",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,15,7)"
                        }
                    }
                },
                {
                    "name": "\u6559\u80b2\u8f85\u5bfc",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,34,146)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u8574\u6db5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,133,87)"
                        }
                    }
                },
                {
                    "name": "opengl",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,88,97)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5e93",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,3,83)"
                        }
                    }
                },
                {
                    "name": "\u70b9\u4e91",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,96,48)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u8bbe\u8ba1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,6,160)"
                        }
                    }
                },
                {
                    "name": "\u6d41\u5a92\u4f53",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,103,74)"
                        }
                    }
                },
                {
                    "name": "Pytorch",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,98,75)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u5668\u68b0",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,131,93)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u5316\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,17,52)"
                        }
                    }
                },
                {
                    "name": "\u8f6f\u4ef6\u5f00\u53d1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,47,149)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u5bb6\u5c45",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,41,122)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u539a\u5e74\u7ec8",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,52,157)"
                        }
                    }
                },
                {
                    "name": "matlab",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,28,136)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79\u5b66",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,138,149)"
                        }
                    }
                },
                {
                    "name": "\u5d4c\u5165\u5f0f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,123,114)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u7ffb\u8bd1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,2,110)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5206\u7ea2",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,131,105)"
                        }
                    }
                },
                {
                    "name": "\u672c\u5206",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,34,96)"
                        }
                    }
                },
                {
                    "name": "\u5e05\u54e5\u591a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,139,57)"
                        }
                    }
                },
                {
                    "name": "\u5f3a\u5316\u5b66\u4e60",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,148,106)"
                        }
                    }
                },
                {
                    "name": "slam",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,90,114)"
                        }
                    }
                },
                {
                    "name": "ElasticSearch",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,15,145)"
                        }
                    }
                },
                {
                    "name": "\u8111\u673a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,51,127)"
                        }
                    }
                },
                {
                    "name": "OpenCL",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,157,136)"
                        }
                    }
                },
                {
                    "name": "\u901a\u4fe1/\u7f51\u7edc\u8bbe\u5907",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,106,119)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,135,139)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4ea4\u5a92\u4f53\u5e73\u53f0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,79,82)"
                        }
                    }
                },
                {
                    "name": "\u534f\u540c\u8fc7\u6ee4",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,53,25)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u81ea\u52a8\u5316",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,50,124)"
                        }
                    }
                },
                {
                    "name": "\u805a\u7c7b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,49,39)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u8138\u751f\u6210",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,157,35)"
                        }
                    }
                },
                {
                    "name": "\u5206\u5e03\u5f0f\u641c\u7d22",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,158,16)"
                        }
                    }
                },
                {
                    "name": "\u6392\u5e8f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,68,51)"
                        }
                    }
                },
                {
                    "name": "ACM",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,62,118)"
                        }
                    }
                },
                {
                    "name": "PaddlePddle",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,158,138)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u68c0\u6d4b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,86,160)"
                        }
                    }
                },
                {
                    "name": "\u4f9b\u5e94\u94fe\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,156,59)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,85,141)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,40,73)"
                        }
                    }
                },
                {
                    "name": "\u5348\u9910\u8865\u52a9",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,15,134)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u52a8\u65e5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,129,102)"
                        }
                    }
                },
                {
                    "name": "\u7cfb\u7edf\u67b6\u6784",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,28,4)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u4ed3\u5e93",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,38,65)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5206\u5272",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,104,7)"
                        }
                    }
                },
                {
                    "name": "\u7535\u673a\u63a7\u5236",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,88,67)"
                        }
                    }
                },
                {
                    "name": "CAD",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,95,49)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7406\u89e3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,153,123)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u8bbe\u8ba1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,46,48)"
                        }
                    }
                },
                {
                    "name": "\u7ade\u54c1\u5206\u6790",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,115,40)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u4f4d\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,94,61)"
                        }
                    }
                },
                {
                    "name": "\u7248\u9762\u5206\u6790",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,80,54)"
                        }
                    }
                },
                {
                    "name": "SNN",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,141,19)"
                        }
                    }
                },
                {
                    "name": "\u8f66\u8054\u7f51",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,62,93)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,133,67)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,148,23)"
                        }
                    }
                },
                {
                    "name": "\u5236\u9020\u4e1a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,67,126)"
                        }
                    }
                },
                {
                    "name": "PPP",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,105,135)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u76ee",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,133,123)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,79,129)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u7ba1\u7406",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,140,153)"
                        }
                    }
                },
                {
                    "name": "\u7acb\u4f53\u5339\u914d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,148,100)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u52a8\u63a7\u5236",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,57,106)"
                        }
                    }
                },
                {
                    "name": "3D",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,88,120)"
                        }
                    }
                },
                {
                    "name": "JAVA",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,85,100)"
                        }
                    }
                },
                {
                    "name": "Matlab",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,135,61)"
                        }
                    }
                },
                {
                    "name": "C#",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,32,158)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,12,24)"
                        }
                    }
                },
                {
                    "name": "\u6027\u80fd\u6d4b\u8bd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,113,56)"
                        }
                    }
                },
                {
                    "name": "\u5206\u7c7b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,107,52)"
                        }
                    }
                },
                {
                    "name": "\u6570\u4ed3\u67b6\u6784",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,120,111)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u673a\u56fe\u5f62\u5b66",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,63,88)"
                        }
                    }
                },
                {
                    "name": "\u51fa\u56fd\u65c5\u6e38",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,149,139)"
                        }
                    }
                },
                {
                    "name": "gnss",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,83,57)"
                        }
                    }
                },
                {
                    "name": "Flink",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,77,34)"
                        }
                    }
                },
                {
                    "name": "\u76f4\u64ad",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,73,14)"
                        }
                    }
                },
                {
                    "name": "\u53cd\u4f5c\u5f0a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,73,34)"
                        }
                    }
                },
                {
                    "name": "\u7c7b\u8111\u8ba1\u7b97",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,130,119)"
                        }
                    }
                },
                {
                    "name": "\u5168\u7403\u5316",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,8,116)"
                        }
                    }
                },
                {
                    "name": "\u7269\u6d41\u5e73\u53f0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,10,152)"
                        }
                    }
                },
                {
                    "name": "\u4e03\u9669\u4e00\u91d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,24,129)"
                        }
                    }
                },
                {
                    "name": "VIO",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,156,133)"
                        }
                    }
                },
                {
                    "name": "\u5f71\u89c6\uff5c\u52a8\u6f2b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,16,59)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6167\u57ce\u5e02",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,106,63)"
                        }
                    }
                },
                {
                    "name": "hadoop",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,100,2)"
                        }
                    }
                },
                {
                    "name": "\u6c7d\u8f66\u4ea4\u6613\u5e73\u53f0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,67,11)"
                        }
                    }
                },
                {
                    "name": "LR",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,123,71)"
                        }
                    }
                },
                {
                    "name": "Lucene",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,38,127)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u589e\u957f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,138,111)"
                        }
                    }
                },
                {
                    "name": "GPU",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,122,58)"
                        }
                    }
                },
                {
                    "name": "\u9700\u6c42\u5206\u6790",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,142,12)"
                        }
                    }
                },
                {
                    "name": "\u7acb\u4f53\u89c6\u89c9",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,23,70)"
                        }
                    }
                },
                {
                    "name": "\u589e\u957f\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,107,25)"
                        }
                    }
                },
                {
                    "name": "\u5305\u5348\u9910\u665a\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,101,116)"
                        }
                    }
                },
                {
                    "name": "\u836f\u7269\u7814\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,26,137)"
                        }
                    }
                },
                {
                    "name": "rgbd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,5,37)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,136,60)"
                        }
                    }
                },
                {
                    "name": "h264\uff0ch265\uff0cav1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,53,63)"
                        }
                    }
                },
                {
                    "name": "\u56de\u58f0\u6d88\u9664",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,14,70)"
                        }
                    }
                },
                {
                    "name": "\u5b8c\u6210E\u8f6e\u878d\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,156,94)"
                        }
                    }
                },
                {
                    "name": "/Pytorch",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,45,142)"
                        }
                    }
                },
                {
                    "name": "\u68c0\u6d4b\u3001\u8bc6\u522b\u3001\u7f16\u8f91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,147,21)"
                        }
                    }
                },
                {
                    "name": "\u8f66\u8f86\u52a8\u529b\u5b66\u5efa\u6a21",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,9,85)"
                        }
                    }
                },
                {
                    "name": "java",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,33,106)"
                        }
                    }
                },
                {
                    "name": "\u5065\u5eb7\u7761\u7720",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,107,99)"
                        }
                    }
                },
                {
                    "name": "\u6e32\u67d3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,65,30)"
                        }
                    }
                },
                {
                    "name": "\u4e16\u754c500\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,111,6)"
                        }
                    }
                },
                {
                    "name": "webgl",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,104,147)"
                        }
                    }
                },
                {
                    "name": "MXNet",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,150,14)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,78,110)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u7a0b\u80fd\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,109,21)"
                        }
                    }
                },
                {
                    "name": "NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,122,96)"
                        }
                    }
                },
                {
                    "name": "rtk",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,47,57)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u5148\u4e0a\u6d77\u843d\u6237",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,135,131)"
                        }
                    }
                },
                {
                    "name": "\u70b9\u4e91\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,69,142)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,37,7)"
                        }
                    }
                },
                {
                    "name": "\u4e70\u624b\u6218\u7565",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,79,155)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5348\u9910\u665a\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,26,45)"
                        }
                    }
                },
                {
                    "name": "\u5348\u9910\u4ea4\u901a\u8865\u52a9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,19,149)"
                        }
                    }
                },
                {
                    "name": "R",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,124,19)"
                        }
                    }
                },
                {
                    "name": "\u901a\u4fe1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,73,95)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,63,63)"
                        }
                    }
                },
                {
                    "name": "\u5730\u56fe\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,149,89)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u89c6\u89c9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,32,82)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u673a\u5668\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,145,149)"
                        }
                    }
                },
                {
                    "name": "\u5e95\u5c42",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,40,40)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u8f6c\u6362",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,115,60)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u6a21\u578b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,156,60)"
                        }
                    }
                },
                {
                    "name": "salm",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,147,125)"
                        }
                    }
                },
                {
                    "name": "SSD",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,95,120)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,88,78)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u5316\u6d4b\u8bd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,60,143)"
                        }
                    }
                },
                {
                    "name": "UWB",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,58,53)"
                        }
                    }
                },
                {
                    "name": "Cplex",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,66,99)"
                        }
                    }
                },
                {
                    "name": "Tensor",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,71,76)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,26,27)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u90e8\u7f72",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,160,20)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u8fd0\u8f93",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,80,99)"
                        }
                    }
                },
                {
                    "name": "\u5a92\u4f53",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,90,113)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u524d\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,52,78)"
                        }
                    }
                },
                {
                    "name": "C/C++/Python",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,139,154)"
                        }
                    }
                },
                {
                    "name": "x265",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,28,26)"
                        }
                    }
                },
                {
                    "name": "pytorch",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,61,29)"
                        }
                    }
                },
                {
                    "name": "Storm",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,126,75)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5730\u6d4b\u91cf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,56,74)"
                        }
                    }
                },
                {
                    "name": "\u7cfb\u7edf\u5206\u6790",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,38,143)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u4e49\u7406\u89e3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,104,156)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,72,63)"
                        }
                    }
                },
                {
                    "name": "hybrid/end2end",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,62,9)"
                        }
                    }
                },
                {
                    "name": "\u692d\u5706\u66f2\u7ebf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,99,125)"
                        }
                    }
                },
                {
                    "name": "ocr",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,118,151)"
                        }
                    }
                },
                {
                    "name": "\u5bfc\u822a\u5f15\u64ce",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,142,155)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,79,76)"
                        }
                    }
                },
                {
                    "name": "\u8425\u9500",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,119,26)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u725b\u4f17\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,6,130)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,146,33)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b\u538b\u7f29",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,72,4)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u7b56\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,157,153)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u52a0\u901f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,121,66)"
                        }
                    }
                },
                {
                    "name": "CPU",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,156,152)"
                        }
                    }
                },
                {
                    "name": "SSD\u3001Faster",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,38,146)"
                        }
                    }
                },
                {
                    "name": "\u5468\u672b\u53cc\u4f11",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,121,13)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,63,7)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u725b\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,74,53)"
                        }
                    }
                },
                {
                    "name": "\u4e50\u5668",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,2,157)"
                        }
                    }
                },
                {
                    "name": "\u7279\u5f81\u6316\u6398",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,124,55)"
                        }
                    }
                },
                {
                    "name": "Pyspark",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,3,10)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,13,148)"
                        }
                    }
                },
                {
                    "name": "\u8f66\u8f86\u8fd0\u52a8\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,83,78)"
                        }
                    }
                },
                {
                    "name": "SSL/TLS",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,31,39)"
                        }
                    }
                },
                {
                    "name": "AutoML",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,111,109)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7cbe\u5730\u56fe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,153,144)"
                        }
                    }
                },
                {
                    "name": "Node.js",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,111,136)"
                        }
                    }
                },
                {
                    "name": "\u626b\u5730\u673a\u5668\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,66,138)"
                        }
                    }
                },
                {
                    "name": "nlp\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,69,131)"
                        }
                    }
                },
                {
                    "name": "B2B",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,74,132)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u6d4b\u8bc4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,154,157)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u62fc\u63a5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,159,8)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u77e5\u8bc6\u8bc1\u660e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,115,63)"
                        }
                    }
                },
                {
                    "name": "SFM",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,36,105)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u8ba1\u7b97",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,20,41)"
                        }
                    }
                },
                {
                    "name": "\u5e95\u76d8\u63a7\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,153,3)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u5206\u7c7b\uff0c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,17,30)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u63a8\u8350",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,153,6)"
                        }
                    }
                },
                {
                    "name": "python/go",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,48,66)"
                        }
                    }
                },
                {
                    "name": "\u89c4\u5212\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,84,0)"
                        }
                    }
                },
                {
                    "name": "\u786c\u4ef6\u5236\u9020",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,142,135)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u6e38",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,54,91)"
                        }
                    }
                },
                {
                    "name": "AR/VR/MR",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,48,34)"
                        }
                    }
                },
                {
                    "name": "\u773c\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,31,30)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u7814\u7a76",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,105,34)"
                        }
                    }
                },
                {
                    "name": "\u6570\u5b57\u4fe1\u53f7\u5904\u7406\u6570",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,100,39)"
                        }
                    }
                },
                {
                    "name": "Attention",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,0,66)"
                        }
                    }
                },
                {
                    "name": "\u9057\u4f20\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,70,142)"
                        }
                    }
                },
                {
                    "name": "GNSS",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,42,18)"
                        }
                    }
                },
                {
                    "name": "CAD\u56fe\u7eb8\u5206\u6790",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,21,9)"
                        }
                    }
                },
                {
                    "name": "\u5355\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,45,91)"
                        }
                    }
                },
                {
                    "name": "flv\uff0cmp3\uff0cmp4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,22,66)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u5168\u5927\u6570\u636e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,48,111)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u68c0\u6d4b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,93,42)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,157,140)"
                        }
                    }
                },
                {
                    "name": "\u7279\u6548",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,45,65)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u7ed3\u6784\u4e0e\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,102,141)"
                        }
                    }
                },
                {
                    "name": "\u8f68\u8ff9\u89c4\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,103,158)"
                        }
                    }
                },
                {
                    "name": "\u8054\u90a6\u5b66\u4e60",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,55,73)"
                        }
                    }
                },
                {
                    "name": "ADAS\u7cfb\u7edf\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,116,38)"
                        }
                    }
                },
                {
                    "name": "GNSS\u5b9a\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,115,83)"
                        }
                    }
                },
                {
                    "name": "\u4eff\u771f\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,122,88)"
                        }
                    }
                },
                {
                    "name": "\u5206\u7c7b\u4fe1\u606f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,129,140)"
                        }
                    }
                },
                {
                    "name": "\u533b\u5b66\u5f71\u50cf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,89,139)"
                        }
                    }
                },
                {
                    "name": "\u536b\u661f\u9065\u611f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,0,82)"
                        }
                    }
                },
                {
                    "name": "Ackerma",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,150,91)"
                        }
                    }
                },
                {
                    "name": "\u5168\u5458\u51fa\u56fd\u6e38",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,42,142)"
                        }
                    }
                },
                {
                    "name": "\u5956\u91d1\u591a\u591a\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,77,152)"
                        }
                    }
                },
                {
                    "name": "\u7cbe\u5bc6\u5355\u70b9\u5b9a\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,20,10)"
                        }
                    }
                },
                {
                    "name": "neon",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,154,140)"
                        }
                    }
                },
                {
                    "name": "kalman",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,156,76)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7ef4\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,146,24)"
                        }
                    }
                },
                {
                    "name": "TypeScript",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,157,55)"
                        }
                    }
                },
                {
                    "name": "LSTM",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,58,135)"
                        }
                    }
                },
                {
                    "name": "\u4e34\u5e8a\u79d1\u7814",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,19,4)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,132,86)"
                        }
                    }
                },
                {
                    "name": "HIve",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,124,151)"
                        }
                    }
                },
                {
                    "name": "\u4e2a\u6027\u5316\u63a8\u8350",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,139,97)"
                        }
                    }
                },
                {
                    "name": "KALDI",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,107,51)"
                        }
                    }
                },
                {
                    "name": "AILab",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,142,154)"
                        }
                    }
                },
                {
                    "name": "\u672c\u5730\u751f\u6d3b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,77,113)"
                        }
                    }
                },
                {
                    "name": "\u6570\u5b66\u5e93",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,2,55)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u641c\u7d22",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,19,76)"
                        }
                    }
                },
                {
                    "name": "\u6279\u53d1\uff5c\u96f6\u552e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,152,62)"
                        }
                    }
                },
                {
                    "name": "\u573a\u666f\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,23,50)"
                        }
                    }
                },
                {
                    "name": "\u591c\u62cd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,105,122)"
                        }
                    }
                },
                {
                    "name": "\u7269\u4f53\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,143,133)"
                        }
                    }
                },
                {
                    "name": "vr\u3002ar",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,159,10)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7cbe\u5ea6\u5730\u56fe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,118,71)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u7b56\u7565",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,9,159)"
                        }
                    }
                },
                {
                    "name": "Pulp",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,88,77)"
                        }
                    }
                },
                {
                    "name": "DSP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,117,129)"
                        }
                    }
                },
                {
                    "name": "kaldi",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,10,76)"
                        }
                    }
                },
                {
                    "name": "\u786c\u4ef6\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,93,4)"
                        }
                    }
                },
                {
                    "name": "RCNN",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,152,137)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,77,135)"
                        }
                    }
                },
                {
                    "name": "\u59ff\u6001\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,10,103)"
                        }
                    }
                },
                {
                    "name": "\u5b9e\u65f6\u8def\u51b5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,122,116)"
                        }
                    }
                },
                {
                    "name": "\u65f6\u95f4\u5e8f\u5217",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,11,106)"
                        }
                    }
                },
                {
                    "name": "\u77e9\u9635\u5206\u6790",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,134,61)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9slam",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,156,28)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7136\u8bed\u8a00",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,133,13)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u673a\u56fe\u5f62",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,39,138)"
                        }
                    }
                },
                {
                    "name": "\u89c4\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,63,91)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u538b\u7f29",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,66,117)"
                        }
                    }
                },
                {
                    "name": "\u539f\u578b\u8bbe\u8ba1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,129,90)"
                        }
                    }
                },
                {
                    "name": "\u5173\u7cfb\u6316\u6398",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,52,147)"
                        }
                    }
                },
                {
                    "name": "\u519c\u6797\u7267\u6e14",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,106,59)"
                        }
                    }
                },
                {
                    "name": "\u6392\u5e8f\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,86,101)"
                        }
                    }
                },
                {
                    "name": "NPU",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,11,0)"
                        }
                    }
                },
                {
                    "name": "\u8bad\u7ec3\u52a0\u901f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,152,30)"
                        }
                    }
                },
                {
                    "name": "\u78c1\u529b\u8ba1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,88,4)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u5238\u5546",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,105,41)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u5de5\u7a0b\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,75,17)"
                        }
                    }
                },
                {
                    "name": "3D\u6253\u5370",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,26,109)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u89c6\u9891\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,139,32)"
                        }
                    }
                },
                {
                    "name": "\u63a7\u5236\u5668\u8bbe\u8ba1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,90,26)"
                        }
                    }
                },
                {
                    "name": "\u5730\u7406\u8f68\u8ff9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,49,70)"
                        }
                    }
                },
                {
                    "name": "AI\u4ea7\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,81,67)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u5177\u793e\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,46,62)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u89c6\u9891\u7f16\u89e3\u7801",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,149,152)"
                        }
                    }
                },
                {
                    "name": "\u9a6c\u5c14\u514b\u592b\u968f\u673a\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,143,152)"
                        }
                    }
                },
                {
                    "name": "\u63a7\u5236\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,11,92)"
                        }
                    }
                },
                {
                    "name": "\u591a\u4f20\u611f\u5668",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,83,34)"
                        }
                    }
                },
                {
                    "name": "Go",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,21,40)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u611f\u77e5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,90,35)"
                        }
                    }
                },
                {
                    "name": "\u5f3a\u608d\u7684\u521b\u59cb\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,103,149)"
                        }
                    }
                },
                {
                    "name": "Database",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,14,49)"
                        }
                    }
                },
                {
                    "name": "CTR",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,22,12)"
                        }
                    }
                },
                {
                    "name": "\u5b9e\u4f53\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,140,41)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u7edc\u4f20\u8f93\u534f\u8bae",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,121,140)"
                        }
                    }
                },
                {
                    "name": "3DCAD",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,123,77)"
                        }
                    }
                },
                {
                    "name": "Linux\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,6,14)"
                        }
                    }
                },
                {
                    "name": "numpy",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,33,42)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5e02\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,26,79)"
                        }
                    }
                },
                {
                    "name": "VINS",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,54,130)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u52a8\u63a7\u5236\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,132,144)"
                        }
                    }
                },
                {
                    "name": "KF/EKF",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,64,118)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u7b56\u7565",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,66,21)"
                        }
                    }
                },
                {
                    "name": "3dmm",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,47,74)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5206\u7c7b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,60,84)"
                        }
                    }
                },
                {
                    "name": "Transformer",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,80,47)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u9a7e\u9a76",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,81,135)"
                        }
                    }
                },
                {
                    "name": "\u91cf\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,141,159)"
                        }
                    }
                },
                {
                    "name": "SOA",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,31,107)"
                        }
                    }
                },
                {
                    "name": "3D\u59ff\u6001\u91cd\u5efa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,48,75)"
                        }
                    }
                },
                {
                    "name": "flow",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,90,30)"
                        }
                    }
                },
                {
                    "name": "ADAS",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,20,21)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u6280\u5927\u725b\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,47,80)"
                        }
                    }
                },
                {
                    "name": "RCN",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,32,143)"
                        }
                    }
                },
                {
                    "name": "\u6216",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,22,13)"
                        }
                    }
                },
                {
                    "name": "\u8bba\u6587\u5199\u4f5c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,121,134)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u4eff\u771f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,15,29)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u6280\u672f\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,43,144)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5206\u6790",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,66,144)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u901f\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,10,45)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u5f15\u64ce",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,15,80)"
                        }
                    }
                },
                {
                    "name": "\u6df7\u54cd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,46,120)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,102,47)"
                        }
                    }
                },
                {
                    "name": "\u65f6\u5e8f\u6570\u636e\u5e93",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,35,83)"
                        }
                    }
                },
                {
                    "name": "\u5d4c\u5165\u5f0f\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,58,156)"
                        }
                    }
                },
                {
                    "name": "\u5e95\u5c42\u89c6\u89c9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,148,72)"
                        }
                    }
                },
                {
                    "name": "/",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,101,106)"
                        }
                    }
                },
                {
                    "name": "VTK",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,106,70)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u5b66\u4e60\u6a21\u578b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,125,123)"
                        }
                    }
                },
                {
                    "name": "android",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,49,6)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u5173\u952e\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,125,122)"
                        }
                    }
                },
                {
                    "name": "\u878d\u5408\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,37,28)"
                        }
                    }
                },
                {
                    "name": "FLINK",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,51,114)"
                        }
                    }
                },
                {
                    "name": "Gurobi",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,82,133)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51\u51fa\u884c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,154,152)"
                        }
                    }
                },
                {
                    "name": "\u5206\u5e03\u5f0f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,44,4)"
                        }
                    }
                },
                {
                    "name": "MCU",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,12,36)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u6295\u653e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,129,79)"
                        }
                    }
                },
                {
                    "name": "\u6570\u5b57\u56fe\u50cf\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,39,113)"
                        }
                    }
                },
                {
                    "name": "cuda",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,96,136)"
                        }
                    }
                },
                {
                    "name": "\u5149\u5b66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,89,81)"
                        }
                    }
                },
                {
                    "name": "PP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,130,57)"
                        }
                    }
                },
                {
                    "name": "\u89c4\u5219\u5f15\u64ce",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,55,13)"
                        }
                    }
                },
                {
                    "name": "\u5f02\u5e38\u8bca\u65ad",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,93,78)"
                        }
                    }
                },
                {
                    "name": "asr",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,95,134)"
                        }
                    }
                },
                {
                    "name": "\u540d\u6821\u540d\u4f01\u80cc\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,17,69)"
                        }
                    }
                },
                {
                    "name": "\u751f\u4ea7\u8c03\u5ea6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,11,13)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u591a\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,74,79)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u4e1a\u670d\u52a1\uff5c\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,134,87)"
                        }
                    }
                },
                {
                    "name": "\u964d\u566a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,65,41)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u8f6c\u6362",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,55,68)"
                        }
                    }
                },
                {
                    "name": "\u8c03\u62e8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,96,82)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u63a8\u8350",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,8,148)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u5b9a\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,97,114)"
                        }
                    }
                },
                {
                    "name": "3DGIS",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,39,53)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6e05\u6d17",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,145,105)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4ea4\u4ea7\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,44,88)"
                        }
                    }
                },
                {
                    "name": "3D\u5f15\u64ce",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,96,44)"
                        }
                    }
                },
                {
                    "name": "JitterBuffer",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,52,154)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u5b89\u5168",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,36,62)"
                        }
                    }
                },
                {
                    "name": "\u5bfc\u822a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,80,119)"
                        }
                    }
                },
                {
                    "name": "\u5bc6\u7801\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,44,143)"
                        }
                    }
                },
                {
                    "name": "DSP\u7f16\u7a0b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,77,28)"
                        }
                    }
                },
                {
                    "name": "TF",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,160,86)"
                        }
                    }
                },
                {
                    "name": "\u5bfc\u822a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,69,54)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u8c03\u7814",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,25,37)"
                        }
                    }
                },
                {
                    "name": "\u542f\u53d1\u5f0f\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,149,30)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u98ce\u63a7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,54,56)"
                        }
                    }
                },
                {
                    "name": "CRF",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,159,1)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u98df\u4e0b\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,123,152)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u6392\u7a0b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,79,50)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u6587\u5206\u6790",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,157,65)"
                        }
                    }
                },
                {
                    "name": "\u4f11\u95f2\uff5c\u5a31\u4e50",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,118,142)"
                        }
                    }
                },
                {
                    "name": "\u4eff\u771f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,98,73)"
                        }
                    }
                },
                {
                    "name": "\u8def\u51b5\u8ba1\u7b97",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,155,103)"
                        }
                    }
                },
                {
                    "name": "\u8def\u5f84\u4f18\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,135,17)"
                        }
                    }
                },
                {
                    "name": "HADOOP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,37,64)"
                        }
                    }
                },
                {
                    "name": "GO",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,43,27)"
                        }
                    }
                },
                {
                    "name": "sfm",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,12,136)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7136\u8bed\u8a00\u5904",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,73,120)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u8f6f\u4ef6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,3,92)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u57fa\u7840",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,13,115)"
                        }
                    }
                },
                {
                    "name": "\u9065\u611f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,30,31)"
                        }
                    }
                },
                {
                    "name": "\u878d\u5408IMU",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,121,108)"
                        }
                    }
                },
                {
                    "name": "Rust",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,10,114)"
                        }
                    }
                },
                {
                    "name": "\u5206\u5e03\u5f0f\u8bad\u7ec3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,61,148)"
                        }
                    }
                },
                {
                    "name": "\u67b6\u6784\u5e08",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,116,0)"
                        }
                    }
                },
                {
                    "name": "\u542f\u53d1\u5f0f\u89c4\u5219\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,147,45)"
                        }
                    }
                },
                {
                    "name": "SVC",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,67,156)"
                        }
                    }
                },
                {
                    "name": "ppp-rtk",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,148,111)"
                        }
                    }
                },
                {
                    "name": "\u53ec\u56de",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,107,101)"
                        }
                    }
                },
                {
                    "name": "c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,158,55)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u68c0\u6d4b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,157,140)"
                        }
                    }
                },
                {
                    "name": "ERP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,19,44)"
                        }
                    }
                },
                {
                    "name": "Caffe\u3001Pytorch\u3001",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,146,8)"
                        }
                    }
                },
                {
                    "name": "3D\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,65,35)"
                        }
                    }
                },
                {
                    "name": "\u73af\u5883\u611f\u77e5\u4e0e\u878d\u5408",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,99,134)"
                        }
                    }
                },
                {
                    "name": "\u6d4b\u8bd5\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,154,77)"
                        }
                    }
                },
                {
                    "name": "MatLab",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,23,90)"
                        }
                    }
                },
                {
                    "name": "ORBSLAM",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,123,55)"
                        }
                    }
                },
                {
                    "name": "\u9690\u79d8\u8ba1\u7b97\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,78,90)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b\u79fb\u690d\u4f18\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,50,52)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u4f18\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,51,81)"
                        }
                    }
                },
                {
                    "name": "\u901f\u5ea6\u63a7\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,0,48)"
                        }
                    }
                },
                {
                    "name": "\u57fa\u7840\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,31,85)"
                        }
                    }
                },
                {
                    "name": "\u5730\u56fe\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,70,145)"
                        }
                    }
                },
                {
                    "name": "libvpx",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,73,12)"
                        }
                    }
                },
                {
                    "name": "\u6574\u6570\u89c4\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,103,118)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,1,129)"
                        }
                    }
                },
                {
                    "name": "LTE",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,2,142)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u62df\u9000\u706b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,45,116)"
                        }
                    }
                },
                {
                    "name": "PID",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,113,40)"
                        }
                    }
                },
                {
                    "name": "\u6392\u7a0b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,50,42)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u8baf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,144,120)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544aCTR/CVR",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,117,124)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,95,128)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u5316\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,129,90)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u843d\u5730",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,39,34)"
                        }
                    }
                },
                {
                    "name": "H.264/265",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,135,86)"
                        }
                    }
                },
                {
                    "name": "\u611f\u77e5\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,122,107)"
                        }
                    }
                },
                {
                    "name": "\u7ecf\u5178\u63a7\u5236\u7406\u8bba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,21,7)"
                        }
                    }
                },
                {
                    "name": "ECC",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,51,73)"
                        }
                    }
                },
                {
                    "name": "GPS",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,55,26)"
                        }
                    }
                },
                {
                    "name": "CPLEX",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,70,108)"
                        }
                    }
                },
                {
                    "name": "\u52a8\u4f5c\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,7,122)"
                        }
                    }
                },
                {
                    "name": "VR",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,29,125)"
                        }
                    }
                },
                {
                    "name": "Windows",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,102,16)"
                        }
                    }
                },
                {
                    "name": "X264",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,28,79)"
                        }
                    }
                },
                {
                    "name": "PHM",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,159,134)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u98ce\u63a7AI",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,149,47)"
                        }
                    }
                },
                {
                    "name": "\u4f20\u611f\u5668\u6216\u70b9\u4e91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,19,122)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7f16\u8f91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,34,107)"
                        }
                    }
                },
                {
                    "name": "h264",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,26,16)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,109,8)"
                        }
                    }
                },
                {
                    "name": "pandas",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,19,116)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a9\u4e09\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,103,34)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u9886\u57df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,137,89)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u957f\u5e26\u85aa\u5047\u671f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,143,98)"
                        }
                    }
                },
                {
                    "name": "\u516c\u94a5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,134,92)"
                        }
                    }
                },
                {
                    "name": "\u80a2\u4f53\u68c0\u6d4b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,32,101)"
                        }
                    }
                },
                {
                    "name": "AGV",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,99,94)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,87,138)"
                        }
                    }
                },
                {
                    "name": "PID\u63a7\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,3,77)"
                        }
                    }
                },
                {
                    "name": "\u4f4f\u798f\u8ba1\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,17,58)"
                        }
                    }
                },
                {
                    "name": "AEB",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,66,65)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u9884\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,54,74)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u63a8\u8350",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,153,71)"
                        }
                    }
                },
                {
                    "name": "CCF",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,122,58)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,157,67)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u51e0\u4f55",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,83,147)"
                        }
                    }
                },
                {
                    "name": "\u865a\u5047\u6d41\u91cf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,50,115)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u7406\u89e3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,158,157)"
                        }
                    }
                },
                {
                    "name": "\u9886\u519b\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,113,21)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u5bbd\u63a7\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,87,143)"
                        }
                    }
                },
                {
                    "name": "NLP\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,45,92)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u5bfc\u822a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,60,90)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u5904\u7406\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,32,106)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u91cd\u6784",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,15,157)"
                        }
                    }
                },
                {
                    "name": "\u51e0\u4f55\u5b66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,132,113)"
                        }
                    }
                },
                {
                    "name": "BIM+3D",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,105,47)"
                        }
                    }
                },
                {
                    "name": "HBase",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,76,124)"
                        }
                    }
                },
                {
                    "name": "\u751f\u7406\u53c2\u6570",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,65,132)"
                        }
                    }
                },
                {
                    "name": "AIOPS",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,122,59)"
                        }
                    }
                },
                {
                    "name": "\u8def\u51b5\u4f18\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,82,69)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,74,85)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u4e49\u5206\u5272",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,105,65)"
                        }
                    }
                },
                {
                    "name": "\u7f16\u7a0b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,80,55)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u7cca\u63a7\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,66,153)"
                        }
                    }
                },
                {
                    "name": "NPL",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,42,17)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u4e3b\u664b\u5347\u8ba1\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,53,130)"
                        }
                    }
                },
                {
                    "name": "\u4e0b\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,149,75)"
                        }
                    }
                },
                {
                    "name": "\u6709\u524d\u9014",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,134,25)"
                        }
                    }
                },
                {
                    "name": "\u58f0\u7eb9\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,153,69)"
                        }
                    }
                },
                {
                    "name": "rtk\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,64,26)"
                        }
                    }
                },
                {
                    "name": "\u8282\u65e5\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,91,65)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u91c7\u96c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,47,89)"
                        }
                    }
                },
                {
                    "name": "\u52a8\u529b\u5b66\u5efa\u6a21",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,150,150)"
                        }
                    }
                },
                {
                    "name": "\u5168\u94fe\u8defSaaS\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,22,140)"
                        }
                    }
                },
                {
                    "name": "\u5bfc\u822a\u89c4\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,141,152)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u56fe\u5f62",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,108,85)"
                        }
                    }
                },
                {
                    "name": "AI\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,144,75)"
                        }
                    }
                },
                {
                    "name": "\u5bfc\u822a\u5b9a\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,156,25)"
                        }
                    }
                },
                {
                    "name": "\u4f20\u611f\u5668\u878d\u5408",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,1,65)"
                        }
                    }
                },
                {
                    "name": "AR",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,38,113)"
                        }
                    }
                },
                {
                    "name": "\u6ee4\u955c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,30,102)"
                        }
                    }
                },
                {
                    "name": "\u51e0\u4f55\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,43,47)"
                        }
                    }
                },
                {
                    "name": "DeepFM",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,158,2)"
                        }
                    }
                },
                {
                    "name": "ETL",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,110,111)"
                        }
                    }
                },
                {
                    "name": "ACC/AEB/LKA",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,11,85)"
                        }
                    }
                },
                {
                    "name": "C++/python",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,112,154)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5065\u5eb7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,81,59)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u589e\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,95,4)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u76ee\u89c6\u89c9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,101,139)"
                        }
                    }
                },
                {
                    "name": "ISP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,68,132)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9SLAM",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,69,4)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,129,7)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u6a21\u578b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,22,159)"
                        }
                    }
                },
                {
                    "name": "\u76ee\u6807\u5206\u5272",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,28,52)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5a92\u4f53",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,14,29)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u7814",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,71,39)"
                        }
                    }
                },
                {
                    "name": "\u591a\u4f20\u611f\u5668\u878d\u5408",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,57,7)"
                        }
                    }
                },
                {
                    "name": "DNN",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,121,122)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u5b66\u4e60\u7b97\u6cd5\u673a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,138,88)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62\u5b66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,90,92)"
                        }
                    }
                },
                {
                    "name": "\u8fd1\u7ea2\u5916",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,150,114)"
                        }
                    }
                },
                {
                    "name": "\u53bb\u6df7\u54cd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,101,18)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u4e49\u5206\u6790",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,122,39)"
                        }
                    }
                },
                {
                    "name": "\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,143,88)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u91cd\u5efa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,101,107)"
                        }
                    }
                },
                {
                    "name": "\u6295\u8d44/\u878d\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,53,80)"
                        }
                    }
                },
                {
                    "name": "pil",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,150,133)"
                        }
                    }
                },
                {
                    "name": "NLP/CV",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,90,94)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u63a8\u8350",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,85,9)"
                        }
                    }
                },
                {
                    "name": "\u9aa8\u79d1\u673a\u5668\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,139,9)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u4f533D\u91cd\u5efa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,147,40)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u76d1\u7763\u5b66\u4e60",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,132,57)"
                        }
                    }
                },
                {
                    "name": "\u907f\u969c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,17,39)"
                        }
                    }
                },
                {
                    "name": "\u4e50\u7406\u8f6c\u6362",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,61,31)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546\u641c\u7d22",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,61,90)"
                        }
                    }
                },
                {
                    "name": "\u52a8\u4f5c\u6355\u6349",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,16,133)"
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
                "\u673a\u5668\u5b66\u4e60",
                "C/C++"
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
        chart_6ee0591be146426ba0d200687a0c520a.setOption(option_6ee0591be146426ba0d200687a0c520a);
    </script>
                <div id="e6467948103948899914325ca2f0b8ed" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_e6467948103948899914325ca2f0b8ed = echarts.init(
            document.getElementById('e6467948103948899914325ca2f0b8ed'), 'white', {renderer: 'canvas'});
        var option_e6467948103948899914325ca2f0b8ed = {
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
                    "value": 451,
                    "name": "\u6df1\u5ea6\u5b66\u4e60"
                },
                {
                    "value": 286,
                    "name": "\u4eba\u5de5\u667a\u80fd\u670d\u52a1"
                },
                {
                    "value": 184,
                    "name": "Python"
                },
                {
                    "value": 144,
                    "name": "\u6570\u636e\u6316\u6398"
                },
                {
                    "value": 124,
                    "name": "\u56fe\u50cf\u7b97\u6cd5"
                },
                {
                    "value": 119,
                    "name": "\u673a\u5668\u5b66\u4e60"
                },
                {
                    "value": 110,
                    "name": "C/C++"
                },
                {
                    "value": 103,
                    "name": "\u56fe\u7247\u8bc6\u522b"
                },
                {
                    "value": 92,
                    "name": "\u63a8\u8350\u7b97\u6cd5"
                },
                {
                    "value": 84,
                    "name": "\u4eba\u8138\u8bc6\u522b"
                },
                {
                    "value": 70,
                    "name": "\u7535\u5546\u5e73\u53f0"
                },
                {
                    "value": 69,
                    "name": "\u81ea\u7136\u8bed\u8a00\u5904\u7406"
                },
                {
                    "value": 64,
                    "name": "\u4eba\u5de5\u667a\u80fd"
                },
                {
                    "value": 60,
                    "name": "\u7ee9\u6548\u5956\u91d1"
                },
                {
                    "value": 59,
                    "name": "\u667a\u80fd\u786c\u4ef6"
                },
                {
                    "value": 59,
                    "name": "\u8f6f\u4ef6\u670d\u52a1\uff5c\u54a8\u8be2"
                },
                {
                    "value": 56,
                    "name": "\u6570\u636e\u670d\u52a1\uff5c\u54a8\u8be2"
                },
                {
                    "value": 55,
                    "name": "\u5927\u6570\u636e"
                },
                {
                    "value": 54,
                    "name": "Java"
                },
                {
                    "value": 50,
                    "name": "\u6280\u80fd\u57f9\u8bad"
                },
                {
                    "value": 50,
                    "name": "C++"
                },
                {
                    "value": 45,
                    "name": "\u5e26\u85aa\u5e74\u5047"
                },
                {
                    "value": 44,
                    "name": "\u6a21\u5f0f\u8bc6\u522b"
                },
                {
                    "value": 42,
                    "name": "\u641c\u7d22\u7b97\u6cd5"
                },
                {
                    "value": 40,
                    "name": "\u8bed\u97f3\u8bc6\u522b"
                },
                {
                    "value": 38,
                    "name": "\u79fb\u52a8\u4e92\u8054\u7f51"
                },
                {
                    "value": 37,
                    "name": "\u56fe\u50cf\u5904\u7406"
                },
                {
                    "value": 36,
                    "name": "\u5c97\u4f4d\u664b\u5347"
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
                    "value": 32,
                    "name": "\u4e09\u7ef4\u56fe\u50cf\u89c6\u89c9"
                },
                {
                    "value": 31,
                    "name": "\u6241\u5e73\u7ba1\u7406"
                },
                {
                    "value": 31,
                    "name": "\u8ba1\u7b97\u673a\u89c6\u89c9"
                },
                {
                    "value": 31,
                    "name": "\u79d1\u6280\u91d1\u878d"
                },
                {
                    "value": 30,
                    "name": "\u533b\u7597\u5065\u5eb7"
                },
                {
                    "value": 30,
                    "name": "\u9886\u5bfc\u597d"
                },
                {
                    "value": 30,
                    "name": "OpenCV"
                },
                {
                    "value": 29,
                    "name": "\u63a8\u8350\u7cfb\u7edf"
                },
                {
                    "value": 29,
                    "name": "TensoFlow"
                },
                {
                    "value": 29,
                    "name": "\u6587\u672c\u5206\u7c7b"
                },
                {
                    "value": 28,
                    "name": "NLP"
                },
                {
                    "value": 28,
                    "name": "\u6587\u5b57\u8bc6\u522b"
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
                    "value": 26,
                    "name": "PyTorch"
                },
                {
                    "value": 25,
                    "name": "IT\u6280\u672f\u670d\u52a1\uff5c\u54a8\u8be2"
                },
                {
                    "value": 25,
                    "name": "\u81ea\u52a8\u9a7e\u9a76"
                },
                {
                    "value": 24,
                    "name": "\u65b0\u96f6\u552e"
                },
                {
                    "value": 24,
                    "name": "\u80a1\u7968\u671f\u6743"
                },
                {
                    "value": 24,
                    "name": "\u8282\u65e5\u793c\u7269"
                },
                {
                    "value": 24,
                    "name": "nan"
                },
                {
                    "value": 23,
                    "name": "\u540e\u7aef\u5f00\u53d1"
                },
                {
                    "value": 22,
                    "name": "\u5de5\u5177\u7c7b\u4ea7\u54c1"
                },
                {
                    "value": 22,
                    "name": "\u793e\u4ea4\u5e73\u53f0"
                },
                {
                    "value": 21,
                    "name": "\u91d1\u878d"
                },
                {
                    "value": 21,
                    "name": "\u5e74\u5e95\u53cc\u85aa"
                },
                {
                    "value": 19,
                    "name": "\u5728\u7ebf\u6559\u80b2"
                },
                {
                    "value": 19,
                    "name": "\u6e38\u620f"
                },
                {
                    "value": 19,
                    "name": "\u5b9a\u671f\u4f53\u68c0"
                },
                {
                    "value": 19,
                    "name": "\u97f3\u9891\uff5c\u89c6\u9891\u5a92\u4f53"
                },
                {
                    "value": 18,
                    "name": "\u610f\u56fe\u8bc6\u522b"
                },
                {
                    "value": 18,
                    "name": "\u641c\u7d22"
                },
                {
                    "value": 17,
                    "name": "\u8bed\u97f3\u5408\u6210"
                },
                {
                    "value": 17,
                    "name": "\u6570\u636e\u670d\u52a1"
                },
                {
                    "value": 16,
                    "name": "\u5de5\u4e1a\u89c6\u89c9\u68c0\u6d4b"
                },
                {
                    "value": 16,
                    "name": "\u516d\u9669\u4e00\u91d1"
                },
                {
                    "value": 16,
                    "name": "\u7535\u5546"
                },
                {
                    "value": 15,
                    "name": "\u6587\u672c\u751f\u6210"
                },
                {
                    "value": 15,
                    "name": "\u514d\u8d39\u73ed\u8f66"
                },
                {
                    "value": 15,
                    "name": "\u5c31\u8fd1\u79df\u623f\u8865\u8d34"
                },
                {
                    "value": 15,
                    "name": "Hadoop"
                },
                {
                    "value": 14,
                    "name": "\u6559\u80b2"
                },
                {
                    "value": 14,
                    "name": "MATLAB"
                },
                {
                    "value": 13,
                    "name": "\u5e7f\u544a\u670d\u52a1"
                },
                {
                    "value": 12,
                    "name": "\u4e13\u9879\u5956\u91d1"
                },
                {
                    "value": 12,
                    "name": "\u97f3\u9891\u7b97\u6cd5"
                },
                {
                    "value": 12,
                    "name": "\u4e91\u8ba1\u7b97"
                },
                {
                    "value": 12,
                    "name": "\u6d88\u8d39\u751f\u6d3b"
                },
                {
                    "value": 12,
                    "name": "\u533b\u7597\u5f71\u50cf\u8bca\u65ad"
                },
                {
                    "value": 12,
                    "name": "C"
                },
                {
                    "value": 12,
                    "name": "CNN"
                },
                {
                    "value": 12,
                    "name": "\u5e7f\u544a\u7b97\u6cd5"
                },
                {
                    "value": 12,
                    "name": "\u8f85\u52a9/\u667a\u80fd\u9a7e\u9a76"
                },
                {
                    "value": 12,
                    "name": "\u5728\u7ebf\u533b\u7597"
                },
                {
                    "value": 11,
                    "name": "\u6570\u636e\u5206\u6790"
                },
                {
                    "value": 11,
                    "name": "\u670d\u52a1\u673a\u5668\u4eba"
                },
                {
                    "value": 11,
                    "name": "\u5efa\u6a21"
                },
                {
                    "value": 11,
                    "name": "\u6570\u4ed3\u5efa\u6a21"
                },
                {
                    "value": 11,
                    "name": "XGBoost"
                },
                {
                    "value": 11,
                    "name": "\u4f01\u4e1a\u670d\u52a1"
                },
                {
                    "value": 10,
                    "name": "\u65c5\u6e38\uff5c\u51fa\u884c"
                },
                {
                    "value": 10,
                    "name": "\u97f3\u4e50"
                },
                {
                    "value": 10,
                    "name": "AI"
                },
                {
                    "value": 10,
                    "name": "\u7269\u6d41\uff5c\u8fd0\u8f93"
                },
                {
                    "value": 10,
                    "name": "\u89c6\u9891/\u76d1\u63a7\u5206\u6790"
                },
                {
                    "value": 10,
                    "name": "\u8425\u9500\u670d\u52a1\uff5c\u54a8\u8be2"
                },
                {
                    "value": 10,
                    "name": "\u5185\u5bb9\u8d44\u8baf"
                },
                {
                    "value": 10,
                    "name": "\u7f51\u7edc\u901a\u4fe1"
                },
                {
                    "value": 10,
                    "name": "\u7ba1\u7406\u89c4\u8303"
                },
                {
                    "value": 10,
                    "name": "SLAM"
                },
                {
                    "value": 10,
                    "name": "\u533b\u7597\uff5c\u4fdd\u5065\uff5c\u7f8e\u5bb9"
                },
                {
                    "value": 9,
                    "name": "\u63a8\u8350"
                },
                {
                    "value": 9,
                    "name": "\u5185\u5bb9\u793e\u533a"
                },
                {
                    "value": 9,
                    "name": "\u4fe1\u606f\u5b89\u5168"
                },
                {
                    "value": 9,
                    "name": "\u793e\u4ea4"
                },
                {
                    "value": 9,
                    "name": "\u5e7f\u544a\u8425\u9500"
                },
                {
                    "value": 9,
                    "name": "\u95ee\u7b54\u7cfb\u7edf"
                },
                {
                    "value": 8,
                    "name": "\u77ed\u89c6\u9891"
                },
                {
                    "value": 8,
                    "name": "Spark"
                },
                {
                    "value": 8,
                    "name": "\u65b0\u80fd\u6e90\u6c7d\u8f66\u5236\u9020"
                },
                {
                    "value": 7,
                    "name": "\u8def\u5f84\u89c4\u5212"
                },
                {
                    "value": 7,
                    "name": "TensorFlow"
                },
                {
                    "value": 7,
                    "name": "RNN"
                },
                {
                    "value": 7,
                    "name": "Caffe"
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
                    "value": 7,
                    "name": "Shell"
                },
                {
                    "value": 7,
                    "name": "\u4ea4\u901a\u8865\u52a9"
                },
                {
                    "value": 7,
                    "name": "\u7f8e\u5973\u591a"
                },
                {
                    "value": 7,
                    "name": "\u4fe1\u606f\u62bd\u53d6"
                },
                {
                    "value": 7,
                    "name": "Scala"
                },
                {
                    "value": 7,
                    "name": "\u4e92\u8054\u7f51\u91d1\u878d"
                },
                {
                    "value": 7,
                    "name": "\u77e5\u8bc6\u56fe\u8c31"
                },
                {
                    "value": 7,
                    "name": "\u673a\u5668\u4eba"
                },
                {
                    "value": 7,
                    "name": "\u6ef4\u6ef4"
                },
                {
                    "value": 6,
                    "name": "python"
                },
                {
                    "value": 6,
                    "name": "\u671f\u6743\u4e30\u539a"
                },
                {
                    "value": 6,
                    "name": "\u5927\u725b\u56e2\u961f"
                },
                {
                    "value": 6,
                    "name": "\u7269\u6d41"
                },
                {
                    "value": 6,
                    "name": "\u8bed\u97f3\u7b97\u6cd5"
                },
                {
                    "value": 6,
                    "name": "\u529e\u516c\u903c\u683c\u9ad8"
                },
                {
                    "value": 6,
                    "name": "\u5de5\u5177\u8f6f\u4ef6"
                },
                {
                    "value": 6,
                    "name": "\u53e5\u6cd5\u5206\u6790"
                },
                {
                    "value": 6,
                    "name": "Keras"
                },
                {
                    "value": 6,
                    "name": "\u7b97\u6cd5\u5de5\u7a0b\u5e08"
                },
                {
                    "value": 6,
                    "name": "\u5782\u76f4\u641c\u7d22"
                },
                {
                    "value": 6,
                    "name": "MCN\uff5c\u76f4\u64ad\u5e73\u53f0"
                },
                {
                    "value": 6,
                    "name": "Linux"
                },
                {
                    "value": 5,
                    "name": "\u94f6\u884c"
                },
                {
                    "value": 5,
                    "name": "ARM"
                },
                {
                    "value": 5,
                    "name": "linux"
                },
                {
                    "value": 5,
                    "name": "\u793e\u4ea4\u5a92\u4f53"
                },
                {
                    "value": 5,
                    "name": "\u901a\u8baf\u6d25\u8d34"
                },
                {
                    "value": 5,
                    "name": "nlp"
                },
                {
                    "value": 5,
                    "name": "GAN"
                },
                {
                    "value": 5,
                    "name": "\u533a\u5757\u94fe"
                },
                {
                    "value": 5,
                    "name": "Hive"
                },
                {
                    "value": 5,
                    "name": "\u667a\u80fd\u91d1\u878d"
                },
                {
                    "value": 5,
                    "name": "spark"
                },
                {
                    "value": 5,
                    "name": "\u8bcd\u6027\u6807\u6ce8"
                },
                {
                    "value": 5,
                    "name": "\u6559\u80b2\uff5c\u57f9\u8bad"
                },
                {
                    "value": 5,
                    "name": "\u6570\u636e\u7ed3\u6784"
                },
                {
                    "value": 4,
                    "name": "\u56fe\u5f62"
                },
                {
                    "value": 4,
                    "name": "\u5e74\u5ea6\u65c5\u6e38"
                },
                {
                    "value": 4,
                    "name": "tensorflow"
                },
                {
                    "value": 4,
                    "name": "RTK"
                },
                {
                    "value": 4,
                    "name": "CV"
                },
                {
                    "value": 4,
                    "name": "\u6c7d\u8f66"
                },
                {
                    "value": 4,
                    "name": "MySQL"
                },
                {
                    "value": 4,
                    "name": "\u7528\u6237\u753b\u50cf"
                },
                {
                    "value": 4,
                    "name": "c++"
                },
                {
                    "value": 4,
                    "name": "Golang"
                },
                {
                    "value": 4,
                    "name": "\u91d1\u878d\u4e1a"
                },
                {
                    "value": 4,
                    "name": "\u5c45\u4f4f\u670d\u52a1"
                },
                {
                    "value": 4,
                    "name": "opencv"
                },
                {
                    "value": 4,
                    "name": "Tensorflow"
                },
                {
                    "value": 4,
                    "name": "\u8bed\u97f3\u5904\u7406"
                },
                {
                    "value": 4,
                    "name": "CTR\u9884\u4f30"
                },
                {
                    "value": 4,
                    "name": "ROS"
                },
                {
                    "value": 4,
                    "name": "\u89c6\u89c9\u7b97\u6cd5"
                },
                {
                    "value": 4,
                    "name": "\u4e92\u8054\u7f51"
                },
                {
                    "value": 4,
                    "name": "HALCON"
                },
                {
                    "value": 4,
                    "name": "\u6587\u5316\u4f20\u5a92"
                },
                {
                    "value": 4,
                    "name": "kaggle"
                },
                {
                    "value": 4,
                    "name": "SQL"
                },
                {
                    "value": 4,
                    "name": "nlp\u7b97\u6cd5\u5de5\u7a0b\u5e08"
                },
                {
                    "value": 4,
                    "name": "\u7cbe\u82f1\u56e2\u961f"
                },
                {
                    "value": 4,
                    "name": "\u751f\u6d3b\u670d\u52a1"
                },
                {
                    "value": 4,
                    "name": "\u673a\u5668\u89c6\u89c9"
                },
                {
                    "value": 3,
                    "name": "\u4f20\u611f\u5668"
                },
                {
                    "value": 3,
                    "name": "OCR"
                },
                {
                    "value": 3,
                    "name": "\u8fea\u58eb\u5c3c"
                },
                {
                    "value": 3,
                    "name": "\u4fe1\u606f\u68c0\u7d22"
                },
                {
                    "value": 3,
                    "name": "\u5de5\u4e1a\u4e92\u8054\u7f51"
                },
                {
                    "value": 3,
                    "name": "GBDT"
                },
                {
                    "value": 3,
                    "name": "\u5546\u4e1a\u822a\u5929"
                },
                {
                    "value": 3,
                    "name": "\u5730\u56fe"
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
                    "name": "\u56fe\u50cf\u8bc6\u522b"
                },
                {
                    "value": 3,
                    "name": "\u540e\u7aef"
                },
                {
                    "value": 3,
                    "name": "\u97f3\u89c6\u9891"
                },
                {
                    "value": 3,
                    "name": "ROS\u7cfb\u7edf"
                },
                {
                    "value": 3,
                    "name": "\u795e\u7ecf\u7f51\u7edc"
                },
                {
                    "value": 3,
                    "name": "\u89c6\u9891\u641c\u7d22"
                },
                {
                    "value": 3,
                    "name": "ETA"
                },
                {
                    "value": 3,
                    "name": "\u6559\u80b2\u8f85\u5bfc"
                },
                {
                    "value": 3,
                    "name": "\u6587\u672c\u8574\u6db5"
                },
                {
                    "value": 3,
                    "name": "opengl"
                },
                {
                    "value": 3,
                    "name": "\u6570\u636e\u5e93"
                },
                {
                    "value": 3,
                    "name": "\u70b9\u4e91"
                },
                {
                    "value": 3,
                    "name": "\u7b97\u6cd5\u8bbe\u8ba1"
                },
                {
                    "value": 3,
                    "name": "\u6d41\u5a92\u4f53"
                },
                {
                    "value": 3,
                    "name": "Pytorch"
                },
                {
                    "value": 3,
                    "name": "\u533b\u7597\u5668\u68b0"
                },
                {
                    "value": 3,
                    "name": "\u4f18\u5316\u7b97\u6cd5"
                },
                {
                    "value": 3,
                    "name": "\u8f6f\u4ef6\u5f00\u53d1"
                },
                {
                    "value": 3,
                    "name": "\u667a\u80fd\u5bb6\u5c45"
                },
                {
                    "value": 3,
                    "name": "\u4e30\u539a\u5e74\u7ec8"
                },
                {
                    "value": 3,
                    "name": "matlab"
                },
                {
                    "value": 3,
                    "name": "\u8fd0\u7b79\u5b66"
                },
                {
                    "value": 3,
                    "name": "\u5d4c\u5165\u5f0f"
                },
                {
                    "value": 3,
                    "name": "\u673a\u5668\u7ffb\u8bd1"
                },
                {
                    "value": 3,
                    "name": "\u5e74\u7ec8\u5206\u7ea2"
                },
                {
                    "value": 3,
                    "name": "\u672c\u5206"
                },
                {
                    "value": 3,
                    "name": "\u5e05\u54e5\u591a"
                },
                {
                    "value": 3,
                    "name": "\u5f3a\u5316\u5b66\u4e60"
                },
                {
                    "value": 3,
                    "name": "slam"
                },
                {
                    "value": 2,
                    "name": "ElasticSearch"
                },
                {
                    "value": 2,
                    "name": "\u8111\u673a"
                },
                {
                    "value": 2,
                    "name": "OpenCL"
                },
                {
                    "value": 2,
                    "name": "\u901a\u4fe1/\u7f51\u7edc\u8bbe\u5907"
                },
                {
                    "value": 2,
                    "name": "\u89c6\u9891"
                },
                {
                    "value": 2,
                    "name": "\u793e\u4ea4\u5a92\u4f53\u5e73\u53f0"
                },
                {
                    "value": 2,
                    "name": "\u534f\u540c\u8fc7\u6ee4"
                },
                {
                    "value": 2,
                    "name": "\u5de5\u4e1a\u81ea\u52a8\u5316"
                },
                {
                    "value": 2,
                    "name": "\u805a\u7c7b"
                },
                {
                    "value": 2,
                    "name": "\u4eba\u8138\u751f\u6210"
                },
                {
                    "value": 2,
                    "name": "\u5206\u5e03\u5f0f\u641c\u7d22"
                },
                {
                    "value": 2,
                    "name": "\u6392\u5e8f"
                },
                {
                    "value": 2,
                    "name": "ACM"
                },
                {
                    "value": 2,
                    "name": "PaddlePddle"
                },
                {
                    "value": 2,
                    "name": "\u5de5\u4e1a\u68c0\u6d4b"
                },
                {
                    "value": 2,
                    "name": "\u4f9b\u5e94\u94fe\u7b97\u6cd5"
                },
                {
                    "value": 2,
                    "name": "\u89c6\u89c9"
                },
                {
                    "value": 2,
                    "name": "\u98ce\u63a7\u7b97\u6cd5"
                },
                {
                    "value": 2,
                    "name": "\u5348\u9910\u8865\u52a9"
                },
                {
                    "value": 2,
                    "name": "\u8fd0\u52a8\u65e5"
                },
                {
                    "value": 2,
                    "name": "\u7cfb\u7edf\u67b6\u6784"
                },
                {
                    "value": 2,
                    "name": "\u6570\u636e\u4ed3\u5e93"
                },
                {
                    "value": 2,
                    "name": "\u56fe\u50cf\u5206\u5272"
                },
                {
                    "value": 2,
                    "name": "\u7535\u673a\u63a7\u5236"
                },
                {
                    "value": 2,
                    "name": "CAD"
                },
                {
                    "value": 2,
                    "name": "\u89c6\u9891\u7406\u89e3"
                },
                {
                    "value": 2,
                    "name": "\u4ea7\u54c1\u8bbe\u8ba1"
                },
                {
                    "value": 2,
                    "name": "\u7ade\u54c1\u5206\u6790"
                },
                {
                    "value": 2,
                    "name": "\u5b9a\u4f4d\u7b97\u6cd5"
                },
                {
                    "value": 2,
                    "name": "\u7248\u9762\u5206\u6790"
                },
                {
                    "value": 2,
                    "name": "SNN"
                },
                {
                    "value": 2,
                    "name": "\u8f66\u8054\u7f51"
                },
                {
                    "value": 2,
                    "name": "\u89c6\u9891\u7b97\u6cd5"
                },
                {
                    "value": 2,
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5"
                },
                {
                    "value": 2,
                    "name": "\u5236\u9020\u4e1a"
                },
                {
                    "value": 2,
                    "name": "PPP"
                },
                {
                    "value": 2,
                    "name": "\u53cc\u76ee"
                },
                {
                    "value": 2,
                    "name": "\u533b\u7597"
                },
                {
                    "value": 2,
                    "name": "\u6280\u672f\u7ba1\u7406"
                },
                {
                    "value": 2,
                    "name": "\u7acb\u4f53\u5339\u914d"
                },
                {
                    "value": 2,
                    "name": "\u8fd0\u52a8\u63a7\u5236"
                },
                {
                    "value": 2,
                    "name": "3D"
                },
                {
                    "value": 2,
                    "name": "JAVA"
                },
                {
                    "value": 2,
                    "name": "Matlab"
                },
                {
                    "value": 2,
                    "name": "C#"
                },
                {
                    "value": 2,
                    "name": "\u8fd0\u7b79"
                },
                {
                    "value": 2,
                    "name": "\u6027\u80fd\u6d4b\u8bd5"
                },
                {
                    "value": 2,
                    "name": "\u5206\u7c7b"
                },
                {
                    "value": 2,
                    "name": "\u6570\u4ed3\u67b6\u6784"
                },
                {
                    "value": 2,
                    "name": "\u8ba1\u7b97\u673a\u56fe\u5f62\u5b66"
                },
                {
                    "value": 2,
                    "name": "\u51fa\u56fd\u65c5\u6e38"
                },
                {
                    "value": 2,
                    "name": "gnss"
                },
                {
                    "value": 2,
                    "name": "Flink"
                },
                {
                    "value": 2,
                    "name": "\u76f4\u64ad"
                },
                {
                    "value": 2,
                    "name": "\u53cd\u4f5c\u5f0a"
                },
                {
                    "value": 2,
                    "name": "\u7c7b\u8111\u8ba1\u7b97"
                },
                {
                    "value": 2,
                    "name": "\u5168\u7403\u5316"
                },
                {
                    "value": 2,
                    "name": "\u7269\u6d41\u5e73\u53f0"
                },
                {
                    "value": 2,
                    "name": "\u4e03\u9669\u4e00\u91d1"
                },
                {
                    "value": 2,
                    "name": "VIO"
                },
                {
                    "value": 2,
                    "name": "\u5f71\u89c6\uff5c\u52a8\u6f2b"
                },
                {
                    "value": 2,
                    "name": "\u667a\u6167\u57ce\u5e02"
                },
                {
                    "value": 2,
                    "name": "hadoop"
                },
                {
                    "value": 2,
                    "name": "\u6c7d\u8f66\u4ea4\u6613\u5e73\u53f0"
                },
                {
                    "value": 2,
                    "name": "LR"
                },
                {
                    "value": 2,
                    "name": "Lucene"
                },
                {
                    "value": 2,
                    "name": "\u7528\u6237\u589e\u957f"
                },
                {
                    "value": 2,
                    "name": "GPU"
                },
                {
                    "value": 2,
                    "name": "\u9700\u6c42\u5206\u6790"
                },
                {
                    "value": 2,
                    "name": "\u7acb\u4f53\u89c6\u89c9"
                },
                {
                    "value": 1,
                    "name": "\u589e\u957f\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u5305\u5348\u9910\u665a\u9910"
                },
                {
                    "value": 1,
                    "name": "\u836f\u7269\u7814\u53d1"
                },
                {
                    "value": 1,
                    "name": "rgbd"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u50cf"
                },
                {
                    "value": 1,
                    "name": "h264\uff0ch265\uff0cav1"
                },
                {
                    "value": 1,
                    "name": "\u56de\u58f0\u6d88\u9664"
                },
                {
                    "value": 1,
                    "name": "\u5b8c\u6210E\u8f6e\u878d\u8d44"
                },
                {
                    "value": 1,
                    "name": "/Pytorch"
                },
                {
                    "value": 1,
                    "name": "\u68c0\u6d4b\u3001\u8bc6\u522b\u3001\u7f16\u8f91"
                },
                {
                    "value": 1,
                    "name": "\u8f66\u8f86\u52a8\u529b\u5b66\u5efa\u6a21"
                },
                {
                    "value": 1,
                    "name": "java"
                },
                {
                    "value": 1,
                    "name": "\u5065\u5eb7\u7761\u7720"
                },
                {
                    "value": 1,
                    "name": "\u6e32\u67d3"
                },
                {
                    "value": 1,
                    "name": "\u4e16\u754c500\u5f3a"
                },
                {
                    "value": 1,
                    "name": "webgl"
                },
                {
                    "value": 1,
                    "name": "MXNet"
                },
                {
                    "value": 1,
                    "name": "\u6570\u636e\u5f00\u53d1"
                },
                {
                    "value": 1,
                    "name": "\u5de5\u7a0b\u80fd\u529b"
                },
                {
                    "value": 1,
                    "name": "NLP\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "rtk"
                },
                {
                    "value": 1,
                    "name": "\u4f18\u5148\u4e0a\u6d77\u843d\u6237"
                },
                {
                    "value": 1,
                    "name": "\u70b9\u4e91\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u6570\u636e\u7ba1\u7406"
                },
                {
                    "value": 1,
                    "name": "\u4e70\u624b\u6218\u7565"
                },
                {
                    "value": 1,
                    "name": "\u514d\u8d39\u5348\u9910\u665a\u9910"
                },
                {
                    "value": 1,
                    "name": "\u5348\u9910\u4ea4\u901a\u8865\u52a9"
                },
                {
                    "value": 1,
                    "name": "R"
                },
                {
                    "value": 1,
                    "name": "\u901a\u4fe1"
                },
                {
                    "value": 1,
                    "name": "\u98ce\u63a7"
                },
                {
                    "value": 1,
                    "name": "\u5730\u56fe\u5f00\u53d1"
                },
                {
                    "value": 1,
                    "name": "\u673a\u5668\u4eba\u89c6\u89c9"
                },
                {
                    "value": 1,
                    "name": "\u4eba\u5de5\u667a\u80fd\u673a\u5668\u4eba"
                },
                {
                    "value": 1,
                    "name": "\u5e95\u5c42"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u50cf\u8f6c\u6362"
                },
                {
                    "value": 1,
                    "name": "\u6df1\u5ea6\u6a21\u578b"
                },
                {
                    "value": 1,
                    "name": "salm"
                },
                {
                    "value": 1,
                    "name": "SSD"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u52a8\u5316\u6d4b\u8bd5"
                },
                {
                    "value": 1,
                    "name": "UWB"
                },
                {
                    "value": 1,
                    "name": "Cplex"
                },
                {
                    "value": 1,
                    "name": "Tensor"
                },
                {
                    "value": 1,
                    "name": "\u4e09\u7ef4"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u90e8\u7f72"
                },
                {
                    "value": 1,
                    "name": "\u4ea4\u901a\u8fd0\u8f93"
                },
                {
                    "value": 1,
                    "name": "\u5a92\u4f53"
                },
                {
                    "value": 1,
                    "name": "\u8bed\u97f3\u524d\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "C/C++/Python"
                },
                {
                    "value": 1,
                    "name": "x265"
                },
                {
                    "value": 1,
                    "name": "pytorch"
                },
                {
                    "value": 1,
                    "name": "Storm"
                },
                {
                    "value": 1,
                    "name": "\u5927\u5730\u6d4b\u91cf"
                },
                {
                    "value": 1,
                    "name": "\u7cfb\u7edf\u5206\u6790"
                },
                {
                    "value": 1,
                    "name": "\u8bed\u4e49\u7406\u89e3"
                },
                {
                    "value": 1,
                    "name": "\u8fd0\u7b79\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "hybrid/end2end"
                },
                {
                    "value": 1,
                    "name": "\u692d\u5706\u66f2\u7ebf"
                },
                {
                    "value": 1,
                    "name": "ocr"
                },
                {
                    "value": 1,
                    "name": "\u5bfc\u822a\u5f15\u64ce"
                },
                {
                    "value": 1,
                    "name": "\u533b\u7597\u884c\u4e1a"
                },
                {
                    "value": 1,
                    "name": "\u8425\u9500"
                },
                {
                    "value": 1,
                    "name": "\u6280\u672f\u5927\u725b\u4f17\u591a"
                },
                {
                    "value": 1,
                    "name": "\u6570\u636e\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "\u6a21\u578b\u538b\u7f29"
                },
                {
                    "value": 1,
                    "name": "\u4ea7\u54c1\u7b56\u5212"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u52a0\u901f"
                },
                {
                    "value": 1,
                    "name": "CPU"
                },
                {
                    "value": 1,
                    "name": "SSD\u3001Faster"
                },
                {
                    "value": 1,
                    "name": "\u5468\u672b\u53cc\u4f11"
                },
                {
                    "value": 1,
                    "name": "\u9879\u76ee\u7ba1\u7406"
                },
                {
                    "value": 1,
                    "name": "\u6280\u672f\u5927\u725b\u591a"
                },
                {
                    "value": 1,
                    "name": "\u4e50\u5668"
                },
                {
                    "value": 1,
                    "name": "\u7279\u5f81\u6316\u6398"
                },
                {
                    "value": 1,
                    "name": "Pyspark"
                },
                {
                    "value": 1,
                    "name": "\u56e2\u961f\u7ba1\u7406"
                },
                {
                    "value": 1,
                    "name": "\u8f66\u8f86\u8fd0\u52a8\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "SSL/TLS"
                },
                {
                    "value": 1,
                    "name": "AutoML"
                },
                {
                    "value": 1,
                    "name": "\u9ad8\u7cbe\u5730\u56fe"
                },
                {
                    "value": 1,
                    "name": "Node.js"
                },
                {
                    "value": 1,
                    "name": "\u626b\u5730\u673a\u5668\u4eba"
                },
                {
                    "value": 1,
                    "name": "nlp\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "B2B"
                },
                {
                    "value": 1,
                    "name": "\u8bed\u97f3\u6d4b\u8bc4"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u50cf\u62fc\u63a5"
                },
                {
                    "value": 1,
                    "name": "\u96f6\u77e5\u8bc6\u8bc1\u660e"
                },
                {
                    "value": 1,
                    "name": "SFM"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u8ba1\u7b97"
                },
                {
                    "value": 1,
                    "name": "\u5e95\u76d8\u63a7\u5236"
                },
                {
                    "value": 1,
                    "name": "\u6587\u672c\u5206\u7c7b\uff0c"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u63a8\u8350"
                },
                {
                    "value": 1,
                    "name": "python/go"
                },
                {
                    "value": 1,
                    "name": "\u89c4\u5212\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u786c\u4ef6\u5236\u9020"
                },
                {
                    "value": 1,
                    "name": "\u65c5\u6e38"
                },
                {
                    "value": 1,
                    "name": "AR/VR/MR"
                },
                {
                    "value": 1,
                    "name": "\u773c\u52a8"
                },
                {
                    "value": 1,
                    "name": "\u7528\u6237\u7814\u7a76"
                },
                {
                    "value": 1,
                    "name": "\u6570\u5b57\u4fe1\u53f7\u5904\u7406\u6570"
                },
                {
                    "value": 1,
                    "name": "Attention"
                },
                {
                    "value": 1,
                    "name": "\u9057\u4f20\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "GNSS"
                },
                {
                    "value": 1,
                    "name": "CAD\u56fe\u7eb8\u5206\u6790"
                },
                {
                    "value": 1,
                    "name": "\u5355\u76ee"
                },
                {
                    "value": 1,
                    "name": "flv\uff0cmp3\uff0cmp4"
                },
                {
                    "value": 1,
                    "name": "\u5b89\u5168\u5927\u6570\u636e"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u50cf\u68c0\u6d4b"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u5e73\u53f0"
                },
                {
                    "value": 1,
                    "name": "\u7279\u6548"
                },
                {
                    "value": 1,
                    "name": "\u6570\u636e\u7ed3\u6784\u4e0e\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u8f68\u8ff9\u89c4\u5212"
                },
                {
                    "value": 1,
                    "name": "\u8054\u90a6\u5b66\u4e60"
                },
                {
                    "value": 1,
                    "name": "ADAS\u7cfb\u7edf\u5f00\u53d1"
                },
                {
                    "value": 1,
                    "name": "GNSS\u5b9a\u4f4d"
                },
                {
                    "value": 1,
                    "name": "\u4eff\u771f\u4eba"
                },
                {
                    "value": 1,
                    "name": "\u5206\u7c7b\u4fe1\u606f"
                },
                {
                    "value": 1,
                    "name": "\u533b\u5b66\u5f71\u50cf"
                },
                {
                    "value": 1,
                    "name": "\u536b\u661f\u9065\u611f"
                },
                {
                    "value": 1,
                    "name": "Ackerma"
                },
                {
                    "value": 1,
                    "name": "\u5168\u5458\u51fa\u56fd\u6e38"
                },
                {
                    "value": 1,
                    "name": "\u5956\u91d1\u591a\u591a\u591a"
                },
                {
                    "value": 1,
                    "name": "\u7cbe\u5bc6\u5355\u70b9\u5b9a\u4f4d"
                },
                {
                    "value": 1,
                    "name": "neon"
                },
                {
                    "value": 1,
                    "name": "kalman"
                },
                {
                    "value": 1,
                    "name": "\u8fd0\u7ef4\u7ba1\u7406"
                },
                {
                    "value": 1,
                    "name": "TypeScript"
                },
                {
                    "value": 1,
                    "name": "LSTM"
                },
                {
                    "value": 1,
                    "name": "\u4e34\u5e8a\u79d1\u7814"
                },
                {
                    "value": 1,
                    "name": "\u6a21\u578b"
                },
                {
                    "value": 1,
                    "name": "HIve"
                },
                {
                    "value": 1,
                    "name": "\u4e2a\u6027\u5316\u63a8\u8350"
                },
                {
                    "value": 1,
                    "name": "KALDI"
                },
                {
                    "value": 1,
                    "name": "AILab"
                },
                {
                    "value": 1,
                    "name": "\u672c\u5730\u751f\u6d3b"
                },
                {
                    "value": 1,
                    "name": "\u6570\u5b66\u5e93"
                },
                {
                    "value": 1,
                    "name": "\u63a8\u8350\u641c\u7d22"
                },
                {
                    "value": 1,
                    "name": "\u6279\u53d1\uff5c\u96f6\u552e"
                },
                {
                    "value": 1,
                    "name": "\u573a\u666f\u8bc6\u522b"
                },
                {
                    "value": 1,
                    "name": "\u591c\u62cd"
                },
                {
                    "value": 1,
                    "name": "\u7269\u4f53\u8bc6\u522b"
                },
                {
                    "value": 1,
                    "name": "vr\u3002ar"
                },
                {
                    "value": 1,
                    "name": "\u9ad8\u7cbe\u5ea6\u5730\u56fe"
                },
                {
                    "value": 1,
                    "name": "\u5e7f\u544a\u7b56\u7565"
                },
                {
                    "value": 1,
                    "name": "Pulp"
                },
                {
                    "value": 1,
                    "name": "DSP"
                },
                {
                    "value": 1,
                    "name": "kaldi"
                },
                {
                    "value": 1,
                    "name": "\u786c\u4ef6\u5f00\u53d1"
                },
                {
                    "value": 1,
                    "name": "RCNN"
                },
                {
                    "value": 1,
                    "name": "\u5e74\u7ec8\u5956"
                },
                {
                    "value": 1,
                    "name": "\u59ff\u6001\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u5b9e\u65f6\u8def\u51b5"
                },
                {
                    "value": 1,
                    "name": "\u65f6\u95f4\u5e8f\u5217"
                },
                {
                    "value": 1,
                    "name": "\u77e9\u9635\u5206\u6790"
                },
                {
                    "value": 1,
                    "name": "\u89c6\u89c9slam"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u7136\u8bed\u8a00"
                },
                {
                    "value": 1,
                    "name": "\u8ba1\u7b97\u673a\u56fe\u5f62"
                },
                {
                    "value": 1,
                    "name": "\u89c4\u5212"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u50cf\u538b\u7f29"
                },
                {
                    "value": 1,
                    "name": "\u539f\u578b\u8bbe\u8ba1"
                },
                {
                    "value": 1,
                    "name": "\u5173\u7cfb\u6316\u6398"
                },
                {
                    "value": 1,
                    "name": "\u519c\u6797\u7267\u6e14"
                },
                {
                    "value": 1,
                    "name": "\u6392\u5e8f\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "NPU"
                },
                {
                    "value": 1,
                    "name": "\u8bad\u7ec3\u52a0\u901f"
                },
                {
                    "value": 1,
                    "name": "\u78c1\u529b\u8ba1"
                },
                {
                    "value": 1,
                    "name": "\u91d1\u878d\u5238\u5546"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u5de5\u7a0b\u5316"
                },
                {
                    "value": 1,
                    "name": "3D\u6253\u5370"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u50cf\u89c6\u9891\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "\u63a7\u5236\u5668\u8bbe\u8ba1"
                },
                {
                    "value": 1,
                    "name": "\u5730\u7406\u8f68\u8ff9"
                },
                {
                    "value": 1,
                    "name": "AI\u4ea7\u54c1"
                },
                {
                    "value": 1,
                    "name": "\u5de5\u5177\u793e\u533a"
                },
                {
                    "value": 1,
                    "name": "\u97f3\u89c6\u9891\u7f16\u89e3\u7801"
                },
                {
                    "value": 1,
                    "name": "\u9a6c\u5c14\u514b\u592b\u968f\u673a\u52a8"
                },
                {
                    "value": 1,
                    "name": "\u63a7\u5236\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u591a\u4f20\u611f\u5668"
                },
                {
                    "value": 1,
                    "name": "Go"
                },
                {
                    "value": 1,
                    "name": "\u673a\u5668\u611f\u77e5"
                },
                {
                    "value": 1,
                    "name": "\u5f3a\u608d\u7684\u521b\u59cb\u4eba"
                },
                {
                    "value": 1,
                    "name": "Database"
                },
                {
                    "value": 1,
                    "name": "CTR"
                },
                {
                    "value": 1,
                    "name": "\u5b9e\u4f53\u8bc6\u522b"
                },
                {
                    "value": 1,
                    "name": "\u7f51\u7edc\u4f20\u8f93\u534f\u8bae"
                },
                {
                    "value": 1,
                    "name": "3DCAD"
                },
                {
                    "value": 1,
                    "name": "Linux\u5f00\u53d1"
                },
                {
                    "value": 1,
                    "name": "numpy"
                },
                {
                    "value": 1,
                    "name": "\u4e0a\u5e02\u516c\u53f8"
                },
                {
                    "value": 1,
                    "name": "VINS"
                },
                {
                    "value": 1,
                    "name": "\u8fd0\u52a8\u63a7\u5236\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "KF/EKF"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u7b56\u7565"
                },
                {
                    "value": 1,
                    "name": "3dmm"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u50cf\u5206\u7c7b"
                },
                {
                    "value": 1,
                    "name": "Transformer"
                },
                {
                    "value": 1,
                    "name": "\u667a\u80fd\u9a7e\u9a76"
                },
                {
                    "value": 1,
                    "name": "\u91cf\u5316"
                },
                {
                    "value": 1,
                    "name": "SOA"
                },
                {
                    "value": 1,
                    "name": "3D\u59ff\u6001\u91cd\u5efa"
                },
                {
                    "value": 1,
                    "name": "flow"
                },
                {
                    "value": 1,
                    "name": "ADAS"
                },
                {
                    "value": 1,
                    "name": "\u79d1\u6280\u5927\u725b\u516c\u53f8"
                },
                {
                    "value": 1,
                    "name": "RCN"
                },
                {
                    "value": 1,
                    "name": "\u6216"
                },
                {
                    "value": 1,
                    "name": "\u8bba\u6587\u5199\u4f5c"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u4eff\u771f"
                },
                {
                    "value": 1,
                    "name": "\u9ad8\u7ea7\u6280\u672f\u7ba1\u7406"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u5206\u6790"
                },
                {
                    "value": 1,
                    "name": "\u5feb\u901f\u6210\u957f"
                },
                {
                    "value": 1,
                    "name": "\u641c\u7d22\u5f15\u64ce"
                },
                {
                    "value": 1,
                    "name": "\u6df7\u54cd"
                },
                {
                    "value": 1,
                    "name": "\u673a\u5668\u5b66\u4e60\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u65f6\u5e8f\u6570\u636e\u5e93"
                },
                {
                    "value": 1,
                    "name": "\u5d4c\u5165\u5f0f\u6280\u672f"
                },
                {
                    "value": 1,
                    "name": "\u5e95\u5c42\u89c6\u89c9"
                },
                {
                    "value": 1,
                    "name": "/"
                },
                {
                    "value": 1,
                    "name": "VTK"
                },
                {
                    "value": 1,
                    "name": "\u673a\u5668\u5b66\u4e60\u6a21\u578b"
                },
                {
                    "value": 1,
                    "name": "android"
                },
                {
                    "value": 1,
                    "name": "\u673a\u5668\u4eba\u5173\u952e\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u878d\u5408\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "FLINK"
                },
                {
                    "value": 1,
                    "name": "Gurobi"
                },
                {
                    "value": 1,
                    "name": "\u4e92\u8054\u7f51\u51fa\u884c"
                },
                {
                    "value": 1,
                    "name": "\u5206\u5e03\u5f0f"
                },
                {
                    "value": 1,
                    "name": "MCU"
                },
                {
                    "value": 1,
                    "name": "\u5e7f\u544a\u6295\u653e"
                },
                {
                    "value": 1,
                    "name": "\u6570\u5b57\u56fe\u50cf\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "cuda"
                },
                {
                    "value": 1,
                    "name": "\u5149\u5b66"
                },
                {
                    "value": 1,
                    "name": "PP"
                },
                {
                    "value": 1,
                    "name": "\u89c4\u5219\u5f15\u64ce"
                },
                {
                    "value": 1,
                    "name": "\u5f02\u5e38\u8bca\u65ad"
                },
                {
                    "value": 1,
                    "name": "asr"
                },
                {
                    "value": 1,
                    "name": "\u540d\u6821\u540d\u4f01\u80cc\u666f"
                },
                {
                    "value": 1,
                    "name": "\u751f\u4ea7\u8c03\u5ea6"
                },
                {
                    "value": 1,
                    "name": "\u5e74\u7ec8\u591a\u85aa"
                },
                {
                    "value": 1,
                    "name": "\u4e13\u4e1a\u670d\u52a1\uff5c\u54a8\u8be2"
                },
                {
                    "value": 1,
                    "name": "\u964d\u566a"
                },
                {
                    "value": 1,
                    "name": "\u8bed\u97f3\u8f6c\u6362"
                },
                {
                    "value": 1,
                    "name": "\u8c03\u62e8"
                },
                {
                    "value": 1,
                    "name": "\u5e7f\u544a\u63a8\u8350"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u5b9a\u4f4d"
                },
                {
                    "value": 1,
                    "name": "3DGIS"
                },
                {
                    "value": 1,
                    "name": "\u6570\u636e\u6e05\u6d17"
                },
                {
                    "value": 1,
                    "name": "\u793e\u4ea4\u4ea7\u54c1"
                },
                {
                    "value": 1,
                    "name": "3D\u5f15\u64ce"
                },
                {
                    "value": 1,
                    "name": "JitterBuffer"
                },
                {
                    "value": 1,
                    "name": "\u4e91\u5b89\u5168"
                },
                {
                    "value": 1,
                    "name": "\u5bfc\u822a\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u5bc6\u7801\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "DSP\u7f16\u7a0b"
                },
                {
                    "value": 1,
                    "name": "TF"
                },
                {
                    "value": 1,
                    "name": "\u5bfc\u822a"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u8c03\u7814"
                },
                {
                    "value": 1,
                    "name": "\u542f\u53d1\u5f0f\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u91d1\u878d\u98ce\u63a7"
                },
                {
                    "value": 1,
                    "name": "CRF"
                },
                {
                    "value": 1,
                    "name": "\u96f6\u98df\u4e0b\u5348\u8336"
                },
                {
                    "value": 1,
                    "name": "\u5de5\u4e1a\u6392\u7a0b"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u6587\u5206\u6790"
                },
                {
                    "value": 1,
                    "name": "\u4f11\u95f2\uff5c\u5a31\u4e50"
                },
                {
                    "value": 1,
                    "name": "\u4eff\u771f"
                },
                {
                    "value": 1,
                    "name": "\u8def\u51b5\u8ba1\u7b97"
                },
                {
                    "value": 1,
                    "name": "\u8def\u5f84\u4f18\u5316"
                },
                {
                    "value": 1,
                    "name": "HADOOP"
                },
                {
                    "value": 1,
                    "name": "GO"
                },
                {
                    "value": 1,
                    "name": "sfm"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u7136\u8bed\u8a00\u5904"
                },
                {
                    "value": 1,
                    "name": "\u5927\u6570\u636e\u8f6f\u4ef6"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u57fa\u7840"
                },
                {
                    "value": 1,
                    "name": "\u9065\u611f"
                },
                {
                    "value": 1,
                    "name": "\u878d\u5408IMU"
                },
                {
                    "value": 1,
                    "name": "Rust"
                },
                {
                    "value": 1,
                    "name": "\u5206\u5e03\u5f0f\u8bad\u7ec3"
                },
                {
                    "value": 1,
                    "name": "\u67b6\u6784\u5e08"
                },
                {
                    "value": 1,
                    "name": "\u542f\u53d1\u5f0f\u89c4\u5219\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "SVC"
                },
                {
                    "value": 1,
                    "name": "ppp-rtk"
                },
                {
                    "value": 1,
                    "name": "\u53ec\u56de"
                },
                {
                    "value": 1,
                    "name": "c"
                },
                {
                    "value": 1,
                    "name": "\u6587\u672c\u68c0\u6d4b"
                },
                {
                    "value": 1,
                    "name": "ERP"
                },
                {
                    "value": 1,
                    "name": "Caffe\u3001Pytorch\u3001"
                },
                {
                    "value": 1,
                    "name": "3D\u89c6\u89c9\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u73af\u5883\u611f\u77e5\u4e0e\u878d\u5408"
                },
                {
                    "value": 1,
                    "name": "\u6d4b\u8bd5\u5f00\u53d1"
                },
                {
                    "value": 1,
                    "name": "MatLab"
                },
                {
                    "value": 1,
                    "name": "ORBSLAM"
                },
                {
                    "value": 1,
                    "name": "\u9690\u79d8\u8ba1\u7b97\u672f"
                },
                {
                    "value": 1,
                    "name": "\u6a21\u578b\u79fb\u690d\u4f18\u5316"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u4f18\u5316"
                },
                {
                    "value": 1,
                    "name": "\u901f\u5ea6\u63a7\u5236"
                },
                {
                    "value": 1,
                    "name": "\u57fa\u7840\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u5730\u56fe\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "libvpx"
                },
                {
                    "value": 1,
                    "name": "\u6574\u6570\u89c4\u5212"
                },
                {
                    "value": 1,
                    "name": "\u5de5\u4e1a\u89c6\u89c9\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "LTE"
                },
                {
                    "value": 1,
                    "name": "\u6a21\u62df\u9000\u706b\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "PID"
                },
                {
                    "value": 1,
                    "name": "\u6392\u7a0b"
                },
                {
                    "value": 1,
                    "name": "\u8d44\u8baf"
                },
                {
                    "value": 1,
                    "name": "\u5e7f\u544aCTR/CVR"
                },
                {
                    "value": 1,
                    "name": "\u5927\u5e73\u53f0"
                },
                {
                    "value": 1,
                    "name": "\u6241\u5e73\u5316\u7ba1\u7406"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u843d\u5730"
                },
                {
                    "value": 1,
                    "name": "H.264/265"
                },
                {
                    "value": 1,
                    "name": "\u611f\u77e5\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u7ecf\u5178\u63a7\u5236\u7406\u8bba"
                },
                {
                    "value": 1,
                    "name": "ECC"
                },
                {
                    "value": 1,
                    "name": "GPS"
                },
                {
                    "value": 1,
                    "name": "CPLEX"
                },
                {
                    "value": 1,
                    "name": "\u52a8\u4f5c\u8bc6\u522b"
                },
                {
                    "value": 1,
                    "name": "VR"
                },
                {
                    "value": 1,
                    "name": "Windows"
                },
                {
                    "value": 1,
                    "name": "X264"
                },
                {
                    "value": 1,
                    "name": "PHM"
                },
                {
                    "value": 1,
                    "name": "\u91d1\u878d\u98ce\u63a7AI"
                },
                {
                    "value": 1,
                    "name": "\u4f20\u611f\u5668\u6216\u70b9\u4e91"
                },
                {
                    "value": 1,
                    "name": "\u89c6\u9891\u7f16\u8f91"
                },
                {
                    "value": 1,
                    "name": "h264"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u52a8\u5316"
                },
                {
                    "value": 1,
                    "name": "pandas"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u52a9\u4e09\u9910"
                },
                {
                    "value": 1,
                    "name": "\u5de5\u4e1a\u9886\u57df"
                },
                {
                    "value": 1,
                    "name": "\u8d85\u957f\u5e26\u85aa\u5047\u671f"
                },
                {
                    "value": 1,
                    "name": "\u516c\u94a5"
                },
                {
                    "value": 1,
                    "name": "\u80a2\u4f53\u68c0\u6d4b"
                },
                {
                    "value": 1,
                    "name": "AGV"
                },
                {
                    "value": 1,
                    "name": "\u5b9a\u4f4d"
                },
                {
                    "value": 1,
                    "name": "PID\u63a7\u5236"
                },
                {
                    "value": 1,
                    "name": "\u4f4f\u798f\u8ba1\u5212"
                },
                {
                    "value": 1,
                    "name": "AEB"
                },
                {
                    "value": 1,
                    "name": "\u89c6\u9891\u9884\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "\u641c\u7d22\u63a8\u8350"
                },
                {
                    "value": 1,
                    "name": "CCF"
                },
                {
                    "value": 1,
                    "name": "\u5e74\u7ec8\u5956\u91d1"
                },
                {
                    "value": 1,
                    "name": "\u8ba1\u7b97\u51e0\u4f55"
                },
                {
                    "value": 1,
                    "name": "\u865a\u5047\u6d41\u91cf"
                },
                {
                    "value": 1,
                    "name": "\u5185\u5bb9\u7406\u89e3"
                },
                {
                    "value": 1,
                    "name": "\u9886\u519b\u4f01\u4e1a"
                },
                {
                    "value": 1,
                    "name": "\u5e26\u5bbd\u63a7\u5236"
                },
                {
                    "value": 1,
                    "name": "NLP\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u5bfc\u822a"
                },
                {
                    "value": 1,
                    "name": "\u5927\u6570\u636e\u5904\u7406\u6280\u672f"
                },
                {
                    "value": 1,
                    "name": "\u4e09\u7ef4\u91cd\u6784"
                },
                {
                    "value": 1,
                    "name": "\u51e0\u4f55\u5b66"
                },
                {
                    "value": 1,
                    "name": "BIM+3D"
                },
                {
                    "value": 1,
                    "name": "HBase"
                },
                {
                    "value": 1,
                    "name": "\u751f\u7406\u53c2\u6570"
                },
                {
                    "value": 1,
                    "name": "AIOPS"
                },
                {
                    "value": 1,
                    "name": "\u8def\u51b5\u4f18\u5316"
                },
                {
                    "value": 1,
                    "name": "\u5e7f\u544a\u5e73\u53f0"
                },
                {
                    "value": 1,
                    "name": "\u8bed\u4e49\u5206\u5272"
                },
                {
                    "value": 1,
                    "name": "\u7f16\u7a0b"
                },
                {
                    "value": 1,
                    "name": "\u6a21\u7cca\u63a7\u5236"
                },
                {
                    "value": 1,
                    "name": "NPL"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u4e3b\u664b\u5347\u8ba1\u5212"
                },
                {
                    "value": 1,
                    "name": "\u4e0b\u5348\u8336"
                },
                {
                    "value": 1,
                    "name": "\u6709\u524d\u9014"
                },
                {
                    "value": 1,
                    "name": "\u58f0\u7eb9\u8bc6\u522b"
                },
                {
                    "value": 1,
                    "name": "rtk\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u8282\u65e5\u798f\u5229"
                },
                {
                    "value": 1,
                    "name": "\u6570\u636e\u91c7\u96c6"
                },
                {
                    "value": 1,
                    "name": "\u52a8\u529b\u5b66\u5efa\u6a21"
                },
                {
                    "value": 1,
                    "name": "\u5168\u94fe\u8defSaaS\u5e73\u53f0"
                },
                {
                    "value": 1,
                    "name": "\u5bfc\u822a\u89c4\u5212"
                },
                {
                    "value": 1,
                    "name": "\u4e09\u7ef4\u56fe\u5f62"
                },
                {
                    "value": 1,
                    "name": "AI\u56fe\u50cf\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u5bfc\u822a\u5b9a\u4f4d"
                },
                {
                    "value": 1,
                    "name": "\u4f20\u611f\u5668\u878d\u5408"
                },
                {
                    "value": 1,
                    "name": "AR"
                },
                {
                    "value": 1,
                    "name": "\u6ee4\u955c"
                },
                {
                    "value": 1,
                    "name": "\u51e0\u4f55\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "DeepFM"
                },
                {
                    "value": 1,
                    "name": "ETL"
                },
                {
                    "value": 1,
                    "name": "ACC/AEB/LKA"
                },
                {
                    "value": 1,
                    "name": "C++/python"
                },
                {
                    "value": 1,
                    "name": "\u5927\u5065\u5eb7"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u50cf\u589e\u5f3a"
                },
                {
                    "value": 1,
                    "name": "\u53cc\u76ee\u89c6\u89c9"
                },
                {
                    "value": 1,
                    "name": "ISP"
                },
                {
                    "value": 1,
                    "name": "\u89c6\u89c9SLAM"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u5f62\u56fe\u50cf\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u6a21\u578b"
                },
                {
                    "value": 1,
                    "name": "\u76ee\u6807\u5206\u5272"
                },
                {
                    "value": 1,
                    "name": "\u65b0\u5a92\u4f53"
                },
                {
                    "value": 1,
                    "name": "\u79d1\u7814"
                },
                {
                    "value": 1,
                    "name": "\u591a\u4f20\u611f\u5668\u878d\u5408"
                },
                {
                    "value": 1,
                    "name": "DNN"
                },
                {
                    "value": 1,
                    "name": "\u673a\u5668\u5b66\u4e60\u7b97\u6cd5\u673a"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u5f62\u5b66"
                },
                {
                    "value": 1,
                    "name": "\u8fd1\u7ea2\u5916"
                },
                {
                    "value": 1,
                    "name": "\u53bb\u6df7\u54cd"
                },
                {
                    "value": 1,
                    "name": "\u8bed\u4e49\u5206\u6790"
                },
                {
                    "value": 1,
                    "name": "\u5f00\u53d1"
                },
                {
                    "value": 1,
                    "name": "\u4e09\u7ef4\u91cd\u5efa"
                },
                {
                    "value": 1,
                    "name": "\u6295\u8d44/\u878d\u8d44"
                },
                {
                    "value": 1,
                    "name": "pil"
                },
                {
                    "value": 1,
                    "name": "NLP/CV"
                },
                {
                    "value": 1,
                    "name": "\u5185\u5bb9\u63a8\u8350"
                },
                {
                    "value": 1,
                    "name": "\u9aa8\u79d1\u673a\u5668\u4eba"
                },
                {
                    "value": 1,
                    "name": "\u4eba\u4f533D\u91cd\u5efa"
                },
                {
                    "value": 1,
                    "name": "\u65e0\u76d1\u7763\u5b66\u4e60"
                },
                {
                    "value": 1,
                    "name": "\u907f\u969c"
                },
                {
                    "value": 1,
                    "name": "\u4e50\u7406\u8f6c\u6362"
                },
                {
                    "value": 1,
                    "name": "\u7535\u5546\u641c\u7d22"
                },
                {
                    "value": 1,
                    "name": "\u52a8\u4f5c\u6355\u6349"
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
        chart_e6467948103948899914325ca2f0b8ed.setOption(option_e6467948103948899914325ca2f0b8ed);
    </script>
                <div id="d09a42159f8644faa96fdc3d480a70c6" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_d09a42159f8644faa96fdc3d480a70c6 = echarts.init(
            document.getElementById('d09a42159f8644faa96fdc3d480a70c6'), 'white', {renderer: 'canvas'});
        var option_d09a42159f8644faa96fdc3d480a70c6 = {
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
                980,
                505,
                102,
                92,
                48,
                19,
                13,
                4
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
                    "value": 980
                },
                {
                    "name": "\u7855\u58eb",
                    "value": 505
                },
                {
                    "name": "\u5e94\u5c4a / \u672c\u79d1",
                    "value": 102
                },
                {
                    "name": "\u5e94\u5c4a / \u7855\u58eb",
                    "value": 92
                },
                {
                    "name": "\u4e0d\u9650",
                    "value": 48
                },
                {
                    "name": "\u535a\u58eb",
                    "value": 19
                },
                {
                    "name": "\u5e94\u5c4a / \u4e0d\u9650",
                    "value": 13
                },
                {
                    "name": "\u5e94\u5c4a / \u535a\u58eb",
                    "value": 4
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
                    "value": 980
                },
                {
                    "name": "\u7855\u58eb",
                    "value": 505
                },
                {
                    "name": "\u5e94\u5c4a / \u672c\u79d1",
                    "value": 102
                },
                {
                    "name": "\u5e94\u5c4a / \u7855\u58eb",
                    "value": 92
                },
                {
                    "name": "\u4e0d\u9650",
                    "value": 48
                },
                {
                    "name": "\u535a\u58eb",
                    "value": 19
                },
                {
                    "name": "\u5e94\u5c4a / \u4e0d\u9650",
                    "value": 13
                },
                {
                    "name": "\u5e94\u5c4a / \u535a\u58eb",
                    "value": 4
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
                "\u5e94\u5c4a / \u535a\u58eb"
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
                "\u5e94\u5c4a / \u535a\u58eb"
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
        chart_d09a42159f8644faa96fdc3d480a70c6.setOption(option_d09a42159f8644faa96fdc3d480a70c6);
    </script>
                <div id="885711c5885f40dfb2fd445d89d1cebb" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_885711c5885f40dfb2fd445d89d1cebb = echarts.init(
            document.getElementById('885711c5885f40dfb2fd445d89d1cebb'), 'white', {renderer: 'canvas'});
        var option_885711c5885f40dfb2fd445d89d1cebb = {
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
                689,
                375,
                275,
                211,
                200,
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
                    "value": 689
                },
                {
                    "name": "\u7ecf\u9a8c1-3\u5e74",
                    "value": 375
                },
                {
                    "name": "\u7ecf\u9a8c\u4e0d\u9650",
                    "value": 275
                },
                {
                    "name": "\u7ecf\u9a8c\u5728\u6821",
                    "value": 211
                },
                {
                    "name": "\u7ecf\u9a8c5-10\u5e74",
                    "value": 200
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
                    "value": 689
                },
                {
                    "name": "\u7ecf\u9a8c1-3\u5e74",
                    "value": 375
                },
                {
                    "name": "\u7ecf\u9a8c\u4e0d\u9650",
                    "value": 275
                },
                {
                    "name": "\u7ecf\u9a8c\u5728\u6821",
                    "value": 211
                },
                {
                    "name": "\u7ecf\u9a8c5-10\u5e74",
                    "value": 200
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
        chart_885711c5885f40dfb2fd445d89d1cebb.setOption(option_885711c5885f40dfb2fd445d89d1cebb);
    </script>
                <div id="4562f0b8363c426496fe107df707b020" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_4562f0b8363c426496fe107df707b020 = echarts.init(
            document.getElementById('4562f0b8363c426496fe107df707b020'), 'white', {renderer: 'canvas'});
            
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
    
        var option_4562f0b8363c426496fe107df707b020 = {
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
                            "color": "rgb(108,50,5)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u95ee\u7b54",
                    "value": 99,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,69,47)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u52a9\u7406",
                    "value": 98,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,156,46)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u5ba2\u670d",
                    "value": 97,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,9,23)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u8bc6\u56fe\u8c31",
                    "value": 96,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,93,59)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u8bc6\u63a8\u7406",
                    "value": 95,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,75,26)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u6e05\u6d17",
                    "value": 94,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,58,150)"
                        }
                    }
                },
                {
                    "name": "\u60c5\u611f\u5206\u6790",
                    "value": 93,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,140,92)"
                        }
                    }
                },
                {
                    "name": "\u8206\u60c5\u5206\u6790",
                    "value": 92,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,137,51)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u4e49\u7406\u89e3",
                    "value": 91,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,50,155)"
                        }
                    }
                },
                {
                    "name": "\u610f\u56fe\u7406\u89e3",
                    "value": 90,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,106,122)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u6458\u8981",
                    "value": 89,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,3,107)"
                        }
                    }
                },
                {
                    "name": "query\u5206\u6790",
                    "value": 88,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,145,141)"
                        }
                    }
                },
                {
                    "name": "query\u7406\u89e3",
                    "value": 87,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,87,132)"
                        }
                    }
                },
                {
                    "name": "\u62fc\u5199\u7ea0\u9519",
                    "value": 86,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,94,0)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u753b\u50cf",
                    "value": 85,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,84,13)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u95fb\u7279\u5f81",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,0,29)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u4e49\u53ec\u56de",
                    "value": 83,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,127,122)"
                        }
                    }
                },
                {
                    "name": "\u591a\u8f6e\u5bf9\u8bdd",
                    "value": 82,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,156,52)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u68c0\u7d22",
                    "value": 81,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,28,16)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u68c0\u7d22",
                    "value": 80,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,3,58)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u76f8\u5173\u6027",
                    "value": 79,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,109,17)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u8c31\u67e5\u8be2",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,139,6)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u8c31\u63a8\u7406",
                    "value": 77,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,127,83)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u6587\u672c",
                    "value": 76,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,29,79)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u6587\u672c",
                    "value": 75,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,32,115)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u5e7f\u544aNLP",
                    "value": 74,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,133,39)"
                        }
                    }
                },
                {
                    "name": "\u5bf9\u8bdd\u7406\u89e3",
                    "value": 73,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,138,145)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u5b89\u5168",
                    "value": 72,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,149,106)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u8baf\u63a8\u8350\u548c\u641c\u7d22",
                    "value": 71,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,79,37)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u884c\u4e3a\u5206\u6790",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,69,16)"
                        }
                    }
                },
                {
                    "name": "\u5bf9\u8bdd\u8f6c\u5199",
                    "value": 69,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,131,100)"
                        }
                    }
                },
                {
                    "name": "UGC\u6316\u6398",
                    "value": 68,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,135,120)"
                        }
                    }
                },
                {
                    "name": "\u6cd5\u5f8b\u95ee\u7b54",
                    "value": 67,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,89,57)"
                        }
                    }
                },
                {
                    "name": "\u9605\u8bfb\u7406\u89e3",
                    "value": 66,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,57,125)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u6807\u7b7e\u4f53\u7cfb",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,40,57)"
                        }
                    }
                },
                {
                    "name": "\u4efb\u52a1\u5f0f\u5bf9\u8bdd\u7cfb\u7edf",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,133,2)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672cspam\u8bc6\u522b",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,33,49)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u6559\u80b2\u9886\u57df",
                    "value": 62,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,68,130)"
                        }
                    }
                },
                {
                    "name": "\u50ac\u6536\u6587\u672c\u6316\u6398",
                    "value": 61,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,147,140)"
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
        chart_4562f0b8363c426496fe107df707b020.setOption(option_4562f0b8363c426496fe107df707b020);
    </script>
                <div id="86fe6d08f82149e1b07299818e413a24" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_86fe6d08f82149e1b07299818e413a24 = echarts.init(
            document.getElementById('86fe6d08f82149e1b07299818e413a24'), 'white', {renderer: 'canvas'});
            
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
    
        var option_86fe6d08f82149e1b07299818e413a24 = {
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
                            "color": "rgb(36,59,72)"
                        }
                    }
                },
                {
                    "name": "Java",
                    "value": 99,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,27,84)"
                        }
                    }
                },
                {
                    "name": "C++",
                    "value": 98,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,44,129)"
                        }
                    }
                },
                {
                    "name": "GO",
                    "value": 97,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,4,14)"
                        }
                    }
                },
                {
                    "name": "Linux",
                    "value": 96,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,54,68)"
                        }
                    }
                },
                {
                    "name": "TensorFlow",
                    "value": 95,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,146,76)"
                        }
                    }
                },
                {
                    "name": "Keras",
                    "value": 94,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,61,4)"
                        }
                    }
                },
                {
                    "name": "PyTorch",
                    "value": 93,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,49,124)"
                        }
                    }
                },
                {
                    "name": "\u6b63\u5219\u8868\u8fbe\u5f0f",
                    "value": 92,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,160,39)"
                        }
                    }
                },
                {
                    "name": "\u547d\u540d\u5b9e\u4f53\u8bc6\u522b",
                    "value": 91,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,21,80)"
                        }
                    }
                },
                {
                    "name": "\u5173\u7cfb\u62bd\u53d6",
                    "value": 90,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,7,84)"
                        }
                    }
                },
                {
                    "name": "\u5c5e\u6027\u62bd\u53d6",
                    "value": 89,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,147,36)"
                        }
                    }
                },
                {
                    "name": "\u4e8b\u4ef6\u62bd\u53d6",
                    "value": 88,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,145,10)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u5206\u7c7b",
                    "value": 87,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,1,107)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u76f8\u4f3c\u5ea6\u8ba1\u7b97",
                    "value": 86,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,121,18)"
                        }
                    }
                },
                {
                    "name": "\u5173\u7cfb\u62bd\u53d6",
                    "value": 85,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,18,132)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u7b97\u6cd5",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,69,7)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u4e49\u5339\u914d",
                    "value": 83,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,26,2)"
                        }
                    }
                },
                {
                    "name": "\u5e8f\u5217\u6807\u6ce8",
                    "value": 82,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,107,139)"
                        }
                    }
                },
                {
                    "name": "\u591a\u6a21\u6001\u5b66\u4e60",
                    "value": 81,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,54,125)"
                        }
                    }
                },
                {
                    "name": "\u591a\u6a21\u6001\u7406\u89e3",
                    "value": 80,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,53,142)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u8868\u793a",
                    "value": 79,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,89,103)"
                        }
                    }
                },
                {
                    "name": "\u76f8\u5173\u6027",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,155,141)"
                        }
                    }
                },
                {
                    "name": "\u5206\u8bcd",
                    "value": 77,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,104,146)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u68c0\u7d22",
                    "value": 76,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,139,127)"
                        }
                    }
                },
                {
                    "name": "\u5bf9\u8bdd\u751f\u6210",
                    "value": 75,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,19,45)"
                        }
                    }
                },
                {
                    "name": "Embedding",
                    "value": 74,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,143,95)"
                        }
                    }
                },
                {
                    "name": "Q&A",
                    "value": 73,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,123,62)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u7ffb\u8bd1",
                    "value": 72,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,73,69)"
                        }
                    }
                },
                {
                    "name": "SelfAttention",
                    "value": 71,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,146,120)"
                        }
                    }
                },
                {
                    "name": "lda",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,139,115)"
                        }
                    }
                },
                {
                    "name": "RNN",
                    "value": 69,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,7,18)"
                        }
                    }
                },
                {
                    "name": "CNN",
                    "value": 68,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,51,48)"
                        }
                    }
                },
                {
                    "name": "seq2seq",
                    "value": 67,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,85,42)"
                        }
                    }
                },
                {
                    "name": "Word2vec",
                    "value": 66,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,85,17)"
                        }
                    }
                },
                {
                    "name": "GPT2",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,20,80)"
                        }
                    }
                },
                {
                    "name": "Transformer",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,113,22)"
                        }
                    }
                },
                {
                    "name": "BERT",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,98,3)"
                        }
                    }
                },
                {
                    "name": "\u4e3b\u9898\u6a21\u578b",
                    "value": 62,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,19,99)"
                        }
                    }
                },
                {
                    "name": "KBQA",
                    "value": 61,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,159,47)"
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
        chart_86fe6d08f82149e1b07299818e413a24.setOption(option_86fe6d08f82149e1b07299818e413a24);
    </script>
                <div id="10ae9a71fc1b4f6f869e91d9d334d7a7" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_10ae9a71fc1b4f6f869e91d9d334d7a7 = echarts.init(
            document.getElementById('10ae9a71fc1b4f6f869e91d9d334d7a7'), 'white', {renderer: 'canvas'});
            
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
    
        var option_10ae9a71fc1b4f6f869e91d9d334d7a7 = {
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
                            "color": "rgb(82,86,23)"
                        }
                    }
                },
                {
                    "name": "OCR",
                    "value": 99,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,82,146)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u5206\u6790",
                    "value": 98,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,122,50)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u5f71\u50cf\u7406\u89e3",
                    "value": 97,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,3,126)"
                        }
                    }
                },
                {
                    "name": "\u76ee\u6807\u68c0\u6d4b\u548c\u8ddf\u8e2a",
                    "value": 96,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,27,1)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5206\u5272",
                    "value": 95,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,77,138)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u641c\u7d22",
                    "value": 94,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,113,121)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u7a0b\u5b9e\u73b0",
                    "value": 93,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,50,15)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5206\u6790",
                    "value": 92,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,96,70)"
                        }
                    }
                },
                {
                    "name": "\u6027\u80fd\u4f18\u5316",
                    "value": 91,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,146,126)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u89c6\u9891",
                    "value": 90,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,146,24)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u7247\u5185\u5bb9\u751f\u6210",
                    "value": 89,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,49,140)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u63a8\u8350",
                    "value": 88,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,129,32)"
                        }
                    }
                },
                {
                    "name": "\u5bf9\u8c61\u63d0\u53d6",
                    "value": 87,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,129,141)"
                        }
                    }
                },
                {
                    "name": "\u7269\u4f53\u611f\u77e5",
                    "value": 86,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,35,58)"
                        }
                    }
                },
                {
                    "name": "\u7269\u4f53\u5206\u7c7b",
                    "value": 85,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,154,138)"
                        }
                    }
                },
                {
                    "name": "\u7269\u4f53\u8ddf\u8e2a",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,1,97)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7ed3\u6784\u5316",
                    "value": 83,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,2,80)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6167\u57ce\u5e02",
                    "value": 82,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,91,154)"
                        }
                    }
                },
                {
                    "name": "\u9065\u611f\u89e3\u8bd1",
                    "value": 81,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,62,105)"
                        }
                    }
                },
                {
                    "name": "\u4e8b\u4ef6\u5206\u6790",
                    "value": 80,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,83,147)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b\u538b\u7f29\u8f7b\u91cf\u5316\u5e94\u7528",
                    "value": 79,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,62,78)"
                        }
                    }
                },
                {
                    "name": "\u591a\u4f20\u611f\u5668\u878d\u5408",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,66,33)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u4f4d\u548c\u5bfc\u822a",
                    "value": 77,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,72,42)"
                        }
                    }
                },
                {
                    "name": "\u6ee4\u955c\u521b\u4f5c\u5de5\u5177",
                    "value": 76,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,132,15)"
                        }
                    }
                },
                {
                    "name": "\u5173\u952e\u70b9\u68c0\u6d4b",
                    "value": 75,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,11,66)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u751f\u6210",
                    "value": 74,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,17,72)"
                        }
                    }
                },
                {
                    "name": "AR/MR",
                    "value": 73,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,69,130)"
                        }
                    }
                },
                {
                    "name": "3D\u91cd\u5efa",
                    "value": 72,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,110,56)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u6444\u5f71",
                    "value": 71,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,3,108)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u91cd\u5efa",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,98,138)"
                        }
                    }
                },
                {
                    "name": "\u6750\u8d28\u548c\u5916\u89c2\u91cd\u5efa",
                    "value": 69,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,157,83)"
                        }
                    }
                },
                {
                    "name": "\u5ea6\u91cf\u5b66\u4e60",
                    "value": 68,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,7,74)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u4e49/\u5b9e\u4f8b\u5206\u5272",
                    "value": 67,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,57,123)"
                        }
                    }
                },
                {
                    "name": "\u6587\u5b57\u68c0\u6d4b\u8bc6\u522b",
                    "value": 66,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,69,127)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u8138\u68c0\u6d4b\u8bc6\u522b",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,134,19)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u7f16\u8f91\u751f\u6210",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,23,45)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u683c\u8fc1\u79fb",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,139,83)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u56fe\u79c0\u79c0",
                    "value": 62,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,145,9)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u62cd",
                    "value": 61,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,112,40)"
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
        chart_10ae9a71fc1b4f6f869e91d9d334d7a7.setOption(option_10ae9a71fc1b4f6f869e91d9d334d7a7);
    </script>
                <div id="068ef39b14de4f358941e7f1e4b60fa0" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_068ef39b14de4f358941e7f1e4b60fa0 = echarts.init(
            document.getElementById('068ef39b14de4f358941e7f1e4b60fa0'), 'white', {renderer: 'canvas'});
            
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
    
        var option_068ef39b14de4f358941e7f1e4b60fa0 = {
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
                            "color": "rgb(110,58,31)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u8bc6\u522b/\u5206\u7c7b",
                    "value": 99,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,89,67)"
                        }
                    }
                },
                {
                    "name": "\u7269\u4f53\u68c0\u6d4b",
                    "value": 98,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,140,42)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u5206\u6790",
                    "value": 97,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,83,10)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b\u538b\u7f29",
                    "value": 96,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,72,77)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5206\u5272",
                    "value": 95,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,69,12)"
                        }
                    }
                },
                {
                    "name": "GAN",
                    "value": 94,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,138,95)"
                        }
                    }
                },
                {
                    "name": "Linux",
                    "value": 93,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,145,42)"
                        }
                    }
                },
                {
                    "name": "tensorflow",
                    "value": 92,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,76,42)"
                        }
                    }
                },
                {
                    "name": "pytorch",
                    "value": 91,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,6,105)"
                        }
                    }
                },
                {
                    "name": "C++",
                    "value": 90,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,143,47)"
                        }
                    }
                },
                {
                    "name": "Python",
                    "value": 89,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,144,108)"
                        }
                    }
                },
                {
                    "name": "CVPR",
                    "value": 88,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,121,116)"
                        }
                    }
                },
                {
                    "name": "ECCV",
                    "value": 87,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,54,154)"
                        }
                    }
                },
                {
                    "name": "ICCV",
                    "value": 86,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,157,62)"
                        }
                    }
                },
                {
                    "name": "\u5206\u5e03\u5f0f\u8bad\u7ec3",
                    "value": 85,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,114,28)"
                        }
                    }
                },
                {
                    "name": "\u591a\u6a21\u6001",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,43,19)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u76d1\u7763/\u534a\u76d1\u7763\u5b66\u4e60",
                    "value": 83,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,87,67)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u89c6\u89c9",
                    "value": 82,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,132,115)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u751f\u6210",
                    "value": 81,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,40,135)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf/\u89c6\u9891\u8bc6\u522b",
                    "value": 80,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,137,150)"
                        }
                    }
                },
                {
                    "name": "OCR",
                    "value": 79,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,129,66)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b\u538b\u7f29",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,28,38)"
                        }
                    }
                },
                {
                    "name": "SLAM",
                    "value": 77,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,15,79)"
                        }
                    }
                },
                {
                    "name": "OpenCV",
                    "value": 76,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,25,19)"
                        }
                    }
                },
                {
                    "name": "PCL",
                    "value": 75,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,40,123)"
                        }
                    }
                },
                {
                    "name": "\u5355\u76ee/\u53cc\u76ee\u6df1\u5ea6\u4f30\u8ba1",
                    "value": 74,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,33,58)"
                        }
                    }
                },
                {
                    "name": "\u76f8\u673a\u6807\u5b9a/\u914d\u51c6",
                    "value": 73,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,36,6)"
                        }
                    }
                },
                {
                    "name": "3D\u7269\u4f53\u8bc6\u522b\u4e0e\u5206\u5272",
                    "value": 72,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,140,80)"
                        }
                    }
                },
                {
                    "name": "3D\u91cd\u5efa",
                    "value": 71,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,8,108)"
                        }
                    }
                },
                {
                    "name": "Visual SLAM",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,38,23)"
                        }
                    }
                },
                {
                    "name": "SfM\u3001MVS",
                    "value": 69,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,54,31)"
                        }
                    }
                },
                {
                    "name": "\u5206\u7c7b",
                    "value": 68,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,32,157)"
                        }
                    }
                },
                {
                    "name": "\u56de\u5f52",
                    "value": 67,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,110,36)"
                        }
                    }
                },
                {
                    "name": "\u805a\u7c7b",
                    "value": 66,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,114,136)"
                        }
                    }
                },
                {
                    "name": "\u6982\u7387\u6a21\u578b",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,60,111)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5904\u7406",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,152,24)"
                        }
                    }
                },
                {
                    "name": "\u6587\u732e\u9605\u8bfb",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,151,141)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u901f\u5b66\u4e60\u80fd\u529b",
                    "value": 62,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,122,85)"
                        }
                    }
                },
                {
                    "name": "CNN",
                    "value": 61,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,107,139)"
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
        chart_068ef39b14de4f358941e7f1e4b60fa0.setOption(option_068ef39b14de4f358941e7f1e4b60fa0);
    </script>
                <div id="2a0eb8de6cc54bcd9eefdf765ff8141d" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_2a0eb8de6cc54bcd9eefdf765ff8141d = echarts.init(
            document.getElementById('2a0eb8de6cc54bcd9eefdf765ff8141d'), 'white', {renderer: 'canvas'});
            
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
    
        var option_2a0eb8de6cc54bcd9eefdf765ff8141d = {
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
                            "color": "rgb(60,1,122)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u7cfb\u7edf\u6838\u5fc3\u7b97\u6cd5\u7814\u53d1",
                    "value": 99,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,47,69)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u5174\u8da3\u5efa\u6a21",
                    "value": 98,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,66,147)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u5b9e\u65f6\u610f\u56fe\u5efa\u6a21",
                    "value": 97,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,127,88)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6316\u6398",
                    "value": 96,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,69,58)"
                        }
                    }
                },
                {
                    "name": "\u4e2a\u6027\u5316\u63a8\u8350",
                    "value": 95,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,85,6)"
                        }
                    }
                },
                {
                    "name": "\u4e2a\u6027\u5316\u63a8\u9001\u7b97\u6cd5",
                    "value": 94,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,86,22)"
                        }
                    }
                },
                {
                    "name": "\u53ec\u56de",
                    "value": 93,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,114,117)"
                        }
                    }
                },
                {
                    "name": "\u6392\u5e8f",
                    "value": 92,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,36,93)"
                        }
                    }
                },
                {
                    "name": "\u51b7\u542f\u52a8",
                    "value": 91,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,105,50)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u753b\u50cf\u4f18\u5316",
                    "value": 90,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,65,86)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u80fd\u529b\u6a21\u578b",
                    "value": 89,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,25,70)"
                        }
                    }
                },
                {
                    "name": "\u4f9b\u9700\u5173\u7cfb\u6a21\u578b",
                    "value": 88,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,119,143)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u7b56\u7565",
                    "value": 87,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,115,106)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u6d41\u63a8\u8350",
                    "value": 86,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,63,45)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350/\u641c\u7d22/\u5e7f\u544a",
                    "value": 85,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,14,63)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u63a8\u8350",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,95,106)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u8425\u9500",
                    "value": 83,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,69,156)"
                        }
                    }
                },
                {
                    "name": "feed\u6d41\u63a8\u8350\u3001\u76f8\u5173\u6027\u63a8\u8350",
                    "value": 82,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,126,51)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u8d28\u91cf\u4f53\u7cfb",
                    "value": 81,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,108,100)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u6807\u7b7e\u4f53\u7cfb",
                    "value": 80,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,63,88)"
                        }
                    }
                },
                {
                    "name": "\u4e0b\u5355\u9884\u4f30",
                    "value": 79,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,127,63)"
                        }
                    }
                },
                {
                    "name": "\u767e\u5ea6",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,33,56)"
                        }
                    }
                },
                {
                    "name": "\u6dd8\u5b9d",
                    "value": 77,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,48,129)"
                        }
                    }
                },
                {
                    "name": "\u5b57\u8282\u8df3\u52a8",
                    "value": 76,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,34,93)"
                        }
                    }
                },
                {
                    "name": "\u6296\u97f3",
                    "value": 75,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,85,6)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u624b",
                    "value": 74,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,141,150)"
                        }
                    }
                },
                {
                    "name": "\u4eac\u4e1c",
                    "value": 73,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,18,87)"
                        }
                    }
                },
                {
                    "name": "\u7ebf\u4e0a\u6392\u5e8f\u7cfb\u7edf",
                    "value": 72,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,152,81)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u95fb\u63a8\u8350",
                    "value": 71,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,110,51)"
                        }
                    }
                },
                {
                    "name": "\u957f\u77ed\u671f\u753b\u50cf",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,156,36)"
                        }
                    }
                },
                {
                    "name": "query\u7406\u89e3",
                    "value": 69,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,56,147)"
                        }
                    }
                },
                {
                    "name": "query\u76f8\u5173\u63a8\u8350",
                    "value": 68,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,98,153)"
                        }
                    }
                },
                {
                    "name": "\u6d41\u91cf\u4f18\u5316",
                    "value": 67,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,147,101)"
                        }
                    }
                },
                {
                    "name": "\u5546\u4e1a\u5316",
                    "value": 66,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,144,0)"
                        }
                    }
                },
                {
                    "name": "\u6d88\u8d39\u65f6\u957f",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,103,73)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u7559\u5b58",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,128,28)"
                        }
                    }
                },
                {
                    "name": "\u505c\u7559\u65f6\u957f\u4f18\u5316",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,110,1)"
                        }
                    }
                },
                {
                    "name": "\u70b9\u51fb\u7387\u4f18\u5316",
                    "value": 62,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,16,86)"
                        }
                    }
                },
                {
                    "name": "\u7559\u5b58\u7387\u4f18\u5316",
                    "value": 61,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,150,46)"
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
        chart_2a0eb8de6cc54bcd9eefdf765ff8141d.setOption(option_2a0eb8de6cc54bcd9eefdf765ff8141d);
    </script>
                <div id="bb90e206890840b09465eb5f6cabef04" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_bb90e206890840b09465eb5f6cabef04 = echarts.init(
            document.getElementById('bb90e206890840b09465eb5f6cabef04'), 'white', {renderer: 'canvas'});
            
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
    
        var option_bb90e206890840b09465eb5f6cabef04 = {
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
                            "color": "rgb(22,81,27)"
                        }
                    }
                },
                {
                    "name": "Tensorflow",
                    "value": 99,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,45,145)"
                        }
                    }
                },
                {
                    "name": "PyTorch",
                    "value": 98,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,121,104)"
                        }
                    }
                },
                {
                    "name": "\u534f\u540c\u8fc7\u6ee4",
                    "value": 97,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,37,72)"
                        }
                    }
                },
                {
                    "name": "FM",
                    "value": 96,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,42,11)"
                        }
                    }
                },
                {
                    "name": "LR",
                    "value": 95,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,83,53)"
                        }
                    }
                },
                {
                    "name": "NN",
                    "value": 94,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,19,21)"
                        }
                    }
                },
                {
                    "name": "LSTM",
                    "value": 93,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,92,16)"
                        }
                    }
                },
                {
                    "name": "GBDT",
                    "value": 92,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,108,78)"
                        }
                    }
                },
                {
                    "name": "C/C++",
                    "value": 91,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,134,33)"
                        }
                    }
                },
                {
                    "name": "Python",
                    "value": 90,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,154,117)"
                        }
                    }
                },
                {
                    "name": "Java",
                    "value": 89,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,84,52)"
                        }
                    }
                },
                {
                    "name": "Hadoop",
                    "value": 88,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,36,54)"
                        }
                    }
                },
                {
                    "name": "Spark",
                    "value": 87,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,27,91)"
                        }
                    }
                },
                {
                    "name": "Storm",
                    "value": 86,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,140,60)"
                        }
                    }
                },
                {
                    "name": "CTR\u9884\u4f30",
                    "value": 85,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,53,148)"
                        }
                    }
                },
                {
                    "name": "xgboost",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,118,125)"
                        }
                    }
                },
                {
                    "name": "lightgbm",
                    "value": 83,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,128,16)"
                        }
                    }
                },
                {
                    "name": "catboost",
                    "value": 82,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,159,51)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u6216\u641c\u7d22\u76f8\u5173\u7ecf\u9a8c",
                    "value": 81,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,55,42)"
                        }
                    }
                },
                {
                    "name": "\u53ec\u56de/\u6392\u5e8f\u7b97\u6cd5",
                    "value": 80,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,118,100)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60",
                    "value": 79,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,135,72)"
                        }
                    }
                },
                {
                    "name": "\u5f3a\u5316\u5b66\u4e60",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,158,97)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u70b9\u51fb\u7387\u9884\u4f30",
                    "value": 77,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,58,102)"
                        }
                    }
                },
                {
                    "name": "\u4e2a\u6027\u5316\u63a8\u8350\u6a21\u578b",
                    "value": 76,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,155,154)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u6392\u5e8f",
                    "value": 75,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,19,23)"
                        }
                    }
                },
                {
                    "name": "LearningToRank",
                    "value": 74,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,103,56)"
                        }
                    }
                },
                {
                    "name": "word2vec",
                    "value": 73,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,24,124)"
                        }
                    }
                },
                {
                    "name": "RecSys",
                    "value": 72,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,23,82)"
                        }
                    }
                },
                {
                    "name": "SIGIR",
                    "value": 71,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,141,11)"
                        }
                    }
                },
                {
                    "name": "WWW",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,37,51)"
                        }
                    }
                },
                {
                    "name": "ICML",
                    "value": 69,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,129,125)"
                        }
                    }
                },
                {
                    "name": "NIPS",
                    "value": 68,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,76,10)"
                        }
                    }
                },
                {
                    "name": "\u70b9\u51fb\u7387\u9884\u4f30",
                    "value": 67,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,4,92)"
                        }
                    }
                },
                {
                    "name": "\u6295\u9012\u9884\u4f30",
                    "value": 66,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,56,57)"
                        }
                    }
                },
                {
                    "name": "\u9884\u7b97\u5efa\u8bae",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,158,114)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u4ef7\u673a\u5236",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,21,79)"
                        }
                    }
                },
                {
                    "name": "\u5206\u5e03\u5f0f\u8ba1\u7b97",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,127,18)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u5854\u6a21\u578b",
                    "value": 62,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,144,83)"
                        }
                    }
                },
                {
                    "name": "\u7279\u5f81\u5de5\u7a0b",
                    "value": 61,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,72,139)"
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
        chart_bb90e206890840b09465eb5f6cabef04.setOption(option_bb90e206890840b09465eb5f6cabef04);
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
