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
            <button class="tablinks" onclick="showChart(event, '224b0438aef04db7ae682fdf8ef01be7')">公司</button>
            <button class="tablinks" onclick="showChart(event, 'de685747bdd64cc1805ae898640e55f1')">城市</button>
            <button class="tablinks" onclick="showChart(event, '20fe3e072b1a4a4485a6b7bc44fe77fd')">城市占比</button>
            <button class="tablinks" onclick="showChart(event, 'dde64eff7d8642a397022f5be788a6cb')">招聘地图</button>
            <button class="tablinks" onclick="showChart(event, '666d2ead2b0a478ab234ac83c49d0f26')">区域</button>
            <button class="tablinks" onclick="showChart(event, 'ee720df033d142b7aea264931c0ec253')">区域占比</button>
            <button class="tablinks" onclick="showChart(event, '862ff413485641c3b6d259d7da82dc32')">公司规模</button>
            <button class="tablinks" onclick="showChart(event, 'ea897d4112f14914b0fd20b7cfb410df')">人员规模</button>
            <button class="tablinks" onclick="showChart(event, '16806f3562174744abd2074641ebe9f1')">行业</button>
            <button class="tablinks" onclick="showChart(event, '9d4d9061574943ce9a2cc45813203298')">招聘方向</button>
            <button class="tablinks" onclick="showChart(event, '8a8456c56af54905929a14cf6ff782a4')">公司福利</button>
    </div>

    <div class="box">
                <div id="224b0438aef04db7ae682fdf8ef01be7" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_224b0438aef04db7ae682fdf8ef01be7 = echarts.init(
            document.getElementById('224b0438aef04db7ae682fdf8ef01be7'), 'white', {renderer: 'canvas'});
            
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
    
        var option_224b0438aef04db7ae682fdf8ef01be7 = {
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
                34,
                30,
                21,
                14,
                14,
                13,
                12,
                12,
                12,
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
                    "value": 34,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,24,82)"
                        }
                    }
                },
                {
                    "name": "\u5b57\u8282\u8df3\u52a8",
                    "value": 30,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,84,144)"
                        }
                    }
                },
                {
                    "name": "\u4eac\u4e1c\u96c6\u56e2",
                    "value": 21,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,88,139)"
                        }
                    }
                },
                {
                    "name": "\u6ef4\u6ef4",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,120,156)"
                        }
                    }
                },
                {
                    "name": "OPPO",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,61,59)"
                        }
                    }
                },
                {
                    "name": "\u7231\u5947\u827a",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,81,152)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u624b",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,119,33)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u6613",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,79,86)"
                        }
                    }
                },
                {
                    "name": "\u4eac\u4e1c\u7269\u6d41",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,10,127)"
                        }
                    }
                },
                {
                    "name": "\u777f\u8d44\u8fbe",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,90,123)"
                        }
                    }
                },
                {
                    "name": "\u643a\u7a0b\u96c6\u56e2",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,157,59)"
                        }
                    }
                },
                {
                    "name": "\u5357\u6e56\u9662",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,80,9)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u78c1\u77f3",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,85,79)"
                        }
                    }
                },
                {
                    "name": "\u6167\u5b89\u91d1\u79d1",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,68,44)"
                        }
                    }
                },
                {
                    "name": "\u767e\u5ea6",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,27,64)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u67d4\u521b\u65b0",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,121,27)"
                        }
                    }
                },
                {
                    "name": "Versa",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,9,150)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u6d6a\u7f51",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,38,147)"
                        }
                    }
                },
                {
                    "name": "\u9177\u5bb6\u4e50",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,63,151)"
                        }
                    }
                },
                {
                    "name": "\u8682\u8681\u96c6\u56e2",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,35,98)"
                        }
                    }
                },
                {
                    "name": "\u4e07\u79d1",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,68,41)"
                        }
                    }
                },
                {
                    "name": "\u4ebf\u8058\u4e16\u7eaa",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,151,99)"
                        }
                    }
                },
                {
                    "name": "\u8d5b\u76ee\u79d1\u6280",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,76,12)"
                        }
                    }
                },
                {
                    "name": "\u5faa\u73af\u667a\u80fd",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,146,88)"
                        }
                    }
                },
                {
                    "name": "\u4f5c\u4e1a\u5e2e",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,32,31)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u51b0",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,77,69)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u4eba\u5bff",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,159,119)"
                        }
                    }
                },
                {
                    "name": "\u5546\u6c64\u79d1\u6280",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,45,58)"
                        }
                    }
                },
                {
                    "name": "\u76c8\u5609\u4e92\u8054",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,23,118)"
                        }
                    }
                },
                {
                    "name": "\u730e\u6237\u661f\u7a7a",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,92,25)"
                        }
                    }
                },
                {
                    "name": "\u7693\u884c\u79d1\u6280",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,53,152)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u79d1\u6280",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,20,13)"
                        }
                    }
                },
                {
                    "name": "Gostudy",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,32,73)"
                        }
                    }
                },
                {
                    "name": "\u5929\u773c\u67e5",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,152,33)"
                        }
                    }
                },
                {
                    "name": "\u5fc5\u793a\u79d1\u6280",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,125,36)"
                        }
                    }
                },
                {
                    "name": "\u706b\u773c\u4e91",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,111,71)"
                        }
                    }
                },
                {
                    "name": "360os",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,86,70)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77\u6c38\u8f89\u8d85\u5e02\u6709\u9650\u516c\u53f8",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,43,68)"
                        }
                    }
                },
                {
                    "name": "\u9605\u6587\u96c6\u56e2",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,49,69)"
                        }
                    }
                },
                {
                    "name": "\u6ee1\u5e2e\u96c6\u56e2",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,23,109)"
                        }
                    }
                },
                {
                    "name": "360",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,36,99)"
                        }
                    }
                },
                {
                    "name": "Shopee",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,45,124)"
                        }
                    }
                },
                {
                    "name": "\u6566\u714c\u7f51",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,128,50)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u5e02\u6bd4\u4e00\u6bd4\u7f51\u7edc\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,40,158)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5c1a\u79d1\u6280",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,107,5)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u5929\u52b1\u98de",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,77,6)"
                        }
                    }
                },
                {
                    "name": "\u667a\u62d3\u89c6\u754c",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,153,146)"
                        }
                    }
                },
                {
                    "name": "\u597d\u672a\u6765",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,83,94)"
                        }
                    }
                },
                {
                    "name": "\u8d1d\u58f3",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,113,33)"
                        }
                    }
                },
                {
                    "name": "Yeahmobi",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,14,25)"
                        }
                    }
                },
                {
                    "name": "\u8c31\u65f6\u660a\u552f\u6570\u636e",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,80,140)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u5982\u79c4",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,71,99)"
                        }
                    }
                },
                {
                    "name": "\u4eac\u4e1c\u79d1\u6280",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,157,142)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77\u6cdb\u89c6\u89d2",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,107,42)"
                        }
                    }
                },
                {
                    "name": "Keep",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,116,68)"
                        }
                    }
                },
                {
                    "name": "\u56db\u5408\u5929\u5730",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,102,52)"
                        }
                    }
                },
                {
                    "name": "\u5f97\u7269App",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,102,157)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u56fe\u79d1\u6280",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,31,62)"
                        }
                    }
                },
                {
                    "name": "\u5cb1\u609f\u667a\u80fd",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,77,39)"
                        }
                    }
                },
                {
                    "name": "\u597d\u5927\u592b\u5728\u7ebf",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,160,50)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u5b8f\u74f4\u79d1\u6280\u53d1\u5c55\u6709\u9650...",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,134,10)"
                        }
                    }
                },
                {
                    "name": "PowerVision",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,33,28)"
                        }
                    }
                },
                {
                    "name": "\u89e6\u5b9d",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,76,18)"
                        }
                    }
                },
                {
                    "name": "\u641c\u72d7",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,128,105)"
                        }
                    }
                },
                {
                    "name": "GYENNO",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,77,18)"
                        }
                    }
                },
                {
                    "name": "\u6570\u5764\u79d1\u6280",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,37,62)"
                        }
                    }
                },
                {
                    "name": "\u5600\u55d2\u51fa\u884c",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,89,56)"
                        }
                    }
                },
                {
                    "name": "ZOOM",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,124,57)"
                        }
                    }
                },
                {
                    "name": "\u8c10\u76df\u673a\u5668\u4eba",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,150,152)"
                        }
                    }
                },
                {
                    "name": "\u827e\u8015\u79d1\u6280",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,60,76)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u597d\u5b66",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,106,95)"
                        }
                    }
                },
                {
                    "name": "Insta360\u5f71\u77f3",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,21,16)"
                        }
                    }
                },
                {
                    "name": "westwell\u897f\u4e95\u79d1\u6280",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,35,98)"
                        }
                    }
                },
                {
                    "name": "\u65f7\u89c6MEGVII",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,32,137)"
                        }
                    }
                },
                {
                    "name": "\u5927\u540d\u8f6f\u4ef6",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,49,67)"
                        }
                    }
                },
                {
                    "name": "\u6700\u53f3",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,26,39)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u89c6\u521b\u65b0",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,140,69)"
                        }
                    }
                },
                {
                    "name": "MINIEYE",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,60,51)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u6052\u4fe1\u606f",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,116,69)"
                        }
                    }
                },
                {
                    "name": "\u6d4b\u6d4b",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,26,7)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u62cd\u5802",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,158,159)"
                        }
                    }
                },
                {
                    "name": "\u9177\u72d7\u97f3\u4e50",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,5,97)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u601d\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,141,21)"
                        }
                    }
                },
                {
                    "name": "\u9053\u9053",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,123,8)"
                        }
                    }
                },
                {
                    "name": "\u5143\u6a61\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,40,102)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u6da6\u5bcc\u8054",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,76,79)"
                        }
                    }
                },
                {
                    "name": "\u8054\u901a\uff08\u5e7f\u4e1c\uff09\u4ea7\u4e1a\u4e92\u8054\u7f51...",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,121,38)"
                        }
                    }
                },
                {
                    "name": "Soul",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,127,76)"
                        }
                    }
                },
                {
                    "name": "\u8304\u5b50\u5feb\u4f20",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,131,103)"
                        }
                    }
                },
                {
                    "name": "\u5e03\u5c14\u827a\u6570",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,86,115)"
                        }
                    }
                },
                {
                    "name": "\u77e9\u9635\u5143",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,150,120)"
                        }
                    }
                },
                {
                    "name": "\u8fbe\u89c2\u6570\u636e",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,14,17)"
                        }
                    }
                },
                {
                    "name": "\u57c3\u514b\u65af\u5de5\u4e1a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,132,47)"
                        }
                    }
                },
                {
                    "name": "CraiditX",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,35,124)"
                        }
                    }
                },
                {
                    "name": "\u534e\u4e3a\u6280\u672f\u6709\u9650\u516c\u53f8",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,40,43)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u72d7\u6253\u8f66",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,125,160)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u7586\u667a\u80fd",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,57,44)"
                        }
                    }
                },
                {
                    "name": "\u8f7b\u821f\u667a\u822a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,91,7)"
                        }
                    }
                },
                {
                    "name": "\u963f\u91cc\u5df4\u5df4-\u9ad8\u5fb7",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,29,27)"
                        }
                    }
                },
                {
                    "name": "\u8fc5\u6e38\u7f51\u7edc",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,50,98)"
                        }
                    }
                },
                {
                    "name": "\u51fa\u95e8\u95ee\u95ee",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,17,113)"
                        }
                    }
                },
                {
                    "name": "Convert lab",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,48,90)"
                        }
                    }
                },
                {
                    "name": "FunPlus \u8da3\u52a0\u6e38\u620f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,75,59)"
                        }
                    }
                },
                {
                    "name": "\u89c2\u8fdc\u6570\u636e",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,80,56)"
                        }
                    }
                },
                {
                    "name": "\u5151\u5427",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,44,116)"
                        }
                    }
                },
                {
                    "name": "\u54d4\u54e9\u54d4\u54e9",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,14,86)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u4ed3\u667a\u80fd\u4ed3\u50a8",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,124,3)"
                        }
                    }
                },
                {
                    "name": "\u7ea2\u661f\u7f8e\u51ef\u9f99",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,57,79)"
                        }
                    }
                },
                {
                    "name": "\u5f71\u8c31\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,36,75)"
                        }
                    }
                },
                {
                    "name": "\u6d3e\u5ba2\u6734\u98df",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,77,98)"
                        }
                    }
                },
                {
                    "name": "EM3",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,156,160)"
                        }
                    }
                },
                {
                    "name": "\u84dd\u9e3d\u96c6\u56e2",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,142,77)"
                        }
                    }
                },
                {
                    "name": "\u71e7\u4eba\u533b\u7597",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,94,67)"
                        }
                    }
                },
                {
                    "name": "Roborock",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,143,141)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u77e5\u672a\u6765",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,35,65)"
                        }
                    }
                },
                {
                    "name": "\u8da3\u5934\u6761",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,65,13)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u56fd\u90ae\u653f\u50a8\u84c4\u94f6\u884c",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,88,78)"
                        }
                    }
                },
                {
                    "name": "AKULAKU",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,74,110)"
                        }
                    }
                },
                {
                    "name": "\u8d27\u62c9\u62c9",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,101,36)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u5065\u5eb7",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,51,63)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u8111\u94f6\u6cb3",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,141,151)"
                        }
                    }
                },
                {
                    "name": "\u6781\u5149",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,18,37)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e4b\u6613",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,14,99)"
                        }
                    }
                },
                {
                    "name": "\u9cb8\u822a\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,113,103)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u60f3\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,89,15)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u533b\u7597",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,66,30)"
                        }
                    }
                },
                {
                    "name": "\u9646\u91d1\u6240",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,160,19)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u9c7c\u6613\u8fde",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,47,127)"
                        }
                    }
                },
                {
                    "name": "\u5f71\u521b\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,129,97)"
                        }
                    }
                },
                {
                    "name": "\u79fb\u52a8\u7814\u7a76\u9662",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,103,80)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6167\u82bd",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,146,50)"
                        }
                    }
                },
                {
                    "name": "\u8054\u5408\u96c6\u56e2",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,152,153)"
                        }
                    }
                },
                {
                    "name": "\u6167\u62e9\u7f51",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,66,136)"
                        }
                    }
                },
                {
                    "name": "\u95ea\u9a6c\u667a\u80fd",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,109,142)"
                        }
                    }
                },
                {
                    "name": "\u58a8\u4e91\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,66,22)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u7bc7",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,58,118)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u4e1c\u4e09\u7ef4\u5bb6\u4fe1\u606f\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,39,122)"
                        }
                    }
                },
                {
                    "name": "\u957f\u5730\u4e07\u65b9",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,86,150)"
                        }
                    }
                },
                {
                    "name": "\u5c45\u7406\u65b0\u623f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,17,61)"
                        }
                    }
                },
                {
                    "name": "Disney+Hotstar",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,8,8)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u4ea7\u9669",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,145,74)"
                        }
                    }
                },
                {
                    "name": "\u7fcc\u65e5\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,150,124)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77\u827e\u9e92",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,20,132)"
                        }
                    }
                },
                {
                    "name": "Uni-Ubi",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,67,62)"
                        }
                    }
                },
                {
                    "name": "\u534e\u98de\u6570\u636e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,145,116)"
                        }
                    }
                },
                {
                    "name": "\u5bbd\u5f85\u4e92\u8054\u7f51",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,34,79)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u7535\u6167\u5b89",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,119,152)"
                        }
                    }
                },
                {
                    "name": "Beta\u8d22\u5bcc",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,139,127)"
                        }
                    }
                },
                {
                    "name": "\u7269\u754c\uff08\u4e0a\u6d77\uff09\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,66,115)"
                        }
                    }
                },
                {
                    "name": "\u7d2b\u5149\u6559\u80b2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,41,150)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u89c2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,50,76)"
                        }
                    }
                },
                {
                    "name": "\u733f\u8f85\u5bfc",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,140,28)"
                        }
                    }
                },
                {
                    "name": "\u7ecf\u4f20\u591a\u8d62",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,53,25)"
                        }
                    }
                },
                {
                    "name": "\u8bc1\u901a\u80a1\u4efd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,74,71)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u805a\u672a\u6765",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,149,82)"
                        }
                    }
                },
                {
                    "name": "\u900f\u5f7b\u5f71\u50cf",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,92,46)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77\u4e92\u6559\u6559\u80b2\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,6,16)"
                        }
                    }
                },
                {
                    "name": "\u592a\u5b57\u6d41\u52a8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,87,126)"
                        }
                    }
                },
                {
                    "name": "roobo",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,70,36)"
                        }
                    }
                },
                {
                    "name": "\u6da6\u5efa\u80a1\u4efd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,109,128)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u7684\u96c6\u56e2IT",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,125,87)"
                        }
                    }
                },
                {
                    "name": "vivo",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,11,98)"
                        }
                    }
                },
                {
                    "name": "BLUE",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,78,117)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u65b9\u660e\u73e0\u65b0\u5a92\u4f53",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,138,18)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u4e4e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,114,99)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u539f\u6d88\u8d39\u91d1\u878d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,139,26)"
                        }
                    }
                },
                {
                    "name": "\u667a\u52a0\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,94,96)"
                        }
                    }
                },
                {
                    "name": "\u7d2b\u5149\u534e\u667a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,46,128)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u58f0\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,30,66)"
                        }
                    }
                },
                {
                    "name": "\u864e\u535a\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,14,57)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u79d8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,133,18)"
                        }
                    }
                },
                {
                    "name": "\u6210\u90fd\u5e02\u5c39\u8679\u4fe1\u606f\u6280\u672f\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,114,76)"
                        }
                    }
                },
                {
                    "name": "\u661f\u836f\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,121,13)"
                        }
                    }
                },
                {
                    "name": "\u667a\u610f\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,60,82)"
                        }
                    }
                },
                {
                    "name": "\u795e\u7b56\u6570\u636e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,115,76)"
                        }
                    }
                },
                {
                    "name": "\u8f66\u597d\u591a\u96c6\u56e2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,41,91)"
                        }
                    }
                },
                {
                    "name": "\u7ffc\u9e25\u6559\u80b2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,70,90)"
                        }
                    }
                },
                {
                    "name": "\u6700\u6709\u6599",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,135,111)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5965\u7279\u89c6\u9891",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,119,51)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u5c71\u4e16\u6e38",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,60,4)"
                        }
                    }
                },
                {
                    "name": "\u5b8f\u5251\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,10,88)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u5965\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,49,125)"
                        }
                    }
                },
                {
                    "name": "\u777f\u9b54\u667a\u80fd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,73,78)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u4ed5\u5bfb\u4eba\u529b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,81,84)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u5dde\u9ed1\u683c\u667a\u9020\u4fe1\u606f\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,52,90)"
                        }
                    }
                },
                {
                    "name": "\u6bb7\u56fe\u7f51\u8054",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,63,129)"
                        }
                    }
                },
                {
                    "name": "\u5929\u55bb\u4fe1\u606f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,111,20)"
                        }
                    }
                },
                {
                    "name": "\u5927\u519c\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,54,39)"
                        }
                    }
                },
                {
                    "name": "Momenta",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,79,93)"
                        }
                    }
                },
                {
                    "name": "TalkingData",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,122,154)"
                        }
                    }
                },
                {
                    "name": "\u90bb\u6c47\u5427",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,37,141)"
                        }
                    }
                },
                {
                    "name": "\u548c\u4fe1\u5eb7",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,20,59)"
                        }
                    }
                },
                {
                    "name": "\u8d27\u7279\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,27,9)"
                        }
                    }
                },
                {
                    "name": "\u677e\u7acb\u63a7\u80a1\u96c6\u56e2\u80a1\u4efd\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,35,87)"
                        }
                    }
                },
                {
                    "name": "\u8206\u9686\u5174\u8fbe",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,24,81)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5e0c\u671b\u516d\u548c",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,130,55)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u8054\u82f1\u8bed",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,39,38)"
                        }
                    }
                },
                {
                    "name": "\u5965\u6bd4\u4e2d\u5149",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,104,119)"
                        }
                    }
                },
                {
                    "name": "\u5929\u6e90\u8fea\u79d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,64,63)"
                        }
                    }
                },
                {
                    "name": "\u751f\u7269\u56fe\u817e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,4,69)"
                        }
                    }
                },
                {
                    "name": "\u63a2\u77e5\u6570\u636e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,17,44)"
                        }
                    }
                },
                {
                    "name": "\u6885\u5361\u66fc\u5fb7",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,85,107)"
                        }
                    }
                },
                {
                    "name": "\u4f73\u5146\u4e1a\u6295\u8d44\u54a8\u8be2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,119,78)"
                        }
                    }
                },
                {
                    "name": "YY",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,77,105)"
                        }
                    }
                },
                {
                    "name": "\u5e86\u4e91\u77f3\u6cb9",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,30,15)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u8bc1\u80a1\u4efd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,80,15)"
                        }
                    }
                },
                {
                    "name": "\u6c83\u98de\u957f\u7a7a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,88,13)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u5dde\u5e02\u5965\u5a01\u4e9a\u7535\u5b50\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,107,105)"
                        }
                    }
                },
                {
                    "name": "\u9890\u90a6\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,117,90)"
                        }
                    }
                },
                {
                    "name": "\u4e3a\u534e\u7f51\u7edc",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,81,120)"
                        }
                    }
                },
                {
                    "name": "\u9053\u8fbe\u5929\u9645",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,44,89)"
                        }
                    }
                },
                {
                    "name": "\u5343\u5de1\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,115,147)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u77e5\u667a\u80fd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,9,146)"
                        }
                    }
                },
                {
                    "name": "\u873b\u8713FM",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,15,116)"
                        }
                    }
                },
                {
                    "name": "\u516d\u4e00\u6559\u80b2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,62,67)"
                        }
                    }
                },
                {
                    "name": "\u672a\u6765\u79d1\u6280\u57ce",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,96,106)"
                        }
                    }
                },
                {
                    "name": "\u6cf0\u5766\u667a\u6167",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,134,114)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u5dde\u5c0f\u8fc8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,150,80)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u65b9\u56fd\u4fe1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,0,45)"
                        }
                    }
                },
                {
                    "name": "\u9489\u9489",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,20,82)"
                        }
                    }
                },
                {
                    "name": "\u84dd\u6e56",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,153,60)"
                        }
                    }
                },
                {
                    "name": "\u6ef4\u666e\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,47,84)"
                        }
                    }
                },
                {
                    "name": "\u6765\u672a\u6765",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,74,82)"
                        }
                    }
                },
                {
                    "name": "\u6b66\u6c49\u7269\u6613\u4e91\u901a\u7f51\u7edc\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,96,84)"
                        }
                    }
                },
                {
                    "name": "\u9014\u864e\u517b\u8f66",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,155,13)"
                        }
                    }
                },
                {
                    "name": "\u4f2f\u6069\u5149\u5b66",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,121,145)"
                        }
                    }
                },
                {
                    "name": "\u90a3\u4e0e\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,134,115)"
                        }
                    }
                },
                {
                    "name": "\u8fc1\u79fb\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,83,158)"
                        }
                    }
                },
                {
                    "name": "\u8da3\u94fe\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,150,147)"
                        }
                    }
                },
                {
                    "name": "\u767e\u878d\u4e91\u521b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,27,24)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u4e50\u79cd\u5b50",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,141,30)"
                        }
                    }
                },
                {
                    "name": "\u6c5f\u884c\u667a\u80fd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,157,37)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u6e90\u6052\u9645",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,90,80)"
                        }
                    }
                },
                {
                    "name": "\u8611\u83c7\u8857",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,32,13)"
                        }
                    }
                },
                {
                    "name": "\u8de8\u8d8a\u901f\u8fd0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,54,30)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u5e02\u6709\u4f20\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,155,61)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u5c45\u5ba2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,79,61)"
                        }
                    }
                },
                {
                    "name": "\u676d\u5dde\u667a\u56e2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,79,67)"
                        }
                    }
                },
                {
                    "name": "\u5f71\u7b11\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,16,115)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u56fe\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,46,30)"
                        }
                    }
                },
                {
                    "name": "\u5706\u901a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,11,31)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u8bc1\u4f18\u667a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,60,156)"
                        }
                    }
                },
                {
                    "name": "\u4e50\u6211\u65e0\u9650",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,6,96)"
                        }
                    }
                },
                {
                    "name": "\u6613\u6d41",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,12,133)"
                        }
                    }
                },
                {
                    "name": "\u6709\u4e3a\u4fe1\u606f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,136,65)"
                        }
                    }
                },
                {
                    "name": "\u676d\u5dde\u9886\u89c1\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,22,64)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u6cf0\u661f\u4e91",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,8,137)"
                        }
                    }
                },
                {
                    "name": "\u987a\u4e30\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,105,98)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u7814\u7f51",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,83,97)"
                        }
                    }
                },
                {
                    "name": "\u666e\u6e21\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,35,98)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77\u835f\u529b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,75,143)"
                        }
                    }
                },
                {
                    "name": "\u89c5\u777f\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,135,133)"
                        }
                    }
                },
                {
                    "name": "\u957f\u6295\u5b66\u5802",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,70,58)"
                        }
                    }
                },
                {
                    "name": "\u53ca\u672a\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,79,157)"
                        }
                    }
                },
                {
                    "name": "\u5fb7\u9002\u751f\u7269",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,10,103)"
                        }
                    }
                },
                {
                    "name": "\u51cc\u5b87\u667a\u63a7\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,18,59)"
                        }
                    }
                },
                {
                    "name": "\u4eb2\u5b9d\u5b9d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,160,111)"
                        }
                    }
                },
                {
                    "name": "\u9f99\u6e56\u96c6\u56e2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,30,152)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u5168\u751f\u4ea7\u79d1\u5b66\u7814\u7a76\u9662",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,126,41)"
                        }
                    }
                },
                {
                    "name": "\u533b\u836f\u9b54\u65b9",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,52,80)"
                        }
                    }
                },
                {
                    "name": "\u601d\u7ef4\u9020\u7269",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,121,14)"
                        }
                    }
                },
                {
                    "name": "\u521b\u90bb\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,33,7)"
                        }
                    }
                },
                {
                    "name": "\u8f6c\u8f6c",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,26,40)"
                        }
                    }
                },
                {
                    "name": "\u8da3\u4e38",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,20,87)"
                        }
                    }
                },
                {
                    "name": "\u91cd\u5e86\u957f\u5b89\u6c7d\u8f66\u8f6f\u4ef6\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,101,116)"
                        }
                    }
                },
                {
                    "name": "\u8fc8\u6da6\u667a\u80fd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,143,76)"
                        }
                    }
                },
                {
                    "name": "\u665f\u89c6\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,117,83)"
                        }
                    }
                },
                {
                    "name": "\u4f34\u9c7c",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,27,127)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u5929\u4f1f\u4e1a\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,113,81)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u6df1\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,137,0)"
                        }
                    }
                },
                {
                    "name": "\u6d6a\u6dd8\u91d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,57,123)"
                        }
                    }
                },
                {
                    "name": "\u6d41\u5229\u8bf4\u00ae",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,29,120)"
                        }
                    }
                },
                {
                    "name": "\u7279\u8d5e|Tezign",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,76,64)"
                        }
                    }
                },
                {
                    "name": "\u601d\u8d24\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,83,54)"
                        }
                    }
                },
                {
                    "name": "\u949b\u6c2a\u65b0\u5a92\u4f53\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,111,29)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u8d4b\u667a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,129,89)"
                        }
                    }
                },
                {
                    "name": "\u6749\u6570\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,110,21)"
                        }
                    }
                },
                {
                    "name": "\u817e\u8baf",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,19,24)"
                        }
                    }
                },
                {
                    "name": "\u864e\u7259\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,125,28)"
                        }
                    }
                },
                {
                    "name": "\u5e93\u73c0\u6052\u5b89",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,108,69)"
                        }
                    }
                },
                {
                    "name": "\u6dfb\u695a\u701a\u624d\u4f20\u5a92",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,16,130)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u80fd\u534e\u667a\u80fd\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,105,132)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u5c71\u529e\u516c\u8f6f\u4ef6",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,20,5)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e91\u667a\u80fd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,46,40)"
                        }
                    }
                },
                {
                    "name": "\u5fb7\u777f\u667a\u836f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,122,77)"
                        }
                    }
                },
                {
                    "name": "\u5927\u9a90\u6570\u636e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,69,116)"
                        }
                    }
                },
                {
                    "name": "\u7075\u52a8\u97f3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,34,160)"
                        }
                    }
                },
                {
                    "name": "\u534e\u91cc\u7f51\u7edc",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,39,82)"
                        }
                    }
                },
                {
                    "name": "\u4ebf\u5496\u901a\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,34,5)"
                        }
                    }
                },
                {
                    "name": "\u6807\u8d1d\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,16,39)"
                        }
                    }
                },
                {
                    "name": "\u817e\u5c55\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,23,159)"
                        }
                    }
                },
                {
                    "name": "Moka",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,28,54)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u6717\u9053\u667a\u901a\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,18,34)"
                        }
                    }
                },
                {
                    "name": "\u536b\u74f4\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,0,121)"
                        }
                    }
                },
                {
                    "name": "\u6210\u90fd\u62df\u5408\u672a\u6765\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,105,72)"
                        }
                    }
                },
                {
                    "name": "\u8054\u4ec1\u5065\u5eb7\u533b\u7597\u5927\u6570\u636e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,18,123)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u627f\u6cf0\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,44,15)"
                        }
                    }
                },
                {
                    "name": "\u835f\u8bda\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,145,5)"
                        }
                    }
                },
                {
                    "name": "\u6709\u4e2a\u673a\u5668\u4eba",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,88,153)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u601d\u7586",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,24,17)"
                        }
                    }
                },
                {
                    "name": "\u54d7\u5566\u5566",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,84,31)"
                        }
                    }
                },
                {
                    "name": "TCL",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,59,20)"
                        }
                    }
                },
                {
                    "name": "LAYABOX",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,118,14)"
                        }
                    }
                },
                {
                    "name": "\u7279\u9e4f\u7f51\u7edc",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,89,12)"
                        }
                    }
                },
                {
                    "name": "\u661f\u71b9\u5143\u6295\u8d44\u7ba1\u7406",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,44,102)"
                        }
                    }
                },
                {
                    "name": "\u6253\u9020\u6700\u597d\u7684\u5728\u7ebf\u4eba\u8138\u8bc6\u522b\u5f15\u64ce",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,42,30)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u4fe1\u65f6\u4ee3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,5,47)"
                        }
                    }
                },
                {
                    "name": "Long Bridge",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,20,49)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u56fd\u79d1\u5b66\u9662\u7535\u5b50\u5b66\u7814\u7a76\u6240\u82cf\u5dde\u7814\u7a76\u9662",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,108,141)"
                        }
                    }
                },
                {
                    "name": "\u8bfa\u5a01\u534e\u4ed5\u7ba1\u7406\u54a8\u8be2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,150,132)"
                        }
                    }
                },
                {
                    "name": "\u521b\u6cf0\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,148,119)"
                        }
                    }
                },
                {
                    "name": "\u671d\u4e91\u5e06\u751f\u7269",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,74,144)"
                        }
                    }
                },
                {
                    "name": "\u6c34\u6ef4 WATERDROP INC",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,1,3)"
                        }
                    }
                },
                {
                    "name": "\u8389\u8389\u4e1d\u6e38\u620f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,28,61)"
                        }
                    }
                },
                {
                    "name": "MetaApp",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,141,112)"
                        }
                    }
                },
                {
                    "name": "\u827e\u7f8e\u7f51\u7edc\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,9,20)"
                        }
                    }
                },
                {
                    "name": "\u72ee\u6865\u96c6\u56e2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,140,63)"
                        }
                    }
                },
                {
                    "name": "\u4f73\u987a\u667a\u80fd\u673a\u5668\u4eba",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,120,109)"
                        }
                    }
                },
                {
                    "name": "Aibee",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,48,67)"
                        }
                    }
                },
                {
                    "name": "\u4e3a\u5de5\u667a\u80fd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,44,128)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u90ae\u4fe1\u606f\u79d1\u6280\uff08\u5317\u4eac\uff09\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,152,128)"
                        }
                    }
                },
                {
                    "name": "\u5149\u7ebf\u4e91",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,148,92)"
                        }
                    }
                },
                {
                    "name": "\u521b\u65b0\u5de5\u573aAI\u5de5\u7a0b\u9662",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,33,84)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u4ea7360",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,7,70)"
                        }
                    }
                },
                {
                    "name": "\u82f1\u8bed\u8da3\u914d\u97f3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,52,54)"
                        }
                    }
                },
                {
                    "name": "\u6cfd\u97f6\u667a\u80fd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,1,53)"
                        }
                    }
                },
                {
                    "name": "\u661f\u8206\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,35,38)"
                        }
                    }
                },
                {
                    "name": "\u8ff7\u9e7f\u97f3\u4e50",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,117,93)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u5a31\u65f6\u5149",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,42,5)"
                        }
                    }
                },
                {
                    "name": "Walmart China",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,146,20)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u68f5\u6995\u4f01\u4e1a\u7ba1\u7406\u987e\u95ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,107,136)"
                        }
                    }
                },
                {
                    "name": "\u767b\u8679",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,36,119)"
                        }
                    }
                },
                {
                    "name": "\u5f53\u5f53\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,146,144)"
                        }
                    }
                },
                {
                    "name": "\u7279\u91d1\u65e0\u7ebf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,125,15)"
                        }
                    }
                },
                {
                    "name": "\u5fb7\u624d\u4f01\u4e1a\u54a8\u8be2\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,74,140)"
                        }
                    }
                },
                {
                    "name": "\u64ce\u76fe\u6570\u636e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,133,82)"
                        }
                    }
                },
                {
                    "name": "\u7bf1\u7b06\u5899",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,53,26)"
                        }
                    }
                },
                {
                    "name": "\u4f0a\u5bf9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,122,63)"
                        }
                    }
                },
                {
                    "name": "\u9a6c\u4e0a\u8d62",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,78,111)"
                        }
                    }
                },
                {
                    "name": "\u8f7b\u8f7b\u6559\u80b2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,9,34)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u7ec7\u7b97\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,139,70)"
                        }
                    }
                },
                {
                    "name": "\u767e\u4fe1\u94f6\u884c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,124,141)"
                        }
                    }
                },
                {
                    "name": "\u827e\u6d1b\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,148,117)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u8003\u76f4\u901a\u8f66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,77,130)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u65b9\u4f4e\u78b3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,107,39)"
                        }
                    }
                },
                {
                    "name": "\u6210\u90fd\u8086\u96f6\u8086",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,81,157)"
                        }
                    }
                },
                {
                    "name": "Kika Tech(\u65b0\u7f8e\u4e92\u901a)",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,117,50)"
                        }
                    }
                },
                {
                    "name": "\u8fdc\u7738\u8f6f\u4ef6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,91,118)"
                        }
                    }
                },
                {
                    "name": "\u68f1\u955c\u4e91\u6865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,8,108)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u4e1a\u989c\u7a76\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,133,144)"
                        }
                    }
                },
                {
                    "name": "\u62e9\u8fbe\u4eba\u529b\u8d44\u6e90",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,39,136)"
                        }
                    }
                },
                {
                    "name": "\u540c\u7eb3\u4fe1\u606f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,143,154)"
                        }
                    }
                },
                {
                    "name": "\u8d5b\u8235\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,121,1)"
                        }
                    }
                },
                {
                    "name": "\u7ade\u6280\u4e16\u754c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,87,69)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u949b\u673a\u5668\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,146,6)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u6ee1\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,102,95)"
                        }
                    }
                },
                {
                    "name": "DataEye",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,50,28)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u56fd\u65c5\u6e38\u96c6\u56e2\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,112,123)"
                        }
                    }
                },
                {
                    "name": "\u5927\u542f\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,105,146)"
                        }
                    }
                },
                {
                    "name": "\u5343\u725b\u7f51\u7edc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,84,157)"
                        }
                    }
                },
                {
                    "name": "\u5546\u60c5\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,97,20)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,49,121)"
                        }
                    }
                },
                {
                    "name": "\u592a\u5e73\u6d0b\u623f\u5730\u4ea7\u7ecf\u7eaa\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,147,152)"
                        }
                    }
                },
                {
                    "name": "\u7c73\u7edc\u661f\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,69,151)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u5bb6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,82,101)"
                        }
                    }
                },
                {
                    "name": "\u534e\u5f55\u8d85\u6e05\u6587\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,138,83)"
                        }
                    }
                },
                {
                    "name": "\u730e\u4f18\u4f01\u4e1a\u7ba1\u7406\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,79,75)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u57df\u94ed\u5c9b\uff08\u5409\u5229\u5de5\u4e1a\u4e92\u8054\u7f51\uff09",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,68,53)"
                        }
                    }
                },
                {
                    "name": "\u9510\u4ed5\u65b9\u8fbe\u6d4e\u5357\u5206\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,72,36)"
                        }
                    }
                },
                {
                    "name": "\u6b66\u6c49TCL",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,143,142)"
                        }
                    }
                },
                {
                    "name": "\u51ef\u8fea\u4ed5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,155,138)"
                        }
                    }
                },
                {
                    "name": "\u84dd\u8bfa\u5fae\u94f6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,147,78)"
                        }
                    }
                },
                {
                    "name": "\u5609\u9a70\u56fd\u9645\u5546\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,151,64)"
                        }
                    }
                },
                {
                    "name": "\u9633\u5149\u4fdd\u9669\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,25,129)"
                        }
                    }
                },
                {
                    "name": "\u5353\u671b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,36,65)"
                        }
                    }
                },
                {
                    "name": "\u795e\u5dde\u79df\u8f66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,28,151)"
                        }
                    }
                },
                {
                    "name": "\u548f\u67f3\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,23,94)"
                        }
                    }
                },
                {
                    "name": "\u805a\u5bbd JoinQuant",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,21,147)"
                        }
                    }
                },
                {
                    "name": "\u7545\u804a\u5929\u4e0b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,124,130)"
                        }
                    }
                },
                {
                    "name": "\u535a\u777f\u701a\u8fbe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,29,62)"
                        }
                    }
                },
                {
                    "name": "\u6613\u5c45\u4e2d\u56fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,36,55)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5965\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,94,125)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u7684\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,46,158)"
                        }
                    }
                },
                {
                    "name": "\u6444\u661f\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,9,100)"
                        }
                    }
                },
                {
                    "name": "\u963f\u91cc\u5df4\u5df4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,43,73)"
                        }
                    }
                },
                {
                    "name": "\u827e\u7f8e\u661f\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,123,87)"
                        }
                    }
                },
                {
                    "name": "\u683c\u5170\u4ed5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,153,82)"
                        }
                    }
                },
                {
                    "name": "\u8baf\u6c47\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,130,1)"
                        }
                    }
                },
                {
                    "name": "\u6a0a\u767b\u8bfb\u4e66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,68,27)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u6c47\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,17,92)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u6b65\u7f51\u7edc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,80,106)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u5c16\u5cf0\u6b66\u6c49\u5206\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,48,41)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u5dde\u7075\u611f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,152,78)"
                        }
                    }
                },
                {
                    "name": "\u5317\u660e\u6570\u79d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,29,111)"
                        }
                    }
                },
                {
                    "name": "\u9e7f\u9e6d\u7f51\u7edc\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,50,135)"
                        }
                    }
                },
                {
                    "name": "\u7545\u6377\u901a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,117,37)"
                        }
                    }
                },
                {
                    "name": "\u63a2\u63a2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,133,9)"
                        }
                    }
                },
                {
                    "name": "\u767e\u70bc\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,146,76)"
                        }
                    }
                },
                {
                    "name": "\u8fde\u4fe1\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,109,11)"
                        }
                    }
                },
                {
                    "name": "\u9518\u5d34\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,101,95)"
                        }
                    }
                },
                {
                    "name": "\u65f6\u4ee3\u62d3\u7075",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,51,101)"
                        }
                    }
                },
                {
                    "name": "\u5b8f\u9e3f\u94a5\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,55,121)"
                        }
                    }
                },
                {
                    "name": "\u6d59\u6c5f\u6cd5\u4e4b\u9053\u4fe1\u606f\u6280\u672f\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,58,101)"
                        }
                    }
                },
                {
                    "name": "\u957f\u4ead\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,36,58)"
                        }
                    }
                },
                {
                    "name": "\u5171\u6709\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,69,7)"
                        }
                    }
                },
                {
                    "name": "\u9f50\u78b3\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,155,82)"
                        }
                    }
                },
                {
                    "name": "\u521b\u65b0\u5947\u667a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,67,7)"
                        }
                    }
                },
                {
                    "name": "\u732b\u773c\u7535\u5f71",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,67,109)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6167\u732b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,52,21)"
                        }
                    }
                },
                {
                    "name": "\u661f\u5c18\u6570\u636e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,64,1)"
                        }
                    }
                },
                {
                    "name": "\u667a\u8d1d\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,132,43)"
                        }
                    }
                },
                {
                    "name": "Flash express",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,59,38)"
                        }
                    }
                },
                {
                    "name": "\u534e\u667a\u751f\u7269",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,155,119)"
                        }
                    }
                },
                {
                    "name": "\u9c81\u73ed\u5ae1\u7cfb\u673a\u5668\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,134,148)"
                        }
                    }
                },
                {
                    "name": "\u9177\u5f00\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,107,108)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u4e1c\u4ebf\u8fc5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,58,73)"
                        }
                    }
                },
                {
                    "name": "\u5929\u6570\u667a\u82af",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,110,91)"
                        }
                    }
                },
                {
                    "name": "\u8054\u901a\u4e91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,105,57)"
                        }
                    }
                },
                {
                    "name": "\u9b54\u7b77\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,12,72)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u4e1c\u667a\u6e90",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,13,18)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u84dd\u5361\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,127,96)"
                        }
                    }
                },
                {
                    "name": "\u9633\u5149\u94ed\u5c9b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,1,89)"
                        }
                    }
                },
                {
                    "name": "\u7425\u73c0\u521b\u60f3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,44,136)"
                        }
                    }
                },
                {
                    "name": "\u4f20\u5174\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,26,133)"
                        }
                    }
                },
                {
                    "name": "\u8054\u901a\u667a\u7f51\u521b\u65b0\u4e2d\u5fc3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,84,128)"
                        }
                    }
                },
                {
                    "name": "\u4f9d\u777f\u8fea\u4e9a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,151,135)"
                        }
                    }
                },
                {
                    "name": "\u533a\u5757\u661f\u8fb0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,6,72)"
                        }
                    }
                },
                {
                    "name": "\u6e05\u9e64\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,136,78)"
                        }
                    }
                },
                {
                    "name": "\u878d\u6167\u91d1\u79d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,47,105)"
                        }
                    }
                },
                {
                    "name": "Mai\u5c0f\u9ea6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,43,139)"
                        }
                    }
                },
                {
                    "name": "\u8bfa\u535a\u533b\u7597",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,87,116)"
                        }
                    }
                },
                {
                    "name": "\u4f0a\u6fb3\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,140,55)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u5fc5\u9009\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,76,10)"
                        }
                    }
                },
                {
                    "name": "\u58f0\u901a\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,97,123)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u4e1c\u5e7f\u4fe1\u901a\u4fe1\u670d\u52a1\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,154,14)"
                        }
                    }
                },
                {
                    "name": "\u7ea2\u84ddCP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,98,46)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u8d62\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,3,86)"
                        }
                    }
                },
                {
                    "name": "\u6ef4\u6ef4\u4f18\u70b9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,35,2)"
                        }
                    }
                },
                {
                    "name": "\u535a\u4f9d\u7279",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,87,133)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u6773\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,147,52)"
                        }
                    }
                },
                {
                    "name": "\u6b4c\u707f\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,160,109)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u5730\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,93,111)"
                        }
                    }
                },
                {
                    "name": "\u521b\u5fc5\u627f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,67,111)"
                        }
                    }
                },
                {
                    "name": "LBE \u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,107,120)"
                        }
                    }
                },
                {
                    "name": "\u5b9d\u5c0a\u7535\u5546",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,1,103)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u79d1\u777f\u89c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,6,0)"
                        }
                    }
                },
                {
                    "name": "\u4eb2\u5bb6\u7f51\u7edc\u6280\u672f\uff08\u5317\u4eac\uff09\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,146,15)"
                        }
                    }
                },
                {
                    "name": "\u552f\u54c1\u4f1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,27,31)"
                        }
                    }
                },
                {
                    "name": "\u7231\u5b66\u4e60\u6559\u80b2\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,92,20)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u6d4e\u533b\u7597",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,31,156)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77\u541b\u9a6d\u4f01\u4e1a\u7ba1\u7406\u54a8\u8be2\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,109,86)"
                        }
                    }
                },
                {
                    "name": "\u535a\u5f66\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,29,134)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u64ad\u7535\u89c6\u7814\u7a76\u6240",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,148,20)"
                        }
                    }
                },
                {
                    "name": "KLOOK \u5ba2\u8def\u65c5\u884c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,66,71)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u4e16\u76f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,80,155)"
                        }
                    }
                },
                {
                    "name": "\u968f\u8eab\u542c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,119,4)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u5b8f\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,140,88)"
                        }
                    }
                },
                {
                    "name": "\u5357\u5a01\u8f6f\u4ef6\u80a1\u4efd\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,125,139)"
                        }
                    }
                },
                {
                    "name": "Camera360",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,39,1)"
                        }
                    }
                },
                {
                    "name": "\u6717\u65b0\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,30,76)"
                        }
                    }
                },
                {
                    "name": "\u7545\u884c\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,83,96)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u4e07\u7ef4\u76c8\u521b\u79d1\u6280\u53d1\u5c55\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,75,3)"
                        }
                    }
                },
                {
                    "name": "\u5373\u523b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,91,5)"
                        }
                    }
                },
                {
                    "name": "\u6708\u76db\u658b\u6295\u8d44\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,134,18)"
                        }
                    }
                },
                {
                    "name": "\u5782\u8863",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,146,84)"
                        }
                    }
                },
                {
                    "name": "\u84dd\u706f\u9c7c\u667a\u80fd\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,12,103)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u79d1\u95fb\u6b4c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,73,141)"
                        }
                    }
                },
                {
                    "name": "\u6beb\u672b\u667a\u884c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,61,11)"
                        }
                    }
                },
                {
                    "name": "\u5965\u7279\u7ef4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,131,87)"
                        }
                    }
                },
                {
                    "name": "\u683c\u521b\u4e1c\u667a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,31,35)"
                        }
                    }
                },
                {
                    "name": "\u9510\u4ed5\u65b9\u8fbe\u4eba\u529b\u8d44\u6e90",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,18,121)"
                        }
                    }
                },
                {
                    "name": "\u540d\u7af9\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,89,144)"
                        }
                    }
                },
                {
                    "name": "\u6253\u626e\u5bb6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,91,6)"
                        }
                    }
                },
                {
                    "name": "\u6d82\u9e26\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,10,151)"
                        }
                    }
                },
                {
                    "name": "\u4e16\u7eaa\u4f73\u7f18",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,8,90)"
                        }
                    }
                },
                {
                    "name": "\u8230\u76fe\u5b89\u68c0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,157,34)"
                        }
                    }
                },
                {
                    "name": "\u797a\u9cb8\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,5,20)"
                        }
                    }
                },
                {
                    "name": "\u521b\u5ba2\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,62,154)"
                        }
                    }
                },
                {
                    "name": "\u70ab\u751f\u6d3b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,113,103)"
                        }
                    }
                },
                {
                    "name": "\u9e4f\u5143\u5f81\u4fe1\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,89,55)"
                        }
                    }
                },
                {
                    "name": "\u5a31\u516c\u4e92\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,118,100)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u8863\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,72,144)"
                        }
                    }
                },
                {
                    "name": "\u571f\u756a\u85af\u730e\u5934",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,126,110)"
                        }
                    }
                },
                {
                    "name": "\u8bfa\u65b9\u7535\u5b50",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,151,20)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u5173\u6751\u6613\u521b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,86,60)"
                        }
                    }
                },
                {
                    "name": "\u5b8c\u7f8e\u4e16\u754c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,107,21)"
                        }
                    }
                },
                {
                    "name": "\u8def\u884c\u901a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,19,75)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u79d1\u5f18\u4e91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,88,103)"
                        }
                    }
                },
                {
                    "name": "\u638c\u4e0a\u5148\u673a-\u65fa\u5e97\u901aERP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,28,34)"
                        }
                    }
                },
                {
                    "name": "\u5916\u8111\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,22,17)"
                        }
                    }
                },
                {
                    "name": "\u4ebf\u8054\u7f51\u7edc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,131,96)"
                        }
                    }
                },
                {
                    "name": "\u897f\u5c71\u5c45\u6e38\u620f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,107,108)"
                        }
                    }
                },
                {
                    "name": "\u8054\u4f17\u91d1\u878d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,139,132)"
                        }
                    }
                },
                {
                    "name": "\u9752\u5c9b\u5e03\u9c81\u514b\u65af\u4e50\u5668\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,117,141)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5927\u701a\u4eba\u529b\u8d44\u6e90\u7ba1\u7406\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,43,107)"
                        }
                    }
                },
                {
                    "name": "\u5411\u65e5\u8475\u5988\u5988",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,22,155)"
                        }
                    }
                },
                {
                    "name": "\u53ee\u549a\u4e70\u83dc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,55,37)"
                        }
                    }
                },
                {
                    "name": "\u591a\u70b9\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,128,152)"
                        }
                    }
                },
                {
                    "name": "BaseBit AI \u7ffc\u65b9\u5065\u6570",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,64,96)"
                        }
                    }
                },
                {
                    "name": "\u53bb\u54ea\u513f\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,127,61)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u516b\u7ef4\u7814\u4fee\u5b66\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,141,108)"
                        }
                    }
                },
                {
                    "name": "\u5bfa\u5e93",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,131,30)"
                        }
                    }
                },
                {
                    "name": "\u55b5\u67da\u7f51\u7edc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,89,150)"
                        }
                    }
                },
                {
                    "name": "\u5c11\u5e74\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,44,62)"
                        }
                    }
                },
                {
                    "name": "OKAY\u667a\u6167\u6559\u80b2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,151,42)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u6cf0\u4ea7\u9669",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,79,123)"
                        }
                    }
                },
                {
                    "name": "\u597d\u597d\u4f4f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,21,77)"
                        }
                    }
                },
                {
                    "name": "\u534e\u783a\u667a\u884c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,6,72)"
                        }
                    }
                },
                {
                    "name": "Vyou\u5fae\u4f60",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,141,140)"
                        }
                    }
                },
                {
                    "name": "\u5229\u57fa\u4e07\u5546\u52a1\u4fe1\u606f\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,122,67)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u5b89\u6613",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,13,29)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u949e\u79d1\u4fe1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,83,26)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77\u5594\u8da3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,138,141)"
                        }
                    }
                },
                {
                    "name": "\u672a\u6765\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,79,25)"
                        }
                    }
                },
                {
                    "name": "\u5408\u5408\u4fe1\u606f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,92,94)"
                        }
                    }
                },
                {
                    "name": "\u4e07\u91cc\u76ee\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,123,122)"
                        }
                    }
                },
                {
                    "name": "\u533b\u667a\u5f71",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,125,77)"
                        }
                    }
                },
                {
                    "name": "\u667a\u795e\u4fe1\u606f\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,127,90)"
                        }
                    }
                },
                {
                    "name": "OSR",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,147,92)"
                        }
                    }
                },
                {
                    "name": "\u67d2\u96f6\u58f9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,141,42)"
                        }
                    }
                },
                {
                    "name": "\u5927\u97f6\u6295\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,121,111)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u91d1\u670d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,11,55)"
                        }
                    }
                },
                {
                    "name": "\u601d\u5f00\u8fbe\u8bed\u97f3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,13,2)"
                        }
                    }
                },
                {
                    "name": "\u53cb\u5854\u6e38\u620f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,127,65)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77\u6469\u8c61\u7f51\u7edc\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,153,146)"
                        }
                    }
                },
                {
                    "name": "\u9014\u5bb6\u6c11\u5bbf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,46,68)"
                        }
                    }
                },
                {
                    "name": "\u73de\u73c8\u4f17\u6052",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,151,46)"
                        }
                    }
                },
                {
                    "name": "\u725b\u7801\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,28,18)"
                        }
                    }
                },
                {
                    "name": "\u6c49\u738b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,101,71)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u5361\u7279\u52a0\u7279\u667a\u80fd\u79d1\u6280\u6709\u9650\u516c\u53f8\u5317\u4eac\u5206\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,20,83)"
                        }
                    }
                },
                {
                    "name": "\u745e\u8fb0\u660c\u9686",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,72,17)"
                        }
                    }
                },
                {
                    "name": "AutoX",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,128,159)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u6b65\u5728\u5bb6\u65e9\u6559",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,67,47)"
                        }
                    }
                },
                {
                    "name": "\u827e\u5fb7\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,139,32)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u667a\u7c73\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,133,59)"
                        }
                    }
                },
                {
                    "name": "\u53a6\u95e8\u79d1\u62d3\u901a\u8baf\u6280\u672f\u80a1\u4efd\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,61,6)"
                        }
                    }
                },
                {
                    "name": "\u9752\u5cb3\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,57,51)"
                        }
                    }
                },
                {
                    "name": "\u539f\u5b50\u673a\u5668\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,97,140)"
                        }
                    }
                },
                {
                    "name": "\u6b63\u4fdd\u8fdc\u7a0b\u6559\u80b2\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,64,52)"
                        }
                    }
                },
                {
                    "name": "\u6cf0\u5eb7\u5728\u7ebf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,82,112)"
                        }
                    }
                },
                {
                    "name": "\u5495\u549a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,35,102)"
                        }
                    }
                },
                {
                    "name": "\u94f6\u6cb3\u4fe1\u901a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,9,73)"
                        }
                    }
                },
                {
                    "name": "\u827e\u8fc8\u79d1\u65af\u5a92\u4f53\u79d1\u6280\uff08\u5317\u4eac\uff09\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,66,47)"
                        }
                    }
                },
                {
                    "name": "\u58a8\u5947\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,44,49)"
                        }
                    }
                },
                {
                    "name": "\u5b8f\u7131\u7f51\u7edc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,108,36)"
                        }
                    }
                },
                {
                    "name": "\u82f1\u5a01\u8bfa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,86,112)"
                        }
                    }
                },
                {
                    "name": "\u95ea\u5e03\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,144,57)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u7f8e\u63a7\u80a1\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,44,7)"
                        }
                    }
                },
                {
                    "name": "\u4e0d\u8a00\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,79,159)"
                        }
                    }
                },
                {
                    "name": "58\u5b66\u8f66-\u9a7e\u6821\u4e00\u70b9\u901a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,97,19)"
                        }
                    }
                },
                {
                    "name": "\u5341\u835f\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,44,50)"
                        }
                    }
                },
                {
                    "name": "\u4f9d\u77b3\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,62,51)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u53c2\u6570",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,155,153)"
                        }
                    }
                },
                {
                    "name": "\u6f6e\u6d41\u7f51\u7edc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,59,160)"
                        }
                    }
                },
                {
                    "name": "\u96ea\u6d6a\u6570\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,123,87)"
                        }
                    }
                },
                {
                    "name": "\u957f\u57ce\u6c7d\u8f66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,102,96)"
                        }
                    }
                },
                {
                    "name": "\u683c\u7f57\u592b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,20,156)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5c14\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,84,69)"
                        }
                    }
                },
                {
                    "name": "\u534e\u5764\u9053\u5a01",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,147,52)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u901a\u8f6f\u4ef6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,102,105)"
                        }
                    }
                },
                {
                    "name": "\u6cf0\u5eb7\u4fdd\u9669\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,113,151)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5723\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,68,112)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u4fe1\u521b\u65b0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,22,62)"
                        }
                    }
                },
                {
                    "name": "\u770b\u623f\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,47,95)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u4ee5\u8d24",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,137,55)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u540c\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,143,129)"
                        }
                    }
                },
                {
                    "name": "\u82cf\u5dde\u624d\u5ba2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,147,34)"
                        }
                    }
                },
                {
                    "name": "\u897f\u6e56\u5927\u5b66\u667a\u80fd\u4ea7\u4e1a\u7814\u7a76\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,128,140)"
                        }
                    }
                },
                {
                    "name": "\u6f8e\u601d\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,7,50)"
                        }
                    }
                },
                {
                    "name": "NIO\u851a\u6765",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,108,15)"
                        }
                    }
                },
                {
                    "name": "\u878d\u6613\u63a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,37,10)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u5065\u5eb7\u4fdd\u9669",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,125,43)"
                        }
                    }
                },
                {
                    "name": "\u70b9\u4f17\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,158,60)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u6444",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,57,76)"
                        }
                    }
                },
                {
                    "name": "\u6570\u777f\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,140,154)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u8c61\u4f18\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,97,70)"
                        }
                    }
                },
                {
                    "name": "\u8d1d\u53f6\u65af\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,113,87)"
                        }
                    }
                },
                {
                    "name": "Xeno Dynamics",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,3,64)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u4e07\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,58,18)"
                        }
                    }
                },
                {
                    "name": "\u8bc6\u56e0\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,29,49)"
                        }
                    }
                },
                {
                    "name": "\u53f8\u5357\u6570\u636e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,63,13)"
                        }
                    }
                },
                {
                    "name": "\u4f17\u5b89\u4fdd\u9669",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,70,40)"
                        }
                    }
                },
                {
                    "name": "\u822a\u7a7a\u5927\u90fd\u5e02\u7814\u7a76\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,54,106)"
                        }
                    }
                },
                {
                    "name": "\u8377\u798f\u4eba\u5de5\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,68,47)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u8bc1\u5238",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,117,126)"
                        }
                    }
                },
                {
                    "name": "\u84dd\u6df1\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,160,4)"
                        }
                    }
                },
                {
                    "name": "\u7231\u7acb\u5eb7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,100,11)"
                        }
                    }
                },
                {
                    "name": "\u76c8\u4f73\u4fe1\u8054",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,72,20)"
                        }
                    }
                },
                {
                    "name": "\u4eac\u4e1c\u5546\u57ce",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,3,0)"
                        }
                    }
                },
                {
                    "name": "\u67cf\u8fbe\u4eba\u529b\u8d44\u6e90\u987e\u95ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,69,106)"
                        }
                    }
                },
                {
                    "name": "\u9646\u6cfd\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,144,130)"
                        }
                    }
                },
                {
                    "name": "\u6a59\u5b50\u6570\u5b57\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,114,63)"
                        }
                    }
                },
                {
                    "name": "\u67cf\u7f8e\u8fea\u5eb7\u4e0a\u6d77",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,55,118)"
                        }
                    }
                },
                {
                    "name": "\u82cf\u82af\u7269\u8054",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,136,129)"
                        }
                    }
                },
                {
                    "name": "\u5bcc\u6e2f\u4e07\u5609",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,44,142)"
                        }
                    }
                },
                {
                    "name": "UMU",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,152,111)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u8ff9\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,68,1)"
                        }
                    }
                },
                {
                    "name": "\u661f\u9645\u5927\u9646",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,124,94)"
                        }
                    }
                },
                {
                    "name": "IntraMirror",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,64,14)"
                        }
                    }
                },
                {
                    "name": "\u73af\u7403\u8f66\u4eab",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,120,63)"
                        }
                    }
                },
                {
                    "name": "\u5a5a\u793c\u7eaa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,153,73)"
                        }
                    }
                },
                {
                    "name": "\u534e\u4e91\u4e2d\u76db",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,50,149)"
                        }
                    }
                },
                {
                    "name": "\u53f6\u6d6a\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,100,61)"
                        }
                    }
                },
                {
                    "name": "\u5047\u9762\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,10,61)"
                        }
                    }
                },
                {
                    "name": "\u8f6f\u725b\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,119,29)"
                        }
                    }
                },
                {
                    "name": "\u6155\u8bfe\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,115,144)"
                        }
                    }
                },
                {
                    "name": "\u7c89\u8c61\u751f\u6d3b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,117,54)"
                        }
                    }
                },
                {
                    "name": "\u601d\u7075\u673a\u5668\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,32,99)"
                        }
                    }
                },
                {
                    "name": "\u6bcf\u65e5\u4f18\u9c9c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,1,25)"
                        }
                    }
                },
                {
                    "name": "\u660e\u6e90\u4e91\u5ba2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,67,124)"
                        }
                    }
                },
                {
                    "name": "\u540c\u82b1\u987a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,4,143)"
                        }
                    }
                },
                {
                    "name": "\u8da3\u9014\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,87,127)"
                        }
                    }
                },
                {
                    "name": "\u5353\u817e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,127,0)"
                        }
                    }
                },
                {
                    "name": "\u711c\u8000\u7f51\u7edc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,138,60)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6e05\u91d1\u79d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,67,102)"
                        }
                    }
                },
                {
                    "name": "\u89e6\u6f2b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,9,118)"
                        }
                    }
                },
                {
                    "name": "\u4f20\u97f3\u63a7\u80a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,137,131)"
                        }
                    }
                },
                {
                    "name": "AfterShip\u7231\u5ba2\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,71,84)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u839e\u7f8e\u5b9c\u4f73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,84,10)"
                        }
                    }
                },
                {
                    "name": "\u8d22\u76c8\u901a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,148,136)"
                        }
                    }
                },
                {
                    "name": "WeSure\u5fae\u4fdd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,9,76)"
                        }
                    }
                },
                {
                    "name": "\u5c1a\u4e91\u4f9d\u56fe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,48,132)"
                        }
                    }
                },
                {
                    "name": "\u7384\u6b66\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,25,45)"
                        }
                    }
                },
                {
                    "name": "\u54aa\u5495",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,18,28)"
                        }
                    }
                },
                {
                    "name": "\u6cf0\u5eb7\u4eba\u5bff",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,31,106)"
                        }
                    }
                },
                {
                    "name": "\u5343\u5bfb\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,71,144)"
                        }
                    }
                },
                {
                    "name": "\u5988\u5988\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,7,120)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u770b\u80a1\u4efd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,125,27)"
                        }
                    }
                },
                {
                    "name": "FREE BRIO",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,54,160)"
                        }
                    }
                },
                {
                    "name": "e\u7b7e\u5b9d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,91,127)"
                        }
                    }
                },
                {
                    "name": "Riley Cillian\u83b1\u7199\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,51,37)"
                        }
                    }
                },
                {
                    "name": "\u8054\u901a\u65f6\u79d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,78,27)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u8109",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,11,55)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u6210",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,156,35)"
                        }
                    }
                },
                {
                    "name": "\u6587\u76db\u8d44\u4ea7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,135,95)"
                        }
                    }
                },
                {
                    "name": "\u9636\u5f62",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,112,63)"
                        }
                    }
                },
                {
                    "name": "\u533b\u767e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,44,20)"
                        }
                    }
                },
                {
                    "name": "\u8ffd\u89c5\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,106,54)"
                        }
                    }
                },
                {
                    "name": "\u82f1\u96c4\u4e92\u5a31",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,143,50)"
                        }
                    }
                },
                {
                    "name": "\u6c47\u4fe1\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,80,89)"
                        }
                    }
                },
                {
                    "name": "\u897f\u5b89\u7acb\u8fb0\u8fdc\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,158,59)"
                        }
                    }
                },
                {
                    "name": "\u534e\u4fa8\u57ce\u6587\u65c5\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,28,41)"
                        }
                    }
                },
                {
                    "name": "\u638c\u95e8\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,65,81)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u5f99\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,142,143)"
                        }
                    }
                },
                {
                    "name": "\u660e\u4e4b\u6570\u636e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,93,104)"
                        }
                    }
                },
                {
                    "name": "\u8001\u864e\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,70,3)"
                        }
                    }
                },
                {
                    "name": "\u6d3e\u8fe9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,109,87)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u5cfb\u4fe1\u606f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,76,44)"
                        }
                    }
                },
                {
                    "name": "\u4e16\u7eaa\u5fb7\u8fb0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,102,23)"
                        }
                    }
                },
                {
                    "name": "GALASPORTS",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,104,95)"
                        }
                    }
                },
                {
                    "name": "\u76ef\u76ef\u62cd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,116,127)"
                        }
                    }
                },
                {
                    "name": "\u6c49\u71b5\u901a\u4fe1\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,9,146)"
                        }
                    }
                },
                {
                    "name": "\u8c6a\u732a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,140,22)"
                        }
                    }
                },
                {
                    "name": "\u5353\u4fe1\u4f01\u4e1a\u54a8\u8be2\u670d\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,104,32)"
                        }
                    }
                },
                {
                    "name": "\u987a\u4e30\u56fd\u9645",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,112,34)"
                        }
                    }
                },
                {
                    "name": "\u6cdb\u534e\u91d1\u878d\u63a7\u80a1\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,95,160)"
                        }
                    }
                },
                {
                    "name": "deepcam",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,74,45)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u679c\u6bd4\u7279",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,157,51)"
                        }
                    }
                },
                {
                    "name": "\u6a59\u8272\u4e91\u4e92\u8054\u7f51\u8bbe\u8ba1\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,28,120)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u60f3\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,14,66)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u534e\u7814\u7a76\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,14,119)"
                        }
                    }
                },
                {
                    "name": "\u65f6\u8da3social-touch",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,144,109)"
                        }
                    }
                },
                {
                    "name": "DataCastle",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,158,87)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u6e7e\u521b\u65b0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,87,137)"
                        }
                    }
                },
                {
                    "name": "\u8d5b\u5427\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,31,2)"
                        }
                    }
                },
                {
                    "name": "\u6c49\u4eea\u5b57\u5e93",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,105,145)"
                        }
                    }
                },
                {
                    "name": "\u591a\u725b\u4f20\u5a92",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,13,27)"
                        }
                    }
                },
                {
                    "name": "\u987a\u5b89\u4f1f\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,37,27)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u7535\u535a\u4e9a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,139,16)"
                        }
                    }
                },
                {
                    "name": "\u6613\u79d1\u5947\u901a\u4fe1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,121,67)"
                        }
                    }
                },
                {
                    "name": "\u5609\u4e3a\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,0,98)"
                        }
                    }
                },
                {
                    "name": "\u62ff\u706b\u97f3\u4e50",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,36,76)"
                        }
                    }
                },
                {
                    "name": "\u623f\u8f66\u5b9d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,97,71)"
                        }
                    }
                },
                {
                    "name": "\u623f\u5929\u4e0b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,50,108)"
                        }
                    }
                },
                {
                    "name": "\u8eba\u5e73\u8bbe\u8ba1\u5bb6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,85,106)"
                        }
                    }
                },
                {
                    "name": "\u524d\u6d77\u4e91\u4e1c\u5bb6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,37,116)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u5343\u4e91\u5929\u4e0b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,137,25)"
                        }
                    }
                },
                {
                    "name": "\u60e0\u6bcf\u4e91\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,74,42)"
                        }
                    }
                },
                {
                    "name": "\u8fc8\u5916\u8fea",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,146,23)"
                        }
                    }
                },
                {
                    "name": "\u534e\u98ce\u7231\u79d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,99,146)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u901a\u5feb\u9012",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,94,154)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u9690\u865a\u7b49\u8d24\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,71,121)"
                        }
                    }
                },
                {
                    "name": "\u5370\u8c61\u7b14\u8bb0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,73,22)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u5dde\u5e7b\u5883\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,132,21)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u5341\u516d\u8fdb\u5236\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,78,14)"
                        }
                    }
                },
                {
                    "name": "\u5609\u5b9e\u57fa\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,67,140)"
                        }
                    }
                },
                {
                    "name": "\u62d3\u4fdd\u8f6f\u4ef6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,19,63)"
                        }
                    }
                },
                {
                    "name": "\u6c90\u77b3\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,48,66)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u777f\u533b\u7597",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,32,64)"
                        }
                    }
                },
                {
                    "name": "\u5fc3\u5a31\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,155,12)"
                        }
                    }
                },
                {
                    "name": "\u963f\u5361\u7d22\u5916\u6559\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,68,44)"
                        }
                    }
                },
                {
                    "name": "\u7ffc\u8bfe\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,19,108)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u83dc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,153,144)"
                        }
                    }
                },
                {
                    "name": "\u51ef\u8bda\u5546\u52a1\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,19,11)"
                        }
                    }
                },
                {
                    "name": "\u4e07\u5174\u79d1\u6280\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,12,153)"
                        }
                    }
                },
                {
                    "name": "\u6c38\u8f89\u4e91\u521b\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,24,112)"
                        }
                    }
                },
                {
                    "name": "\u534e\u7b56",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,41,8)"
                        }
                    }
                },
                {
                    "name": "\u638c\u9605",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,95,1)"
                        }
                    }
                },
                {
                    "name": "\u6930\u5b50\u4f20\u5a92",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,15,121)"
                        }
                    }
                },
                {
                    "name": "\u5730\u576a\u7ebf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,113,77)"
                        }
                    }
                },
                {
                    "name": "\u9541\u4fe1\u5065\u5eb7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,126,79)"
                        }
                    }
                },
                {
                    "name": "\u6676\u786e\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,124,98)"
                        }
                    }
                },
                {
                    "name": "\u74e6\u529b\u5728\u7ebf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,105,68)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u91cf\u8d28\u5b50",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,83,151)"
                        }
                    }
                },
                {
                    "name": "\u878d360",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,22,98)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5bb6\u5065\u6295",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,16,148)"
                        }
                    }
                },
                {
                    "name": "DMAI\u667a\u80fd\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,124,143)"
                        }
                    }
                },
                {
                    "name": "\u96f7\u5ea6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,128,18)"
                        }
                    }
                },
                {
                    "name": "\u98de\u5e38\u51c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,145,44)"
                        }
                    }
                },
                {
                    "name": "\u542c\u4e91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,139,119)"
                        }
                    }
                },
                {
                    "name": "\u4e5d\u53f7\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,34,87)"
                        }
                    }
                },
                {
                    "name": "\u7c73\u96c5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,156,64)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u56fd\u7535\u4fe1\u589e\u503c\u4e1a\u52a1\u8fd0\u8425\u4e2d\u5fc3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,136,40)"
                        }
                    }
                },
                {
                    "name": "\u9cb8\u6984\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,74,23)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u7280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,86,25)"
                        }
                    }
                },
                {
                    "name": "\u5929\u6cfd\u667a\u4e91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,67,70)"
                        }
                    }
                },
                {
                    "name": "\u9b54\u65b9\u706b\u79cd\u4f01\u4e1a\u7ba1\u7406\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,17,51)"
                        }
                    }
                },
                {
                    "name": "\u521b\u4e16\u4e91\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,91,37)"
                        }
                    }
                },
                {
                    "name": "\u6b66\u6c49\u653f\u901a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,5,54)"
                        }
                    }
                },
                {
                    "name": "\u798f\u7c73\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,137,36)"
                        }
                    }
                },
                {
                    "name": "\u6d66\u53d1\u4fe1\u7528\u5361",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,100,58)"
                        }
                    }
                },
                {
                    "name": "\u5927\u7bb4\uff08\u676d\u5dde\uff09\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,144,79)"
                        }
                    }
                },
                {
                    "name": "\u5927\u9053\u4e4b\u884c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,120,141)"
                        }
                    }
                },
                {
                    "name": "\u827e\u96f7\u7279\u54a8\u8be2\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,52,109)"
                        }
                    }
                },
                {
                    "name": "\u9876\u70b9\u8f6f\u4ef6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,129,128)"
                        }
                    }
                },
                {
                    "name": "\u51b0\u6cb3\u4e91\u5b58\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,47,130)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u8d1d\u864e\u7269\u8054\u6280\u672f\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,6,105)"
                        }
                    }
                },
                {
                    "name": "\u79be\u6728",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,38,98)"
                        }
                    }
                },
                {
                    "name": "\u4ee5\u89c1\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,35,145)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u6781\u777f\u79d1\u6280\u6709\u9650\u8d23\u4efb\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,81,40)"
                        }
                    }
                },
                {
                    "name": "\u6b66\u6c49\u675e\u6893\u4f01\u4e1a\u7ba1\u7406\u54a8\u8be2\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,141,80)"
                        }
                    }
                },
                {
                    "name": "\u5915\u5915\u65f6\u4ee3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,26,48)"
                        }
                    }
                },
                {
                    "name": "\u9884\u7b56\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,15,142)"
                        }
                    }
                },
                {
                    "name": "\u79fb\u5361",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,79,13)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77\u91d1\u5927\u5e08\u7f51\u7edc\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,136,47)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u79df\u8d41",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,101,135)"
                        }
                    }
                },
                {
                    "name": "\u745b\u592a\u83b1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,84,45)"
                        }
                    }
                },
                {
                    "name": "\u8054\u5408\u4f18\u521b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,155,31)"
                        }
                    }
                },
                {
                    "name": "\u65b9\u76f4\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,113,32)"
                        }
                    }
                },
                {
                    "name": "\u83ab\u6bd4\u55e8\u5ba2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,35,127)"
                        }
                    }
                },
                {
                    "name": "\u667a\u9f7f\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,85,22)"
                        }
                    }
                },
                {
                    "name": "Micagent",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,38,78)"
                        }
                    }
                },
                {
                    "name": "\u6210\u90fd\u8d5b\u57fa\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,133,154)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u7535\u91d1\u4fe1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,110,21)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u7ef4\u901a\u4fe1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,142,133)"
                        }
                    }
                },
                {
                    "name": "\u5929\u5f18\u57fa\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,71,2)"
                        }
                    }
                },
                {
                    "name": "\u667a\u7406\u7269\u8054",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,30,95)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u745e\u601d\u62d3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,106,8)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u9a70\u533b\u7597",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,58,37)"
                        }
                    }
                },
                {
                    "name": "\u54c8\u5de5\u9a71\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,41,45)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u987e\u4eba\u529b\u8d44\u6e90",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,105,88)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u4e1c\u8dc3\u6609\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,151,6)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u7c73\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,62,144)"
                        }
                    }
                },
                {
                    "name": "\u5a01\u661f\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,25,37)"
                        }
                    }
                },
                {
                    "name": "\u76df\u6d6a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,28,43)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u4e03\u4e92\u5a31",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,69,63)"
                        }
                    }
                },
                {
                    "name": "\u7280\u8bed\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,88,47)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u5bb6\u91d1\u878d\u79d1\u6280\u6d4b\u8bc4\u4e2d\u5fc3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,20,157)"
                        }
                    }
                },
                {
                    "name": "\u5c55\u98de\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,80,18)"
                        }
                    }
                },
                {
                    "name": "\u94a2\u94c1\u4fa0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,124,61)"
                        }
                    }
                },
                {
                    "name": "\u805a\u5747\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,17,48)"
                        }
                    }
                },
                {
                    "name": "\u6597\u9c7c\u76f4\u64ad",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,11,128)"
                        }
                    }
                },
                {
                    "name": "\u4f20\u6613",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,33,149)"
                        }
                    }
                },
                {
                    "name": "\u4f4d\u52a8\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,153,17)"
                        }
                    }
                },
                {
                    "name": "\u6570\u7f8e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,82,14)"
                        }
                    }
                },
                {
                    "name": "\u8054\u8fd0\u77e5\u6167\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,41,25)"
                        }
                    }
                },
                {
                    "name": "\u7231\u7279\u66fc\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,155,23)"
                        }
                    }
                },
                {
                    "name": "\u76df\u5927\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,71,62)"
                        }
                    }
                },
                {
                    "name": "RealAI",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,6,121)"
                        }
                    }
                },
                {
                    "name": "\u9e25\u601d\u90a6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,109,102)"
                        }
                    }
                },
                {
                    "name": "\u9752\u677e\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,105,21)"
                        }
                    }
                },
                {
                    "name": "\u5982\u797a\u51fa\u884c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,8,153)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u79ef\u4e92\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,89,124)"
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
                "\u5b57\u8282\u8df3\u52a8",
                "\u4eac\u4e1c\u96c6\u56e2",
                "\u6ef4\u6ef4",
                "OPPO",
                "\u7231\u5947\u827a",
                "\u5feb\u624b",
                "\u7f51\u6613",
                "\u4eac\u4e1c\u7269\u6d41",
                "\u777f\u8d44\u8fbe"
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
        chart_224b0438aef04db7ae682fdf8ef01be7.setOption(option_224b0438aef04db7ae682fdf8ef01be7);
    </script>
                <div id="de685747bdd64cc1805ae898640e55f1" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_de685747bdd64cc1805ae898640e55f1 = echarts.init(
            document.getElementById('de685747bdd64cc1805ae898640e55f1'), 'white', {renderer: 'canvas'});
        var option_de685747bdd64cc1805ae898640e55f1 = {
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
                601,
                281,
                250,
                166,
                82,
                47,
                30,
                16,
                12,
                12
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
                    "value": 601,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,28,152)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77",
                    "value": 281,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,11,159)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733",
                    "value": 250,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,16,37)"
                        }
                    }
                },
                {
                    "name": "\u676d\u5dde",
                    "value": 166,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,152,21)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u5dde",
                    "value": 82,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,119,30)"
                        }
                    }
                },
                {
                    "name": "\u6210\u90fd",
                    "value": 47,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,110,71)"
                        }
                    }
                },
                {
                    "name": "\u6b66\u6c49",
                    "value": 30,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,128,54)"
                        }
                    }
                },
                {
                    "name": "\u82cf\u5dde",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,107,32)"
                        }
                    }
                },
                {
                    "name": "\u897f\u5b89",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,125,67)"
                        }
                    }
                },
                {
                    "name": "\u5357\u4eac",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,2,144)"
                        }
                    }
                },
                {
                    "name": "\u4f5b\u5c71",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,126,109)"
                        }
                    }
                },
                {
                    "name": "\u53a6\u95e8",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,64,5)"
                        }
                    }
                },
                {
                    "name": "\u91cd\u5e86",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,93,102)"
                        }
                    }
                },
                {
                    "name": "\u5408\u80a5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,107,53)"
                        }
                    }
                },
                {
                    "name": "\u957f\u6c99",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,83,112)"
                        }
                    }
                },
                {
                    "name": "\u90d1\u5dde",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,113,116)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u9521",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,12,107)"
                        }
                    }
                },
                {
                    "name": "\u9752\u5c9b",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,20,88)"
                        }
                    }
                },
                {
                    "name": "\u73e0\u6d77",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,135,144)"
                        }
                    }
                },
                {
                    "name": "\u6d4e\u5357",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,71,126)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5dde",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,0,9)"
                        }
                    }
                },
                {
                    "name": "\u9f50\u9f50\u54c8\u5c14",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,28,89)"
                        }
                    }
                },
                {
                    "name": "\u5609\u5174",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,113,76)"
                        }
                    }
                },
                {
                    "name": "\u60e0\u5dde",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,10,52)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u839e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,98,151)"
                        }
                    }
                },
                {
                    "name": "\u5927\u8fde",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,18,84)"
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
        chart_de685747bdd64cc1805ae898640e55f1.setOption(option_de685747bdd64cc1805ae898640e55f1);
    </script>
                <div id="20fe3e072b1a4a4485a6b7bc44fe77fd" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_20fe3e072b1a4a4485a6b7bc44fe77fd = echarts.init(
            document.getElementById('20fe3e072b1a4a4485a6b7bc44fe77fd'), 'white', {renderer: 'canvas'});
        var option_20fe3e072b1a4a4485a6b7bc44fe77fd = {
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
                    "value": 601,
                    "name": "\u5317\u4eac"
                },
                {
                    "value": 281,
                    "name": "\u4e0a\u6d77"
                },
                {
                    "value": 250,
                    "name": "\u6df1\u5733"
                },
                {
                    "value": 166,
                    "name": "\u676d\u5dde"
                },
                {
                    "value": 82,
                    "name": "\u5e7f\u5dde"
                },
                {
                    "value": 47,
                    "name": "\u6210\u90fd"
                },
                {
                    "value": 30,
                    "name": "\u6b66\u6c49"
                },
                {
                    "value": 16,
                    "name": "\u82cf\u5dde"
                },
                {
                    "value": 12,
                    "name": "\u897f\u5b89"
                },
                {
                    "value": 12,
                    "name": "\u5357\u4eac"
                },
                {
                    "value": 11,
                    "name": "\u4f5b\u5c71"
                },
                {
                    "value": 6,
                    "name": "\u53a6\u95e8"
                },
                {
                    "value": 6,
                    "name": "\u91cd\u5e86"
                },
                {
                    "value": 4,
                    "name": "\u5408\u80a5"
                },
                {
                    "value": 4,
                    "name": "\u957f\u6c99"
                },
                {
                    "value": 3,
                    "name": "\u90d1\u5dde"
                },
                {
                    "value": 3,
                    "name": "\u65e0\u9521"
                },
                {
                    "value": 3,
                    "name": "\u9752\u5c9b"
                },
                {
                    "value": 3,
                    "name": "\u73e0\u6d77"
                },
                {
                    "value": 3,
                    "name": "\u6d4e\u5357"
                },
                {
                    "value": 2,
                    "name": "\u798f\u5dde"
                },
                {
                    "value": 1,
                    "name": "\u9f50\u9f50\u54c8\u5c14"
                },
                {
                    "value": 1,
                    "name": "\u5609\u5174"
                },
                {
                    "value": 1,
                    "name": "\u60e0\u5dde"
                },
                {
                    "value": 1,
                    "name": "\u4e1c\u839e"
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
        chart_20fe3e072b1a4a4485a6b7bc44fe77fd.setOption(option_20fe3e072b1a4a4485a6b7bc44fe77fd);
    </script>
                <div id="dde64eff7d8642a397022f5be788a6cb" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_dde64eff7d8642a397022f5be788a6cb = echarts.init(
            document.getElementById('dde64eff7d8642a397022f5be788a6cb'), 'white', {renderer: 'canvas'});
            
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
    
        var option_dde64eff7d8642a397022f5be788a6cb = {
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
                        601
                    ]
                },
                {
                    "name": "\u4e0a\u6d77",
                    "value": [
                        121.473701,
                        31.230416,
                        281
                    ]
                },
                {
                    "name": "\u6df1\u5733",
                    "value": [
                        114.07,
                        22.62,
                        250
                    ]
                },
                {
                    "name": "\u676d\u5dde",
                    "value": [
                        120.19,
                        30.26,
                        166
                    ]
                },
                {
                    "name": "\u5e7f\u5dde",
                    "value": [
                        113.23,
                        23.16,
                        82
                    ]
                },
                {
                    "name": "\u6210\u90fd",
                    "value": [
                        104.06,
                        30.67,
                        47
                    ]
                },
                {
                    "name": "\u6b66\u6c49",
                    "value": [
                        114.31,
                        30.52,
                        30
                    ]
                },
                {
                    "name": "\u82cf\u5dde",
                    "value": [
                        120.62,
                        31.32,
                        16
                    ]
                },
                {
                    "name": "\u897f\u5b89",
                    "value": [
                        108.95,
                        34.27,
                        12
                    ]
                },
                {
                    "name": "\u5357\u4eac",
                    "value": [
                        118.78,
                        32.04,
                        12
                    ]
                },
                {
                    "name": "\u4f5b\u5c71",
                    "value": [
                        113.11,
                        23.05,
                        11
                    ]
                },
                {
                    "name": "\u53a6\u95e8",
                    "value": [
                        118.1,
                        24.46,
                        6
                    ]
                },
                {
                    "name": "\u91cd\u5e86",
                    "value": [
                        106.551556,
                        29.563009,
                        6
                    ]
                },
                {
                    "name": "\u5408\u80a5",
                    "value": [
                        117.27,
                        31.86,
                        4
                    ]
                },
                {
                    "name": "\u957f\u6c99",
                    "value": [
                        113,
                        28.21,
                        4
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
                    "name": "\u65e0\u9521",
                    "value": [
                        120.29,
                        31.59,
                        3
                    ]
                },
                {
                    "name": "\u9752\u5c9b",
                    "value": [
                        120.33,
                        36.07,
                        3
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
                    "name": "\u6d4e\u5357",
                    "value": [
                        117,
                        36.65,
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
                    "name": "\u9f50\u9f50\u54c8\u5c14",
                    "value": [
                        123.97,
                        47.33,
                        1
                    ]
                },
                {
                    "name": "\u5609\u5174",
                    "value": [
                        120.76,
                        30.77,
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
                    "name": "\u4e1c\u839e",
                    "value": [
                        113.75,
                        23.04,
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
        chart_dde64eff7d8642a397022f5be788a6cb.setOption(option_dde64eff7d8642a397022f5be788a6cb);
    </script>
                <div id="666d2ead2b0a478ab234ac83c49d0f26" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_666d2ead2b0a478ab234ac83c49d0f26 = echarts.init(
            document.getElementById('666d2ead2b0a478ab234ac83c49d0f26'), 'white', {renderer: 'canvas'});
        var option_666d2ead2b0a478ab234ac83c49d0f26 = {
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
                166,
                118,
                98,
                41,
                39,
                38,
                33,
                30,
                29,
                28
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
                    "value": 166,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,89,84)"
                        }
                    }
                },
                {
                    "name": "\u671d\u9633\u533a",
                    "value": 118,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,77,75)"
                        }
                    }
                },
                {
                    "name": "\u5357\u5c71\u533a",
                    "value": 98,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,67,84)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u6280\u56ed",
                    "value": 41,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,33,63)"
                        }
                    }
                },
                {
                    "name": "\u4f59\u676d\u533a",
                    "value": 39,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,29,64)"
                        }
                    }
                },
                {
                    "name": "\u6d66\u4e1c\u65b0\u2026",
                    "value": 38,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,30,141)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u5173\u6751",
                    "value": 33,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,75,109)"
                        }
                    }
                },
                {
                    "name": "\u5f90\u6c47\u533a",
                    "value": 30,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,111,115)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u65b0\u533a",
                    "value": 29,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,125,124)"
                        }
                    }
                },
                {
                    "name": "\u5f20\u6c5f",
                    "value": 28,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,131,146)"
                        }
                    }
                },
                {
                    "name": "\u897f\u5317\u65fa",
                    "value": 27,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,50,117)"
                        }
                    }
                },
                {
                    "name": "\u5b9d\u5b89\u533a",
                    "value": 26,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,63,127)"
                        }
                    }
                },
                {
                    "name": "\u798f\u7530\u533a",
                    "value": 25,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,87,5)"
                        }
                    }
                },
                {
                    "name": "\u897f\u6e56\u533a",
                    "value": 25,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,99,63)"
                        }
                    }
                },
                {
                    "name": "\u671b\u4eac",
                    "value": 25,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,26,116)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9053\u53e3",
                    "value": 23,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,114,116)"
                        }
                    }
                },
                {
                    "name": "\u957f\u5b81\u533a",
                    "value": 20,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,92,132)"
                        }
                    }
                },
                {
                    "name": "\u897f\u6eaa",
                    "value": 20,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,65,11)"
                        }
                    }
                },
                {
                    "name": "\u95f5\u884c\u533a",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,71,24)"
                        }
                    }
                },
                {
                    "name": "\u6ee8\u6c5f\u533a",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,40,157)"
                        }
                    }
                },
                {
                    "name": "\u901a\u5dde\u533a",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,126,140)"
                        }
                    }
                },
                {
                    "name": "\u5929\u6cb3\u533a",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,90,13)"
                        }
                    }
                },
                {
                    "name": "\u897f\u4e8c\u65d7",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,30,3)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u6e56\u65b0\u2026",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,103,10)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5174\u533a",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,55,107)"
                        }
                    }
                },
                {
                    "name": "\u5927\u51b2",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,22,0)"
                        }
                    }
                },
                {
                    "name": "\u9759\u5b89\u533a",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,74,1)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u73e0\u533a",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,21,13)"
                        }
                    }
                },
                {
                    "name": "\u756a\u79ba\u533a",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,142,15)"
                        }
                    }
                },
                {
                    "name": "\u6b66\u4faf\u533a",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,6,127)"
                        }
                    }
                },
                {
                    "name": "\u6768\u6d66\u533a",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,85,130)"
                        }
                    }
                },
                {
                    "name": "\u8679\u6885\u8def",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,127,109)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u56ed\u2026",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,30,49)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u9662\u8def",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,146,88)"
                        }
                    }
                },
                {
                    "name": "\u987a\u5fb7\u533a",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,29,58)"
                        }
                    }
                },
                {
                    "name": "\u62f1\u5885\u533a",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,94,29)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u6e7e",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,49,146)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5730",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,120,141)"
                        }
                    }
                },
                {
                    "name": "\u9f99\u534e",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,32,0)"
                        }
                    }
                },
                {
                    "name": "\u8679\u53e3\u533a",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,19,111)"
                        }
                    }
                },
                {
                    "name": "\u897f\u5174",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,17,51)"
                        }
                    }
                },
                {
                    "name": "\u9ec4\u6d66\u533a",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,113,16)"
                        }
                    }
                },
                {
                    "name": "\u6d2a\u5c71\u533a",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,139,2)"
                        }
                    }
                },
                {
                    "name": "\u96c1\u5854\u533a",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,126,65)"
                        }
                    }
                },
                {
                    "name": "\u5f90\u5bb6\u6c47",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,76,159)"
                        }
                    }
                },
                {
                    "name": "\u5317\u65b0\u6cfe",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,112,4)"
                        }
                    }
                },
                {
                    "name": "\u4ea6\u5e84",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,60,139)"
                        }
                    }
                },
                {
                    "name": "\u4e9a\u8fd0\u6751",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,155,121)"
                        }
                    }
                },
                {
                    "name": "\u957f\u6cb3",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,53,42)"
                        }
                    }
                },
                {
                    "name": "\u897f\u4e09\u65d7",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,92,39)"
                        }
                    }
                },
                {
                    "name": "\u677e\u6c5f\u533a",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,50,30)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u5c71\u516c\u2026",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,57,63)"
                        }
                    }
                },
                {
                    "name": "\u4ed3\u524d",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,76,115)"
                        }
                    }
                },
                {
                    "name": "\u9152\u4ed9\u6865",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,123,35)"
                        }
                    }
                },
                {
                    "name": "\u96e8\u82b1\u53f0\u2026",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,131,116)"
                        }
                    }
                },
                {
                    "name": "\u77f3\u666f\u5c71\u2026",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,125,17)"
                        }
                    }
                },
                {
                    "name": "\u6587\u4e09\u8def",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,145,64)"
                        }
                    }
                },
                {
                    "name": "\u9752\u6d66\u533a",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,155,36)"
                        }
                    }
                },
                {
                    "name": "\u897f\u6e56",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,160,135)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u57ce\u533a",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,156,31)"
                        }
                    }
                },
                {
                    "name": "\u6765\u5e7f\u8425",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,149,153)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u6625\u8def",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,6,60)"
                        }
                    }
                },
                {
                    "name": "\u56de\u9f99\u89c2",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,85,50)"
                        }
                    }
                },
                {
                    "name": "\u601d\u660e\u533a",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,141,114)"
                        }
                    }
                },
                {
                    "name": "\u9f99\u534e\u65b0\u2026",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,93,129)"
                        }
                    }
                },
                {
                    "name": "\u660c\u5e73\u533a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,122,34)"
                        }
                    }
                },
                {
                    "name": "\u751c\u6c34\u56ed",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,6,135)"
                        }
                    }
                },
                {
                    "name": "\u56db\u60e0",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,47,65)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u6e2f",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,3,50)"
                        }
                    }
                },
                {
                    "name": "\u897f\u4e3d",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,120,7)"
                        }
                    }
                },
                {
                    "name": "\u9547\u5b81\u8def",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,20,11)"
                        }
                    }
                },
                {
                    "name": "\u9ec4\u57d4\u533a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,158,143)"
                        }
                    }
                },
                {
                    "name": "\u548c\u5e73\u91cc",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,137,10)"
                        }
                    }
                },
                {
                    "name": "\u897f\u57ce\u533a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,55,35)"
                        }
                    }
                },
                {
                    "name": "\u8d8a\u79c0\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,122,122)"
                        }
                    }
                },
                {
                    "name": "\u71d5\u838e",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,104,153)"
                        }
                    }
                },
                {
                    "name": "\u8700\u5c71\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,63,80)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u53f0\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,151,62)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5c71\u5b50",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,94,158)"
                        }
                    }
                },
                {
                    "name": "\u6e1d\u5317\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,10,95)"
                        }
                    }
                },
                {
                    "name": "\u897f\u76f4\u95e8",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,31,79)"
                        }
                    }
                },
                {
                    "name": "\u5742\u7530",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,91,110)"
                        }
                    }
                },
                {
                    "name": "\u9999\u6d32\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,109,29)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u65b0\u6280\u2026",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,65,55)"
                        }
                    }
                },
                {
                    "name": "\u5b98\u6d32",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,0,155)"
                        }
                    }
                },
                {
                    "name": "\u671d\u5916",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,121,26)"
                        }
                    }
                },
                {
                    "name": "\u897f\u4e61",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,49,53)"
                        }
                    }
                },
                {
                    "name": "\u5efa\u5916\u5927\u2026",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,37,109)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u798f\u5e84",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,83,156)"
                        }
                    }
                },
                {
                    "name": "\u7acb\u6c34\u6865",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,58,9)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u58a9",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,32,112)"
                        }
                    }
                },
                {
                    "name": "\u5927\u671b\u8def",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,63,113)"
                        }
                    }
                },
                {
                    "name": "\u4e0b\u57ce\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,36,19)"
                        }
                    }
                },
                {
                    "name": "\u666e\u9640\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,55,129)"
                        }
                    }
                },
                {
                    "name": "\u73e0\u6c5f\u65b0\u2026",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,71,80)"
                        }
                    }
                },
                {
                    "name": "\u5357\u6cb9",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,65,101)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u89d2\u573a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,41,136)"
                        }
                    }
                },
                {
                    "name": "\u7f57\u6e56\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,27,117)"
                        }
                    }
                },
                {
                    "name": "\u68e0\u4e0b",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,86,19)"
                        }
                    }
                },
                {
                    "name": "\u5317\u5916\u6ee9",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,132,0)"
                        }
                    }
                },
                {
                    "name": "\u957f\u5f81",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,18,97)"
                        }
                    }
                },
                {
                    "name": "\u5ef6\u5409",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,159,33)"
                        }
                    }
                },
                {
                    "name": "\u94b1\u5858\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,14,92)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7891\u5e97",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,83,121)"
                        }
                    }
                },
                {
                    "name": "\u5cb3\u9e93\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,1,78)"
                        }
                    }
                },
                {
                    "name": "\u671d\u9633\u95e8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,74,66)"
                        }
                    }
                },
                {
                    "name": "\u7fe0\u82d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,151,117)"
                        }
                    }
                },
                {
                    "name": "\u524d\u6d77",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,124,150)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u8d1e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,135,106)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u4ead",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,51,30)"
                        }
                    }
                },
                {
                    "name": "\u897f\u82d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,39,130)"
                        }
                    }
                },
                {
                    "name": "\u9526\u6c5f\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,122,72)"
                        }
                    }
                },
                {
                    "name": "\u5317\u82d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,18,36)"
                        }
                    }
                },
                {
                    "name": "\u5173\u5c71",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,117,13)"
                        }
                    }
                },
                {
                    "name": "\u6253\u6d66\u6865",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,158,21)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5434\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,140,54)"
                        }
                    }
                },
                {
                    "name": "\u7ea2\u5e99",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,115,17)"
                        }
                    }
                },
                {
                    "name": "\u82b1\u6728",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,74,132)"
                        }
                    }
                },
                {
                    "name": "\u592a\u9633\u5bab",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,134,68)"
                        }
                    }
                },
                {
                    "name": "\u8427\u5c71\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,114,48)"
                        }
                    }
                },
                {
                    "name": "\u6d66\u6cbf",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,20,24)"
                        }
                    }
                },
                {
                    "name": "\u534e\u6f15",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,151,129)"
                        }
                    }
                },
                {
                    "name": "\u9f99\u9633\u8def\u2026",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,110,74)"
                        }
                    }
                },
                {
                    "name": "\u9646\u5bb6\u5634",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,75,31)"
                        }
                    }
                },
                {
                    "name": "\u80dc\u6d66",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,7,105)"
                        }
                    }
                },
                {
                    "name": "\u540e\u6d77",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,147,145)"
                        }
                    }
                },
                {
                    "name": "\u8398\u5e84",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,106,123)"
                        }
                    }
                },
                {
                    "name": "\u4e03\u5b9d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,140,69)"
                        }
                    }
                },
                {
                    "name": "\u6797\u548c",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,23,135)"
                        }
                    }
                },
                {
                    "name": "\u8679\u6865",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,124,15)"
                        }
                    }
                },
                {
                    "name": "\u5357\u5934",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,132,37)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5b89",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,62,77)"
                        }
                    }
                },
                {
                    "name": "\u9f13\u697c\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,71,110)"
                        }
                    }
                },
                {
                    "name": "\u5efa\u56fd\u95e8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,140,157)"
                        }
                    }
                },
                {
                    "name": "\u6816\u971e\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,138,121)"
                        }
                    }
                },
                {
                    "name": "\u5929\u6cb3\u57ce",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,137,45)"
                        }
                    }
                },
                {
                    "name": "\u6f4d\u574a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,105,70)"
                        }
                    }
                },
                {
                    "name": "\u9f99\u5c97\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,78,128)"
                        }
                    }
                },
                {
                    "name": "\u9f99\u6eaa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,96,66)"
                        }
                    }
                },
                {
                    "name": "\u4e07\u5bff\u5bfa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,80,54)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u6e56",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,58,40)"
                        }
                    }
                },
                {
                    "name": "\u4e16\u754c\u516c\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,0,81)"
                        }
                    }
                },
                {
                    "name": "\u4e07\u6cc9\u6cb3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,64,145)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u6c34\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,72,110)"
                        }
                    }
                },
                {
                    "name": "\u5357\u6e56\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,158,79)"
                        }
                    }
                },
                {
                    "name": "\u5e02\u5357\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,144,66)"
                        }
                    }
                },
                {
                    "name": "\u5929\u5c71\u8def",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,60,88)"
                        }
                    }
                },
                {
                    "name": "\u5cad\u5357",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,127,48)"
                        }
                    }
                },
                {
                    "name": "\u5357\u793c\u58eb\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,0,106)"
                        }
                    }
                },
                {
                    "name": "\u8f66\u516c\u5e99",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,128,109)"
                        }
                    }
                },
                {
                    "name": "\u5c55\u89c8\u8def",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,123,125)"
                        }
                    }
                },
                {
                    "name": "\u56db\u5b63\u9752",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,47,81)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u839e\u5e02\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,153,100)"
                        }
                    }
                },
                {
                    "name": "\u6d0b\u6cfe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,11,110)"
                        }
                    }
                },
                {
                    "name": "\u767b\u5cf0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,41,19)"
                        }
                    }
                },
                {
                    "name": "\u8df3\u4f1e\u5854",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,160,46)"
                        }
                    }
                },
                {
                    "name": "\u5434\u4e2d\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,20,10)"
                        }
                    }
                },
                {
                    "name": "\u5949\u8d24\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,154,79)"
                        }
                    }
                },
                {
                    "name": "\u6e2d\u5858",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,52,127)"
                        }
                    }
                },
                {
                    "name": "\u5357\u6d77\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,9,103)"
                        }
                    }
                },
                {
                    "name": "\u5357\u6c99\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,35,132)"
                        }
                    }
                },
                {
                    "name": "\u5927\u7af9\u6797",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,14,150)"
                        }
                    }
                },
                {
                    "name": "\u5d02\u5c71\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,105,101)"
                        }
                    }
                },
                {
                    "name": "\u6885\u9647",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,14,83)"
                        }
                    }
                },
                {
                    "name": "\u8299\u84c9\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,32,65)"
                        }
                    }
                },
                {
                    "name": "\u6ee8\u6e56\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,137,159)"
                        }
                    }
                },
                {
                    "name": "\u8f66\u7ad9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,21,114)"
                        }
                    }
                },
                {
                    "name": "\u9f99\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,7,113)"
                        }
                    }
                },
                {
                    "name": "\u6dd8\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,26,90)"
                        }
                    }
                },
                {
                    "name": "\u5b81\u56f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,73,124)"
                        }
                    }
                },
                {
                    "name": "\u6c5f\u5357",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,46,62)"
                        }
                    }
                },
                {
                    "name": "\u89c2\u6c99\u5cad",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,75,61)"
                        }
                    }
                },
                {
                    "name": "\u821c\u8015\u8def",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,29,157)"
                        }
                    }
                },
                {
                    "name": "\u57ce\u968d\u5e99",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,158,136)"
                        }
                    }
                },
                {
                    "name": "\u957f\u5bff\u8def",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,75,146)"
                        }
                    }
                },
                {
                    "name": "\u95e8\u5934\u6c9f\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,99,98)"
                        }
                    }
                },
                {
                    "name": "\u83b2\u82b1\u4e8c\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,69,79)"
                        }
                    }
                },
                {
                    "name": "\u60e0\u9633\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,116,57)"
                        }
                    }
                },
                {
                    "name": "\u592a\u5e73\u6865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,54,35)"
                        }
                    }
                },
                {
                    "name": "\u4e8c\u90ce",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,139,53)"
                        }
                    }
                },
                {
                    "name": "\u6b66\u6c49\u7ecf\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,104,153)"
                        }
                    }
                },
                {
                    "name": "\u6731\u96c0\u5927\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,41,67)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u548c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,29,38)"
                        }
                    }
                },
                {
                    "name": "\u6c5f\u590f\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,137,156)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u5c71\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,6,123)"
                        }
                    }
                },
                {
                    "name": "\u69d0\u836b\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,156,8)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u91cc\u6cb3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,30,160)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5b66\u57ce",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,148,152)"
                        }
                    }
                },
                {
                    "name": "\u8096\u5bb6\u6cb3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,37,142)"
                        }
                    }
                },
                {
                    "name": "\u5965\u4f53",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,16,103)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u6167\u5bfa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,139,125)"
                        }
                    }
                },
                {
                    "name": "\u9ec4\u5c9b\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,106,110)"
                        }
                    }
                },
                {
                    "name": "\u4eac\u5e7f\u6865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,114,51)"
                        }
                    }
                },
                {
                    "name": "\u822a\u7a7a\u6e2f\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,136,19)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u534e\u8def",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,78,146)"
                        }
                    }
                },
                {
                    "name": "\u6f15\u5b9d\u8def",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,54,84)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,0,68)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u5173",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,39,107)"
                        }
                    }
                },
                {
                    "name": "\u5143\u548c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,97,32)"
                        }
                    }
                },
                {
                    "name": "\u6c5f\u5cb8\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,138,134)"
                        }
                    }
                },
                {
                    "name": "\u767e\u5b50\u6e7e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,100,84)"
                        }
                    }
                },
                {
                    "name": "\u592a\u548c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,0,12)"
                        }
                    }
                },
                {
                    "name": "\u53e4\u58a9\u8def",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,51,66)"
                        }
                    }
                },
                {
                    "name": "\u5d07\u660e\u53bf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,101,84)"
                        }
                    }
                },
                {
                    "name": "\u841d\u5c97\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,6,138)"
                        }
                    }
                },
                {
                    "name": "\u5386\u57ce\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,85,102)"
                        }
                    }
                },
                {
                    "name": "\u6c34\u836b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,133,118)"
                        }
                    }
                },
                {
                    "name": "\u957f\u9633\u8def",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,43,91)"
                        }
                    }
                },
                {
                    "name": "\u897f\u5173",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,18,142)"
                        }
                    }
                },
                {
                    "name": "\u90eb\u90fd\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,21,93)"
                        }
                    }
                },
                {
                    "name": "\u5de6\u5bb6\u5e84",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,93,116)"
                        }
                    }
                },
                {
                    "name": "\u5efa\u8bbe\u4e8c\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,97,154)"
                        }
                    }
                },
                {
                    "name": "\u6c5f\u5b81\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,130,22)"
                        }
                    }
                },
                {
                    "name": "\u576a\u5c71\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,6,37)"
                        }
                    }
                },
                {
                    "name": "\u95f2\u6797",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,134,8)"
                        }
                    }
                },
                {
                    "name": "\u90d1\u4e1c\u65b0\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,106,32)"
                        }
                    }
                },
                {
                    "name": "\u8f6f\u4ef6\u56ed",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,67,131)"
                        }
                    }
                },
                {
                    "name": "\u8857\u9053\u53e3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,83,55)"
                        }
                    }
                },
                {
                    "name": "\u5317\u592a\u5e73\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,37,112)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u5927\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,70,158)"
                        }
                    }
                },
                {
                    "name": "\u8f66\u9642",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,138,92)"
                        }
                    }
                },
                {
                    "name": "\u5357\u4eac",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,65,35)"
                        }
                    }
                },
                {
                    "name": "\u5efa\u90ba\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,96,124)"
                        }
                    }
                },
                {
                    "name": "\u576a\u5c71\u65b0\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,135,141)"
                        }
                    }
                },
                {
                    "name": "\u78a7\u4e91\u793e\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,107,85)"
                        }
                    }
                },
                {
                    "name": "\u6e56\u91cc\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,24,8)"
                        }
                    }
                },
                {
                    "name": "\u7530\u6751",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,122,159)"
                        }
                    }
                },
                {
                    "name": "\u6f15\u6cb3\u6cfe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,90,62)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u8857",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,107,19)"
                        }
                    }
                },
                {
                    "name": "\u5458\u6751",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,44,134)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u5dde",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,5,124)"
                        }
                    }
                },
                {
                    "name": "\u4e08\u516b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,46,137)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u725b\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,155,109)"
                        }
                    }
                },
                {
                    "name": "\u5e38\u8425",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,99,160)"
                        }
                    }
                },
                {
                    "name": "\u5357\u5c71\u533b\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,69,35)"
                        }
                    }
                },
                {
                    "name": "\u897f\u5c71",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,86,5)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u6986\u6811",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,160,148)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u76f4\u95e8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,71,91)"
                        }
                    }
                },
                {
                    "name": "\u4e07\u67f3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,61,31)"
                        }
                    }
                },
                {
                    "name": "\u4eae\u9a6c\u6865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,40,34)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u6865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,77,140)"
                        }
                    }
                },
                {
                    "name": "\u6d41\u82b3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,30,60)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u5703",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,116,145)"
                        }
                    }
                },
                {
                    "name": "\u5ba3\u6b66\u95e8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,31,29)"
                        }
                    }
                },
                {
                    "name": "\u53e4\u8361",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,96,25)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u56db",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,151,66)"
                        }
                    }
                },
                {
                    "name": "\u6a2a\u5c97",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,89,37)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u5c71",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,64,45)"
                        }
                    }
                },
                {
                    "name": "\u5f00\u53d1\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,86,60)"
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
                "\u5f90\u6c47\u533a",
                "\u9ad8\u65b0\u533a",
                "\u5f20\u6c5f"
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
        chart_666d2ead2b0a478ab234ac83c49d0f26.setOption(option_666d2ead2b0a478ab234ac83c49d0f26);
    </script>
                <div id="ee720df033d142b7aea264931c0ec253" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_ee720df033d142b7aea264931c0ec253 = echarts.init(
            document.getElementById('ee720df033d142b7aea264931c0ec253'), 'white', {renderer: 'canvas'});
        var option_ee720df033d142b7aea264931c0ec253 = {
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
                    "value": 166,
                    "name": "\u6d77\u6dc0\u533a"
                },
                {
                    "value": 118,
                    "name": "\u671d\u9633\u533a"
                },
                {
                    "value": 98,
                    "name": "\u5357\u5c71\u533a"
                },
                {
                    "value": 41,
                    "name": "\u79d1\u6280\u56ed"
                },
                {
                    "value": 39,
                    "name": "\u4f59\u676d\u533a"
                },
                {
                    "value": 38,
                    "name": "\u6d66\u4e1c\u65b0\u2026"
                },
                {
                    "value": 33,
                    "name": "\u4e2d\u5173\u6751"
                },
                {
                    "value": 30,
                    "name": "\u5f90\u6c47\u533a"
                },
                {
                    "value": 29,
                    "name": "\u9ad8\u65b0\u533a"
                },
                {
                    "value": 28,
                    "name": "\u5f20\u6c5f"
                },
                {
                    "value": 27,
                    "name": "\u897f\u5317\u65fa"
                },
                {
                    "value": 26,
                    "name": "\u5b9d\u5b89\u533a"
                },
                {
                    "value": 25,
                    "name": "\u798f\u7530\u533a"
                },
                {
                    "value": 25,
                    "name": "\u897f\u6e56\u533a"
                },
                {
                    "value": 25,
                    "name": "\u671b\u4eac"
                },
                {
                    "value": 23,
                    "name": "\u4e94\u9053\u53e3"
                },
                {
                    "value": 20,
                    "name": "\u957f\u5b81\u533a"
                },
                {
                    "value": 20,
                    "name": "\u897f\u6eaa"
                },
                {
                    "value": 19,
                    "name": "\u95f5\u884c\u533a"
                },
                {
                    "value": 19,
                    "name": "\u6ee8\u6c5f\u533a"
                },
                {
                    "value": 17,
                    "name": "\u901a\u5dde\u533a"
                },
                {
                    "value": 17,
                    "name": "\u5929\u6cb3\u533a"
                },
                {
                    "value": 16,
                    "name": "\u897f\u4e8c\u65d7"
                },
                {
                    "value": 15,
                    "name": "\u4e1c\u6e56\u65b0\u2026"
                },
                {
                    "value": 15,
                    "name": "\u5927\u5174\u533a"
                },
                {
                    "value": 14,
                    "name": "\u5927\u51b2"
                },
                {
                    "value": 13,
                    "name": "\u9759\u5b89\u533a"
                },
                {
                    "value": 13,
                    "name": "\u6d77\u73e0\u533a"
                },
                {
                    "value": 13,
                    "name": "\u756a\u79ba\u533a"
                },
                {
                    "value": 13,
                    "name": "\u6b66\u4faf\u533a"
                },
                {
                    "value": 12,
                    "name": "\u6768\u6d66\u533a"
                },
                {
                    "value": 11,
                    "name": "\u8679\u6885\u8def"
                },
                {
                    "value": 11,
                    "name": "\u5de5\u4e1a\u56ed\u2026"
                },
                {
                    "value": 11,
                    "name": "\u5b66\u9662\u8def"
                },
                {
                    "value": 10,
                    "name": "\u987a\u5fb7\u533a"
                },
                {
                    "value": 10,
                    "name": "\u62f1\u5885\u533a"
                },
                {
                    "value": 9,
                    "name": "\u6df1\u5733\u6e7e"
                },
                {
                    "value": 9,
                    "name": "\u4e0a\u5730"
                },
                {
                    "value": 9,
                    "name": "\u9f99\u534e"
                },
                {
                    "value": 9,
                    "name": "\u8679\u53e3\u533a"
                },
                {
                    "value": 9,
                    "name": "\u897f\u5174"
                },
                {
                    "value": 8,
                    "name": "\u9ec4\u6d66\u533a"
                },
                {
                    "value": 7,
                    "name": "\u6d2a\u5c71\u533a"
                },
                {
                    "value": 7,
                    "name": "\u96c1\u5854\u533a"
                },
                {
                    "value": 7,
                    "name": "\u5f90\u5bb6\u6c47"
                },
                {
                    "value": 7,
                    "name": "\u5317\u65b0\u6cfe"
                },
                {
                    "value": 7,
                    "name": "\u4ea6\u5e84"
                },
                {
                    "value": 7,
                    "name": "\u4e9a\u8fd0\u6751"
                },
                {
                    "value": 7,
                    "name": "\u957f\u6cb3"
                },
                {
                    "value": 7,
                    "name": "\u897f\u4e09\u65d7"
                },
                {
                    "value": 6,
                    "name": "\u677e\u6c5f\u533a"
                },
                {
                    "value": 6,
                    "name": "\u4e2d\u5c71\u516c\u2026"
                },
                {
                    "value": 6,
                    "name": "\u4ed3\u524d"
                },
                {
                    "value": 6,
                    "name": "\u9152\u4ed9\u6865"
                },
                {
                    "value": 6,
                    "name": "\u96e8\u82b1\u53f0\u2026"
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
                    "value": 5,
                    "name": "\u9752\u6d66\u533a"
                },
                {
                    "value": 5,
                    "name": "\u897f\u6e56"
                },
                {
                    "value": 5,
                    "name": "\u4e1c\u57ce\u533a"
                },
                {
                    "value": 5,
                    "name": "\u6765\u5e7f\u8425"
                },
                {
                    "value": 5,
                    "name": "\u77e5\u6625\u8def"
                },
                {
                    "value": 5,
                    "name": "\u56de\u9f99\u89c2"
                },
                {
                    "value": 5,
                    "name": "\u601d\u660e\u533a"
                },
                {
                    "value": 4,
                    "name": "\u9f99\u534e\u65b0\u2026"
                },
                {
                    "value": 4,
                    "name": "\u660c\u5e73\u533a"
                },
                {
                    "value": 4,
                    "name": "\u751c\u6c34\u56ed"
                },
                {
                    "value": 4,
                    "name": "\u56db\u60e0"
                },
                {
                    "value": 4,
                    "name": "\u65b0\u6e2f"
                },
                {
                    "value": 4,
                    "name": "\u897f\u4e3d"
                },
                {
                    "value": 4,
                    "name": "\u9547\u5b81\u8def"
                },
                {
                    "value": 4,
                    "name": "\u9ec4\u57d4\u533a"
                },
                {
                    "value": 4,
                    "name": "\u548c\u5e73\u91cc"
                },
                {
                    "value": 4,
                    "name": "\u897f\u57ce\u533a"
                },
                {
                    "value": 3,
                    "name": "\u8d8a\u79c0\u533a"
                },
                {
                    "value": 3,
                    "name": "\u71d5\u838e"
                },
                {
                    "value": 3,
                    "name": "\u8700\u5c71\u533a"
                },
                {
                    "value": 3,
                    "name": "\u4e30\u53f0\u533a"
                },
                {
                    "value": 3,
                    "name": "\u5927\u5c71\u5b50"
                },
                {
                    "value": 3,
                    "name": "\u6e1d\u5317\u533a"
                },
                {
                    "value": 3,
                    "name": "\u897f\u76f4\u95e8"
                },
                {
                    "value": 3,
                    "name": "\u5742\u7530"
                },
                {
                    "value": 3,
                    "name": "\u9999\u6d32\u533a"
                },
                {
                    "value": 3,
                    "name": "\u9ad8\u65b0\u6280\u2026"
                },
                {
                    "value": 3,
                    "name": "\u5b98\u6d32"
                },
                {
                    "value": 3,
                    "name": "\u671d\u5916"
                },
                {
                    "value": 3,
                    "name": "\u897f\u4e61"
                },
                {
                    "value": 3,
                    "name": "\u5efa\u5916\u5927\u2026"
                },
                {
                    "value": 3,
                    "name": "\u5b9a\u798f\u5e84"
                },
                {
                    "value": 3,
                    "name": "\u7acb\u6c34\u6865"
                },
                {
                    "value": 3,
                    "name": "\u4e09\u58a9"
                },
                {
                    "value": 3,
                    "name": "\u5927\u671b\u8def"
                },
                {
                    "value": 3,
                    "name": "\u4e0b\u57ce\u533a"
                },
                {
                    "value": 3,
                    "name": "\u666e\u9640\u533a"
                },
                {
                    "value": 3,
                    "name": "\u73e0\u6c5f\u65b0\u2026"
                },
                {
                    "value": 3,
                    "name": "\u5357\u6cb9"
                },
                {
                    "value": 3,
                    "name": "\u4e94\u89d2\u573a"
                },
                {
                    "value": 3,
                    "name": "\u7f57\u6e56\u533a"
                },
                {
                    "value": 3,
                    "name": "\u68e0\u4e0b"
                },
                {
                    "value": 3,
                    "name": "\u5317\u5916\u6ee9"
                },
                {
                    "value": 3,
                    "name": "\u957f\u5f81"
                },
                {
                    "value": 2,
                    "name": "\u5ef6\u5409"
                },
                {
                    "value": 2,
                    "name": "\u94b1\u5858\u533a"
                },
                {
                    "value": 2,
                    "name": "\u9ad8\u7891\u5e97"
                },
                {
                    "value": 2,
                    "name": "\u5cb3\u9e93\u533a"
                },
                {
                    "value": 2,
                    "name": "\u671d\u9633\u95e8"
                },
                {
                    "value": 2,
                    "name": "\u7fe0\u82d1"
                },
                {
                    "value": 2,
                    "name": "\u524d\u6d77"
                },
                {
                    "value": 2,
                    "name": "\u5b89\u8d1e"
                },
                {
                    "value": 2,
                    "name": "\u5b89\u4ead"
                },
                {
                    "value": 2,
                    "name": "\u897f\u82d1"
                },
                {
                    "value": 2,
                    "name": "\u9526\u6c5f\u533a"
                },
                {
                    "value": 2,
                    "name": "\u5317\u82d1"
                },
                {
                    "value": 2,
                    "name": "\u5173\u5c71"
                },
                {
                    "value": 2,
                    "name": "\u6253\u6d66\u6865"
                },
                {
                    "value": 2,
                    "name": "\u65b0\u5434\u533a"
                },
                {
                    "value": 2,
                    "name": "\u7ea2\u5e99"
                },
                {
                    "value": 2,
                    "name": "\u82b1\u6728"
                },
                {
                    "value": 2,
                    "name": "\u592a\u9633\u5bab"
                },
                {
                    "value": 2,
                    "name": "\u8427\u5c71\u533a"
                },
                {
                    "value": 2,
                    "name": "\u6d66\u6cbf"
                },
                {
                    "value": 2,
                    "name": "\u534e\u6f15"
                },
                {
                    "value": 2,
                    "name": "\u9f99\u9633\u8def\u2026"
                },
                {
                    "value": 2,
                    "name": "\u9646\u5bb6\u5634"
                },
                {
                    "value": 2,
                    "name": "\u80dc\u6d66"
                },
                {
                    "value": 2,
                    "name": "\u540e\u6d77"
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
                    "name": "\u6797\u548c"
                },
                {
                    "value": 2,
                    "name": "\u8679\u6865"
                },
                {
                    "value": 2,
                    "name": "\u5357\u5934"
                },
                {
                    "value": 2,
                    "name": "\u65b0\u5b89"
                },
                {
                    "value": 2,
                    "name": "\u9f13\u697c\u533a"
                },
                {
                    "value": 2,
                    "name": "\u5efa\u56fd\u95e8"
                },
                {
                    "value": 2,
                    "name": "\u6816\u971e\u533a"
                },
                {
                    "value": 2,
                    "name": "\u5929\u6cb3\u57ce"
                },
                {
                    "value": 2,
                    "name": "\u6f4d\u574a"
                },
                {
                    "value": 2,
                    "name": "\u9f99\u5c97\u533a"
                },
                {
                    "value": 1,
                    "name": "\u9f99\u6eaa"
                },
                {
                    "value": 1,
                    "name": "\u4e07\u5bff\u5bfa"
                },
                {
                    "value": 1,
                    "name": "\u5e73\u6e56"
                },
                {
                    "value": 1,
                    "name": "\u4e16\u754c\u516c\u2026"
                },
                {
                    "value": 1,
                    "name": "\u4e07\u6cc9\u6cb3"
                },
                {
                    "value": 1,
                    "name": "\u91d1\u6c34\u533a"
                },
                {
                    "value": 1,
                    "name": "\u5357\u6e56\u533a"
                },
                {
                    "value": 1,
                    "name": "\u5e02\u5357\u533a"
                },
                {
                    "value": 1,
                    "name": "\u5929\u5c71\u8def"
                },
                {
                    "value": 1,
                    "name": "\u5cad\u5357"
                },
                {
                    "value": 1,
                    "name": "\u5357\u793c\u58eb\u2026"
                },
                {
                    "value": 1,
                    "name": "\u8f66\u516c\u5e99"
                },
                {
                    "value": 1,
                    "name": "\u5c55\u89c8\u8def"
                },
                {
                    "value": 1,
                    "name": "\u56db\u5b63\u9752"
                },
                {
                    "value": 1,
                    "name": "\u4e1c\u839e\u5e02\u2026"
                },
                {
                    "value": 1,
                    "name": "\u6d0b\u6cfe"
                },
                {
                    "value": 1,
                    "name": "\u767b\u5cf0"
                },
                {
                    "value": 1,
                    "name": "\u8df3\u4f1e\u5854"
                },
                {
                    "value": 1,
                    "name": "\u5434\u4e2d\u533a"
                },
                {
                    "value": 1,
                    "name": "\u5949\u8d24\u533a"
                },
                {
                    "value": 1,
                    "name": "\u6e2d\u5858"
                },
                {
                    "value": 1,
                    "name": "\u5357\u6d77\u533a"
                },
                {
                    "value": 1,
                    "name": "\u5357\u6c99\u533a"
                },
                {
                    "value": 1,
                    "name": "\u5927\u7af9\u6797"
                },
                {
                    "value": 1,
                    "name": "\u5d02\u5c71\u533a"
                },
                {
                    "value": 1,
                    "name": "\u6885\u9647"
                },
                {
                    "value": 1,
                    "name": "\u8299\u84c9\u533a"
                },
                {
                    "value": 1,
                    "name": "\u6ee8\u6e56\u533a"
                },
                {
                    "value": 1,
                    "name": "\u8f66\u7ad9"
                },
                {
                    "value": 1,
                    "name": "\u9f99\u2026"
                },
                {
                    "value": 1,
                    "name": "\u6dd8\u91d1"
                },
                {
                    "value": 1,
                    "name": "\u5b81\u56f4"
                },
                {
                    "value": 1,
                    "name": "\u6c5f\u5357"
                },
                {
                    "value": 1,
                    "name": "\u89c2\u6c99\u5cad"
                },
                {
                    "value": 1,
                    "name": "\u821c\u8015\u8def"
                },
                {
                    "value": 1,
                    "name": "\u57ce\u968d\u5e99"
                },
                {
                    "value": 1,
                    "name": "\u957f\u5bff\u8def"
                },
                {
                    "value": 1,
                    "name": "\u95e8\u5934\u6c9f\u2026"
                },
                {
                    "value": 1,
                    "name": "\u83b2\u82b1\u4e8c\u2026"
                },
                {
                    "value": 1,
                    "name": "\u60e0\u9633\u533a"
                },
                {
                    "value": 1,
                    "name": "\u592a\u5e73\u6865"
                },
                {
                    "value": 1,
                    "name": "\u4e8c\u90ce"
                },
                {
                    "value": 1,
                    "name": "\u6b66\u6c49\u7ecf\u2026"
                },
                {
                    "value": 1,
                    "name": "\u6731\u96c0\u5927\u2026"
                },
                {
                    "value": 1,
                    "name": "\u4eba\u548c"
                },
                {
                    "value": 1,
                    "name": "\u6c5f\u590f\u533a"
                },
                {
                    "value": 1,
                    "name": "\u91d1\u5c71\u533a"
                },
                {
                    "value": 1,
                    "name": "\u69d0\u836b\u533a"
                },
                {
                    "value": 1,
                    "name": "\u4e09\u91cc\u6cb3"
                },
                {
                    "value": 1,
                    "name": "\u5927\u5b66\u57ce"
                },
                {
                    "value": 1,
                    "name": "\u8096\u5bb6\u6cb3"
                },
                {
                    "value": 1,
                    "name": "\u5965\u4f53"
                },
                {
                    "value": 1,
                    "name": "\u5b9a\u6167\u5bfa"
                },
                {
                    "value": 1,
                    "name": "\u9ec4\u5c9b\u533a"
                },
                {
                    "value": 1,
                    "name": "\u4eac\u5e7f\u6865"
                },
                {
                    "value": 1,
                    "name": "\u822a\u7a7a\u6e2f\u2026"
                },
                {
                    "value": 1,
                    "name": "\u65b0\u534e\u8def"
                },
                {
                    "value": 1,
                    "name": "\u6f15\u5b9d\u8def"
                },
                {
                    "value": 1,
                    "name": "\u4e0a\u6d77"
                },
                {
                    "value": 1,
                    "name": "\u5c0f\u5173"
                },
                {
                    "value": 1,
                    "name": "\u5143\u548c"
                },
                {
                    "value": 1,
                    "name": "\u6c5f\u5cb8\u533a"
                },
                {
                    "value": 1,
                    "name": "\u767e\u5b50\u6e7e"
                },
                {
                    "value": 1,
                    "name": "\u592a\u548c"
                },
                {
                    "value": 1,
                    "name": "\u53e4\u58a9\u8def"
                },
                {
                    "value": 1,
                    "name": "\u5d07\u660e\u53bf"
                },
                {
                    "value": 1,
                    "name": "\u841d\u5c97\u533a"
                },
                {
                    "value": 1,
                    "name": "\u5386\u57ce\u533a"
                },
                {
                    "value": 1,
                    "name": "\u6c34\u836b"
                },
                {
                    "value": 1,
                    "name": "\u957f\u9633\u8def"
                },
                {
                    "value": 1,
                    "name": "\u897f\u5173"
                },
                {
                    "value": 1,
                    "name": "\u90eb\u90fd\u533a"
                },
                {
                    "value": 1,
                    "name": "\u5de6\u5bb6\u5e84"
                },
                {
                    "value": 1,
                    "name": "\u5efa\u8bbe\u4e8c\u2026"
                },
                {
                    "value": 1,
                    "name": "\u6c5f\u5b81\u533a"
                },
                {
                    "value": 1,
                    "name": "\u576a\u5c71\u533a"
                },
                {
                    "value": 1,
                    "name": "\u95f2\u6797"
                },
                {
                    "value": 1,
                    "name": "\u90d1\u4e1c\u65b0\u2026"
                },
                {
                    "value": 1,
                    "name": "\u8f6f\u4ef6\u56ed"
                },
                {
                    "value": 1,
                    "name": "\u8857\u9053\u53e3"
                },
                {
                    "value": 1,
                    "name": "\u5317\u592a\u5e73\u2026"
                },
                {
                    "value": 1,
                    "name": "\u5317\u4eac\u5927\u2026"
                },
                {
                    "value": 1,
                    "name": "\u8f66\u9642"
                },
                {
                    "value": 1,
                    "name": "\u5357\u4eac"
                },
                {
                    "value": 1,
                    "name": "\u5efa\u90ba\u533a"
                },
                {
                    "value": 1,
                    "name": "\u576a\u5c71\u65b0\u2026"
                },
                {
                    "value": 1,
                    "name": "\u78a7\u4e91\u793e\u2026"
                },
                {
                    "value": 1,
                    "name": "\u6e56\u91cc\u533a"
                },
                {
                    "value": 1,
                    "name": "\u7530\u6751"
                },
                {
                    "value": 1,
                    "name": "\u6f15\u6cb3\u6cfe"
                },
                {
                    "value": 1,
                    "name": "\u91d1\u878d\u8857"
                },
                {
                    "value": 1,
                    "name": "\u5458\u6751"
                },
                {
                    "value": 1,
                    "name": "\u5e7f\u5dde"
                },
                {
                    "value": 1,
                    "name": "\u4e08\u516b"
                },
                {
                    "value": 1,
                    "name": "\u91d1\u725b\u533a"
                },
                {
                    "value": 1,
                    "name": "\u5e38\u8425"
                },
                {
                    "value": 1,
                    "name": "\u5357\u5c71\u533b\u2026"
                },
                {
                    "value": 1,
                    "name": "\u897f\u5c71"
                },
                {
                    "value": 1,
                    "name": "\u53cc\u6986\u6811"
                },
                {
                    "value": 1,
                    "name": "\u4e1c\u76f4\u95e8"
                },
                {
                    "value": 1,
                    "name": "\u4e07\u67f3"
                },
                {
                    "value": 1,
                    "name": "\u4eae\u9a6c\u6865"
                },
                {
                    "value": 1,
                    "name": "\u91d1\u6865"
                },
                {
                    "value": 1,
                    "name": "\u6d41\u82b3"
                },
                {
                    "value": 1,
                    "name": "\u4e1c\u5703"
                },
                {
                    "value": 1,
                    "name": "\u5ba3\u6b66\u95e8"
                },
                {
                    "value": 1,
                    "name": "\u53e4\u8361"
                },
                {
                    "value": 1,
                    "name": "\u4e1c\u56db"
                },
                {
                    "value": 1,
                    "name": "\u6a2a\u5c97"
                },
                {
                    "value": 1,
                    "name": "\u4e94\u5c71"
                },
                {
                    "value": 1,
                    "name": "\u5f00\u53d1\u533a"
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
        chart_ee720df033d142b7aea264931c0ec253.setOption(option_ee720df033d142b7aea264931c0ec253);
    </script>
                <div id="862ff413485641c3b6d259d7da82dc32" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_862ff413485641c3b6d259d7da82dc32 = echarts.init(
            document.getElementById('862ff413485641c3b6d259d7da82dc32'), 'white', {renderer: 'canvas'});
        var option_862ff413485641c3b6d259d7da82dc32 = {
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
                367,
                301,
                230,
                192,
                151,
                143,
                87,
                79
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
                    "value": 367
                },
                {
                    "name": "\u4e0d\u9700\u8981\u878d\u8d44",
                    "value": 301
                },
                {
                    "name": "A\u8f6e",
                    "value": 230
                },
                {
                    "name": "B\u8f6e",
                    "value": 192
                },
                {
                    "name": "\u672a\u878d\u8d44",
                    "value": 151
                },
                {
                    "name": "D\u8f6e\u53ca\u4ee5\u4e0a",
                    "value": 143
                },
                {
                    "name": "C\u8f6e",
                    "value": 87
                },
                {
                    "name": "\u5929\u4f7f\u8f6e",
                    "value": 79
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
                    "value": 367
                },
                {
                    "name": "\u4e0d\u9700\u8981\u878d\u8d44",
                    "value": 301
                },
                {
                    "name": "A\u8f6e",
                    "value": 230
                },
                {
                    "name": "B\u8f6e",
                    "value": 192
                },
                {
                    "name": "\u672a\u878d\u8d44",
                    "value": 151
                },
                {
                    "name": "D\u8f6e\u53ca\u4ee5\u4e0a",
                    "value": 143
                },
                {
                    "name": "C\u8f6e",
                    "value": 87
                },
                {
                    "name": "\u5929\u4f7f\u8f6e",
                    "value": 79
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
                "\u672a\u878d\u8d44",
                "D\u8f6e\u53ca\u4ee5\u4e0a",
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
                "\u672a\u878d\u8d44",
                "D\u8f6e\u53ca\u4ee5\u4e0a",
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
        chart_862ff413485641c3b6d259d7da82dc32.setOption(option_862ff413485641c3b6d259d7da82dc32);
    </script>
                <div id="ea897d4112f14914b0fd20b7cfb410df" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_ea897d4112f14914b0fd20b7cfb410df = echarts.init(
            document.getElementById('ea897d4112f14914b0fd20b7cfb410df'), 'white', {renderer: 'canvas'});
        var option_ea897d4112f14914b0fd20b7cfb410df = {
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
                436,
                331,
                296,
                287,
                180,
                20
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
                    "value": 436
                },
                {
                    "name": "150-500\u4eba",
                    "value": 331
                },
                {
                    "name": "50-150\u4eba",
                    "value": 296
                },
                {
                    "name": "500-2000\u4eba",
                    "value": 287
                },
                {
                    "name": "15-50\u4eba",
                    "value": 180
                },
                {
                    "name": "\u5c11\u4e8e15\u4eba",
                    "value": 20
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
                    "value": 436
                },
                {
                    "name": "150-500\u4eba",
                    "value": 331
                },
                {
                    "name": "50-150\u4eba",
                    "value": 296
                },
                {
                    "name": "500-2000\u4eba",
                    "value": 287
                },
                {
                    "name": "15-50\u4eba",
                    "value": 180
                },
                {
                    "name": "\u5c11\u4e8e15\u4eba",
                    "value": 20
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
        chart_ea897d4112f14914b0fd20b7cfb410df.setOption(option_ea897d4112f14914b0fd20b7cfb410df);
    </script>
                <div id="16806f3562174744abd2074641ebe9f1" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_16806f3562174744abd2074641ebe9f1 = echarts.init(
            document.getElementById('16806f3562174744abd2074641ebe9f1'), 'white', {renderer: 'canvas'});
        var option_16806f3562174744abd2074641ebe9f1 = {
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
                438,
                245,
                151,
                144,
                140,
                108,
                90
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
                    "value": 438,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,10,110)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u670d\u52a1",
                    "value": 245,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,139,41)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u670d\u52a1",
                    "value": 151,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,81,44)"
                        }
                    }
                },
                {
                    "name": "\u8f6f\u4ef6\u670d\u52a1",
                    "value": 144,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,46,149)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u786c\u4ef6",
                    "value": 140,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,109,121)"
                        }
                    }
                },
                {
                    "name": "IT\u6280\u672f\u670d\u52a1",
                    "value": 108,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,102,141)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u6280\u91d1\u878d",
                    "value": 90,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,53,52)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u5177\u7c7b\u4ea7\u54c1",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,5,70)"
                        }
                    }
                },
                {
                    "name": "\u79fb\u52a8\u4e92\u8054\u7f51",
                    "value": 75,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,30,104)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546\u5e73\u53f0",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,65,135)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd",
                    "value": 57,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,134,77)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u8d44\u8baf",
                    "value": 57,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,95,112)"
                        }
                    }
                },
                {
                    "name": "\u4f01\u4e1a\u670d\u52a1",
                    "value": 55,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,91,81)"
                        }
                    }
                },
                {
                    "name": "\u6e38\u620f",
                    "value": 51,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,64,153)"
                        }
                    }
                },
                {
                    "name": "\u7269\u8054\u7f51",
                    "value": 51,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,143,142)"
                        }
                    }
                },
                {
                    "name": "\u5728\u7ebf\u6559\u80b2",
                    "value": 49,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,50,127)"
                        }
                    }
                },
                {
                    "name": "\u6d88\u8d39\u751f\u6d3b",
                    "value": 49,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,115,70)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u4e1a\u670d\u52a1",
                    "value": 48,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,72,127)"
                        }
                    }
                },
                {
                    "name": "\u5176\u4ed6",
                    "value": 48,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,3,74)"
                        }
                    }
                },
                {
                    "name": "\u77ed\u89c6\u9891",
                    "value": 48,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,67,68)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u5a92\u4f53",
                    "value": 45,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,25,99)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u9891",
                    "value": 45,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,132,35)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u793e\u533a",
                    "value": 44,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,46,100)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u6e38",
                    "value": 39,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,147,50)"
                        }
                    }
                },
                {
                    "name": "\u51fa\u884c",
                    "value": 38,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,20,61)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4ea4\u5e73\u53f0",
                    "value": 37,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,148,147)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u5b89\u5168",
                    "value": 35,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,34,93)"
                        }
                    }
                },
                {
                    "name": "\u8425\u9500\u670d\u52a1",
                    "value": 32,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,55,93)"
                        }
                    }
                },
                {
                    "name": "\u5236\u9020\u4e1a",
                    "value": 27,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,31,2)"
                        }
                    }
                },
                {
                    "name": "\u8f6f\u4ef6\u5f00\u53d1",
                    "value": 24,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,1,141)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u4e28\u5065\u5eb7",
                    "value": 24,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,79,70)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u4e1a",
                    "value": 24,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,20,38)"
                        }
                    }
                },
                {
                    "name": "\u786c\u4ef6",
                    "value": 24,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,145,55)"
                        }
                    }
                },
                {
                    "name": "\u5728\u7ebf\u533b\u7597",
                    "value": 23,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,112,80)"
                        }
                    }
                },
                {
                    "name": "\u7269\u6d41",
                    "value": 23,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,85,83)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u8f93",
                    "value": 23,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,72,26)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546",
                    "value": 20,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,29,75)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u68c0\u7d22",
                    "value": 18,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,18,35)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4ea4\u5a92\u4f53",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,80,78)"
                        }
                    }
                },
                {
                    "name": "\u5c45\u4f4f\u670d\u52a1",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,15,8)"
                        }
                    }
                },
                {
                    "name": "\u7269\u4e1a",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,119,56)"
                        }
                    }
                },
                {
                    "name": "\u623f\u5730\u4ea7",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,73,10)"
                        }
                    }
                },
                {
                    "name": "\u6559\u80b2",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,111,62)"
                        }
                    }
                },
                {
                    "name": "\u76f4\u64ad\u5e73\u53f0",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,101,118)"
                        }
                    }
                },
                {
                    "name": "MCN",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,74,105)"
                        }
                    }
                },
                {
                    "name": "\u5efa\u7b51",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,4,150)"
                        }
                    }
                },
                {
                    "name": "\u7269\u6d41\u5e73\u53f0",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,22,87)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u96f6\u552e",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,113,100)"
                        }
                    }
                },
                {
                    "name": "\u6279\u53d1",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,100,107)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u552e",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,103,108)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,60,64)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u7edc\u901a\u4fe1",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,155,29)"
                        }
                    }
                },
                {
                    "name": "\u901a\u8baf\u7535\u5b50",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,18,42)"
                        }
                    }
                },
                {
                    "name": "\u533a\u5757\u94fe",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,117,31)"
                        }
                    }
                },
                {
                    "name": "\u8fdb\u51fa\u53e3",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,125,92)"
                        }
                    }
                },
                {
                    "name": "\u8d38\u6613",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,92,119)"
                        }
                    }
                },
                {
                    "name": "\u6587\u5a31\u4e28\u5185\u5bb9",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,33,36)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5a92\u4f53",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,118,43)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u5bb9",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,81,61)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,94,16)"
                        }
                    }
                },
                {
                    "name": "\u4fdd\u5065",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,123,91)"
                        }
                    }
                },
                {
                    "name": "\u5a31\u4e50",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,21,60)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u5177",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,145,112)"
                        }
                    }
                },
                {
                    "name": "\u4f11\u95f2",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,6,90)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4ea4",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,20,95)"
                        }
                    }
                },
                {
                    "name": "\u7269\u6d41\u4e28\u8fd0\u8f93",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,35,86)"
                        }
                    }
                },
                {
                    "name": "\u6c7d\u8f66\u4e28\u51fa\u884c",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,23,98)"
                        }
                    }
                },
                {
                    "name": "\u6587\u5316\u4f20\u5a92",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,138,100)"
                        }
                    }
                },
                {
                    "name": "\u57f9\u8bad",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,142,85)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u80fd\u6e90\u6c7d\u8f66\u5236\u9020",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,95,23)"
                        }
                    }
                },
                {
                    "name": "\u751f\u6d3b\u670d\u52a1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,77,5)"
                        }
                    }
                },
                {
                    "name": "\u52a8\u6f2b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,67,32)"
                        }
                    }
                },
                {
                    "name": "\u5f71\u89c6",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,82,8)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u3001\u8f6f\u4ef6\u5f00\u53d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,25,34)"
                        }
                    }
                },
                {
                    "name": "\u6c7d\u8f66\u4ea4\u6613\u5e73\u53f0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,120,70)"
                        }
                    }
                },
                {
                    "name": "\u519c\u6797\u7267\u6e14",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,70,25)"
                        }
                    }
                },
                {
                    "name": "\u80fd\u6e90",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,72,8)"
                        }
                    }
                },
                {
                    "name": "\u4f01\u4e1a\u670d\u52a1 \u8f6f\u4ef6\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,104,52)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u3001\u6c7d\u8f66\u4e28\u51fa\u884c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,100,102)"
                        }
                    }
                },
                {
                    "name": "\u79fb\u52a8\u4e92\u8054\u7f51 \u4f01\u4e1a\u670d\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,24,93)"
                        }
                    }
                },
                {
                    "name": "\u77ff\u4ea7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,91,130)"
                        }
                    }
                },
                {
                    "name": "\u623f\u4ea7\u5bb6\u5c45",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,109,45)"
                        }
                    }
                },
                {
                    "name": "\u73af\u4fdd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,19,120)"
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
        chart_16806f3562174744abd2074641ebe9f1.setOption(option_16806f3562174744abd2074641ebe9f1);
    </script>
                <div id="9d4d9061574943ce9a2cc45813203298" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_9d4d9061574943ce9a2cc45813203298 = echarts.init(
            document.getElementById('9d4d9061574943ce9a2cc45813203298'), 'white', {renderer: 'canvas'});
        var option_9d4d9061574943ce9a2cc45813203298 = {
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
                421,
                97,
                78,
                62,
                54,
                38,
                29
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
                    "value": 421,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,101,4)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u7b97\u6cd5",
                    "value": 97,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,53,51)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u7b97\u6cd5",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,109,8)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 62,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,9,142)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5",
                    "value": 54,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,53,86)"
                        }
                    }
                },
                {
                    "name": "AI\u7b97\u6cd5",
                    "value": 38,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,90,146)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                    "value": 29,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,116,151)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9\u7b97\u6cd5",
                    "value": 25,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,87,21)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u9891\u7b97\u6cd5",
                    "value": 23,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,133,74)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u7b97\u6cd5",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,111,74)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u673a\u89c6\u89c9\u7b97\u6cd5",
                    "value": 18,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,155,73)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u7b97\u6cd5",
                    "value": 18,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,82,63)"
                        }
                    }
                },
                {
                    "name": "ai\u7b97\u6cd5",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,35,130)"
                        }
                    }
                },
                {
                    "name": "slam\u7b97\u6cd5",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,55,65)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7136\u8bed\u8a00\u5904\u7406\u7b97\u6cd5",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,73,114)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u8bc6\u522b\u7b97\u6cd5",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,75,37)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u63a8\u8350\u7b97\u6cd5",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,140,18)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u7b97\u6cd5",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,22,130)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u56fe\u50cf\u7b97\u6cd5",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,11,148)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u7b97\u6cd5",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,142,124)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7\u7b97\u6cd5",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,104,4)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62\u7b97\u6cd5",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,105,60)"
                        }
                    }
                },
                {
                    "name": "\u611f\u77e5\u7b97\u6cd5",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,115,62)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u8bc6\u522b\u7b97\u6cd5",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,137,143)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u63a8\u8350\u7b97\u6cd5",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,3,103)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6316\u6398\u7b97\u6cd5",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,0,29)"
                        }
                    }
                },
                {
                    "name": "\u5bfc\u822a\u7b97\u6cd5",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,12,142)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7b97\u6cd5",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,76,33)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7/\u8d44\u6df1\u7b97\u6cd5",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,116,124)"
                        }
                    }
                },
                {
                    "name": "SLAM\u7b97\u6cd5",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,81,6)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u7b97\u6cd5",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,147,132)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u7b97\u6cd5",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,103,1)"
                        }
                    }
                },
                {
                    "name": "\u63a7\u5236\u7b97\u6cd5",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,14,124)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5904\u7406\u7b97\u6cd5",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,148,51)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u89c6\u89c9\u7b97\u6cd5",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,72,150)"
                        }
                    }
                },
                {
                    "name": "ocr\u7b97\u6cd5",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,60,56)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7AI\u7b97\u6cd5",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,154,147)"
                        }
                    }
                },
                {
                    "name": "CV\u7b97\u6cd5",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,61,158)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u7b97\u6cd5",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,44,83)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79\u7b97\u6cd5",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,149,88)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79\u4f18\u5316\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,103,51)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u53f7\u5904\u7406 \u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,5,45)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,23,108)"
                        }
                    }
                },
                {
                    "name": "\u51b3\u7b56\u89c4\u5212\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,55,92)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,17,138)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u4f4d\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,11,81)"
                        }
                    }
                },
                {
                    "name": "\u533a\u5757\u94fe\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,61,110)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u8bc6\u56fe\u8c31\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,34,69)"
                        }
                    }
                },
                {
                    "name": "3D\u91cd\u5efa\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,59,19)"
                        }
                    }
                },
                {
                    "name": "\u7b56\u7565\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,12,41)"
                        }
                    }
                },
                {
                    "name": "\u521d\u7ea7\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,68,115)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u7ea7\u56fe\u50cf\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,45,55)"
                        }
                    }
                },
                {
                    "name": "\u9884\u6d4b\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,53,8)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u641c\u7d22\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,68,139)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u5e7f\u544a\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,48,87)"
                        }
                    }
                },
                {
                    "name": "\u51e0\u4f55\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,138,108)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u5408\u6210\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,53,95)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u7814\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,133,1)"
                        }
                    }
                },
                {
                    "name": "O2O\u5373\u65f6\u914d\u9001\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,19,81)"
                        }
                    }
                },
                {
                    "name": "\u5730\u56fe\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,103,52)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u56fe\u50cf\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,7,65)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u97f3\u9891\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,143,123)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u3001\u56fe\u50cf\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,113,138)"
                        }
                    }
                },
                {
                    "name": "\u901a\u4fe1\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,1,3)"
                        }
                    }
                },
                {
                    "name": "AI \u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,116,112)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u611f\u77e5\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,120,80)"
                        }
                    }
                },
                {
                    "name": "\u6210\u50cf\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,138,64)"
                        }
                    }
                },
                {
                    "name": "\u7c7b\u8111\u667a\u80fd\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,66,44)"
                        }
                    }
                },
                {
                    "name": "2D/3D\u56fe\u5f62\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,4,58)"
                        }
                    }
                },
                {
                    "name": "AR\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,65,83)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u5168\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,15,127)"
                        }
                    }
                },
                {
                    "name": "AI\u8d44\u6df1\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,104,89)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u52a8\u63a7\u5236\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,100,19)"
                        }
                    }
                },
                {
                    "name": "\u6821\u62db-\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,25,131)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1AI\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,114,114)"
                        }
                    }
                },
                {
                    "name": "\u8682\u8681\u96c6\u56e2-\u63a8\u8350\u641c\u7d22\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,147,108)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7f16\u89e3\u7801\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,24,145)"
                        }
                    }
                },
                {
                    "name": "\u7b56\u7565\u67b6\u6784\u7814\u53d1\u5de5\u7a0b\u5e08\uff08\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,0,8)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u63a7\u5236\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,114,127)"
                        }
                    }
                },
                {
                    "name": "\u5171\u8bc6\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,109,29)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9\u56fe\u50cf\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,94,36)"
                        }
                    }
                },
                {
                    "name": "\u9065\u611f\u56fe\u50cf\u5904\u7406\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,35,19)"
                        }
                    }
                },
                {
                    "name": "TOC\u4e1a\u52a1\u7fa4O2O\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,9,10)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,54,130)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62\u56fe\u50cf\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,93,15)"
                        }
                    }
                },
                {
                    "name": "CT\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,54,31)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7f16\u7801\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,140,61)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,10,96)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u7cfb\u7edf\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,147,133)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u5bfc\u822a\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,121,139)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u641c\u7d22\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,20,106)"
                        }
                    }
                },
                {
                    "name": "ROS\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,124,62)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9\u667a\u80fd\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,88,26)"
                        }
                    }
                },
                {
                    "name": "\u91cf\u5316\u4ea4\u6613\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,32,7)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u6570\u636e\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,47,55)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5206\u6790\u5e08\\\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,26,18)"
                        }
                    }
                },
                {
                    "name": "\u589e\u957f\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,124,77)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u63a7\u5236\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,86,55)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u5b66\u4e60/\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,53,41)"
                        }
                    }
                },
                {
                    "name": "\u5f3a\u5316\u5b66\u4e60\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,65,12)"
                        }
                    }
                },
                {
                    "name": "OCR\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,26,76)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u603b\u76d1\uff08\u6570\u636e\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,144,108)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u89c6\u89c9/\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,53,127)"
                        }
                    }
                },
                {
                    "name": "\u8bca\u65ad\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,91,159)"
                        }
                    }
                },
                {
                    "name": "00206-NLP\u9ad8\u7ea7\u5de5\u7a0b\u5e08/\u8d44\u6df1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,77,18)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u56fe\u5f62\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,99,20)"
                        }
                    }
                },
                {
                    "name": "\u4eff\u771f\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,103,137)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7cbe\u5730\u56fe\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,14,24)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u68c0\u7d22\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,58,83)"
                        }
                    }
                },
                {
                    "name": "ADAS\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,70,148)"
                        }
                    }
                },
                {
                    "name": "254138-NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,9,129)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,131,106)"
                        }
                    }
                },
                {
                    "name": "ASR\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,124,13)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u56e2\u9a91\u884c-\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,17,108)"
                        }
                    }
                },
                {
                    "name": "Soul App-\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,80,146)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u8a00\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,88,2)"
                        }
                    }
                },
                {
                    "name": "0341DO-NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,45,40)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u56e2App-\u7f8e\u56e2\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,65,48)"
                        }
                    }
                },
                {
                    "name": "\u4f20\u611f\u5668\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,5,70)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,157,42)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,59,149)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7\u53cd\u6b3a\u8bc8\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,96,38)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,54,7)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u95fb\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,16,11)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u8425\u9500\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,121,149)"
                        }
                    }
                },
                {
                    "name": "\u9884\u4f30\u6a21\u578b \u7528\u6237\u753b\u50cf \u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,46,55)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u5316\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,132,120)"
                        }
                    }
                },
                {
                    "name": "0241VF-NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,94,144)"
                        }
                    }
                },
                {
                    "name": "\u5b9e\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,130,44)"
                        }
                    }
                },
                {
                    "name": "\u8f6f\u4ef6\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,69,77)"
                        }
                    }
                },
                {
                    "name": "3D\u70b9\u4e91\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,59,125)"
                        }
                    }
                },
                {
                    "name": "\u4eac\u4e1c\u96c6\u56e2-\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,104,16)"
                        }
                    }
                },
                {
                    "name": "5G\u901a\u4fe1\u667a\u80fd\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,77,131)"
                        }
                    }
                },
                {
                    "name": "26310R-\u81ea\u7136\u8bed\u8a00\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,27,48)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u753b\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,88,156)"
                        }
                    }
                },
                {
                    "name": "AEB/LKA/ACC\u7814\u53d1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,58,6)"
                        }
                    }
                },
                {
                    "name": "\u5730\u56fe\u5b9a\u4f4d\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,90,71)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u5b89\u5168\u53ca\u5bc6\u7801\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,95,41)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf/OCR\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,52,17)"
                        }
                    }
                },
                {
                    "name": "25215M-AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,49,144)"
                        }
                    }
                },
                {
                    "name": "\u6821\u62db-\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,94,52)"
                        }
                    }
                },
                {
                    "name": "\u533b\u5b66\u5f71\u50cf\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,54,35)"
                        }
                    }
                },
                {
                    "name": "024168-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,96,84)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u56fe\u50cf\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,81,57)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u51b3\u7b56\u89c4\u5212\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,28,69)"
                        }
                    }
                },
                {
                    "name": "09412L-NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,128,93)"
                        }
                    }
                },
                {
                    "name": "\u51b3\u7b56\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,126,101)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u6392\u5e8f\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,15,26)"
                        }
                    }
                },
                {
                    "name": "\u5782\u76f4\u884c\u4e1a\u5e7f\u544a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,28,42)"
                        }
                    }
                },
                {
                    "name": "\u589e\u5f3a\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,104,109)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u5168\u7b56\u7565\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,105,2)"
                        }
                    }
                },
                {
                    "name": "NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,22,101)"
                        }
                    }
                },
                {
                    "name": "\u3010\u521b\u4e1a\u5408\u4f19\u4eba\u3011java/iOS/Android/PD/\u6570\u636e/\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,93,131)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6316\u6398\u4e0e\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,29,23)"
                        }
                    }
                },
                {
                    "name": "\u4fdd\u9669\u4ea7\u54c1\u7ecf\u7406\uff08\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,51,81)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u591a\u6a21\u6001\u7406\u89e3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,108,46)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u5e73\u53f0-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,46,12)"
                        }
                    }
                },
                {
                    "name": "\u6fc0\u5149\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,104,129)"
                        }
                    }
                },
                {
                    "name": "AR\u56fe\u5f62\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,75,2)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u8ba1\u7b97\u673a\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,107,111)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,33,114)"
                        }
                    }
                },
                {
                    "name": "\u79fb\u52a8\u7aef\u63a8\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,83,39)"
                        }
                    }
                },
                {
                    "name": "\u6fc0\u5149SLAM/\u591a\u4f20\u611f\u5668\u878d\u5408\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,30,158)"
                        }
                    }
                },
                {
                    "name": "\u8054\u90a6\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,143,126)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u6570\u636e\u6316\u6398\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,51,28)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546\u98ce\u63a7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,35,101)"
                        }
                    }
                },
                {
                    "name": "0232KT-\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,115,29)"
                        }
                    }
                },
                {
                    "name": "ASR/TTS\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,123,15)"
                        }
                    }
                },
                {
                    "name": "\u56f4\u68cbAI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,137,89)"
                        }
                    }
                },
                {
                    "name": "5G\u57fa\u5e26\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,107,59)"
                        }
                    }
                },
                {
                    "name": "0341DN-\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,31,52)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u7ebf\u7535\u4fe1\u53f7\u8bc6\u522b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,126,160)"
                        }
                    }
                },
                {
                    "name": "MIG-\u81ea\u52a8\u9a7e\u9a76\u611f\u77e5\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,42,119)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u8bed\u97f3\u8bc6\u522b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,76,56)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7136\u8bed\u8a00\u5904\u7406\u90e8_ \u81ea\u7136\u8bed\u8a00\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,5,120)"
                        }
                    }
                },
                {
                    "name": "\u4f20\u7edf\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,2,100)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u7406\u89e3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,86,117)"
                        }
                    }
                },
                {
                    "name": "\u6d41\u5a92\u4f53\u4f20\u8f93\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,39,148)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u5e94\u7528\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,113,131)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u8138\u8bc6\u522b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,4,45)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6316\u6398\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,140,93)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62\u5b66\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,65,91)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u7ecf\u7406\uff08\u786c\u4ef6\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,141,85)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7/\u8d44\u6df1\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,62,61)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u786c\u4ef6\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,49,115)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,113,30)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7\u7b56\u7565\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,4,155)"
                        }
                    }
                },
                {
                    "name": "3A\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,98,108)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u6d4b\u91cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,42,114)"
                        }
                    }
                },
                {
                    "name": "[\u6025]\u7f51\u5b89\u8d44\u6df1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,61,135)"
                        }
                    }
                },
                {
                    "name": "SPBU-\u9ad8\u7ea7\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,105,143)"
                        }
                    }
                },
                {
                    "name": "11414F-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,131,58)"
                        }
                    }
                },
                {
                    "name": "\u30102021\u6821\u62db-\u672a\u6765\u661f\u9879\u76ee\u3011\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,73,79)"
                        }
                    }
                },
                {
                    "name": "MIG-\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,136,19)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u7ea7AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,20,39)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,143,76)"
                        }
                    }
                },
                {
                    "name": "AF\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,22,32)"
                        }
                    }
                },
                {
                    "name": "\u3010\u6821\u62db\u3011\u641c\u7d22\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,108,6)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,103,75)"
                        }
                    }
                },
                {
                    "name": "55413O-AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,34,55)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u5e73\u53f0-\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,51,156)"
                        }
                    }
                },
                {
                    "name": "CFD\u5f00\u6e90\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,158,69)"
                        }
                    }
                },
                {
                    "name": "Vslam\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,88,130)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u8c03\u5ea6\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,89,83)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u7814\u53d1\u5de5\u7a0b\u5e08-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,83,62)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u4e0eNLP\u90e8-\u641c\u7d22\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,14,27)"
                        }
                    }
                },
                {
                    "name": "\u58f0\u5b66\u6a21\u578b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,67,149)"
                        }
                    }
                },
                {
                    "name": "1141BI-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,11,102)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,3,99)"
                        }
                    }
                },
                {
                    "name": "55413Q-AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,114,95)"
                        }
                    }
                },
                {
                    "name": "\u878d\u5408\u5b9a\u4f4d\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,25,8)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u5e73\u53f0\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,33,9)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u89c6\u9891\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,100,24)"
                        }
                    }
                },
                {
                    "name": "\u6c14\u8c61/\u9065\u611f\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,114,16)"
                        }
                    }
                },
                {
                    "name": "\u52a0\u5bc6\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,38,99)"
                        }
                    }
                },
                {
                    "name": "\u591a\u4f20\u611f\u5668\u878d\u5408\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,112,27)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u8bc6\u522b\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,114,35)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u673a\u89c6\u89c9\uff083D\u65b9\u5411\uff09\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,74,72)"
                        }
                    }
                },
                {
                    "name": "\u5b9e\u4e60\u751f-\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,28,83)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,9,46)"
                        }
                    }
                },
                {
                    "name": "\u60c5\u666f\u667a\u80fd\u878d\u5408\u5b9a\u4f4d\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,93,82)"
                        }
                    }
                },
                {
                    "name": "\u70b9\u4e91\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,22,155)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u97f3\u9891\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,43,31)"
                        }
                    }
                },
                {
                    "name": "\u7535\u8c03\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,14,90)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6316\u6398/\u53cd\u4f5c\u5f0a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,52,99)"
                        }
                    }
                },
                {
                    "name": "\u51b3\u7b56\u4e0e\u8fd0\u52a8\u89c4\u5212\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,151,132)"
                        }
                    }
                },
                {
                    "name": "3D\u5f71\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,4,104)"
                        }
                    }
                },
                {
                    "name": "39318E-\u8ba1\u7b97\u673a\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,131,95)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5206\u6790\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,83,135)"
                        }
                    }
                },
                {
                    "name": "\u3010\u7f8e\u56e2\u4f18\u9009\u3011-\u8425\u9500\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,153,89)"
                        }
                    }
                },
                {
                    "name": "\u5e94\u7528\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,87,24)"
                        }
                    }
                },
                {
                    "name": "024208-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,107,158)"
                        }
                    }
                },
                {
                    "name": "\u4eac\u4e1c\u5e7f\u544a-\u8d44\u6df1\u5e7f\u544a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,152,120)"
                        }
                    }
                },
                {
                    "name": "\u5546\u54c1\u7ecf\u8425\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,34,62)"
                        }
                    }
                },
                {
                    "name": "XH4713-\u6d41\u5a92\u4f53\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,32,29)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u79d1\u6280\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,68,50)"
                        }
                    }
                },
                {
                    "name": "0232S5-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,80,91)"
                        }
                    }
                },
                {
                    "name": "\u5546\u4e1a\u641c\u7d22-\u5e7f\u544a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,54,7)"
                        }
                    }
                },
                {
                    "name": "\u6e38\u620f\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,79,120)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u641c\u7d22\u5e7f\u544a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,97,116)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u81ea\u7136\u8bed\u8a00\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,71,130)"
                        }
                    }
                },
                {
                    "name": "\u8292\u679c\u7f51\u516c\u53f8-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,37,14)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7/\u8d44\u6df1/\u4e13\u5bb6\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,55,137)"
                        }
                    }
                },
                {
                    "name": "\u7535\u673a\u9a71\u52a8\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,158,45)"
                        }
                    }
                },
                {
                    "name": "\u3010\u4e0a\u6d77\u677e\u6c5f\u533a\u3011\u6545\u969c\u9884\u6d4b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,39,152)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u56fe\u5f62\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,85,1)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,150,96)"
                        }
                    }
                },
                {
                    "name": "\u533b\u5b66\u5f71\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,160,34)"
                        }
                    }
                },
                {
                    "name": "\u533b\u5b66\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,104,38)"
                        }
                    }
                },
                {
                    "name": "SG8103-SPBU-\u89c6\u9891\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,31,3)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u9645\u5316\u5b9a\u4ef7\u8865\u8d34\u4e13\u5bb6\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,95,33)"
                        }
                    }
                },
                {
                    "name": "\u5f02\u6784\u8ba1\u7b97\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,27,113)"
                        }
                    }
                },
                {
                    "name": "\u6c83\u98de\u957f\u7a7a-\u884c\u4e1a\u89e3\u51b3\u65b9\u6848\u53ca\u4ea7\u54c1\u5e73\u53f0-\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,94,151)"
                        }
                    }
                },
                {
                    "name": "324121-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,106,7)"
                        }
                    }
                },
                {
                    "name": "05412O-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,76,43)"
                        }
                    }
                },
                {
                    "name": "\u641c\u72d7\u6570\u5b57\u4eba-3D\u4eba\u8138\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,132,144)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u56e2App-\u7528\u6237\u589e\u957f\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,103,70)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u70b9\u4e91\u5206\u6790\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,42,28)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u8bc6\u56fe\u8c31\u90e8_\u7b56\u7565\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,1,76)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22/\u6392\u5e8f\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,146,89)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546\u7b56\u7565\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,42,14)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u8ba1\u7b97\u673a\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,122,70)"
                        }
                    }
                },
                {
                    "name": "\u5929\u732b\u7cbe\u7075\u4e8b\u4e1a\u90e8-\u8bed\u97f3\u5408\u6210\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,117,113)"
                        }
                    }
                },
                {
                    "name": "0241QC-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,117,126)"
                        }
                    }
                },
                {
                    "name": "\u98de\u63a7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,101,79)"
                        }
                    }
                },
                {
                    "name": "\u4e2a\u6027\u5316\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,123,112)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u4e92\u5de5\u7a0b-\u521b\u610f\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,98,60)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u98ce\u63a7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,101,79)"
                        }
                    }
                },
                {
                    "name": "MIG-\u81ea\u52a8\u9a7e\u9a76\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,43,100)"
                        }
                    }
                },
                {
                    "name": "\u6c14\u8c61\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,18,107)"
                        }
                    }
                },
                {
                    "name": "\u8f68\u8ff9\u8ddf\u968f\u63a7\u5236\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,130,119)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,154,2)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u7edc\u56fe\u8c31\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,71,24)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,62,153)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u56fe\u7247\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,157,148)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u5e7f\u544a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,22,116)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u589e\u957f\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,85,26)"
                        }
                    }
                },
                {
                    "name": "\u57fa\u91d1\u4ea7\u54c1\u7ecf\u7406\uff08\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,20,160)"
                        }
                    }
                },
                {
                    "name": "\u58f0\u7eb9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,11,146)"
                        }
                    }
                },
                {
                    "name": "\u3010\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,115,42)"
                        }
                    }
                },
                {
                    "name": "BL5944-SPBU-\u7f8e\u989c\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,35,58)"
                        }
                    }
                },
                {
                    "name": "\u5bc6\u7801\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,53,126)"
                        }
                    }
                },
                {
                    "name": "\u521d\u4e2d\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,46,34)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u4fe1\u53f7\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,140,62)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u722c\u866b\u7b56\u7565\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,109,35)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u8bc4\u6d4b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,69,1)"
                        }
                    }
                },
                {
                    "name": "\u957f\u5b89\u8f6f\u4ef6\u516c\u53f8-\u6fc0\u5149\u5b9a\u4f4d\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,96,134)"
                        }
                    }
                },
                {
                    "name": "AI/\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,159,34)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u5e7f\u544a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,48,97)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7136\u8bed\u8a00\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,68,25)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u6027\u80fdAI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,26,94)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u5168\u90e8_\u5185\u5bb9\u4fdd\u62a4\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,31,135)"
                        }
                    }
                },
                {
                    "name": "\u589e\u957f\u6295\u653e\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,64,20)"
                        }
                    }
                },
                {
                    "name": "\u5b9e\u65f6\u8def\u51b5\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,40,121)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u8d37\u6a21\u578b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,124,137)"
                        }
                    }
                },
                {
                    "name": "\u89c4\u5212\u5bfc\u822a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,82,109)"
                        }
                    }
                },
                {
                    "name": "\u5929\u732b\u597d\u623f-\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,136,49)"
                        }
                    }
                },
                {
                    "name": "\u8def\u5f84\u89c4\u5212\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,106,20)"
                        }
                    }
                },
                {
                    "name": "\u6253\u8f66\u667a\u80fd\u4f9b\u7ed9\u7b56\u7565\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,68,42)"
                        }
                    }
                },
                {
                    "name": "\u96f7\u8fbe\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,1,27)"
                        }
                    }
                },
                {
                    "name": "SW-\u5e94\u7528\u5f00\u53d1\u5de5\u7a0b\u5e08",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,24,54)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5efa\u6a21\uff08\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,33,53)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u4e0e\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,67,81)"
                        }
                    }
                },
                {
                    "name": "NLP&CV\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,110,71)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u91cd\u5efa\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,4,40)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u7b56\u7565\u90e8_\u89c6\u9891/\u89c6\u89c9\u7406\u89e3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,0,27)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u5fb7-Java\u9ad8\u7ea7\u5f00\u53d1\u5de5\u7a0b\u5e08/\u4e13\u5bb6-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,98,56)"
                        }
                    }
                },
                {
                    "name": "\u5bf9\u8bdd\u63a8\u8350\u8d44\u6df1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,92,88)"
                        }
                    }
                },
                {
                    "name": "\u767e\u5ea6\u5730\u56fe\u70b9\u4e91/\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,8,16)"
                        }
                    }
                },
                {
                    "name": "113154-\u8d44\u6df1/\u4e13\u5bb6\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,120,34)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u70b9\u4e91\u5206\u6790\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,84,159)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\uff08\u56fe\u50cf\u8bc6\u522b\uff09\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,111,45)"
                        }
                    }
                },
                {
                    "name": "FF2824-\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,42,131)"
                        }
                    }
                },
                {
                    "name": "2021\u6821\u62db-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,13,5)"
                        }
                    }
                },
                {
                    "name": "NLP/\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,57,140)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u673a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,136,116)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u7b56\u7565\u90e8-\u673a\u5668\u5b66\u4e60/\u6570\u636e\u6316\u6398/NLP/\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,142,115)"
                        }
                    }
                },
                {
                    "name": "TTS\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,141,5)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9\u5b9a\u4f4d\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,138,55)"
                        }
                    }
                },
                {
                    "name": "TTS\u8bed\u97f3\u5408\u6210\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,34,66)"
                        }
                    }
                },
                {
                    "name": "\u7535\u78c1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,42,58)"
                        }
                    }
                },
                {
                    "name": "\u7aef\u4fa7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,85,152)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,37,77)"
                        }
                    }
                },
                {
                    "name": "\u91cf\u5316\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,89,80)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u89c6\u9891\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,11,47)"
                        }
                    }
                },
                {
                    "name": "\u6d4b\u8bd5\uff08\u8bed\u97f3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,18,140)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,73,61)"
                        }
                    }
                },
                {
                    "name": "SLAM/VIO/\u4e09\u7ef4\u91cd\u5efa\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,19,14)"
                        }
                    }
                },
                {
                    "name": "\u6fc0\u5149SLAM\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,62,32)"
                        }
                    }
                },
                {
                    "name": "\u8f6f\u4ef6\u5de5\u7a0b\u5e08\u3001\u5d4c\u5165\u5f0f\u8f6f\u4ef6\u5de5\u7a0b\u5e08\u3001\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,107,39)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7Gnss\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,82,67)"
                        }
                    }
                },
                {
                    "name": "DSP\u5e7f\u544a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,142,56)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,140,0)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u53f7\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,32,31)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1(\u63a8\u8350)\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,139,105)"
                        }
                    }
                },
                {
                    "name": "\u6559\u80b2\u6d4b\u91cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,80,50)"
                        }
                    }
                },
                {
                    "name": "\u6fc0\u5149slam\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,42,77)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7f16\u89e3\u7801\u4e0e\u89c6\u9891\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,95,133)"
                        }
                    }
                },
                {
                    "name": "3D \u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,67,53)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u548c\u89c6\u9891\u7406\u89e3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,44,160)"
                        }
                    }
                },
                {
                    "name": "\u957f\u5b89\u8f6f\u4ef6\u516c\u53f8-\u4f17\u5305\u5730\u56fe\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,26,51)"
                        }
                    }
                },
                {
                    "name": "0341ET-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,119,79)"
                        }
                    }
                },
                {
                    "name": "\u652f\u4ed8\u98ce\u63a7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,82,69)"
                        }
                    }
                },
                {
                    "name": "25318B-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,25,68)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u4fe1\u53f7\u5904\u7406/\u8bed\u97f3\u8bc6\u522b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,136,84)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u7acb\u4f53\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,92,24)"
                        }
                    }
                },
                {
                    "name": "3D\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,91,77)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u683c\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,79,142)"
                        }
                    }
                },
                {
                    "name": "NN\u964d\u566a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,67,45)"
                        }
                    }
                },
                {
                    "name": "\u5d4c\u5165\u5f0f\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,144,145)"
                        }
                    }
                },
                {
                    "name": "\u3010\u6df1\u5733\u3011GNSS\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,127,84)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350/\u641c\u7d22\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,36,100)"
                        }
                    }
                },
                {
                    "name": "\u4f9b\u5e94\u94fe\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,110,42)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7/\u8d44\u6df1\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,86,26)"
                        }
                    }
                },
                {
                    "name": "RU0112-SPBU-\u89c6\u9891\u7f16\u89e3\u7801\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,64,22)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u7cfb\u7edf/\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,136,159)"
                        }
                    }
                },
                {
                    "name": "\u5b9e\u4e60\u751f\uff08\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,68,24)"
                        }
                    }
                },
                {
                    "name": "\u5916\u5356\u6280\u672f\u90e8-\u8d44\u6df1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,51,158)"
                        }
                    }
                },
                {
                    "name": "AY0300-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,58,57)"
                        }
                    }
                },
                {
                    "name": "1131OJ-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,143,160)"
                        }
                    }
                },
                {
                    "name": "11312G-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,107,89)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,59,132)"
                        }
                    }
                },
                {
                    "name": "\u6c83\u98de\u957f\u7a7a-\u6280\u672f\u7814\u53d1\u4e2d\u5fc3-\u98de\u884c\u63a7\u5236\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,79,87)"
                        }
                    }
                },
                {
                    "name": "\u6e32\u67d3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,35,71)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u538b\u7f29\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,63,152)"
                        }
                    }
                },
                {
                    "name": "\u8c03\u5ea6\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,53,4)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7\u6a21\u578b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,158,116)"
                        }
                    }
                },
                {
                    "name": "55413P-AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,68,160)"
                        }
                    }
                },
                {
                    "name": "\u3010\u5357\u5c71\u536b\u661f\u3011\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,122,7)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u4eba\u9a7e\u9a76\u8f66\u8f86\u63a7\u5236\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,151,124)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7136\u8bed\u8a00\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,133,153)"
                        }
                    }
                },
                {
                    "name": "\u6fc0\u5149\u5b9a\u4f4d\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,95,29)"
                        }
                    }
                },
                {
                    "name": "LJ5001-\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,49,121)"
                        }
                    }
                },
                {
                    "name": "FPGA\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,69,64)"
                        }
                    }
                },
                {
                    "name": "0241VZ-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,148,128)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7GNSS\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,31,137)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u56fe\u5f62\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,125,120)"
                        }
                    }
                },
                {
                    "name": "AI\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,145,73)"
                        }
                    }
                },
                {
                    "name": "\u5a92\u4f53\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,24,18)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u56fe\u50cf\u6548\u679c\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,2,86)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u89c4\u5212\u4e0e\u51b3\u7b56\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,16,138)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u8fd0\u52a8\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,157,155)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u667a\u80fd\u521b\u610f\u8d44\u6df1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,115,17)"
                        }
                    }
                },
                {
                    "name": "QQ\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,113,12)"
                        }
                    }
                },
                {
                    "name": "\u67b6\u6784\u5e08/\u5de5\u7a0b\u5e08\uff08\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,149,54)"
                        }
                    }
                },
                {
                    "name": "\u672c\u5730\u751f\u6d3b-\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,23,125)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u4ea7\u54c1\u7ecf\u7406\uff08\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,23,77)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546\u5e7f\u544a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,128,4)"
                        }
                    }
                },
                {
                    "name": "\u5546\u4e1a\u5e7f\u544a-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,116,1)"
                        }
                    }
                },
                {
                    "name": "39314F-\u901a\u7528\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,120,100)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60/\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,148,3)"
                        }
                    }
                },
                {
                    "name": "\u65f6\u7a7a\u6570\u636e\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,148,82)"
                        }
                    }
                },
                {
                    "name": "\u533b\u5b66\u5f71\u50cf\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,150,64)"
                        }
                    }
                },
                {
                    "name": "\u7f16\u8bd1\u5668\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,152,159)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u6d41\u5e7f\u544a-\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,129,140)"
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
        chart_9d4d9061574943ce9a2cc45813203298.setOption(option_9d4d9061574943ce9a2cc45813203298);
    </script>
                <div id="8a8456c56af54905929a14cf6ff782a4" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_8a8456c56af54905929a14cf6ff782a4 = echarts.init(
            document.getElementById('8a8456c56af54905929a14cf6ff782a4'), 'white', {renderer: 'canvas'});
            
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
    
        var option_8a8456c56af54905929a14cf6ff782a4 = {
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
                    "value": 218,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,143,88)"
                        }
                    }
                },
                {
                    "name": "\u516d\u9669\u4e00\u91d1",
                    "value": 104,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,82,117)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u7a7a\u95f4\u5927",
                    "value": 98,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,103,0)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u5e74\u5047",
                    "value": 88,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,140,102)"
                        }
                    }
                },
                {
                    "name": "\u5468\u672b\u53cc\u4f11",
                    "value": 82,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,49,27)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u5de5\u4f5c",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,104,24)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u4f11",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,65,37)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956",
                    "value": 57,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,137,2)"
                        }
                    }
                },
                {
                    "name": "\u8282\u65e5\u798f\u5229",
                    "value": 49,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,105,0)"
                        }
                    }
                },
                {
                    "name": "\u4e0b\u5348\u8336",
                    "value": 48,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,6,49)"
                        }
                    }
                },
                {
                    "name": "\u7ee9\u6548\u5956\u91d1",
                    "value": 46,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,65,70)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5e73\u53f0",
                    "value": 39,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,81,90)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4\u597d",
                    "value": 39,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,87,149)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u597d",
                    "value": 36,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,73,55)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u5316\u7ba1\u7406",
                    "value": 35,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,45,84)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u7ba1\u7406",
                    "value": 34,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,148,70)"
                        }
                    }
                },
                {
                    "name": "\u80a1\u7968\u671f\u6743",
                    "value": 32,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,1,98)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u671f\u4f53\u68c0",
                    "value": 32,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,140,55)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5e02\u516c\u53f8",
                    "value": 31,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,36,152)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u597d",
                    "value": 31,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,64,34)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f",
                    "value": 29,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,81,20)"
                        }
                    }
                },
                {
                    "name": "\u9886\u5bfcnice",
                    "value": 28,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,37,127)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4\u597d",
                    "value": 28,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,83,73)"
                        }
                    }
                },
                {
                    "name": "\u9910\u8865",
                    "value": 27,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,54,54)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u725b",
                    "value": 27,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,158,15)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u4e91\u96c6",
                    "value": 24,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,93,100)"
                        }
                    }
                },
                {
                    "name": "\u671f\u6743\u6fc0\u52b1",
                    "value": 23,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,2,54)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd",
                    "value": 22,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,100,76)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u91d1",
                    "value": 21,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,151,81)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u7a7a\u95f4\u5927",
                    "value": 21,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,20,125)"
                        }
                    }
                },
                {
                    "value": 21,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,124,120)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u5927",
                    "value": 20,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,26,20)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u597d",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,86,16)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f\u7a7a\u95f4\u5927",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,97,17)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u56e2\u961f",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,0,68)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u4e09\u9910",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,17,119)"
                        }
                    }
                },
                {
                    "name": "\u9886\u5bfc\u597d",
                    "value": 18,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,101,136)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u5e26\u961f",
                    "value": 18,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,98,14)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u591a",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,67,142)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u597d",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,53,18)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u4f11\u5047",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,13,139)"
                        }
                    }
                },
                {
                    "name": "\u7a7a\u95f4\u5927",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,88,53)"
                        }
                    }
                },
                {
                    "name": "\u524d\u666f\u597d",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,30,151)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u524d\u666f\u597d",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,157,8)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u5956\u91d1",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,17,159)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u7a7a\u95f4",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,121,79)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u5de5\u4f5c\u5236",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,26,5)"
                        }
                    }
                },
                {
                    "name": "\u725b\u4eba\u56e2\u961f",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,49,113)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u5feb",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,149,69)"
                        }
                    }
                },
                {
                    "name": "\u671f\u6743",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,115,110)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u5316",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,24,62)"
                        }
                    }
                },
                {
                    "name": "\u8282\u5047\u65e5\u798f\u5229",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,99,38)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5ea6\u4f53\u68c0",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,104,157)"
                        }
                    }
                },
                {
                    "name": "\u5065\u8eab\u745c\u4f3d",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,28,37)"
                        }
                    }
                },
                {
                    "name": "\u4e0d\u6253\u5361",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,74,104)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u6c1b\u56f4\u597d",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,90,157)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5e95\u53cc\u85aa",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,129,114)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5b9e\u529b\u5f3a",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,0,64)"
                        }
                    }
                },
                {
                    "name": "\u80a1\u6743\u6fc0\u52b1",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,155,21)"
                        }
                    }
                },
                {
                    "name": "\u4e03\u9669\u4e00\u91d1",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,142,106)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u7a7a\u95f4",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,9,92)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u56e2\u961f",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,39,57)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u578b\u7814\u7a76\u9662",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,146,66)"
                        }
                    }
                },
                {
                    "name": "\u5065\u8eab\u623f",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,2,30)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u624d\u623f\u7968",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,99,72)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u901f\u53d1\u5c55",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,155,82)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6c1b\u56f4\u597d",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,58,150)"
                        }
                    }
                },
                {
                    "name": "\u7cbe\u82f1\u56e2\u961f",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,36,131)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u540d\u592e\u4f01",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,1,110)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961fnice",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,111,126)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f\u7a7a\u95f4",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,7,99)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u4e0a\u73ed",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,90,62)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u5927",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,35,74)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u73ed\u8f66",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,93,32)"
                        }
                    }
                },
                {
                    "name": "\u8865\u5145\u533b\u7597",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,10,49)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u5e73\u53f0\u5927",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,9,31)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u5feb",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,129,81)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,158,45)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u4f18\u79c0",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,113,44)"
                        }
                    }
                },
                {
                    "name": "AI",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,23,71)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u9886\u5148",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,152,39)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5382",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,69,82)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u5efa",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,40,11)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u4fbf\u5229",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,63,160)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u4e30\u539a",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,135,34)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u5de5\u4f5c\u65f6\u95f4",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,79,97)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u9f50\u5168",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,57,17)"
                        }
                    }
                },
                {
                    "name": "\u5956\u91d1\u4e30\u539a",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,151,2)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u539a\u5e74\u7ec8\u5956",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,96,136)"
                        }
                    }
                },
                {
                    "name": "\u516d\u9669\u4e8c\u91d1",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,26,32)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u4e1a\u52a1",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,115,147)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u597d",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,159,159)"
                        }
                    }
                },
                {
                    "name": "\u5c97\u4f4d\u664b\u5347",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,46,146)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5347\u7a7a\u95f4\u5927",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,153,129)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u524d\u6cbf",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,127,74)"
                        }
                    }
                },
                {
                    "name": "16\u85aa",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,92,41)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,99,81)"
                        }
                    }
                },
                {
                    "name": "\u5305\u4e09\u9910",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,142,156)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u5956",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,77,146)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u90e8\u95e8",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,79,121)"
                        }
                    }
                },
                {
                    "name": "\u9910\u996e\u8865\u8d34",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,5,155)"
                        }
                    }
                },
                {
                    "name": "\u996d\u8865",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,7,24)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,92,118)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u91cf\u6570\u636e",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,120,35)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u4f18\u539a",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,29,3)"
                        }
                    }
                },
                {
                    "name": "\u5348\u9910\u8865\u52a9",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,27,55)"
                        }
                    }
                },
                {
                    "name": "\u751f\u65e5\u4f1a",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,8,133)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u597d",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,30,142)"
                        }
                    }
                },
                {
                    "name": "\u8865\u5145\u5546\u4e1a\u4fdd\u9669",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,9,34)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u5de5\u65f6",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,37,80)"
                        }
                    }
                },
                {
                    "name": "\u524d\u666f\u5e7f\u9614",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,149,109)"
                        }
                    }
                },
                {
                    "name": "\u9910\u8865\u7b49",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,122,150)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u65f6\u95f4",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,85,14)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u597d",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,67,118)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5ea6\u65c5\u6e38",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,54,60)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5047",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,48,155)"
                        }
                    }
                },
                {
                    "name": "\u79df\u623f\u8865\u8d34",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,118,121)"
                        }
                    }
                },
                {
                    "name": "\u6709\u8f6c\u6b63\u673a\u4f1a",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,30,59)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u72ec\u89d2\u517d",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,33,136)"
                        }
                    }
                },
                {
                    "name": "\u5305\u5403",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,77,110)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u5b66\u4e60",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,16,117)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u957f\u5e74\u5047",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,29,8)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u901f\u53d1\u5c55",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,67,98)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5b9e\u529b",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,62,5)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f\u5feb",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,23,113)"
                        }
                    }
                },
                {
                    "name": "\u673a\u4f1a\u591a",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,119,127)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u6e38",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,137,114)"
                        }
                    }
                },
                {
                    "name": "\u4e16\u754c\u4e94\u767e\u5f3a",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,91,107)"
                        }
                    }
                },
                {
                    "name": "\u524d\u6cbf\u6280\u672f",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,72,105)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u6210\u957f",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,90,8)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u901f\u6210\u957f",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,142,82)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4\u8f7b\u677e",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,5,19)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u5efa\u7b49",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,79,92)"
                        }
                    }
                },
                {
                    "name": "\u5927\u843d\u5730\u573a\u666f",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,67,76)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5916\u5e02\u573a",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,148,126)"
                        }
                    }
                },
                {
                    "name": "\u8865\u5145\u533b\u7597\u4fdd\u9669",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,7,63)"
                        }
                    }
                },
                {
                    "name": "15\u85aa",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,52,16)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u725b\u591a",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,39,152)"
                        }
                    }
                },
                {
                    "name": "\u671f\u6743\u80a1\u7968",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,40,127)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u529e\u516c",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,115,156)"
                        }
                    }
                },
                {
                    "name": "\u7ee9\u6548\u5956",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,156,59)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u9a71\u52a8",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,111,156)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c\u798f\u5229\u597d",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,47,86)"
                        }
                    }
                },
                {
                    "name": "\u5404\u79cd\u798f\u5229",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,10,50)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u9ad8\u901f\u53d1\u5c55",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,116,67)"
                        }
                    }
                },
                {
                    "name": "\u8001\u677fnice",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,115,132)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u5956\u91d1",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,72,65)"
                        }
                    }
                },
                {
                    "name": "\u6280\u80fd\u57f9\u8bad",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,53,100)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u6c1b\u56f4\u597d",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,12,8)"
                        }
                    }
                },
                {
                    "name": "12\u5929\u5e74\u5047",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,95,153)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u673a\u4f1a\u591a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,71,79)"
                        }
                    }
                },
                {
                    "name": "14\u85aa",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,17,88)"
                        }
                    }
                },
                {
                    "name": "\u671f\u6743\u5956\u52b1",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,112,71)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5348\u9910",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,61,3)"
                        }
                    }
                },
                {
                    "name": "\u804c\u4e1a\u5927\u725b",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,39,59)"
                        }
                    }
                },
                {
                    "name": "\u4e0d996",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,119,79)"
                        }
                    }
                },
                {
                    "name": "\u524d\u666f\u53ef\u89c2",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,15,2)"
                        }
                    }
                },
                {
                    "name": "\u9886\u5bfcNICE",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,146,142)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u6c14\u5341\u8db3",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,0,104)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5065\u8eab",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,33,71)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u4e13\u4e1a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,86,18)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u4eba\u9a7e\u9a76",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,92,139)"
                        }
                    }
                },
                {
                    "name": "\u4e8b\u4e1a\u5355\u4f4d",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,128,81)"
                        }
                    }
                },
                {
                    "name": "\u8fc7\u8282\u8d39",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,156,97)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u5c97\u4f4d",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,95,122)"
                        }
                    }
                },
                {
                    "name": "\u623f\u8865",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,89,66)"
                        }
                    }
                },
                {
                    "name": "\u671d\u4e5d\u665a\u516d",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,106,132)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u878d\u6d3d",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,31,144)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u4f01",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,50,80)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u85aa",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,56,106)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u989d\u5956\u91d1",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,38,53)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u8865\u52a9",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,119,95)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u5e7f",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,124,0)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u53d1\u5c55\u597d",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,154,158)"
                        }
                    }
                },
                {
                    "name": "\u80a1\u4efd\u671f\u6743",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,10,5)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u7a33\u5b9a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,8,148)"
                        }
                    }
                },
                {
                    "name": "\u4e0d\u52a0\u73ed",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,130,152)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,41,149)"
                        }
                    }
                },
                {
                    "name": "\u5065\u5168\u664b\u5347\u673a\u5236",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,99,42)"
                        }
                    }
                },
                {
                    "name": "\u9910\u8d39\u8865\u8d34",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,117,76)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,2,139)"
                        }
                    }
                },
                {
                    "name": "\u73ed\u8f66",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,43,35)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u7a0b\u5e08\u6587\u5316",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,146,52)"
                        }
                    }
                },
                {
                    "name": "\u671d\u9633\u884c\u4e1a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,125,51)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u798f\u5229",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,96,30)"
                        }
                    }
                },
                {
                    "name": "\u4e16\u754c500\u5f3a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,62,17)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u9ad8",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,94,146)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u9614\u5e73\u53f0",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,138,88)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7814\u56e2\u961f",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,11,79)"
                        }
                    }
                },
                {
                    "name": "\u5168\u989d\u4e94\u9669\u4e00\u91d1",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,43,84)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c\u798f\u5229",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,41,102)"
                        }
                    }
                },
                {
                    "name": "\u804c\u4f4d\u664b\u5347",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,3,145)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4\u4f73",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,89,156)"
                        }
                    }
                },
                {
                    "name": "AI\u72ec\u89d2\u517d",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,71,155)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u798f\u5229",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,50,110)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5e74\u8f7b",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,153,148)"
                        }
                    }
                },
                {
                    "name": "\u72ec\u89d2\u517d",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,67,19)"
                        }
                    }
                },
                {
                    "name": "\u5730\u94c1\u5468\u8fb9",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,157,2)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u591a\u591a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,117,55)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f\u5feb\u901f",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,37,151)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u673a\u4f1a\u591a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,2,105)"
                        }
                    }
                },
                {
                    "name": "1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,80,160)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4\u73af\u5883\u597d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,36,78)"
                        }
                    }
                },
                {
                    "name": "\u73af\u5883\u597d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,77,64)"
                        }
                    }
                },
                {
                    "name": "\u5165\u804c\u8d2d\u4e70\u4e94\u9669\u4e00\u91d1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,22,53)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u4f18\u539a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,74,37)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u7f8e\u5473\u4e09\u9910",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,44,53)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5168",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,89,46)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5347\u7a7a\u95f4",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,21,45)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,52,70)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4\u6d3b\u8dc3",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,23,81)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c14\u6c1b\u597d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,131,79)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u52b1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,16,0)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u98df\u996e\u6599",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,129,95)"
                        }
                    }
                },
                {
                    "name": "\u591f\u6311\u6218\u591f\u523a\u6fc0",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,113,21)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u591a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,151,54)"
                        }
                    }
                },
                {
                    "name": "base",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,6,105)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u8fdb\u597d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,106,78)"
                        }
                    }
                },
                {
                    "name": "\u6709\u73ed\u8f66",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,159,44)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u8865\u8d34",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,160,85)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u9910\u98df",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,66,118)"
                        }
                    }
                },
                {
                    "name": "\u65e0996",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,6,56)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u68d2",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,16,154)"
                        }
                    }
                },
                {
                    "name": "\u72ec\u89d2\u517d\u516c\u53f8",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,104,108)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c\u798f\u5229\u4f73",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,0,46)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u524d\u666f\u597d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,9,82)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u5927\u725b",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,15,52)"
                        }
                    }
                },
                {
                    "name": "\u5546\u4e1a\u4fdd\u9669",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,156,99)"
                        }
                    }
                },
                {
                    "name": "\u7ee9\u6548\u80a1\u7968",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,111,24)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4nice",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,89,127)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1\u5168\u989d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,27,116)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6c1b\u56f4\u6d53\u539a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,127,33)"
                        }
                    }
                },
                {
                    "name": "\u72ec\u5f53\u4e00\u9762",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,18,122)"
                        }
                    }
                },
                {
                    "name": "\u521b\u4e1a\u56e2\u961f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,10,32)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,52,70)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,127,151)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u9645\u5316\u56e2\u961f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,59,26)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u671f\u56e2\u5efa",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,117,107)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6709\u7231",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,113,2)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u6709\u5927\u884c\u76f4\u9500\u94f6\u884c",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,64,101)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u65b9\u4fbf",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,39,13)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u79c0\u56e2\u961f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,128,8)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u7ebf\u798f\u5229",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,20,123)"
                        }
                    }
                },
                {
                    "name": "14-20\u85aa",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,149,38)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u4f4f\u5bbf",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,1,53)"
                        }
                    }
                },
                {
                    "name": "\u7269\u8054\u7f51",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,29,58)"
                        }
                    }
                },
                {
                    "name": "\u51fa\u56fd\u65c5\u6e38",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,110,20)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u798f\u5229\u4f73",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,0,93)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u7a33\u5b9a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,36,116)"
                        }
                    }
                },
                {
                    "name": "2",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,131,83)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u8fc7\u4ebf",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,2,31)"
                        }
                    }
                },
                {
                    "name": "\u7b7e\u5b57\u73b0\u91d1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,143,104)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u9ad8",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,2,24)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1\u7b49",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,64,13)"
                        }
                    }
                },
                {
                    "name": "\u6e05\u534e\u56e2\u961f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,139,130)"
                        }
                    }
                },
                {
                    "name": "\u5168\u52e4\u5956",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,65,50)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u6f5c\u529b",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,108,71)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u826f\u597d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,56,68)"
                        }
                    }
                },
                {
                    "name": "\u5165\u804c\u80a1\u7968",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,54,122)"
                        }
                    }
                },
                {
                    "name": "13\u85aa+\u5e74\u7ec8\u5956+\u5458\u5de5\u6301\u80a1\u5236\u5ea6",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,100,53)"
                        }
                    }
                },
                {
                    "name": "13\u85aa",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,150,35)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u901f\u5ea6\u5feb",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,84,66)"
                        }
                    }
                },
                {
                    "name": "\u6253\u8f66\u62a5\u9500",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,102,114)"
                        }
                    }
                },
                {
                    "name": "\u51fa\u6d77\u4e1a\u52a1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,131,137)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u65c5\u6e38",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,144,152)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u901f\u6210\u957f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,12,28)"
                        }
                    }
                },
                {
                    "name": "\u521b\u4e1a\u516c\u53f8",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,144,104)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u85aa\u9ad8\u80a1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,1,70)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u4f18",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,29,60)"
                        }
                    }
                },
                {
                    "name": "\u6781\u5ba2\u6587\u5316",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,127,75)"
                        }
                    }
                },
                {
                    "name": "\u5e02\u573a\u5316\u85aa\u916c",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,74,96)"
                        }
                    }
                },
                {
                    "name": "\u901a\u8baf\u8865\u8d34",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,40,148)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u4f1a\u7a7a\u95f4\u5927",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,76,46)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u884c\u4e1a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,151,38)"
                        }
                    }
                },
                {
                    "name": "\u91cd\u70b9\u9879\u76ee",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,123,115)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u5bfc\u5e08",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,51,125)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,29,23)"
                        }
                    }
                },
                {
                    "name": "\u51fa\u56fd\u57f9\u8bad",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,92,149)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u9879\u76ee",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,156,92)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u8f6c\u6b63",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,62,120)"
                        }
                    }
                },
                {
                    "name": "\u573a\u666f\u4e30\u5bcc",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,15,69)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u7814\u673a\u6784",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,146,19)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5927\u725b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,133,109)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u6237\u53e3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,134,121)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u900f\u660e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,67,20)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u5feb\u901f\u53d1\u5c55",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,31,138)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u8f7b\u5316",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,100,124)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u75c5\u5047",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,134,66)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u4e1a\u56e2\u961f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,113,34)"
                        }
                    }
                },
                {
                    "name": "\u6bcf\u5468\u56e2\u5efa",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,77,94)"
                        }
                    }
                },
                {
                    "name": "\u8c03\u85aa\u673a\u5236",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,145,124)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5065\u8eab\u623f\u7406\u53d1\u5e97",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,74,17)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,108,14)"
                        }
                    }
                },
                {
                    "name": "\u793e\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,103,157)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5065\u5168",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,99,48)"
                        }
                    }
                },
                {
                    "name": "\u5341\u4e94\u85aa",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,119,82)"
                        }
                    }
                },
                {
                    "name": "\u5168\u989d\u516d\u9669\u4e00\u91d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,57,137)"
                        }
                    }
                },
                {
                    "name": "\u4f9b\u5e94\u4e09\u9910",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,35,100)"
                        }
                    }
                },
                {
                    "name": "\u529e\u516c\u73af\u5883\u597d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,154,155)"
                        }
                    }
                },
                {
                    "name": "\u51fa\u6d77****0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,129,158)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u4f11\u5047",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,75,57)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u4e0b\u5348\u8336",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,2,10)"
                        }
                    }
                },
                {
                    "name": "\u7a33\u5b9a\u5e73\u53f0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,148,155)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u5efa\u6d3b\u52a8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,8,12)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u843d\u5730",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,118,151)"
                        }
                    }
                },
                {
                    "name": "\u5468\u672b\u52a0\u73ed\u53cc\u500d\u5de5\u8d44",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,129,9)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u5f85\u9047\u597d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,38,92)"
                        }
                    }
                },
                {
                    "name": "\u591a\u6b21\u8c03\u85aa",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,150,51)"
                        }
                    }
                },
                {
                    "name": "\u4f9b\u5e94\u94fe",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,158,32)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u80a1\u4e0a\u5e02",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,26,22)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u5357\u4e9a\u5e02\u573a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,128,38)"
                        }
                    }
                },
                {
                    "name": "\u72ec\u89d2\u517d\u4f01\u4e1a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,130,20)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u7b97\u6cd5\u7814\u53d1\u56e2\u961f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,102,1)"
                        }
                    }
                },
                {
                    "name": "3D\u89c6\u89c9",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,37,52)"
                        }
                    }
                },
                {
                    "name": "\u529e\u516c\u73af\u5883\u4f18\u8d8a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,101,67)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u65c5\u6e38",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,33,1)"
                        }
                    }
                },
                {
                    "name": "\u524d\u666f\u5e7f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,74,57)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u4f01\u80cc\u666f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,101,95)"
                        }
                    }
                },
                {
                    "name": "\u516d\u9669\u4e00\u91d1\u5168\u989d\u7f34\u7eb3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,24,94)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u4e1a\u57f9\u8bad",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,147,101)"
                        }
                    }
                },
                {
                    "name": "\u5047\u671f\u591a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,78,74)"
                        }
                    }
                },
                {
                    "name": "\u4e3b\u52a8\u52a0\u85aa",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,137,102)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u4e0a\u4e0b\u73ed",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,131,51)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u540d\u7535\u5546\u5e73\u53f0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,112,109)"
                        }
                    }
                },
                {
                    "name": "\u91cd\u89c6\u6280\u672f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,140,159)"
                        }
                    }
                },
                {
                    "name": "\u94f6\u884c\u80cc\u666f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,96,98)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u672a\u6765\u91cd\u70b9\u53d1\u5c55",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,134,117)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u5e73\u53f0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,110,46)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u5e7f\u9614",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,98,71)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u591a\u5927\u725b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,95,70)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,102,61)"
                        }
                    }
                },
                {
                    "name": "AI\u72ec\u89d2\u517d\u4f01\u4e1a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,37,110)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u7a33\u5b9a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,154,151)"
                        }
                    }
                },
                {
                    "name": "\u6e05\u534e\u6d59\u5927",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,107,107)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u53e3\u6d6a\u5c16",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,153,121)"
                        }
                    }
                },
                {
                    "name": "\u6781\u5ba2\u6c1b\u56f4",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,97,51)"
                        }
                    }
                },
                {
                    "name": "\u6210\u719f\u5927\u5e73\u53f0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,112,133)"
                        }
                    }
                },
                {
                    "name": "\u6709\u517c\u804c\u5c97\u4f4d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,20,67)"
                        }
                    }
                },
                {
                    "name": "\u5730\u94c1\u4e0a\u76d6",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,42,157)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u5496\u591a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,44,75)"
                        }
                    }
                },
                {
                    "name": "\u5168\u989d\u516c\u79ef\u91d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,39,25)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u4f73",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,112,131)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u4e0a\u73ed\u65f6\u95f4",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,13,38)"
                        }
                    }
                },
                {
                    "name": "\u804c\u4f4d\u664b\u5347\u7a7a\u95f4\u5927",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,30,42)"
                        }
                    }
                },
                {
                    "name": "\u8c03\u85aa",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,59,158)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,118,50)"
                        }
                    }
                },
                {
                    "name": "AI\u672a\u6765",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,103,85)"
                        }
                    }
                },
                {
                    "name": "\u3010\u76c8\u5cf0\u79d1\u6280\u3011\u730e\u5934\u804c\u4f4d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,69,127)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u533b\u7597",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,89,62)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u901f\u63d0\u5347",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,101,138)"
                        }
                    }
                },
                {
                    "name": "\u4e8b\u4e1a\u7f16\u5236",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,144,80)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u9879\u76ee",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,53,65)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u6280\u672f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,127,53)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u4e1a\u7684\u56e2\u961f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,39,56)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u6f5c\u529b\u5927",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,124,6)"
                        }
                    }
                },
                {
                    "name": "\u5305\u4f4f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,102,122)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u9614\u53d1\u5c55\u7a7a\u95f4",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,154,17)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u6280\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,136,87)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5348\u665a\u9910",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,62,157)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u5927\u725b\u591a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,75,107)"
                        }
                    }
                },
                {
                    "name": "\u5782\u76f4\u7535\u5546",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,151,35)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4open",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,106,139)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u91d12-6\u4e2a\u6708",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,114,122)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u5047",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,139,43)"
                        }
                    }
                },
                {
                    "name": "\u300e\u77f3\u5934\u79d1\u6280\u300f\u730e\u5934\u804c\u4f4d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,65,70)"
                        }
                    }
                },
                {
                    "name": "\u73af\u5883\u8212\u9002",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,68,9)"
                        }
                    }
                },
                {
                    "name": "\u8bf1\u4eba\u798f\u5229",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,41,23)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u5e7f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,159,136)"
                        }
                    }
                },
                {
                    "name": "\u521b\u65b0\u56e2\u961f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,124,49)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u5e74\u4e0a\u6d77\u843d\u6237",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,12,143)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u5956\u91d1+\u80a1\u6743/\u671f\u6743\u6fc0\u52b1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,0,155)"
                        }
                    }
                },
                {
                    "name": "k12\u6559\u80b2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,125,136)"
                        }
                    }
                },
                {
                    "name": "\u5305\u9910",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,4,102)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u91d1+\u5b63\u5ea6\u5956\u91d1+\u597d\u5fc3\u60c5+\u798f\u5229\u591a\u591a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,66,16)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u6587\u5316\u597d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,151,26)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u7a7a\u95f4\u5927\u3002",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,46,7)"
                        }
                    }
                },
                {
                    "name": "\u725b\u4eba\u5171\u4e8b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,24,150)"
                        }
                    }
                },
                {
                    "name": "\u5168\u989d\u793e\u4fdd\u516c\u79ef\u91d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,135,156)"
                        }
                    }
                },
                {
                    "name": "\u7814\u53d1\u6c1b\u56f4\u4ff1\u4f73",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,33,117)"
                        }
                    }
                },
                {
                    "name": "\u5404\u9879\u8865\u8d34",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,21,142)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u7a7a\u95f4\u5145\u6ee1\u60f3\u8c61",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,156,38)"
                        }
                    }
                },
                {
                    "name": "\u9910\u8865\u4ea4\u8865",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,68,145)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6d3b\u52a8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,118,146)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u6253\u5361",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,11,119)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u96f6\u98df",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,136,144)"
                        }
                    }
                },
                {
                    "name": "**\u56e2\u961f+\u53d1\u5c55\u7a7a\u95f4\u5927",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,45,31)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u80fd\u529b\u5f3a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,78,79)"
                        }
                    }
                },
                {
                    "name": "\u524d\u6cbf\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,26,117)"
                        }
                    }
                },
                {
                    "name": "\u540d\u6821\u540d\u4f01",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,31,52)"
                        }
                    }
                },
                {
                    "name": "\u524d\u6cbf\u884c\u4e1a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,110,97)"
                        }
                    }
                },
                {
                    "name": "\u529e\u516c\u6c1b\u56f4\u597d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,64,12)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u56e2\u961f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,138,92)"
                        }
                    }
                },
                {
                    "name": "\u7a33\u5b9a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,83,128)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u6e38\u6216\u6237\u5916\u62d3\u5c55\u57f9\u8bad",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,118,63)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u5236\u5ea6",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,98,69)"
                        }
                    }
                },
                {
                    "name": "AI+\u6559\u80b2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,9,24)"
                        }
                    }
                },
                {
                    "name": "\u6ef4\u6ef4\u6253\u8f66",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,51,16)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6d3b\u529b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,65,95)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u4e30\u539a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,95,109)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u4e1a\u6280\u80fd\u8fc5\u901f\u63d0\u5347",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,102,113)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u8d85\u597d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,123,111)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u4f73",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,152,128)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u9645\u5316",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,3,87)"
                        }
                    }
                },
                {
                    "name": "\u8282\u5047\u65e5\u798f\u5229\u7b49",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,52,0)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u65b0\u9896",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,36,121)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u798f\u5229\u4f18\u539a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,37,7)"
                        }
                    }
                },
                {
                    "name": "\u660e\u661f\u56e2\u961f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,79,33)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u524d\u666f\u597d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,84,144)"
                        }
                    }
                },
                {
                    "name": "\u52a0\u73ed\u5c11",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,150,76)"
                        }
                    }
                },
                {
                    "name": "\u901a\u8baf\u6d25\u8d34",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,112,2)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u85aa",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,17,105)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u667a\u80fd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,128,46)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u6838\u5fc3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,13,64)"
                        }
                    }
                },
                {
                    "name": "\u5927\u7528\u6237\u91cf",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,118,31)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u8f7b\u6d3b\u529b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,1,77)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u798f\u5229\u597d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,67,56)"
                        }
                    }
                },
                {
                    "name": "\u91cd\u70b9\u673a\u6784",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,160,23)"
                        }
                    }
                },
                {
                    "name": "2-6\u4e2a\u6708\u5e74\u7ec8\u5956",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,118,26)"
                        }
                    }
                },
                {
                    "name": "\u7845\u8c37\u5927\u725b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,20,50)"
                        }
                    }
                },
                {
                    "name": "\u4f01\u4e1a\u6c1b\u56f4\u7b80\u5355",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,126,52)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u5973\u591a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,86,68)"
                        }
                    }
                },
                {
                    "name": "\u6625\u8282\u957f\u5047",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,58,15)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u98df",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,104,116)"
                        }
                    }
                },
                {
                    "name": "\u524d\u666f\u884c\u4e1a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,133,35)"
                        }
                    }
                },
                {
                    "name": "\u5c97\u4f4d\u53d1\u5c55\u597d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,125,65)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u524d\u6cbf",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,152,143)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u8fdc\u7a0b\u529e\u516c",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,4,61)"
                        }
                    }
                },
                {
                    "name": ".",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,103,102)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u665a\u9910",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,4,46)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u725b\u6307\u5bfc",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,92,71)"
                        }
                    }
                },
                {
                    "name": "\u9760\u8c31\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,76,21)"
                        }
                    }
                },
                {
                    "name": "\u6709\u671f\u6743",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,30,64)"
                        }
                    }
                },
                {
                    "name": "\u6709\u53d1\u5c55\u673a\u4f1a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,90,103)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u63d0\u5347",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,34,52)"
                        }
                    }
                },
                {
                    "name": "\u4f53\u68c0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,78,67)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u67b6\u6784",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,107,159)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u60278\u5c0f\u65f6",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,133,100)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u98df\u5bbf",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,43,51)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5496\u4e91\u96c6",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,154,99)"
                        }
                    }
                },
                {
                    "name": "\u6280\u80fd\u63d0\u5347",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,88,53)"
                        }
                    }
                },
                {
                    "name": "\u672a\u6765\u53ef\u671f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,49,76)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6c1b\u56f4\u6d53",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,110,45)"
                        }
                    }
                },
                {
                    "name": "\u6311\u6218\u5927",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,43,97)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5b8c\u5584",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,5,43)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u671f\u57f9\u8bad",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,48,134)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u8d28\u56e2\u961f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,129,40)"
                        }
                    }
                },
                {
                    "name": "\u5468\u672b\u4e0d\u52a0\u73ed",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,55,10)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u65e0\u9650",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,75,122)"
                        }
                    }
                },
                {
                    "name": "\u51c6\u5907\u4e0a\u5e02",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,144,74)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u6709\u524d\u666f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,99,53)"
                        }
                    }
                },
                {
                    "name": "\u8f66\u5382\u5408\u4f5c",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,45,134)"
                        }
                    }
                },
                {
                    "name": "\u5177\u6709\u7ade\u4e89\u529b\u7684\u85aa\u8d44\u6c34\u5e73",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,87,140)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u524d\u666f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,103,65)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u8f6f\u521b\u4e1a\u56e2\u961f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,30,43)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44OPEN",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,21,68)"
                        }
                    }
                },
                {
                    "name": "\u73ed\u8f66\u63a5\u9001",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,109,106)"
                        }
                    }
                },
                {
                    "name": "\u6bcf\u534a\u5e74\u8c03\u85aa\u4e00\u6b21",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,54,90)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u6e38\u57fa\u91d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,139,74)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5047\u591a\u591a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,78,49)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u725b\u56e2\u961f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,69,112)"
                        }
                    }
                },
                {
                    "name": "\u98df\u5802",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,56,13)"
                        }
                    }
                },
                {
                    "name": "AI\u91d1\u878d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,115,106)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u9f99\u5934",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,54,32)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,53,7)"
                        }
                    }
                },
                {
                    "name": "\u826f\u597d\u7684\u6280\u672f\u6c1b\u56f4",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,130,75)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u522b\u5885\u5de5\u4f5c\u4e0e\u4f4f\u5bbf\u73af\u5883",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,0,74)"
                        }
                    }
                },
                {
                    "name": "\u6301\u724c\u673a\u6784",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,126,126)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u5168\u9762",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,71,36)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5e95\u5956\u91d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,52,21)"
                        }
                    }
                },
                {
                    "name": "\u660e\u661f\u4ea7\u54c1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,125,113)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u5021\u8ffd\u6c42\u5353\u8d8a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,99,160)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1\u798f\u5229\u5b8c\u5584",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,107,138)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5206\u7ea2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,56,132)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4\u4f73",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,66,54)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6241\u5e73\u5316",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,100,78)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u85aa+\u80a1\u6743",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,107,144)"
                        }
                    }
                },
                {
                    "name": "\u524d\u666f\u53ef\u89c2\u3002",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,147,79)"
                        }
                    }
                },
                {
                    "name": "\u8f6c\u6b63\u673a\u4f1a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,59,89)"
                        }
                    }
                },
                {
                    "name": "3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,124,109)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u9ad8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,149,150)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u6280\u672f\u9886\u5148",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,50,62)"
                        }
                    }
                },
                {
                    "name": "\u6d25\u8d34\u8865\u52a9",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,119,98)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u901a\u9053\u5b8c\u5584",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,103,119)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u798f\u5229\u597d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,158,109)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5382\u80cc\u666f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,9,17)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u540d\u4f01\u4e1a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,101,7)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u597d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,9,145)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u5e76\u53d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,94,70)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u7a33\u5b9a+\u6210\u957f\u664b\u5347+\u6280\u672f\u9a71\u52a8+\u80a1\u7968\u6fc0\u52b1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,86,60)"
                        }
                    }
                },
                {
                    "name": "\u6e05\u534e\u6d77\u5f52\u56e2\u961f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,12,156)"
                        }
                    }
                },
                {
                    "name": "\u7a33\u5b9a\u6027\u597d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,89,72)"
                        }
                    }
                },
                {
                    "name": "\u6025\u901f\u6210\u957f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,79,18)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u4f18\u539a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,117,127)"
                        }
                    }
                },
                {
                    "name": "\u73af\u5883\u4f18\u7f8e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,134,38)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u53d1\u5c55\u6f5c\u529b\u5927",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,123,6)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u673a\u5236",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,123,25)"
                        }
                    }
                },
                {
                    "name": "\u5404\u79cd\u8865\u8d34",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,110,153)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u9910",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,74,23)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u665a\u9910",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,126,87)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u7ebf\u6e38\u620f\u5927\u5382",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,115,71)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51\u533b\u7597\u9886\u5934\u7f8a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,50,54)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u65c5\u6e38\u4e0b\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,112,70)"
                        }
                    }
                },
                {
                    "name": "\u6709\u671f\u6743\u6388\u4e88",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,85,151)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u5f39\u6027",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,54,115)"
                        }
                    }
                },
                {
                    "name": "\u767e\u4ebf\u7f8e\u91d1\u4f30\u503c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,154,117)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u9650\u6210\u957f\uff01",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,46,102)"
                        }
                    }
                },
                {
                    "name": "\u963f\u91cc\u7cfb\u77e5\u540d\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,95,33)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u79c0\u7684\u6280\u672f\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,156,132)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u5f85\u9047\u5f88\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,42,117)"
                        }
                    }
                },
                {
                    "name": "\u878d\u8d44\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,139,51)"
                        }
                    }
                },
                {
                    "name": "\u73af\u5883\u5bbd\u677e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,117,16)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u5f88\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,65,125)"
                        }
                    }
                },
                {
                    "name": "\u5341\u56db\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,15,64)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u4f19\u4f34\u4f18\u79c0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,7,47)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u7814\u548c\u5e94\u7528\u7ed3\u5408",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,26,112)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u53d1\u5c55\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,155,33)"
                        }
                    }
                },
                {
                    "name": "\u8bdd\u8865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,11,111)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u534f\u52a9\u843d\u6237",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,98,135)"
                        }
                    }
                },
                {
                    "name": "\u767e\u4eba\u6280\u672f\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,96,115)"
                        }
                    }
                },
                {
                    "name": "\u805a\u9910\u56e2\u5efa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,48,151)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u5bcc\u9879\u76ee\u7ecf\u9a8c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,111,5)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f\u671f\u521b\u4e1a\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,147,123)"
                        }
                    }
                },
                {
                    "name": "\u597d\u7684\u5f00\u53d1\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,26,121)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5916\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,155,110)"
                        }
                    }
                },
                {
                    "name": "\u751f\u4fe1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,107,92)"
                        }
                    }
                },
                {
                    "name": "\u5173\u952e\u5c97\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,134,82)"
                        }
                    }
                },
                {
                    "name": "\u65e0007",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,45,56)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u8d44\u6df1\u5e26\u961f\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,95,123)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u524d\u666f\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,16,71)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e24\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,14,141)"
                        }
                    }
                },
                {
                    "name": "\u5927\u578b\u8de8\u5883\u7535\u5546",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,82,126)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u901f\u6210\u957f/\u5e74\u7ec8\u5956\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,119,94)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u53d1\u5c55\u524d\u666f\u5e7f\u9614",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,132,92)"
                        }
                    }
                },
                {
                    "name": "\u8865\u5145\u533b\u7597\u7b49",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,65,139)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u9645\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,119,129)"
                        }
                    }
                },
                {
                    "name": "\u4e03\u9669\u4e8c\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,32,28)"
                        }
                    }
                },
                {
                    "name": "2\u5e74\u7ecf\u9a8c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,94,158)"
                        }
                    }
                },
                {
                    "name": "\u7532\u65b9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,46,126)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u73af\u7ed5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,97,43)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6c1b\u56f4\u5f00\u653e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,25,94)"
                        }
                    }
                },
                {
                    "name": "AI\u5f71\u50cf\u9886\u57df\u72ec\u89d2\u517d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,128,104)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u5927\u725b\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,29,139)"
                        }
                    }
                },
                {
                    "name": "\u4ebf\u7ea7\u6570\u636e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,99,11)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u6210\u7acb\u4eba\u5de5\u667a\u80fd\u4e0e\u5927\u6570\u636e\u90e8\u95e8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,106,38)"
                        }
                    }
                },
                {
                    "name": "\u5173\u6ce8\u5458\u5de5\u53d1\u5c55",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,59,110)"
                        }
                    }
                },
                {
                    "name": "\u8682\u8681\u63a7\u80a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,86,148)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5b9e\u529b\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,53,144)"
                        }
                    }
                },
                {
                    "name": "\u53ea\u8981\u8db3\u591f\u4f18\u79c0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,119,13)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f\u673a\u4f1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,31,93)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5382\u4f18\u79c0\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,9,5)"
                        }
                    }
                },
                {
                    "name": "\u6e05\u534e\u5927\u5b66\u7684\u667a\u80fd\u8fd0\u7ef4\u5b9e\u9a8c\u5ba4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,20,25)"
                        }
                    }
                },
                {
                    "name": "\u62e5\u6709TB\u7ea7\u6570\u636e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,74,3)"
                        }
                    }
                },
                {
                    "name": "1~\u221e\u9ad8\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,137,70)"
                        }
                    }
                },
                {
                    "name": "\u826f\u597d\u7684\u6210\u957f\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,64,45)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,37,144)"
                        }
                    }
                },
                {
                    "name": "\u98df\u54c1\u996e\u6599",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,86,44)"
                        }
                    }
                },
                {
                    "name": "\u6f5c\u529b\u5de8\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,56,99)"
                        }
                    }
                },
                {
                    "name": "\u5ba2\u6237\u8986\u76d6\u591a\u5bb6\u4e00\u7ebf\u5de8\u5934\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,94,110)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,6,21)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u524d\u666f\u53ef\u89c2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,151,12)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u578b\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,50,139)"
                        }
                    }
                },
                {
                    "name": "F\u8f6e\u878d\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,49,46)"
                        }
                    }
                },
                {
                    "name": "\u6d59\u5927\u80cc\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,64,37)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4\u8d85\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,119,101)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u53d1\u5c55\u5feb\u901f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,110,23)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u6210\u957f\u6027",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,39,18)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u4e0d\u6253\u5361",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,149,23)"
                        }
                    }
                },
                {
                    "name": "\u843d\u5730\u573a\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,3,158)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u516d\u9669\u4e00\u91d1\u996d\u8d34\u8f66\u8d34\u7ee9\u6548\u5956\u5b9a\u671f\u4f53\u68c0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,11,34)"
                        }
                    }
                },
                {
                    "name": "\u524d\u9014\u9886\u57df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,16,146)"
                        }
                    }
                },
                {
                    "name": "\u6709\u80a1\u6743",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,41,110)"
                        }
                    }
                },
                {
                    "name": "\u5916\u4f01\u98ce",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,121,136)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u6b23\u6b23\u5411\u8363",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,29,94)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u85aa\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,99,23)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u524d\u666f\u4f73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,143,39)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u5e74\u5047\u75c5\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,50,84)"
                        }
                    }
                },
                {
                    "name": "AI\u667a\u6167\u6559\u80b2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,11,58)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1\u4e00\u6863",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,106,42)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u9f84\u5956",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,133,109)"
                        }
                    }
                },
                {
                    "name": "\u771f\u5b9e\u7684\u9879\u76ee\u6311\u6218\u4e0e\u5386\u7ec3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,86,56)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u56e2\u961f\u80fd\u529b\u4f18\u79c0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,48,92)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u4f18\u79c0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,82,72)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6167\u57ce\u5e02",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,13,51)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u6c11\u7ea7\u5e94\u7528",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,57,18)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51\u51fa\u6d77\u4f01\u4e1a\u6807\u6746",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,74,73)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u8f7b\u6241\u5e73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,153,140)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,74,136)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u4e00\u6d41",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,132,64)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u901f\u589e\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,18,45)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u524d\u666f\u5e7f\u9614",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,85,152)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6e90\u5e73\u53f0\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,91,64)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u805a\u7126",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,67,136)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u540d\u5934\u90e8\u4e92\u8054\u7f51\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,126,121)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5382\u7ecf\u9a8c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,88,60)"
                        }
                    }
                },
                {
                    "name": "\u7eaf\u6280\u672f\u80cc\u4e66\u7684\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,159,89)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4\u6d3b\u6cfc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,143,85)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u5e7f\u544a\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,104,110)"
                        }
                    }
                },
                {
                    "name": "\u548c\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,33,81)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7\u72ec\u89d2\u517d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,72,15)"
                        }
                    }
                },
                {
                    "name": "\u5bfc\u5e08\u4e00\u5e26\u4e00",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,144,62)"
                        }
                    }
                },
                {
                    "name": "\u52a0\u73ed\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,80,25)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u597d\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,16,12)"
                        }
                    }
                },
                {
                    "name": "\u90e8\u95e8\u4f18\u80dc\u5956",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,94,120)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u8f6f\u591a\u5e74\u670d\u52a1\u80cc\u666f\u6280\u672f\u5927\u62ff\u4eb2\u81ea\u5e26\u6559\u57f9\u8bad",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,56,36)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u4f01\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,50,75)"
                        }
                    }
                },
                {
                    "name": "\u521b\u9020\u524d\u6cbfAI\u4ea7\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,140,36)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u53ef\u89c2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,136,67)"
                        }
                    }
                },
                {
                    "name": "\u6ca1\u6709KPI",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,47,14)"
                        }
                    }
                },
                {
                    "name": "\u7814\u7a76\u548c\u5b9e\u9645\u5e94\u7528\u7ed3\u5408",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,6,21)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f\u6311\u6218\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,122,5)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u914d\u7f6e\u671f\u6743",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,81,63)"
                        }
                    }
                },
                {
                    "name": "DevOps",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,37,101)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u5047\u671f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,91,98)"
                        }
                    }
                },
                {
                    "name": "\u6da6\u8054\uff08\u730e\u5934\uff09",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,74,25)"
                        }
                    }
                },
                {
                    "name": "\u7d27\u6025",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,156,10)"
                        }
                    }
                },
                {
                    "name": "\u6fc0\u52b1\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,145,58)"
                        }
                    }
                },
                {
                    "name": "D\u8f6e\u6f5c\u529b\u80a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,93,82)"
                        }
                    }
                },
                {
                    "name": "\u6559\u80b2\u57f9\u8bad",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,54,41)"
                        }
                    }
                },
                {
                    "name": "\u672a\u6765\u770b\u597d\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,26,20)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u63d0\u6210",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,62,156)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4\u68d2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,84,8)"
                        }
                    }
                },
                {
                    "name": "ai\u7b97\u6cd5\u5728\u4f9b\u5e94\u94fe\u548c\u7269\u6d41\u9886\u57df\u7684\u5e94\u7528",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,110,160)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u65b0\u65b9\u5411",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,152,17)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6280\u672f\u5927\u5496\u4e91\u96c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,118,20)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6316\u6398\u5de5\u7a0b\u5e08",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,106,67)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u5927\u725b\u5e26\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,121,8)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u5927\u725b\u4e91\u96c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,2,60)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u5b66\u5bb6\u5927\u725b\u5e26\u961f\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,20,57)"
                        }
                    }
                },
                {
                    "name": "\u67b6\u6784\u6241\u5e73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,68,9)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u9614\u7a7a\u95f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,141,8)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u5e73\u53f0\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,26,108)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u5bcc\u7684\u516c\u53f8\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,41,28)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,95,47)"
                        }
                    }
                },
                {
                    "name": "\u6709\u673a\u4f1a\u517c\u4efb\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,113,143)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u9ad8P",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,21,90)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u6c1b\u56f4\u548c\u8c10",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,66,45)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u5b8c\u5584",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,153,13)"
                        }
                    }
                },
                {
                    "name": "\u5404\u79cd\u4e0b\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,12,35)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u65b0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,60,27)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1/\u9910\u8865/\u7ee9\u6548\u5956\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,38,43)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u666f\u529e\u516c\u697c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,152,107)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u5f02\u8005\u53ef\u8f6c\u6821\u62db\u6b63\u5f0f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,94,85)"
                        }
                    }
                },
                {
                    "name": "\u8ddf\u725b\u4eba\u4e00\u8d77\u5de5\u4f5c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,133,129)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u534f\u4f5c\u529b\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,160,4)"
                        }
                    }
                },
                {
                    "name": "\u840c\u5ba0\u5f85\u64b8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,47,119)"
                        }
                    }
                },
                {
                    "name": "\u9f13\u52b1\u81ea\u6211\u5b66\u4e60",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,82,97)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u4ea4\u4e92",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,48,113)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5b9e\u529b\u96c4\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,149,155)"
                        }
                    }
                },
                {
                    "name": "\u6253\u9020\u4e16\u754c**\u7684\u6df7\u6c8c\u5de5\u7a0b\u4e50\u56ed",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,87,8)"
                        }
                    }
                },
                {
                    "name": "\u5982\u679c\u4f60\u6b63\u5728\u8ffd\u68a6\u7684\u8def\u4e0a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,139,47)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u53d1\u5c55\u5f85\u9047\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,75,130)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79\u5b66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,105,113)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u9614\u51ed\u9c7c\u8dc3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,156,134)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u5927\u6570\u636e\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,149,0)"
                        }
                    }
                },
                {
                    "name": "\u52a0\u73ed\u53cc\u500d\u5de5\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,107,29)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u665a\u9910\u4e0b\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,142,159)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u671f\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,91,23)"
                        }
                    }
                },
                {
                    "name": "E\u8f6e\u878d\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,55,60)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u672f\u548c\u5de5\u4f5c\u80cc\u666f\u725b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,18,94)"
                        }
                    }
                },
                {
                    "name": "2012\u5b9e\u9a8c\u5ba4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,103,117)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a**\u72ec\u89d2\u517d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,12,7)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u7efc\u5408\u7d20\u8d28\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,55,77)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4nice",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,44,58)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u65b0\u6280\u672f\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,21,151)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6280\u672f\u6c1b\u56f4\u6d53\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,90,135)"
                        }
                    }
                },
                {
                    "name": "\u8282\u65e5\u798f\u5229\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,30,45)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u8f7b\u677e\u6709\u7231",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,60,9)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u98df\u5802",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,55,119)"
                        }
                    }
                },
                {
                    "name": "3\u4f4d\u535a\u58eb\u751f\u5bfc\u5e08\u6302\u5e05\u7684\u79d1\u5b66\u5bb6\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,80,157)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u6587\u5316\u56e2\u961fnice",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,153,45)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u9645\u5316\u6c1b\u56f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,140,63)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u725b\u7684\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,36,29)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,91,79)"
                        }
                    }
                },
                {
                    "name": "\u9886\u5bfc\u8d85\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,105,65)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u7fd8\u695a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,82,29)"
                        }
                    }
                },
                {
                    "name": "\u6bd4\u80a9BAT\u7684\u85aa\u916c\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,77,132)"
                        }
                    }
                },
                {
                    "name": "\u505a\u6700\u524d\u6cbf\u7684\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,66,32)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u4e0d\u9519",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,48,31)"
                        }
                    }
                },
                {
                    "name": "\u521b\u4e1a\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,141,40)"
                        }
                    }
                },
                {
                    "name": "\u5305\u9910\u53cc\u4f11\u4e0d\u6253\u5361",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,29,130)"
                        }
                    }
                },
                {
                    "name": "\u767e\u4ebf\u72ec\u89d2\u517d\u4e92\u8054\u7f51\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,107,124)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u901f\u53d1\u5c55\u4e2d\u7684\u521b\u4e1a\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,135,57)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u540c\u4e8b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,32,63)"
                        }
                    }
                },
                {
                    "name": "\u77ed\u89c6\u9891",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,118,22)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u5316\u5f15\u64ce\u7684\u7cfb\u7edf\u67b6\u6784",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,121,46)"
                        }
                    }
                },
                {
                    "name": "\u673a\u52a8\u7075\u6d3b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,94,15)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u79c0\u7684\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,47,27)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u989d\u9910\u8865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,52,123)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u7a33\u5b9a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,6,62)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u5e26\u961f\uff01\uff01",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,102,141)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5065\u8eab/\u96f6\u98df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,111,70)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5e95\u591a\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,11,105)"
                        }
                    }
                },
                {
                    "name": "\u5165\u804c\u7f34\u7eb3\u4e94\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,85,139)"
                        }
                    }
                },
                {
                    "name": "\u7ba1\u7406\u6241\u5e73\u900f\u660e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,37,50)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u53d1\u5c55\u7a7a\u95f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,137,70)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u9510\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,117,55)"
                        }
                    }
                },
                {
                    "name": "\u5168\u989d\u793e\u4fdd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,51,56)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u957f\u5047\u671f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,136,9)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u98df\u4e0b\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,75,93)"
                        }
                    }
                },
                {
                    "name": "\u5f88\u6709\u524d\u666f\u7684\u90e8\u95e8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,32,7)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u798f\u5229\u4f18\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,92,55)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1/\u5e74\u5e95\u53cc\u85aa/\u7ee9\u6548\u5956\u91d1/\u5b9a\u671f\u4f53\u68c0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,55,119)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u798f\u5229\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,17,1)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u4e8b\u4e1a\u90e8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,40,135)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5c0f\u5468",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,142,34)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u9910\u4e0b\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,63,69)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6167\u533b\u7597",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,131,152)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4Nice",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,94,56)"
                        }
                    }
                },
                {
                    "name": "\u6b22\u8fce\u52a0\u5165",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,47,111)"
                        }
                    }
                },
                {
                    "name": "\u57f9\u8bad",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,103,84)"
                        }
                    }
                },
                {
                    "name": "\u6587\u5316\u548c\u81ea\u7531\u5f00\u53d1\u6c1b\u56f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,91,9)"
                        }
                    }
                },
                {
                    "name": "\u5168\u6808\u6280\u672f\u5927\u725b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,32,152)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u7a33\u5b9a\u5feb\u901f\u589e\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,155,98)"
                        }
                    }
                },
                {
                    "name": "Geek\u6587\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,36,132)"
                        }
                    }
                },
                {
                    "name": "\u805a\u4e00\u7fa4\u6709\u60c5\u4e49\u7684\u4eba\u505a\u6210\u6709\u610f\u4e49\u7684\u4e8b\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,53,135)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f\u673a\u4f1a\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,45,159)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5a92\u4f53",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,104,143)"
                        }
                    }
                },
                {
                    "name": "\u725b\u4eba\u4e91\u96c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,92,95)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u672f\u548c\u5e94\u7528\u7ed3\u5408",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,0,141)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u673a\u4f1a\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,134,132)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u7b97\u6cd5\u4e13\u5bb6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,67,85)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5e74\u8f7b\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,97,148)"
                        }
                    }
                },
                {
                    "name": "\u5f3a\u5927\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,127,130)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u5185\u4ea7\u54c1\u5f71\u54cd\u529b\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,55,69)"
                        }
                    }
                },
                {
                    "name": "\u5b9e\u73b0\u521b\u65b0\u6280\u672f\u9a71\u52a8\u7269\u6d41\u884c\u4e1a\u5347\u7ea7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,117,52)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u4f11",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,74,16)"
                        }
                    }
                },
                {
                    "name": "\u7aef\u70b9\u7f51\u7edc\u730e\u5934\u804c\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,114,106)"
                        }
                    }
                },
                {
                    "name": "\u8865\u5145\u5e74\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,101,159)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u9ad8\u7cbe\u5c16\u4eba\u624d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,91,85)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u53d1\u5c55\u5feb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,83,62)"
                        }
                    }
                },
                {
                    "name": "\u6700\u5177\u60f3\u8c61\u529b\u7684\u8d5b\u9053",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,109,159)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5347\u7a7a\u95f4\u5de8\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,4,47)"
                        }
                    }
                },
                {
                    "name": "\u5177\u6709\u5e02\u573a\u7ade\u4e89\u529b\u7684\u85aa\u916c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,42,151)"
                        }
                    }
                },
                {
                    "name": "\u7cbe\u6e5b\u7684\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,112,13)"
                        }
                    }
                },
                {
                    "name": "\u6709\u66f4\u9ad8\u66f4\u5927\u7684\u53d1\u5c55\u524d\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,82,111)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u673a\u4f1a\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,58,125)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5eb7\u5a01\u89c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,94,105)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u63a8\u8350",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,130,0)"
                        }
                    }
                },
                {
                    "name": "\u5956\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,93,49)"
                        }
                    }
                },
                {
                    "name": "\u9886\u5bfc\u6c1b\u56f4\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,5,27)"
                        }
                    }
                },
                {
                    "name": "\u5168\u5458mac",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,12,98)"
                        }
                    }
                },
                {
                    "name": "16\u85aa\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,57,18)"
                        }
                    }
                },
                {
                    "name": "undefined",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,42,110)"
                        }
                    }
                },
                {
                    "name": "***\u5b9e\u9a8c\u5ba4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,39,81)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u884c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,7,126)"
                        }
                    }
                },
                {
                    "name": "\u5305\u5403\u5305\u4f4f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,94,21)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u53d1\u5c55\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,130,74)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u7a33\u5b9a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,43,6)"
                        }
                    }
                },
                {
                    "name": "\u5404\u79cd\u56e2\u5efa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,49,100)"
                        }
                    }
                },
                {
                    "name": "\u5343\u4e07\u7ea7\u7528\u6237",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,106,57)"
                        }
                    }
                },
                {
                    "name": "\u8d70\u5728\u7b97\u6cd5\u524d\u6cbf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,37,131)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u4e1a\u52a1\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,110,106)"
                        }
                    }
                },
                {
                    "name": "\u6cd5\u5b9a\u8282\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,20,2)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u5efa\u65c5\u6e38",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,1,35)"
                        }
                    }
                },
                {
                    "name": "\u5b9e\u529b\u592e\u4f01",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,61,12)"
                        }
                    }
                },
                {
                    "name": "\u5f00\u653e\u81ea\u7531",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,28,152)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u5e7416\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,3,109)"
                        }
                    }
                },
                {
                    "name": "\u6709\u7b97\u6cd5\u5927\u725b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,70,148)"
                        }
                    }
                },
                {
                    "name": "\u6709\u5e02\u573a\u7ade\u4e89\u529b\u7684\u85aa\u916c\u5f85\u9047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,84,52)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1(\u6700\u9ad8\u6bd4\u4f8b)",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,149,123)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956+\u53cc\u4f11+\u516d\u9669\u4e00\u91d1+\u665a\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,139,79)"
                        }
                    }
                },
                {
                    "name": "\u6e05\u534e\u7814\u7a76\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,50,65)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5f52\u79d1\u7814\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,83,39)"
                        }
                    }
                },
                {
                    "name": "5\u59297\u5c0f\u65f6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,122,59)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u671f\u65c5\u6e38",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,47,125)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u5bcc\u4e0b\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,10,6)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,152,75)"
                        }
                    }
                },
                {
                    "name": "\u91cd\u65b0\u5b9a\u4e49\u884c\u4e1a\u89c4\u5219",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,23,65)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u4e13\u5bb6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,16,148)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6709\u5927\u725b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,114,62)"
                        }
                    }
                },
                {
                    "name": "\u521b\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,61,89)"
                        }
                    }
                },
                {
                    "name": "\u4f4f\u623f\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,49,100)"
                        }
                    }
                },
                {
                    "name": "\u6d41\u91cf\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,42,141)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u5316\u7ba1\u7406\u5de5\u4f5c\u6c1b\u56f4\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,122,11)"
                        }
                    }
                },
                {
                    "name": "\u80a1\u4e1c\u80cc\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,92,149)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u96f6\u552e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,71,42)"
                        }
                    }
                },
                {
                    "name": "AI\u533b\u7597\u9886\u57df\u72ec\u89d2\u517d\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,32,103)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u81ea\u7531",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,124,84)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u9a7e\u9a76",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,130,113)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c\u6fc0\u52b1\u8ba1\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,59,77)"
                        }
                    }
                },
                {
                    "name": "\u91cd\u70b9\u6295\u5165",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,19,119)"
                        }
                    }
                },
                {
                    "name": "\u533a\u5757\u94fe\u77ff\u4e1a\u9879\u76ee\u6709\u524d\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,159,99)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u4e60\u673a\u4f1a\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,144,81)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u9650\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,20,41)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u6c1b\u56f4\u597d\uff01",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,53,52)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c\u798f\u5229\u4f18",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,89,83)"
                        }
                    }
                },
                {
                    "name": "\u6559\u80b2\u9879\u76ee\u6709\u524d\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,124,42)"
                        }
                    }
                },
                {
                    "name": "\u826f\u597d\u7684\u53d1\u5c55\u524d\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,62,34)"
                        }
                    }
                },
                {
                    "name": "\u6709\u7ade\u4e89\u529b\u7684\u85aa\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,12,42)"
                        }
                    }
                },
                {
                    "name": "\u73af\u5883open",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,79,114)"
                        }
                    }
                },
                {
                    "name": "\u5168\u7403\u5316\u4eba\u5de5\u667a\u80fd\u4ea7\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,141,41)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u6e20\u9053\u901a\u7545",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,47,77)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u539a\u5e74\u7ec8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,66,120)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,27,75)"
                        }
                    }
                },
                {
                    "name": "\u6548\u76ca\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,12,25)"
                        }
                    }
                },
                {
                    "name": "\u5b5d\u987a\u57fa\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,130,2)"
                        }
                    }
                },
                {
                    "name": "\u8865\u5145\u533b\u7597\u4fdd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,86,152)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u516d\u9669\u4e00\u91d1\u996d\u8d34\u8f66\u8d34\u7ee9\u6548\u5956\u5b9a\u671f\u4f53\u68c0\u805a\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,64,108)"
                        }
                    }
                },
                {
                    "name": "\u5145\u5206\u653e\u6743/\u9ad8\u6311\u6218",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,4,101)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u81ea\u7531\u5ea6\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,139,94)"
                        }
                    }
                },
                {
                    "name": "\u4f01\u4e1a\u5feb\u901f\u6210\u957f\u671f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,79,60)"
                        }
                    }
                },
                {
                    "name": "\u5ba2\u6237\u8986\u76d6\u591a\u5bb6\u4e00\u7ebf\u5de8\u5934",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,57,152)"
                        }
                    }
                },
                {
                    "name": "\u821e\u53f0\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,88,21)"
                        }
                    }
                },
                {
                    "name": "\u9053\u8def\u68c0\u6d4b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,11,69)"
                        }
                    }
                },
                {
                    "name": "\u805a\u7126\u524d\u6cbf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,51,98)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u5927\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,95,151)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u540d\u81ea\u52a8\u9a7e\u9a76\u65b0\u80fd\u6e90\u6c7d\u8f66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,20,152)"
                        }
                    }
                },
                {
                    "name": "\u5927\u516c\u53f8\u5e73\u53f0\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,122,144)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u53e3\u5348\u665a\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,122,16)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u591a\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,45,158)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u53d1\u5c55\u524d\u666f\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,61,106)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u5b9a\u8282\u5047\u65e5\u653e\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,107,23)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e+AI\u672a\u676510\u5e74\u8d8b\u52bf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,144,113)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,7,132)"
                        }
                    }
                },
                {
                    "name": "\u5927\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,48,83)"
                        }
                    }
                },
                {
                    "name": "IBM",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,157,21)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,128,123)"
                        }
                    }
                },
                {
                    "name": "\u7ee9\u6548\u8c03\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,41,21)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,117,43)"
                        }
                    }
                },
                {
                    "name": "\u6cd5\u5b9a\u8282\u5047\u65e5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,64,45)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u9614\u7684\u53d1\u5c55\u524d\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,61,14)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u98df\u5802\u73ed\u8f66\u5065\u8eab\u623f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,126,139)"
                        }
                    }
                },
                {
                    "name": "\u516d\u9669\u4e00\u91d1+\u5e26\u85aa\u5e74\u5047+\u5e74\u7ec8\u5956\u91d1+\u8282\u65e5\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,118,58)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u98df\u4e0b\u5348\u8336outing\u4e0d\u505c\u6b47",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,45,99)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u98df\u4efb\u610f\u5403",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,36,54)"
                        }
                    }
                },
                {
                    "name": "\u5f3a\u6709\u529b\u7684\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,9,30)"
                        }
                    }
                },
                {
                    "name": "\u4e2a\u4eba\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,42,9)"
                        }
                    }
                },
                {
                    "name": "500\u5f3a\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,83,123)"
                        }
                    }
                },
                {
                    "name": "\u4e2a\u4eba\u6210\u957f\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,112,90)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7531\u5f00\u653e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,71,67)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5f52\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,138,55)"
                        }
                    }
                },
                {
                    "name": "\u5065\u8eab\u623f\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,128,44)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1;\u8282\u65e5\u8865\u8d34;\u7ee9\u6548\u5956\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,121,98)"
                        }
                    }
                },
                {
                    "name": "\u65bd\u5c55\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,61,27)"
                        }
                    }
                },
                {
                    "name": "\u524d\u6cbf\u7684\u5e73\u53f0\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,89,58)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u56e2\u961f\u6765\u81ea\u6d59\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,80,124)"
                        }
                    }
                },
                {
                    "name": "\u5168\u5e02\u514d\u8d39\u73ed\u8f66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,152,68)"
                        }
                    }
                },
                {
                    "name": "\u9f13\u52b1\u521b\u65b0\u7684\u5de5\u4f5c\u73af\u5883",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,103,53)"
                        }
                    }
                },
                {
                    "name": "\u6f5c\u529b\u65e0\u9650",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,64,124)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u591a\u6837\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,84,118)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u8bf1\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,96,99)"
                        }
                    }
                },
                {
                    "name": "\u65e5\u6570\u636e\u767e\u4ebf\u7ea7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,114,33)"
                        }
                    }
                },
                {
                    "name": "\u5916\u5305",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,129,54)"
                        }
                    }
                },
                {
                    "name": "\u6709\u5348\u4f11",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,90,94)"
                        }
                    }
                },
                {
                    "name": "\u98df\u5802\u7528\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,136,33)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u98ce\u53e3\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,2,70)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u65c5\u6e38",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,69,158)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u57fa\u5efa\u9886\u57df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,81,21)"
                        }
                    }
                },
                {
                    "name": "\u9910\u8865\u623f\u8865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,50,70)"
                        }
                    }
                },
                {
                    "name": "\u5b5d\u5fc3\u57fa\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,56,153)"
                        }
                    }
                },
                {
                    "name": "\u8fd1\u4e07\u4eba\u89c4\u6a21",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,62,56)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u7814\u80cc\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,107,101)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4\u81ea\u7531",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,36,12)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5408\u4f5c\u878d\u6d3d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,24,135)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u5bcc\u7684\u5458\u5de5\u6d3b\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,41,75)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u524d\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,146,62)"
                        }
                    }
                },
                {
                    "name": "\u6709\u8f83\u597d\u7684\u8d44\u6e90\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,45,43)"
                        }
                    }
                },
                {
                    "name": "B2B\u91d1\u878d\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,139,125)"
                        }
                    }
                },
                {
                    "name": "\u94b1\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,138,39)"
                        }
                    }
                },
                {
                    "name": "\u672a\u6765\u53d1\u5c55\u6f5c\u529b\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,68,69)"
                        }
                    }
                },
                {
                    "name": "\u643a\u624b\u594b\u6597\u672a\u6765\u53ef\u671f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,0,58)"
                        }
                    }
                },
                {
                    "name": "K12\u6559\u80b2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,32,108)"
                        }
                    }
                },
                {
                    "name": "\u878d\u8d44\u8d8510\u4ebf\u7f8e\u5143",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,116,45)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u6e29\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,120,79)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u5f85\u9047\u4f18",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,122,95)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u5185\u5934\u90e8\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,138,44)"
                        }
                    }
                },
                {
                    "name": "GPU\u4e0a\u76f4\u63a5\u505a\u5b9e\u9a8c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,152,37)"
                        }
                    }
                },
                {
                    "name": "\u524d\u6cbf\u9879\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,36,87)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u9910\u996e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,116,153)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c\u6709\u7ade\u4e89\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,108,41)"
                        }
                    }
                },
                {
                    "name": "\u5c11\u52a0\u73ed",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,5,80)"
                        }
                    }
                },
                {
                    "name": "\u521b\u4e1a\u578b\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,46,97)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u4ece0-1\u7684\u8fc7\u7a0b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,24,157)"
                        }
                    }
                },
                {
                    "name": "\u5546\u4e1a\u4fdd\u9669\u7b49\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,145,83)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u6613\u6709\u9053",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,95,79)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u8425\u9500",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,111,103)"
                        }
                    }
                },
                {
                    "name": "BAT\u6280\u672fleader\u4eb2\u81ea\u5e26",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,92,113)"
                        }
                    }
                },
                {
                    "name": "\u529e\u516c\u5ba4\u96f6\u98df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,135,146)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u98de\u901f\u53d1\u5c55",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,137,109)"
                        }
                    }
                },
                {
                    "name": "\u521b\u4e1a\u4eba\u56e2\u961f\u80cc\u666f\u725b\u903c\u548c\u8d44\u672c\u5145\u8db3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,130,118)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u98df\u81ea\u7531",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,15,155)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5ea6\u8c03\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,21,156)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u91d1\u96c4\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,150,145)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u8282\u594f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,77,54)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u53d1\u5c55\u7a7a\u95f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,1,123)"
                        }
                    }
                },
                {
                    "name": "\u8de8\u5883\u5962\u4f88\u54c1\u7535\u5546",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,153,47)"
                        }
                    }
                },
                {
                    "name": "\u91cd\u70b9\u4e1a\u52a1\u5feb\u901f\u53d1\u5c55",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,33,43)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u4e1a\u56fe\u8c31",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,4,61)"
                        }
                    }
                },
                {
                    "name": "\u72ec\u89d2\u517d\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,93,76)"
                        }
                    }
                },
                {
                    "name": "\u90e8\u95e8\u65c5\u6e38",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,7,28)"
                        }
                    }
                },
                {
                    "name": "\u9f13\u52b1\u7814\u7a76\u65b0\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,142,53)"
                        }
                    }
                },
                {
                    "name": "\u8d1f\u8d23\u4eba\u7684\u89d2\u8272",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,10,0)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u989d\u5e74\u7ec8\u5956",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,156,158)"
                        }
                    }
                },
                {
                    "name": "\u5b8c\u5584\u664b\u5347\u673a\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,17,88)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5b9e\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,44,125)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u6da8\u5e45\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,110,141)"
                        }
                    }
                },
                {
                    "name": "AI\u667a\u80fd\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,8,87)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5148\u8fdb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,153,158)"
                        }
                    }
                },
                {
                    "name": "\u6301\u7eed\u521b\u65b0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,149,93)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u65b9\u5f0f\u7075\u6d3b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,46,87)"
                        }
                    }
                },
                {
                    "name": "\u548c\u6709\u8da3\u7684\u4eba\u505a\u6709\u8da3\u7684\u4e8b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,105,156)"
                        }
                    }
                },
                {
                    "name": "\u6f5c\u529b\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,10,86)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u6c1b\u56f4\u878d\u6d3d\u53d1\u5c55\u6f5c\u529b\u5de8\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,111,74)"
                        }
                    }
                },
                {
                    "name": "\u963f\u91cc\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,53,51)"
                        }
                    }
                },
                {
                    "name": "\u8bd5\u7528\u671f\u4ea4\u4e94\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,41,128)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u5185\u9f99\u5934\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,30,22)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4\u4f73\u7b49\u7b49",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,84,159)"
                        }
                    }
                },
                {
                    "name": "\u6625\u8282\u5047\u671f\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,57,77)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u673a\u89c6\u89c9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,87,129)"
                        }
                    }
                },
                {
                    "name": "90\u540e\u5e74\u8f7b\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,69,74)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u53d1\u5c55\u524d\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,103,6)"
                        }
                    }
                },
                {
                    "name": "AI\u573a\u666f\u4e30\u5bcc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,118,17)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,99,127)"
                        }
                    }
                },
                {
                    "name": "\u521b\u65b0\u4e1a\u52a1\u573a\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,62,6)"
                        }
                    }
                },
                {
                    "name": "\u660e\u661f\u8d44\u672c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,145,143)"
                        }
                    }
                },
                {
                    "name": "\u961f\u53cb\u5948\u65af",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,160,122)"
                        }
                    }
                },
                {
                    "name": "\u9633\u5149\u900f\u660e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,41,57)"
                        }
                    }
                },
                {
                    "name": "\u91cd\u70b9\u53d1\u5c55\u7684\u53d8\u73b0\u9879\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,77,15)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u4f18\u52bf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,99,95)"
                        }
                    }
                },
                {
                    "name": "\u5c97\u4f4d\u53d1\u5c55\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,37,86)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,128,101)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u6709\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,80,129)"
                        }
                    }
                },
                {
                    "name": "\u5347\u804c\u52a0\u85aa\u5feb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,131,110)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u91cf\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,76,48)"
                        }
                    }
                },
                {
                    "name": "\u963f\u91cc\u8de8\u5883\u521b\u4e1a\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,86,54)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u5e7f\u9614",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,75,72)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u5496\u4e91\u96c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,122,107)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u8c08\u671f\u6743",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,133,51)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5916\u76f4\u64ad\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,128,89)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u80fd\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,95,68)"
                        }
                    }
                },
                {
                    "name": "\u516c\u5e73\u664b\u5347",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,92,147)"
                        }
                    }
                },
                {
                    "name": "\u5bfc\u5e08nice",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,76,59)"
                        }
                    }
                },
                {
                    "name": "\u8001\u677fNice",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,84,106)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u53d1\u5c55\u8fc5\u901f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,141,48)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u9ad8\u901f\u6210\u957f\u671f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,69,53)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5e74\u8f7b\u6709\u6d3b\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,123,160)"
                        }
                    }
                },
                {
                    "name": "\u5f00\u653e\u578b\u6587\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,110,114)"
                        }
                    }
                },
                {
                    "name": "ROS\u76f8\u5173\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,118,117)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4\u597d\u798f\u5229\u786c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,86,115)"
                        }
                    }
                },
                {
                    "name": "\u725b\u4eba\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,6,47)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u52a8\u578b\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,154,152)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u901f\u7684\u53d1\u5c55\u524d\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,98,53)"
                        }
                    }
                },
                {
                    "name": "\u5496\u5561\u6c34\u679c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,31,56)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u9a71\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,32,66)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,66,91)"
                        }
                    }
                },
                {
                    "name": "\u671f\u6743\u80a1\u6743",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,48,135)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u7a7a\u95f4\u5e7f\u9614",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,117,101)"
                        }
                    }
                },
                {
                    "name": "\u73af\u5883\u4f73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,18,33)"
                        }
                    }
                },
                {
                    "name": "\u6b63\u96c5\u9f7f\u79d1-\u730e\u5934\u804c\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,125,44)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u5e02\u573a\u6f5c\u529b\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,141,37)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u901f\u664b\u5347\u7684\u804c\u573a\u673a\u4f1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,86,27)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u5e26\u961f\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,50,95)"
                        }
                    }
                },
                {
                    "name": "\u6765\u8fd9\u91cc\u4e00\u8d77\u5f00\u62d3\u4e0d\u4e00\u6837\u7684\u4eba\u751f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,153,72)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u5feb\u901f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,20,157)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5b9e\u529b\u5f3a\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,20,67)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4\u6781\u4f73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,5,139)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4\u878d\u6d3d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,126,118)"
                        }
                    }
                },
                {
                    "name": "\u76c8\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,77,28)"
                        }
                    }
                },
                {
                    "name": "\u5916\u4f01\u98ce\u683c\u7b49",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,119,116)"
                        }
                    }
                },
                {
                    "name": "bat\u5927\u725b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,82,87)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4\u5411\u4e0a\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,97,119)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u9886\u5148",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,82,72)"
                        }
                    }
                },
                {
                    "name": "\u6ee1\u52e4\u5956",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,99,136)"
                        }
                    }
                },
                {
                    "name": "\u5c31\u6765\u641c\u72d7\u5546\u4e1a\u641c\u7d22\u5427\uff01",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,106,136)"
                        }
                    }
                },
                {
                    "name": "\u8865\u52a9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,5,116)"
                        }
                    }
                },
                {
                    "name": "\u7ba1\u4e24\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,127,111)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,156,87)"
                        }
                    }
                },
                {
                    "name": "AI\u524d\u666f\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,60,11)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5382\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,134,58)"
                        }
                    }
                },
                {
                    "name": "\u4fdd\u9669",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,160,149)"
                        }
                    }
                },
                {
                    "name": "6\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,86,79)"
                        }
                    }
                },
                {
                    "name": "\u6d3b\u529b\u65e0\u9650",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,37,79)"
                        }
                    }
                },
                {
                    "name": "\u7b80\u5355\u771f\u8bda",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,46,120)"
                        }
                    }
                },
                {
                    "name": "\uff08\u54c8\u5570\u51fa\u884c\uff09\u730e\u5934\u804c\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,100,101)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u5750\u9547",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,153,112)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u9650\u96f6\u98df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,69,90)"
                        }
                    }
                },
                {
                    "name": "500\u5f3a\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,150,136)"
                        }
                    }
                },
                {
                    "name": "\u7814\u7a76\u4e2d\u5fc3\u72ec\u7acb\u529e\u516c\u5ba4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,129,145)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c\u798f\u5229\u4f18\u8d8a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,98,19)"
                        }
                    }
                },
                {
                    "name": "\u5730\u7406\u4f4d\u7f6e\u4fbf\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,6,131)"
                        }
                    }
                },
                {
                    "name": "AI\u98ce\u53e3\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,92,43)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u4e0d\u9519",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,133,59)"
                        }
                    }
                },
                {
                    "name": "\u5bfc\u5e08\u4e00\u5bf9\u4e00\u5e26",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,135,151)"
                        }
                    }
                },
                {
                    "name": "\u90e8\u95e8\u53d1\u5c55\u8fc5\u901f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,142,60)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u5236\u9020",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,10,83)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u5b66\u5bb6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,66,2)"
                        }
                    }
                },
                {
                    "name": "\u5929\u9ad8\u4efb\u9e1f\u98de",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,28,118)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5185\u5bb9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,55,48)"
                        }
                    }
                },
                {
                    "name": "\u5305\u4f4f\u5bbf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,30,103)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u5fc3\u7814\u7a76\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,57,55)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u5496\u5e26\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,40,91)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6df1\u5ea6ok",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,30,149)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u5bbf\u820d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,150,0)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u754c\u5148\u8fdb\u7684\u5e7f\u544a\u6295\u653e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,125,136)"
                        }
                    }
                },
                {
                    "name": "Mac\u529e\u516c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,94,76)"
                        }
                    }
                },
                {
                    "name": "13\u85aa+\u5e74\u7ec8\u5956+\u5458\u5de5\u6301\u80a1\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,11,33)"
                        }
                    }
                },
                {
                    "name": "\u5305\u53cc\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,58,8)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u8d28\u7684\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,145,133)"
                        }
                    }
                },
                {
                    "name": "\u4e3b\u5bfc\u9879\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,94,30)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u65e5\u56db\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,47,46)"
                        }
                    }
                },
                {
                    "name": "\u6253\u9020\u4e00\u6d41\u7684\u7814\u53d1\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,152,147)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u89c4\u6a21\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,136,82)"
                        }
                    }
                },
                {
                    "name": "\u516c\u79df\u623f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,116,112)"
                        }
                    }
                },
                {
                    "name": "\u5404\u79cd\u5458\u5de5\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,22,38)"
                        }
                    }
                },
                {
                    "name": "10\u5929\u5e26\u85aa\u75c5\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,69,130)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5e74\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,119,4)"
                        }
                    }
                },
                {
                    "name": "19\u85aa\u514d\u8d39\u4e0b\u5348\u8336\u4f4f\u623f\u8865\u8d34\u6253\u8f66\u62a5\u9500\u5176\u4ed6\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,35,35)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u4ece\u4f18",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,32,122)"
                        }
                    }
                },
                {
                    "name": "\u90e8\u95e8\u8bc4\u4f18\u5956",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,114,101)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u5f85\u9047\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,49,2)"
                        }
                    }
                },
                {
                    "name": "\u505a\u4e94\u4f11\u4e8c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,8,1)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u6f5c\u529b\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,98,63)"
                        }
                    }
                },
                {
                    "name": "\u6709\u5927\u725b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,126,37)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7814\u4ea7\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,68,137)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u5e26\u9886",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,14,66)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u7684\u8d77\u70b9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,149,9)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u4e92\u8054\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,92,27)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u6709\u7ade\u4e89\u529b\u7684\u85aa\u8d44\u53d1\u5c55",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,121,71)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u5347\u4e2a\u4eba\u4ef7\u503c\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,145,17)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u673a\u4f1a\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,127,93)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5e02\u51c6\u5907\u671f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,22,100)"
                        }
                    }
                },
                {
                    "name": "\u5f15\u9886\u884c\u4e1a\u8d70\u52bf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,95,77)"
                        }
                    }
                },
                {
                    "name": "\u540d\u6821\u5927\u5382",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,9,54)"
                        }
                    }
                },
                {
                    "name": "\u5927\u4f6c\u4e91\u96c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,154,114)"
                        }
                    }
                },
                {
                    "name": "\u7b80\u5355\u5feb\u901f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,158,120)"
                        }
                    }
                },
                {
                    "name": "\u4e0e\u4e16\u754c\u9886\u5148\u7684AI\u7814\u53d1\u56e2\u961f\u5408\u4f5c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,82,64)"
                        }
                    }
                },
                {
                    "name": "\u6d53\u539a\u7684\u6280\u672f\u5b66\u4e60\u6c1b\u56f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,108,30)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6311\u6218",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,53,33)"
                        }
                    }
                },
                {
                    "name": "\u521b\u65b0\u9879\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,56,118)"
                        }
                    }
                },
                {
                    "name": "\u4f01\u4e1a\u798f\u5229\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,84,32)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u53d1\u5c55\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,60,22)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u4e1a\u4e13\u5fc3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,28,18)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u65b0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,103,114)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u5229\u9879\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,26,130)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u5373\u5c06\u4e0a\u5e02",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,152,127)"
                        }
                    }
                },
                {
                    "name": "\u5f00\u53d1\u94bb\u7814\u524d\u6cbf\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,59,148)"
                        }
                    }
                },
                {
                    "name": "\u8f66\u8054\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,141,118)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u53d1\u5c55\u5feb\u901f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,157,141)"
                        }
                    }
                },
                {
                    "name": "\u826f\u597d\u7684\u5de5\u4f5c\u73af\u5883",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,20,104)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6311\u6218\u548c\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,35,28)"
                        }
                    }
                },
                {
                    "name": "\u7ec6\u5206\u884c\u4e1a\u9f99\u5934\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,44,100)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u7814\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,36,160)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4fdd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,65,126)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u5de5\u7a0b\u5de5\u4e1a\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,144,72)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u9886\u8dd1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,21,147)"
                        }
                    }
                },
                {
                    "name": "\u5496\u5561\u5385",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,5,43)"
                        }
                    }
                },
                {
                    "name": "\u5927\u4f6c\u5e26\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,34,94)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u5168",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,24,109)"
                        }
                    }
                },
                {
                    "name": "\u521b\u65b0\u5e94\u7528",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,78,41)"
                        }
                    }
                },
                {
                    "name": "\u56fa\u5b9a\u6da8\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,84,65)"
                        }
                    }
                },
                {
                    "name": "\u80a1\u6743\u8ba1\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,112,39)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u5b9e\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,107,28)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u90e8\u95e8\u6838\u5fc3\u5c97\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,15,151)"
                        }
                    }
                },
                {
                    "name": "\u6709XLNet\u4e00\u4f5c\u5927\u795e\u5e26\u60a8\u5728\u7b97\u6cd5\u91cc\u6df1\u8015",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,48,102)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,143,75)"
                        }
                    }
                },
                {
                    "name": "\u51fa\u6d77",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,25,34)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u9760",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,89,52)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,13,77)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u56e2\u961f\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,35,20)"
                        }
                    }
                },
                {
                    "name": "\u6bcf\u6708\u623f\u88652000",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,82,10)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u671f\u805a\u9910~",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,127,16)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5e02\u516c\u53f8/\u524d\u666f\u597d/\u5927\u725b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,59,51)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u53d1\u5c55\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,121,59)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u589e\u957f\u5feb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,55,63)"
                        }
                    }
                },
                {
                    "name": "\u9910\u996e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,145,75)"
                        }
                    }
                },
                {
                    "name": "\u9886\u5bfcNic",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,54,40)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u798f\u5229/\u56e2\u961f\u6c1b\u56f4/\u5b9a\u671f\u57f9\u8bad/\u664b\u5347\u901a\u9053",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,71,107)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u6307\u5bfc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,67,127)"
                        }
                    }
                },
                {
                    "name": "***\u9879\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,152,128)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1\u4e0d\u5b9a\u671f\u56e2\u5efa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,60,2)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u6838\u5fc3\u5927\u8111\u9879\u76ee\u80a1\u7968\u671f\u6743",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,125,35)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u5f85\u9047\u4f18\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,112,145)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u4e09\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,125,158)"
                        }
                    }
                },
                {
                    "name": "3D\u89c6\u89c9+AI",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,131,0)"
                        }
                    }
                },
                {
                    "name": "\u517c\u804c\u5c97\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,103,11)"
                        }
                    }
                },
                {
                    "name": "\u3010\u6b63\u96c5\u9f7f\u79d1\u3011\u730e\u5934\u5c97\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,146,138)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6167\u73af\u4fdd\u9886\u519b\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,120,59)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u73ed\u8f66\u63a5\u9001",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,48,126)"
                        }
                    }
                },
                {
                    "name": "90\u540e\u9017\u6bd4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,3,114)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u56fe\u50cf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,23,153)"
                        }
                    }
                },
                {
                    "name": "\u4e5d\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,121,84)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u573a\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,50,56)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u9886\u57df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,111,89)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u699c****",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,68,105)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c\u798f\u5229\u826f\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,64,63)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u4e0d\u9519",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,118,125)"
                        }
                    }
                },
                {
                    "name": "16-18\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,143,95)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u8f6c\u6b63\u673a\u4f1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,93,116)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6709\u6311\u6218",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,80,18)"
                        }
                    }
                },
                {
                    "name": "9\u70b9\u6253\u8f66\u62a5\u9500",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,28,50)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u5927\u4e0a\u73af\u5883",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,106,71)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u624d\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,128,72)"
                        }
                    }
                },
                {
                    "name": "\u5168\u5e7416-18\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,23,103)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,135,74)"
                        }
                    }
                },
                {
                    "name": "\u897f\u5de5\u5927\u7b49\u9ad8\u5c42\u6b21\u79d1\u7814\u5355\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,55,114)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u4e1a\u52a1\u7684\u98ce\u63a7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,70,142)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4\u597d\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,106,129)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u9760\u8c31\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,100,76)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u7684\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,27,38)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u8c03\u5ea6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,70,124)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5916\u9879\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,63,159)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6167\u4ea4\u901a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,111,14)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u7ebf\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,59,62)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u9645\u5316\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,126,27)"
                        }
                    }
                },
                {
                    "name": "\u524d\u6cbf\u4ea7\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,76,36)"
                        }
                    }
                },
                {
                    "name": "\u8fbe\u5230\u4e00\u5b9a\u804c\u7ea7\u53ef\u83b7\u5f97\u516c\u53f8\u80a1\u6743",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,134,11)"
                        }
                    }
                },
                {
                    "name": "\u4ebf\u7ea7\u6d41\u91cf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,155,149)"
                        }
                    }
                },
                {
                    "name": "\u725b\u4eba\u5e26\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,77,159)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4\u68d2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,151,154)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u4eba\u914d\u9001",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,127,88)"
                        }
                    }
                },
                {
                    "name": "\u4e24\u4f4d\u9662\u58eb\u4e09\u4f4d\u535a\u58eb\u9886\u8854\u7684\u521d\u521b\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,60,84)"
                        }
                    }
                },
                {
                    "name": "\u817e\u8baf\u9886\u6295",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,40,63)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51\u6c1b\u56f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,8,31)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u65e9\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,43,44)"
                        }
                    }
                },
                {
                    "name": "\u9910\u996e\u8865\u52a9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,102,72)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u5c97\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,34,108)"
                        }
                    }
                },
                {
                    "name": "AI\u4ea7\u54c1\u7814\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,35,33)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5bfc\u5411",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,142,77)"
                        }
                    }
                },
                {
                    "name": "\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,63,49)"
                        }
                    }
                },
                {
                    "name": "\u8bd5\u7528\u671f\u5168\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,126,14)"
                        }
                    }
                },
                {
                    "name": "\u6709\u80a1\u7968\u671f\u6743\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,154,152)"
                        }
                    }
                },
                {
                    "name": "\u4f01\u4e1a\u6587\u5316\u4f73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,129,136)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u63a8\u8350\u7cfb\u7edf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,109,26)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u7ebf\u98ce\u6295\u52a0\u6301",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,96,24)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u6838\u5fc3\u56e2\u961f\u5feb\u901f\u6269\u5c55",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,19,113)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u4f4f\u5bbf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,149,13)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u7a33\u5b9a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,0,37)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u7b80\u5355",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,6,31)"
                        }
                    }
                },
                {
                    "name": "\u6709\u6311\u6218",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,118,19)"
                        }
                    }
                },
                {
                    "name": "\u300e\u76c8\u5cf0\u79d1\u6280\u300f\u730e\u5934\u804c\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,107,141)"
                        }
                    }
                },
                {
                    "name": "\u575a\u6301\u81ea\u4e3b\u521b\u65b0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,122,58)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u8d28\u9879\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,97,41)"
                        }
                    }
                },
                {
                    "name": "\u5f3a\u5927\u7684\u6280\u672f\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,146,46)"
                        }
                    }
                },
                {
                    "name": "\u4f4f\u623f\u6216\u4ea4\u901a\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,89,68)"
                        }
                    }
                },
                {
                    "name": "AI\u4ea7\u54c1\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,23,111)"
                        }
                    }
                },
                {
                    "name": "ai\u533b\u7597\u72ec\u89d2\u517d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,102,13)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u4f18\u6e25",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,54,152)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u4e00\u7ebf\u4e92\u8054\u7f51\u516c\u53f8\u85aa\u6c34\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,64,20)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5927\u725b\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,125,127)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u901f\u53d1\u5c55\u9636\u6bb5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,141,68)"
                        }
                    }
                },
                {
                    "name": "\u5e02\u573a\u524d\u666f\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,85,38)"
                        }
                    }
                },
                {
                    "name": "\u5bfc\u5e08\u6307\u5bfc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,92,154)"
                        }
                    }
                },
                {
                    "name": "\u80fd\u529b\u7a81\u51fa\u8005\u664b\u5347\u5feb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,42,15)"
                        }
                    }
                },
                {
                    "name": "top5\u624b\u673a\u5382\u5546",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,84,92)"
                        }
                    }
                },
                {
                    "name": "\u5b63\u5ea6\u5956\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,157,59)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u8865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,113,159)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u5efa\u6d3b\u52a8\u7b49",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,14,113)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u901f\u53d1\u5c55\u4e2d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,143,130)"
                        }
                    }
                },
                {
                    "name": "\u62df\u4e0a\u5e02",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,130,49)"
                        }
                    }
                },
                {
                    "name": "\u5730\u4ea7\u9f99\u5934",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,77,83)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u4f53\u68c0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,68,109)"
                        }
                    }
                },
                {
                    "name": "\u771f\u5b9e\u4e30\u5bcc\u7684\u5e94\u7528\u573a\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,51,106)"
                        }
                    }
                },
                {
                    "name": "D\u8f6e\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,160,121)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,108,95)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u6df1\u8015\u571f\u58e4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,133,114)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u7814\u9662\u6821\u9f0e\u529b\u652f\u6301",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,158,123)"
                        }
                    }
                },
                {
                    "name": "\u5df2\u83b7\u591a\u5bb6\u4e00\u7ebfVC\u6295\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,149,99)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5382\u80cc\u666f\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,10,28)"
                        }
                    }
                },
                {
                    "name": "\u3010\u4eac\u4e1c\u7269\u6d41\u3011\u730e\u5934\u5c97\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,71,144)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,1,139)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,115,153)"
                        }
                    }
                },
                {
                    "name": "\u661f\u5df4\u514b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,26,145)"
                        }
                    }
                },
                {
                    "name": "\u7075\u6d3b\u5de5\u65f6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,50,129)"
                        }
                    }
                },
                {
                    "name": "\u79fb\u52a8\u51fa\u6d77",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,106,147)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u5de5\u4f5c\u673a\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,116,32)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u98df\u65e0\u9650\u91cf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,66,40)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c\u798f\u5229\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,99,73)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u6280\u672f\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,9,118)"
                        }
                    }
                },
                {
                    "name": "\u7a33\u5b9a\u53d1\u5c55",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,14,67)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u6807\u6746",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,150,22)"
                        }
                    }
                },
                {
                    "name": "\u8865\u5145\u533b\u4fdd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,120,100)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ee9\u6548\u53ca\u5956\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,41,17)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5e95\u53cc\u85aa-\u5e74\u7ec8\u5956-\u6241\u5e73\u5316\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,22,17)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u805a\u96c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,16,145)"
                        }
                    }
                },
                {
                    "name": "\u4fdd\u5e9513\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,14,121)"
                        }
                    }
                },
                {
                    "name": "\u535a\u58eb\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,91,87)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5458\u57f9\u517b\u673a\u5236\u5b8c\u5584",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,70,153)"
                        }
                    }
                },
                {
                    "name": "\u8282\u65e5\u793c\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,108,143)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u5bf9\u4e00\u5e26\u6559",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,158,55)"
                        }
                    }
                },
                {
                    "name": "\u8d1f\u8d23\u641c\u72d7\u6570\u5b57\u4eba\u76843D\u4eba\u8138\u7b97\u6cd5\u65b9\u9762\u7684\u7814\u7a76",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,154,30)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u7a7a\u95f4\u5de8\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,93,74)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u85aa\uff0b\u671f\u6743",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,120,116)"
                        }
                    }
                },
                {
                    "name": "500\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,34,157)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u8d5b\u9053",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,83,60)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u5b50\u5973\u8865\u5145\u533b\u7597",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,74,87)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5347\u5feb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,39,40)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5b9e\u4e60\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,102,74)"
                        }
                    }
                },
                {
                    "name": "\u610f\u5916\u8865\u52a9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,142,96)"
                        }
                    }
                },
                {
                    "name": "SaaS",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,83,66)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u5929\u516b\u5c0f\u65f6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,131,40)"
                        }
                    }
                },
                {
                    "name": "\u4f01\u4e1a\u5185\u521b\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,87,15)"
                        }
                    }
                },
                {
                    "name": "\u5168\u7403\u5316\u89c6\u91ce",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,122,74)"
                        }
                    }
                },
                {
                    "name": "\u5185\u90e8\u664b\u5347\u6e20\u9053\u5e7f\u9614",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,121,158)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u7d20\u8d28\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,20,5)"
                        }
                    }
                },
                {
                    "name": "BAT\u6280\u672fleader",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,73,119)"
                        }
                    }
                },
                {
                    "name": "\u51fa\u56fd\u6e38",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,110,52)"
                        }
                    }
                },
                {
                    "name": "\u3010OPPO\u3011\u730e\u5934\u804c\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,32,0)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u53d1\u5c55\u524d\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,6,43)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u5185\u542b\u5065\u8eab\u623f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,153,109)"
                        }
                    }
                },
                {
                    "name": "\u7b80\u5355\u6587\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,109,34)"
                        }
                    }
                },
                {
                    "name": "\u5782\u76f4\u9886\u57df****",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,151,103)"
                        }
                    }
                },
                {
                    "name": "\u6709\u53d1\u5c55",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,19,22)"
                        }
                    }
                },
                {
                    "name": "Top\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,41,65)"
                        }
                    }
                },
                {
                    "name": "\u3010\u6b63\u96c5\u9f7f\u79d1\u3011\u730e\u5934\u804c\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,68,1)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u4e30\u5bcc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,48,120)"
                        }
                    }
                },
                {
                    "name": "\u98de\u901f\u53d1\u5c55",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,37,88)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c\u798f\u5229\u4f18\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,91,54)"
                        }
                    }
                },
                {
                    "name": "2\u4f4d\u9662\u58eb\u9886\u8854",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,148,160)"
                        }
                    }
                },
                {
                    "name": "\u6708\u5ea6\u6d3b\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,113,156)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u7814\u53d1\u5b9e\u529b\u96c4\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,52,155)"
                        }
                    }
                },
                {
                    "name": "\u7d2b\u5149\u96c6\u56e2\u65d7\u4e0b\u6559\u80b2\u4fe1\u606f\u5316\u884c\u4e1a\u5934\u90e8\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,72,13)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5f52\u79d1\u7814\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,33,91)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,7,117)"
                        }
                    }
                },
                {
                    "name": "\u5bbd\u5e7f\u7684\u53d1\u5c55\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,83,119)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u6316\u6398",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,39,6)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u72ec\u89d2\u517d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,109,152)"
                        }
                    }
                },
                {
                    "name": "5\u59298\u5c0f\u65f6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,101,130)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4ea4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,36,36)"
                        }
                    }
                },
                {
                    "name": "\u4e0d\u5b9a\u671f\u56e2\u5efa\u6d3b\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,91,30)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u90e8\u95e8\u6838\u5fc3\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,90,48)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u73af\u5883\u8f7b\u677e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,120,25)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u5f85\u9047open",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,37,61)"
                        }
                    }
                },
                {
                    "name": "\u8fd8\u53ef\u4ee5\u64b8\u732b\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,137,76)"
                        }
                    }
                },
                {
                    "name": "**\u751f\u7269\u533b\u5b66\u4fe1\u606f\u4e13\u5bb6\u5e26\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,37,125)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1atop\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,39,53)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u4e8b\u5047\u4e94\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,49,60)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u7a33\u5b9a/\u85aa\u916c\u4f18\u6e25",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,119,2)"
                        }
                    }
                },
                {
                    "name": "\u975e\u5e38\u4eba\u6027\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,6,119)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u521b\u65b0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,107,120)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u4e30\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,129,80)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u4e0a\u4e0b\u73ed\u53cc\u4f11",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,29,40)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u524d\u6cbf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,18,107)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u9886",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,112,90)"
                        }
                    }
                },
                {
                    "name": "AI\u56e2\u961f\u7b79\u5efa\u4e2d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,122,154)"
                        }
                    }
                },
                {
                    "name": "\u72ec\u7acb\u8d1f\u8d23",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,13,130)"
                        }
                    }
                },
                {
                    "name": "\u4f4f\u623f\u514d\u606f\u8d37",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,99,98)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u91d1\u7b49",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,147,130)"
                        }
                    }
                },
                {
                    "name": "\u91cd\u70b9\u90e8\u95e8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,108,37)"
                        }
                    }
                },
                {
                    "name": "\u535a\u58eb\u843d\u6237",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,7,20)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u540d\u4e92\u8054\u7f51\u7535\u5546\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,90,87)"
                        }
                    }
                },
                {
                    "name": "\u516d\u9669\u4e00\u91d1\u5e26\u85aa\u4e8b\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,6,48)"
                        }
                    }
                },
                {
                    "name": "\u521b\u65b0\u6c1b\u56f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,92,31)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1atop",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,88,133)"
                        }
                    }
                },
                {
                    "name": "\u957f\u671f\u7a33\u5b9a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,151,133)"
                        }
                    }
                },
                {
                    "name": "\u767e\u4ebf\u72ec\u89d2\u517d\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,99,152)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4\u8f7b\u677e\u6709\u7231",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,20,136)"
                        }
                    }
                },
                {
                    "name": "\u7a33\u5065\u589e\u957f\u7684\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,28,49)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u524d\u77bb\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,39,7)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u89c6\u9891",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,41,42)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5065\u8eab\u623f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,139,41)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,57,79)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u5348\u9910\u665a\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,119,156)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5347\u671f\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,130,3)"
                        }
                    }
                },
                {
                    "name": "\u5468\u672b\u53cc\u4f118\u5c0f\u65f6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,111,38)"
                        }
                    }
                },
                {
                    "name": "\u79fb\u52a8\u4e92\u8054\u7f51\u5e7f\u544a\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,15,90)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u4f6c\u5e26\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,97,131)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5916\u4ea7\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,108,66)"
                        }
                    }
                },
                {
                    "name": "\u822a\u7a7aIT\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,10,9)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,130,152)"
                        }
                    }
                },
                {
                    "name": "\u300a\u77f3\u5934\u79d1\u6280\u300b\u730e\u5934\u804c\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,53,25)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u6311\u6218",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,33,0)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u53d1\u5c55\u5feb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,15,112)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u5e73\u53f0\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,145,102)"
                        }
                    }
                },
                {
                    "name": "\u73b0\u573a\u9762\u8bd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,87,10)"
                        }
                    }
                },
                {
                    "name": "\u6e38\u620fUGC",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,135,16)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u5229\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,138,82)"
                        }
                    }
                },
                {
                    "name": "\u5927\u7528\u6237\u91cf\u7ea7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,39,55)"
                        }
                    }
                },
                {
                    "name": "\u6c7d\u8f66\u884c\u4e1a\u4e07\u4ebf\u8d5b\u9053\u98ce\u63a7\u662f\u884c\u4e1a\u75db\u70b9\u53d1\u5c55\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,77,154)"
                        }
                    }
                },
                {
                    "name": "\u8f7b\u677e\u6d3b\u8dc3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,83,60)"
                        }
                    }
                },
                {
                    "name": "\u725b\u4eba\u56e2\u961f\u80cc\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,116,32)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u80a1\u4e0a\u5e02\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,149,3)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u4ea7\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,126,29)"
                        }
                    }
                },
                {
                    "name": "TCL\u5927\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,77,160)"
                        }
                    }
                },
                {
                    "name": "\u786c\u8f6f\u4ef6\u7ed3\u5408",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,149,137)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5927\u725b\u4f17\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,69,149)"
                        }
                    }
                },
                {
                    "name": "\u9886\u5bfcNice",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,84,80)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u826f\u7684\u4e0a\u5347\u901a\u9053",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,140,86)"
                        }
                    }
                },
                {
                    "name": "\u4ebf\u7ea7\u7528\u6237",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,84,53)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5e9514\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,65,76)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u7814\u53d1\u5b9e\u529b\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,23,45)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u7a7a\u95f4\u5e7f\u9614\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,133,141)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5348\u9910\u665a\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,147,144)"
                        }
                    }
                },
                {
                    "name": "\u516b\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,142,110)"
                        }
                    }
                },
                {
                    "name": "\u4f11\u95f2\u96f6\u98df\u4e0b\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,66,159)"
                        }
                    }
                },
                {
                    "name": "\u8fdc\u7a0b\u529e\u516c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,120,2)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u8fc5\u901f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,118,47)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u798f\u5229\u5f85\u9047\u4f18\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,71,7)"
                        }
                    }
                },
                {
                    "name": "\u8282\u65e5\u793c\u7269",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,100,143)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u5929\u516b\u5c0f\u65f6\u5de5\u4f5c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,96,9)"
                        }
                    }
                },
                {
                    "name": "\u9633\u5149\u73af\u5883",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,131,116)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u4f53\u7cfb\u5b8c\u5584",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,30,118)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u5e7414\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,16,103)"
                        }
                    }
                },
                {
                    "name": "open",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,48,97)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u6c1b\u56f4\u6d3b\u8dc3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,66,15)"
                        }
                    }
                },
                {
                    "name": "python\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,36,106)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u8865\u52a9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,58,92)"
                        }
                    }
                },
                {
                    "name": "12\u5929\u5e26\u85aa\u5e74\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,9,125)"
                        }
                    }
                },
                {
                    "name": "\u7eff\u8c37\u5236\u836f\u5b50\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,30,38)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u81f3\u4e0a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,137,86)"
                        }
                    }
                },
                {
                    "name": "\u4e0d\u9650\u91cf\u4e0b\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,71,4)"
                        }
                    }
                },
                {
                    "name": "\u529e\u516c\u73af\u5883\u4f73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,65,11)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u5e72\u9884\u662f\u7f8e\u56e2\u9a91\u884c\u4e1a\u52a1\u6838\u5fc3\u90e8\u5206",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,113,40)"
                        }
                    }
                },
                {
                    "name": "\u5168\u7ebf\u73ed\u8f66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,118,55)"
                        }
                    }
                },
                {
                    "name": "\u8001\u677f\u683c\u5c40\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,13,101)"
                        }
                    }
                },
                {
                    "name": "\u96c6\u56e2\u80cc\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,80,112)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u4ea7\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,28,92)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u5904\u4e8e\u5feb\u901f\u53d1\u5c55",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,116,4)"
                        }
                    }
                },
                {
                    "name": "Linux",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,62,9)"
                        }
                    }
                },
                {
                    "name": "\u5168\u7403\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,24,155)"
                        }
                    }
                },
                {
                    "name": "\u7d2b\u5149\u96c6\u56e2\u65d7\u4e0b\u6559\u80b2\u4fe1\u606f\u5316\u5934\u90e8\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,42,73)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u9910\u514d\u8d39",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,125,95)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u7ee9\u6548\u5956\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,112,55)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u7ed9\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,111,83)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u4f53\u68c0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,21,38)"
                        }
                    }
                },
                {
                    "name": "LayaAir\u5f15\u64ce\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,124,150)"
                        }
                    }
                },
                {
                    "name": "14-16\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,41,23)"
                        }
                    }
                },
                {
                    "name": "10\u5929\u6625\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,5,32)"
                        }
                    }
                },
                {
                    "name": "\u5168\u989d5\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,74,100)"
                        }
                    }
                },
                {
                    "name": "A\u8f6e\u878d\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,82,35)"
                        }
                    }
                },
                {
                    "name": "\u6700\u80fd\u53d1\u6325\u521b\u9020\u529b\u7684\u7a7a\u95f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,112,103)"
                        }
                    }
                },
                {
                    "name": "\u7b80\u5355\u5f00\u653e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,95,110)"
                        }
                    }
                },
                {
                    "name": "\u878d\u8d4411\u4ebf\u7f8e\u5143",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,147,24)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u4e00\u65e5\u4e09\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,9,129)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4\u826f\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,74,38)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u73ed\u5f00\u5fc3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,138,82)"
                        }
                    }
                },
                {
                    "name": "\u597d\u73a9\u7684\u6e38\u620f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,122,80)"
                        }
                    }
                },
                {
                    "name": "\u7814\u53d1\u56e2\u961f\u5b9e\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,24,64)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6df1\u5ea6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,95,142)"
                        }
                    }
                },
                {
                    "name": "\u9910\u8865\u901a\u8baf\u8865\u7535\u8111\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,126,19)"
                        }
                    }
                },
                {
                    "name": "\u7269\u6d41",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,129,58)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u73af\u5883\u4f18\u7f8e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,122,114)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u98df\u6c34\u679c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,105,73)"
                        }
                    }
                },
                {
                    "name": "\u524d\u6cbf\u9886\u57df\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,19,89)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u85aa\u8d44\u4f18\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,130,105)"
                        }
                    }
                },
                {
                    "name": "\u6bcf\u5e742\u6b21\u8c03\u85aa\u7a97\u53e3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,147,33)"
                        }
                    }
                },
                {
                    "name": "\u5305\u5403\u4f4f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,149,60)"
                        }
                    }
                },
                {
                    "name": "\u516c\u68c0\u6cd5\u5927\u6570\u636e\u52a0\u4eba\u5de5\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,21,129)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7d20\u8d28\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,87,19)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4\u798f\u5229\u5f85\u9047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,141,52)"
                        }
                    }
                },
                {
                    "name": "\u592e\u4f01",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,38,154)"
                        }
                    }
                },
                {
                    "name": "\u9f13\u52b1\u8bd5\u9519",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,109,19)"
                        }
                    }
                },
                {
                    "name": "\u51fa\u5dee\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,43,5)"
                        }
                    }
                },
                {
                    "name": "\u664b\u7ea7\u664b\u5347",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,123,58)"
                        }
                    }
                },
                {
                    "name": "\u7845\u8c37\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,142,67)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u540d\u836f\u4f01",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,150,27)"
                        }
                    }
                },
                {
                    "name": "\u540c\u4e8b\u597d\u76f8\u5904",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,75,51)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u7a7a\u95f4\u53ca\u85aa\u916c\u9ad8\u4e8e\u540c\u884c\u4e1a\u6c34\u5e73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,44,147)"
                        }
                    }
                },
                {
                    "name": "\u5171\u540c\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,119,139)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4NICE",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,22,93)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u80cc\u666f\u5f3a\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,17,31)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u540d\u7535\u5546",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,160,94)"
                        }
                    }
                },
                {
                    "name": "\u3010\u89c9\u975e\u79d1\u6280\u3011\u730e\u5934\u5c97\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,62,141)"
                        }
                    }
                },
                {
                    "name": "\u5065\u5eb7\u4f53\u68c0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,69,110)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u901a\u8baf\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,69,93)"
                        }
                    }
                },
                {
                    "name": "\u963f\u91cc\u7cfb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,107,36)"
                        }
                    }
                },
                {
                    "name": "\u8fdb\u4fee\u673a\u4f1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,74,73)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u989d\u9910\u8865/TB\u8d39\u7528",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,90,93)"
                        }
                    }
                },
                {
                    "name": "\u4e2a\u4eba\u6210\u957f\u6027",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,68,83)"
                        }
                    }
                },
                {
                    "name": "\u5229\u7528\u6700\u524d\u6cbf\u7684\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,132,69)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u957f\u5e26\u85aa\u5e74\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,46,89)"
                        }
                    }
                },
                {
                    "name": "\u52a0\u73ed\u8d39\u53e6\u7b97",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,159,90)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u68d2\u7684\u9886\u5bfc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,125,135)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,155,120)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u672a\u6765\u91cd\u70b9\u53d1\u5c55\u6295\u5165",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,124,130)"
                        }
                    }
                },
                {
                    "name": "\u725b\u4eba\u540c\u4e8b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,156,43)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u4f18\u6e25",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,94,40)"
                        }
                    }
                },
                {
                    "name": "\u6210\u5458\u5e74\u8f7b\u5316\u6709\u524d\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,17,126)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5165\u4e86\u89e3\u5927\u89c4\u6a21\u6570\u636e\u8bad\u7ec3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,127,93)"
                        }
                    }
                },
                {
                    "name": "\u83b7\u591a\u5bb6**\u673a\u6784\u6295\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,63,94)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5206\u4eab",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,6,0)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u5bfc\u5e08\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,20,10)"
                        }
                    }
                },
                {
                    "name": "007",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,160,39)"
                        }
                    }
                },
                {
                    "name": "\u5927\u4f6c\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,82,139)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u4f73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,41,109)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u798f\u5229\u4f18",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,53,137)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u5065\u8eab\u623f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,73,72)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u6cdb\u6210\u957f\u7a7a\u95f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,120,156)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u5229\u5956\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,35,11)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u6325\u6240\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,99,99)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u8c03\u5ea6\u4f18\u5316\u5f15\u64ce\u7684\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,60,0)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u4e30\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,159,38)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u4e60\u8d44\u6e90\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,111,95)"
                        }
                    }
                },
                {
                    "name": "995\u85aa\u8d44\u5f85\u9047\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,102,66)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u63a8\u8350\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,7,77)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6269\u62db",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,11,98)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u91cf\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,131,133)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u4e60\u5b9e\u8df5\u673a\u4f1a\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,130,7)"
                        }
                    }
                },
                {
                    "name": "\u516d\u9669\u4e00\u91d1+\u5b63\u5ea6\u7ee9\u6548\u5956\u91d1/\u5e74\u7ec8\u5956",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,89,35)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5496\u5e26\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,79,130)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u9886\u519b\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,85,138)"
                        }
                    }
                },
                {
                    "name": "\u505a\u4e8b\u81ea\u7531\u5ea6\u8db3\u591f\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,35,126)"
                        }
                    }
                },
                {
                    "name": "\u673a\u4f1a\u591a\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,100,89)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u91cf\u8fc5\u731b\u53d1\u5c55",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,124,17)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u9ad8\u798f\u5229\u597d\u5927\u725b\u8eab\u8fb9\u7ed5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,9,55)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u665a\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,23,43)"
                        }
                    }
                },
                {
                    "name": "B\u8f6e\u878d\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,40,138)"
                        }
                    }
                },
                {
                    "name": "NLP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,27,133)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5347\u671f\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,56,79)"
                        }
                    }
                },
                {
                    "name": "\u7a33\u5b9a\u6027\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,105,118)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u6e38\u56e2\u5efa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,137,55)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u56e2\u961f\u4f18\u79c0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,123,99)"
                        }
                    }
                },
                {
                    "name": "\u529f\u8bfe\u524d\u6cbf\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,129,8)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u5bb6\u91cd\u70b9\u65b9\u5411",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,51,68)"
                        }
                    }
                },
                {
                    "name": "\u5927\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,75,105)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u901f\u53d1\u5c55\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,156,72)"
                        }
                    }
                },
                {
                    "name": "nice\u9886\u5bfc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,7,151)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,27,108)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,17,157)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u901a\u9053",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,60,123)"
                        }
                    }
                },
                {
                    "name": "\u504f\u5e73\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,70,101)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4\u8f7b\u677e\uff01",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,121,21)"
                        }
                    }
                },
                {
                    "name": "\u6d3b\u529b\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,70,62)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u524d\u666f\u8d5e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,74,87)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,103,142)"
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
        chart_8a8456c56af54905929a14cf6ff782a4.setOption(option_8a8456c56af54905929a14cf6ff782a4);
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