---
title: 算法招聘_公司与业务分析
---



<html>
<head>
    <meta charset="UTF-8">
    <title>Awesome-pyecharts</title>
            <script type="text/javascript" src="https://assets.pyecharts.org/assets/echarts.min.js"></script>
        <script type="text/javascript" src="https://assets.pyecharts.org/assets/echarts-wordcloud.min.js"></script>
        <script type="text/javascript" src="https://assets.pyecharts.org/assets/maps/china.js"></script>

    

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

<h2>（2021-05-15更新）</h2>

<h2>点击按钮查看招聘数据分析详情</h2>
    
<a href="https://showmeai-hub.github.io/2021/05/13/job_data_anlysis.html">
    <button class="button">看薪资</button>
</a>
<a href="https://showmeai-hub.github.io/2021/05/13/job_anlysis_company.html">
    <button class="button">看公司</button>
</a>
<a href="https://showmeai-hub.github.io/2021/05/13/job_anlysis_skills.html">
    <button class="button">看要求</button>
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
            <button class="tablinks" onclick="showChart(event, '0a5fa73bce8f462989d7ceed666c5517')">公司</button>
            <button class="tablinks" onclick="showChart(event, 'c8a0b07252c947459567ed40faea9381')">城市</button>
            <button class="tablinks" onclick="showChart(event, '8122d9105840413ba9435a16c7c63f1b')">城市占比</button>
            <button class="tablinks" onclick="showChart(event, '5d8b6e60e21f4bfe8948bbbbd2add75b')">招聘地图</button>
            <button class="tablinks" onclick="showChart(event, '3ce48f09c9714c1d9a704c42c2423404')">区域</button>
            <button class="tablinks" onclick="showChart(event, '94ba5219eb84465188efe2a54c0e87f1')">区域占比</button>
            <button class="tablinks" onclick="showChart(event, 'ef66dffff7f444ef9306782c92d2be65')">公司规模</button>
            <button class="tablinks" onclick="showChart(event, '9e057d9f60944db9b9782ccee28090dd')">人员规模</button>
            <button class="tablinks" onclick="showChart(event, '8e1b97b4ac3c4d2eb1ffeca243937b4f')">行业</button>
            <button class="tablinks" onclick="showChart(event, 'e90296e156434267af332b558f71c03d')">招聘方向</button>
            <button class="tablinks" onclick="showChart(event, 'c8ef1fb9cfe447dbb6a3c3b4d49f723f')">公司福利</button>
    </div>

    <div class="box">
                <div id="0a5fa73bce8f462989d7ceed666c5517" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_0a5fa73bce8f462989d7ceed666c5517 = echarts.init(
            document.getElementById('0a5fa73bce8f462989d7ceed666c5517'), 'white', {renderer: 'canvas'});
            
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
    
        var option_0a5fa73bce8f462989d7ceed666c5517 = {
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
                31,
                21,
                20,
                13,
                13,
                12,
                12,
                10,
                10,
                9
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
            "name": "\u516c\u53f8\u5206\u5e03",
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
                    "name": "\u7f8e\u56e2",
                    "value": 31,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,3,139)"
                        }
                    }
                },
                {
                    "name": "\u4eac\u4e1c\u96c6\u56e2",
                    "value": 21,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,83,115)"
                        }
                    }
                },
                {
                    "name": "\u5b57\u8282\u8df3\u52a8",
                    "value": 20,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,2,68)"
                        }
                    }
                },
                {
                    "name": "\u6ef4\u6ef4",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,36,136)"
                        }
                    }
                },
                {
                    "name": "\u7231\u5947\u827a",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,106,113)"
                        }
                    }
                },
                {
                    "name": "\u4eac\u4e1c\u7269\u6d41",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,90,105)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u624b",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,27,154)"
                        }
                    }
                },
                {
                    "name": "\u5357\u6e56\u9662",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,87,3)"
                        }
                    }
                },
                {
                    "name": "OPPO",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,17,139)"
                        }
                    }
                },
                {
                    "name": "\u6167\u5b89\u91d1\u79d1",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,116,38)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u78c1\u77f3",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,42,57)"
                        }
                    }
                },
                {
                    "name": "\u4e07\u79d1",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,3,146)"
                        }
                    }
                },
                {
                    "name": "Versa",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,128,44)"
                        }
                    }
                },
                {
                    "name": "\u8682\u8681\u96c6\u56e2",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,17,35)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u67d4\u521b\u65b0",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,10,153)"
                        }
                    }
                },
                {
                    "name": "\u8d5b\u76ee\u79d1\u6280",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,2,41)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u6d6a\u7f51",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,39,119)"
                        }
                    }
                },
                {
                    "name": "\u777f\u8d44\u8fbe",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,98,15)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u6613",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,46,73)"
                        }
                    }
                },
                {
                    "name": "\u5546\u6c64\u79d1\u6280",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,50,131)"
                        }
                    }
                },
                {
                    "name": "\u730e\u6237\u661f\u7a7a",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,12,93)"
                        }
                    }
                },
                {
                    "name": "\u76c8\u5609\u4e92\u8054",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,138,127)"
                        }
                    }
                },
                {
                    "name": "\u4f5c\u4e1a\u5e2e",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,119,71)"
                        }
                    }
                },
                {
                    "name": "\u767e\u5ea6",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,113,91)"
                        }
                    }
                },
                {
                    "name": "\u5faa\u73af\u667a\u80fd",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,28,131)"
                        }
                    }
                },
                {
                    "name": "\u667a\u62d3\u89c6\u754c",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,113,156)"
                        }
                    }
                },
                {
                    "name": "Shopee",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,57,19)"
                        }
                    }
                },
                {
                    "name": "\u9177\u5bb6\u4e50",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,109,97)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77\u6cdb\u89c6\u89d2",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,27,93)"
                        }
                    }
                },
                {
                    "name": "\u4eac\u4e1c\u79d1\u6280",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,25,74)"
                        }
                    }
                },
                {
                    "name": "\u597d\u672a\u6765",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,52,34)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u5e02\u6bd4\u4e00\u6bd4\u7f51\u7edc\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,47,91)"
                        }
                    }
                },
                {
                    "name": "Gostudy",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,37,53)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u4eba\u5bff",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,91,56)"
                        }
                    }
                },
                {
                    "name": "\u8c31\u65f6\u660a\u552f\u6570\u636e",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,48,87)"
                        }
                    }
                },
                {
                    "name": "\u6ee1\u5e2e\u96c6\u56e2",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,92,34)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u51b0",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,153,115)"
                        }
                    }
                },
                {
                    "name": "\u5fc5\u793a\u79d1\u6280",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,115,34)"
                        }
                    }
                },
                {
                    "name": "\u6566\u714c\u7f51",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,134,43)"
                        }
                    }
                },
                {
                    "name": "360",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,19,30)"
                        }
                    }
                },
                {
                    "name": "\u8d1d\u58f3",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,43,113)"
                        }
                    }
                },
                {
                    "name": "\u706b\u773c\u4e91",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,11,51)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u5929\u52b1\u98de",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,81,78)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5c1a\u79d1\u6280",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,70,99)"
                        }
                    }
                },
                {
                    "name": "360os",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,128,84)"
                        }
                    }
                },
                {
                    "name": "Insta360\u5f71\u77f3",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,148,137)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u56fe\u79d1\u6280",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,105,81)"
                        }
                    }
                },
                {
                    "name": "\u827e\u8015\u79d1\u6280",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,143,7)"
                        }
                    }
                },
                {
                    "name": "\u8c10\u76df\u673a\u5668\u4eba",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,17,75)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77\u6c38\u8f89\u8d85\u5e02\u6709\u9650\u516c\u53f8",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,0,55)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u89c6\u521b\u65b0",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,6,70)"
                        }
                    }
                },
                {
                    "name": "PowerVision",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,34,25)"
                        }
                    }
                },
                {
                    "name": "\u89e6\u5b9d",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,14,49)"
                        }
                    }
                },
                {
                    "name": "\u5600\u55d2\u51fa\u884c",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,70,47)"
                        }
                    }
                },
                {
                    "name": "\u597d\u5927\u592b\u5728\u7ebf",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,53,13)"
                        }
                    }
                },
                {
                    "name": "\u5cb1\u609f\u667a\u80fd",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,79,100)"
                        }
                    }
                },
                {
                    "name": "\u6570\u5764\u79d1\u6280",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,43,126)"
                        }
                    }
                },
                {
                    "name": "\u5f97\u7269App",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,150,60)"
                        }
                    }
                },
                {
                    "name": "\u5927\u540d\u8f6f\u4ef6",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,108,31)"
                        }
                    }
                },
                {
                    "name": "Yeahmobi",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,13,157)"
                        }
                    }
                },
                {
                    "name": "westwell\u897f\u4e95\u79d1\u6280",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,58,60)"
                        }
                    }
                },
                {
                    "name": "\u6700\u53f3",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,126,158)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u6052\u4fe1\u606f",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,160,115)"
                        }
                    }
                },
                {
                    "name": "\u6d4b\u6d4b",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,29,11)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u5b8f\u74f4\u79d1\u6280\u53d1\u5c55\u6709\u9650...",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,10,38)"
                        }
                    }
                },
                {
                    "name": "ZOOM",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,25,56)"
                        }
                    }
                },
                {
                    "name": "MINIEYE",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,55,85)"
                        }
                    }
                },
                {
                    "name": "\u9605\u6587\u96c6\u56e2",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,103,11)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u5982\u79c4",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,33,75)"
                        }
                    }
                },
                {
                    "name": "GYENNO",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,42,105)"
                        }
                    }
                },
                {
                    "name": "\u5929\u773c\u67e5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,135,75)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e4b\u6613",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,150,7)"
                        }
                    }
                },
                {
                    "name": "Soul",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,24,137)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u533b\u7597",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,125,132)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u7bc7",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,64,102)"
                        }
                    }
                },
                {
                    "name": "\u89c2\u8fdc\u6570\u636e",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,41,47)"
                        }
                    }
                },
                {
                    "name": "\u6d3e\u5ba2\u6734\u98df",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,116,156)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u7586\u667a\u80fd",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,46,63)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u4e1c\u4e09\u7ef4\u5bb6\u4fe1\u606f\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,79,21)"
                        }
                    }
                },
                {
                    "name": "\u65f7\u89c6MEGVII",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,86,153)"
                        }
                    }
                },
                {
                    "name": "\u54d4\u54e9\u54d4\u54e9",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,49,135)"
                        }
                    }
                },
                {
                    "name": "\u84dd\u9e3d\u96c6\u56e2",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,121,98)"
                        }
                    }
                },
                {
                    "name": "\u534e\u4e3a\u6280\u672f\u6709\u9650\u516c\u53f8",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,44,91)"
                        }
                    }
                },
                {
                    "name": "\u57c3\u514b\u65af\u5de5\u4e1a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,127,149)"
                        }
                    }
                },
                {
                    "name": "\u5151\u5427",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,85,38)"
                        }
                    }
                },
                {
                    "name": "\u5143\u6a61\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,66,17)"
                        }
                    }
                },
                {
                    "name": "\u957f\u5730\u4e07\u65b9",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,42,107)"
                        }
                    }
                },
                {
                    "name": "\u8da3\u5934\u6761",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,27,47)"
                        }
                    }
                },
                {
                    "name": "\u71e7\u4eba\u533b\u7597",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,50,110)"
                        }
                    }
                },
                {
                    "name": "\u8fc5\u6e38\u7f51\u7edc",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,27,86)"
                        }
                    }
                },
                {
                    "name": "\u6781\u5149",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,52,117)"
                        }
                    }
                },
                {
                    "name": "\u56db\u5408\u5929\u5730",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,3,124)"
                        }
                    }
                },
                {
                    "name": "\u7ea2\u661f\u7f8e\u51ef\u9f99",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,14,97)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u6da6\u5bcc\u8054",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,157,49)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u9c7c\u6613\u8fde",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,40,19)"
                        }
                    }
                },
                {
                    "name": "\u9646\u91d1\u6240",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,116,72)"
                        }
                    }
                },
                {
                    "name": "\u8304\u5b50\u5feb\u4f20",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,99,93)"
                        }
                    }
                },
                {
                    "name": "\u5f71\u521b\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,129,16)"
                        }
                    }
                },
                {
                    "name": "EM3",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,59,8)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u8111\u94f6\u6cb3",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,20,127)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6167\u82bd",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,42,94)"
                        }
                    }
                },
                {
                    "name": "Keep",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,78,63)"
                        }
                    }
                },
                {
                    "name": "\u79fb\u52a8\u7814\u7a76\u9662",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,45,5)"
                        }
                    }
                },
                {
                    "name": "\u643a\u7a0b\u96c6\u56e2",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,128,151)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u72d7\u6253\u8f66",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,156,35)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u601d\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,109,142)"
                        }
                    }
                },
                {
                    "name": "\u5e03\u5c14\u827a\u6570",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,106,12)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u62cd\u5802",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,51,23)"
                        }
                    }
                },
                {
                    "name": "\u4ebf\u8058\u4e16\u7eaa",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,25,26)"
                        }
                    }
                },
                {
                    "name": "CraiditX",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,4,133)"
                        }
                    }
                },
                {
                    "name": "\u8f7b\u821f\u667a\u822a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,9,72)"
                        }
                    }
                },
                {
                    "name": "\u8fbe\u89c2\u6570\u636e",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,98,109)"
                        }
                    }
                },
                {
                    "name": "AKULAKU",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,89,102)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u77e5\u672a\u6765",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,24,48)"
                        }
                    }
                },
                {
                    "name": "\u8d27\u62c9\u62c9",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,50,85)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,61,69)"
                        }
                    }
                },
                {
                    "name": "\u8ff7\u9e7f\u97f3\u4e50",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,79,147)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77\u835f\u529b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,113,14)"
                        }
                    }
                },
                {
                    "name": "Long Bridge",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,60,91)"
                        }
                    }
                },
                {
                    "name": "\u9177\u72d7\u97f3\u4e50",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,131,2)"
                        }
                    }
                },
                {
                    "name": "\u601d\u8d24\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,17,50)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u5c71\u4e16\u6e38",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,20,8)"
                        }
                    }
                },
                {
                    "name": "\u7ecf\u4f20\u591a\u8d62",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,135,135)"
                        }
                    }
                },
                {
                    "name": "\u9cb8\u822a\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,5,20)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u8bc1\u4f18\u667a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,114,152)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u8054\u82f1\u8bed",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,143,95)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u80fd\u534e\u667a\u80fd\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,137,62)"
                        }
                    }
                },
                {
                    "name": "\u8054\u4ec1\u5065\u5eb7\u533b\u7597\u5927\u6570\u636e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,56,133)"
                        }
                    }
                },
                {
                    "name": "\u667a\u610f\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,91,86)"
                        }
                    }
                },
                {
                    "name": "\u63a2\u77e5\u6570\u636e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,117,37)"
                        }
                    }
                },
                {
                    "name": "\u6ef4\u666e\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,84,119)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77\u4e92\u6559\u6559\u80b2\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,82,38)"
                        }
                    }
                },
                {
                    "name": "\u72ee\u6865\u96c6\u56e2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,76,98)"
                        }
                    }
                },
                {
                    "name": "\u8f66\u597d\u591a\u96c6\u56e2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,152,120)"
                        }
                    }
                },
                {
                    "name": "\u6613\u6d41",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,113,123)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u5dde\u5c0f\u8fc8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,39,116)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u601d\u7586",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,117,44)"
                        }
                    }
                },
                {
                    "name": "\u6709\u4e3a\u4fe1\u606f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,104,94)"
                        }
                    }
                },
                {
                    "name": "\u9f99\u6e56\u96c6\u56e2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,77,150)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u90ae\u4fe1\u606f\u79d1\u6280\uff08\u5317\u4eac\uff09\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,48,98)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u56fd\u90ae\u653f\u50a8\u84c4\u94f6\u884c",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,75,119)"
                        }
                    }
                },
                {
                    "name": "\u949b\u6c2a\u65b0\u5a92\u4f53\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,67,158)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u5dde\u9ed1\u683c\u667a\u9020\u4fe1\u606f\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,87,62)"
                        }
                    }
                },
                {
                    "name": "\u5929\u6e90\u8fea\u79d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,147,138)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u4ed5\u5bfb\u4eba\u529b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,67,23)"
                        }
                    }
                },
                {
                    "name": "\u5706\u901a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,117,9)"
                        }
                    }
                },
                {
                    "name": "\u5f71\u7b11\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,151,69)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u56fd\u79d1\u5b66\u9662\u7535\u5b50\u5b66\u7814\u7a76\u6240\u82cf\u5dde\u7814\u7a76\u9662",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,25,86)"
                        }
                    }
                },
                {
                    "name": "\u661f\u836f\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,82,58)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u5065\u5eb7",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,86,108)"
                        }
                    }
                },
                {
                    "name": "\u4ebf\u5496\u901a\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,7,134)"
                        }
                    }
                },
                {
                    "name": "Walmart China",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,122,79)"
                        }
                    }
                },
                {
                    "name": "FunPlus \u8da3\u52a0\u6e38\u620f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,127,56)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u7684\u96c6\u56e2IT",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,59,85)"
                        }
                    }
                },
                {
                    "name": "\u8d27\u7279\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,53,151)"
                        }
                    }
                },
                {
                    "name": "\u873b\u8713FM",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,96,102)"
                        }
                    }
                },
                {
                    "name": "roobo",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,28,46)"
                        }
                    }
                },
                {
                    "name": "\u9053\u9053",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,17,45)"
                        }
                    }
                },
                {
                    "name": "\u5fb7\u9002\u751f\u7269",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,153,34)"
                        }
                    }
                },
                {
                    "name": "\u6709\u4e2a\u673a\u5668\u4eba",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,96,92)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u6cf0\u661f\u4e91",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,55,60)"
                        }
                    }
                },
                {
                    "name": "\u8da3\u4e38",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,105,126)"
                        }
                    }
                },
                {
                    "name": "\u8de8\u8d8a\u901f\u8fd0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,123,51)"
                        }
                    }
                },
                {
                    "name": "\u4e3a\u534e\u7f51\u7edc",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,78,141)"
                        }
                    }
                },
                {
                    "name": "\u8bfa\u5a01\u534e\u4ed5\u7ba1\u7406\u54a8\u8be2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,73,81)"
                        }
                    }
                },
                {
                    "name": "\u4e50\u6211\u65e0\u9650",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,32,27)"
                        }
                    }
                },
                {
                    "name": "\u9053\u8fbe\u5929\u9645",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,87,45)"
                        }
                    }
                },
                {
                    "name": "\u82f1\u8bed\u8da3\u914d\u97f3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,122,39)"
                        }
                    }
                },
                {
                    "name": "Convert lab",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,62,85)"
                        }
                    }
                },
                {
                    "name": "\u8389\u8389\u4e1d\u6e38\u620f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,40,146)"
                        }
                    }
                },
                {
                    "name": "\u54d7\u5566\u5566",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,25,153)"
                        }
                    }
                },
                {
                    "name": "\u676d\u5dde\u9886\u89c1\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,22,72)"
                        }
                    }
                },
                {
                    "name": "\u7ffc\u9e25\u6559\u80b2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,22,52)"
                        }
                    }
                },
                {
                    "name": "\u8f6c\u8f6c",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,34,55)"
                        }
                    }
                },
                {
                    "name": "TalkingData",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,145,66)"
                        }
                    }
                },
                {
                    "name": "\u5bbd\u5f85\u4e92\u8054\u7f51",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,23,42)"
                        }
                    }
                },
                {
                    "name": "\u777f\u9b54\u667a\u80fd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,64,54)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u4ea7\u9669",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,124,115)"
                        }
                    }
                },
                {
                    "name": "\u5343\u5de1\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,78,122)"
                        }
                    }
                },
                {
                    "name": "\u5965\u6bd4\u4e2d\u5149",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,119,124)"
                        }
                    }
                },
                {
                    "name": "\u817e\u5c55\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,40,17)"
                        }
                    }
                },
                {
                    "name": "\u6bb7\u56fe\u7f51\u8054",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,35,159)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u5a31\u65f6\u5149",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,128,61)"
                        }
                    }
                },
                {
                    "name": "\u7279\u8d5e|Tezign",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,107,32)"
                        }
                    }
                },
                {
                    "name": "TCL",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,81,159)"
                        }
                    }
                },
                {
                    "name": "\u548c\u4fe1\u5eb7",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,31,47)"
                        }
                    }
                },
                {
                    "name": "\u864e\u7259\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,153,30)"
                        }
                    }
                },
                {
                    "name": "\u661f\u8206\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,33,149)"
                        }
                    }
                },
                {
                    "name": "\u7269\u754c\uff08\u4e0a\u6d77\uff09\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,106,21)"
                        }
                    }
                },
                {
                    "name": "\u5b8f\u5251\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,18,108)"
                        }
                    }
                },
                {
                    "name": "\u641c\u72d7",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,131,106)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u5e02\u6709\u4f20\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,25,154)"
                        }
                    }
                },
                {
                    "name": "\u6807\u8d1d\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,149,0)"
                        }
                    }
                },
                {
                    "name": "\u5927\u9a90\u6570\u636e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,118,112)"
                        }
                    }
                },
                {
                    "name": "\u7693\u884c\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,53,31)"
                        }
                    }
                },
                {
                    "name": "\u521b\u6cf0\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,27,5)"
                        }
                    }
                },
                {
                    "name": "\u6253\u9020\u6700\u597d\u7684\u5728\u7ebf\u4eba\u8138\u8bc6\u522b\u5f15\u64ce",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,18,156)"
                        }
                    }
                },
                {
                    "name": "\u8611\u83c7\u8857",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,42,119)"
                        }
                    }
                },
                {
                    "name": "\u6c34\u6ef4 WATERDROP INC",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,7,63)"
                        }
                    }
                },
                {
                    "name": "\u4f73\u987a\u667a\u80fd\u673a\u5668\u4eba",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,141,69)"
                        }
                    }
                },
                {
                    "name": "\u6749\u6570\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,120,46)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u4e50\u79cd\u5b50",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,71,20)"
                        }
                    }
                },
                {
                    "name": "\u665f\u89c6\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,0,75)"
                        }
                    }
                },
                {
                    "name": "\u817e\u8baf",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,107,38)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u5c71\u529e\u516c\u8f6f\u4ef6",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,145,148)"
                        }
                    }
                },
                {
                    "name": "MetaApp",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,106,72)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u7535\u6167\u5b89",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,28,158)"
                        }
                    }
                },
                {
                    "name": "\u7279\u9e4f\u7f51\u7edc",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,11,158)"
                        }
                    }
                },
                {
                    "name": "\u51fa\u95e8\u95ee\u95ee",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,60,71)"
                        }
                    }
                },
                {
                    "name": "\u8054\u5408\u96c6\u56e2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,18,132)"
                        }
                    }
                },
                {
                    "name": "\u89c5\u777f\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,59,1)"
                        }
                    }
                },
                {
                    "name": "\u6700\u6709\u6599",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,65,145)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u79d8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,62,124)"
                        }
                    }
                },
                {
                    "name": "Disney+Hotstar",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,133,17)"
                        }
                    }
                },
                {
                    "name": "\u667a\u52a0\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,69,66)"
                        }
                    }
                },
                {
                    "name": "\u9489\u9489",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,76,94)"
                        }
                    }
                },
                {
                    "name": "\u676d\u5dde\u667a\u56e2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,101,69)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u6df1\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,47,45)"
                        }
                    }
                },
                {
                    "name": "YY",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,59,10)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u4ed3\u667a\u80fd\u4ed3\u50a8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,23,121)"
                        }
                    }
                },
                {
                    "name": "\u6167\u62e9\u7f51",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,160,100)"
                        }
                    }
                },
                {
                    "name": "\u4f34\u9c7c",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,17,118)"
                        }
                    }
                },
                {
                    "name": "\u6b66\u6c49\u7269\u6613\u4e91\u901a\u7f51\u7edc\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,94,64)"
                        }
                    }
                },
                {
                    "name": "\u8bc1\u901a\u80a1\u4efd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,19,15)"
                        }
                    }
                },
                {
                    "name": "\u5f71\u8c31\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,44,47)"
                        }
                    }
                },
                {
                    "name": "BLUE",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,63,99)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e91\u667a\u80fd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,122,54)"
                        }
                    }
                },
                {
                    "name": "Aibee",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,85,84)"
                        }
                    }
                },
                {
                    "name": "\u58a8\u4e91\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,38,68)"
                        }
                    }
                },
                {
                    "name": "\u7d2b\u5149\u534e\u667a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,103,158)"
                        }
                    }
                },
                {
                    "name": "\u95ea\u9a6c\u667a\u80fd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,80,37)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u7814\u7f51",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,138,101)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u5965\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,25,33)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u56fe\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,15,74)"
                        }
                    }
                },
                {
                    "name": "\u5fb7\u777f\u667a\u836f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,64,112)"
                        }
                    }
                },
                {
                    "name": "\u672a\u6765\u79d1\u6280\u57ce",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,40,115)"
                        }
                    }
                },
                {
                    "name": "\u6c83\u98de\u957f\u7a7a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,160,158)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u77e5\u667a\u80fd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,60,141)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u5c45\u5ba2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,15,144)"
                        }
                    }
                },
                {
                    "name": "\u533b\u836f\u9b54\u65b9",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,54,93)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u6e90\u6052\u9645",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,136,144)"
                        }
                    }
                },
                {
                    "name": "\u6d41\u5229\u8bf4\u00ae",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,83,4)"
                        }
                    }
                },
                {
                    "name": "\u666e\u6e21\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,156,62)"
                        }
                    }
                },
                {
                    "name": "\u6765\u672a\u6765",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,96,111)"
                        }
                    }
                },
                {
                    "name": "\u521b\u90bb\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,68,41)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u4fe1\u65f6\u4ee3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,32,98)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u58f0\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,117,53)"
                        }
                    }
                },
                {
                    "name": "\u6cfd\u97f6\u667a\u80fd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,4,37)"
                        }
                    }
                },
                {
                    "name": "\u534e\u98de\u6570\u636e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,6,123)"
                        }
                    }
                },
                {
                    "name": "Moka",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,109,17)"
                        }
                    }
                },
                {
                    "name": "\u91cd\u5e86\u957f\u5b89\u6c7d\u8f66\u8f6f\u4ef6\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,28,150)"
                        }
                    }
                },
                {
                    "name": "\u767e\u878d\u4e91\u521b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,112,118)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u60f3\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,63,14)"
                        }
                    }
                },
                {
                    "name": "\u6d6a\u6dd8\u91d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,126,99)"
                        }
                    }
                },
                {
                    "name": "\u77e9\u9635\u5143",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,17,148)"
                        }
                    }
                },
                {
                    "name": "\u900f\u5f7b\u5f71\u50cf",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,96,46)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5965\u7279\u89c6\u9891",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,20,145)"
                        }
                    }
                },
                {
                    "name": "\u733f\u8f85\u5bfc",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,34,101)"
                        }
                    }
                },
                {
                    "name": "\u8da3\u94fe\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,130,126)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u5168\u751f\u4ea7\u79d1\u5b66\u7814\u7a76\u9662",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,17,63)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u627f\u6cf0\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,101,61)"
                        }
                    }
                },
                {
                    "name": "\u4f73\u5146\u4e1a\u6295\u8d44\u54a8\u8be2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,71,55)"
                        }
                    }
                },
                {
                    "name": "\u957f\u6295\u5b66\u5802",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,50,69)"
                        }
                    }
                },
                {
                    "name": "\u5e93\u73c0\u6052\u5b89",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,140,108)"
                        }
                    }
                },
                {
                    "name": "\u8054\u901a\uff08\u5e7f\u4e1c\uff09\u4ea7\u4e1a\u4e92\u8054\u7f51...",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,36,115)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u805a\u672a\u6765",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,98,63)"
                        }
                    }
                },
                {
                    "name": "\u536b\u74f4\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,71,39)"
                        }
                    }
                },
                {
                    "name": "\u5927\u519c\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,134,11)"
                        }
                    }
                },
                {
                    "name": "\u90a3\u4e0e\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,68,118)"
                        }
                    }
                },
                {
                    "name": "\u8fc8\u6da6\u667a\u80fd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,18,87)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u539f\u6d88\u8d39\u91d1\u878d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,83,12)"
                        }
                    }
                },
                {
                    "name": "\u6c5f\u884c\u667a\u80fd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,31,41)"
                        }
                    }
                },
                {
                    "name": "\u9014\u864e\u517b\u8f66",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,156,7)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u4ea7360",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,134,25)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u597d\u5b66",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,64,136)"
                        }
                    }
                },
                {
                    "name": "\u6210\u90fd\u62df\u5408\u672a\u6765\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,132,83)"
                        }
                    }
                },
                {
                    "name": "\u7d2b\u5149\u6559\u80b2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,48,40)"
                        }
                    }
                },
                {
                    "name": "\u4eb2\u5b9d\u5b9d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,120,45)"
                        }
                    }
                },
                {
                    "name": "LAYABOX",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,14,115)"
                        }
                    }
                },
                {
                    "name": "\u6cf0\u5766\u667a\u6167",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,77,93)"
                        }
                    }
                },
                {
                    "name": "\u827e\u7f8e\u7f51\u7edc\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,45,12)"
                        }
                    }
                },
                {
                    "name": "\u661f\u71b9\u5143\u6295\u8d44\u7ba1\u7406",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,126,13)"
                        }
                    }
                },
                {
                    "name": "\u9890\u90a6\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,39,73)"
                        }
                    }
                },
                {
                    "name": "\u6885\u5361\u66fc\u5fb7",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,137,92)"
                        }
                    }
                },
                {
                    "name": "\u84dd\u6e56",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,4,160)"
                        }
                    }
                },
                {
                    "name": "\u8fc1\u79fb\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,71,132)"
                        }
                    }
                },
                {
                    "name": "\u53ca\u672a\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,24,24)"
                        }
                    }
                },
                {
                    "name": "\u4f2f\u6069\u5149\u5b66",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,158,120)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u65b9\u56fd\u4fe1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,133,88)"
                        }
                    }
                },
                {
                    "name": "\u8206\u9686\u5174\u8fbe",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,127,134)"
                        }
                    }
                },
                {
                    "name": "\u7075\u52a8\u97f3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,8,118)"
                        }
                    }
                },
                {
                    "name": "\u534e\u91cc\u7f51\u7edc",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,66,128)"
                        }
                    }
                },
                {
                    "name": "\u795e\u7b56\u6570\u636e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,116,110)"
                        }
                    }
                },
                {
                    "name": "Momenta",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,2,116)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u8d4b\u667a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,89,131)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u64ad\u7535\u89c6\u7814\u7a76\u6240",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,43,95)"
                        }
                    }
                },
                {
                    "name": "\u9752\u5c9b\u5e03\u9c81\u514b\u65af\u4e50\u5668\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,63,113)"
                        }
                    }
                },
                {
                    "name": "\u5229\u57fa\u4e07\u5546\u52a1\u4fe1\u606f\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,119,73)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u770b\u80a1\u4efd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,31,132)"
                        }
                    }
                },
                {
                    "name": "\u6210\u90fd\u8086\u96f6\u8086",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,95,150)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u91cf\u8d28\u5b50",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,25,120)"
                        }
                    }
                },
                {
                    "name": "\u53f8\u5357\u6570\u636e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,128,86)"
                        }
                    }
                },
                {
                    "name": "\u60e0\u6bcf\u4e91\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,2,35)"
                        }
                    }
                },
                {
                    "name": "\u5929\u6cfd\u667a\u4e91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,39,86)"
                        }
                    }
                },
                {
                    "name": "\u9b54\u7b77\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,81,59)"
                        }
                    }
                },
                {
                    "name": "\u5fc3\u5a31\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,48,18)"
                        }
                    }
                },
                {
                    "name": "DataEye",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,93,154)"
                        }
                    }
                },
                {
                    "name": "\u745e\u8fb0\u660c\u9686",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,116,4)"
                        }
                    }
                },
                {
                    "name": "\u84dd\u6df1\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,6,18)"
                        }
                    }
                },
                {
                    "name": "\u533b\u767e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,122,106)"
                        }
                    }
                },
                {
                    "name": "\u6597\u9c7c\u76f4\u64ad",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,146,101)"
                        }
                    }
                },
                {
                    "name": "\u521b\u4e16\u4e91\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,76,159)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u7535\u535a\u4e9a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,4,82)"
                        }
                    }
                },
                {
                    "name": "OKAY\u667a\u6167\u6559\u80b2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,106,49)"
                        }
                    }
                },
                {
                    "name": "\u6bcf\u65e5\u4f18\u9c9c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,21,9)"
                        }
                    }
                },
                {
                    "name": "\u73af\u7403\u8f66\u4eab",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,78,62)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u5730\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,6,26)"
                        }
                    }
                },
                {
                    "name": "\u534e\u783a\u667a\u884c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,139,34)"
                        }
                    }
                },
                {
                    "name": "\u9636\u5f62",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,58,71)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u5173\u6751\u6613\u521b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,101,112)"
                        }
                    }
                },
                {
                    "name": "UMU",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,113,87)"
                        }
                    }
                },
                {
                    "name": "\u7425\u73c0\u521b\u60f3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,109,47)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u65b9\u4f4e\u78b3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,25,89)"
                        }
                    }
                },
                {
                    "name": "\u65f6\u8da3social-touch",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,69,94)"
                        }
                    }
                },
                {
                    "name": "\u7279\u91d1\u65e0\u7ebf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,117,33)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u79d1\u5f18\u4e91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,56,97)"
                        }
                    }
                },
                {
                    "name": "\u745b\u592a\u83b1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,108,74)"
                        }
                    }
                },
                {
                    "name": "\u5929\u6570\u667a\u82af",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,115,35)"
                        }
                    }
                },
                {
                    "name": "\u798f\u7c73\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,91,118)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u4ee5\u8d24",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,28,90)"
                        }
                    }
                },
                {
                    "name": "\u6570\u7f8e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,59,152)"
                        }
                    }
                },
                {
                    "name": "\u8054\u8fd0\u77e5\u6167\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,113,18)"
                        }
                    }
                },
                {
                    "name": "FREE BRIO",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,135,42)"
                        }
                    }
                },
                {
                    "name": "\u6a0a\u767b\u8bfb\u4e66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,82,106)"
                        }
                    }
                },
                {
                    "name": "\u534e\u7b56",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,157,67)"
                        }
                    }
                },
                {
                    "name": "\u521b\u5fc5\u627f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,106,71)"
                        }
                    }
                },
                {
                    "name": "\u7384\u6b66\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,67,126)"
                        }
                    }
                },
                {
                    "name": "\u6b63\u4fdd\u8fdc\u7a0b\u6559\u80b2\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,44,59)"
                        }
                    }
                },
                {
                    "name": "\u878d\u6167\u91d1\u79d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,49,51)"
                        }
                    }
                },
                {
                    "name": "\u957f\u57ce\u6c7d\u8f66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,63,92)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u6b65\u5728\u5bb6\u65e9\u6559",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,73,121)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u5fc5\u9009\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,102,119)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u8d1d\u864e\u7269\u8054\u6280\u672f\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,85,128)"
                        }
                    }
                },
                {
                    "name": "KLOOK \u5ba2\u8def\u65c5\u884c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,116,131)"
                        }
                    }
                },
                {
                    "name": "\u5927\u7bb4\uff08\u676d\u5dde\uff09\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,6,114)"
                        }
                    }
                },
                {
                    "name": "58\u5b66\u8f66-\u9a7e\u6821\u4e00\u70b9\u901a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,93,145)"
                        }
                    }
                },
                {
                    "name": "\u8c6a\u732a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,157,147)"
                        }
                    }
                },
                {
                    "name": "\u730e\u4f18\u4f01\u4e1a\u7ba1\u7406\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,63,113)"
                        }
                    }
                },
                {
                    "name": "\u5988\u5988\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,123,108)"
                        }
                    }
                },
                {
                    "name": "\u5408\u5408\u4fe1\u606f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,152,102)"
                        }
                    }
                },
                {
                    "name": "\u6676\u786e\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,89,156)"
                        }
                    }
                },
                {
                    "name": "\u9633\u5149\u4fdd\u9669\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,129,78)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u516b\u7ef4\u7814\u4fee\u5b66\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,77,24)"
                        }
                    }
                },
                {
                    "name": "\u9541\u4fe1\u5065\u5eb7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,29,45)"
                        }
                    }
                },
                {
                    "name": "\u6b66\u6c49\u675e\u6893\u4f01\u4e1a\u7ba1\u7406\u54a8\u8be2\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,83,81)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u540c\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,47,140)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u57df\u94ed\u5c9b\uff08\u5409\u5229\u5de5\u4e1a\u4e92\u8054\u7f51\uff09",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,74,92)"
                        }
                    }
                },
                {
                    "name": "\u4e07\u5174\u79d1\u6280\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,15,120)"
                        }
                    }
                },
                {
                    "name": "\u5353\u671b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,64,38)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u5bb6\u91d1\u878d\u79d1\u6280\u6d4b\u8bc4\u4e2d\u5fc3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,18,128)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u5065\u5eb7\u4fdd\u9669",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,115,116)"
                        }
                    }
                },
                {
                    "name": "\u592a\u5e73\u6d0b\u623f\u5730\u4ea7\u7ecf\u7eaa\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,46,112)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u7f8e\u63a7\u80a1\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,2,19)"
                        }
                    }
                },
                {
                    "name": "\u9e4f\u5143\u5f81\u4fe1\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,153,83)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u8863\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,135,49)"
                        }
                    }
                },
                {
                    "name": "\u8377\u798f\u4eba\u5de5\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,84,46)"
                        }
                    }
                },
                {
                    "name": "\u67d2\u96f6\u58f9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,95,98)"
                        }
                    }
                },
                {
                    "name": "AfterShip\u7231\u5ba2\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,41,33)"
                        }
                    }
                },
                {
                    "name": "\u8fdc\u7738\u8f6f\u4ef6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,30,37)"
                        }
                    }
                },
                {
                    "name": "\u5915\u5915\u65f6\u4ee3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,121,74)"
                        }
                    }
                },
                {
                    "name": "\u95ea\u5e03\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,49,90)"
                        }
                    }
                },
                {
                    "name": "\u9510\u4ed5\u65b9\u8fbe\u4eba\u529b\u8d44\u6e90",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,154,70)"
                        }
                    }
                },
                {
                    "name": "\u6dfb\u695a\u701a\u624d\u4f20\u5a92",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,106,72)"
                        }
                    }
                },
                {
                    "name": "\u6587\u76db\u8d44\u4ea7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,101,140)"
                        }
                    }
                },
                {
                    "name": "\u827e\u5fb7\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,7,27)"
                        }
                    }
                },
                {
                    "name": "\u5a01\u661f\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,137,96)"
                        }
                    }
                },
                {
                    "name": "\u9f50\u78b3\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,20,123)"
                        }
                    }
                },
                {
                    "name": "\u8baf\u6c47\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,150,89)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u6c47\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,14,97)"
                        }
                    }
                },
                {
                    "name": "\u767e\u4fe1\u94f6\u884c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,66,136)"
                        }
                    }
                },
                {
                    "name": "\u963f\u91cc\u5df4\u5df4-\u9ad8\u5fb7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,100,44)"
                        }
                    }
                },
                {
                    "name": "\u8fde\u4fe1\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,65,62)"
                        }
                    }
                },
                {
                    "name": "\u7ffc\u8bfe\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,73,12)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6167\u732b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,156,61)"
                        }
                    }
                },
                {
                    "name": "\u5916\u8111\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,33,129)"
                        }
                    }
                },
                {
                    "name": "\u8d22\u76c8\u901a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,34,108)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u79d1\u777f\u89c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,104,85)"
                        }
                    }
                },
                {
                    "name": "Flash express",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,107,73)"
                        }
                    }
                },
                {
                    "name": "\u9876\u70b9\u8f6f\u4ef6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,73,21)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u6781\u777f\u79d1\u6280\u6709\u9650\u8d23\u4efb\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,157,1)"
                        }
                    }
                },
                {
                    "name": "\u7c73\u96c5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,127,110)"
                        }
                    }
                },
                {
                    "name": "\u4ee5\u89c1\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,37,108)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u5b89\u6613",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,79,41)"
                        }
                    }
                },
                {
                    "name": "\u987a\u4e30\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,48,141)"
                        }
                    }
                },
                {
                    "name": "\u521b\u5ba2\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,118,22)"
                        }
                    }
                },
                {
                    "name": "\u6d3e\u8fe9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,55,160)"
                        }
                    }
                },
                {
                    "name": "\u62ff\u706b\u97f3\u4e50",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,79,47)"
                        }
                    }
                },
                {
                    "name": "\u535a\u4f9d\u7279",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,39,130)"
                        }
                    }
                },
                {
                    "name": "\u82cf\u5dde\u624d\u5ba2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,34,80)"
                        }
                    }
                },
                {
                    "name": "Camera360",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,108,70)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u8c61\u4f18\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,116,1)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u84dd\u5361\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,156,43)"
                        }
                    }
                },
                {
                    "name": "\u6beb\u672b\u667a\u884c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,75,28)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u534e\u7814\u7a76\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,49,13)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u5341\u516d\u8fdb\u5236\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,111,79)"
                        }
                    }
                },
                {
                    "name": "\u5a5a\u793c\u7eaa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,113,154)"
                        }
                    }
                },
                {
                    "name": "\u822a\u7a7a\u5927\u90fd\u5e02\u7814\u7a76\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,20,143)"
                        }
                    }
                },
                {
                    "name": "\u7ea2\u84ddCP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,41,144)"
                        }
                    }
                },
                {
                    "name": "\u84dd\u8bfa\u5fae\u94f6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,128,95)"
                        }
                    }
                },
                {
                    "name": "\u5927\u542f\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,74,147)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u7280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,126,145)"
                        }
                    }
                },
                {
                    "name": "\u6ef4\u6ef4\u4f18\u70b9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,141,101)"
                        }
                    }
                },
                {
                    "name": "\u987a\u5b89\u4f1f\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,4,58)"
                        }
                    }
                },
                {
                    "name": "\u795e\u5dde\u79df\u8f66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,14,21)"
                        }
                    }
                },
                {
                    "name": "\u6210\u90fd\u5e02\u5c39\u8679\u4fe1\u606f\u6280\u672f\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,45,94)"
                        }
                    }
                },
                {
                    "name": "\u963f\u5361\u7d22\u5916\u6559\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,20,140)"
                        }
                    }
                },
                {
                    "name": "\u878d\u6613\u63a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,156,143)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u667a\u7c73\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,72,9)"
                        }
                    }
                },
                {
                    "name": "\u672a\u6765\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,95,135)"
                        }
                    }
                },
                {
                    "name": "\u7545\u804a\u5929\u4e0b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,139,128)"
                        }
                    }
                },
                {
                    "name": "\u601d\u5f00\u8fbe\u8bed\u97f3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,13,72)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u4e1a\u989c\u7a76\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,8,7)"
                        }
                    }
                },
                {
                    "name": "\u6c49\u4eea\u5b57\u5e93",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,52,135)"
                        }
                    }
                },
                {
                    "name": "\u67cf\u7f8e\u8fea\u5eb7\u4e0a\u6d77",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,73,116)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u4e07\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,31,66)"
                        }
                    }
                },
                {
                    "name": "GALASPORTS",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,82,88)"
                        }
                    }
                },
                {
                    "name": "\u63a2\u63a2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,9,25)"
                        }
                    }
                },
                {
                    "name": "\u827e\u7f8e\u661f\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,115,83)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u4e1c\u5e7f\u4fe1\u901a\u4fe1\u670d\u52a1\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,79,93)"
                        }
                    }
                },
                {
                    "name": "\u897f\u6e56\u5927\u5b66\u667a\u80fd\u4ea7\u4e1a\u7814\u7a76\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,87,7)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u79ef\u4e92\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,132,135)"
                        }
                    }
                },
                {
                    "name": "\u8054\u4f17\u91d1\u878d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,119,43)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u6cf0\u4ea7\u9669",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,49,147)"
                        }
                    }
                },
                {
                    "name": "\u770b\u623f\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,131,132)"
                        }
                    }
                },
                {
                    "name": "\u70b9\u4f17\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,43,76)"
                        }
                    }
                },
                {
                    "name": "\u8fc8\u5916\u8fea",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,154,143)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u5c16\u5cf0\u6b66\u6c49\u5206\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,153,42)"
                        }
                    }
                },
                {
                    "name": "\u4f20\u6613",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,86,118)"
                        }
                    }
                },
                {
                    "name": "\u540c\u82b1\u987a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,119,35)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u4e03\u4e92\u5a31",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,50,63)"
                        }
                    }
                },
                {
                    "name": "\u711c\u8000\u7f51\u7edc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,113,28)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u6b65\u7f51\u7edc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,17,119)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u6e7e\u521b\u65b0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,0,75)"
                        }
                    }
                },
                {
                    "name": "\u5927\u9053\u4e4b\u884c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,73,12)"
                        }
                    }
                },
                {
                    "name": "\u6a59\u8272\u4e91\u4e92\u8054\u7f51\u8bbe\u8ba1\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,97,18)"
                        }
                    }
                },
                {
                    "name": "\u5609\u9a70\u56fd\u9645\u5546\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,57,11)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u60f3\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,66,89)"
                        }
                    }
                },
                {
                    "name": "\u957f\u4ead\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,70,75)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u6ee1\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,101,89)"
                        }
                    }
                },
                {
                    "name": "\u5495\u549a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,7,107)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77\u91d1\u5927\u5e08\u7f51\u7edc\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,50,152)"
                        }
                    }
                },
                {
                    "name": "\u90bb\u6c47\u5427",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,115,114)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u7c73\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,28,40)"
                        }
                    }
                },
                {
                    "name": "\u552f\u54c1\u4f1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,0,117)"
                        }
                    }
                },
                {
                    "name": "\u638c\u4e0a\u5148\u673a-\u65fa\u5e97\u901aERP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,61,72)"
                        }
                    }
                },
                {
                    "name": "IntraMirror",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,157,130)"
                        }
                    }
                },
                {
                    "name": "\u7c73\u7edc\u661f\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,7,112)"
                        }
                    }
                },
                {
                    "name": "\u5373\u523b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,17,26)"
                        }
                    }
                },
                {
                    "name": "\u4ebf\u8054\u7f51\u7edc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,69,137)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u8003\u76f4\u901a\u8f66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,70,92)"
                        }
                    }
                },
                {
                    "name": "\u542c\u4e91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,112,148)"
                        }
                    }
                },
                {
                    "name": "\u4f0a\u6fb3\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,157,90)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u5cfb\u4fe1\u606f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,2,111)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u777f\u533b\u7597",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,115,44)"
                        }
                    }
                },
                {
                    "name": "\u9177\u5f00\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,2,134)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,149,12)"
                        }
                    }
                },
                {
                    "name": "\u9014\u5bb6\u6c11\u5bbf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,57,8)"
                        }
                    }
                },
                {
                    "name": "\u5bfa\u5e93",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,149,12)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5723\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,76,130)"
                        }
                    }
                },
                {
                    "name": "\u878d360",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,41,91)"
                        }
                    }
                },
                {
                    "name": "\u534e\u4e91\u4e2d\u76db",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,69,119)"
                        }
                    }
                },
                {
                    "name": "\u4f4d\u52a8\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,78,42)"
                        }
                    }
                },
                {
                    "name": "\u8054\u5408\u4f18\u521b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,49,135)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u7ec7\u7b97\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,6,95)"
                        }
                    }
                },
                {
                    "name": "\u58f0\u901a\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,151,115)"
                        }
                    }
                },
                {
                    "name": "RealAI",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,62,55)"
                        }
                    }
                },
                {
                    "name": "\u805a\u5747\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,102,57)"
                        }
                    }
                },
                {
                    "name": "\u638c\u9605",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,122,151)"
                        }
                    }
                },
                {
                    "name": "\u805a\u5bbd JoinQuant",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,111,98)"
                        }
                    }
                },
                {
                    "name": "\u6210\u90fd\u8d5b\u57fa\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,81,65)"
                        }
                    }
                },
                {
                    "name": "\u533a\u5757\u661f\u8fb0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,134,71)"
                        }
                    }
                },
                {
                    "name": "\u725b\u7801\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,118,95)"
                        }
                    }
                },
                {
                    "name": "\u9510\u4ed5\u65b9\u8fbe\u6d4e\u5357\u5206\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,159,78)"
                        }
                    }
                },
                {
                    "name": "\u539f\u5b50\u673a\u5668\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,92,78)"
                        }
                    }
                },
                {
                    "name": "\u4f17\u5b89\u4fdd\u9669",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,104,46)"
                        }
                    }
                },
                {
                    "name": "\u521b\u65b0\u5947\u667a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,89,47)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u6d4e\u533b\u7597",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,13,122)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77\u5594\u8da3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,119,11)"
                        }
                    }
                },
                {
                    "name": "\u79fb\u5361",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,69,94)"
                        }
                    }
                },
                {
                    "name": "\u5343\u5bfb\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,72,51)"
                        }
                    }
                },
                {
                    "name": "\u732b\u773c\u7535\u5f71",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,143,2)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5e0c\u671b\u516d\u548c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,71,48)"
                        }
                    }
                },
                {
                    "name": "\u94f6\u6cb3\u4fe1\u901a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,144,40)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u4fe1\u521b\u65b0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,39,24)"
                        }
                    }
                },
                {
                    "name": "\u5341\u835f\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,92,9)"
                        }
                    }
                },
                {
                    "name": "\u83ab\u6bd4\u55e8\u5ba2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,66,148)"
                        }
                    }
                },
                {
                    "name": "\u51ef\u8bda\u5546\u52a1\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,82,147)"
                        }
                    }
                },
                {
                    "name": "\u82f1\u96c4\u4e92\u5a31",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,94,68)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5c14\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,42,67)"
                        }
                    }
                },
                {
                    "name": "\u6c90\u77b3\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,151,2)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u679c\u6bd4\u7279",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,12,50)"
                        }
                    }
                },
                {
                    "name": "\u661f\u9645\u5927\u9646",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,54,14)"
                        }
                    }
                },
                {
                    "name": "OSR",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,25,143)"
                        }
                    }
                },
                {
                    "name": "\u6c38\u8f89\u4e91\u521b\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,139,120)"
                        }
                    }
                },
                {
                    "name": "\u98de\u5e38\u51c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,140,62)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u5dde\u7075\u611f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,32,129)"
                        }
                    }
                },
                {
                    "name": "\u660e\u4e4b\u6570\u636e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,67,107)"
                        }
                    }
                },
                {
                    "name": "\u5047\u9762\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,138,25)"
                        }
                    }
                },
                {
                    "name": "\u5357\u5a01\u8f6f\u4ef6\u80a1\u4efd\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,11,87)"
                        }
                    }
                },
                {
                    "name": "\u963f\u91cc\u5df4\u5df4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,141,160)"
                        }
                    }
                },
                {
                    "name": "\u516d\u4e00\u6559\u80b2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,74,9)"
                        }
                    }
                },
                {
                    "name": "\u6cf0\u5eb7\u4eba\u5bff",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,140,18)"
                        }
                    }
                },
                {
                    "name": "\u5c11\u5e74\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,45,75)"
                        }
                    }
                },
                {
                    "name": "\u5a31\u516c\u4e92\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,17,53)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u8109",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,141,112)"
                        }
                    }
                },
                {
                    "name": "\u67cf\u8fbe\u4eba\u529b\u8d44\u6e90\u987e\u95ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,93,65)"
                        }
                    }
                },
                {
                    "name": "\u7fcc\u65e5\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,53,123)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u4e16\u76f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,134,115)"
                        }
                    }
                },
                {
                    "name": "\u827e\u96f7\u7279\u54a8\u8be2\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,144,96)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5bb6\u5065\u6295",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,154,111)"
                        }
                    }
                },
                {
                    "name": "\u683c\u5170\u4ed5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,135,138)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u4e1c\u4ebf\u8fc5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,122,154)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u8bc1\u5238",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,51,9)"
                        }
                    }
                },
                {
                    "name": "\u7ade\u6280\u4e16\u754c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,114,126)"
                        }
                    }
                },
                {
                    "name": "\u4eb2\u5bb6\u7f51\u7edc\u6280\u672f\uff08\u5317\u4eac\uff09\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,120,158)"
                        }
                    }
                },
                {
                    "name": "\u5c1a\u4e91\u4f9d\u56fe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,140,131)"
                        }
                    }
                },
                {
                    "name": "\u6613\u79d1\u5947\u901a\u4fe1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,123,130)"
                        }
                    }
                },
                {
                    "name": "\u5730\u576a\u7ebf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,124,107)"
                        }
                    }
                },
                {
                    "name": "NIO\u851a\u6765",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,71,139)"
                        }
                    }
                },
                {
                    "name": "\u8da3\u9014\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,57,148)"
                        }
                    }
                },
                {
                    "name": "Vyou\u5fae\u4f60",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,22,148)"
                        }
                    }
                },
                {
                    "name": "\u8f6f\u725b\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,143,160)"
                        }
                    }
                },
                {
                    "name": "\u9752\u5cb3\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,103,153)"
                        }
                    }
                },
                {
                    "name": "\u6613\u5c45\u4e2d\u56fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,148,23)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5927\u701a\u4eba\u529b\u8d44\u6e90\u7ba1\u7406\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,34,67)"
                        }
                    }
                },
                {
                    "name": "\u6cf0\u5eb7\u4fdd\u9669\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,125,19)"
                        }
                    }
                },
                {
                    "name": "\u4e5d\u53f7\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,86,141)"
                        }
                    }
                },
                {
                    "name": "\u6f8e\u601d\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,124,15)"
                        }
                    }
                },
                {
                    "name": "\u6c47\u4fe1\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,32,92)"
                        }
                    }
                },
                {
                    "name": "\u835f\u8bda\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,123,53)"
                        }
                    }
                },
                {
                    "name": "\u4f9d\u77b3\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,120,40)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u4e4e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,143,121)"
                        }
                    }
                },
                {
                    "name": "\u534e\u98ce\u7231\u79d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,104,35)"
                        }
                    }
                },
                {
                    "name": "Xeno Dynamics",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,72,132)"
                        }
                    }
                },
                {
                    "name": "\u4e16\u7eaa\u5fb7\u8fb0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,126,48)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u987e\u4eba\u529b\u8d44\u6e90",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,124,58)"
                        }
                    }
                },
                {
                    "name": "\u5370\u8c61\u7b14\u8bb0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,151,45)"
                        }
                    }
                },
                {
                    "name": "\u533b\u667a\u5f71",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,7,49)"
                        }
                    }
                },
                {
                    "name": "\u96f7\u5ea6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,112,95)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u79df\u8d41",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,148,54)"
                        }
                    }
                },
                {
                    "name": "\u76df\u6d6a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,24,125)"
                        }
                    }
                },
                {
                    "name": "\u767b\u8679",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,63,16)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u5361\u7279\u52a0\u7279\u667a\u80fd\u79d1\u6280\u6709\u9650\u516c\u53f8\u5317\u4eac\u5206\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,26,90)"
                        }
                    }
                },
                {
                    "name": "\u6f6e\u6d41\u7f51\u7edc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,58,28)"
                        }
                    }
                },
                {
                    "name": "\u767e\u70bc\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,76,92)"
                        }
                    }
                },
                {
                    "name": "\u4e0d\u8a00\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,91,80)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u4e1c\u8dc3\u6609\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,93,123)"
                        }
                    }
                },
                {
                    "name": "\u534e\u4fa8\u57ce\u6587\u65c5\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,148,127)"
                        }
                    }
                },
                {
                    "name": "\u8def\u884c\u901a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,86,58)"
                        }
                    }
                },
                {
                    "name": "\u76df\u5927\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,135,72)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u8d62\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,63,84)"
                        }
                    }
                },
                {
                    "name": "\u4eac\u4e1c\u5546\u57ce",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,23,143)"
                        }
                    }
                },
                {
                    "name": "\u667a\u8d1d\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,142,115)"
                        }
                    }
                },
                {
                    "name": "\u597d\u597d\u4f4f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,10,97)"
                        }
                    }
                },
                {
                    "name": "\u65f6\u4ee3\u62d3\u7075",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,25,35)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u9690\u865a\u7b49\u8d24\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,69,69)"
                        }
                    }
                },
                {
                    "name": "\u540d\u7af9\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,47,76)"
                        }
                    }
                },
                {
                    "name": "\u96ea\u6d6a\u6570\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,102,59)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u5b8f\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,133,92)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u6210",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,63,27)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u68f5\u6995\u4f01\u4e1a\u7ba1\u7406\u987e\u95ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,143,108)"
                        }
                    }
                },
                {
                    "name": "\u4e16\u7eaa\u4f73\u7f18",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,122,90)"
                        }
                    }
                },
                {
                    "name": "\u661f\u5c18\u6570\u636e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,158,103)"
                        }
                    }
                },
                {
                    "name": "\u5546\u60c5\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,32,141)"
                        }
                    }
                },
                {
                    "name": "\u6253\u626e\u5bb6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,93,117)"
                        }
                    }
                },
                {
                    "name": "\u7bf1\u7b06\u5899",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,12,24)"
                        }
                    }
                },
                {
                    "name": "\u571f\u756a\u85af\u730e\u5934",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,61,52)"
                        }
                    }
                },
                {
                    "name": "\u8bfa\u535a\u533b\u7597",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,21,53)"
                        }
                    }
                },
                {
                    "name": "\u6b66\u6c49TCL",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,3,56)"
                        }
                    }
                },
                {
                    "name": "\u5982\u797a\u51fa\u884c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,0,102)"
                        }
                    }
                },
                {
                    "name": "\u7231\u5b66\u4e60\u6559\u80b2\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,120,95)"
                        }
                    }
                },
                {
                    "name": "\u8ffd\u89c5\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,71,151)"
                        }
                    }
                },
                {
                    "name": "\u797a\u9cb8\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,159,86)"
                        }
                    }
                },
                {
                    "name": "\u7545\u6377\u901a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,66,24)"
                        }
                    }
                },
                {
                    "name": "\u5609\u5b9e\u57fa\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,101,35)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6e05\u91d1\u79d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,129,9)"
                        }
                    }
                },
                {
                    "name": "\u9633\u5149\u94ed\u5c9b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,143,84)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u79d1\u95fb\u6b4c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,29,61)"
                        }
                    }
                },
                {
                    "name": "\u660e\u6e90\u4e91\u5ba2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,79,29)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u949e\u79d1\u4fe1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,63,122)"
                        }
                    }
                },
                {
                    "name": "\u897f\u5c71\u5c45\u6e38\u620f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,115,104)"
                        }
                    }
                },
                {
                    "name": "\u667a\u7406\u7269\u8054",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,102,143)"
                        }
                    }
                },
                {
                    "name": "\u89e6\u6f2b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,159,74)"
                        }
                    }
                },
                {
                    "name": "\u897f\u5b89\u7acb\u8fb0\u8fdc\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,154,137)"
                        }
                    }
                },
                {
                    "name": "\u827e\u8fc8\u79d1\u65af\u5a92\u4f53\u79d1\u6280\uff08\u5317\u4eac\uff09\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,64,79)"
                        }
                    }
                },
                {
                    "name": "\u683c\u521b\u4e1c\u667a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,14,9)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u4e1c\u667a\u6e90",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,82,95)"
                        }
                    }
                },
                {
                    "name": "\u9884\u7b56\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,12,128)"
                        }
                    }
                },
                {
                    "name": "\u6d66\u53d1\u4fe1\u7528\u5361",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,96,56)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u949b\u673a\u5668\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,132,103)"
                        }
                    }
                },
                {
                    "name": "\u7231\u7279\u66fc\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,39,87)"
                        }
                    }
                },
                {
                    "name": "\u62d3\u4fdd\u8f6f\u4ef6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,68,106)"
                        }
                    }
                },
                {
                    "name": "\u53ee\u549a\u4e70\u83dc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,44,13)"
                        }
                    }
                },
                {
                    "name": "\u8230\u76fe\u5b89\u68c0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,82,139)"
                        }
                    }
                },
                {
                    "name": "Kika Tech(\u65b0\u7f8e\u4e92\u901a)",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,111,112)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5965\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,63,123)"
                        }
                    }
                },
                {
                    "name": "\u591a\u725b\u4f20\u5a92",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,136,52)"
                        }
                    }
                },
                {
                    "name": "\u540c\u7eb3\u4fe1\u606f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,143,70)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u901a\u5feb\u9012",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,10,28)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u745e\u601d\u62d3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,54,17)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u5343\u4e91\u5929\u4e0b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,126,157)"
                        }
                    }
                },
                {
                    "name": "\u827e\u6d1b\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,80,46)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u56fd\u7535\u4fe1\u589e\u503c\u4e1a\u52a1\u8fd0\u8425\u4e2d\u5fc3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,37,154)"
                        }
                    }
                },
                {
                    "name": "\u9b54\u65b9\u706b\u79cd\u4f01\u4e1a\u7ba1\u7406\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,60,80)"
                        }
                    }
                },
                {
                    "name": "\u667a\u9f7f\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,92,28)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u53c2\u6570",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,120,114)"
                        }
                    }
                },
                {
                    "name": "\u6570\u777f\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,67,2)"
                        }
                    }
                },
                {
                    "name": "\u8d5b\u5427\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,1,108)"
                        }
                    }
                },
                {
                    "name": "\u8d5b\u8235\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,51,77)"
                        }
                    }
                },
                {
                    "name": "\u601d\u7075\u673a\u5668\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,33,153)"
                        }
                    }
                },
                {
                    "name": "\u623f\u8f66\u5b9d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,126,2)"
                        }
                    }
                },
                {
                    "name": "\u9a6c\u4e0a\u8d62",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,8,155)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u6773\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,139,124)"
                        }
                    }
                },
                {
                    "name": "\u6b66\u6c49\u653f\u901a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,102,74)"
                        }
                    }
                },
                {
                    "name": "\u8054\u901a\u65f6\u79d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,51,156)"
                        }
                    }
                },
                {
                    "name": "\u70ab\u751f\u6d3b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,79,25)"
                        }
                    }
                },
                {
                    "name": "\u6d82\u9e26\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,34,150)"
                        }
                    }
                },
                {
                    "name": "\u9518\u5d34\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,72,116)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u6444",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,55,74)"
                        }
                    }
                },
                {
                    "name": "\u683c\u7f57\u592b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,123,1)"
                        }
                    }
                },
                {
                    "name": "\u5609\u4e3a\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,18,85)"
                        }
                    }
                },
                {
                    "name": "\u534e\u5764\u9053\u5a01",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,11,144)"
                        }
                    }
                },
                {
                    "name": "\u82cf\u82af\u7269\u8054",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,38,20)"
                        }
                    }
                },
                {
                    "name": "\u968f\u8eab\u542c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,42,107)"
                        }
                    }
                },
                {
                    "name": "\u6d59\u6c5f\u6cd5\u4e4b\u9053\u4fe1\u606f\u6280\u672f\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,157,100)"
                        }
                    }
                },
                {
                    "name": "\u8054\u901a\u4e91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,57,80)"
                        }
                    }
                },
                {
                    "name": "\u548f\u67f3\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,34,52)"
                        }
                    }
                },
                {
                    "name": "\u5353\u4fe1\u4f01\u4e1a\u54a8\u8be2\u670d\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,130,146)"
                        }
                    }
                },
                {
                    "name": "\u84dd\u706f\u9c7c\u667a\u80fd\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,159,81)"
                        }
                    }
                },
                {
                    "name": "\u667a\u795e\u4fe1\u606f\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,114,45)"
                        }
                    }
                },
                {
                    "name": "\u9752\u677e\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,62,119)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77\u6469\u8c61\u7f51\u7edc\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,2,114)"
                        }
                    }
                },
                {
                    "name": "\u8bc6\u56e0\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,54,57)"
                        }
                    }
                },
                {
                    "name": "\u54c8\u5de5\u9a71\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,153,110)"
                        }
                    }
                },
                {
                    "name": "\u5f53\u5f53\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,24,20)"
                        }
                    }
                },
                {
                    "name": "e\u7b7e\u5b9d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,61,106)"
                        }
                    }
                },
                {
                    "name": "\u6e05\u9e64\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,158,79)"
                        }
                    }
                },
                {
                    "name": "\u4f20\u5174\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,19,74)"
                        }
                    }
                },
                {
                    "name": "\u6c49\u71b5\u901a\u4fe1\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,134,104)"
                        }
                    }
                },
                {
                    "name": "\u9646\u6cfd\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,29,30)"
                        }
                    }
                },
                {
                    "name": "\u6cdb\u534e\u91d1\u878d\u63a7\u80a1\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,4,160)"
                        }
                    }
                },
                {
                    "name": "\u8054\u901a\u667a\u7f51\u521b\u65b0\u4e2d\u5fc3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,142,40)"
                        }
                    }
                },
                {
                    "name": "\u68f1\u955c\u4e91\u6865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,71,148)"
                        }
                    }
                },
                {
                    "name": "\u6cf0\u5eb7\u5728\u7ebf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,107,75)"
                        }
                    }
                },
                {
                    "name": "\u53f6\u6d6a\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,45,121)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u4e07\u7ef4\u76c8\u521b\u79d1\u6280\u53d1\u5c55\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,93,138)"
                        }
                    }
                },
                {
                    "name": "\u58a8\u5947\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,112,47)"
                        }
                    }
                },
                {
                    "name": "\u7280\u8bed\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,128,140)"
                        }
                    }
                },
                {
                    "name": "\u5bcc\u6e2f\u4e07\u5609",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,25,67)"
                        }
                    }
                },
                {
                    "name": "\u94a2\u94c1\u4fa0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,20,121)"
                        }
                    }
                },
                {
                    "name": "\u5b8f\u9e3f\u94a5\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,30,99)"
                        }
                    }
                },
                {
                    "name": "\u535a\u777f\u701a\u8fbe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,93,154)"
                        }
                    }
                },
                {
                    "name": "\u534e\u667a\u751f\u7269",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,156,98)"
                        }
                    }
                },
                {
                    "name": "\u8eba\u5e73\u8bbe\u8ba1\u5bb6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,27,113)"
                        }
                    }
                },
                {
                    "name": "\u76c8\u4f73\u4fe1\u8054",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,154,77)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u7535\u91d1\u4fe1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,80,97)"
                        }
                    }
                },
                {
                    "name": "\u5b9d\u5c0a\u7535\u5546",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,29,78)"
                        }
                    }
                },
                {
                    "name": "\u53bb\u54ea\u513f\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,26,131)"
                        }
                    }
                },
                {
                    "name": "Riley Cillian\u83b1\u7199\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,119,42)"
                        }
                    }
                },
                {
                    "name": "AutoX",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,88,56)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u901a\u8f6f\u4ef6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,38,38)"
                        }
                    }
                },
                {
                    "name": "\u6930\u5b50\u4f20\u5a92",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,83,151)"
                        }
                    }
                },
                {
                    "name": "\u8d1d\u53f6\u65af\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,89,38)"
                        }
                    }
                },
                {
                    "name": "Mai\u5c0f\u9ea6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,159,117)"
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
                "\u7f8e\u56e2",
                "\u4eac\u4e1c\u96c6\u56e2",
                "\u5b57\u8282\u8df3\u52a8",
                "\u6ef4\u6ef4",
                "\u7231\u5947\u827a",
                "\u4eac\u4e1c\u7269\u6d41",
                "\u5feb\u624b",
                "\u5357\u6e56\u9662",
                "OPPO",
                "\u6167\u5b89\u91d1\u79d1"
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
            "text": "\u62db\u8058\u516c\u53f8\u5206\u5e03",
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
            "top": "55%",
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
        chart_0a5fa73bce8f462989d7ceed666c5517.setOption(option_0a5fa73bce8f462989d7ceed666c5517);
    </script>
                <div id="c8a0b07252c947459567ed40faea9381" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_c8a0b07252c947459567ed40faea9381 = echarts.init(
            document.getElementById('c8a0b07252c947459567ed40faea9381'), 'white', {renderer: 'canvas'});
        var option_c8a0b07252c947459567ed40faea9381 = {
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
                522,
                239,
                220,
                143,
                69,
                40,
                23,
                14,
                10,
                10
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
            "name": "\u57ce\u5e02\u5206\u5e03",
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
                    "name": "\u5317\u4eac",
                    "value": 522,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,96,118)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77",
                    "value": 239,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,13,143)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733",
                    "value": 220,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,156,134)"
                        }
                    }
                },
                {
                    "name": "\u676d\u5dde",
                    "value": 143,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,157,43)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u5dde",
                    "value": 69,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,82,63)"
                        }
                    }
                },
                {
                    "name": "\u6210\u90fd",
                    "value": 40,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,57,3)"
                        }
                    }
                },
                {
                    "name": "\u6b66\u6c49",
                    "value": 23,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,37,77)"
                        }
                    }
                },
                {
                    "name": "\u82cf\u5dde",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,129,6)"
                        }
                    }
                },
                {
                    "name": "\u897f\u5b89",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,3,140)"
                        }
                    }
                },
                {
                    "name": "\u5357\u4eac",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,25,86)"
                        }
                    }
                },
                {
                    "name": "\u4f5b\u5c71",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,159,140)"
                        }
                    }
                },
                {
                    "name": "\u91cd\u5e86",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,57,86)"
                        }
                    }
                },
                {
                    "name": "\u73e0\u6d77",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,49,94)"
                        }
                    }
                },
                {
                    "name": "\u90d1\u5dde",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,17,4)"
                        }
                    }
                },
                {
                    "name": "\u957f\u6c99",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,88,12)"
                        }
                    }
                },
                {
                    "name": "\u53a6\u95e8",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,100,33)"
                        }
                    }
                },
                {
                    "name": "\u5408\u80a5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,123,68)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5dde",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,90,75)"
                        }
                    }
                },
                {
                    "name": "\u9752\u5c9b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,58,130)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u9521",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,70,36)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u839e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,158,13)"
                        }
                    }
                },
                {
                    "name": "\u60e0\u5dde",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,4,66)"
                        }
                    }
                },
                {
                    "name": "\u6d4e\u5357",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,67,22)"
                        }
                    }
                },
                {
                    "name": "\u5927\u8fde",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,64,106)"
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
                "\u5317\u4eac",
                "\u4e0a\u6d77",
                "\u6df1\u5733",
                "\u676d\u5dde",
                "\u5e7f\u5dde",
                "\u6210\u90fd",
                "\u6b66\u6c49",
                "\u82cf\u5dde",
                "\u897f\u5b89",
                "\u5357\u4eac"
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
            "text": "\u62db\u8058\u57ce\u5e02\u5206\u5e03",
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
            "top": "55%",
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
        chart_c8a0b07252c947459567ed40faea9381.setOption(option_c8a0b07252c947459567ed40faea9381);
    </script>
                <div id="8122d9105840413ba9435a16c7c63f1b" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_8122d9105840413ba9435a16c7c63f1b = echarts.init(
            document.getElementById('8122d9105840413ba9435a16c7c63f1b'), 'white', {renderer: 'canvas'});
        var option_8122d9105840413ba9435a16c7c63f1b = {
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
            "name": "\u5c97\u4f4d\u5206\u5e03\u6811\u72b6\u56fe",
            "data": [
                {
                    "value": 522,
                    "name": "\u5317\u4eac"
                },
                {
                    "value": 239,
                    "name": "\u4e0a\u6d77"
                },
                {
                    "value": 220,
                    "name": "\u6df1\u5733"
                },
                {
                    "value": 143,
                    "name": "\u676d\u5dde"
                },
                {
                    "value": 69,
                    "name": "\u5e7f\u5dde"
                },
                {
                    "value": 40,
                    "name": "\u6210\u90fd"
                },
                {
                    "value": 23,
                    "name": "\u6b66\u6c49"
                },
                {
                    "value": 14,
                    "name": "\u82cf\u5dde"
                },
                {
                    "value": 10,
                    "name": "\u897f\u5b89"
                },
                {
                    "value": 10,
                    "name": "\u5357\u4eac"
                },
                {
                    "value": 6,
                    "name": "\u4f5b\u5c71"
                },
                {
                    "value": 4,
                    "name": "\u91cd\u5e86"
                },
                {
                    "value": 3,
                    "name": "\u73e0\u6d77"
                },
                {
                    "value": 3,
                    "name": "\u90d1\u5dde"
                },
                {
                    "value": 3,
                    "name": "\u957f\u6c99"
                },
                {
                    "value": 3,
                    "name": "\u53a6\u95e8"
                },
                {
                    "value": 3,
                    "name": "\u5408\u80a5"
                },
                {
                    "value": 2,
                    "name": "\u798f\u5dde"
                },
                {
                    "value": 2,
                    "name": "\u9752\u5c9b"
                },
                {
                    "value": 1,
                    "name": "\u65e0\u9521"
                },
                {
                    "value": 1,
                    "name": "\u4e1c\u839e"
                },
                {
                    "value": 1,
                    "name": "\u60e0\u5dde"
                },
                {
                    "value": 1,
                    "name": "\u6d4e\u5357"
                },
                {
                    "value": 1,
                    "name": "\u5927\u8fde"
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
                "\u5c97\u4f4d\u5206\u5e03\u6811\u72b6\u56fe"
            ],
            "selected": {
                "\u5c97\u4f4d\u5206\u5e03\u6811\u72b6\u56fe": true
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
            "text": "\u57ce\u5e02\u5206\u5e03\u6811\u72b6\u56fe",
            "padding": 5,
            "itemGap": 10
        }
    ]
};
        chart_8122d9105840413ba9435a16c7c63f1b.setOption(option_8122d9105840413ba9435a16c7c63f1b);
    </script>
                <div id="5d8b6e60e21f4bfe8948bbbbd2add75b" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_5d8b6e60e21f4bfe8948bbbbd2add75b = echarts.init(
            document.getElementById('5d8b6e60e21f4bfe8948bbbbd2add75b'), 'white', {renderer: 'canvas'});
            
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
    
        var option_5d8b6e60e21f4bfe8948bbbbd2add75b = {
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
            "type": "effectScatter",
            "name": "\u62db\u8058\u4e3b\u8981\u57ce\u5e02\u5206\u5e03",
            "coordinateSystem": "geo",
            "showEffectOn": "render",
            "rippleEffect": {
                "show": true,
                "brushType": "stroke",
                "scale": 2.5,
                "period": 4
            },
            "symbolSize": 12,
            "data": [
                {
                    "name": "\u5317\u4eac",
                    "value": [
                        116.407526,
                        39.90403,
                        522
                    ]
                },
                {
                    "name": "\u4e0a\u6d77",
                    "value": [
                        121.473701,
                        31.230416,
                        239
                    ]
                },
                {
                    "name": "\u6df1\u5733",
                    "value": [
                        114.07,
                        22.62,
                        220
                    ]
                },
                {
                    "name": "\u676d\u5dde",
                    "value": [
                        120.19,
                        30.26,
                        143
                    ]
                },
                {
                    "name": "\u5e7f\u5dde",
                    "value": [
                        113.23,
                        23.16,
                        69
                    ]
                },
                {
                    "name": "\u6210\u90fd",
                    "value": [
                        104.06,
                        30.67,
                        40
                    ]
                },
                {
                    "name": "\u6b66\u6c49",
                    "value": [
                        114.31,
                        30.52,
                        23
                    ]
                },
                {
                    "name": "\u82cf\u5dde",
                    "value": [
                        120.62,
                        31.32,
                        14
                    ]
                },
                {
                    "name": "\u897f\u5b89",
                    "value": [
                        108.95,
                        34.27,
                        10
                    ]
                },
                {
                    "name": "\u5357\u4eac",
                    "value": [
                        118.78,
                        32.04,
                        10
                    ]
                },
                {
                    "name": "\u4f5b\u5c71",
                    "value": [
                        113.11,
                        23.05,
                        6
                    ]
                },
                {
                    "name": "\u91cd\u5e86",
                    "value": [
                        106.551556,
                        29.563009,
                        4
                    ]
                },
                {
                    "name": "\u73e0\u6d77",
                    "value": [
                        113.52,
                        22.3,
                        3
                    ]
                },
                {
                    "name": "\u90d1\u5dde",
                    "value": [
                        113.65,
                        34.76,
                        3
                    ]
                },
                {
                    "name": "\u957f\u6c99",
                    "value": [
                        113,
                        28.21,
                        3
                    ]
                },
                {
                    "name": "\u53a6\u95e8",
                    "value": [
                        118.1,
                        24.46,
                        3
                    ]
                },
                {
                    "name": "\u5408\u80a5",
                    "value": [
                        117.27,
                        31.86,
                        3
                    ]
                },
                {
                    "name": "\u798f\u5dde",
                    "value": [
                        119.3,
                        26.08,
                        2
                    ]
                },
                {
                    "name": "\u9752\u5c9b",
                    "value": [
                        120.33,
                        36.07,
                        2
                    ]
                },
                {
                    "name": "\u65e0\u9521",
                    "value": [
                        120.29,
                        31.59,
                        1
                    ]
                },
                {
                    "name": "\u4e1c\u839e",
                    "value": [
                        113.75,
                        23.04,
                        1
                    ]
                },
                {
                    "name": "\u60e0\u5dde",
                    "value": [
                        114.4,
                        23.09,
                        1
                    ]
                },
                {
                    "name": "\u6d4e\u5357",
                    "value": [
                        117,
                        36.65,
                        1
                    ]
                },
                {
                    "name": "\u5927\u8fde",
                    "value": [
                        121.62,
                        38.92,
                        1
                    ]
                }
            ],
            "label": {
                "show": false,
                "position": "top",
                "margin": 8
            }
        }
    ],
    "legend": [
        {
            "data": [
                "\u62db\u8058\u4e3b\u8981\u57ce\u5e02\u5206\u5e03"
            ],
            "selected": {
                "\u62db\u8058\u4e3b\u8981\u57ce\u5e02\u5206\u5e03": true
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
        "formatter": function (params) {        return params.name + ' : ' + params.value[2];    },
        "textStyle": {
            "fontSize": 14
        },
        "borderWidth": 0,
        "padding": 5
    },
    "title": [
        {
            "text": "\u62db\u8058\u57ce\u5e02\u5206\u5e03",
            "padding": 5,
            "itemGap": 10
        }
    ],
    "geo": {
        "map": "china",
        "roam": true,
        "aspectScale": 0.75,
        "nameProperty": "name",
        "selectedMode": false,
        "emphasis": {}
    }
};
        chart_5d8b6e60e21f4bfe8948bbbbd2add75b.setOption(option_5d8b6e60e21f4bfe8948bbbbd2add75b);
    </script>
                <div id="3ce48f09c9714c1d9a704c42c2423404" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_3ce48f09c9714c1d9a704c42c2423404 = echarts.init(
            document.getElementById('3ce48f09c9714c1d9a704c42c2423404'), 'white', {renderer: 'canvas'});
        var option_3ce48f09c9714c1d9a704c42c2423404 = {
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
                144,
                99,
                89,
                37,
                34,
                32,
                31,
                27,
                25,
                25
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
            "name": "\u533a\u57df\u5206\u5e03",
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
                    "name": "\u6d77\u6dc0\u533a",
                    "value": 144,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,34,55)"
                        }
                    }
                },
                {
                    "name": "\u671d\u9633\u533a",
                    "value": 99,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,7,88)"
                        }
                    }
                },
                {
                    "name": "\u5357\u5c71\u533a",
                    "value": 89,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,83,43)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u6280\u56ed",
                    "value": 37,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,139,104)"
                        }
                    }
                },
                {
                    "name": "\u4f59\u676d\u533a",
                    "value": 34,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,138,95)"
                        }
                    }
                },
                {
                    "name": "\u6d66\u4e1c\u65b0\u2026",
                    "value": 32,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,111,136)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u5173\u6751",
                    "value": 31,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,132,99)"
                        }
                    }
                },
                {
                    "name": "\u5f20\u6c5f",
                    "value": 27,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,158,29)"
                        }
                    }
                },
                {
                    "name": "\u5f90\u6c47\u533a",
                    "value": 25,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,47,1)"
                        }
                    }
                },
                {
                    "name": "\u671b\u4eac",
                    "value": 25,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,109,31)"
                        }
                    }
                },
                {
                    "name": "\u5b9d\u5b89\u533a",
                    "value": 24,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,128,78)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u65b0\u533a",
                    "value": 23,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,30,39)"
                        }
                    }
                },
                {
                    "name": "\u798f\u7530\u533a",
                    "value": 22,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,22,154)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9053\u53e3",
                    "value": 21,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,15,79)"
                        }
                    }
                },
                {
                    "name": "\u897f\u5317\u65fa",
                    "value": 20,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,159,38)"
                        }
                    }
                },
                {
                    "name": "\u897f\u6eaa",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,56,6)"
                        }
                    }
                },
                {
                    "name": "\u957f\u5b81\u533a",
                    "value": 18,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,147,132)"
                        }
                    }
                },
                {
                    "name": "\u6ee8\u6c5f\u533a",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,77,1)"
                        }
                    }
                },
                {
                    "name": "\u901a\u5dde\u533a",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,33,21)"
                        }
                    }
                },
                {
                    "name": "\u897f\u6e56\u533a",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,99,100)"
                        }
                    }
                },
                {
                    "name": "\u95f5\u884c\u533a",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,99,9)"
                        }
                    }
                },
                {
                    "name": "\u897f\u4e8c\u65d7",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,142,29)"
                        }
                    }
                },
                {
                    "name": "\u5929\u6cb3\u533a",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,82,110)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u6e56\u65b0\u2026",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,109,143)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5174\u533a",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,122,144)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u73e0\u533a",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,67,33)"
                        }
                    }
                },
                {
                    "name": "\u6b66\u4faf\u533a",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,122,67)"
                        }
                    }
                },
                {
                    "name": "\u9759\u5b89\u533a",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,21,123)"
                        }
                    }
                },
                {
                    "name": "\u756a\u79ba\u533a",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,72,157)"
                        }
                    }
                },
                {
                    "name": "\u5927\u51b2",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,97,153)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u56ed\u2026",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,56,84)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u9662\u8def",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,89,46)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5730",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,27,59)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u6e7e",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,65,82)"
                        }
                    }
                },
                {
                    "name": "\u9f99\u534e",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,66,121)"
                        }
                    }
                },
                {
                    "name": "\u8679\u6885\u8def",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,108,32)"
                        }
                    }
                },
                {
                    "name": "\u897f\u5174",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,91,8)"
                        }
                    }
                },
                {
                    "name": "\u62f1\u5885\u533a",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,43,91)"
                        }
                    }
                },
                {
                    "name": "\u6768\u6d66\u533a",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,16,29)"
                        }
                    }
                },
                {
                    "name": "\u4ea6\u5e84",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,37,45)"
                        }
                    }
                },
                {
                    "name": "\u96e8\u82b1\u53f0\u2026",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,44,75)"
                        }
                    }
                },
                {
                    "name": "\u8679\u53e3\u533a",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,22,95)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u5c71\u516c\u2026",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,83,150)"
                        }
                    }
                },
                {
                    "name": "\u4e9a\u8fd0\u6751",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,160,26)"
                        }
                    }
                },
                {
                    "name": "\u987a\u5fb7\u533a",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,117,65)"
                        }
                    }
                },
                {
                    "name": "\u9ec4\u6d66\u533a",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,45,42)"
                        }
                    }
                },
                {
                    "name": "\u4ed3\u524d",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,100,152)"
                        }
                    }
                },
                {
                    "name": "\u5f90\u5bb6\u6c47",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,23,16)"
                        }
                    }
                },
                {
                    "name": "\u9152\u4ed9\u6865",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,129,79)"
                        }
                    }
                },
                {
                    "name": "\u677e\u6c5f\u533a",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,157,30)"
                        }
                    }
                },
                {
                    "name": "\u957f\u6cb3",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,134,110)"
                        }
                    }
                },
                {
                    "name": "\u96c1\u5854\u533a",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,160,143)"
                        }
                    }
                },
                {
                    "name": "\u897f\u4e09\u65d7",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,147,6)"
                        }
                    }
                },
                {
                    "name": "\u77f3\u666f\u5c71\u2026",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,41,117)"
                        }
                    }
                },
                {
                    "name": "\u6587\u4e09\u8def",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,42,114)"
                        }
                    }
                },
                {
                    "name": "\u56db\u60e0",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,148,160)"
                        }
                    }
                },
                {
                    "name": "\u897f\u57ce\u533a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,37,111)"
                        }
                    }
                },
                {
                    "name": "\u897f\u6e56",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,80,135)"
                        }
                    }
                },
                {
                    "name": "\u548c\u5e73\u91cc",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,90,33)"
                        }
                    }
                },
                {
                    "name": "\u9752\u6d66\u533a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,143,47)"
                        }
                    }
                },
                {
                    "name": "\u897f\u4e3d",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,75,76)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u6e2f",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,75,48)"
                        }
                    }
                },
                {
                    "name": "\u6765\u5e7f\u8425",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,150,43)"
                        }
                    }
                },
                {
                    "name": "\u71d5\u838e",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,115,142)"
                        }
                    }
                },
                {
                    "name": "\u8d8a\u79c0\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,148,34)"
                        }
                    }
                },
                {
                    "name": "\u5742\u7530",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,150,157)"
                        }
                    }
                },
                {
                    "name": "\u5317\u5916\u6ee9",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,74,126)"
                        }
                    }
                },
                {
                    "name": "\u7acb\u6c34\u6865",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,112,18)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u89d2\u573a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,148,125)"
                        }
                    }
                },
                {
                    "name": "\u73e0\u6c5f\u65b0\u2026",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,154,87)"
                        }
                    }
                },
                {
                    "name": "\u5317\u65b0\u6cfe",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,97,145)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u798f\u5e84",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,63,156)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u57ce\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,123,44)"
                        }
                    }
                },
                {
                    "name": "\u897f\u4e61",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,17,73)"
                        }
                    }
                },
                {
                    "name": "\u671d\u5916",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,113,134)"
                        }
                    }
                },
                {
                    "name": "\u7f57\u6e56\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,35,71)"
                        }
                    }
                },
                {
                    "name": "\u56de\u9f99\u89c2",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,87,76)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u6625\u8def",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,79,16)"
                        }
                    }
                },
                {
                    "name": "\u957f\u5f81",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,21,92)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u65b0\u6280\u2026",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,158,56)"
                        }
                    }
                },
                {
                    "name": "\u5efa\u5916\u5927\u2026",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,157,75)"
                        }
                    }
                },
                {
                    "name": "\u4e0b\u57ce\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,155,135)"
                        }
                    }
                },
                {
                    "name": "\u9f99\u534e\u65b0\u2026",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,75,28)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u58a9",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,143,128)"
                        }
                    }
                },
                {
                    "name": "\u9999\u6d32\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,128,130)"
                        }
                    }
                },
                {
                    "name": "\u751c\u6c34\u56ed",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,112,71)"
                        }
                    }
                },
                {
                    "name": "\u8700\u5c71\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,15,61)"
                        }
                    }
                },
                {
                    "name": "\u5357\u5934",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,57,125)"
                        }
                    }
                },
                {
                    "name": "\u7ea2\u5e99",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,128,81)"
                        }
                    }
                },
                {
                    "name": "\u897f\u76f4\u95e8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,146,144)"
                        }
                    }
                },
                {
                    "name": "\u9646\u5bb6\u5634",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,50,135)"
                        }
                    }
                },
                {
                    "name": "\u5929\u6cb3\u57ce",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,160,118)"
                        }
                    }
                },
                {
                    "name": "\u5efa\u56fd\u95e8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,83,142)"
                        }
                    }
                },
                {
                    "name": "\u9f13\u697c\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,130,148)"
                        }
                    }
                },
                {
                    "name": "\u9f99\u9633\u8def\u2026",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,11,61)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u4ead",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,91,134)"
                        }
                    }
                },
                {
                    "name": "\u8427\u5c71\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,82,25)"
                        }
                    }
                },
                {
                    "name": "\u5173\u5c71",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,96,132)"
                        }
                    }
                },
                {
                    "name": "\u6d2a\u5c71\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,93,128)"
                        }
                    }
                },
                {
                    "name": "\u534e\u6f15",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,141,45)"
                        }
                    }
                },
                {
                    "name": "\u601d\u660e\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,46,27)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u53f0\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,105,99)"
                        }
                    }
                },
                {
                    "name": "\u6d66\u6cbf",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,98,90)"
                        }
                    }
                },
                {
                    "name": "\u7fe0\u82d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,13,97)"
                        }
                    }
                },
                {
                    "name": "\u68e0\u4e0b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,24,127)"
                        }
                    }
                },
                {
                    "name": "\u671d\u9633\u95e8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,73,141)"
                        }
                    }
                },
                {
                    "name": "\u666e\u9640\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,25,56)"
                        }
                    }
                },
                {
                    "name": "\u9547\u5b81\u8def",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,66,154)"
                        }
                    }
                },
                {
                    "name": "\u80dc\u6d66",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,49,101)"
                        }
                    }
                },
                {
                    "name": "\u5ef6\u5409",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,67,104)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7891\u5e97",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,136,64)"
                        }
                    }
                },
                {
                    "name": "\u6f4d\u574a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,47,126)"
                        }
                    }
                },
                {
                    "name": "\u6797\u548c",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,9,83)"
                        }
                    }
                },
                {
                    "name": "\u5b98\u6d32",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,94,66)"
                        }
                    }
                },
                {
                    "name": "\u5317\u82d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,47,116)"
                        }
                    }
                },
                {
                    "name": "\u9f99\u5c97\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,152,153)"
                        }
                    }
                },
                {
                    "name": "\u660c\u5e73\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,55,145)"
                        }
                    }
                },
                {
                    "name": "\u8398\u5e84",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,107,37)"
                        }
                    }
                },
                {
                    "name": "\u4e03\u5b9d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,23,76)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5c71\u5b50",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,81,22)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u8d1e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,68,88)"
                        }
                    }
                },
                {
                    "name": "\u94b1\u5858\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,22,158)"
                        }
                    }
                },
                {
                    "name": "\u5efa\u8bbe\u4e8c\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,66,45)"
                        }
                    }
                },
                {
                    "name": "\u767e\u5b50\u6e7e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,142,117)"
                        }
                    }
                },
                {
                    "name": "\u5e38\u8425",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,111,68)"
                        }
                    }
                },
                {
                    "name": "\u5927\u671b\u8def",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,68,105)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5b89",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,142,121)"
                        }
                    }
                },
                {
                    "name": "\u6ee8\u6e56\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,146,2)"
                        }
                    }
                },
                {
                    "name": "\u5357\u4eac",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,156,15)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,137,98)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u76f4\u95e8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,123,55)"
                        }
                    }
                },
                {
                    "name": "\u5949\u8d24\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,87,23)"
                        }
                    }
                },
                {
                    "name": "\u5efa\u90ba\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,63,29)"
                        }
                    }
                },
                {
                    "name": "\u822a\u7a7a\u6e2f\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,51,28)"
                        }
                    }
                },
                {
                    "name": "\u6d0b\u6cfe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,109,111)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u5c71\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,69,84)"
                        }
                    }
                },
                {
                    "name": "\u524d\u6d77",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,35,145)"
                        }
                    }
                },
                {
                    "name": "\u6f15\u6cb3\u6cfe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,86,141)"
                        }
                    }
                },
                {
                    "name": "\u6d41\u82b3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,49,132)"
                        }
                    }
                },
                {
                    "name": "\u5927\u7af9\u6797",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,133,52)"
                        }
                    }
                },
                {
                    "name": "\u6816\u971e\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,99,154)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u725b\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,42,54)"
                        }
                    }
                },
                {
                    "name": "\u6e56\u91cc\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,41,91)"
                        }
                    }
                },
                {
                    "name": "\u53e4\u58a9\u8def",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,91,20)"
                        }
                    }
                },
                {
                    "name": "\u5cad\u5357",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,33,55)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u6167\u5bfa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,52,148)"
                        }
                    }
                },
                {
                    "name": "\u897f\u5173",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,103,8)"
                        }
                    }
                },
                {
                    "name": "\u5357\u6cb9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,73,100)"
                        }
                    }
                },
                {
                    "name": "\u9ec4\u57d4\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,116,141)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u56db",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,131,78)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u6e56",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,113,99)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u5dde",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,143,8)"
                        }
                    }
                },
                {
                    "name": "\u5458\u6751",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,143,38)"
                        }
                    }
                },
                {
                    "name": "\u5b81\u56f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,20,2)"
                        }
                    }
                },
                {
                    "name": "\u90d1\u4e1c\u65b0\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,51,87)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u6c34\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,6,78)"
                        }
                    }
                },
                {
                    "name": "\u6253\u6d66\u6865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,123,67)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u5c71",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,99,43)"
                        }
                    }
                },
                {
                    "name": "\u90eb\u90fd\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,47,92)"
                        }
                    }
                },
                {
                    "name": "\u6f15\u5b9d\u8def",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,128,26)"
                        }
                    }
                },
                {
                    "name": "\u6b66\u6c49\u7ecf\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,104,5)"
                        }
                    }
                },
                {
                    "name": "\u897f\u82d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,140,9)"
                        }
                    }
                },
                {
                    "name": "\u4eac\u5e7f\u6865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,19,38)"
                        }
                    }
                },
                {
                    "name": "\u78a7\u4e91\u793e\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,68,119)"
                        }
                    }
                },
                {
                    "name": "\u4e8c\u90ce",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,61,73)"
                        }
                    }
                },
                {
                    "name": "\u57ce\u968d\u5e99",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,142,151)"
                        }
                    }
                },
                {
                    "name": "\u4e07\u5bff\u5bfa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,67,47)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u5173",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,27,29)"
                        }
                    }
                },
                {
                    "name": "\u8f6f\u4ef6\u56ed",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,139,93)"
                        }
                    }
                },
                {
                    "name": "\u5c55\u89c8\u8def",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,93,58)"
                        }
                    }
                },
                {
                    "name": "\u5cb3\u9e93\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,83,4)"
                        }
                    }
                },
                {
                    "name": "\u592a\u548c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,55,83)"
                        }
                    }
                },
                {
                    "name": "\u4e07\u67f3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,38,0)"
                        }
                    }
                },
                {
                    "name": "\u5f00\u53d1\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,50,157)"
                        }
                    }
                },
                {
                    "name": "\u89c2\u6c99\u5cad",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,18,80)"
                        }
                    }
                },
                {
                    "name": "\u6dd8\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,118,104)"
                        }
                    }
                },
                {
                    "name": "\u6731\u96c0\u5927\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,78,124)"
                        }
                    }
                },
                {
                    "name": "\u576a\u5c71\u65b0\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,2,62)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u6865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,130,56)"
                        }
                    }
                },
                {
                    "name": "\u767b\u5cf0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,149,87)"
                        }
                    }
                },
                {
                    "name": "\u8096\u5bb6\u6cb3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,94,111)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u6986\u6811",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,68,12)"
                        }
                    }
                },
                {
                    "name": "\u592a\u5e73\u6865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,156,139)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u839e\u5e02\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,45,156)"
                        }
                    }
                },
                {
                    "name": "\u9ec4\u5c9b\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,97,152)"
                        }
                    }
                },
                {
                    "name": "\u60e0\u9633\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,79,110)"
                        }
                    }
                },
                {
                    "name": "\u6885\u9647",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,71,128)"
                        }
                    }
                },
                {
                    "name": "\u6c5f\u5cb8\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,102,106)"
                        }
                    }
                },
                {
                    "name": "\u4eae\u9a6c\u6865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,152,101)"
                        }
                    }
                },
                {
                    "name": "\u5ba3\u6b66\u95e8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,101,150)"
                        }
                    }
                },
                {
                    "name": "\u8679\u6865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,109,160)"
                        }
                    }
                },
                {
                    "name": "\u5d02\u5c71\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,118,154)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u5927\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,114,93)"
                        }
                    }
                },
                {
                    "name": "\u4e08\u516b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,151,18)"
                        }
                    }
                },
                {
                    "name": "\u5d07\u660e\u53bf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,83,95)"
                        }
                    }
                },
                {
                    "name": "\u8f66\u516c\u5e99",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,139,46)"
                        }
                    }
                },
                {
                    "name": "\u957f\u9633\u8def",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,28,95)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u91cc\u6cb3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,56,32)"
                        }
                    }
                },
                {
                    "name": "\u83b2\u82b1\u4e8c\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,133,131)"
                        }
                    }
                },
                {
                    "name": "\u5434\u4e2d\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,34,158)"
                        }
                    }
                },
                {
                    "name": "\u8299\u84c9\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,74,139)"
                        }
                    }
                },
                {
                    "name": "\u6c5f\u5357",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,150,82)"
                        }
                    }
                },
                {
                    "name": "\u95f2\u6797",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,29,115)"
                        }
                    }
                },
                {
                    "name": "\u5de6\u5bb6\u5e84",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,93,44)"
                        }
                    }
                },
                {
                    "name": "\u6e1d\u5317\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,127,109)"
                        }
                    }
                },
                {
                    "name": "\u957f\u5bff\u8def",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,128,18)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u534e\u8def",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,133,142)"
                        }
                    }
                },
                {
                    "name": "\u7530\u6751",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,6,65)"
                        }
                    }
                },
                {
                    "name": "\u9526\u6c5f\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,107,6)"
                        }
                    }
                },
                {
                    "name": "\u5965\u4f53",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,77,44)"
                        }
                    }
                },
                {
                    "name": "\u8df3\u4f1e\u5854",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,103,93)"
                        }
                    }
                },
                {
                    "name": "\u8f66\u7ad9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,41,126)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u548c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,33,129)"
                        }
                    }
                },
                {
                    "name": "\u540e\u6d77",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,78,21)"
                        }
                    }
                },
                {
                    "name": "\u5317\u592a\u5e73\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,76,133)"
                        }
                    }
                },
                {
                    "name": "\u9f99\u6eaa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,148,157)"
                        }
                    }
                },
                {
                    "name": "\u6c5f\u590f\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,93,116)"
                        }
                    }
                },
                {
                    "name": "\u5929\u5c71\u8def",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,51,105)"
                        }
                    }
                },
                {
                    "name": "\u56db\u5b63\u9752",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,133,50)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u8857",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,23,136)"
                        }
                    }
                },
                {
                    "name": "\u841d\u5c97\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,116,74)"
                        }
                    }
                },
                {
                    "name": "\u8f66\u9642",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,40,130)"
                        }
                    }
                },
                {
                    "name": "\u5143\u548c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,132,149)"
                        }
                    }
                },
                {
                    "name": "\u4e07\u6cc9\u6cb3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,3,72)"
                        }
                    }
                },
                {
                    "name": "\u69d0\u836b\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,150,87)"
                        }
                    }
                },
                {
                    "name": "\u897f\u5c71",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,91,60)"
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
                "\u6d77\u6dc0\u533a",
                "\u671d\u9633\u533a",
                "\u5357\u5c71\u533a",
                "\u79d1\u6280\u56ed",
                "\u4f59\u676d\u533a",
                "\u6d66\u4e1c\u65b0\u2026",
                "\u4e2d\u5173\u6751",
                "\u5f20\u6c5f",
                "\u5f90\u6c47\u533a",
                "\u671b\u4eac"
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
            "text": "\u62db\u8058\u533a\u57df\u5206\u5e03",
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
            "top": "55%",
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
        chart_3ce48f09c9714c1d9a704c42c2423404.setOption(option_3ce48f09c9714c1d9a704c42c2423404);
    </script>
                <div id="94ba5219eb84465188efe2a54c0e87f1" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_94ba5219eb84465188efe2a54c0e87f1 = echarts.init(
            document.getElementById('94ba5219eb84465188efe2a54c0e87f1'), 'white', {renderer: 'canvas'});
        var option_94ba5219eb84465188efe2a54c0e87f1 = {
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
            "name": "\u5c97\u4f4d\u5206\u5e03\u6811\u72b6\u56fe",
            "data": [
                {
                    "value": 144,
                    "name": "\u6d77\u6dc0\u533a"
                },
                {
                    "value": 99,
                    "name": "\u671d\u9633\u533a"
                },
                {
                    "value": 89,
                    "name": "\u5357\u5c71\u533a"
                },
                {
                    "value": 37,
                    "name": "\u79d1\u6280\u56ed"
                },
                {
                    "value": 34,
                    "name": "\u4f59\u676d\u533a"
                },
                {
                    "value": 32,
                    "name": "\u6d66\u4e1c\u65b0\u2026"
                },
                {
                    "value": 31,
                    "name": "\u4e2d\u5173\u6751"
                },
                {
                    "value": 27,
                    "name": "\u5f20\u6c5f"
                },
                {
                    "value": 25,
                    "name": "\u5f90\u6c47\u533a"
                },
                {
                    "value": 25,
                    "name": "\u671b\u4eac"
                },
                {
                    "value": 24,
                    "name": "\u5b9d\u5b89\u533a"
                },
                {
                    "value": 23,
                    "name": "\u9ad8\u65b0\u533a"
                },
                {
                    "value": 22,
                    "name": "\u798f\u7530\u533a"
                },
                {
                    "value": 21,
                    "name": "\u4e94\u9053\u53e3"
                },
                {
                    "value": 20,
                    "name": "\u897f\u5317\u65fa"
                },
                {
                    "value": 19,
                    "name": "\u897f\u6eaa"
                },
                {
                    "value": 18,
                    "name": "\u957f\u5b81\u533a"
                },
                {
                    "value": 17,
                    "name": "\u6ee8\u6c5f\u533a"
                },
                {
                    "value": 17,
                    "name": "\u901a\u5dde\u533a"
                },
                {
                    "value": 16,
                    "name": "\u897f\u6e56\u533a"
                },
                {
                    "value": 16,
                    "name": "\u95f5\u884c\u533a"
                },
                {
                    "value": 15,
                    "name": "\u897f\u4e8c\u65d7"
                },
                {
                    "value": 15,
                    "name": "\u5929\u6cb3\u533a"
                },
                {
                    "value": 14,
                    "name": "\u4e1c\u6e56\u65b0\u2026"
                },
                {
                    "value": 14,
                    "name": "\u5927\u5174\u533a"
                },
                {
                    "value": 13,
                    "name": "\u6d77\u73e0\u533a"
                },
                {
                    "value": 12,
                    "name": "\u6b66\u4faf\u533a"
                },
                {
                    "value": 12,
                    "name": "\u9759\u5b89\u533a"
                },
                {
                    "value": 11,
                    "name": "\u756a\u79ba\u533a"
                },
                {
                    "value": 11,
                    "name": "\u5927\u51b2"
                },
                {
                    "value": 10,
                    "name": "\u5de5\u4e1a\u56ed\u2026"
                },
                {
                    "value": 10,
                    "name": "\u5b66\u9662\u8def"
                },
                {
                    "value": 9,
                    "name": "\u4e0a\u5730"
                },
                {
                    "value": 9,
                    "name": "\u6df1\u5733\u6e7e"
                },
                {
                    "value": 9,
                    "name": "\u9f99\u534e"
                },
                {
                    "value": 9,
                    "name": "\u8679\u6885\u8def"
                },
                {
                    "value": 9,
                    "name": "\u897f\u5174"
                },
                {
                    "value": 8,
                    "name": "\u62f1\u5885\u533a"
                },
                {
                    "value": 8,
                    "name": "\u6768\u6d66\u533a"
                },
                {
                    "value": 7,
                    "name": "\u4ea6\u5e84"
                },
                {
                    "value": 6,
                    "name": "\u96e8\u82b1\u53f0\u2026"
                },
                {
                    "value": 6,
                    "name": "\u8679\u53e3\u533a"
                },
                {
                    "value": 6,
                    "name": "\u4e2d\u5c71\u516c\u2026"
                },
                {
                    "value": 6,
                    "name": "\u4e9a\u8fd0\u6751"
                },
                {
                    "value": 6,
                    "name": "\u987a\u5fb7\u533a"
                },
                {
                    "value": 6,
                    "name": "\u9ec4\u6d66\u533a"
                },
                {
                    "value": 6,
                    "name": "\u4ed3\u524d"
                },
                {
                    "value": 6,
                    "name": "\u5f90\u5bb6\u6c47"
                },
                {
                    "value": 6,
                    "name": "\u9152\u4ed9\u6865"
                },
                {
                    "value": 6,
                    "name": "\u677e\u6c5f\u533a"
                },
                {
                    "value": 5,
                    "name": "\u957f\u6cb3"
                },
                {
                    "value": 5,
                    "name": "\u96c1\u5854\u533a"
                },
                {
                    "value": 5,
                    "name": "\u897f\u4e09\u65d7"
                },
                {
                    "value": 5,
                    "name": "\u77f3\u666f\u5c71\u2026"
                },
                {
                    "value": 5,
                    "name": "\u6587\u4e09\u8def"
                },
                {
                    "value": 4,
                    "name": "\u56db\u60e0"
                },
                {
                    "value": 4,
                    "name": "\u897f\u57ce\u533a"
                },
                {
                    "value": 4,
                    "name": "\u897f\u6e56"
                },
                {
                    "value": 4,
                    "name": "\u548c\u5e73\u91cc"
                },
                {
                    "value": 4,
                    "name": "\u9752\u6d66\u533a"
                },
                {
                    "value": 4,
                    "name": "\u897f\u4e3d"
                },
                {
                    "value": 4,
                    "name": "\u65b0\u6e2f"
                },
                {
                    "value": 4,
                    "name": "\u6765\u5e7f\u8425"
                },
                {
                    "value": 3,
                    "name": "\u71d5\u838e"
                },
                {
                    "value": 3,
                    "name": "\u8d8a\u79c0\u533a"
                },
                {
                    "value": 3,
                    "name": "\u5742\u7530"
                },
                {
                    "value": 3,
                    "name": "\u5317\u5916\u6ee9"
                },
                {
                    "value": 3,
                    "name": "\u7acb\u6c34\u6865"
                },
                {
                    "value": 3,
                    "name": "\u4e94\u89d2\u573a"
                },
                {
                    "value": 3,
                    "name": "\u73e0\u6c5f\u65b0\u2026"
                },
                {
                    "value": 3,
                    "name": "\u5317\u65b0\u6cfe"
                },
                {
                    "value": 3,
                    "name": "\u5b9a\u798f\u5e84"
                },
                {
                    "value": 3,
                    "name": "\u4e1c\u57ce\u533a"
                },
                {
                    "value": 3,
                    "name": "\u897f\u4e61"
                },
                {
                    "value": 3,
                    "name": "\u671d\u5916"
                },
                {
                    "value": 3,
                    "name": "\u7f57\u6e56\u533a"
                },
                {
                    "value": 3,
                    "name": "\u56de\u9f99\u89c2"
                },
                {
                    "value": 3,
                    "name": "\u77e5\u6625\u8def"
                },
                {
                    "value": 3,
                    "name": "\u957f\u5f81"
                },
                {
                    "value": 3,
                    "name": "\u9ad8\u65b0\u6280\u2026"
                },
                {
                    "value": 3,
                    "name": "\u5efa\u5916\u5927\u2026"
                },
                {
                    "value": 3,
                    "name": "\u4e0b\u57ce\u533a"
                },
                {
                    "value": 3,
                    "name": "\u9f99\u534e\u65b0\u2026"
                },
                {
                    "value": 3,
                    "name": "\u4e09\u58a9"
                },
                {
                    "value": 3,
                    "name": "\u9999\u6d32\u533a"
                },
                {
                    "value": 3,
                    "name": "\u751c\u6c34\u56ed"
                },
                {
                    "value": 3,
                    "name": "\u8700\u5c71\u533a"
                },
                {
                    "value": 2,
                    "name": "\u5357\u5934"
                },
                {
                    "value": 2,
                    "name": "\u7ea2\u5e99"
                },
                {
                    "value": 2,
                    "name": "\u897f\u76f4\u95e8"
                },
                {
                    "value": 2,
                    "name": "\u9646\u5bb6\u5634"
                },
                {
                    "value": 2,
                    "name": "\u5929\u6cb3\u57ce"
                },
                {
                    "value": 2,
                    "name": "\u5efa\u56fd\u95e8"
                },
                {
                    "value": 2,
                    "name": "\u9f13\u697c\u533a"
                },
                {
                    "value": 2,
                    "name": "\u9f99\u9633\u8def\u2026"
                },
                {
                    "value": 2,
                    "name": "\u5b89\u4ead"
                },
                {
                    "value": 2,
                    "name": "\u8427\u5c71\u533a"
                },
                {
                    "value": 2,
                    "name": "\u5173\u5c71"
                },
                {
                    "value": 2,
                    "name": "\u6d2a\u5c71\u533a"
                },
                {
                    "value": 2,
                    "name": "\u534e\u6f15"
                },
                {
                    "value": 2,
                    "name": "\u601d\u660e\u533a"
                },
                {
                    "value": 2,
                    "name": "\u4e30\u53f0\u533a"
                },
                {
                    "value": 2,
                    "name": "\u6d66\u6cbf"
                },
                {
                    "value": 2,
                    "name": "\u7fe0\u82d1"
                },
                {
                    "value": 2,
                    "name": "\u68e0\u4e0b"
                },
                {
                    "value": 2,
                    "name": "\u671d\u9633\u95e8"
                },
                {
                    "value": 2,
                    "name": "\u666e\u9640\u533a"
                },
                {
                    "value": 2,
                    "name": "\u9547\u5b81\u8def"
                },
                {
                    "value": 2,
                    "name": "\u80dc\u6d66"
                },
                {
                    "value": 2,
                    "name": "\u5ef6\u5409"
                },
                {
                    "value": 2,
                    "name": "\u9ad8\u7891\u5e97"
                },
                {
                    "value": 2,
                    "name": "\u6f4d\u574a"
                },
                {
                    "value": 2,
                    "name": "\u6797\u548c"
                },
                {
                    "value": 2,
                    "name": "\u5b98\u6d32"
                },
                {
                    "value": 2,
                    "name": "\u5317\u82d1"
                },
                {
                    "value": 2,
                    "name": "\u9f99\u5c97\u533a"
                },
                {
                    "value": 2,
                    "name": "\u660c\u5e73\u533a"
                },
                {
                    "value": 2,
                    "name": "\u8398\u5e84"
                },
                {
                    "value": 2,
                    "name": "\u4e03\u5b9d"
                },
                {
                    "value": 2,
                    "name": "\u5927\u5c71\u5b50"
                },
                {
                    "value": 2,
                    "name": "\u5b89\u8d1e"
                },
                {
                    "value": 2,
                    "name": "\u94b1\u5858\u533a"
                },
                {
                    "value": 1,
                    "name": "\u5efa\u8bbe\u4e8c\u2026"
                },
                {
                    "value": 1,
                    "name": "\u767e\u5b50\u6e7e"
                },
                {
                    "value": 1,
                    "name": "\u5e38\u8425"
                },
                {
                    "value": 1,
                    "name": "\u5927\u671b\u8def"
                },
                {
                    "value": 1,
                    "name": "\u65b0\u5b89"
                },
                {
                    "value": 1,
                    "name": "\u6ee8\u6e56\u533a"
                },
                {
                    "value": 1,
                    "name": "\u5357\u4eac"
                },
                {
                    "value": 1,
                    "name": "\u4e0a\u6d77"
                },
                {
                    "value": 1,
                    "name": "\u4e1c\u76f4\u95e8"
                },
                {
                    "value": 1,
                    "name": "\u5949\u8d24\u533a"
                },
                {
                    "value": 1,
                    "name": "\u5efa\u90ba\u533a"
                },
                {
                    "value": 1,
                    "name": "\u822a\u7a7a\u6e2f\u2026"
                },
                {
                    "value": 1,
                    "name": "\u6d0b\u6cfe"
                },
                {
                    "value": 1,
                    "name": "\u91d1\u5c71\u533a"
                },
                {
                    "value": 1,
                    "name": "\u524d\u6d77"
                },
                {
                    "value": 1,
                    "name": "\u6f15\u6cb3\u6cfe"
                },
                {
                    "value": 1,
                    "name": "\u6d41\u82b3"
                },
                {
                    "value": 1,
                    "name": "\u5927\u7af9\u6797"
                },
                {
                    "value": 1,
                    "name": "\u6816\u971e\u533a"
                },
                {
                    "value": 1,
                    "name": "\u91d1\u725b\u533a"
                },
                {
                    "value": 1,
                    "name": "\u6e56\u91cc\u533a"
                },
                {
                    "value": 1,
                    "name": "\u53e4\u58a9\u8def"
                },
                {
                    "value": 1,
                    "name": "\u5cad\u5357"
                },
                {
                    "value": 1,
                    "name": "\u5b9a\u6167\u5bfa"
                },
                {
                    "value": 1,
                    "name": "\u897f\u5173"
                },
                {
                    "value": 1,
                    "name": "\u5357\u6cb9"
                },
                {
                    "value": 1,
                    "name": "\u9ec4\u57d4\u533a"
                },
                {
                    "value": 1,
                    "name": "\u4e1c\u56db"
                },
                {
                    "value": 1,
                    "name": "\u5e73\u6e56"
                },
                {
                    "value": 1,
                    "name": "\u5e7f\u5dde"
                },
                {
                    "value": 1,
                    "name": "\u5458\u6751"
                },
                {
                    "value": 1,
                    "name": "\u5b81\u56f4"
                },
                {
                    "value": 1,
                    "name": "\u90d1\u4e1c\u65b0\u2026"
                },
                {
                    "value": 1,
                    "name": "\u91d1\u6c34\u533a"
                },
                {
                    "value": 1,
                    "name": "\u6253\u6d66\u6865"
                },
                {
                    "value": 1,
                    "name": "\u4e94\u5c71"
                },
                {
                    "value": 1,
                    "name": "\u90eb\u90fd\u533a"
                },
                {
                    "value": 1,
                    "name": "\u6f15\u5b9d\u8def"
                },
                {
                    "value": 1,
                    "name": "\u6b66\u6c49\u7ecf\u2026"
                },
                {
                    "value": 1,
                    "name": "\u897f\u82d1"
                },
                {
                    "value": 1,
                    "name": "\u4eac\u5e7f\u6865"
                },
                {
                    "value": 1,
                    "name": "\u78a7\u4e91\u793e\u2026"
                },
                {
                    "value": 1,
                    "name": "\u4e8c\u90ce"
                },
                {
                    "value": 1,
                    "name": "\u57ce\u968d\u5e99"
                },
                {
                    "value": 1,
                    "name": "\u4e07\u5bff\u5bfa"
                },
                {
                    "value": 1,
                    "name": "\u5c0f\u5173"
                },
                {
                    "value": 1,
                    "name": "\u8f6f\u4ef6\u56ed"
                },
                {
                    "value": 1,
                    "name": "\u5c55\u89c8\u8def"
                },
                {
                    "value": 1,
                    "name": "\u5cb3\u9e93\u533a"
                },
                {
                    "value": 1,
                    "name": "\u592a\u548c"
                },
                {
                    "value": 1,
                    "name": "\u4e07\u67f3"
                },
                {
                    "value": 1,
                    "name": "\u5f00\u53d1\u533a"
                },
                {
                    "value": 1,
                    "name": "\u89c2\u6c99\u5cad"
                },
                {
                    "value": 1,
                    "name": "\u6dd8\u91d1"
                },
                {
                    "value": 1,
                    "name": "\u6731\u96c0\u5927\u2026"
                },
                {
                    "value": 1,
                    "name": "\u576a\u5c71\u65b0\u2026"
                },
                {
                    "value": 1,
                    "name": "\u91d1\u6865"
                },
                {
                    "value": 1,
                    "name": "\u767b\u5cf0"
                },
                {
                    "value": 1,
                    "name": "\u8096\u5bb6\u6cb3"
                },
                {
                    "value": 1,
                    "name": "\u53cc\u6986\u6811"
                },
                {
                    "value": 1,
                    "name": "\u592a\u5e73\u6865"
                },
                {
                    "value": 1,
                    "name": "\u4e1c\u839e\u5e02\u2026"
                },
                {
                    "value": 1,
                    "name": "\u9ec4\u5c9b\u533a"
                },
                {
                    "value": 1,
                    "name": "\u60e0\u9633\u533a"
                },
                {
                    "value": 1,
                    "name": "\u6885\u9647"
                },
                {
                    "value": 1,
                    "name": "\u6c5f\u5cb8\u533a"
                },
                {
                    "value": 1,
                    "name": "\u4eae\u9a6c\u6865"
                },
                {
                    "value": 1,
                    "name": "\u5ba3\u6b66\u95e8"
                },
                {
                    "value": 1,
                    "name": "\u8679\u6865"
                },
                {
                    "value": 1,
                    "name": "\u5d02\u5c71\u533a"
                },
                {
                    "value": 1,
                    "name": "\u5317\u4eac\u5927\u2026"
                },
                {
                    "value": 1,
                    "name": "\u4e08\u516b"
                },
                {
                    "value": 1,
                    "name": "\u5d07\u660e\u53bf"
                },
                {
                    "value": 1,
                    "name": "\u8f66\u516c\u5e99"
                },
                {
                    "value": 1,
                    "name": "\u957f\u9633\u8def"
                },
                {
                    "value": 1,
                    "name": "\u4e09\u91cc\u6cb3"
                },
                {
                    "value": 1,
                    "name": "\u83b2\u82b1\u4e8c\u2026"
                },
                {
                    "value": 1,
                    "name": "\u5434\u4e2d\u533a"
                },
                {
                    "value": 1,
                    "name": "\u8299\u84c9\u533a"
                },
                {
                    "value": 1,
                    "name": "\u6c5f\u5357"
                },
                {
                    "value": 1,
                    "name": "\u95f2\u6797"
                },
                {
                    "value": 1,
                    "name": "\u5de6\u5bb6\u5e84"
                },
                {
                    "value": 1,
                    "name": "\u6e1d\u5317\u533a"
                },
                {
                    "value": 1,
                    "name": "\u957f\u5bff\u8def"
                },
                {
                    "value": 1,
                    "name": "\u65b0\u534e\u8def"
                },
                {
                    "value": 1,
                    "name": "\u7530\u6751"
                },
                {
                    "value": 1,
                    "name": "\u9526\u6c5f\u533a"
                },
                {
                    "value": 1,
                    "name": "\u5965\u4f53"
                },
                {
                    "value": 1,
                    "name": "\u8df3\u4f1e\u5854"
                },
                {
                    "value": 1,
                    "name": "\u8f66\u7ad9"
                },
                {
                    "value": 1,
                    "name": "\u4eba\u548c"
                },
                {
                    "value": 1,
                    "name": "\u540e\u6d77"
                },
                {
                    "value": 1,
                    "name": "\u5317\u592a\u5e73\u2026"
                },
                {
                    "value": 1,
                    "name": "\u9f99\u6eaa"
                },
                {
                    "value": 1,
                    "name": "\u6c5f\u590f\u533a"
                },
                {
                    "value": 1,
                    "name": "\u5929\u5c71\u8def"
                },
                {
                    "value": 1,
                    "name": "\u56db\u5b63\u9752"
                },
                {
                    "value": 1,
                    "name": "\u91d1\u878d\u8857"
                },
                {
                    "value": 1,
                    "name": "\u841d\u5c97\u533a"
                },
                {
                    "value": 1,
                    "name": "\u8f66\u9642"
                },
                {
                    "value": 1,
                    "name": "\u5143\u548c"
                },
                {
                    "value": 1,
                    "name": "\u4e07\u6cc9\u6cb3"
                },
                {
                    "value": 1,
                    "name": "\u69d0\u836b\u533a"
                },
                {
                    "value": 1,
                    "name": "\u897f\u5c71"
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
                "\u5c97\u4f4d\u5206\u5e03\u6811\u72b6\u56fe"
            ],
            "selected": {
                "\u5c97\u4f4d\u5206\u5e03\u6811\u72b6\u56fe": true
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
            "text": "\u5730\u533a\u5206\u5e03\u6811\u72b6\u56fe",
            "padding": 5,
            "itemGap": 10
        }
    ]
};
        chart_94ba5219eb84465188efe2a54c0e87f1.setOption(option_94ba5219eb84465188efe2a54c0e87f1);
    </script>
                <div id="ef66dffff7f444ef9306782c92d2be65" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_ef66dffff7f444ef9306782c92d2be65 = echarts.init(
            document.getElementById('ef66dffff7f444ef9306782c92d2be65'), 'white', {renderer: 'canvas'});
        var option_ef66dffff7f444ef9306782c92d2be65 = {
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
                303,
                255,
                209,
                172,
                122,
                119,
                75,
                69
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
                    "name": "\u4e0a\u5e02\u516c\u53f8",
                    "value": 303
                },
                {
                    "name": "\u4e0d\u9700\u8981\u878d\u8d44",
                    "value": 255
                },
                {
                    "name": "A\u8f6e",
                    "value": 209
                },
                {
                    "name": "B\u8f6e",
                    "value": 172
                },
                {
                    "name": "D\u8f6e\u53ca\u4ee5\u4e0a",
                    "value": 122
                },
                {
                    "name": "\u672a\u878d\u8d44",
                    "value": 119
                },
                {
                    "name": "C\u8f6e",
                    "value": 75
                },
                {
                    "name": "\u5929\u4f7f\u8f6e",
                    "value": 69
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
                    "name": "\u4e0a\u5e02\u516c\u53f8",
                    "value": 303
                },
                {
                    "name": "\u4e0d\u9700\u8981\u878d\u8d44",
                    "value": 255
                },
                {
                    "name": "A\u8f6e",
                    "value": 209
                },
                {
                    "name": "B\u8f6e",
                    "value": 172
                },
                {
                    "name": "D\u8f6e\u53ca\u4ee5\u4e0a",
                    "value": 122
                },
                {
                    "name": "\u672a\u878d\u8d44",
                    "value": 119
                },
                {
                    "name": "C\u8f6e",
                    "value": 75
                },
                {
                    "name": "\u5929\u4f7f\u8f6e",
                    "value": 69
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
                "\u4e0a\u5e02\u516c\u53f8",
                "\u4e0d\u9700\u8981\u878d\u8d44",
                "A\u8f6e",
                "B\u8f6e",
                "D\u8f6e\u53ca\u4ee5\u4e0a",
                "\u672a\u878d\u8d44",
                "C\u8f6e",
                "\u5929\u4f7f\u8f6e"
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
                "\u4e0a\u5e02\u516c\u53f8",
                "\u4e0d\u9700\u8981\u878d\u8d44",
                "A\u8f6e",
                "B\u8f6e",
                "D\u8f6e\u53ca\u4ee5\u4e0a",
                "\u672a\u878d\u8d44",
                "C\u8f6e",
                "\u5929\u4f7f\u8f6e"
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
            "text": "\u516c\u53f8\u89c4\u6a21",
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
        chart_ef66dffff7f444ef9306782c92d2be65.setOption(option_ef66dffff7f444ef9306782c92d2be65);
    </script>
                <div id="9e057d9f60944db9b9782ccee28090dd" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_9e057d9f60944db9b9782ccee28090dd = echarts.init(
            document.getElementById('9e057d9f60944db9b9782ccee28090dd'), 'white', {renderer: 'canvas'});
        var option_9e057d9f60944db9b9782ccee28090dd = {
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
                359,
                289,
                255,
                249,
                157,
                15
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
                    "name": "2000\u4eba\u4ee5\u4e0a",
                    "value": 359
                },
                {
                    "name": "150-500\u4eba",
                    "value": 289
                },
                {
                    "name": "50-150\u4eba",
                    "value": 255
                },
                {
                    "name": "500-2000\u4eba",
                    "value": 249
                },
                {
                    "name": "15-50\u4eba",
                    "value": 157
                },
                {
                    "name": "\u5c11\u4e8e15\u4eba",
                    "value": 15
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
                    "name": "2000\u4eba\u4ee5\u4e0a",
                    "value": 359
                },
                {
                    "name": "150-500\u4eba",
                    "value": 289
                },
                {
                    "name": "50-150\u4eba",
                    "value": 255
                },
                {
                    "name": "500-2000\u4eba",
                    "value": 249
                },
                {
                    "name": "15-50\u4eba",
                    "value": 157
                },
                {
                    "name": "\u5c11\u4e8e15\u4eba",
                    "value": 15
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
                "2000\u4eba\u4ee5\u4e0a",
                "150-500\u4eba",
                "50-150\u4eba",
                "500-2000\u4eba",
                "15-50\u4eba",
                "\u5c11\u4e8e15\u4eba"
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
                "2000\u4eba\u4ee5\u4e0a",
                "150-500\u4eba",
                "50-150\u4eba",
                "500-2000\u4eba",
                "15-50\u4eba",
                "\u5c11\u4e8e15\u4eba"
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
            "text": "\u4eba\u5458\u89c4\u6a21",
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
        chart_9e057d9f60944db9b9782ccee28090dd.setOption(option_9e057d9f60944db9b9782ccee28090dd);
    </script>
                <div id="8e1b97b4ac3c4d2eb1ffeca243937b4f" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_8e1b97b4ac3c4d2eb1ffeca243937b4f = echarts.init(
            document.getElementById('8e1b97b4ac3c4d2eb1ffeca243937b4f'), 'white', {renderer: 'canvas'});
        var option_8e1b97b4ac3c4d2eb1ffeca243937b4f = {
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
                377,
                215,
                132,
                127,
                118,
                90,
                77
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
            "name": "\u884c\u4e1a\u5206\u5e03",
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
                    "name": "\u54a8\u8be2",
                    "value": 377,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,42,33)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u670d\u52a1",
                    "value": 215,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,49,150)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u670d\u52a1",
                    "value": 132,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,116,102)"
                        }
                    }
                },
                {
                    "name": "\u8f6f\u4ef6\u670d\u52a1",
                    "value": 127,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,157,43)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u786c\u4ef6",
                    "value": 118,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,132,3)"
                        }
                    }
                },
                {
                    "name": "IT\u6280\u672f\u670d\u52a1",
                    "value": 90,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,94,118)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u6280\u91d1\u878d",
                    "value": 77,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,79,10)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546\u5e73\u53f0",
                    "value": 66,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,29,79)"
                        }
                    }
                },
                {
                    "name": "\u79fb\u52a8\u4e92\u8054\u7f51",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,137,139)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u5177\u7c7b\u4ea7\u54c1",
                    "value": 61,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,142,52)"
                        }
                    }
                },
                {
                    "name": "\u4f01\u4e1a\u670d\u52a1",
                    "value": 52,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,7,24)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd",
                    "value": 50,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,128,58)"
                        }
                    }
                },
                {
                    "name": "\u7269\u8054\u7f51",
                    "value": 44,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,104,129)"
                        }
                    }
                },
                {
                    "name": "\u6d88\u8d39\u751f\u6d3b",
                    "value": 43,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,10,3)"
                        }
                    }
                },
                {
                    "name": "\u6e38\u620f",
                    "value": 42,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,110,24)"
                        }
                    }
                },
                {
                    "name": "\u5176\u4ed6",
                    "value": 41,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,49,86)"
                        }
                    }
                },
                {
                    "name": "\u5728\u7ebf\u6559\u80b2",
                    "value": 41,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,17,47)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u8d44\u8baf",
                    "value": 41,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,43,95)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u793e\u533a",
                    "value": 39,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,15,113)"
                        }
                    }
                },
                {
                    "name": "\u77ed\u89c6\u9891",
                    "value": 35,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,110,151)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u4e1a\u670d\u52a1",
                    "value": 35,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,131,75)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4ea4\u5e73\u53f0",
                    "value": 33,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,82,142)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u5b89\u5168",
                    "value": 33,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,127,79)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u9891",
                    "value": 32,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,107,51)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u5a92\u4f53",
                    "value": 32,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,26,73)"
                        }
                    }
                },
                {
                    "name": "\u8425\u9500\u670d\u52a1",
                    "value": 30,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,2,45)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u6e38",
                    "value": 30,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,7,111)"
                        }
                    }
                },
                {
                    "name": "\u51fa\u884c",
                    "value": 29,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,63,75)"
                        }
                    }
                },
                {
                    "name": "\u5236\u9020\u4e1a",
                    "value": 26,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,13,19)"
                        }
                    }
                },
                {
                    "name": "\u7269\u6d41",
                    "value": 22,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,110,84)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u8f93",
                    "value": 22,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,11,141)"
                        }
                    }
                },
                {
                    "name": "\u786c\u4ef6",
                    "value": 22,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,100,17)"
                        }
                    }
                },
                {
                    "name": "\u5728\u7ebf\u533b\u7597",
                    "value": 22,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,101,92)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u4e1a",
                    "value": 21,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,110,102)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u4e28\u5065\u5eb7",
                    "value": 20,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,22,30)"
                        }
                    }
                },
                {
                    "name": "\u8f6f\u4ef6\u5f00\u53d1",
                    "value": 18,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,11,32)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u68c0\u7d22",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,133,31)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,147,72)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4ea4\u5a92\u4f53",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,147,158)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u96f6\u552e",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,77,101)"
                        }
                    }
                },
                {
                    "name": "\u7269\u6d41\u5e73\u53f0",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,75,111)"
                        }
                    }
                },
                {
                    "name": "\u7269\u4e1a",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,2,91)"
                        }
                    }
                },
                {
                    "name": "\u5efa\u7b51",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,29,11)"
                        }
                    }
                },
                {
                    "name": "\u623f\u5730\u4ea7",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,136,42)"
                        }
                    }
                },
                {
                    "name": "\u5c45\u4f4f\u670d\u52a1",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,116,74)"
                        }
                    }
                },
                {
                    "name": "\u76f4\u64ad\u5e73\u53f0",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,127,92)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u7edc\u901a\u4fe1",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,100,136)"
                        }
                    }
                },
                {
                    "name": "MCN",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,54,57)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,13,81)"
                        }
                    }
                },
                {
                    "name": "\u6559\u80b2",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,153,43)"
                        }
                    }
                },
                {
                    "name": "\u533a\u5757\u94fe",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,101,31)"
                        }
                    }
                },
                {
                    "name": "\u8fdb\u51fa\u53e3",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,29,74)"
                        }
                    }
                },
                {
                    "name": "\u6279\u53d1",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,52,71)"
                        }
                    }
                },
                {
                    "name": "\u8d38\u6613",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,26,63)"
                        }
                    }
                },
                {
                    "name": "\u6587\u5a31\u4e28\u5185\u5bb9",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,129,17)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u552e",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,26,63)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5a92\u4f53",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,11,145)"
                        }
                    }
                },
                {
                    "name": "\u901a\u8baf\u7535\u5b50",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,58,25)"
                        }
                    }
                },
                {
                    "name": "\u5a31\u4e50",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,146,67)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,53,9)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u5177",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,41,72)"
                        }
                    }
                },
                {
                    "name": "\u4f11\u95f2",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,151,30)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u5bb9",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,131,67)"
                        }
                    }
                },
                {
                    "name": "\u4fdd\u5065",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,114,146)"
                        }
                    }
                },
                {
                    "name": "\u7269\u6d41\u4e28\u8fd0\u8f93",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,126,17)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u80fd\u6e90\u6c7d\u8f66\u5236\u9020",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,57,5)"
                        }
                    }
                },
                {
                    "name": "\u6c7d\u8f66\u4e28\u51fa\u884c",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,59,85)"
                        }
                    }
                },
                {
                    "name": "\u751f\u6d3b\u670d\u52a1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,25,130)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4ea4",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,160,63)"
                        }
                    }
                },
                {
                    "name": "\u57f9\u8bad",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,28,110)"
                        }
                    }
                },
                {
                    "name": "\u6c7d\u8f66\u4ea4\u6613\u5e73\u53f0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,103,61)"
                        }
                    }
                },
                {
                    "name": "\u52a8\u6f2b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,20,33)"
                        }
                    }
                },
                {
                    "name": "\u623f\u4ea7\u5bb6\u5c45",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,60,41)"
                        }
                    }
                },
                {
                    "name": "\u5f71\u89c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,86,83)"
                        }
                    }
                },
                {
                    "name": "\u519c\u6797\u7267\u6e14",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,72,42)"
                        }
                    }
                },
                {
                    "name": "\u73af\u4fdd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,98,133)"
                        }
                    }
                },
                {
                    "name": "\u4f01\u4e1a\u670d\u52a1 \u8f6f\u4ef6\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,159,110)"
                        }
                    }
                },
                {
                    "name": "\u77ff\u4ea7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,81,8)"
                        }
                    }
                },
                {
                    "name": "\u80fd\u6e90",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,66,75)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u3001\u6c7d\u8f66\u4e28\u51fa\u884c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,57,67)"
                        }
                    }
                },
                {
                    "name": "\u6587\u5316\u4f20\u5a92",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,33,25)"
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
                "\u54a8\u8be2",
                "\u4eba\u5de5\u667a\u80fd\u670d\u52a1",
                "\u6570\u636e\u670d\u52a1",
                "\u8f6f\u4ef6\u670d\u52a1",
                "\u667a\u80fd\u786c\u4ef6",
                "IT\u6280\u672f\u670d\u52a1",
                "\u79d1\u6280\u91d1\u878d"
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
            "text": "\u884c\u4e1a\u5206\u5e03",
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
            "top": "55%",
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
        chart_8e1b97b4ac3c4d2eb1ffeca243937b4f.setOption(option_8e1b97b4ac3c4d2eb1ffeca243937b4f);
    </script>
                <div id="e90296e156434267af332b558f71c03d" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_e90296e156434267af332b558f71c03d = echarts.init(
            document.getElementById('e90296e156434267af332b558f71c03d'), 'white', {renderer: 'canvas'});
        var option_e90296e156434267af332b558f71c03d = {
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
                372,
                81,
                67,
                54,
                51,
                35,
                24
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
            "name": "\u7b97\u6cd5\u65b9\u5411\u5206\u6790",
            "shape": "circle",
            "rotationRange": [
                -90,
                90
            ],
            "rotationStep": 45,
            "girdSize": 20,
            "sizeRange": [
                18,
                50
            ],
            "data": [
                {
                    "name": "\u7b97\u6cd5",
                    "value": 372,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,103,96)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u7b97\u6cd5",
                    "value": 81,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,38,92)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u7b97\u6cd5",
                    "value": 67,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,155,152)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 54,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,45,55)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5",
                    "value": 51,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,77,114)"
                        }
                    }
                },
                {
                    "name": "AI\u7b97\u6cd5",
                    "value": 35,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,42,92)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                    "value": 24,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,32,134)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9\u7b97\u6cd5",
                    "value": 22,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,34,82)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u9891\u7b97\u6cd5",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,34,95)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u7b97\u6cd5",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,132,128)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u7b97\u6cd5",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,4,71)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u673a\u89c6\u89c9\u7b97\u6cd5",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,98,126)"
                        }
                    }
                },
                {
                    "name": "slam\u7b97\u6cd5",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,103,19)"
                        }
                    }
                },
                {
                    "name": "ai\u7b97\u6cd5",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,9,12)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u63a8\u8350\u7b97\u6cd5",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,98,14)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7136\u8bed\u8a00\u5904\u7406\u7b97\u6cd5",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,130,110)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7\u7b97\u6cd5",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,20,160)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u7b97\u6cd5",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,114,59)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u8bc6\u522b\u7b97\u6cd5",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,113,120)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u7b97\u6cd5",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,30,85)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u56fe\u50cf\u7b97\u6cd5",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,119,117)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62\u7b97\u6cd5",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,116,7)"
                        }
                    }
                },
                {
                    "name": "\u611f\u77e5\u7b97\u6cd5",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,143,77)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u63a8\u8350\u7b97\u6cd5",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,9,153)"
                        }
                    }
                },
                {
                    "name": "SLAM\u7b97\u6cd5",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,8,47)"
                        }
                    }
                },
                {
                    "name": "\u5bfc\u822a\u7b97\u6cd5",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,113,150)"
                        }
                    }
                },
                {
                    "name": "ocr\u7b97\u6cd5",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,108,29)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u8bc6\u522b\u7b97\u6cd5",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,6,107)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6316\u6398\u7b97\u6cd5",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,124,40)"
                        }
                    }
                },
                {
                    "name": "\u63a7\u5236\u7b97\u6cd5",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,87,34)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u7b97\u6cd5",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,144,48)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7AI\u7b97\u6cd5",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,141,81)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u7b97\u6cd5",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,89,23)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u7b97\u6cd5",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,76,139)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7b97\u6cd5",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,9,115)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u89c6\u89c9\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,9,46)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7/\u8d44\u6df1\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,135,118)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79\u4f18\u5316\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,24,116)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u53f7\u5904\u7406 \u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,38,39)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,144,68)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,117,132)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u7814\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,127,116)"
                        }
                    }
                },
                {
                    "name": "\u9884\u6d4b\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,110,5)"
                        }
                    }
                },
                {
                    "name": "\u5730\u56fe\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,75,83)"
                        }
                    }
                },
                {
                    "name": "3D\u91cd\u5efa\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,40,44)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u7ea7\u56fe\u50cf\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,108,56)"
                        }
                    }
                },
                {
                    "name": "CV\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,117,128)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,11,160)"
                        }
                    }
                },
                {
                    "name": "O2O\u5373\u65f6\u914d\u9001\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,35,111)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u4f4d\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,11,38)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u8bc6\u56fe\u8c31\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,110,95)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u5408\u6210\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,13,112)"
                        }
                    }
                },
                {
                    "name": "\u51b3\u7b56\u89c4\u5212\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,48,35)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u641c\u7d22\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,155,118)"
                        }
                    }
                },
                {
                    "name": "AR\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,93,116)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5904\u7406\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,83,136)"
                        }
                    }
                },
                {
                    "name": "\u8682\u8681\u96c6\u56e2-\u63a8\u8350\u641c\u7d22\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,37,140)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u97f3\u9891\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,84,132)"
                        }
                    }
                },
                {
                    "name": "\u51e0\u4f55\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,86,26)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7f16\u7801\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,138,77)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,30,56)"
                        }
                    }
                },
                {
                    "name": "AI\u8d44\u6df1\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,80,64)"
                        }
                    }
                },
                {
                    "name": "OCR\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,142,89)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62\u56fe\u50cf\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,89,80)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u3001\u56fe\u50cf\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,38,11)"
                        }
                    }
                },
                {
                    "name": "\u5171\u8bc6\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,13,122)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u56fe\u50cf\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,70,48)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u5e7f\u544a\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,44,137)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u63a7\u5236\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,113,131)"
                        }
                    }
                },
                {
                    "name": "\u7b56\u7565\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,97,113)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u7cfb\u7edf\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,40,118)"
                        }
                    }
                },
                {
                    "name": "AI \u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,148,37)"
                        }
                    }
                },
                {
                    "name": "\u901a\u4fe1\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,149,109)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9\u56fe\u50cf\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,25,133)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u603b\u76d1\uff08\u6570\u636e\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,92,70)"
                        }
                    }
                },
                {
                    "name": "\u589e\u957f\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,154,56)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5206\u6790\u5e08\\\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,118,133)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u5b66\u4e60/\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,119,109)"
                        }
                    }
                },
                {
                    "name": "\u533a\u5757\u94fe\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,136,35)"
                        }
                    }
                },
                {
                    "name": "\u6210\u50cf\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,31,58)"
                        }
                    }
                },
                {
                    "name": "\u6821\u62db-\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,0,63)"
                        }
                    }
                },
                {
                    "name": "2D/3D\u56fe\u5f62\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,138,36)"
                        }
                    }
                },
                {
                    "name": "TOC\u4e1a\u52a1\u7fa4O2O\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,156,74)"
                        }
                    }
                },
                {
                    "name": "\u5f3a\u5316\u5b66\u4e60\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,68,67)"
                        }
                    }
                },
                {
                    "name": "CT\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,65,51)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u641c\u7d22\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,5,85)"
                        }
                    }
                },
                {
                    "name": "\u91cf\u5316\u4ea4\u6613\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,34,48)"
                        }
                    }
                },
                {
                    "name": "\u7b56\u7565\u67b6\u6784\u7814\u53d1\u5de5\u7a0b\u5e08\uff08\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,53,108)"
                        }
                    }
                },
                {
                    "name": "\u521d\u7ea7\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,76,80)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u6570\u636e\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,149,83)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7f16\u89e3\u7801\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,105,119)"
                        }
                    }
                },
                {
                    "name": "\u9065\u611f\u56fe\u50cf\u5904\u7406\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,81,145)"
                        }
                    }
                },
                {
                    "name": "\u7c7b\u8111\u667a\u80fd\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,27,101)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u5e7f\u544a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,139,146)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u8a00\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,32,44)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u538b\u7f29\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,4,141)"
                        }
                    }
                },
                {
                    "name": "AI/\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,156,58)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u9645\u5316\u5b9a\u4ef7\u8865\u8d34\u4e13\u5bb6\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,139,79)"
                        }
                    }
                },
                {
                    "name": "MIG-\u81ea\u52a8\u9a7e\u9a76\u611f\u77e5\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,132,142)"
                        }
                    }
                },
                {
                    "name": "254138-NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,120,135)"
                        }
                    }
                },
                {
                    "name": "39314F-\u901a\u7528\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,41,142)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5206\u6790\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,85,47)"
                        }
                    }
                },
                {
                    "name": "\u51b3\u7b56\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,31,46)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6316\u6398/\u53cd\u4f5c\u5f0a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,85,91)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,32,73)"
                        }
                    }
                },
                {
                    "name": "AR\u56fe\u5f62\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,82,101)"
                        }
                    }
                },
                {
                    "name": "\u5f02\u6784\u8ba1\u7b97\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,99,80)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u7406\u89e3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,77,31)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,116,65)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,94,1)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,24,21)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u7cfb\u7edf/\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,155,101)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u5b89\u5168\u53ca\u5bc6\u7801\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,25,22)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u6d4b\u91cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,127,119)"
                        }
                    }
                },
                {
                    "name": "\u591a\u4f20\u611f\u5668\u878d\u5408\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,123,86)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u7814\u53d1\u5de5\u7a0b\u5e08-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,78,81)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,107,76)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u8bc6\u56fe\u8c31\u90e8_\u7b56\u7565\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,47,146)"
                        }
                    }
                },
                {
                    "name": "\u8054\u90a6\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,58,21)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,147,6)"
                        }
                    }
                },
                {
                    "name": "\u4f20\u7edf\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,68,106)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,25,33)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u591a\u6a21\u6001\u7406\u89e3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,46,92)"
                        }
                    }
                },
                {
                    "name": "\u7535\u78c1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,9,98)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u8425\u9500\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,12,11)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,72,7)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u548c\u89c6\u9891\u7406\u89e3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,5,3)"
                        }
                    }
                },
                {
                    "name": "\u3010\u6df1\u5733\u3011GNSS\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,51,33)"
                        }
                    }
                },
                {
                    "name": "CFD\u5f00\u6e90\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,85,62)"
                        }
                    }
                },
                {
                    "name": "\u6559\u80b2\u6d4b\u91cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,36,57)"
                        }
                    }
                },
                {
                    "name": "\u7535\u8c03\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,136,147)"
                        }
                    }
                },
                {
                    "name": "3D\u70b9\u4e91\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,109,125)"
                        }
                    }
                },
                {
                    "name": "FPGA\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,150,57)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7136\u8bed\u8a00\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,38,96)"
                        }
                    }
                },
                {
                    "name": "\u6d4b\u8bd5\uff08\u8bed\u97f3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,65,141)"
                        }
                    }
                },
                {
                    "name": "39318E-\u8ba1\u7b97\u673a\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,35,41)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350/\u641c\u7d22\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,73,128)"
                        }
                    }
                },
                {
                    "name": "\u589e\u5f3a\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,148,87)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u5bfc\u822a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,77,72)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7/\u8d44\u6df1\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,126,94)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,61,45)"
                        }
                    }
                },
                {
                    "name": "\u4eac\u4e1c\u5e7f\u544a-\u8d44\u6df1\u5e7f\u544a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,91,132)"
                        }
                    }
                },
                {
                    "name": "2021\u6821\u62db-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,12,45)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u4e92\u5de5\u7a0b-\u521b\u610f\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,21,110)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u81ea\u7136\u8bed\u8a00\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,120,99)"
                        }
                    }
                },
                {
                    "name": "\u5916\u5356\u6280\u672f\u90e8-\u8d44\u6df1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,74,22)"
                        }
                    }
                },
                {
                    "name": "NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,67,51)"
                        }
                    }
                },
                {
                    "name": "\u65f6\u7a7a\u6570\u636e\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,54,57)"
                        }
                    }
                },
                {
                    "name": "ASR\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,72,115)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7\u6a21\u578b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,71,155)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u6392\u5e8f\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,98,102)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u68c0\u7d22\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,141,35)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u53f7\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,111,19)"
                        }
                    }
                },
                {
                    "name": "024168-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,114,77)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7/\u8d44\u6df1/\u4e13\u5bb6\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,95,91)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u56e2App-\u7528\u6237\u589e\u957f\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,43,33)"
                        }
                    }
                },
                {
                    "name": "XH4713-\u6d41\u5a92\u4f53\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,9,58)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u97f3\u9891\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,47,107)"
                        }
                    }
                },
                {
                    "name": "\u8f68\u8ff9\u8ddf\u968f\u63a7\u5236\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,63,147)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u8138\u8bc6\u522b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,51,146)"
                        }
                    }
                },
                {
                    "name": "\u533b\u5b66\u5f71\u50cf\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,117,142)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u5168\u7b56\u7565\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,66,28)"
                        }
                    }
                },
                {
                    "name": "\u641c\u72d7\u6570\u5b57\u4eba-3D\u4eba\u8138\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,1,19)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6316\u6398\u4e0e\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,105,100)"
                        }
                    }
                },
                {
                    "name": "5G\u901a\u4fe1\u667a\u80fd\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,12,151)"
                        }
                    }
                },
                {
                    "name": "MIG-\u81ea\u52a8\u9a7e\u9a76\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,16,84)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,69,113)"
                        }
                    }
                },
                {
                    "name": "\u98de\u63a7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,21,115)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546\u98ce\u63a7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,114,56)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7Gnss\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,125,9)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u51b3\u7b56\u89c4\u5212\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,53,85)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u91cd\u5efa\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,152,51)"
                        }
                    }
                },
                {
                    "name": "0232KT-\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,82,112)"
                        }
                    }
                },
                {
                    "name": "\u533b\u5b66\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,2,17)"
                        }
                    }
                },
                {
                    "name": "\u8def\u5f84\u89c4\u5212\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,20,105)"
                        }
                    }
                },
                {
                    "name": "\u60c5\u666f\u667a\u80fd\u878d\u5408\u5b9a\u4f4d\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,98,17)"
                        }
                    }
                },
                {
                    "name": "\u767e\u5ea6\u5730\u56fe\u70b9\u4e91/\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,30,24)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7f16\u89e3\u7801\u4e0e\u89c6\u9891\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,10,143)"
                        }
                    }
                },
                {
                    "name": "\u8f6f\u4ef6\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,126,92)"
                        }
                    }
                },
                {
                    "name": "\u6fc0\u5149SLAM/\u591a\u4f20\u611f\u5668\u878d\u5408\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,120,147)"
                        }
                    }
                },
                {
                    "name": "\u3010\u4e0a\u6d77\u677e\u6c5f\u533a\u3011\u6545\u969c\u9884\u6d4b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,45,6)"
                        }
                    }
                },
                {
                    "name": "NN\u964d\u566a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,46,155)"
                        }
                    }
                },
                {
                    "name": "11414F-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,14,95)"
                        }
                    }
                },
                {
                    "name": "\u8c03\u5ea6\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,112,146)"
                        }
                    }
                },
                {
                    "name": "\u51b3\u7b56\u4e0e\u8fd0\u52a8\u89c4\u5212\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,87,160)"
                        }
                    }
                },
                {
                    "name": "\u52a0\u5bc6\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,34,5)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546\u5e7f\u544a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,56,152)"
                        }
                    }
                },
                {
                    "name": "\u67b6\u6784\u5e08/\u5de5\u7a0b\u5e08\uff08\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,65,89)"
                        }
                    }
                },
                {
                    "name": "SW-\u5e94\u7528\u5f00\u53d1\u5de5\u7a0b\u5e08",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,58,66)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,31,81)"
                        }
                    }
                },
                {
                    "name": "\u957f\u5b89\u8f6f\u4ef6\u516c\u53f8-\u6fc0\u5149\u5b9a\u4f4d\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,85,17)"
                        }
                    }
                },
                {
                    "name": "0341ET-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,48,69)"
                        }
                    }
                },
                {
                    "name": "3D \u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,94,7)"
                        }
                    }
                },
                {
                    "name": "[\u6025]\u7f51\u5b89\u8d44\u6df1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,62,43)"
                        }
                    }
                },
                {
                    "name": "25318B-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,158,55)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u4eba\u9a7e\u9a76\u8f66\u8f86\u63a7\u5236\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,2,105)"
                        }
                    }
                },
                {
                    "name": "\u5b9e\u65f6\u8def\u51b5\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,66,7)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\uff08\u56fe\u50cf\u8bc6\u522b\uff09\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,39,138)"
                        }
                    }
                },
                {
                    "name": "\u5a92\u4f53\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,14,71)"
                        }
                    }
                },
                {
                    "name": "\u5782\u76f4\u884c\u4e1a\u5e7f\u544a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,121,106)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u56fe\u5f62\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,133,88)"
                        }
                    }
                },
                {
                    "name": "\u91cf\u5316\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,69,70)"
                        }
                    }
                },
                {
                    "name": "0241VZ-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,130,109)"
                        }
                    }
                },
                {
                    "name": "09412L-NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,35,105)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,104,83)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u70b9\u4e91\u5206\u6790\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,4,26)"
                        }
                    }
                },
                {
                    "name": "\u533b\u5b66\u5f71\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,51,153)"
                        }
                    }
                },
                {
                    "name": "\u5d4c\u5165\u5f0f\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,79,157)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u95fb\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,125,50)"
                        }
                    }
                },
                {
                    "name": "SPBU-\u9ad8\u7ea7\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,43,107)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u8bed\u97f3\u8bc6\u522b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,9,98)"
                        }
                    }
                },
                {
                    "name": "0341DO-NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,49,48)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u98ce\u63a7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,62,132)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,122,112)"
                        }
                    }
                },
                {
                    "name": "\u6c14\u8c61\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,34,121)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u5e7f\u544a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,105,8)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u8fd0\u52a8\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,117,108)"
                        }
                    }
                },
                {
                    "name": "\u5b9e\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,74,80)"
                        }
                    }
                },
                {
                    "name": "\u521d\u4e2d\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,119,23)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,137,25)"
                        }
                    }
                },
                {
                    "name": "0241QC-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,55,43)"
                        }
                    }
                },
                {
                    "name": "\u878d\u5408\u5b9a\u4f4d\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,136,108)"
                        }
                    }
                },
                {
                    "name": "\u3010\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,116,96)"
                        }
                    }
                },
                {
                    "name": "\u5546\u54c1\u7ecf\u8425\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,128,49)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7136\u8bed\u8a00\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,41,55)"
                        }
                    }
                },
                {
                    "name": "NLP/\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,19,121)"
                        }
                    }
                },
                {
                    "name": "\u5546\u4e1a\u641c\u7d22-\u5e7f\u544a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,22,52)"
                        }
                    }
                },
                {
                    "name": "00206-NLP\u9ad8\u7ea7\u5de5\u7a0b\u5e08/\u8d44\u6df1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,115,97)"
                        }
                    }
                },
                {
                    "name": "\u6253\u8f66\u667a\u80fd\u4f9b\u7ed9\u7b56\u7565\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,78,127)"
                        }
                    }
                },
                {
                    "name": "AY0300-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,88,108)"
                        }
                    }
                },
                {
                    "name": "Soul App-\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,62,3)"
                        }
                    }
                },
                {
                    "name": "AEB/LKA/ACC\u7814\u53d1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,43,33)"
                        }
                    }
                },
                {
                    "name": "NLP&CV\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,82,73)"
                        }
                    }
                },
                {
                    "name": "RU0112-SPBU-\u89c6\u9891\u7f16\u89e3\u7801\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,53,80)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u8ba1\u7b97\u673a\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,75,19)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u89c6\u9891\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,62,51)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u589e\u957f\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,22,11)"
                        }
                    }
                },
                {
                    "name": "\u96f7\u8fbe\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,117,11)"
                        }
                    }
                },
                {
                    "name": "\u56f4\u68cbAI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,137,46)"
                        }
                    }
                },
                {
                    "name": "Vslam\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,105,119)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u8bc4\u6d4b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,35,96)"
                        }
                    }
                },
                {
                    "name": "\u30102021\u6821\u62db-\u672a\u6765\u661f\u9879\u76ee\u3011\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,127,28)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u56fe\u7247\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,126,57)"
                        }
                    }
                },
                {
                    "name": "25215M-AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,26,123)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60/\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,62,70)"
                        }
                    }
                },
                {
                    "name": "\u5e94\u7528\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,117,68)"
                        }
                    }
                },
                {
                    "name": "\u5929\u732b\u597d\u623f-\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,44,112)"
                        }
                    }
                },
                {
                    "name": "\u6fc0\u5149\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,141,135)"
                        }
                    }
                },
                {
                    "name": "\u533b\u5b66\u5f71\u50cf\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,80,144)"
                        }
                    }
                },
                {
                    "name": "\u4eac\u4e1c\u96c6\u56e2-\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,47,83)"
                        }
                    }
                },
                {
                    "name": "\u3010\u5357\u5c71\u536b\u661f\u3011\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,3,141)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u7acb\u4f53\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,65,37)"
                        }
                    }
                },
                {
                    "name": "QQ\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,43,75)"
                        }
                    }
                },
                {
                    "name": "MIG-\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,42,115)"
                        }
                    }
                },
                {
                    "name": "\u6d41\u5a92\u4f53\u4f20\u8f93\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,84,16)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7\u53cd\u6b3a\u8bc8\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,148,67)"
                        }
                    }
                },
                {
                    "name": "\u672c\u5730\u751f\u6d3b-\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,37,96)"
                        }
                    }
                },
                {
                    "name": "FF2824-\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,102,125)"
                        }
                    }
                },
                {
                    "name": "\u3010\u7f8e\u56e2\u4f18\u9009\u3011-\u8425\u9500\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,83,86)"
                        }
                    }
                },
                {
                    "name": "\u5bf9\u8bdd\u63a8\u8350\u8d44\u6df1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,56,127)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u5e73\u53f0-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,31,156)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7/\u8d44\u6df1\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,51,148)"
                        }
                    }
                },
                {
                    "name": "DSP\u5e7f\u544a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,38,99)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u786c\u4ef6\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,32,94)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7GNSS\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,143,58)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u5168\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,18,43)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u8c03\u5ea6\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,83,132)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u56e2\u9a91\u884c-\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,27,37)"
                        }
                    }
                },
                {
                    "name": "\u4e2a\u6027\u5316\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,117,116)"
                        }
                    }
                },
                {
                    "name": "\u957f\u5b89\u8f6f\u4ef6\u516c\u53f8-\u4f17\u5305\u5730\u56fe\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,102,92)"
                        }
                    }
                },
                {
                    "name": "ADAS\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,38,127)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u4fe1\u53f7\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,55,74)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u56fe\u5f62\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,56,65)"
                        }
                    }
                },
                {
                    "name": "\u6c83\u98de\u957f\u7a7a-\u6280\u672f\u7814\u53d1\u4e2d\u5fc3-\u98de\u884c\u63a7\u5236\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,61,59)"
                        }
                    }
                },
                {
                    "name": "\u589e\u957f\u6295\u653e\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,35,137)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,100,33)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u8d37\u6a21\u578b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,125,85)"
                        }
                    }
                },
                {
                    "name": "\u6e32\u67d3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,21,23)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u70b9\u4e91\u5206\u6790\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,52,99)"
                        }
                    }
                },
                {
                    "name": "AF\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,18,141)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7cbe\u5730\u56fe\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,127,29)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u8bc6\u522b\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,13,58)"
                        }
                    }
                },
                {
                    "name": "SLAM/VIO/\u4e09\u7ef4\u91cd\u5efa\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,39,116)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u56e2App-\u7f8e\u56e2\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,49,144)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6316\u6398\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,80,86)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62\u5b66\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,0,157)"
                        }
                    }
                },
                {
                    "name": "\u7535\u673a\u9a71\u52a8\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,139,81)"
                        }
                    }
                },
                {
                    "name": "55413P-AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,46,115)"
                        }
                    }
                },
                {
                    "name": "\u89c4\u5212\u5bfc\u822a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,64,53)"
                        }
                    }
                },
                {
                    "name": "\u5929\u732b\u7cbe\u7075\u4e8b\u4e1a\u90e8-\u8bed\u97f3\u5408\u6210\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,111,96)"
                        }
                    }
                },
                {
                    "name": "3D\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,142,155)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546\u7b56\u7565\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,143,47)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u4e0eNLP\u90e8-\u641c\u7d22\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,141,57)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u5e73\u53f0\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,68,153)"
                        }
                    }
                },
                {
                    "name": "05412O-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,103,123)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u5e73\u53f0-\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,139,156)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9\u5b9a\u4f4d\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,160,117)"
                        }
                    }
                },
                {
                    "name": "ASR/TTS\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,21,126)"
                        }
                    }
                },
                {
                    "name": "0232S5-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,48,28)"
                        }
                    }
                },
                {
                    "name": "\u58f0\u5b66\u6a21\u578b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,156,159)"
                        }
                    }
                },
                {
                    "name": "TTS\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,110,104)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u611f\u77e5\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,134,0)"
                        }
                    }
                },
                {
                    "name": "\u58f0\u7eb9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,150,106)"
                        }
                    }
                },
                {
                    "name": "26310R-\u81ea\u7136\u8bed\u8a00\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,12,131)"
                        }
                    }
                },
                {
                    "name": "\u6c83\u98de\u957f\u7a7a-\u884c\u4e1a\u89e3\u51b3\u65b9\u6848\u53ca\u4ea7\u54c1\u5e73\u53f0-\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,128,142)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u4fe1\u53f7\u5904\u7406/\u8bed\u97f3\u8bc6\u522b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,110,82)"
                        }
                    }
                },
                {
                    "name": "\u9884\u4f30\u6a21\u578b \u7528\u6237\u753b\u50cf \u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,121,75)"
                        }
                    }
                },
                {
                    "name": "\u5bc6\u7801\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,37,67)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7136\u8bed\u8a00\u5904\u7406\u90e8_ \u81ea\u7136\u8bed\u8a00\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,48,50)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u89c4\u5212\u4e0e\u51b3\u7b56\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,59,69)"
                        }
                    }
                },
                {
                    "name": "\u4f9b\u5e94\u94fe\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,99,118)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u4e0e\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,25,48)"
                        }
                    }
                },
                {
                    "name": "1141BI-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,119,130)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7\u7b56\u7565\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,38,152)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,46,21)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u63a7\u5236\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,12,63)"
                        }
                    }
                },
                {
                    "name": "SG8103-SPBU-\u89c6\u9891\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,152,129)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u5e94\u7528\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,89,103)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u641c\u7d22\u5e7f\u544a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,27,2)"
                        }
                    }
                },
                {
                    "name": "1131OJ-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,141,1)"
                        }
                    }
                },
                {
                    "name": "\u3010\u6821\u62db\u3011\u641c\u7d22\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,48,156)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u7ea7AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,34,118)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5efa\u6a21\uff08\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,145,21)"
                        }
                    }
                },
                {
                    "name": "0241VF-NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,127,110)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u89c6\u89c9/\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,143,80)"
                        }
                    }
                },
                {
                    "name": "\u70b9\u4e91\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,60,73)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,2,96)"
                        }
                    }
                },
                {
                    "name": "324121-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,25,144)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u5316\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,96,118)"
                        }
                    }
                },
                {
                    "name": "AI\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,101,45)"
                        }
                    }
                },
                {
                    "name": "\u6fc0\u5149\u5b9a\u4f4d\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,24,104)"
                        }
                    }
                },
                {
                    "name": "\u6fc0\u5149slam\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,65,149)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u8ba1\u7b97\u673a\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,115,11)"
                        }
                    }
                },
                {
                    "name": "5G\u57fa\u5e26\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,146,3)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf/OCR\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,12,8)"
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
                "\u7b97\u6cd5",
                "\u63a8\u8350\u7b97\u6cd5",
                "\u56fe\u50cf\u7b97\u6cd5",
                "\u9ad8\u7ea7\u7b97\u6cd5",
                "\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5",
                "AI\u7b97\u6cd5",
                "\u673a\u5668\u5b66\u4e60\u7b97\u6cd5"
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
            "text": "\u7b97\u6cd5\u65b9\u5411\u5206\u6790",
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
            "top": "55%",
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
        chart_e90296e156434267af332b558f71c03d.setOption(option_e90296e156434267af332b558f71c03d);
    </script>
                <div id="c8ef1fb9cfe447dbb6a3c3b4d49f723f" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_c8ef1fb9cfe447dbb6a3c3b4d49f723f = echarts.init(
            document.getElementById('c8ef1fb9cfe447dbb6a3c3b4d49f723f'), 'white', {renderer: 'canvas'});
            
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
    
        var option_c8ef1fb9cfe447dbb6a3c3b4d49f723f = {
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
            "name": "\u798f\u5229&\u4f18\u52bf",
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
                    "name": "\u4e94\u9669\u4e00\u91d1",
                    "value": 189,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,93,94)"
                        }
                    }
                },
                {
                    "name": "\u516d\u9669\u4e00\u91d1",
                    "value": 85,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,50,53)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u7a7a\u95f4\u5927",
                    "value": 80,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,49,18)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u5e74\u5047",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,18,106)"
                        }
                    }
                },
                {
                    "name": "\u5468\u672b\u53cc\u4f11",
                    "value": 75,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,45,32)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u4f11",
                    "value": 57,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,67,86)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956",
                    "value": 54,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,114,77)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u5de5\u4f5c",
                    "value": 53,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,120,17)"
                        }
                    }
                },
                {
                    "name": "\u8282\u65e5\u798f\u5229",
                    "value": 41,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,11,69)"
                        }
                    }
                },
                {
                    "name": "\u7ee9\u6548\u5956\u91d1",
                    "value": 38,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,118,92)"
                        }
                    }
                },
                {
                    "name": "\u4e0b\u5348\u8336",
                    "value": 37,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,34,129)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5e73\u53f0",
                    "value": 34,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,82,91)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u5316\u7ba1\u7406",
                    "value": 33,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,157,76)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u597d",
                    "value": 30,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,100,68)"
                        }
                    }
                },
                {
                    "name": "\u80a1\u7968\u671f\u6743",
                    "value": 29,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,89,116)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4\u597d",
                    "value": 29,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,138,137)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5e02\u516c\u53f8",
                    "value": 27,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,123,122)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u671f\u4f53\u68c0",
                    "value": 27,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,7,125)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u597d",
                    "value": 27,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,36,104)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u7ba1\u7406",
                    "value": 27,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,90,36)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u725b",
                    "value": 26,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,65,157)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4\u597d",
                    "value": 25,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,48,155)"
                        }
                    }
                },
                {
                    "name": "\u9886\u5bfcnice",
                    "value": 25,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,120,131)"
                        }
                    }
                },
                {
                    "name": "\u9910\u8865",
                    "value": 23,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,70,150)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u4e91\u96c6",
                    "value": 23,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,138,107)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd",
                    "value": 22,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,53,107)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f",
                    "value": 20,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,33,9)"
                        }
                    }
                },
                {
                    "name": "\u671f\u6743\u6fc0\u52b1",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,61,110)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f\u7a7a\u95f4\u5927",
                    "value": 18,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,9,10)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u7a7a\u95f4\u5927",
                    "value": 18,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,108,112)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u5927",
                    "value": 18,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,57,66)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u4e09\u9910",
                    "value": 18,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,133,144)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u597d",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,135,120)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u91d1",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,22,38)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u5e26\u961f",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,134,13)"
                        }
                    }
                },
                {
                    "name": "\u9886\u5bfc\u597d",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,159,2)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u56e2\u961f",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,117,36)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u591a",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,152,2)"
                        }
                    }
                },
                {
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,134,83)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u4f11\u5047",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,147,56)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u7a7a\u95f4",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,45,89)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u524d\u666f\u597d",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,6,46)"
                        }
                    }
                },
                {
                    "name": "\u524d\u666f\u597d",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,46,59)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u5feb",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,55,148)"
                        }
                    }
                },
                {
                    "name": "\u671f\u6743",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,150,52)"
                        }
                    }
                },
                {
                    "name": "\u8282\u5047\u65e5\u798f\u5229",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,57,38)"
                        }
                    }
                },
                {
                    "name": "\u725b\u4eba\u56e2\u961f",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,94,41)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u5de5\u4f5c\u5236",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,20,82)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u5316",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,50,50)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5e95\u53cc\u85aa",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,128,69)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u597d",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,8,104)"
                        }
                    }
                },
                {
                    "name": "\u4e03\u9669\u4e00\u91d1",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,10,57)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5b9e\u529b\u5f3a",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,61,133)"
                        }
                    }
                },
                {
                    "name": "\u7a7a\u95f4\u5927",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,61,129)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u578b\u7814\u7a76\u9662",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,116,69)"
                        }
                    }
                },
                {
                    "name": "\u80a1\u6743\u6fc0\u52b1",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,94,101)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u901f\u53d1\u5c55",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,24,154)"
                        }
                    }
                },
                {
                    "name": "\u7cbe\u82f1\u56e2\u961f",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,126,58)"
                        }
                    }
                },
                {
                    "name": "\u4e0d\u6253\u5361",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,121,79)"
                        }
                    }
                },
                {
                    "name": "\u5065\u8eab\u623f",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,151,124)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u5956\u91d1",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,1,158)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u540d\u592e\u4f01",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,136,126)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u624d\u623f\u7968",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,30,30)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5ea6\u4f53\u68c0",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,157,20)"
                        }
                    }
                },
                {
                    "name": "\u8865\u5145\u533b\u7597",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,130,157)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u6c1b\u56f4\u597d",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,54,99)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961fnice",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,137,6)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f\u7a7a\u95f4",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,109,31)"
                        }
                    }
                },
                {
                    "name": "AI",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,24,67)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6c1b\u56f4\u597d",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,26,11)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5382",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,33,116)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u73ed\u8f66",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,103,25)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u7a7a\u95f4",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,20,132)"
                        }
                    }
                },
                {
                    "name": "\u5065\u8eab\u745c\u4f3d",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,142,12)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u4fbf\u5229",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,106,93)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u56e2\u961f",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,146,72)"
                        }
                    }
                },
                {
                    "name": "\u516d\u9669\u4e8c\u91d1",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,0,87)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u4e30\u539a",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,71,99)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,74,81)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u5efa",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,96,134)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u5927",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,48,84)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u9886\u5148",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,158,80)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u4f18\u79c0",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,114,98)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u5feb",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,59,114)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u539a\u5e74\u7ec8\u5956",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,37,24)"
                        }
                    }
                },
                {
                    "name": "\u5305\u4e09\u9910",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,156,42)"
                        }
                    }
                },
                {
                    "name": "\u524d\u666f\u5e7f\u9614",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,143,42)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5347\u7a7a\u95f4\u5927",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,156,159)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u4e1a\u52a1",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,40,16)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,125,72)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,92,101)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u9f50\u5168",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,112,38)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u4e0a\u73ed",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,32,154)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u597d",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,24,64)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u91cf\u6570\u636e",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,46,30)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u5de5\u4f5c\u65f6\u95f4",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,111,98)"
                        }
                    }
                },
                {
                    "name": "\u5c97\u4f4d\u664b\u5347",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,17,41)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u4f18\u539a",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,11,55)"
                        }
                    }
                },
                {
                    "name": "\u5348\u9910\u8865\u52a9",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,66,10)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u65f6\u95f4",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,84,2)"
                        }
                    }
                },
                {
                    "name": "\u5305\u5403",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,78,80)"
                        }
                    }
                },
                {
                    "name": "\u8865\u5145\u533b\u7597\u4fdd\u9669",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,46,112)"
                        }
                    }
                },
                {
                    "name": "\u5404\u79cd\u798f\u5229",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,68,28)"
                        }
                    }
                },
                {
                    "name": "\u4e16\u754c\u4e94\u767e\u5f3a",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,55,35)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u90e8\u95e8",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,83,107)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5047",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,72,28)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5ea6\u65c5\u6e38",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,99,0)"
                        }
                    }
                },
                {
                    "name": "\u996d\u8865",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,145,39)"
                        }
                    }
                },
                {
                    "name": "\u524d\u6cbf\u6280\u672f",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,103,63)"
                        }
                    }
                },
                {
                    "name": "\u751f\u65e5\u4f1a",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,145,8)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u5efa\u7b49",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,44,96)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u524d\u6cbf",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,36,28)"
                        }
                    }
                },
                {
                    "name": "\u7ee9\u6548\u5956",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,111,118)"
                        }
                    }
                },
                {
                    "name": "\u9910\u8865\u7b49",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,82,71)"
                        }
                    }
                },
                {
                    "name": "16\u85aa",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,130,16)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u5b66\u4e60",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,52,24)"
                        }
                    }
                },
                {
                    "name": "\u79df\u623f\u8865\u8d34",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,53,151)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u5956",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,105,75)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u957f\u5e74\u5047",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,49,88)"
                        }
                    }
                },
                {
                    "name": "\u8865\u5145\u5546\u4e1a\u4fdd\u9669",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,118,32)"
                        }
                    }
                },
                {
                    "name": "\u6709\u8f6c\u6b63\u673a\u4f1a",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,152,74)"
                        }
                    }
                },
                {
                    "name": "\u5956\u91d1\u4e30\u539a",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,89,110)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u6210\u957f",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,56,63)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u72ec\u89d2\u517d",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,20,117)"
                        }
                    }
                },
                {
                    "name": "\u671f\u6743\u80a1\u7968",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,68,121)"
                        }
                    }
                },
                {
                    "name": "\u804c\u4f4d\u664b\u5347",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,72,55)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u6c14\u5341\u8db3",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,20,138)"
                        }
                    }
                },
                {
                    "name": "\u73ed\u8f66",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,145,100)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u6c1b\u56f4\u597d",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,25,33)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f\u5feb\u901f",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,72,42)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u8865\u52a9",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,158,126)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u597d",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,39,43)"
                        }
                    }
                },
                {
                    "name": "\u8fc7\u8282\u8d39",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,122,82)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7814\u56e2\u961f",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,158,132)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u4eba\u9a7e\u9a76",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,90,86)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u4f01",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,56,88)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u989d\u5956\u91d1",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,132,68)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u4e13\u4e1a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,98,18)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u901f\u53d1\u5c55",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,80,66)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c\u798f\u5229",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,80,29)"
                        }
                    }
                },
                {
                    "name": "12\u5929\u5e74\u5047",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,32,57)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u798f\u5229",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,11,30)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u5956\u91d1",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,96,12)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,45,4)"
                        }
                    }
                },
                {
                    "name": "\u5730\u94c1\u5468\u8fb9",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,79,38)"
                        }
                    }
                },
                {
                    "name": "\u5065\u5168\u664b\u5347\u673a\u5236",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,22,145)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u5c97\u4f4d",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,115,155)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u9614\u5e73\u53f0",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,114,39)"
                        }
                    }
                },
                {
                    "name": "\u9910\u996e\u8865\u8d34",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,105,137)"
                        }
                    }
                },
                {
                    "name": "\u671d\u4e5d\u665a\u516d",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,20,100)"
                        }
                    }
                },
                {
                    "name": "\u804c\u4e1a\u5927\u725b",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,120,82)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u5de5\u65f6",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,89,24)"
                        }
                    }
                },
                {
                    "name": "\u4e0d996",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,132,79)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5065\u8eab",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,104,62)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5916\u5e02\u573a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,105,117)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4\u8f7b\u677e",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,45,49)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u7a0b\u5e08\u6587\u5316",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,155,17)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u798f\u5229",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,25,9)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u529e\u516c",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,80,85)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u878d\u6d3d",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,129,116)"
                        }
                    }
                },
                {
                    "name": "\u5927\u843d\u5730\u573a\u666f",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,41,61)"
                        }
                    }
                },
                {
                    "name": "\u8001\u677fnice",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,11,145)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u53d1\u5c55\u597d",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,154,145)"
                        }
                    }
                },
                {
                    "name": "14\u85aa",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,26,107)"
                        }
                    }
                },
                {
                    "name": "\u4e8b\u4e1a\u5355\u4f4d",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,159,38)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u5e7f",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,50,61)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u5e73\u53f0\u5927",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,49,114)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u85aa",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,66,109)"
                        }
                    }
                },
                {
                    "name": "\u80a1\u4efd\u671f\u6743",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,65,7)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u7a33\u5b9a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,36,38)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u9ad8\u901f\u53d1\u5c55",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,25,115)"
                        }
                    }
                },
                {
                    "name": "\u9910\u8d39\u8865\u8d34",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,145,17)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u901f\u6210\u957f",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,149,21)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4\u4f73",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,38,75)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u524d\u666f\u597d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,125,24)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c\u798f\u5229\u4f73",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,18,12)"
                        }
                    }
                },
                {
                    "name": "\u51fa\u6d77\u4e1a\u52a1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,79,2)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u798f\u5229\u4f73",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,159,86)"
                        }
                    }
                },
                {
                    "name": "AI\u72ec\u89d2\u517d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,63,77)"
                        }
                    }
                },
                {
                    "name": "13\u85aa",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,80,142)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u8fdb\u597d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,63,149)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u7a33\u5b9a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,35,155)"
                        }
                    }
                },
                {
                    "name": "\u673a\u4f1a\u591a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,125,73)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u673a\u4f1a\u591a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,82,141)"
                        }
                    }
                },
                {
                    "name": "\u73af\u5883\u597d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,44,101)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u4f18\u539a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,147,42)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u4f18",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,4,86)"
                        }
                    }
                },
                {
                    "name": "\u72ec\u89d2\u517d\u516c\u53f8",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,8,147)"
                        }
                    }
                },
                {
                    "name": "\u9886\u5bfcNICE",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,45,159)"
                        }
                    }
                },
                {
                    "name": "\u901a\u8baf\u8865\u8d34",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,109,64)"
                        }
                    }
                },
                {
                    "name": "\u5168\u989d\u4e94\u9669\u4e00\u91d1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,128,42)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f\u5feb",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,98,159)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u79c0\u56e2\u961f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,49,78)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u8865\u8d34",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,117,98)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4nice",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,109,34)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u6e38",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,139,23)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u6f5c\u529b",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,71,34)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u4f1a\u7a7a\u95f4\u5927",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,20,142)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u7ebf\u798f\u5229",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,25,155)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u65b9\u4fbf",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,15,143)"
                        }
                    }
                },
                {
                    "name": "\u521b\u4e1a\u56e2\u961f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,74,124)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u591a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,18,37)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c14\u6c1b\u597d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,55,117)"
                        }
                    }
                },
                {
                    "name": "\u623f\u8865",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,124,133)"
                        }
                    }
                },
                {
                    "name": "\u7269\u8054\u7f51",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,116,51)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u5927\u725b",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,0,153)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u901f\u6210\u957f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,66,56)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1\u5168\u989d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,82,153)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u597d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,114,116)"
                        }
                    }
                },
                {
                    "name": "\u671f\u6743\u5956\u52b1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,55,100)"
                        }
                    }
                },
                {
                    "name": "\u6709\u73ed\u8f66",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,156,106)"
                        }
                    }
                },
                {
                    "name": "\u51fa\u56fd\u57f9\u8bad",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,18,88)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u68d2",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,156,34)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4\u6d3b\u8dc3",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,24,144)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5e74\u8f7b",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,114,119)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1\u7b49",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,145,119)"
                        }
                    }
                },
                {
                    "name": "\u72ec\u89d2\u517d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,109,15)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6709\u7231",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,138,156)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u98df\u996e\u6599",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,25,117)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u9ad8",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,149,34)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,59,8)"
                        }
                    }
                },
                {
                    "name": "\u6781\u5ba2\u6587\u5316",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,54,90)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u9910\u98df",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,21,63)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u591a\u591a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,151,141)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5347\u7a7a\u95f4",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,130,141)"
                        }
                    }
                },
                {
                    "name": "\u521b\u4e1a\u516c\u53f8",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,117,74)"
                        }
                    }
                },
                {
                    "name": "\u524d\u666f\u53ef\u89c2",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,49,6)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u9645\u5316\u56e2\u961f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,61,102)"
                        }
                    }
                },
                {
                    "name": "\u671d\u9633\u884c\u4e1a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,8,72)"
                        }
                    }
                },
                {
                    "name": "\u591f\u6311\u6218\u591f\u523a\u6fc0",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,157,158)"
                        }
                    }
                },
                {
                    "name": "\u6253\u8f66\u62a5\u9500",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,132,74)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u5bfc\u5e08",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,132,86)"
                        }
                    }
                },
                {
                    "name": "\u51fa\u56fd\u65c5\u6e38",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,75,34)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c\u798f\u5229\u597d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,57,89)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u85aa\u9ad8\u80a1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,76,112)"
                        }
                    }
                },
                {
                    "name": "\u6280\u80fd\u57f9\u8bad",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,57,96)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4\u73af\u5883\u597d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,83,85)"
                        }
                    }
                },
                {
                    "name": "\u5165\u804c\u8d2d\u4e70\u4e94\u9669\u4e00\u91d1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,43,40)"
                        }
                    }
                },
                {
                    "name": "\u6e05\u534e\u56e2\u961f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,60,64)"
                        }
                    }
                },
                {
                    "name": "\u4e16\u754c500\u5f3a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,92,125)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5b9e\u529b",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,158,54)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5348\u9910",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,124,83)"
                        }
                    }
                },
                {
                    "name": "\u72ec\u5f53\u4e00\u9762",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,155,63)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u884c\u4e1a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,131,147)"
                        }
                    }
                },
                {
                    "name": "13\u85aa+\u5e74\u7ec8\u5956+\u5458\u5de5\u6301\u80a1\u5236\u5ea6",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,78,4)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u65c5\u6e38",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,127,127)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5168",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,46,0)"
                        }
                    }
                },
                {
                    "name": "\u5546\u4e1a\u4fdd\u9669",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,41,58)"
                        }
                    }
                },
                {
                    "name": "\u524d\u666f\u5e7f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,116,132)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u53d1\u5c55\u6f5c\u529b\u5927",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,68,94)"
                        }
                    }
                },
                {
                    "name": "\u300e\u77f3\u5934\u79d1\u6280\u300f\u730e\u5934\u804c\u4f4d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,71,111)"
                        }
                    }
                },
                {
                    "name": "\u9910\u8865\u4ea4\u8865",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,57,24)"
                        }
                    }
                },
                {
                    "name": "\u5927\u7528\u6237\u91cf",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,7,13)"
                        }
                    }
                },
                {
                    "name": "\u660e\u661f\u56e2\u961f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,11,51)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u6237\u53e3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,17,37)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u7814\u673a\u6784",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,106,81)"
                        }
                    }
                },
                {
                    "name": "\u9760\u8c31\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,100,79)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u6587\u5316\u597d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,80,53)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u7a33\u5b9a+\u6210\u957f\u664b\u5347+\u6280\u672f\u9a71\u52a8+\u80a1\u7968\u6fc0\u52b1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,68,107)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u8d28\u56e2\u961f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,103,103)"
                        }
                    }
                },
                {
                    "name": "\u4f53\u68c0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,133,133)"
                        }
                    }
                },
                {
                    "name": "\u5404\u9879\u8865\u8d34",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,75,136)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u4f11\u5047",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,6,53)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u5e7f\u9614",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,106,95)"
                        }
                    }
                },
                {
                    "name": "\u91cd\u70b9\u9879\u76ee",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,34,77)"
                        }
                    }
                },
                {
                    "name": "\u725b\u4eba\u5171\u4e8b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,51,39)"
                        }
                    }
                },
                {
                    "name": "\u6e05\u534e\u6d77\u5f52\u56e2\u961f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,39,47)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u725b\u591a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,53,69)"
                        }
                    }
                },
                {
                    "name": "\u8282\u5047\u65e5\u798f\u5229\u7b49",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,95,153)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u5956\u91d1+\u80a1\u6743/\u671f\u6743\u6fc0\u52b1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,131,56)"
                        }
                    }
                },
                {
                    "name": "\u65e0996",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,122,154)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u7a7a\u95f4\u5145\u6ee1\u60f3\u8c61",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,45,152)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u667a\u80fd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,34,148)"
                        }
                    }
                },
                {
                    "name": "\u94f6\u884c\u80cc\u666f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,12,93)"
                        }
                    }
                },
                {
                    "name": "\u5305\u9910",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,160,49)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u91d1+\u5b63\u5ea6\u5956\u91d1+\u597d\u5fc3\u60c5+\u798f\u5229\u591a\u591a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,43,133)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u7a7a\u95f4\u5927\u3002",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,7,113)"
                        }
                    }
                },
                {
                    "name": "\u901a\u8baf\u6d25\u8d34",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,141,130)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u540d\u7535\u5546\u5e73\u53f0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,138,43)"
                        }
                    }
                },
                {
                    "name": "\u51c6\u5907\u4e0a\u5e02",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,134,53)"
                        }
                    }
                },
                {
                    "name": "\u5730\u94c1\u4e0a\u76d6",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,128,147)"
                        }
                    }
                },
                {
                    "name": "\u5e02\u573a\u5316\u85aa\u916c",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,130,54)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u7f8e\u5473\u4e09\u9910",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,127,46)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u5927\u725b\u591a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,37,111)"
                        }
                    }
                },
                {
                    "name": "\u5168\u989d\u516c\u79ef\u91d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,48,74)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u8f6f\u521b\u4e1a\u56e2\u961f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,11,142)"
                        }
                    }
                },
                {
                    "name": "\u793e\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,70,76)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1\u798f\u5229\u5b8c\u5584",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,142,54)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u5e76\u53d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,124,54)"
                        }
                    }
                },
                {
                    "name": "\u5404\u79cd\u8865\u8d34",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,24,151)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5047\u591a\u591a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,47,18)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u4f01\u80cc\u666f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,51,32)"
                        }
                    }
                },
                {
                    "name": "\u73af\u5883\u4f18\u7f8e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,152,96)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5348\u665a\u9910",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,50,84)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u798f\u5229\u4f18\u539a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,113,124)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5e95\u5956\u91d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,143,5)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u843d\u5730",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,135,128)"
                        }
                    }
                },
                {
                    "name": "base",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,45,120)"
                        }
                    }
                },
                {
                    "name": "\u4f01\u4e1a\u6c1b\u56f4\u7b80\u5355",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,62,77)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u4f18\u539a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,61,148)"
                        }
                    }
                },
                {
                    "name": "\u6280\u80fd\u63d0\u5347",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,29,116)"
                        }
                    }
                },
                {
                    "name": "\u4e0d\u52a0\u73ed",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,48,85)"
                        }
                    }
                },
                {
                    "name": "\u6025\u901f\u6210\u957f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,31,35)"
                        }
                    }
                },
                {
                    "name": "\u6301\u724c\u673a\u6784",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,46,32)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u4e0a\u73ed\u65f6\u95f4",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,90,129)"
                        }
                    }
                },
                {
                    "name": "\u51fa\u6d77****0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,127,14)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,117,144)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u6709\u524d\u666f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,86,18)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u672a\u6765\u91cd\u70b9\u53d1\u5c55",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,101,135)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5b8c\u5584",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,114,146)"
                        }
                    }
                },
                {
                    "name": "\u4f9b\u5e94\u4e09\u9910",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,56,20)"
                        }
                    }
                },
                {
                    "name": ".",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,88,46)"
                        }
                    }
                },
                {
                    "name": "\u5177\u6709\u7ade\u4e89\u529b\u7684\u85aa\u8d44\u6c34\u5e73",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,30,8)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u5e74\u4e0a\u6d77\u843d\u6237",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,149,69)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u6280\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,60,83)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u67b6\u6784",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,144,12)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u725b\u6307\u5bfc",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,95,93)"
                        }
                    }
                },
                {
                    "name": "\u5165\u804c\u80a1\u7968",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,109,66)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u75c5\u5047",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,6,158)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u4e0a\u4e0b\u73ed",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,138,156)"
                        }
                    }
                },
                {
                    "name": "AI\u91d1\u878d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,128,72)"
                        }
                    }
                },
                {
                    "name": "\u7ee9\u6548\u80a1\u7968",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,129,24)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u8f7b\u6d3b\u529b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,84,56)"
                        }
                    }
                },
                {
                    "name": "\u6210\u719f\u5927\u5e73\u53f0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,155,142)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u91d12-6\u4e2a\u6708",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,51,29)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u8fdc\u7a0b\u529e\u516c",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,48,145)"
                        }
                    }
                },
                {
                    "name": "\u8bf1\u4eba\u798f\u5229",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,112,130)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u5efa\u6d3b\u52a8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,63,63)"
                        }
                    }
                },
                {
                    "name": "AI\u672a\u6765",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,73,75)"
                        }
                    }
                },
                {
                    "name": "\u8f6c\u6b63\u673a\u4f1a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,12,51)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u9614\u53d1\u5c55\u7a7a\u95f4",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,14,81)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,126,135)"
                        }
                    }
                },
                {
                    "name": "\u5168\u989d\u793e\u4fdd\u516c\u79ef\u91d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,83,14)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u901a\u9053\u5b8c\u5584",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,103,120)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u5e7f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,140,120)"
                        }
                    }
                },
                {
                    "name": "\u4f9b\u5e94\u94fe",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,20,144)"
                        }
                    }
                },
                {
                    "name": "\u529e\u516c\u73af\u5883\u4f18\u8d8a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,22,160)"
                        }
                    }
                },
                {
                    "name": "\u524d\u666f\u884c\u4e1a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,6,137)"
                        }
                    }
                },
                {
                    "name": "\u5168\u989d\u516d\u9669\u4e00\u91d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,3,74)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u533b\u7597",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,25,149)"
                        }
                    }
                },
                {
                    "name": "\u73ed\u8f66\u63a5\u9001",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,104,87)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u65e0\u9650",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,59,151)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u6e38\u6216\u6237\u5916\u62d3\u5c55\u57f9\u8bad",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,155,12)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u6f5c\u529b\u5927",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,114,109)"
                        }
                    }
                },
                {
                    "name": "\u73af\u5883\u8212\u9002",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,81,133)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u5feb\u901f\u53d1\u5c55",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,14,45)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u9879\u76ee",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,93,152)"
                        }
                    }
                },
                {
                    "name": "\u6625\u8282\u957f\u5047",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,116,69)"
                        }
                    }
                },
                {
                    "name": "\u524d\u666f\u53ef\u89c2\u3002",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,113,158)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6c1b\u56f4\u6d53\u539a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,121,19)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u60278\u5c0f\u65f6",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,142,46)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u6709\u5927\u884c\u76f4\u9500\u94f6\u884c",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,111,124)"
                        }
                    }
                },
                {
                    "name": "\u516d\u9669\u4e00\u91d1\u5168\u989d\u7f34\u7eb3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,99,79)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u673a\u5236",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,7,101)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5206\u7ea2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,5,5)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u725b\u56e2\u961f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,57,45)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u7a33\u5b9a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,67,101)"
                        }
                    }
                },
                {
                    "name": "\u6bcf\u534a\u5e74\u8c03\u85aa\u4e00\u6b21",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,120,2)"
                        }
                    }
                },
                {
                    "name": "\u72ec\u89d2\u517d\u4f01\u4e1a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,89,46)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u5496\u591a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,60,23)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u8f6c\u6b63",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,152,58)"
                        }
                    }
                },
                {
                    "name": "\u524d\u6cbf\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,115,133)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u591a\u5927\u725b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,78,106)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u900f\u660e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,41,139)"
                        }
                    }
                },
                {
                    "name": "\u4e8b\u4e1a\u7f16\u5236",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,73,134)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,38,78)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u524d\u666f\u597d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,92,108)"
                        }
                    }
                },
                {
                    "name": "\u91cd\u70b9\u673a\u6784",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,64,73)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u8d85\u597d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,151,94)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,74,31)"
                        }
                    }
                },
                {
                    "name": "\u5468\u672b\u4e0d\u52a0\u73ed",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,103,63)"
                        }
                    }
                },
                {
                    "name": "\u6e05\u534e\u6d59\u5927",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,103,56)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,29,74)"
                        }
                    }
                },
                {
                    "name": "\u672a\u6765\u53ef\u671f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,87,2)"
                        }
                    }
                },
                {
                    "name": "\u8c03\u85aa\u673a\u5236",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,22,61)"
                        }
                    }
                },
                {
                    "name": "\u6bcf\u5468\u56e2\u5efa",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,76,36)"
                        }
                    }
                },
                {
                    "name": "\u98df\u5802",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,138,36)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u6253\u5361",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,102,75)"
                        }
                    }
                },
                {
                    "name": "\u540d\u6821\u540d\u4f01",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,46,84)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u53e3\u6d6a\u5c16",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,111,58)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u6280\u672f\u9886\u5148",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,57,57)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u7b97\u6cd5\u7814\u53d1\u56e2\u961f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,136,27)"
                        }
                    }
                },
                {
                    "name": "\u4e3b\u52a8\u52a0\u85aa",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,87,150)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6d3b\u529b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,63,154)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u5236\u5ea6",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,90,83)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u9910",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,81,24)"
                        }
                    }
                },
                {
                    "name": "k12\u6559\u80b2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,145,108)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5927\u725b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,18,99)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u9ad8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,41,90)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5496\u4e91\u96c6",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,118,15)"
                        }
                    }
                },
                {
                    "name": "14-20\u85aa",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,35,12)"
                        }
                    }
                },
                {
                    "name": "15\u85aa",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,125,3)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u540d\u4f01\u4e1a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,109,112)"
                        }
                    }
                },
                {
                    "name": "2-6\u4e2a\u6708\u5e74\u7ec8\u5956",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,20,51)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5065\u5168",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,145,38)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u901f\u63d0\u5347",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,146,54)"
                        }
                    }
                },
                {
                    "name": "3D\u89c6\u89c9",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,64,101)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u63d0\u5347",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,13,119)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u5357\u4e9a\u5e02\u573a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,72,86)"
                        }
                    }
                },
                {
                    "name": "**\u56e2\u961f+\u53d1\u5c55\u7a7a\u95f4\u5927",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,160,14)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u8f7b\u5316",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,74,45)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u6838\u5fc3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,45,45)"
                        }
                    }
                },
                {
                    "name": "\u524d\u6cbf\u884c\u4e1a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,98,53)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u665a\u9910",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,138,4)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6c1b\u56f4\u6d53",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,19,62)"
                        }
                    }
                },
                {
                    "name": "\u591a\u6b21\u8c03\u85aa",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,44,16)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u52b1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,39,95)"
                        }
                    }
                },
                {
                    "name": "\u6709\u517c\u804c\u5c97\u4f4d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,142,9)"
                        }
                    }
                },
                {
                    "name": "\u5c97\u4f4d\u53d1\u5c55\u597d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,109,57)"
                        }
                    }
                },
                {
                    "name": "\u3010\u76c8\u5cf0\u79d1\u6280\u3011\u730e\u5934\u804c\u4f4d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,15,7)"
                        }
                    }
                },
                {
                    "name": "\u6ef4\u6ef4\u6253\u8f66",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,4,140)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u6e38\u57fa\u91d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,135,72)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u5e73\u53f0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,83,96)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u4f73",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,149,120)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u524d\u6cbf",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,118,45)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u5168\u9762",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,89,118)"
                        }
                    }
                },
                {
                    "name": "\u6709\u53d1\u5c55\u673a\u4f1a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,154,133)"
                        }
                    }
                },
                {
                    "name": "\u660e\u661f\u4ea7\u54c1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,87,140)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u5021\u8ffd\u6c42\u5353\u8d8a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,72,27)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u9a71\u52a8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,135,22)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u65c5\u6e38",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,158,117)"
                        }
                    }
                },
                {
                    "name": "\u8f66\u5382\u5408\u4f5c",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,48,62)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u85aa",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,109,55)"
                        }
                    }
                },
                {
                    "name": "\u5341\u4e94\u85aa",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,7,91)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u98df",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,127,117)"
                        }
                    }
                },
                {
                    "name": "\u7a33\u5b9a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,9,160)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5065\u8eab\u623f\u7406\u53d1\u5e97",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,43,43)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u9f99\u5934",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,56,86)"
                        }
                    }
                },
                {
                    "name": "\u7b7e\u5b57\u73b0\u91d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,33,23)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u96f6\u98df",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,20,102)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u98df\u5bbf",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,80,42)"
                        }
                    }
                },
                {
                    "name": "\u5305\u4f4f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,81,150)"
                        }
                    }
                },
                {
                    "name": "\u7a33\u5b9a\u6027\u597d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,68,124)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u671f\u57f9\u8bad",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,96,58)"
                        }
                    }
                },
                {
                    "name": "\u5047\u671f\u591a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,18,54)"
                        }
                    }
                },
                {
                    "name": "\u6311\u6218\u5927",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,19,91)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u9645\u5316",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,159,118)"
                        }
                    }
                },
                {
                    "name": "\u826f\u597d\u7684\u6280\u672f\u6c1b\u56f4",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,92,78)"
                        }
                    }
                },
                {
                    "name": "\u5468\u672b\u52a0\u73ed\u53cc\u500d\u5de5\u8d44",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,120,10)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u671f\u56e2\u5efa",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,160,25)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u665a\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,27,12)"
                        }
                    }
                },
                {
                    "name": "\u90e8\u95e8\u8bc4\u4f18\u5956",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,70,143)"
                        }
                    }
                },
                {
                    "name": "\u8d70\u5728\u7b97\u6cd5\u524d\u6cbf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,101,31)"
                        }
                    }
                },
                {
                    "name": "\u5305\u9910\u53cc\u4f11\u4e0d\u6253\u5361",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,146,142)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1/\u9910\u8865/\u7ee9\u6548\u5956\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,27,90)"
                        }
                    }
                },
                {
                    "name": "13\u85aa+\u5e74\u7ec8\u5956+\u5458\u5de5\u6301\u80a1\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,106,103)"
                        }
                    }
                },
                {
                    "name": "\u7d27\u6025",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,79,142)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5e74\u8f7b\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,157,34)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,53,43)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u4ea4\u4e92",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,110,24)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u81ea\u7531",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,76,152)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u5e74\u5047\u75c5\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,104,32)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u85aa\u8d44\u4f18\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,51,97)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u56e2\u961f\u6765\u81ea\u6d59\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,51,2)"
                        }
                    }
                },
                {
                    "name": "\u8fd1\u4e07\u4eba\u89c4\u6a21",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,82,18)"
                        }
                    }
                },
                {
                    "name": "90\u540e\u5e74\u8f7b\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,74,111)"
                        }
                    }
                },
                {
                    "name": "AI\u56e2\u961f\u7b79\u5efa\u4e2d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,96,50)"
                        }
                    }
                },
                {
                    "name": "\u4e0e\u4e16\u754c\u9886\u5148\u7684AI\u7814\u53d1\u56e2\u961f\u5408\u4f5c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,100,100)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u8f6c\u6b63\u673a\u4f1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,9,142)"
                        }
                    }
                },
                {
                    "name": "\u516c\u68c0\u6cd5\u5927\u6570\u636e\u52a0\u4eba\u5de5\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,135,6)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u957f\u5047\u671f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,23,80)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u4f53\u68c0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,106,17)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u4e0d\u9519",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,18,76)"
                        }
                    }
                },
                {
                    "name": "\u6301\u7eed\u521b\u65b0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,137,67)"
                        }
                    }
                },
                {
                    "name": "\u8282\u65e5\u793c\u7269",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,148,128)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u7a7a\u95f4\u5e7f\u9614\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,75,112)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c\u798f\u5229\u4f18\u8d8a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,2,6)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u5e73\u53f0\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,42,14)"
                        }
                    }
                },
                {
                    "name": "\u8ddf\u725b\u4eba\u4e00\u8d77\u5de5\u4f5c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,26,10)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u673a\u4f1a\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,69,114)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u4e8b\u5047\u4e94\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,117,84)"
                        }
                    }
                },
                {
                    "name": "\u516c\u5e73\u664b\u5347",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,138,118)"
                        }
                    }
                },
                {
                    "name": "DevOps",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,71,84)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u524d\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,135,13)"
                        }
                    }
                },
                {
                    "name": "\u597d\u73a9\u7684\u6e38\u620f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,43,128)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u9ad8\u798f\u5229\u597d\u5927\u725b\u8eab\u8fb9\u7ed5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,152,142)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a**\u72ec\u89d2\u517d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,106,113)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u6838\u5fc3\u5927\u8111\u9879\u76ee\u80a1\u7968\u671f\u6743",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,131,121)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,79,9)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5f52\u79d1\u7814\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,11,140)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956+\u53cc\u4f11+\u516d\u9669\u4e00\u91d1+\u665a\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,49,151)"
                        }
                    }
                },
                {
                    "name": "\u521b\u4e1a\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,112,127)"
                        }
                    }
                },
                {
                    "name": "\u72ec\u7acb\u8d1f\u8d23",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,100,126)"
                        }
                    }
                },
                {
                    "name": "\u878d\u8d44\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,67,156)"
                        }
                    }
                },
                {
                    "name": "\u805a\u4e00\u7fa4\u6709\u60c5\u4e49\u7684\u4eba\u505a\u6210\u6709\u610f\u4e49\u7684\u4e8b\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,39,156)"
                        }
                    }
                },
                {
                    "name": "\u804c\u4f4d\u664b\u5347\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,64,131)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u5347\u4e2a\u4eba\u4ef7\u503c\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,136,112)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u65b0\u9896",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,103,12)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,89,148)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u989d\u9910\u8865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,36,81)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u591a\u6837\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,34,104)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5382\u4f18\u79c0\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,45,23)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c\u798f\u5229\u4f18\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,99,86)"
                        }
                    }
                },
                {
                    "name": "AI\u4ea7\u54c1\u7814\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,11,92)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u5e72\u9884\u662f\u7f8e\u56e2\u9a91\u884c\u4e1a\u52a1\u6838\u5fc3\u90e8\u5206",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,129,131)"
                        }
                    }
                },
                {
                    "name": "\u529e\u516c\u5ba4\u96f6\u98df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,28,146)"
                        }
                    }
                },
                {
                    "name": "\u961f\u53cb\u5948\u65af",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,68,125)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u540d\u7535\u5546",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,111,8)"
                        }
                    }
                },
                {
                    "name": "1~\u221e\u9ad8\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,106,91)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u8425\u9500",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,58,80)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u79c0\u7684\u6280\u672f\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,69,114)"
                        }
                    }
                },
                {
                    "name": "AI\u667a\u80fd\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,34,87)"
                        }
                    }
                },
                {
                    "name": "\u4f11\u95f2\u96f6\u98df\u4e0b\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,53,3)"
                        }
                    }
                },
                {
                    "name": "AI+\u6559\u80b2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,9,10)"
                        }
                    }
                },
                {
                    "name": "\u6709\u671f\u6743",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,116,118)"
                        }
                    }
                },
                {
                    "name": "\u5496\u5561\u5385",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,55,25)"
                        }
                    }
                },
                {
                    "name": "\u90e8\u95e8\u4f18\u80dc\u5956",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,34,22)"
                        }
                    }
                },
                {
                    "name": "\u5929\u9ad8\u4efb\u9e1f\u98de",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,15,151)"
                        }
                    }
                },
                {
                    "name": "\u9f13\u52b1\u81ea\u6211\u5b66\u4e60",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,30,30)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u4ece\u4f18",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,140,27)"
                        }
                    }
                },
                {
                    "name": "Mac\u529e\u516c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,110,98)"
                        }
                    }
                },
                {
                    "name": "\u73af\u5883\u4f73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,152,130)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u8d44\u6df1\u5e26\u961f\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,101,145)"
                        }
                    }
                },
                {
                    "name": "\u5927\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,31,63)"
                        }
                    }
                },
                {
                    "name": "\u5b8c\u5584\u664b\u5347\u673a\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,66,61)"
                        }
                    }
                },
                {
                    "name": "\u79fb\u52a8\u4e92\u8054\u7f51\u5e7f\u544a\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,139,135)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,116,127)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5eb7\u5a01\u89c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,156,104)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u672f\u548c\u5e94\u7528\u7ed3\u5408",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,38,96)"
                        }
                    }
                },
                {
                    "name": "\u52a0\u73ed\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,149,91)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1;\u8282\u65e5\u8865\u8d34;\u7ee9\u6548\u5956\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,89,86)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6e90\u5e73\u53f0\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,102,30)"
                        }
                    }
                },
                {
                    "name": "\u5e02\u573a\u524d\u666f\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,83,37)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u7a33\u5b9a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,40,50)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,80,34)"
                        }
                    }
                },
                {
                    "name": "\u7ee9\u6548\u8c03\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,6,65)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u989d\u9910\u8865/TB\u8d39\u7528",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,58,130)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u7b97\u6cd5\u4e13\u5bb6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,158,52)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u5feb\u901f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,15,62)"
                        }
                    }
                },
                {
                    "name": "AI\u524d\u666f\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,32,14)"
                        }
                    }
                },
                {
                    "name": "\u5f15\u9886\u884c\u4e1a\u8d70\u52bf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,139,133)"
                        }
                    }
                },
                {
                    "name": "AI\u98ce\u53e3\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,60,9)"
                        }
                    }
                },
                {
                    "name": "\u8865\u52a9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,56,138)"
                        }
                    }
                },
                {
                    "name": "\u6ca1\u6709KPI",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,41,46)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u5f85\u9047\u5f88\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,103,120)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u9650\u96f6\u98df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,80,54)"
                        }
                    }
                },
                {
                    "name": "open",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,127,104)"
                        }
                    }
                },
                {
                    "name": "\u671f\u6743\u80a1\u6743",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,51,98)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6167\u73af\u4fdd\u9886\u519b\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,84,119)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6316\u6398\u5de5\u7a0b\u5e08",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,33,72)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u98df\u4e0b\u5348\u8336outing\u4e0d\u505c\u6b47",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,78,101)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c\u6fc0\u52b1\u8ba1\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,45,80)"
                        }
                    }
                },
                {
                    "name": "\u548c\u6709\u8da3\u7684\u4eba\u505a\u6709\u8da3\u7684\u4e8b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,128,121)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u6709\u7ade\u4e89\u529b\u7684\u85aa\u8d44\u53d1\u5c55",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,85,153)"
                        }
                    }
                },
                {
                    "name": "\u6f5c\u529b\u5de8\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,137,134)"
                        }
                    }
                },
                {
                    "name": "\u9f13\u52b1\u8bd5\u9519",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,40,48)"
                        }
                    }
                },
                {
                    "name": "\u67b6\u6784\u6241\u5e73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,101,135)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5c0f\u5468",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,124,2)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u98df\u81ea\u7531",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,90,44)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u65b0\u6280\u672f\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,48,93)"
                        }
                    }
                },
                {
                    "name": "\u6d41\u91cf\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,153,97)"
                        }
                    }
                },
                {
                    "name": "\u521b\u65b0\u6c1b\u56f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,118,36)"
                        }
                    }
                },
                {
                    "name": "\u521b\u65b0\u5e94\u7528",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,103,144)"
                        }
                    }
                },
                {
                    "name": "\u529e\u516c\u73af\u5883\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,65,33)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1(\u6700\u9ad8\u6bd4\u4f8b)",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,21,83)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5ea6\u8c03\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,102,102)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5e9514\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,89,27)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u4e0a\u4e0b\u73ed\u53cc\u4f11",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,62,124)"
                        }
                    }
                },
                {
                    "name": "\u5404\u79cd\u56e2\u5efa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,69,103)"
                        }
                    }
                },
                {
                    "name": "2\u4f4d\u9662\u58eb\u9886\u8854",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,133,145)"
                        }
                    }
                },
                {
                    "name": "\u72ec\u89d2\u517d\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,35,142)"
                        }
                    }
                },
                {
                    "name": "\u6fc0\u52b1\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,70,150)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u540d\u836f\u4f01",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,69,7)"
                        }
                    }
                },
                {
                    "name": "E\u8f6e\u878d\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,74,4)"
                        }
                    }
                },
                {
                    "name": "\u592e\u4f01",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,145,16)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u5f85\u9047open",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,26,132)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u91cf\u8fc5\u731b\u53d1\u5c55",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,124,123)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u4e30\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,87,61)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u798f\u5229\u4f18",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,23,43)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u4e92\u8054\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,122,150)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6311\u6218\u548c\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,95,101)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u7814\u53d1\u5b9e\u529b\u96c4\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,61,134)"
                        }
                    }
                },
                {
                    "name": "\u4ebf\u7ea7\u6d41\u91cf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,31,50)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u7ebf\u98ce\u6295\u52a0\u6301",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,56,147)"
                        }
                    }
                },
                {
                    "name": "\u4e2a\u4eba\u6210\u957f\u6027",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,134,116)"
                        }
                    }
                },
                {
                    "name": "\u725b\u4eba\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,118,108)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5f52\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,24,84)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u4ea7\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,1,125)"
                        }
                    }
                },
                {
                    "name": "\u9886\u5bfcNic",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,2,34)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u5b50\u5973\u8865\u5145\u533b\u7597",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,127,34)"
                        }
                    }
                },
                {
                    "name": "\u7eff\u8c37\u5236\u836f\u5b50\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,73,120)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u65b9\u5f0f\u7075\u6d3b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,39,128)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,29,51)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5e95\u53cc\u85aa-\u5e74\u7ec8\u5956-\u6241\u5e73\u5316\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,17,15)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u9645\u5316\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,134,142)"
                        }
                    }
                },
                {
                    "name": "\u6253\u9020\u4e00\u6d41\u7684\u7814\u53d1\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,114,127)"
                        }
                    }
                },
                {
                    "name": "\u7a33\u5b9a\u6027\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,60,94)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f\u671f\u521b\u4e1a\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,137,36)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u73af\u5883\u4f18\u7f8e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,39,9)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u6587\u5316\u56e2\u961fnice",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,101,157)"
                        }
                    }
                },
                {
                    "name": "BAT\u6280\u672fleader",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,135,55)"
                        }
                    }
                },
                {
                    "name": "\u4f4f\u623f\u514d\u606f\u8d37",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,152,126)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,73,136)"
                        }
                    }
                },
                {
                    "name": "\u9910\u8865\u901a\u8baf\u8865\u7535\u8111\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,136,138)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u4e0d\u9519",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,101,136)"
                        }
                    }
                },
                {
                    "name": "\u610f\u5916\u8865\u52a9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,46,2)"
                        }
                    }
                },
                {
                    "name": "\u3010\u4eac\u4e1c\u7269\u6d41\u3011\u730e\u5934\u5c97\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,87,101)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u798f\u5229/\u56e2\u961f\u6c1b\u56f4/\u5b9a\u671f\u57f9\u8bad/\u664b\u5347\u901a\u9053",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,149,28)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u5bfc\u5e08\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,10,74)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u524d\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,141,20)"
                        }
                    }
                },
                {
                    "name": "\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,140,123)"
                        }
                    }
                },
                {
                    "name": "NLP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,10,90)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u9886\u8dd1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,154,147)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u53d1\u5c55\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,100,94)"
                        }
                    }
                },
                {
                    "name": "5\u59297\u5c0f\u65f6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,136,98)"
                        }
                    }
                },
                {
                    "name": "\u5468\u672b\u53cc\u4f118\u5c0f\u65f6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,26,142)"
                        }
                    }
                },
                {
                    "name": "\u6b22\u8fce\u52a0\u5165",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,154,83)"
                        }
                    }
                },
                {
                    "name": "\u57f9\u8bad",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,55,120)"
                        }
                    }
                },
                {
                    "name": "AI\u4ea7\u54c1\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,123,76)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u6cdb\u6210\u957f\u7a7a\u95f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,157,109)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u524d\u77bb\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,77,71)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u6210\u7acb\u4eba\u5de5\u667a\u80fd\u4e0e\u5927\u6570\u636e\u90e8\u95e8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,99,32)"
                        }
                    }
                },
                {
                    "name": "\u643a\u624b\u594b\u6597\u672a\u6765\u53ef\u671f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,15,127)"
                        }
                    }
                },
                {
                    "name": "\u524d\u9014\u9886\u57df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,15,75)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u4f18\u6e25",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,124,15)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u5f85\u9047\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,81,114)"
                        }
                    }
                },
                {
                    "name": "python\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,111,125)"
                        }
                    }
                },
                {
                    "name": "3\u4f4d\u535a\u58eb\u751f\u5bfc\u5e08\u6302\u5e05\u7684\u79d1\u5b66\u5bb6\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,24,2)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e+AI\u672a\u676510\u5e74\u8d8b\u52bf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,13,20)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u8fc5\u901f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,69,93)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u540d\u5934\u90e8\u4e92\u8054\u7f51\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,30,11)"
                        }
                    }
                },
                {
                    "name": "***\u5b9e\u9a8c\u5ba4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,153,76)"
                        }
                    }
                },
                {
                    "name": "IBM",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,51,26)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,18,31)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,136,19)"
                        }
                    }
                },
                {
                    "name": "\u6bcf\u6708\u623f\u88652000",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,140,112)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4nice",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,86,108)"
                        }
                    }
                },
                {
                    "name": "\u6e38\u620fUGC",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,1,72)"
                        }
                    }
                },
                {
                    "name": "\u6709\u5348\u4f11",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,44,146)"
                        }
                    }
                },
                {
                    "name": "\u6bcf\u5e742\u6b21\u8c03\u85aa\u7a97\u53e3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,151,75)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5185\u5bb9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,47,74)"
                        }
                    }
                },
                {
                    "name": "\u9f13\u52b1\u7814\u7a76\u65b0\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,46,157)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u673a\u4f1a\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,65,89)"
                        }
                    }
                },
                {
                    "name": "\u6709\u6311\u6218",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,95,27)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u516d\u9669\u4e00\u91d1\u996d\u8d34\u8f66\u8d34\u7ee9\u6548\u5956\u5b9a\u671f\u4f53\u68c0\u805a\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,120,32)"
                        }
                    }
                },
                {
                    "name": "\u9053\u8def\u68c0\u6d4b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,129,128)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u4ece0-1\u7684\u8fc7\u7a0b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,18,8)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6167\u4ea4\u901a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,75,117)"
                        }
                    }
                },
                {
                    "name": "\u8682\u8681\u63a7\u80a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,119,80)"
                        }
                    }
                },
                {
                    "name": "\u6709\u66f4\u9ad8\u66f4\u5927\u7684\u53d1\u5c55\u524d\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,72,93)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5bfc\u5411",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,95,114)"
                        }
                    }
                },
                {
                    "name": "\u7ba1\u4e24\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,117,82)"
                        }
                    }
                },
                {
                    "name": "\u5916\u5305",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,78,28)"
                        }
                    }
                },
                {
                    "name": "\u963f\u91cc\u7cfb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,146,136)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u4e0d\u9519",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,157,21)"
                        }
                    }
                },
                {
                    "name": "\u6c7d\u8f66\u884c\u4e1a\u4e07\u4ebf\u8d5b\u9053\u98ce\u63a7\u662f\u884c\u4e1a\u75db\u70b9\u53d1\u5c55\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,146,4)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7814\u4ea7\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,61,150)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u57fa\u5efa\u9886\u57df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,127,96)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u53d1\u5c55\u5feb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,116,70)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u957f\u5e26\u85aa\u5e74\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,67,149)"
                        }
                    }
                },
                {
                    "name": "12\u5929\u5e26\u85aa\u5e74\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,104,52)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u7ed9\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,142,146)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u8282\u594f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,91,131)"
                        }
                    }
                },
                {
                    "name": "\u73af\u5883open",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,133,146)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u805a\u7126",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,6,8)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u671f\u805a\u9910~",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,135,125)"
                        }
                    }
                },
                {
                    "name": "\u8fbe\u5230\u4e00\u5b9a\u804c\u7ea7\u53ef\u83b7\u5f97\u516c\u53f8\u80a1\u6743",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,89,154)"
                        }
                    }
                },
                {
                    "name": "\u524d\u6cbf\u7684\u5e73\u53f0\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,21,65)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u5316\u7ba1\u7406\u5de5\u4f5c\u6c1b\u56f4\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,113,99)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u8bf1\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,83,21)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u8865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,91,3)"
                        }
                    }
                },
                {
                    "name": "\u9886\u5bfc\u8d85\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,26,72)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u5750\u9547",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,138,26)"
                        }
                    }
                },
                {
                    "name": "\u767e\u4eba\u6280\u672f\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,129,100)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u524d\u666f\u8d5e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,145,129)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5927\u725b\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,51,15)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u624d\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,144,12)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u9650\u6210\u957f\uff01",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,137,7)"
                        }
                    }
                },
                {
                    "name": "\u91cd\u70b9\u4e1a\u52a1\u5feb\u901f\u53d1\u5c55",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,70,147)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u9510\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,74,118)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u4e00\u7ebf\u4e92\u8054\u7f51\u516c\u53f8\u85aa\u6c34\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,70,27)"
                        }
                    }
                },
                {
                    "name": "\u9910\u996e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,44,59)"
                        }
                    }
                },
                {
                    "name": "16-18\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,153,30)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u4f73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,53,29)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6280\u672f\u6c1b\u56f4\u6d53\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,55,54)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u73af\u5883\u8f7b\u677e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,61,75)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u7a33\u5b9a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,117,4)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u4e30\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,35,15)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u73ed\u5f00\u5fc3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,138,48)"
                        }
                    }
                },
                {
                    "name": "\u76c8\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,53,79)"
                        }
                    }
                },
                {
                    "name": "**\u751f\u7269\u533b\u5b66\u4fe1\u606f\u4e13\u5bb6\u5e26\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,19,125)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u591a\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,16,104)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u5e7f\u9614",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,112,136)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u4e00\u6d41",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,153,51)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,61,20)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u4e1a\u57f9\u8bad",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,66,160)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,97,132)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5f52\u79d1\u7814\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,4,62)"
                        }
                    }
                },
                {
                    "name": "\u5b5d\u5fc3\u57fa\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,4,50)"
                        }
                    }
                },
                {
                    "name": "\u3010OPPO\u3011\u730e\u5934\u804c\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,75,153)"
                        }
                    }
                },
                {
                    "name": "\u7d2b\u5149\u96c6\u56e2\u65d7\u4e0b\u6559\u80b2\u4fe1\u606f\u5316\u5934\u90e8\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,139,47)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u7a7a\u95f4\u5e7f\u9614",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,42,148)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5382\u80cc\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,130,140)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u4f18\u79c0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,80,64)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,85,94)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u98de\u901f\u53d1\u5c55",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,32,95)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5b9e\u4e60\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,134,74)"
                        }
                    }
                },
                {
                    "name": "\u7b80\u5355\u6587\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,146,11)"
                        }
                    }
                },
                {
                    "name": "\u6709XLNet\u4e00\u4f5c\u5927\u795e\u5e26\u60a8\u5728\u7b97\u6cd5\u91cc\u6df1\u8015",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,114,106)"
                        }
                    }
                },
                {
                    "name": "\u5177\u6709\u5e02\u573a\u7ade\u4e89\u529b\u7684\u85aa\u916c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,157,58)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u9a7e\u9a76",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,75,36)"
                        }
                    }
                },
                {
                    "name": "\u4f4f\u623f\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,160,114)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u80fd\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,1,31)"
                        }
                    }
                },
                {
                    "name": "\u5168\u6808\u6280\u672f\u5927\u725b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,160,7)"
                        }
                    }
                },
                {
                    "name": "\u660e\u661f\u8d44\u672c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,34,55)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5e02\u516c\u53f8/\u524d\u666f\u597d/\u5927\u725b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,106,138)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4\u8d85\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,152,45)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u98df\u5802\u73ed\u8f66\u5065\u8eab\u623f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,87,149)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u4eba\u914d\u9001",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,41,90)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u540d\u4e92\u8054\u7f51\u7535\u5546\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,58,150)"
                        }
                    }
                },
                {
                    "name": "\u4e03\u9669\u4e8c\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,56,24)"
                        }
                    }
                },
                {
                    "name": "\u5173\u6ce8\u5458\u5de5\u53d1\u5c55",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,25,112)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u901f\u5ea6\u5feb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,128,19)"
                        }
                    }
                },
                {
                    "name": "AI\u573a\u666f\u4e30\u5bcc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,146,152)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u52a8\u578b\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,106,19)"
                        }
                    }
                },
                {
                    "name": "\u805a\u9910\u56e2\u5efa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,71,143)"
                        }
                    }
                },
                {
                    "name": "D\u8f6e\u6f5c\u529b\u80a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,43,122)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u5bbf\u820d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,67,150)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5916\u4ea7\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,120,134)"
                        }
                    }
                },
                {
                    "name": "\u535a\u58eb\u843d\u6237",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,86,79)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u673a\u89c6\u89c9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,143,106)"
                        }
                    }
                },
                {
                    "name": "\u533a\u5757\u94fe\u77ff\u4e1a\u9879\u76ee\u6709\u524d\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,150,15)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5927\u725b\u4f17\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,64,70)"
                        }
                    }
                },
                {
                    "name": "\u5065\u8eab\u623f\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,78,74)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1\u4e0d\u5b9a\u671f\u56e2\u5efa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,77,134)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u5bcc\u7684\u516c\u53f8\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,102,53)"
                        }
                    }
                },
                {
                    "name": "\u540c\u4e8b\u597d\u76f8\u5904",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,133,133)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u72ec\u89d2\u517d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,122,94)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u901a\u9053",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,59,25)"
                        }
                    }
                },
                {
                    "name": "\u771f\u5b9e\u7684\u9879\u76ee\u6311\u6218\u4e0e\u5386\u7ec3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,26,61)"
                        }
                    }
                },
                {
                    "name": "\u8282\u65e5\u793c\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,114,76)"
                        }
                    }
                },
                {
                    "name": "\u6b63\u96c5\u9f7f\u79d1-\u730e\u5934\u804c\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,73,75)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u901f\u664b\u5347\u7684\u804c\u573a\u673a\u4f1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,111,41)"
                        }
                    }
                },
                {
                    "name": "\u516d\u9669\u4e00\u91d1+\u5e26\u85aa\u5e74\u5047+\u5e74\u7ec8\u5956\u91d1+\u8282\u65e5\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,140,57)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u673a\u4f1a\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,34,86)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1\u4e00\u6863",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,8,114)"
                        }
                    }
                },
                {
                    "name": "\u673a\u4f1a\u591a\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,160,157)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u7a33\u5b9a/\u85aa\u916c\u4f18\u6e25",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,32,107)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u5373\u5c06\u4e0a\u5e02",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,49,158)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u4e30\u5bcc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,140,35)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u80cc\u666f\u5f3a\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,131,152)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u9614\u51ed\u9c7c\u8dc3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,100,128)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u53d1\u5c55\u7a7a\u95f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,120,66)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51\u6c1b\u56f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,117,140)"
                        }
                    }
                },
                {
                    "name": "\u5bfc\u5e08nice",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,110,8)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u5bcc\u4e0b\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,141,153)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u80a1\u4e0a\u5e02",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,23,49)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u7814\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,36,48)"
                        }
                    }
                },
                {
                    "name": "\u826f\u597d\u7684\u53d1\u5c55\u524d\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,103,17)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,61,23)"
                        }
                    }
                },
                {
                    "name": "\u672a\u6765\u53d1\u5c55\u6f5c\u529b\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,130,44)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u5f88\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,91,133)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44OPEN",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,5,64)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u6df1\u8015\u571f\u58e4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,82,62)"
                        }
                    }
                },
                {
                    "name": "\u3010\u6b63\u96c5\u9f7f\u79d1\u3011\u730e\u5934\u5c97\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,103,89)"
                        }
                    }
                },
                {
                    "name": "2012\u5b9e\u9a8c\u5ba4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,113,141)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,96,65)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u534f\u4f5c\u529b\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,145,15)"
                        }
                    }
                },
                {
                    "name": "Top\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,159,20)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5e95\u591a\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,5,75)"
                        }
                    }
                },
                {
                    "name": "\u521b\u65b0\u9879\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,121,32)"
                        }
                    }
                },
                {
                    "name": "\u51fa\u5dee\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,139,107)"
                        }
                    }
                },
                {
                    "name": "\u8d1f\u8d23\u641c\u72d7\u6570\u5b57\u4eba\u76843D\u4eba\u8138\u7b97\u6cd5\u65b9\u9762\u7684\u7814\u7a76",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,13,92)"
                        }
                    }
                },
                {
                    "name": "\u767e\u4ebf\u72ec\u89d2\u517d\u4e92\u8054\u7f51\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,91,7)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5b9e\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,71,81)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u5e73\u53f0\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,52,72)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u5185\u4ea7\u54c1\u5f71\u54cd\u529b\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,31,75)"
                        }
                    }
                },
                {
                    "name": "\u4ebf\u7ea7\u7528\u6237",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,48,43)"
                        }
                    }
                },
                {
                    "name": "nice\u9886\u5bfc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,9,146)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,152,40)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u56e2\u961f\u4f18\u79c0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,4,25)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e24\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,75,112)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5408\u4f5c\u878d\u6d3d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,96,145)"
                        }
                    }
                },
                {
                    "name": "\u661f\u5df4\u514b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,105,1)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u665a\u9910\u4e0b\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,39,70)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u5185\u542b\u5065\u8eab\u623f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,84,99)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4\u878d\u6d3d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,113,156)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u7ee9\u6548\u5956\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,106,81)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u989d\u5e74\u7ec8\u5956",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,2,127)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u8d28\u7684\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,119,1)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u672f\u548c\u5de5\u4f5c\u80cc\u666f\u725b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,129,21)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u5e02\u573a\u6f5c\u529b\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,87,138)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5916\u76f4\u64ad\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,139,117)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u63d0\u6210",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,133,33)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u7684\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,48,10)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u53d1\u5c55\u8fc5\u901f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,70,94)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5148\u8fdb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,16,58)"
                        }
                    }
                },
                {
                    "name": "\u8001\u677f\u683c\u5c40\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,37,12)"
                        }
                    }
                },
                {
                    "name": "\u8865\u5145\u533b\u7597\u7b49",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,57,120)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,131,152)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u524d\u666f\u53ef\u89c2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,53,146)"
                        }
                    }
                },
                {
                    "name": "\u521b\u4e1a\u4eba\u56e2\u961f\u80cc\u666f\u725b\u903c\u548c\u8d44\u672c\u5145\u8db3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,131,51)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u4e1a\u4e13\u5fc3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,59,100)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u5bcc\u9879\u76ee\u7ecf\u9a8c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,21,8)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u8865\u52a9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,37,125)"
                        }
                    }
                },
                {
                    "name": "\u767e\u4ebf\u72ec\u89d2\u517d\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,117,128)"
                        }
                    }
                },
                {
                    "name": "\u4fdd\u5e9513\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,10,19)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u8c08\u671f\u6743",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,13,123)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u5f02\u8005\u53ef\u8f6c\u6821\u62db\u6b63\u5f0f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,66,99)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u9a71\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,85,73)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c\u798f\u5229\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,141,9)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u9614\u7a7a\u95f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,63,119)"
                        }
                    }
                },
                {
                    "name": "\u5173\u952e\u5c97\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,55,72)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u5929\u516b\u5c0f\u65f6\u5de5\u4f5c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,48,157)"
                        }
                    }
                },
                {
                    "name": "\u4e0d\u5b9a\u671f\u56e2\u5efa\u6d3b\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,2,36)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u524d\u6cbf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,123,106)"
                        }
                    }
                },
                {
                    "name": "\u65e0007",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,110,114)"
                        }
                    }
                },
                {
                    "name": "\u8fdb\u4fee\u673a\u4f1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,46,137)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u6c11\u7ea7\u5e94\u7528",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,93,139)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4\u68d2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,11,112)"
                        }
                    }
                },
                {
                    "name": "A\u8f6e\u878d\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,144,112)"
                        }
                    }
                },
                {
                    "name": "\u5927\u4f6c\u4e91\u96c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,112,77)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u671f\u65c5\u6e38",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,129,85)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u56e2\u961f\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,132,88)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u4e09\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,8,88)"
                        }
                    }
                },
                {
                    "name": "\u7b80\u5355\u5feb\u901f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,86,54)"
                        }
                    }
                },
                {
                    "name": "\u767e\u4ebf\u7f8e\u91d1\u4f30\u503c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,159,155)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u5929\u516b\u5c0f\u65f6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,99,145)"
                        }
                    }
                },
                {
                    "name": "\u6548\u76ca\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,151,159)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u96f6\u552e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,28,69)"
                        }
                    }
                },
                {
                    "name": "\u5171\u540c\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,66,99)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7d20\u8d28\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,160,145)"
                        }
                    }
                },
                {
                    "name": "\u5927\u7528\u6237\u91cf\u7ea7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,137,137)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5b9e\u529b\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,134,40)"
                        }
                    }
                },
                {
                    "name": "\u6cd5\u5b9a\u8282\u5047\u65e5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,60,118)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u5236\u9020",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,40,122)"
                        }
                    }
                },
                {
                    "name": "\u5165\u804c\u7f34\u7eb3\u4e94\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,9,151)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u98df\u6c34\u679c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,98,104)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u7d20\u8d28\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,157,82)"
                        }
                    }
                },
                {
                    "name": "\u821e\u53f0\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,54,74)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u914d\u7f6e\u671f\u6743",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,72,96)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5916\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,60,158)"
                        }
                    }
                },
                {
                    "name": "\u5168\u52e4\u5956",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,148,104)"
                        }
                    }
                },
                {
                    "name": "\u9910\u8865\u623f\u8865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,85,71)"
                        }
                    }
                },
                {
                    "name": "\u878d\u8d4411\u4ebf\u7f8e\u5143",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,111,154)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u7b80\u5355",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,70,113)"
                        }
                    }
                },
                {
                    "name": "\u822a\u7a7aIT\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,150,45)"
                        }
                    }
                },
                {
                    "name": "\u5168\u7403\u5316\u89c6\u91ce",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,23,14)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u5b66\u5bb6\u5927\u725b\u5e26\u961f\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,63,17)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u9645\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,57,74)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u9910\u514d\u8d39",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,142,54)"
                        }
                    }
                },
                {
                    "name": "\u6709\u5e02\u573a\u7ade\u4e89\u529b\u7684\u85aa\u916c\u5f85\u9047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,52,84)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u4f18\u6e25",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,2,67)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u901f\u53d1\u5c55\u4e2d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,22,153)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u578b\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,152,8)"
                        }
                    }
                },
                {
                    "name": "\u5f3a\u6709\u529b\u7684\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,104,154)"
                        }
                    }
                },
                {
                    "name": "10\u5929\u6625\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,15,128)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u5b8c\u5584",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,80,126)"
                        }
                    }
                },
                {
                    "name": "\u6709\u7ade\u4e89\u529b\u7684\u85aa\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,49,137)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u9886\u5148",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,115,149)"
                        }
                    }
                },
                {
                    "name": "\u6708\u5ea6\u6d3b\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,121,27)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c\u798f\u5229\u826f\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,32,140)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u6316\u6398",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,94,107)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u521b\u65b0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,117,142)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u91cf\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,80,141)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u53ef\u89c2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,158,8)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u4f01\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,118,73)"
                        }
                    }
                },
                {
                    "name": "\u52a0\u73ed\u5c11",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,115,4)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5206\u4eab",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,148,86)"
                        }
                    }
                },
                {
                    "name": "14-16\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,8,92)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1atop\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,31,86)"
                        }
                    }
                },
                {
                    "name": "\u516b\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,83,3)"
                        }
                    }
                },
                {
                    "name": "\u529f\u8bfe\u524d\u6cbf\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,93,21)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u80a1\u4e0a\u5e02\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,37,81)"
                        }
                    }
                },
                {
                    "name": "\u80a1\u6743\u8ba1\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,106,69)"
                        }
                    }
                },
                {
                    "name": "\u9633\u5149\u900f\u660e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,47,112)"
                        }
                    }
                },
                {
                    "name": "\u840c\u5ba0\u5f85\u64b8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,66,29)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u65b0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,137,145)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u53d1\u5c55\u5feb\u901f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,126,100)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u9910\u4e0b\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,130,6)"
                        }
                    }
                },
                {
                    "name": "\u5343\u4e07\u7ea7\u7528\u6237",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,105,128)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u7684\u8d77\u70b9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,63,36)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5382\u80cc\u666f\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,153,65)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u6807\u6746",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,81,20)"
                        }
                    }
                },
                {
                    "name": "\u91cd\u65b0\u5b9a\u4e49\u884c\u4e1a\u89c4\u5219",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,138,68)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u901a\u8baf\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,140,30)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6167\u533b\u7597",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,16,36)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u5f85\u9047\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,88,90)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,153,80)"
                        }
                    }
                },
                {
                    "name": "\u8f66\u8054\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,58,126)"
                        }
                    }
                },
                {
                    "name": "6\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,82,138)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u79c0\u7684\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,159,158)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51\u533b\u7597\u9886\u5934\u7f8a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,56,82)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,48,91)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,18,156)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u4e60\u5b9e\u8df5\u673a\u4f1a\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,127,98)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u63a8\u8350",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,121,109)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u5927\u4e0a\u73af\u5883",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,80,146)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u90e8\u95e8\u6838\u5fc3\u5c97\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,30,153)"
                        }
                    }
                },
                {
                    "name": "\u5c31\u6765\u641c\u72d7\u5546\u4e1a\u641c\u7d22\u5427\uff01",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,95,44)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79\u5b66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,10,23)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u4f53\u68c0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,15,43)"
                        }
                    }
                },
                {
                    "name": "\u7a33\u5b9a\u53d1\u5c55",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,105,67)"
                        }
                    }
                },
                {
                    "name": "\u5f3a\u5927\u7684\u6280\u672f\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,30,86)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u9f84\u5956",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,52,106)"
                        }
                    }
                },
                {
                    "name": "top5\u624b\u673a\u5382\u5546",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,84,91)"
                        }
                    }
                },
                {
                    "name": "\u4e2a\u4eba\u6210\u957f\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,24,66)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u7a7a\u95f4\u53ca\u85aa\u916c\u9ad8\u4e8e\u540c\u884c\u4e1a\u6c34\u5e73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,135,42)"
                        }
                    }
                },
                {
                    "name": "2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,106,105)"
                        }
                    }
                },
                {
                    "name": "\u5546\u4e1a\u4fdd\u9669\u7b49\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,36,71)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u5bf9\u4e00\u5e26\u6559",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,76,16)"
                        }
                    }
                },
                {
                    "name": "\u80fd\u529b\u7a81\u51fa\u8005\u664b\u5347\u5feb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,138,12)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,71,52)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5348\u9910\u665a\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,142,28)"
                        }
                    }
                },
                {
                    "name": "\u6d53\u539a\u7684\u6280\u672f\u5b66\u4e60\u6c1b\u56f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,105,94)"
                        }
                    }
                },
                {
                    "name": "ai\u533b\u7597\u72ec\u89d2\u517d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,133,105)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u9886\u57df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,67,7)"
                        }
                    }
                },
                {
                    "name": "\u521b\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,100,23)"
                        }
                    }
                },
                {
                    "name": "\u505a\u6700\u524d\u6cbf\u7684\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,28,136)"
                        }
                    }
                },
                {
                    "name": "Geek\u6587\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,114,4)"
                        }
                    }
                },
                {
                    "name": "\u963f\u91cc\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,129,59)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u65b0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,116,85)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u8f7b\u6241\u5e73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,17,72)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u6311\u6218",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,79,55)"
                        }
                    }
                },
                {
                    "name": "\u7532\u65b9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,67,27)"
                        }
                    }
                },
                {
                    "name": "\u573a\u666f\u4e30\u5bcc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,9,59)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u7814\u53d1\u5b9e\u529b\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,47,46)"
                        }
                    }
                },
                {
                    "name": "\u5916\u4f01\u98ce\u683c\u7b49",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,58,26)"
                        }
                    }
                },
                {
                    "name": "\u5f3a\u5927\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,87,152)"
                        }
                    }
                },
                {
                    "name": "***\u9879\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,101,119)"
                        }
                    }
                },
                {
                    "name": "\u6ee1\u52e4\u5956",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,14,150)"
                        }
                    }
                },
                {
                    "name": "\u6709\u673a\u4f1a\u517c\u4efb\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,39,150)"
                        }
                    }
                },
                {
                    "name": "\u62e5\u6709TB\u7ea7\u6570\u636e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,60,144)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u901f\u589e\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,102,67)"
                        }
                    }
                },
                {
                    "name": "\u4f01\u4e1a\u5feb\u901f\u6210\u957f\u671f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,81,100)"
                        }
                    }
                },
                {
                    "name": "\u5185\u90e8\u664b\u5347\u6e20\u9053\u5e7f\u9614",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,50,146)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4\u826f\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,121,10)"
                        }
                    }
                },
                {
                    "name": "\u7a33\u5b9a\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,160,71)"
                        }
                    }
                },
                {
                    "name": "10\u5929\u5e26\u85aa\u75c5\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,30,95)"
                        }
                    }
                },
                {
                    "name": "\u7269\u6d41",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,143,16)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u7814\u9662\u6821\u9f0e\u529b\u652f\u6301",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,63,62)"
                        }
                    }
                },
                {
                    "name": "\u521b\u9020\u524d\u6cbfAI\u4ea7\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,5,41)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u5229\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,159,61)"
                        }
                    }
                },
                {
                    "name": "\u73b0\u573a\u9762\u8bd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,39,55)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u53d1\u5c55\u524d\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,130,145)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u9614\u7684\u53d1\u5c55\u524d\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,12,51)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u91d1\u7b49",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,99,108)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u9886",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,63,123)"
                        }
                    }
                },
                {
                    "name": "\u540d\u6821\u5927\u5382",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,71,39)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u89c4\u6a21\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,126,80)"
                        }
                    }
                },
                {
                    "name": "\u300a\u77f3\u5934\u79d1\u6280\u300b\u730e\u5934\u804c\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,53,51)"
                        }
                    }
                },
                {
                    "name": "AI\u533b\u7597\u9886\u57df\u72ec\u89d2\u517d\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,74,153)"
                        }
                    }
                },
                {
                    "name": "AI\u72ec\u89d2\u517d\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,106,39)"
                        }
                    }
                },
                {
                    "name": "\u897f\u5de5\u5927\u7b49\u9ad8\u5c42\u6b21\u79d1\u7814\u5355\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,144,51)"
                        }
                    }
                },
                {
                    "name": "\u6559\u80b2\u57f9\u8bad",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,124,156)"
                        }
                    }
                },
                {
                    "name": "\u505a\u4e8b\u81ea\u7531\u5ea6\u8db3\u591f\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,125,125)"
                        }
                    }
                },
                {
                    "name": "\u65e5\u6570\u636e\u767e\u4ebf\u7ea7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,36,130)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c\u6709\u7ade\u4e89\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,56,154)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4\u597d\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,92,117)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,12,135)"
                        }
                    }
                },
                {
                    "name": "\u5305\u4f4f\u5bbf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,91,112)"
                        }
                    }
                },
                {
                    "name": "\u5145\u5206\u653e\u6743/\u9ad8\u6311\u6218",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,55,122)"
                        }
                    }
                },
                {
                    "name": "\u5168\u5e7416-18\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,112,154)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1/\u5e74\u5e95\u53cc\u85aa/\u7ee9\u6548\u5956\u91d1/\u5b9a\u671f\u4f53\u68c0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,52,65)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u65e9\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,35,46)"
                        }
                    }
                },
                {
                    "name": "\u817e\u8baf\u9886\u6295",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,16,12)"
                        }
                    }
                },
                {
                    "name": "\u6bd4\u80a9BAT\u7684\u85aa\u916c\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,10,86)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u6c1b\u56f4\u548c\u8c10",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,133,13)"
                        }
                    }
                },
                {
                    "name": "\u98de\u901f\u53d1\u5c55",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,35,70)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,12,92)"
                        }
                    }
                },
                {
                    "name": "bat\u5927\u725b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,100,116)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5065\u8eab/\u96f6\u98df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,105,109)"
                        }
                    }
                },
                {
                    "name": "\u5168\u5458mac",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,130,95)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u798f\u5229\u4f18\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,87,104)"
                        }
                    }
                },
                {
                    "name": "\u786c\u8f6f\u4ef6\u7ed3\u5408",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,125,76)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u6838\u5fc3\u56e2\u961f\u5feb\u901f\u6269\u5c55",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,48,136)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4\u798f\u5229\u5f85\u9047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,87,19)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u9760",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,147,124)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u53d1\u5c55\u524d\u666f\u5e7f\u9614",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,92,60)"
                        }
                    }
                },
                {
                    "name": "\u4e24\u4f4d\u9662\u58eb\u4e09\u4f4d\u535a\u58eb\u9886\u8854\u7684\u521d\u521b\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,7,68)"
                        }
                    }
                },
                {
                    "name": "\u53ea\u8981\u8db3\u591f\u4f18\u79c0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,123,116)"
                        }
                    }
                },
                {
                    "name": "\u8282\u65e5\u798f\u5229\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,95,76)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u5047\u671f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,64,32)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7531\u5f00\u653e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,110,155)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5458\u57f9\u517b\u673a\u5236\u5b8c\u5584",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,14,38)"
                        }
                    }
                },
                {
                    "name": "500\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,149,107)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u9886\u519b\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,25,73)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u53d1\u5c55\u5feb\u901f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,49,102)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u6280\u672f\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,108,74)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u9910\u996e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,12,146)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u53d1\u5c55\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,45,34)"
                        }
                    }
                },
                {
                    "name": "\u6d3b\u529b\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,76,10)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u5927\u6570\u636e\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,88,31)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u4e0d\u6253\u5361",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,29,99)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5496\u5e26\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,123,89)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u98df\u4e0b\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,157,54)"
                        }
                    }
                },
                {
                    "name": "\u5f00\u653e\u81ea\u7531",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,81,124)"
                        }
                    }
                },
                {
                    "name": "B\u8f6e\u878d\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,104,138)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u4e1a\u56fe\u8c31",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,115,149)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u5efa\u65c5\u6e38",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,1,27)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u4e1a\u52a1\u7684\u98ce\u63a7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,147,45)"
                        }
                    }
                },
                {
                    "name": "\u597d\u7684\u5f00\u53d1\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,130,67)"
                        }
                    }
                },
                {
                    "name": "\u5168\u5e02\u514d\u8d39\u73ed\u8f66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,87,76)"
                        }
                    }
                },
                {
                    "name": "\u96c6\u56e2\u80cc\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,29,144)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u65b0\u65b9\u5411",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,100,137)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4\u68d2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,150,139)"
                        }
                    }
                },
                {
                    "name": "\u7eaf\u6280\u672f\u80cc\u4e66\u7684\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,39,146)"
                        }
                    }
                },
                {
                    "name": "\u805a\u7126\u524d\u6cbf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,39,40)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4open",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,142,61)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u7a33\u5b9a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,36,144)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5e02\u51c6\u5907\u671f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,104,17)"
                        }
                    }
                },
                {
                    "name": "\u5f88\u6709\u524d\u666f\u7684\u90e8\u95e8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,121,63)"
                        }
                    }
                },
                {
                    "name": "\u524d\u6cbf\u9886\u57df\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,18,49)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4\u5411\u4e0a\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,135,74)"
                        }
                    }
                },
                {
                    "name": "\u529e\u516c\u73af\u5883\u4f73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,119,92)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,141,77)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4NICE",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,102,113)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u9ad8\u901f\u6210\u957f\u671f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,121,13)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u8fc7\u4ebf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,85,44)"
                        }
                    }
                },
                {
                    "name": "\u90e8\u95e8\u65c5\u6e38",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,40,122)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u5496\u5e26\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,126,156)"
                        }
                    }
                },
                {
                    "name": "3D\u89c6\u89c9+AI",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,70,42)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u901f\u6210\u957f/\u5e74\u7ec8\u5956\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,86,46)"
                        }
                    }
                },
                {
                    "name": "\u5065\u5eb7\u4f53\u68c0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,42,113)"
                        }
                    }
                },
                {
                    "name": "\u524d\u6cbf\u4ea7\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,129,2)"
                        }
                    }
                },
                {
                    "name": "\u5956\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,50,102)"
                        }
                    }
                },
                {
                    "name": "\u51fa\u56fd\u6e38",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,5,141)"
                        }
                    }
                },
                {
                    "name": "\u8c03\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,132,109)"
                        }
                    }
                },
                {
                    "name": "\u8865\u5145\u533b\u4fdd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,129,68)"
                        }
                    }
                },
                {
                    "name": "B2B\u91d1\u878d\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,141,136)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u4f73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,102,4)"
                        }
                    }
                },
                {
                    "name": "\u5f00\u653e\u578b\u6587\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,135,101)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5e74\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,93,50)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5916\u9879\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,5,26)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u98df\u65e0\u9650\u91cf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,10,144)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u85aa\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,94,5)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u53d1\u5c55\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,154,40)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u7efc\u5408\u7d20\u8d28\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,24,154)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u5e7414\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,160,95)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u5348\u9910\u665a\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,82,117)"
                        }
                    }
                },
                {
                    "name": "\u4e2a\u4eba\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,4,13)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,6,124)"
                        }
                    }
                },
                {
                    "name": "\u548c\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,60,140)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u5f85\u9047\u4f18\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,32,130)"
                        }
                    }
                },
                {
                    "name": "\u4e5d\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,147,135)"
                        }
                    }
                },
                {
                    "name": "\u9886\u5bfcNice",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,53,7)"
                        }
                    }
                },
                {
                    "name": "\u6253\u9020\u4e16\u754c**\u7684\u6df7\u6c8c\u5de5\u7a0b\u4e50\u56ed",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,5,136)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4\u6781\u4f73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,87,130)"
                        }
                    }
                },
                {
                    "name": "\u5168\u989d5\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,42,120)"
                        }
                    }
                },
                {
                    "name": "\u5496\u5561\u6c34\u679c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,126,1)"
                        }
                    }
                },
                {
                    "name": "\u6e05\u534e\u5927\u5b66\u7684\u667a\u80fd\u8fd0\u7ef4\u5b9e\u9a8c\u5ba4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,26,89)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51\u51fa\u6d77\u4f01\u4e1a\u6807\u6746",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,35,109)"
                        }
                    }
                },
                {
                    "name": "\u56fa\u5b9a\u6da8\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,151,104)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u56e2\u961f\u80fd\u529b\u4f18\u79c0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,140,118)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f\u673a\u4f1a\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,134,0)"
                        }
                    }
                },
                {
                    "name": "\u5b9e\u73b0\u521b\u65b0\u6280\u672f\u9a71\u52a8\u7269\u6d41\u884c\u4e1a\u5347\u7ea7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,75,116)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6df1\u5ea6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,56,22)"
                        }
                    }
                },
                {
                    "name": "2\u5e74\u7ecf\u9a8c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,33,106)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4fdd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,91,139)"
                        }
                    }
                },
                {
                    "name": "\u73af\u5883\u5bbd\u677e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,23,46)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u573a\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,23,111)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,128,127)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u8c03\u5ea6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,93,117)"
                        }
                    }
                },
                {
                    "name": "\u7814\u7a76\u548c\u5b9e\u9645\u5e94\u7528\u7ed3\u5408",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,65,151)"
                        }
                    }
                },
                {
                    "name": "\u521b\u65b0\u4e1a\u52a1\u573a\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,42,88)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c\u798f\u5229\u4f18",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,127,54)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u8d5b\u9053",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,64,108)"
                        }
                    }
                },
                {
                    "name": "\u7b80\u5355\u771f\u8bda",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,126,16)"
                        }
                    }
                },
                {
                    "name": "\u843d\u5730\u573a\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,132,103)"
                        }
                    }
                },
                {
                    "name": "\u4f4f\u623f\u6216\u4ea4\u901a\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,51,112)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u91d1\u96c4\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,6,108)"
                        }
                    }
                },
                {
                    "name": "\u6210\u5458\u5e74\u8f7b\u5316\u6709\u524d\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,136,26)"
                        }
                    }
                },
                {
                    "name": "995\u85aa\u8d44\u5f85\u9047\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,99,39)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u6c1b\u56f4\u597d\uff01",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,39,12)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4\u8f7b\u677e\uff01",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,75,94)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4Nice",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,29,95)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5347\u7a7a\u95f4\u5de8\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,150,60)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u673a\u4f1a\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,24,16)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u9645\u5316\u6c1b\u56f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,22,24)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,128,65)"
                        }
                    }
                },
                {
                    "name": "\u5b63\u5ea6\u5956\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,29,120)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u5496\u4e91\u96c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,66,23)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u5927\u725b\u4e91\u96c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,107,85)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u9650\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,1,57)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,144,87)"
                        }
                    }
                },
                {
                    "name": "\u5c97\u4f4d\u53d1\u5c55\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,127,127)"
                        }
                    }
                },
                {
                    "name": "500\u5f3a\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,137,158)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5065\u8eab\u623f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,114,105)"
                        }
                    }
                },
                {
                    "name": "\u8fd8\u53ef\u4ee5\u64b8\u732b\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,31,119)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u901f\u53d1\u5c55\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,111,65)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4\u81ea\u7531",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,92,48)"
                        }
                    }
                },
                {
                    "name": "\u4f01\u4e1a\u798f\u5229\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,56,126)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u7a7a\u95f4\u5de8\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,48,142)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u4e30\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,80,85)"
                        }
                    }
                },
                {
                    "name": "K12\u6559\u80b2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,41,25)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u4e13\u5bb6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,116,87)"
                        }
                    }
                },
                {
                    "name": "GPU\u4e0a\u76f4\u63a5\u505a\u5b9e\u9a8c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,25,70)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u5fc3\u7814\u7a76\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,139,18)"
                        }
                    }
                },
                {
                    "name": "\u6709\u671f\u6743\u6388\u4e88",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,48,54)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u5927\u725b\u5e26\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,64,118)"
                        }
                    }
                },
                {
                    "name": "16\u85aa\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,111,90)"
                        }
                    }
                },
                {
                    "name": "\u90e8\u95e8\u53d1\u5c55\u8fc5\u901f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,0,115)"
                        }
                    }
                },
                {
                    "name": "\u8865\u5145\u533b\u7597\u4fdd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,62,39)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6167\u57ce\u5e02",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,142,132)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u53d1\u5c55\u5f85\u9047\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,128,152)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u4e00\u65e5\u4e09\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,24,92)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u5bb6\u91cd\u70b9\u65b9\u5411",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,31,26)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5a92\u4f53",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,57,81)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6709\u6311\u6218",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,42,108)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u5927\u725b\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,17,73)"
                        }
                    }
                },
                {
                    "name": "\u52a0\u73ed\u53cc\u500d\u5de5\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,98,6)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f\u6311\u6218\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,30,53)"
                        }
                    }
                },
                {
                    "name": "F\u8f6e\u878d\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,32,124)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u4e1a\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,127,35)"
                        }
                    }
                },
                {
                    "name": "LayaAir\u5f15\u64ce\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,100,58)"
                        }
                    }
                },
                {
                    "name": "ai\u7b97\u6cd5\u5728\u4f9b\u5e94\u94fe\u548c\u7269\u6d41\u9886\u57df\u7684\u5e94\u7528",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,5,19)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u4e8b\u4e1a\u90e8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,16,66)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u6da8\u5e45\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,66,11)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u6e29\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,123,152)"
                        }
                    }
                },
                {
                    "name": "\u771f\u5b9e\u4e30\u5bcc\u7684\u5e94\u7528\u573a\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,65,38)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u7ebf\u6e38\u620f\u5927\u5382",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,146,102)"
                        }
                    }
                },
                {
                    "name": "\u5168\u989d\u793e\u4fdd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,55,159)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,116,92)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u9760\u8c31\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,134,139)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5b9e\u529b\u96c4\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,0,106)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u4f18\u52bf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,82,51)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u5316\u5f15\u64ce\u7684\u7cfb\u7edf\u67b6\u6784",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,88,64)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u56fe\u50cf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,132,139)"
                        }
                    }
                },
                {
                    "name": "\u6709\u8f83\u597d\u7684\u8d44\u6e90\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,22,90)"
                        }
                    }
                },
                {
                    "name": "undefined",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,67,75)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u901f\u7684\u53d1\u5c55\u524d\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,83,4)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f\u673a\u4f1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,145,57)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u5065\u8eab\u623f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,39,93)"
                        }
                    }
                },
                {
                    "name": "\u8de8\u5883\u5962\u4f88\u54c1\u7535\u5546",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,75,85)"
                        }
                    }
                },
                {
                    "name": "1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,41,149)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u5927\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,122,92)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u5229\u9879\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,46,23)"
                        }
                    }
                },
                {
                    "name": "\u575a\u6301\u81ea\u4e3b\u521b\u65b0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,35,29)"
                        }
                    }
                },
                {
                    "name": "\u957f\u671f\u7a33\u5b9a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,102,117)"
                        }
                    }
                },
                {
                    "name": "AI\u667a\u6167\u6559\u80b2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,90,36)"
                        }
                    }
                },
                {
                    "name": "\u516d\u9669\u4e00\u91d1+\u5b63\u5ea6\u7ee9\u6548\u5956\u91d1/\u5e74\u7ec8\u5956",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,65,55)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u6e38\u56e2\u5efa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,80,44)"
                        }
                    }
                },
                {
                    "name": "\u5bfc\u5e08\u4e00\u5e26\u4e00",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,135,127)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u699c****",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,6,88)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u8c03\u5ea6\u4f18\u5316\u5f15\u64ce\u7684\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,33,42)"
                        }
                    }
                },
                {
                    "name": "\u5730\u7406\u4f4d\u7f6e\u4fbf\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,42,129)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u5e7416\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,52,49)"
                        }
                    }
                },
                {
                    "name": "\u9f13\u52b1\u521b\u65b0\u7684\u5de5\u4f5c\u73af\u5883",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,5,151)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u98ce\u53e3\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,140,7)"
                        }
                    }
                },
                {
                    "name": "\u98df\u54c1\u996e\u6599",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,18,116)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u73ed\u8f66\u63a5\u9001",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,138,21)"
                        }
                    }
                },
                {
                    "name": "\u8f7b\u677e\u6d3b\u8dc3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,47,73)"
                        }
                    }
                },
                {
                    "name": "SaaS",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,41,23)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6df1\u5ea6ok",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,62,20)"
                        }
                    }
                },
                {
                    "name": "\u6709\u80a1\u7968\u671f\u6743\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,30,66)"
                        }
                    }
                },
                {
                    "name": "\u5c11\u52a0\u73ed",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,137,132)"
                        }
                    }
                },
                {
                    "name": "\uff08\u54c8\u5570\u51fa\u884c\uff09\u730e\u5934\u804c\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,56,84)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u754c\u5148\u8fdb\u7684\u5e7f\u544a\u6295\u653e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,110,87)"
                        }
                    }
                },
                {
                    "name": "007",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,151,119)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u798f\u5229\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,40,87)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u524d\u666f\u5e7f\u9614",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,28,111)"
                        }
                    }
                },
                {
                    "name": "\u6d59\u5927\u80cc\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,84,141)"
                        }
                    }
                },
                {
                    "name": "\u826f\u597d\u7684\u5de5\u4f5c\u73af\u5883",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,111,11)"
                        }
                    }
                },
                {
                    "name": "\u524d\u6cbf\u9879\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,118,108)"
                        }
                    }
                },
                {
                    "name": "\u7d2b\u5149\u96c6\u56e2\u65d7\u4e0b\u6559\u80b2\u4fe1\u606f\u5316\u884c\u4e1a\u5934\u90e8\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,157,60)"
                        }
                    }
                },
                {
                    "name": "\u5982\u679c\u4f60\u6b63\u5728\u8ffd\u68a6\u7684\u8def\u4e0a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,135,34)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u7814\u548c\u5e94\u7528\u7ed3\u5408",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,76,125)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ee9\u6548\u53ca\u5956\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,101,105)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u539a\u5e74\u7ec8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,69,30)"
                        }
                    }
                },
                {
                    "name": "\u6700\u80fd\u53d1\u6325\u521b\u9020\u529b\u7684\u7a7a\u95f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,42,139)"
                        }
                    }
                },
                {
                    "name": "\u963f\u91cc\u7cfb\u77e5\u540d\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,76,46)"
                        }
                    }
                },
                {
                    "name": "\u5bfc\u5e08\u4e00\u5bf9\u4e00\u5e26",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,22,139)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u7814\u80cc\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,82,140)"
                        }
                    }
                },
                {
                    "name": "\u521b\u4e1a\u578b\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,16,106)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u666f\u529e\u516c\u697c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,39,77)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u8f6f\u591a\u5e74\u670d\u52a1\u80cc\u666f\u6280\u672f\u5927\u62ff\u4eb2\u81ea\u5e26\u6559\u57f9\u8bad",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,8,47)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u6210\u957f\u6027",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,100,6)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u5de5\u7a0b\u5de5\u4e1a\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,67,21)"
                        }
                    }
                },
                {
                    "name": "\u5782\u76f4\u7535\u5546",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,80,80)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u516d\u9669\u4e00\u91d1\u996d\u8d34\u8f66\u8d34\u7ee9\u6548\u5956\u5b9a\u671f\u4f53\u68c0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,122,30)"
                        }
                    }
                },
                {
                    "name": "AI\u5f71\u50cf\u9886\u57df\u72ec\u89d2\u517d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,60,47)"
                        }
                    }
                },
                {
                    "name": "\u5f00\u53d1\u94bb\u7814\u524d\u6cbf\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,7,143)"
                        }
                    }
                },
                {
                    "name": "\u6709\u7b97\u6cd5\u5927\u725b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,14,151)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u4e60\u8d44\u6e90\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,156,59)"
                        }
                    }
                },
                {
                    "name": "\u6700\u5177\u60f3\u8c61\u529b\u7684\u8d5b\u9053",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,8,129)"
                        }
                    }
                },
                {
                    "name": "\u9910\u996e\u8865\u52a9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,93,76)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,109,149)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u90e8\u95e8\u6838\u5fc3\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,33,83)"
                        }
                    }
                },
                {
                    "name": "\u975e\u5e38\u4eba\u6027\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,104,39)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,146,24)"
                        }
                    }
                },
                {
                    "name": "\u535a\u58eb\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,11,125)"
                        }
                    }
                },
                {
                    "name": "TCL\u5927\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,71,79)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u672a\u6765\u91cd\u70b9\u53d1\u5c55\u6295\u5165",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,136,1)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4\u4f73\u7b49\u7b49",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,111,23)"
                        }
                    }
                },
                {
                    "name": "\u3010\u6b63\u96c5\u9f7f\u79d1\u3011\u730e\u5934\u804c\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,155,2)"
                        }
                    }
                },
                {
                    "name": "\u77ed\u89c6\u9891",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,49,106)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6269\u62db",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,95,32)"
                        }
                    }
                },
                {
                    "name": "\u521b\u65b0\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,65,74)"
                        }
                    }
                },
                {
                    "name": "\u516d\u9669\u4e00\u91d1\u5e26\u85aa\u4e8b\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,9,22)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u6325\u6240\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,68,147)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u81ea\u7531\u5ea6\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,135,20)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u540c\u4e8b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,56,9)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u4ea7\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,146,2)"
                        }
                    }
                },
                {
                    "name": "\u5168\u7ebf\u73ed\u8f66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,144,64)"
                        }
                    }
                },
                {
                    "name": "\u6e05\u534e\u7814\u7a76\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,71,15)"
                        }
                    }
                },
                {
                    "name": "\u8bd5\u7528\u671f\u4ea4\u4e94\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,148,128)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u89c6\u9891",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,123,151)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u53d1\u5c55\u5feb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,146,88)"
                        }
                    }
                },
                {
                    "name": "\u5782\u76f4\u9886\u57df****",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,137,129)"
                        }
                    }
                },
                {
                    "name": "\u7a33\u5065\u589e\u957f\u7684\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,45,58)"
                        }
                    }
                },
                {
                    "name": "\u725b\u4eba\u4e91\u96c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,66,146)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u4e1a\u7684\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,47,19)"
                        }
                    }
                },
                {
                    "name": "\u9886\u5bfc\u6c1b\u56f4\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,119,48)"
                        }
                    }
                },
                {
                    "name": "90\u540e\u9017\u6bd4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,148,116)"
                        }
                    }
                },
                {
                    "name": "\u80a1\u4e1c\u80cc\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,10,63)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u65e5\u56db\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,55,12)"
                        }
                    }
                },
                {
                    "name": "\u6709\u53d1\u5c55",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,116,54)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u5904\u4e8e\u5feb\u901f\u53d1\u5c55",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,160,109)"
                        }
                    }
                },
                {
                    "name": "\u5927\u4f6c\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,101,158)"
                        }
                    }
                },
                {
                    "name": "\u7ec6\u5206\u884c\u4e1a\u9f99\u5934\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,124,66)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u5168",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,36,133)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u798f\u5229\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,108,115)"
                        }
                    }
                },
                {
                    "name": "\u91cd\u70b9\u6295\u5165",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,159,66)"
                        }
                    }
                },
                {
                    "name": "\u4ebf\u7ea7\u6570\u636e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,121,137)"
                        }
                    }
                },
                {
                    "name": "\u725b\u4eba\u56e2\u961f\u80cc\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,81,68)"
                        }
                    }
                },
                {
                    "name": "\u5bbd\u5e7f\u7684\u53d1\u5c55\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,95,121)"
                        }
                    }
                },
                {
                    "name": "\u65bd\u5c55\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,10,96)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u98df\u5802",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,114,74)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u6307\u5bfc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,27,48)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u5185\u5934\u90e8\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,3,89)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u901f\u53d1\u5c55\u4e2d\u7684\u521b\u4e1a\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,95,32)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u798f\u5229\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,13,50)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7\u72ec\u89d2\u517d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,155,96)"
                        }
                    }
                },
                {
                    "name": "\u5b5d\u987a\u57fa\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,130,153)"
                        }
                    }
                },
                {
                    "name": "\u5730\u4ea7\u9f99\u5934",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,13,105)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u7a33\u5b9a\u5feb\u901f\u589e\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,150,160)"
                        }
                    }
                },
                {
                    "name": "\u51fa\u6d77",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,85,157)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5382\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,126,38)"
                        }
                    }
                },
                {
                    "name": "\u5168\u7403\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,105,15)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u524d\u666f\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,6,95)"
                        }
                    }
                },
                {
                    "name": "\u725b\u4eba\u5e26\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,48,34)"
                        }
                    }
                },
                {
                    "name": "500\u5f3a\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,31,142)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u805a\u96c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,47,88)"
                        }
                    }
                },
                {
                    "name": "\u8001\u677fNice",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,84,17)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6c1b\u56f4\u5f00\u653e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,17,117)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,118,148)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u5f39\u6027",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,114,26)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u826f\u7684\u4e0a\u5347\u901a\u9053",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,113,139)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u53d1\u5c55\u524d\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,100,102)"
                        }
                    }
                },
                {
                    "name": "\u7b80\u5355\u5f00\u653e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,43,132)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u7ebf\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,155,45)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1atop",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,27,82)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u5f85\u9047\u4f18",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,132,40)"
                        }
                    }
                },
                {
                    "name": "9\u70b9\u6253\u8f66\u62a5\u9500",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,100,41)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u597d\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,102,126)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u4f53\u7cfb\u5b8c\u5584",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,65,27)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,22,77)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u589e\u957f\u5feb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,83,27)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6280\u672f\u5927\u5496\u4e91\u96c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,11,25)"
                        }
                    }
                },
                {
                    "name": "\u6f5c\u529b\u65e0\u9650",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,22,55)"
                        }
                    }
                },
                {
                    "name": "D\u8f6e\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,29,27)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,20,20)"
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
            "text": "\u798f\u5229&\u4f18\u52bf",
            "padding": 5,
            "itemGap": 10,
            "textStyle": {
                "fontSize": 23
            }
        }
    ]
};
        chart_c8ef1fb9cfe447dbb6a3c3b4d49f723f.setOption(option_c8ef1fb9cfe447dbb6a3c3b4d49f723f);
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
