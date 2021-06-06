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

<h2>（2021-06-06更新）</h2>

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
            <button class="tablinks" onclick="showChart(event, 'f1a30280e3db4d74a628c6af3c60001f')">公司</button>
            <button class="tablinks" onclick="showChart(event, '513ef5ede4114c158d756f6a06bb7ac0')">城市</button>
            <button class="tablinks" onclick="showChart(event, 'ba68464ba85b474b89edd609ee10f2c1')">城市占比</button>
            <button class="tablinks" onclick="showChart(event, '060468ceb33f4b6b844f583058ea1b01')">招聘地图</button>
            <button class="tablinks" onclick="showChart(event, '8b94b28c8104489e912febe0e4b518ae')">区域</button>
            <button class="tablinks" onclick="showChart(event, '52beb97995c649be956bd359b66fe9a4')">区域占比</button>
            <button class="tablinks" onclick="showChart(event, '2bf0758cf0af401d9e4a7030b27371a3')">公司规模</button>
            <button class="tablinks" onclick="showChart(event, '9fbfcbb90c6a40798531be2419d1fa57')">人员规模</button>
            <button class="tablinks" onclick="showChart(event, 'f3b6ba5499ce4bc5b66b3b3bf2dfd207')">行业</button>
            <button class="tablinks" onclick="showChart(event, '7da50258cf3e46f9bef8dee4d9ae64bd')">招聘方向</button>
            <button class="tablinks" onclick="showChart(event, '860a1b78649e4a07bcc3bb4fbe0bedac')">公司福利</button>
    </div>

    <div class="box">
                <div id="f1a30280e3db4d74a628c6af3c60001f" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_f1a30280e3db4d74a628c6af3c60001f = echarts.init(
            document.getElementById('f1a30280e3db4d74a628c6af3c60001f'), 'white', {renderer: 'canvas'});
            
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
    
        var option_f1a30280e3db4d74a628c6af3c60001f = {
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
                58,
                41,
                35,
                28,
                21,
                16,
                15,
                14,
                14,
                14
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
                    "value": 58,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,108,72)"
                        }
                    }
                },
                {
                    "name": "\u5b57\u8282\u8df3\u52a8",
                    "value": 41,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,146,37)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u5982\u79c4",
                    "value": 35,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,9,146)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u79d1\u6280",
                    "value": 28,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,4,112)"
                        }
                    }
                },
                {
                    "name": "\u597d\u897f\u67da\u6559\u80b2",
                    "value": 21,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,32,22)"
                        }
                    }
                },
                {
                    "name": "\u9177\u72d7\u97f3\u4e50",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,63,56)"
                        }
                    }
                },
                {
                    "name": "\u9177\u5bb6\u4e50",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,20,13)"
                        }
                    }
                },
                {
                    "name": "\u964c\u964c",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,100,147)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u8d4b\u667a",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,84,137)"
                        }
                    }
                },
                {
                    "name": "Insta360\u5f71\u77f3",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,102,94)"
                        }
                    }
                },
                {
                    "name": "\u6ef4\u6ef4",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,150,30)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u4eba\u5bff",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,21,71)"
                        }
                    }
                },
                {
                    "name": "\u5929\u773c\u67e5",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,17,50)"
                        }
                    }
                },
                {
                    "name": "\u6167\u5b89\u91d1\u79d1",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,142,66)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u6613",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,160,84)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u6d6a\u7f51",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,122,13)"
                        }
                    }
                },
                {
                    "name": "\u641c\u72d7",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,19,140)"
                        }
                    }
                },
                {
                    "name": "\u62fc\u591a\u591a",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,92,33)"
                        }
                    }
                },
                {
                    "name": "\u666e\u6e21\u79d1\u6280",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,97,84)"
                        }
                    }
                },
                {
                    "name": "\u5546\u6c64\u79d1\u6280",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,128,4)"
                        }
                    }
                },
                {
                    "name": "\u7231\u5947\u827a",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,128,128)"
                        }
                    }
                },
                {
                    "name": "MINIEYE",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,126,67)"
                        }
                    }
                },
                {
                    "name": "\u6d82\u9e26\u667a\u80fd",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,72,133)"
                        }
                    }
                },
                {
                    "name": "\u9b54\u65b9\u706b\u79cd\u4f01\u4e1a\u7ba1\u7406\u54a8\u8be2",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,129,76)"
                        }
                    }
                },
                {
                    "name": "\u6570\u7f8e",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,95,78)"
                        }
                    }
                },
                {
                    "name": "\u76c8\u5609\u4e92\u8054",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,80,42)"
                        }
                    }
                },
                {
                    "name": "\u817e\u8baf",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,110,80)"
                        }
                    }
                },
                {
                    "name": "\u901a\u8054\u6570\u636e",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,95,10)"
                        }
                    }
                },
                {
                    "name": "\u767e\u5ea6",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,110,6)"
                        }
                    }
                },
                {
                    "name": "\u8c31\u65f6\u660a\u552f\u6570\u636e",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,91,119)"
                        }
                    }
                },
                {
                    "name": "Versa",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,18,38)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u78c1\u77f3",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,0,40)"
                        }
                    }
                },
                {
                    "name": "\u7693\u884c\u79d1\u6280",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,9,2)"
                        }
                    }
                },
                {
                    "name": "360os",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,79,22)"
                        }
                    }
                },
                {
                    "name": "\u65f7\u89c6MEGVII",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,30,21)"
                        }
                    }
                },
                {
                    "name": "\u631a\u9014\u79d1\u6280",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,128,37)"
                        }
                    }
                },
                {
                    "name": "\u5fc5\u793a\u79d1\u6280",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,109,10)"
                        }
                    }
                },
                {
                    "name": "\u5343\u5bfb\u4f4d\u7f6e",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,118,53)"
                        }
                    }
                },
                {
                    "name": "\u5f97\u7269App",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,92,85)"
                        }
                    }
                },
                {
                    "name": "\u8054\u5408\u96c6\u56e2",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,142,58)"
                        }
                    }
                },
                {
                    "name": "DMAI\u667a\u80fd\u79d1\u6280",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,59,26)"
                        }
                    }
                },
                {
                    "name": "\u732b\u5c90\u667a\u80fd",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,125,61)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u5c45\u5ba2",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,88,154)"
                        }
                    }
                },
                {
                    "name": "\u53c2\u6570",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,96,150)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u56fe\u79d1\u6280",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,58,160)"
                        }
                    }
                },
                {
                    "name": "\u827a\u6570\u672a\u6765",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,93,56)"
                        }
                    }
                },
                {
                    "name": "\u5f71\u521b\u79d1\u6280",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,10,148)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u51b0",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,119,147)"
                        }
                    }
                },
                {
                    "name": "OPPO",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,6,89)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5730\u91cf\u5b50",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,131,154)"
                        }
                    }
                },
                {
                    "name": "\u8d1d\u58f3",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,150,27)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u6052\u4fe1\u606f",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,96,49)"
                        }
                    }
                },
                {
                    "name": "\u8f7b\u821f\u667a\u822a",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,83,86)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u4ed9\u673a\u5668\u4eba",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,138,9)"
                        }
                    }
                },
                {
                    "name": "Soul",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,11,25)"
                        }
                    }
                },
                {
                    "name": "\u5faa\u73af\u667a\u80fd",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,47,158)"
                        }
                    }
                },
                {
                    "name": "\u8363\u8000\u7ec8\u7aef",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,133,119)"
                        }
                    }
                },
                {
                    "name": "\u987a\u4e30\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,3,152)"
                        }
                    }
                },
                {
                    "name": "\u5efa\u4fe1\u91d1\u79d1",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,116,13)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u4ed3\u667a\u80fd\u4ed3\u50a8",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,152,60)"
                        }
                    }
                },
                {
                    "name": "\u8d5b\u76ee\u79d1\u6280",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,51,84)"
                        }
                    }
                },
                {
                    "name": "\u8fbe\u89c2\u6570\u636e",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,87,83)"
                        }
                    }
                },
                {
                    "name": "Gostudy",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,41,31)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u667a\u6167",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,12,154)"
                        }
                    }
                },
                {
                    "name": "\u667a\u62d3\u89c6\u754c",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,141,106)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5c1a\u79d1\u6280",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,125,158)"
                        }
                    }
                },
                {
                    "name": "\u638c\u95e8\u6559\u80b2",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,159,70)"
                        }
                    }
                },
                {
                    "name": "\u4eac\u4e1c\u96c6\u56e2",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,134,35)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u7c73\u96c6\u56e2",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,63,144)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u597d\u5b66",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,48,150)"
                        }
                    }
                },
                {
                    "name": "Aibee",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,40,86)"
                        }
                    }
                },
                {
                    "name": "\u6587\u5411\u4e7e",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,16,14)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u81f4",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,92,119)"
                        }
                    }
                },
                {
                    "name": "\u9605\u6587\u96c6\u56e2",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,90,62)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u624b",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,106,63)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77\u6c38\u8f89\u8d85\u5e02\u6709\u9650\u516c\u53f8",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,46,125)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77\u6cdb\u89c6\u89d2",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,98,109)"
                        }
                    }
                },
                {
                    "name": "\u84dd\u6e56",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,127,113)"
                        }
                    }
                },
                {
                    "name": "\u6b63\u96c5\u9f7f\u79d1",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,117,39)"
                        }
                    }
                },
                {
                    "name": "\u6749\u6570\u79d1\u6280",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,157,108)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u6da6\u5bcc\u8054",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,69,4)"
                        }
                    }
                },
                {
                    "name": "\u6155\u601d\u5065\u5eb7\u7761\u7720",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,32,156)"
                        }
                    }
                },
                {
                    "name": "\u5219\u4e00\u4f9b\u5e94\u94fe",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,48,100)"
                        }
                    }
                },
                {
                    "name": "\u730e\u6237\u661f\u7a7a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,108,46)"
                        }
                    }
                },
                {
                    "name": "\u534e\u4e3a\u6280\u672f\u6709\u9650\u516c\u53f8",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,28,48)"
                        }
                    }
                },
                {
                    "name": "Roborock",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,108,3)"
                        }
                    }
                },
                {
                    "name": "\u4f2f\u6069\u5149\u5b66",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,151,32)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u5b8f\u74f4\u79d1\u6280\u53d1\u5c55\u6709\u9650...",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,74,58)"
                        }
                    }
                },
                {
                    "name": "\u5600\u55d2\u51fa\u884c",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,156,74)"
                        }
                    }
                },
                {
                    "name": "\u8fc5\u96f7",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,102,77)"
                        }
                    }
                },
                {
                    "name": "TalkingData",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,139,135)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u4e1c\u4e09\u7ef4\u5bb6\u4fe1\u606f\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,156,131)"
                        }
                    }
                },
                {
                    "name": "GYENNO",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,70,7)"
                        }
                    }
                },
                {
                    "name": "\u706b\u773c\u4e91",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,35,121)"
                        }
                    }
                },
                {
                    "name": "\u660e\u7565\u79d1\u6280\u96c6\u56e2",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,111,115)"
                        }
                    }
                },
                {
                    "name": "\u5cb1\u609f\u667a\u80fd",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,142,103)"
                        }
                    }
                },
                {
                    "name": "360",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,128,60)"
                        }
                    }
                },
                {
                    "name": "\u5341\u4e5d\u8857\u4eba\u529b\u8d44\u6e90\u7ba1\u7406",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,43,57)"
                        }
                    }
                },
                {
                    "name": "\u8682\u8681\u96c6\u56e2",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,3,95)"
                        }
                    }
                },
                {
                    "name": "\u5706\u901a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,154,35)"
                        }
                    }
                },
                {
                    "name": "\u597d\u5927\u592b\u5728\u7ebf",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,73,3)"
                        }
                    }
                },
                {
                    "name": "\u5b9d\u5b9d\u6811",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,111,143)"
                        }
                    }
                },
                {
                    "name": "\u6597\u9c7c\u76f4\u64ad",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,71,111)"
                        }
                    }
                },
                {
                    "name": "\u6765\u672a\u6765",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,121,14)"
                        }
                    }
                },
                {
                    "name": "vivo",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,5,137)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u6df1\u79d1\u6280",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,83,64)"
                        }
                    }
                },
                {
                    "name": "\u643a\u7a0b\u96c6\u56e2",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,147,133)"
                        }
                    }
                },
                {
                    "name": "\u5c71\u666f\u667a\u80fd",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,61,150)"
                        }
                    }
                },
                {
                    "name": "\u56db\u5408\u5929\u5730",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,38,143)"
                        }
                    }
                },
                {
                    "name": "\u54d4\u54e9\u54d4\u54e9",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,131,3)"
                        }
                    }
                },
                {
                    "name": "\u5357\u6e56\u9662",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,25,46)"
                        }
                    }
                },
                {
                    "name": "\u5927\u540d\u8f6f\u4ef6",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,105,4)"
                        }
                    }
                },
                {
                    "name": "\u7279\u65af\u8054",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,127,154)"
                        }
                    }
                },
                {
                    "name": "\u683c\u7075\u6df1\u77b3",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,42,68)"
                        }
                    }
                },
                {
                    "name": "\u5929\u55bb\u4fe1\u606f",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,90,95)"
                        }
                    }
                },
                {
                    "name": "\u5151\u5427",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,104,114)"
                        }
                    }
                },
                {
                    "name": "\u9890\u90a6\u79d1\u6280",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,59,151)"
                        }
                    }
                },
                {
                    "name": "\u58f0\u667a\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,110,54)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5c1a\u535a\u745e",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,103,95)"
                        }
                    }
                },
                {
                    "name": "\u89c2\u8fdc\u6570\u636e",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,156,130)"
                        }
                    }
                },
                {
                    "name": "\u601d\u7ef4\u9020\u7269",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,114,96)"
                        }
                    }
                },
                {
                    "name": "\u6ef4\u666e\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,160,138)"
                        }
                    }
                },
                {
                    "name": "\u7269\u754c\uff08\u4e0a\u6d77\uff09\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,21,36)"
                        }
                    }
                },
                {
                    "name": "ZOOM",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,118,85)"
                        }
                    }
                },
                {
                    "name": "\u6dfb\u695a\u701a\u624d\u4f20\u5a92",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,96,99)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u76c8\u745e\u6052",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,18,49)"
                        }
                    }
                },
                {
                    "name": "FunPlus \u8da3\u52a0\u6e38\u620f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,73,121)"
                        }
                    }
                },
                {
                    "name": "Mobvista",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,56,15)"
                        }
                    }
                },
                {
                    "name": "\u73e0\u6d77\u4f18\u7279\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,153,102)"
                        }
                    }
                },
                {
                    "name": "\u4eac\u4e1c\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,156,103)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u6d6a\u91d1\u878d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,89,8)"
                        }
                    }
                },
                {
                    "name": "\u827e\u8fc8\u79d1\u65af\u5a92\u4f53\u79d1\u6280\uff08\u5317\u4eac\uff09\u6709\u9650\u516c\u53f8",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,102,61)"
                        }
                    }
                },
                {
                    "name": "\u641c\u624d\u4eba\u529b\u8d44\u6e90",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,138,129)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u9c7c\u6613\u8fde",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,96,1)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u533b\u7597",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,159,77)"
                        }
                    }
                },
                {
                    "name": "\u9cb2\u9e4f\u4e91\u667a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,145,16)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u5c71\u529e\u516c\u8f6f\u4ef6",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,110,135)"
                        }
                    }
                },
                {
                    "name": "\u521b\u65b0\u5947\u667a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,58,108)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u79d1\u5f18\u4e91",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,116,134)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u97f3\u667a\u80fd\u79d1\u6280  SpeakIn",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,2,74)"
                        }
                    }
                },
                {
                    "name": "\u5916\u8111\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,143,124)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u56fd\u90ae\u653f\u50a8\u84c4\u94f6\u884c",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,147,81)"
                        }
                    }
                },
                {
                    "name": "\u9cb8\u822a\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,25,85)"
                        }
                    }
                },
                {
                    "name": "Moka",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,84,10)"
                        }
                    }
                },
                {
                    "name": "\u6781\u5149",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,83,121)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e4b\u6613",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,104,154)"
                        }
                    }
                },
                {
                    "name": "\u574e\u5fb7\u62c9",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,134,21)"
                        }
                    }
                },
                {
                    "name": "\u676d\u5dde\u667a\u56e2",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,146,31)"
                        }
                    }
                },
                {
                    "name": "AKULAKU",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,52,65)"
                        }
                    }
                },
                {
                    "name": "\u4e50\u6211\u65e0\u9650",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,71,52)"
                        }
                    }
                },
                {
                    "name": "Disney+Hotstar",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,43,9)"
                        }
                    }
                },
                {
                    "name": "\u4eb2\u5b9d\u5b9d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,24,106)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u89c6\u521b\u65b0",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,99,14)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u77e5\u672a\u6765",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,94,48)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u5065\u5eb7",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,51,105)"
                        }
                    }
                },
                {
                    "name": "\u539a\u6734\u6c47\u667a\u54a8\u8be2",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,27,122)"
                        }
                    }
                },
                {
                    "name": "\u6570\u5b57\u7eff\u571f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,60,19)"
                        }
                    }
                },
                {
                    "name": "\u8304\u5b50\u5feb\u4f20",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,111,107)"
                        }
                    }
                },
                {
                    "name": "\u4f73\u987a\u667a\u80fd\u673a\u5668\u4eba",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,36,100)"
                        }
                    }
                },
                {
                    "name": "\u533b\u836f\u9b54\u65b9",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,107,101)"
                        }
                    }
                },
                {
                    "name": "\u888b\u9f20\u4e91",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,136,158)"
                        }
                    }
                },
                {
                    "name": "\u53ee\u549a\u4e70\u83dc",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,61,19)"
                        }
                    }
                },
                {
                    "name": "\u767e\u878d\u4e91\u521b",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,66,88)"
                        }
                    }
                },
                {
                    "name": "\u9a6c\u4e0a\u8d62",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,140,133)"
                        }
                    }
                },
                {
                    "name": "\u6210\u90fd\u62df\u5408\u672a\u6765\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,116,126)"
                        }
                    }
                },
                {
                    "name": "\u534e\u5927\u7814\u7a76\u9662",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,19,84)"
                        }
                    }
                },
                {
                    "name": "\u5168\u65f6",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,58,51)"
                        }
                    }
                },
                {
                    "name": "\u8d5b\u601d\u4fe1\u5b89",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,82,24)"
                        }
                    }
                },
                {
                    "name": "\u6d3e\u5ba2\u6734\u98df",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,129,137)"
                        }
                    }
                },
                {
                    "name": "\u5143\u6a61\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,152,141)"
                        }
                    }
                },
                {
                    "name": "\u6570\u5764\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,110,30)"
                        }
                    }
                },
                {
                    "name": "\u58a8\u4e91\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,115,139)"
                        }
                    }
                },
                {
                    "name": "westwell\u897f\u4e95\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,131,139)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6167\u82bd",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,76,52)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u4ea7\u9669",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,156,19)"
                        }
                    }
                },
                {
                    "name": "\u54c1\u89c8Pinlan",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,52,132)"
                        }
                    }
                },
                {
                    "name": "\u4e07\u79d1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,66,60)"
                        }
                    }
                },
                {
                    "name": "\u8611\u83c7\u8857",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,94,2)"
                        }
                    }
                },
                {
                    "name": "\u9646\u91d1\u6240",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,155,155)"
                        }
                    }
                },
                {
                    "name": "\u835f\u8bda\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,5,115)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u62cd\u5802",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,112,78)"
                        }
                    }
                },
                {
                    "name": "\u9ea6\u5b50\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,153,46)"
                        }
                    }
                },
                {
                    "name": "\u676d\u5dde\u9886\u89c1\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,83,152)"
                        }
                    }
                },
                {
                    "name": "\u521b\u90bb\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,46,78)"
                        }
                    }
                },
                {
                    "name": "StepBeats",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,120,150)"
                        }
                    }
                },
                {
                    "name": "\u6dfb\u624d\u4f01\u4e1a\u7ba1\u7406\u54a8\u8be2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,151,4)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u56fe\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,64,125)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u5f71APP",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,108,97)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u8ff9\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,68,0)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u90ae\u4fe1\u606f\u79d1\u6280\uff08\u5317\u4eac\uff09\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,129,109)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u6e90\u6052\u9645",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,19,112)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u901a\u5feb\u9012",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,29,61)"
                        }
                    }
                },
                {
                    "name": "\u6807\u8d1d\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,89,140)"
                        }
                    }
                },
                {
                    "name": "\u6e56\u5317\u4e5d\u540c\u65b9\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,124,78)"
                        }
                    }
                },
                {
                    "name": "\u8861\u660a\u6570\u636e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,93,8)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u770b\u6f2b\u753b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,35,100)"
                        }
                    }
                },
                {
                    "name": "\u7c89\u8c61\u751f\u6d3b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,84,38)"
                        }
                    }
                },
                {
                    "name": "\u601d\u8d24\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,100,13)"
                        }
                    }
                },
                {
                    "name": "\u817e\u8baf\u97f3\u4e50",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,60,76)"
                        }
                    }
                },
                {
                    "name": "\u7fcc\u65e5\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,55,101)"
                        }
                    }
                },
                {
                    "name": "\u521b\u6cf0\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,103,127)"
                        }
                    }
                },
                {
                    "name": "\u65f6\u8da3social-touch",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,0,142)"
                        }
                    }
                },
                {
                    "name": "\u8fc1\u79fb\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,97,103)"
                        }
                    }
                },
                {
                    "name": "\u6709\u4e3a\u4fe1\u606f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,66,107)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u725b\u7535\u52a8\u8f66",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,78,18)"
                        }
                    }
                },
                {
                    "name": "\u7b2c\u4e09\u77f3\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,48,125)"
                        }
                    }
                },
                {
                    "name": "\u8da3\u94fe\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,42,58)"
                        }
                    }
                },
                {
                    "name": "RealAI",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,129,59)"
                        }
                    }
                },
                {
                    "name": "\u4f34\u9c7c",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,152,151)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u5c71\u4e16\u6e38",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,26,58)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u65b9\u56fd\u4fe1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,71,121)"
                        }
                    }
                },
                {
                    "name": "\u9053\u8fbe\u5929\u9645",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,56,46)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5e0c\u671b\u516d\u548c",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,46,118)"
                        }
                    }
                },
                {
                    "name": "PowerVision",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,83,76)"
                        }
                    }
                },
                {
                    "name": "\u84dd\u6708\u4eae",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,47,116)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u539f\u6d88\u8d39\u91d1\u878d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,40,10)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u58f0\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,46,42)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u5e02\u5a01\u5bcc\u89c6\u754c\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,133,58)"
                        }
                    }
                },
                {
                    "name": "Rokid",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,75,78)"
                        }
                    }
                },
                {
                    "name": "\u89c6+AR",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,158,84)"
                        }
                    }
                },
                {
                    "name": "\u7279\u8d5e|Tezign",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,44,2)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u67d4\u521b\u65b0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,79,69)"
                        }
                    }
                },
                {
                    "name": "\u8eba\u5e73\u8bbe\u8ba1\u5bb6",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,58,134)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u7267\u539f\u6570\u5b57\u6280\u672f\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,119,61)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u535a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,53,46)"
                        }
                    }
                },
                {
                    "name": "LinkDoc",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,129,21)"
                        }
                    }
                },
                {
                    "name": "\u5f71\u7b11\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,40,6)"
                        }
                    }
                },
                {
                    "name": "\u97e9\u521b\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,146,38)"
                        }
                    }
                },
                {
                    "name": "Flash express",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,99,66)"
                        }
                    }
                },
                {
                    "name": "\u8de8\u8d8a\u901f\u8fd0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,76,156)"
                        }
                    }
                },
                {
                    "name": "\u7d2b\u5149\u6559\u80b2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,120,111)"
                        }
                    }
                },
                {
                    "name": "\u5927\u7bb4\uff08\u676d\u5dde\uff09\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,117,93)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u8111\u94f6\u6cb3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,130,126)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u7684\u96c6\u56e2IT",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,155,66)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u65b9\u548c\u5317\u4eac",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,138,65)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u91ce\u91d1\u878d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,72,138)"
                        }
                    }
                },
                {
                    "name": "\u64ce\u76fe\u6570\u636e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,132,134)"
                        }
                    }
                },
                {
                    "name": "\u6d6a\u6dd8\u91d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,86,124)"
                        }
                    }
                },
                {
                    "name": "\u521b\u5fc5\u627f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,123,147)"
                        }
                    }
                },
                {
                    "name": "\u5408\u5408\u4fe1\u606f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,130,102)"
                        }
                    }
                },
                {
                    "name": "\u8389\u8389\u4e1d\u6e38\u620f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,87,49)"
                        }
                    }
                },
                {
                    "name": "\u661f\u8206\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,74,108)"
                        }
                    }
                },
                {
                    "name": "\u8c61\u8f91\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,83,155)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u91cf\u8d28\u5b50",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,8,103)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u5965\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,3,94)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u65b9\u660e\u73e0\u65b0\u5a92\u4f53",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,87,51)"
                        }
                    }
                },
                {
                    "name": "\u8d5b\u9c81\u73ed",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,32,27)"
                        }
                    }
                },
                {
                    "name": "\u534e\u6c49\u4f1f\u4e1a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,128,5)"
                        }
                    }
                },
                {
                    "name": "\u6613\u822a\u667a\u80fd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,88,158)"
                        }
                    }
                },
                {
                    "name": "\u7279\u9e4f\u7f51\u7edc",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,143,78)"
                        }
                    }
                },
                {
                    "name": "\u56db\u5ddd\u5f18\u548c\u96c6\u56e2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,158,78)"
                        }
                    }
                },
                {
                    "name": "\u6d3e\u8fe9",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,151,53)"
                        }
                    }
                },
                {
                    "name": "\u57c3\u514b\u65af\u5de5\u4e1a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,153,123)"
                        }
                    }
                },
                {
                    "name": "\u6570\u6f9c\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,83,101)"
                        }
                    }
                },
                {
                    "name": "\u6c47\u667a\u4f17\u5fc3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,9,40)"
                        }
                    }
                },
                {
                    "name": "LAYABOX",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,70,150)"
                        }
                    }
                },
                {
                    "name": "\u534e\u98de\u6570\u636e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,55,72)"
                        }
                    }
                },
                {
                    "name": "Walmart China",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,128,64)"
                        }
                    }
                },
                {
                    "name": "\u71e7\u4eba\u533b\u7597",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,114,106)"
                        }
                    }
                },
                {
                    "name": "\u6cfd\u97f6\u667a\u80fd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,93,9)"
                        }
                    }
                },
                {
                    "name": "\u6c5f\u884c\u667a\u80fd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,103,82)"
                        }
                    }
                },
                {
                    "name": "INDEMIND",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,9,98)"
                        }
                    }
                },
                {
                    "name": "Uni-Ubi",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,109,123)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u5a31\u65f6\u5149",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,52,30)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5927\u701a\u4eba\u529b\u8d44\u6e90\u7ba1\u7406",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,77,88)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u5dde\u5c0f\u8fc8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,140,72)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u4fe1\u65f6\u4ee3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,26,112)"
                        }
                    }
                },
                {
                    "name": "\u7384\u6b66\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,96,136)"
                        }
                    }
                },
                {
                    "name": "\u8fc8\u6da6\u667a\u80fd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,145,61)"
                        }
                    }
                },
                {
                    "name": "\u65f6\u7a7a\u9053\u5b87",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,82,62)"
                        }
                    }
                },
                {
                    "name": "\u6676\u6cf0\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,51,158)"
                        }
                    }
                },
                {
                    "name": "\u534e\u4fe1\u96c6\u56e2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,51,154)"
                        }
                    }
                },
                {
                    "name": "Ximmerse",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,89,68)"
                        }
                    }
                },
                {
                    "name": "\u57c3\u6469\u68ee",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,132,80)"
                        }
                    }
                },
                {
                    "name": "\u817e\u5c55\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,93,157)"
                        }
                    }
                },
                {
                    "name": "\u4e07\u751f\u534e\u6001",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,77,59)"
                        }
                    }
                },
                {
                    "name": "\u8da3\u5934\u6761",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,82,80)"
                        }
                    }
                },
                {
                    "name": "\u4f17\u4eab\u5929\u5730",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,19,94)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u8863\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,41,96)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u64ad\u7535\u89c6\u7814\u7a76\u6240",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,43,58)"
                        }
                    }
                },
                {
                    "name": "\u90bb\u6c47\u5427",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,151,107)"
                        }
                    }
                },
                {
                    "name": "\u63a2\u9a6c\u4f01\u670d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,76,150)"
                        }
                    }
                },
                {
                    "name": "\u777f\u9b54\u667a\u80fd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,74,42)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77\u835f\u529b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,45,32)"
                        }
                    }
                },
                {
                    "name": "\u638c\u9605",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,11,24)"
                        }
                    }
                },
                {
                    "name": "\u901f\u611f\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,54,155)"
                        }
                    }
                },
                {
                    "name": "\u683c\u5170\u4ed5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,26,114)"
                        }
                    }
                },
                {
                    "name": "\u76db\u4e16\u9e92\u9e9f\u519c\u4e1a\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,126,44)"
                        }
                    }
                },
                {
                    "name": "\u8ff7\u9e7f\u97f3\u4e50",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,153,130)"
                        }
                    }
                },
                {
                    "name": "\u7d2b\u8346\u6843\u674e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,131,131)"
                        }
                    }
                },
                {
                    "name": "\u6781\u89c6\u89d2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,95,147)"
                        }
                    }
                },
                {
                    "name": "\u8206\u9686\u5174\u8fbe",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,149,73)"
                        }
                    }
                },
                {
                    "name": "\u817e\u4e91\u60a6\u667a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,19,84)"
                        }
                    }
                },
                {
                    "name": "\u997f\u4e86\u4e48",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,142,110)"
                        }
                    }
                },
                {
                    "name": "\u521d\u7075\u4fe1\u606f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,49,139)"
                        }
                    }
                },
                {
                    "name": "\u957f\u6295\u5b66\u5802",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,119,38)"
                        }
                    }
                },
                {
                    "name": "\u5929\u6e90\u8fea\u79d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,134,92)"
                        }
                    }
                },
                {
                    "name": "BLUE",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,93,86)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u6cf0\u661f\u4e91",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,149,103)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u8bc1\u80a1\u4efd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,73,91)"
                        }
                    }
                },
                {
                    "name": "\u51cc\u5b87\u667a\u63a7\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,124,157)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u5e02\u4e30\u5de2\u7f51\u7edc\u6280\u672f\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,63,71)"
                        }
                    }
                },
                {
                    "name": "\u7ecf\u4f20\u591a\u8d62",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,63,24)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u5e02\u6709\u4f20\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,151,48)"
                        }
                    }
                },
                {
                    "name": "\u601d\u56fe\u573a\u666f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,102,79)"
                        }
                    }
                },
                {
                    "name": "\u6613\u6d41",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,111,146)"
                        }
                    }
                },
                {
                    "name": "eBrain",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,68,140)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u5dde\u9ed1\u683c\u667a\u9020\u4fe1\u606f\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,33,27)"
                        }
                    }
                },
                {
                    "name": "\u6587\u5b89\u667a\u80fd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,21,157)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u5e02\u9510\u660e\u6280\u672f\u80a1\u4efd\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,147,42)"
                        }
                    }
                },
                {
                    "name": "nice",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,84,65)"
                        }
                    }
                },
                {
                    "name": "\u4e5d\u53f7\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,8,92)"
                        }
                    }
                },
                {
                    "name": "\u6700\u6709\u6599",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,121,54)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u7535\u6167\u5b89",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,124,127)"
                        }
                    }
                },
                {
                    "name": "Long Bridge",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,120,126)"
                        }
                    }
                },
                {
                    "name": "\u572d\u76ee\u673a\u5668\u4eba",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,1,115)"
                        }
                    }
                },
                {
                    "name": "\u7d2b\u5149\u534e\u667a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,99,15)"
                        }
                    }
                },
                {
                    "name": "\u534e\u6d4b\u5bfc\u822a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,48,8)"
                        }
                    }
                },
                {
                    "name": "\u6653\u6a3e\u667a\u80fd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,70,69)"
                        }
                    }
                },
                {
                    "name": "\u7075\u52a8\u97f3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,86,68)"
                        }
                    }
                },
                {
                    "name": "\u5fb7\u9002\u751f\u7269",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,32,84)"
                        }
                    }
                },
                {
                    "name": "\u8bfa\u4fe1\u521b\u8054",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,38,64)"
                        }
                    }
                },
                {
                    "name": "\u89c5\u777f\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,147,38)"
                        }
                    }
                },
                {
                    "name": "\u5929\u667a\u822a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,55,114)"
                        }
                    }
                },
                {
                    "name": "\u536b\u74f4\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,52,67)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u7586\u667a\u80fd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,27,27)"
                        }
                    }
                },
                {
                    "name": "\u661f\u5c18\u6570\u636e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,70,83)"
                        }
                    }
                },
                {
                    "name": "\u84dd\u9e3d\u96c6\u56e2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,55,82)"
                        }
                    }
                },
                {
                    "name": "\u54d7\u5566\u5566",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,44,129)"
                        }
                    }
                },
                {
                    "name": "\u8354\u679d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,136,124)"
                        }
                    }
                },
                {
                    "name": "\u677e\u7acb\u63a7\u80a1\u96c6\u56e2\u80a1\u4efd\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,128,57)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u65b0\u6c27\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,105,135)"
                        }
                    }
                },
                {
                    "name": "\u534e\u91cc\u7f51\u7edc",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,15,14)"
                        }
                    }
                },
                {
                    "name": "\u683c\u6717\u5bb6",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,129,112)"
                        }
                    }
                },
                {
                    "name": "\u6b66\u6c49\u9536\u5170\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,124,29)"
                        }
                    }
                },
                {
                    "name": "\u53ca\u672a\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,14,120)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u96f6\u8dc3\u52a8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,135,69)"
                        }
                    }
                },
                {
                    "name": "\u6cf0\u5766\u667a\u6167",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,44,68)"
                        }
                    }
                },
                {
                    "name": "\u8bc1\u901a\u7535\u5b50",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,104,131)"
                        }
                    }
                },
                {
                    "name": "YY",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,145,104)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u5e2e\u7535\u5b50",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,4,109)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u56fd\u77f3\u6cb9\u5929\u7136\u6c14\u7ba1\u9053\u5de5\u7a0b\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,18,12)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u72d7\u6253\u8f66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,83,23)"
                        }
                    }
                },
                {
                    "name": "\u65af\u683c\u56fd\u9645",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,34,9)"
                        }
                    }
                },
                {
                    "name": "\u7ea2\u84ddCP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,104,99)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u8c61\u4f18\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,94,81)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77\u745e\u72ee\u7f51\u7edc\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,84,125)"
                        }
                    }
                },
                {
                    "name": "\u51b0\u6cb3\u4e91\u5b58\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,121,88)"
                        }
                    }
                },
                {
                    "name": "\u9cb8\u7b97\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,71,126)"
                        }
                    }
                },
                {
                    "name": "\u84dd\u706f\u9c7c\u667a\u80fd\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,89,68)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u8fbe\u8f6f\u4ef6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,62,32)"
                        }
                    }
                },
                {
                    "name": "\u4f5c\u4e1a\u5e2e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,51,29)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u9510\u56fd\u9645",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,108,133)"
                        }
                    }
                },
                {
                    "name": "\u548c\u7f8e\u4fe1\u606f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,94,143)"
                        }
                    }
                },
                {
                    "name": "\u7545\u884c\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,108,110)"
                        }
                    }
                },
                {
                    "name": "\u8d28\u5b50\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,35,12)"
                        }
                    }
                },
                {
                    "name": "\u5357\u74dc\u7535\u5f71",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,55,60)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5723\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,2,152)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u9f9f\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,62,125)"
                        }
                    }
                },
                {
                    "name": "\u5531\u5427-\u73a9\u97f3\u4e50\uff0c\u5c31\u4e0a\u5531\u5427\uff01",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,123,152)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u91cd\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,129,71)"
                        }
                    }
                },
                {
                    "name": "\u6253\u626e\u5bb6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,52,156)"
                        }
                    }
                },
                {
                    "name": "\u5357\u4eac\u6c47\u5ddd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,30,75)"
                        }
                    }
                },
                {
                    "name": "\u4f73\u5146\u4e1a\u6295\u8d44\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,51,20)"
                        }
                    }
                },
                {
                    "name": "\u597d\u672a\u6765",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,78,30)"
                        }
                    }
                },
                {
                    "name": "\u6cf0\u5eb7\u4fdd\u9669\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,135,115)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u6b65\u5728\u5bb6\u65e9\u6559",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,111,26)"
                        }
                    }
                },
                {
                    "name": "\u6570\u777f\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,39,139)"
                        }
                    }
                },
                {
                    "name": "InMobi",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,146,108)"
                        }
                    }
                },
                {
                    "name": "\u8d62\u706b\u866b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,35,101)"
                        }
                    }
                },
                {
                    "name": "\u8fc8\u7279\u56fd\u9645\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,47,27)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u5168\u751f\u4ea7\u79d1\u5b66\u7814\u7a76\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,13,19)"
                        }
                    }
                },
                {
                    "name": "\u949b\u6c2a\u65b0\u5a92\u4f53\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,120,2)"
                        }
                    }
                },
                {
                    "name": "\u660e\u671d\u4e07\u8fbe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,42,81)"
                        }
                    }
                },
                {
                    "name": "\u6708\u76db\u658b\u6295\u8d44\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,129,92)"
                        }
                    }
                },
                {
                    "name": "\u963f\u91cc\u5df4\u5df4-\u9ad8\u5fb7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,83,146)"
                        }
                    }
                },
                {
                    "name": "\u534e\u5f55\u8d85\u6e05\u6587\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,101,159)"
                        }
                    }
                },
                {
                    "name": "\u7eff\u6f2b\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,149,47)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u70b9\u8d44\u8baf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,48,150)"
                        }
                    }
                },
                {
                    "name": "Gridsum \u56fd\u53cc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,40,160)"
                        }
                    }
                },
                {
                    "name": "\u878d\u4e3a\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,4,121)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u7535",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,132,84)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u4e91\u5929\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,147,42)"
                        }
                    }
                },
                {
                    "name": "\u5b9d\u5c0a\u7535\u5546",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,49,39)"
                        }
                    }
                },
                {
                    "name": "\u9518\u5d34\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,129,55)"
                        }
                    }
                },
                {
                    "name": "\u827e\u5fb7\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,70,101)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u7ea7\u7329\u7329\u5065\u8eab",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,95,35)"
                        }
                    }
                },
                {
                    "name": "\u6c57\u9a6c\u4fe1\u606f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,30,27)"
                        }
                    }
                },
                {
                    "name": "GALASPORTS",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,72,136)"
                        }
                    }
                },
                {
                    "name": "\u987a\u4e30\u540c\u57ce",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,135,69)"
                        }
                    }
                },
                {
                    "name": "\u63a2\u9488\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,91,54)"
                        }
                    }
                },
                {
                    "name": "\u4e70\u4e70\u53cb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,81,81)"
                        }
                    }
                },
                {
                    "name": "\u5e93\u73c0\u6052\u5b89",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,91,51)"
                        }
                    }
                },
                {
                    "name": "\u95ea\u5e03\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,2,5)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u6444",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,73,81)"
                        }
                    }
                },
                {
                    "name": "\u9c81\u73ed\u5ae1\u7cfb\u673a\u5668\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,26,107)"
                        }
                    }
                },
                {
                    "name": "\u4f0a\u6fb3\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,108,147)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u839e\u7f8e\u5b9c\u4f73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,25,56)"
                        }
                    }
                },
                {
                    "name": "\u667a\u795e\u4fe1\u606f\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,144,99)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u6f14\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,3,160)"
                        }
                    }
                },
                {
                    "name": "\u9b54\u7b77\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,80,29)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u7535\u535a\u4e9a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,127,94)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u667a\u7c73\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,42,94)"
                        }
                    }
                },
                {
                    "name": "Yeahmobi",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,124,154)"
                        }
                    }
                },
                {
                    "name": "\u886b\u6570\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,139,12)"
                        }
                    }
                },
                {
                    "name": "\u5047\u9762\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,84,54)"
                        }
                    }
                },
                {
                    "name": "\u53eb\u53eb\u5b66\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,64,95)"
                        }
                    }
                },
                {
                    "name": "\u8bfa\u535a\u533b\u7597",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,155,37)"
                        }
                    }
                },
                {
                    "name": "\u4e5d\u7ae0\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,23,113)"
                        }
                    }
                },
                {
                    "name": "\u7d2b\u71d5\u65e0\u4eba\u98de\u884c\u5668",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,132,145)"
                        }
                    }
                },
                {
                    "name": "\u7279\u65af\u62c9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,137,97)"
                        }
                    }
                },
                {
                    "name": "\u827e\u8015\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,88,0)"
                        }
                    }
                },
                {
                    "name": "\u82cf\u7f19\u4f01\u4e1a\u7ba1\u7406\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,151,69)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5c14\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,62,158)"
                        }
                    }
                },
                {
                    "name": "\u8d1d\u53f6\u65af\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,29,5)"
                        }
                    }
                },
                {
                    "name": "Riley Cillian\u83b1\u7199\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,25,74)"
                        }
                    }
                },
                {
                    "name": "\u4e50\u5176\u7535\u5546",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,112,158)"
                        }
                    }
                },
                {
                    "name": "\u5988\u5988\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,157,86)"
                        }
                    }
                },
                {
                    "name": "\u89e6\u5b9d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,81,30)"
                        }
                    }
                },
                {
                    "name": "\u5927\u4e13\u5bb6.COM",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,7,71)"
                        }
                    }
                },
                {
                    "name": "\u8fdc\u7738\u8f6f\u4ef6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,158,151)"
                        }
                    }
                },
                {
                    "name": "\u8def\u884c\u901a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,81,118)"
                        }
                    }
                },
                {
                    "name": "\u6f2b\u5fae\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,57,155)"
                        }
                    }
                },
                {
                    "name": "\u4f0a\u5bf9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,30,57)"
                        }
                    }
                },
                {
                    "name": "\u878d360",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,22,19)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u79df\u8d41",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,8,154)"
                        }
                    }
                },
                {
                    "name": "\u73de\u73c8\u4f17\u6052",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,1,113)"
                        }
                    }
                },
                {
                    "name": "\u745b\u592a\u83b1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,138,94)"
                        }
                    }
                },
                {
                    "name": "\u71b5\u7b80\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,62,64)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u4e50\u79cd\u5b50",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,5,141)"
                        }
                    }
                },
                {
                    "name": "\u82f1\u8bed\u8da3\u914d\u97f3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,37,100)"
                        }
                    }
                },
                {
                    "name": "\u7231\u8bed\u5427",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,86,81)"
                        }
                    }
                },
                {
                    "name": "\u6e05\u534e\u540c\u65b9\u7269\u8054\u7f51\u672c\u90e8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,153,79)"
                        }
                    }
                },
                {
                    "name": "\u81f3\u771f\u4e92\u8054",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,25,69)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u6b65\u7f51\u7edc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,160,2)"
                        }
                    }
                },
                {
                    "name": "\u6c38\u8f89\u4e91\u521b\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,114,113)"
                        }
                    }
                },
                {
                    "name": "\u963f\u91cc\u5df4\u5df4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,47,97)"
                        }
                    }
                },
                {
                    "name": "\u8da3\u4e38",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,23,156)"
                        }
                    }
                },
                {
                    "name": "\u534e\u783a\u667a\u884c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,95,7)"
                        }
                    }
                },
                {
                    "name": "\u76ef\u76ef\u62cd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,23,4)"
                        }
                    }
                },
                {
                    "name": "\u4f9d\u56fe\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,97,69)"
                        }
                    }
                },
                {
                    "name": "\u672a\u6765\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,6,8)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u7f8e\u63a7\u80a1\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,121,93)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u5dde\u6e38\u7231",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,126,88)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u987f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,64,142)"
                        }
                    }
                },
                {
                    "name": "\u96c5\u4e50\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,154,153)"
                        }
                    }
                },
                {
                    "name": "\u73af\u7403\u8f66\u4eab",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,160,145)"
                        }
                    }
                },
                {
                    "name": "\u65b9\u4ed5\u8fbe\u4f01\u4e1a\u7ba1\u7406\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,63,47)"
                        }
                    }
                },
                {
                    "name": "\u7a0e\u53cb\u8f6f\u4ef6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,103,48)"
                        }
                    }
                },
                {
                    "name": "\u8f7b\u8f7b\u6559\u80b2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,56,88)"
                        }
                    }
                },
                {
                    "name": "Stepone",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,106,85)"
                        }
                    }
                },
                {
                    "name": "\u540d\u7af9\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,139,78)"
                        }
                    }
                },
                {
                    "name": "\u8c46\u679c\u7f8e\u98df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,138,67)"
                        }
                    }
                },
                {
                    "name": "\u9752\u56e2\u793e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,80,78)"
                        }
                    }
                },
                {
                    "name": "\u5341\u835f\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,145,31)"
                        }
                    }
                },
                {
                    "name": "\u96ea\u7403",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,123,124)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u5219\u4f18",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,86,100)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u7814\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,46,39)"
                        }
                    }
                },
                {
                    "name": "\u6167\u62e9\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,121,157)"
                        }
                    }
                },
                {
                    "name": "\u6b66\u6c49\u8fea\u8d5b\u5a01\u667a\u80fd\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,8,109)"
                        }
                    }
                },
                {
                    "name": "\u6210\u90fd\u5927\u6570\u636e\u4ea7\u4e1a\u6280\u672f\u7814\u7a76\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,43,4)"
                        }
                    }
                },
                {
                    "name": "\u6613\u9274\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,51,142)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u7280\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,62,100)"
                        }
                    }
                },
                {
                    "name": "\u6469\u822a\u65f6\u4ee3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,149,147)"
                        }
                    }
                },
                {
                    "name": "\u9b54\u98de\u7f51\u7edc-\u8f66\u8f7d\u5a31\u4e50",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,114,16)"
                        }
                    }
                },
                {
                    "name": "\u8f66\u597d\u591a\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,14,42)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u4e4e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,19,6)"
                        }
                    }
                },
                {
                    "name": "\u667a\u8d1d\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,0,84)"
                        }
                    }
                },
                {
                    "name": "\u60e0\u84c9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,22,7)"
                        }
                    }
                },
                {
                    "name": "MetaApp",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,129,77)"
                        }
                    }
                },
                {
                    "name": "\u8f7b\u677e\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,51,0)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u5370\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,50,83)"
                        }
                    }
                },
                {
                    "name": "\u4f20\u5174\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,66,23)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u901a\u8f6f\u4ef6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,97,81)"
                        }
                    }
                },
                {
                    "name": "\u827e\u7f8e\u7f51\u7edc\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,86,17)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77\u5594\u8da3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,57,77)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u6269\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,5,159)"
                        }
                    }
                },
                {
                    "name": "\u5965\u7279\u7ef4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,88,0)"
                        }
                    }
                },
                {
                    "name": "\u592a\u521d\u5f08\u5baa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,106,45)"
                        }
                    }
                },
                {
                    "name": "\u711c\u8000\u7f51\u7edc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,96,93)"
                        }
                    }
                },
                {
                    "name": "\u8c61\u5fc3\u529b\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,131,77)"
                        }
                    }
                },
                {
                    "name": "\u5a5a\u793c\u7eaa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,106,139)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u7535\u79d1\u98ce\u534e\u4fe1\u606f\u88c5\u5907\u80a1\u4efd\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,73,51)"
                        }
                    }
                },
                {
                    "name": "\u667a\u9f7f\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,100,36)"
                        }
                    }
                },
                {
                    "name": "\u6570\u5b57\u4ea7\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,62,2)"
                        }
                    }
                },
                {
                    "name": "\u6c85\u9038\u65b9\u8fbe\u7ba1\u7406\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,136,61)"
                        }
                    }
                },
                {
                    "name": "\u4e16\u7eaa\u4f73\u7f18",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,44,19)"
                        }
                    }
                },
                {
                    "name": "\u79cd\u68a6\u5ba2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,85,99)"
                        }
                    }
                },
                {
                    "name": "\u8d2d\u7269\u515a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,83,37)"
                        }
                    }
                },
                {
                    "name": "\u5353\u671b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,64,158)"
                        }
                    }
                },
                {
                    "name": "Mai",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,72,9)"
                        }
                    }
                },
                {
                    "name": "\u8054\u901a\u65f6\u79d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,59,81)"
                        }
                    }
                },
                {
                    "name": "\u5c0fi\u673a\u5668\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,79,106)"
                        }
                    }
                },
                {
                    "name": "\u7ec7\u70b9\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,136,13)"
                        }
                    }
                },
                {
                    "name": "\u4ebf\u8058\u4e16\u7eaa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,46,19)"
                        }
                    }
                },
                {
                    "name": "\u72ee\u6865\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,43,138)"
                        }
                    }
                },
                {
                    "name": "\u90a6\u5b9a\u667a\u6167",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,71,84)"
                        }
                    }
                },
                {
                    "name": "\u84dd\u8bfa\u5fae\u94f6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,23,66)"
                        }
                    }
                },
                {
                    "name": "\u6f8e\u601d\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,18,71)"
                        }
                    }
                },
                {
                    "name": "Kika Tech(\u65b0\u7f8e\u4e92\u901a)",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,126,155)"
                        }
                    }
                },
                {
                    "name": "\u7384\u5173\u5065\u5eb7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,140,47)"
                        }
                    }
                },
                {
                    "name": "\u540c\u82b1\u987a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,83,54)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u987e\u4eba\u529b\u8d44\u6e90",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,89,90)"
                        }
                    }
                },
                {
                    "name": "CraiditX",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,154,38)"
                        }
                    }
                },
                {
                    "name": "\u53f8\u5357\u6570\u636e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,122,97)"
                        }
                    }
                },
                {
                    "name": "\u5373\u6784\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,128,69)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u5f99\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,139,47)"
                        }
                    }
                },
                {
                    "name": "\u6613\u5c45\u4e2d\u56fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,24,147)"
                        }
                    }
                },
                {
                    "name": "\u6613\u79d1\u5947\u901a\u4fe1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,1,23)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u5730\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,68,119)"
                        }
                    }
                },
                {
                    "name": "\u4f9d\u777f\u8fea\u4e9a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,140,47)"
                        }
                    }
                },
                {
                    "name": "\u535a\u5353\u4f01\u4e1a\u7ba1\u7406\u54a8\u8be2\u670d\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,159,150)"
                        }
                    }
                },
                {
                    "name": "\u5bfa\u5e93",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,14,119)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u6c11\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,47,50)"
                        }
                    }
                },
                {
                    "name": "\u540c\u6e29\u5c42",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,50,123)"
                        }
                    }
                },
                {
                    "name": "\u96c5\u65af\u59ae",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,110,1)"
                        }
                    }
                },
                {
                    "name": "\u638c\u4e0a\u5148\u673a-\u65fa\u5e97\u901aERP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,113,3)"
                        }
                    }
                },
                {
                    "name": "\u7c73\u96c5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,23,133)"
                        }
                    }
                },
                {
                    "name": "\u96f7\u5ea6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,56,105)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u70b9\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,50,72)"
                        }
                    }
                },
                {
                    "name": "\u878d\u6613\u63a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,131,12)"
                        }
                    }
                },
                {
                    "name": "KLOOK \u5ba2\u8def\u65c5\u884c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,47,121)"
                        }
                    }
                },
                {
                    "name": "\u6676\u786e\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,61,99)"
                        }
                    }
                },
                {
                    "name": "\u7231\u7acb\u5eb7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,76,34)"
                        }
                    }
                },
                {
                    "name": "\u5317\u660e\u6570\u79d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,73,120)"
                        }
                    }
                },
                {
                    "name": "\u65b9\u6b63\u624b\u8ff9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,160,157)"
                        }
                    }
                },
                {
                    "name": "WeLab\u536b\u76c8\u8054",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,87,119)"
                        }
                    }
                },
                {
                    "name": "\u5929\u6cfd\u667a\u4e91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,87,79)"
                        }
                    }
                },
                {
                    "name": "\u5495\u549a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,72,17)"
                        }
                    }
                },
                {
                    "name": "\u623f\u8f66\u5b9d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,33,105)"
                        }
                    }
                },
                {
                    "name": "\u7280\u8bed\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,59,143)"
                        }
                    }
                },
                {
                    "name": "\u8d5b\u8235\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,20,11)"
                        }
                    }
                },
                {
                    "name": "\u662f\u5fb7\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,158,27)"
                        }
                    }
                },
                {
                    "name": "Micagent",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,88,118)"
                        }
                    }
                },
                {
                    "name": "\u732b\u773c\u7535\u5f71",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,27,111)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5965\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,50,8)"
                        }
                    }
                },
                {
                    "name": "\u6210\u90fd\u8d28\u6570\u65af\u8fbe\u514b\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,117,144)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u7280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,76,27)"
                        }
                    }
                },
                {
                    "name": "\u9cb8\u6984\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,154,159)"
                        }
                    }
                },
                {
                    "name": "\u9752\u5cb3\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,47,129)"
                        }
                    }
                },
                {
                    "name": "\u667a\u610f\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,106,2)"
                        }
                    }
                },
                {
                    "name": "AutoX",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,40,160)"
                        }
                    }
                },
                {
                    "name": "AfterShip",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,54,158)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u57ce\u601d\u521b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,121,85)"
                        }
                    }
                },
                {
                    "name": "\u592a\u5b57\u6d41\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,141,52)"
                        }
                    }
                },
                {
                    "name": "\u9884\u7b56\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,139,80)"
                        }
                    }
                },
                {
                    "name": "Lazada",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,65,98)"
                        }
                    }
                },
                {
                    "name": "\u897f\u6e56\u5927\u5b66\u667a\u80fd\u4ea7\u4e1a\u7814\u7a76\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,47,140)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u9ad8\u63a7\u80a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,117,142)"
                        }
                    }
                },
                {
                    "name": "\u8054\u901a\u4e91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,78,143)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u5e02\u667a\u80fd\u5236\u9020\u8f6f\u4ef6\u5f00\u53d1\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,99,22)"
                        }
                    }
                },
                {
                    "name": "\u638c\u95e8\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,14,153)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u5e02\u865a\u62df\u73b0\u5b9e\u6280\u672f\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,109,68)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u6728\u667a\u80fd\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,73,19)"
                        }
                    }
                },
                {
                    "name": "\u6e05\u534e\u5927\u5b66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,145,121)"
                        }
                    }
                },
                {
                    "name": "\u60e0\u5408",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,149,27)"
                        }
                    }
                },
                {
                    "name": "\u864e\u7259\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,57,123)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u5929\u52b1\u98de",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,148,1)"
                        }
                    }
                },
                {
                    "name": "e\u7b7e\u5b9d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,123,51)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u5065\u5eb7\u4fdd\u9669",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,88,136)"
                        }
                    }
                },
                {
                    "name": "\u82ac\u4ee5\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,141,98)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u4e07\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,120,5)"
                        }
                    }
                },
                {
                    "name": "\u7ef4\u5ba2\u6615\u5fae",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,110,94)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u79ef\u4e92\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,57,92)"
                        }
                    }
                },
                {
                    "name": "\u7aef\u70c1\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,107,133)"
                        }
                    }
                },
                {
                    "name": "\u503c\u5f97\u4e70\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,153,35)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u949b\u673a\u5668\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,44,49)"
                        }
                    }
                },
                {
                    "name": "\u5c11\u5e74\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,74,87)"
                        }
                    }
                },
                {
                    "name": "\u535a\u4f9d\u7279",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,58,44)"
                        }
                    }
                },
                {
                    "name": "\u5a31\u516c\u4e92\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,86,48)"
                        }
                    }
                },
                {
                    "name": "\u6c47\u82f1\u8fbe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,141,89)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u9886\u4eba\u624d\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,46,47)"
                        }
                    }
                },
                {
                    "name": "\u963f\u5361\u7d22\u5916\u6559\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,118,38)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u8bc1\u5238",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,8,33)"
                        }
                    }
                },
                {
                    "name": "\u8001\u864e\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,38,9)"
                        }
                    }
                },
                {
                    "name": "\u6da6\u5efa\u80a1\u4efd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,128,0)"
                        }
                    }
                },
                {
                    "name": "\u987a\u4e30\u56fd\u9645",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,129,91)"
                        }
                    }
                },
                {
                    "name": "\u9e3f\u6cf0\u9f0e\u77f3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,120,113)"
                        }
                    }
                },
                {
                    "name": "\u6c49\u4eea\u5b57\u5e93",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,0,63)"
                        }
                    }
                },
                {
                    "name": "\u5343\u5bfb\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,118,74)"
                        }
                    }
                },
                {
                    "name": "\u6dfb\u624d\u7ff0\u683c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,149,90)"
                        }
                    }
                },
                {
                    "name": "\u6c47\u4fe1\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,112,48)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6167\u732b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,143,0)"
                        }
                    }
                },
                {
                    "name": "\u822a\u7a7a\u5927\u90fd\u5e02\u7814\u7a76\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,25,51)"
                        }
                    }
                },
                {
                    "name": "\u67cf\u7f8e\u8fea\u5eb7\u4e0a\u6d77",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,16,4)"
                        }
                    }
                },
                {
                    "name": "\u5373\u523b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,107,89)"
                        }
                    }
                },
                {
                    "name": "\u591a\u70b9\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,70,80)"
                        }
                    }
                },
                {
                    "name": "\u660e\u4e4b\u6570\u636e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,134,1)"
                        }
                    }
                },
                {
                    "name": "\u661f\u9645\u5927\u9646",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,131,133)"
                        }
                    }
                },
                {
                    "name": "\u667a\u751f\u9053\u4eba\u624d\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,59,142)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u94f6\u884c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,15,8)"
                        }
                    }
                },
                {
                    "name": "\u5915\u5915\u65f6\u4ee3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,134,94)"
                        }
                    }
                },
                {
                    "name": "\u540c\u4e3a\u6570\u7801",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,118,92)"
                        }
                    }
                },
                {
                    "name": "\u6e05\u51cc\u6587\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,146,123)"
                        }
                    }
                },
                {
                    "name": "roobo",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,68,110)"
                        }
                    }
                },
                {
                    "name": "\u534e\u4e91\u4e2d\u76db",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,106,21)"
                        }
                    }
                },
                {
                    "name": "\u7545\u804a\u5929\u4e0b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,149,45)"
                        }
                    }
                },
                {
                    "name": "\u767e\u7ef4\u91d1\u79d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,82,141)"
                        }
                    }
                },
                {
                    "name": "\u8d5b\u5427\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,89,98)"
                        }
                    }
                },
                {
                    "name": "\u9a6c\u8702\u7a9d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,22,118)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u540c\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,76,110)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u5e93\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,118,95)"
                        }
                    }
                },
                {
                    "name": "\u8ffd\u52bf\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,76,8)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u8003\u76f4\u901a\u8f66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,64,155)"
                        }
                    }
                },
                {
                    "name": "\u767b\u8679",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,151,82)"
                        }
                    }
                },
                {
                    "name": "\u535a\u5f66\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,47,105)"
                        }
                    }
                },
                {
                    "name": "\u9038\u4eab\u7535\u5b50\u5546\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,70,131)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u79d1\u805a\u4fe1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,115,101)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u7ea2\u4e66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,11,82)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u60f3\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,157,128)"
                        }
                    }
                },
                {
                    "name": "\u592a\u5e73\u6d0b\u623f\u5730\u4ea7\u7ecf\u7eaa\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,10,32)"
                        }
                    }
                },
                {
                    "name": "\u4e45\u90a6GOMO",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,136,143)"
                        }
                    }
                },
                {
                    "name": "\u661f\u836f\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,54,134)"
                        }
                    }
                },
                {
                    "name": "\u667a\u4e91\u5065\u5eb7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,4,6)"
                        }
                    }
                },
                {
                    "name": "\u8da3\u9014\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,117,74)"
                        }
                    }
                },
                {
                    "name": "\u5a01\u661f\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,144,41)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u8d62\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,159,86)"
                        }
                    }
                },
                {
                    "name": "\u4e07\u5174\u79d1\u6280\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,64,133)"
                        }
                    }
                },
                {
                    "name": "\u963f\u91cc\u4e92\u52a8\u5a31\u4e50\u4e8b\u4e1a\u7fa4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,108,90)"
                        }
                    }
                },
                {
                    "name": "\u6ef4\u6ef4\u4f18\u70b9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,24,140)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u777f\u533b\u7597",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,3,108)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u7ec7\u7b97\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,83,75)"
                        }
                    }
                },
                {
                    "name": "\u7c73\u7edc\u661f\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,45,13)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u8054\u82f1\u8bed",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,154,54)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u89c8\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,81,151)"
                        }
                    }
                },
                {
                    "name": "\u7545\u6377\u901a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,121,49)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u6773\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,79,129)"
                        }
                    }
                },
                {
                    "name": "\u6cf0\u5eb7\u5728\u7ebf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,23,111)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u4e1c\u5e7f\u4fe1\u901a\u4fe1\u670d\u52a1\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,58,10)"
                        }
                    }
                },
                {
                    "name": "\u76ca\u76df\u64cd\u76d8\u624b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,128,46)"
                        }
                    }
                },
                {
                    "name": "\u767e\u70bc\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,70,73)"
                        }
                    }
                },
                {
                    "name": "\u6cf0\u5eb7\u4eba\u5bff",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,127,80)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5eb7\u5a01\u89c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,66,69)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u5173\u6751\u6613\u521b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,40,54)"
                        }
                    }
                },
                {
                    "name": "\u6765\u56de\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,44,42)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u8f6f\uff08\u4e2d\u56fd\uff09\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,12,147)"
                        }
                    }
                },
                {
                    "name": "\u6444\u661f\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,117,151)"
                        }
                    }
                },
                {
                    "name": "\u5f53\u5f53\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,115,42)"
                        }
                    }
                },
                {
                    "name": "iSpeak",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,17,79)"
                        }
                    }
                },
                {
                    "name": "\u5370\u8c61\u7b14\u8bb0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,49,29)"
                        }
                    }
                },
                {
                    "name": "\u524d\u6d77\u4e91\u4e1c\u5bb6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,143,64)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u516b\u7ef4\u7814\u4fee\u5b66\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,105,115)"
                        }
                    }
                },
                {
                    "name": "\u6930\u5b50\u4f20\u5a92",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,4,153)"
                        }
                    }
                },
                {
                    "name": "\u70ed\u4e91\u6570\u636e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,105,156)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,159,65)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u6d4e\u533b\u7597",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,142,59)"
                        }
                    }
                },
                {
                    "name": "\u8054\u6613\u878dlinklogis",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,143,127)"
                        }
                    }
                },
                {
                    "name": "\u9e70\u4e4b\u773c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,18,130)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u79d1\u4e16\u901a\u4ea8\u5947",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,140,51)"
                        }
                    }
                },
                {
                    "name": "\u5b8f\u7131\u7f51\u7edc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,137,120)"
                        }
                    }
                },
                {
                    "name": "\u73af\u7403\u7f51\u6821",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,120,89)"
                        }
                    }
                },
                {
                    "name": "\u5343\u91cc\u773c\u7ba1\u7406\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,21,71)"
                        }
                    }
                },
                {
                    "name": "\u5341\u624d\u730e\u5934",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,83,23)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u5dde\u7075\u611f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,43,100)"
                        }
                    }
                },
                {
                    "name": "\u6cf0\u5c14\u80a1\u4efd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,96,120)"
                        }
                    }
                },
                {
                    "name": "Trusfort\u82af\u76fe\u65f6\u4ee3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,143,4)"
                        }
                    }
                },
                {
                    "name": "\u9876\u70b9\u8f6f\u4ef6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,157,160)"
                        }
                    }
                },
                {
                    "name": "\u9014\u864e\u517b\u8f66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,127,127)"
                        }
                    }
                },
                {
                    "name": "\u61d2\u4eba\u7545\u542c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,139,31)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u83dc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,74,82)"
                        }
                    }
                },
                {
                    "name": "\u6bcf\u65e5\u4f18\u9c9c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,19,124)"
                        }
                    }
                },
                {
                    "name": "\u667a\u8f85\u7279\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,148,122)"
                        }
                    }
                },
                {
                    "name": "\u8fde\u4fe1\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,135,157)"
                        }
                    }
                },
                {
                    "name": "\u745e\u5a01\u76db",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,2,55)"
                        }
                    }
                },
                {
                    "name": "\u770b\u623f\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,109,20)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u534e\u7814\u7a76\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,7,99)"
                        }
                    }
                },
                {
                    "name": "\u6a59\u5b50\u6570\u5b57\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,137,23)"
                        }
                    }
                },
                {
                    "name": "\u777f\u8c61\u4e91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,24,12)"
                        }
                    }
                },
                {
                    "name": "\u8d1d\u601d\u79d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,33,112)"
                        }
                    }
                },
                {
                    "name": "\u8c6a\u732a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,153,139)"
                        }
                    }
                },
                {
                    "name": "\u8f6f\u725b\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,74,45)"
                        }
                    }
                },
                {
                    "name": "\u4e3a\u534e\u7f51\u7edc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,19,118)"
                        }
                    }
                },
                {
                    "name": "\u8054\u8fd0\u77e5\u6167\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,13,45)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u79d1\u667a\u52a0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,129,29)"
                        }
                    }
                },
                {
                    "name": "FREE BRIO",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,106,72)"
                        }
                    }
                },
                {
                    "name": "deepcam",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,57,94)"
                        }
                    }
                },
                {
                    "name": "\u8bfa\u5a01\u534e\u4ed5\u7ba1\u7406\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,80,148)"
                        }
                    }
                },
                {
                    "name": "\u751f\u547d\u5947\u70b9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,109,135)"
                        }
                    }
                },
                {
                    "name": "\u5357\u5a01\u8f6f\u4ef6\u80a1\u4efd\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,89,146)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u6717\u9053\u667a\u901a\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,9,93)"
                        }
                    }
                },
                {
                    "name": "\u5bd3\u8a00\u901a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,157,121)"
                        }
                    }
                },
                {
                    "name": "\u6210\u90fd\u8086\u96f6\u8086",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,157,47)"
                        }
                    }
                },
                {
                    "name": "\u6781\u777f\u533b\u7597",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,97,32)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u4e1a\u989c\u7a76\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,32,92)"
                        }
                    }
                },
                {
                    "name": "\u76c8\u4f73\u4fe1\u8054",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,94,56)"
                        }
                    }
                },
                {
                    "name": "\u8682\u8681\u805a\u5b9d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,103,136)"
                        }
                    }
                },
                {
                    "name": "\u5fb7\u805a\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,83,160)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77\u91d1\u5927\u5e08\u7f51\u7edc\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,110,53)"
                        }
                    }
                },
                {
                    "name": "Xeno Dynamics",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,19,81)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u5f84\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,76,97)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u79d1\u777f\u89c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,76,78)"
                        }
                    }
                },
                {
                    "name": "\u55b5\u661f\u63a2\u7d22",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,43,160)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u79d8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,109,128)"
                        }
                    }
                },
                {
                    "name": "Camera360",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,16,142)"
                        }
                    }
                },
                {
                    "name": "\u6155\u8bfe\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,14,130)"
                        }
                    }
                },
                {
                    "name": "Nox\u591c\u795e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,9,2)"
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
                "\u7f8e\u56e2",
                "\u5b57\u8282\u8df3\u52a8",
                "\u5317\u4eac\u5982\u79c4",
                "\u5e73\u5b89\u79d1\u6280",
                "\u597d\u897f\u67da\u6559\u80b2",
                "\u9177\u72d7\u97f3\u4e50",
                "\u9177\u5bb6\u4e50",
                "\u964c\u964c",
                "\u6df1\u5ea6\u8d4b\u667a",
                "Insta360\u5f71\u77f3"
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
        chart_f1a30280e3db4d74a628c6af3c60001f.setOption(option_f1a30280e3db4d74a628c6af3c60001f);
    </script>
                <div id="513ef5ede4114c158d756f6a06bb7ac0" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_513ef5ede4114c158d756f6a06bb7ac0 = echarts.init(
            document.getElementById('513ef5ede4114c158d756f6a06bb7ac0'), 'white', {renderer: 'canvas'});
        var option_513ef5ede4114c158d756f6a06bb7ac0 = {
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
                685,
                335,
                300,
                181,
                85,
                63,
                28,
                15,
                13,
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
                    "value": 685,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,127,54)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77",
                    "value": 335,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,139,98)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733",
                    "value": 300,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,135,93)"
                        }
                    }
                },
                {
                    "name": "\u676d\u5dde",
                    "value": 181,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,60,101)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u5dde",
                    "value": 85,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,129,122)"
                        }
                    }
                },
                {
                    "name": "\u6210\u90fd",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,70,73)"
                        }
                    }
                },
                {
                    "name": "\u6b66\u6c49",
                    "value": 28,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,101,74)"
                        }
                    }
                },
                {
                    "name": "\u5357\u4eac",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,25,98)"
                        }
                    }
                },
                {
                    "name": "\u82cf\u5dde",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,60,153)"
                        }
                    }
                },
                {
                    "name": "\u4f5b\u5c71",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,3,14)"
                        }
                    }
                },
                {
                    "name": "\u91cd\u5e86",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,83,1)"
                        }
                    }
                },
                {
                    "name": "\u53a6\u95e8",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,142,97)"
                        }
                    }
                },
                {
                    "name": "\u73e0\u6d77",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,58,56)"
                        }
                    }
                },
                {
                    "name": "\u5408\u80a5",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,67,14)"
                        }
                    }
                },
                {
                    "name": "\u897f\u5b89",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,98,101)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u9521",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,89,128)"
                        }
                    }
                },
                {
                    "name": "\u5b81\u6ce2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,66,102)"
                        }
                    }
                },
                {
                    "name": "\u90d1\u5dde",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,9,4)"
                        }
                    }
                },
                {
                    "name": "\u60e0\u5dde",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,143,150)"
                        }
                    }
                },
                {
                    "name": "\u957f\u6c99",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,50,121)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u839e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,53,113)"
                        }
                    }
                },
                {
                    "name": "\u9752\u5c9b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,100,41)"
                        }
                    }
                },
                {
                    "name": "\u6d4e\u5357",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,14,145)"
                        }
                    }
                },
                {
                    "name": "\u592a\u539f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,141,86)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5dde",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,55,79)"
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
                "\u5317\u4eac",
                "\u4e0a\u6d77",
                "\u6df1\u5733",
                "\u676d\u5dde",
                "\u5e7f\u5dde",
                "\u6210\u90fd",
                "\u6b66\u6c49",
                "\u5357\u4eac",
                "\u82cf\u5dde",
                "\u4f5b\u5c71"
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
        chart_513ef5ede4114c158d756f6a06bb7ac0.setOption(option_513ef5ede4114c158d756f6a06bb7ac0);
    </script>
                <div id="ba68464ba85b474b89edd609ee10f2c1" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_ba68464ba85b474b89edd609ee10f2c1 = echarts.init(
            document.getElementById('ba68464ba85b474b89edd609ee10f2c1'), 'white', {renderer: 'canvas'});
        var option_ba68464ba85b474b89edd609ee10f2c1 = {
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
                    "value": 685,
                    "name": "\u5317\u4eac"
                },
                {
                    "value": 335,
                    "name": "\u4e0a\u6d77"
                },
                {
                    "value": 300,
                    "name": "\u6df1\u5733"
                },
                {
                    "value": 181,
                    "name": "\u676d\u5dde"
                },
                {
                    "value": 85,
                    "name": "\u5e7f\u5dde"
                },
                {
                    "value": 63,
                    "name": "\u6210\u90fd"
                },
                {
                    "value": 28,
                    "name": "\u6b66\u6c49"
                },
                {
                    "value": 15,
                    "name": "\u5357\u4eac"
                },
                {
                    "value": 13,
                    "name": "\u82cf\u5dde"
                },
                {
                    "value": 10,
                    "name": "\u4f5b\u5c71"
                },
                {
                    "value": 7,
                    "name": "\u91cd\u5e86"
                },
                {
                    "value": 6,
                    "name": "\u53a6\u95e8"
                },
                {
                    "value": 5,
                    "name": "\u73e0\u6d77"
                },
                {
                    "value": 5,
                    "name": "\u5408\u80a5"
                },
                {
                    "value": 5,
                    "name": "\u897f\u5b89"
                },
                {
                    "value": 4,
                    "name": "\u65e0\u9521"
                },
                {
                    "value": 2,
                    "name": "\u5b81\u6ce2"
                },
                {
                    "value": 2,
                    "name": "\u90d1\u5dde"
                },
                {
                    "value": 2,
                    "name": "\u60e0\u5dde"
                },
                {
                    "value": 2,
                    "name": "\u957f\u6c99"
                },
                {
                    "value": 1,
                    "name": "\u4e1c\u839e"
                },
                {
                    "value": 1,
                    "name": "\u9752\u5c9b"
                },
                {
                    "value": 1,
                    "name": "\u6d4e\u5357"
                },
                {
                    "value": 1,
                    "name": "\u592a\u539f"
                },
                {
                    "value": 1,
                    "name": "\u798f\u5dde"
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
        chart_ba68464ba85b474b89edd609ee10f2c1.setOption(option_ba68464ba85b474b89edd609ee10f2c1);
    </script>
                <div id="060468ceb33f4b6b844f583058ea1b01" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_060468ceb33f4b6b844f583058ea1b01 = echarts.init(
            document.getElementById('060468ceb33f4b6b844f583058ea1b01'), 'white', {renderer: 'canvas'});
            
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
    
        var option_060468ceb33f4b6b844f583058ea1b01 = {
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
                        685
                    ]
                },
                {
                    "name": "\u4e0a\u6d77",
                    "value": [
                        121.473701,
                        31.230416,
                        335
                    ]
                },
                {
                    "name": "\u6df1\u5733",
                    "value": [
                        114.07,
                        22.62,
                        300
                    ]
                },
                {
                    "name": "\u676d\u5dde",
                    "value": [
                        120.19,
                        30.26,
                        181
                    ]
                },
                {
                    "name": "\u5e7f\u5dde",
                    "value": [
                        113.23,
                        23.16,
                        85
                    ]
                },
                {
                    "name": "\u6210\u90fd",
                    "value": [
                        104.06,
                        30.67,
                        63
                    ]
                },
                {
                    "name": "\u6b66\u6c49",
                    "value": [
                        114.31,
                        30.52,
                        28
                    ]
                },
                {
                    "name": "\u5357\u4eac",
                    "value": [
                        118.78,
                        32.04,
                        15
                    ]
                },
                {
                    "name": "\u82cf\u5dde",
                    "value": [
                        120.62,
                        31.32,
                        13
                    ]
                },
                {
                    "name": "\u4f5b\u5c71",
                    "value": [
                        113.11,
                        23.05,
                        10
                    ]
                },
                {
                    "name": "\u91cd\u5e86",
                    "value": [
                        106.551556,
                        29.563009,
                        7
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
                    "name": "\u73e0\u6d77",
                    "value": [
                        113.52,
                        22.3,
                        5
                    ]
                },
                {
                    "name": "\u5408\u80a5",
                    "value": [
                        117.27,
                        31.86,
                        5
                    ]
                },
                {
                    "name": "\u897f\u5b89",
                    "value": [
                        108.95,
                        34.27,
                        5
                    ]
                },
                {
                    "name": "\u65e0\u9521",
                    "value": [
                        120.29,
                        31.59,
                        4
                    ]
                },
                {
                    "name": "\u5b81\u6ce2",
                    "value": [
                        121.56,
                        29.86,
                        2
                    ]
                },
                {
                    "name": "\u90d1\u5dde",
                    "value": [
                        113.65,
                        34.76,
                        2
                    ]
                },
                {
                    "name": "\u60e0\u5dde",
                    "value": [
                        114.4,
                        23.09,
                        2
                    ]
                },
                {
                    "name": "\u957f\u6c99",
                    "value": [
                        113,
                        28.21,
                        2
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
                    "name": "\u9752\u5c9b",
                    "value": [
                        120.33,
                        36.07,
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
                    "name": "\u592a\u539f",
                    "value": [
                        112.53,
                        37.87,
                        1
                    ]
                },
                {
                    "name": "\u798f\u5dde",
                    "value": [
                        119.3,
                        26.08,
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
        chart_060468ceb33f4b6b844f583058ea1b01.setOption(option_060468ceb33f4b6b844f583058ea1b01);
    </script>
                <div id="8b94b28c8104489e912febe0e4b518ae" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_8b94b28c8104489e912febe0e4b518ae = echarts.init(
            document.getElementById('8b94b28c8104489e912febe0e4b518ae'), 'white', {renderer: 'canvas'});
        var option_8b94b28c8104489e912febe0e4b518ae = {
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
                178,
                171,
                136,
                48,
                46,
                43,
                38,
                35,
                35,
                32
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
                    "value": 178,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,20,90)"
                        }
                    }
                },
                {
                    "name": "\u671d\u9633\u533a",
                    "value": 171,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,2,59)"
                        }
                    }
                },
                {
                    "name": "\u5357\u5c71\u533a",
                    "value": 136,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,8,81)"
                        }
                    }
                },
                {
                    "name": "\u6d66\u4e1c\u65b0\u2026",
                    "value": 48,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,109,74)"
                        }
                    }
                },
                {
                    "name": "\u671b\u4eac",
                    "value": 46,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,138,46)"
                        }
                    }
                },
                {
                    "name": "\u4f59\u676d\u533a",
                    "value": 43,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,5,31)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u6280\u56ed",
                    "value": 38,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,151,110)"
                        }
                    }
                },
                {
                    "name": "\u95f5\u884c\u533a",
                    "value": 35,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,7,89)"
                        }
                    }
                },
                {
                    "name": "\u897f\u5317\u65fa",
                    "value": 35,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,69,124)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u5173\u6751",
                    "value": 32,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,61,142)"
                        }
                    }
                },
                {
                    "name": "\u5f90\u6c47\u533a",
                    "value": 32,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,88,55)"
                        }
                    }
                },
                {
                    "name": "\u5f20\u6c5f",
                    "value": 31,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,159,143)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9053\u53e3",
                    "value": 30,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,129,134)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u65b0\u533a",
                    "value": 29,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,119,29)"
                        }
                    }
                },
                {
                    "name": "\u5b9d\u5b89\u533a",
                    "value": 27,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,148,154)"
                        }
                    }
                },
                {
                    "name": "\u798f\u7530\u533a",
                    "value": 27,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,87,130)"
                        }
                    }
                },
                {
                    "name": "\u6768\u6d66\u533a",
                    "value": 27,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,37,143)"
                        }
                    }
                },
                {
                    "name": "\u897f\u6eaa",
                    "value": 23,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,115,86)"
                        }
                    }
                },
                {
                    "name": "\u897f\u6e56\u533a",
                    "value": 21,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,148,97)"
                        }
                    }
                },
                {
                    "name": "\u8679\u53e3\u533a",
                    "value": 21,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,32,104)"
                        }
                    }
                },
                {
                    "name": "\u6b66\u4faf\u533a",
                    "value": 20,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,112,120)"
                        }
                    }
                },
                {
                    "name": "\u8d8a\u79c0\u533a",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,73,155)"
                        }
                    }
                },
                {
                    "name": "\u6ee8\u6c5f\u533a",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,82,50)"
                        }
                    }
                },
                {
                    "name": "\u957f\u5b81\u533a",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,155,50)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u6625\u8def",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,68,115)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5174\u533a",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,64,35)"
                        }
                    }
                },
                {
                    "name": "\u5927\u51b2",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,15,59)"
                        }
                    }
                },
                {
                    "name": "\u5929\u6cb3\u533a",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,127,115)"
                        }
                    }
                },
                {
                    "name": "\u897f\u4e8c\u65d7",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,155,131)"
                        }
                    }
                },
                {
                    "name": "\u62f1\u5885\u533a",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,77,110)"
                        }
                    }
                },
                {
                    "name": "\u8679\u6885\u8def",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,129,39)"
                        }
                    }
                },
                {
                    "name": "\u9752\u6d66\u533a",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,17,84)"
                        }
                    }
                },
                {
                    "name": "\u987a\u5fb7\u533a",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,128,107)"
                        }
                    }
                },
                {
                    "name": "\u9759\u5b89\u533a",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,87,49)"
                        }
                    }
                },
                {
                    "name": "\u897f\u5174",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,18,0)"
                        }
                    }
                },
                {
                    "name": "\u897f\u4e09\u65d7",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,44,39)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u57ce\u533a",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,151,1)"
                        }
                    }
                },
                {
                    "name": "\u677e\u6c5f\u533a",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,17,12)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u6e56\u65b0\u2026",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,148,38)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u56ed\u2026",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,34,16)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5730",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,99,7)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,76,51)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u6e7e",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,152,65)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u73e0\u533a",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,67,118)"
                        }
                    }
                },
                {
                    "name": "\u9f99\u534e",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,2,156)"
                        }
                    }
                },
                {
                    "name": "\u9f99\u534e\u65b0\u2026",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,63,134)"
                        }
                    }
                },
                {
                    "name": "\u77f3\u666f\u5c71\u2026",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,85,27)"
                        }
                    }
                },
                {
                    "name": "\u957f\u6cb3",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,34,34)"
                        }
                    }
                },
                {
                    "name": "\u5357\u6c99\u533a",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,9,118)"
                        }
                    }
                },
                {
                    "name": "\u4ed3\u524d",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,101,115)"
                        }
                    }
                },
                {
                    "name": "\u666e\u9640\u533a",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,11,149)"
                        }
                    }
                },
                {
                    "name": "\u6d2a\u5c71\u533a",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,112,33)"
                        }
                    }
                },
                {
                    "name": "\u6765\u5e7f\u8425",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,74,60)"
                        }
                    }
                },
                {
                    "name": "\u9ec4\u57d4\u533a",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,144,20)"
                        }
                    }
                },
                {
                    "name": "\u5173\u5c71",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,78,127)"
                        }
                    }
                },
                {
                    "name": "\u756a\u79ba\u533a",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,141,97)"
                        }
                    }
                },
                {
                    "name": "\u5f90\u5bb6\u6c47",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,33,17)"
                        }
                    }
                },
                {
                    "name": "\u5929\u5c71\u8def",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,62,40)"
                        }
                    }
                },
                {
                    "name": "\u9ec4\u6d66\u533a",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,33,57)"
                        }
                    }
                },
                {
                    "name": "\u5927\u671b\u8def",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,117,79)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,86,100)"
                        }
                    }
                },
                {
                    "name": "\u4e9a\u8fd0\u6751",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,5,59)"
                        }
                    }
                },
                {
                    "name": "\u9999\u6d32\u533a",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,49,85)"
                        }
                    }
                },
                {
                    "name": "\u6587\u4e09\u8def",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,89,115)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u9662\u8def",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,27,31)"
                        }
                    }
                },
                {
                    "name": "\u601d\u660e\u533a",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,70,4)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5c71\u5b50",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,10,93)"
                        }
                    }
                },
                {
                    "name": "\u897f\u6e56",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,17,148)"
                        }
                    }
                },
                {
                    "name": "\u5357\u6cb9",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,49,30)"
                        }
                    }
                },
                {
                    "name": "\u9152\u4ed9\u6865",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,153,53)"
                        }
                    }
                },
                {
                    "name": "\u524d\u6d77",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,80,113)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u5927\u2026",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,120,123)"
                        }
                    }
                },
                {
                    "name": "\u68e0\u4e0b",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,50,57)"
                        }
                    }
                },
                {
                    "name": "\u4ea6\u5e84",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,56,91)"
                        }
                    }
                },
                {
                    "name": "\u96e8\u82b1\u53f0\u2026",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,0,69)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u5703",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,21,154)"
                        }
                    }
                },
                {
                    "name": "\u897f\u4e3d",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,53,137)"
                        }
                    }
                },
                {
                    "name": "\u6e1d\u4e2d\u533a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,71,124)"
                        }
                    }
                },
                {
                    "name": "\u53e4\u58a9\u8def",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,65,6)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5b89",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,92,5)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u89d2\u573a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,2,80)"
                        }
                    }
                },
                {
                    "name": "\u96c1\u5854\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,16,159)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u58a9",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,81,1)"
                        }
                    }
                },
                {
                    "name": "\u7f57\u6e56\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,85,75)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u5173",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,67,13)"
                        }
                    }
                },
                {
                    "name": "\u671b\u6c5f\u8def",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,56,53)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u5c71",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,138,67)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u6d41\u53bf",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,115,2)"
                        }
                    }
                },
                {
                    "name": "\u671d\u9633\u95e8",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,25,9)"
                        }
                    }
                },
                {
                    "name": "\u76f8\u57ce\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,102,140)"
                        }
                    }
                },
                {
                    "name": "\u5317\u5916\u6ee9",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,103,44)"
                        }
                    }
                },
                {
                    "name": "\u9526\u6c5f\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,17,103)"
                        }
                    }
                },
                {
                    "name": "\u4e0b\u57ce\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,140,24)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u725b\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,84,64)"
                        }
                    }
                },
                {
                    "name": "\u660c\u5e73\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,110,111)"
                        }
                    }
                },
                {
                    "name": "\u5efa\u56fd\u95e8",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,97,99)"
                        }
                    }
                },
                {
                    "name": "\u56db\u60e0",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,17,144)"
                        }
                    }
                },
                {
                    "name": "\u8427\u5c71\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,42,107)"
                        }
                    }
                },
                {
                    "name": "\u56de\u9f99\u89c2",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,62,79)"
                        }
                    }
                },
                {
                    "name": "\u6ee8\u6e56\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,83,107)"
                        }
                    }
                },
                {
                    "name": "\u676d\u5dde",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,82,149)"
                        }
                    }
                },
                {
                    "name": "\u5929\u6cb3\u57ce",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,67,156)"
                        }
                    }
                },
                {
                    "name": "\u56db\u5e73\u8def",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,56,56)"
                        }
                    }
                },
                {
                    "name": "\u5317\u65b0\u6cfe",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,133,22)"
                        }
                    }
                },
                {
                    "name": "\u5f90\u6cfe",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,96,134)"
                        }
                    }
                },
                {
                    "name": "\u540e\u6d77",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,108,35)"
                        }
                    }
                },
                {
                    "name": "\u547c\u5bb6\u697c",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,4,55)"
                        }
                    }
                },
                {
                    "name": "\u897f\u4e61",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,61,137)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u798f\u5e84",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,6,14)"
                        }
                    }
                },
                {
                    "name": "\u548c\u5e73\u91cc",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,124,136)"
                        }
                    }
                },
                {
                    "name": "\u5317\u82d1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,28,42)"
                        }
                    }
                },
                {
                    "name": "\u5ef6\u5409",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,84,45)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u5c71\u516c\u2026",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,147,152)"
                        }
                    }
                },
                {
                    "name": "\u6c5f\u5b81\u8def",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,53,47)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u6e2f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,129,59)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u53f0\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,99,56)"
                        }
                    }
                },
                {
                    "name": "\u897f\u82d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,141,50)"
                        }
                    }
                },
                {
                    "name": "\u5f00\u53d1\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,22,95)"
                        }
                    }
                },
                {
                    "name": "\u5149\u660e\u65b0\u2026",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,122,32)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u5143\u6865",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,156,149)"
                        }
                    }
                },
                {
                    "name": "\u6f15\u6cb3\u6cfe",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,51,25)"
                        }
                    }
                },
                {
                    "name": "\u6253\u6d66\u6865",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,118,13)"
                        }
                    }
                },
                {
                    "name": "\u6797\u548c",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,112,44)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u65b0\u6280\u2026",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,100,120)"
                        }
                    }
                },
                {
                    "name": "\u9f99\u5c97\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,44,49)"
                        }
                    }
                },
                {
                    "name": "\u9f99\u6cc9\u9a7f\u2026",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,138,8)"
                        }
                    }
                },
                {
                    "name": "\u5609\u5b9a\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,75,84)"
                        }
                    }
                },
                {
                    "name": "\u673a\u6295\u6865",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,14,143)"
                        }
                    }
                },
                {
                    "name": "\u5efa\u5916\u5927\u2026",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,100,146)"
                        }
                    }
                },
                {
                    "name": "\u6d66\u6cbf",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,146,70)"
                        }
                    }
                },
                {
                    "name": "\u57ce\u968d\u5e99",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,143,3)"
                        }
                    }
                },
                {
                    "name": "\u897f\u76f4\u95e8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,102,8)"
                        }
                    }
                },
                {
                    "name": "\u5742\u7530",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,81,26)"
                        }
                    }
                },
                {
                    "name": "\u65e0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,68,121)"
                        }
                    }
                },
                {
                    "name": "\u576a\u5c71\u65b0\u2026",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,123,17)"
                        }
                    }
                },
                {
                    "name": "\u534e\u6f15",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,41,124)"
                        }
                    }
                },
                {
                    "name": "\u6c5f\u5e72\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,116,42)"
                        }
                    }
                },
                {
                    "name": "\u5efa\u90ba\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,99,11)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,22,108)"
                        }
                    }
                },
                {
                    "name": "\u5929\u76ee\u5c71\u2026",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,65,47)"
                        }
                    }
                },
                {
                    "name": "\u8398\u5e84",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,73,17)"
                        }
                    }
                },
                {
                    "name": "\u4e07\u6cc9\u6cb3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,135,113)"
                        }
                    }
                },
                {
                    "name": "\u60e0\u9633\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,31,51)"
                        }
                    }
                },
                {
                    "name": "\u71d5\u838e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,16,139)"
                        }
                    }
                },
                {
                    "name": "\u5de6\u5bb6\u5e84",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,82,75)"
                        }
                    }
                },
                {
                    "name": "\u6c5f\u5b81\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,71,52)"
                        }
                    }
                },
                {
                    "name": "\u5965\u4f53",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,140,19)"
                        }
                    }
                },
                {
                    "name": "\u5149\u8c37",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,112,143)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u4ead",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,100,17)"
                        }
                    }
                },
                {
                    "name": "\u9646\u5bb6\u5634",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,104,145)"
                        }
                    }
                },
                {
                    "name": "\u911e\u5dde\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,79,119)"
                        }
                    }
                },
                {
                    "name": "\u6e2d\u5858",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,110,100)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u6e2f\u4e1c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,40,113)"
                        }
                    }
                },
                {
                    "name": "\u8700\u6c49\u8def",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,9,35)"
                        }
                    }
                },
                {
                    "name": "\u901a\u5dde\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,121,4)"
                        }
                    }
                },
                {
                    "name": "\u6c5f\u590f\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,15,92)"
                        }
                    }
                },
                {
                    "name": "\u767d\u77f3\u6d32",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,2,12)"
                        }
                    }
                },
                {
                    "name": "\u6b66\u6c49\u7ecf\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,123,16)"
                        }
                    }
                },
                {
                    "name": "\u576a\u5c71\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,150,18)"
                        }
                    }
                },
                {
                    "name": "\u6a2a\u5c97",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,10,157)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u548c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,111,59)"
                        }
                    }
                },
                {
                    "name": "\u6f15\u5b9d\u8def",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,79,38)"
                        }
                    }
                },
                {
                    "name": "\u6d41\u82b3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,95,131)"
                        }
                    }
                },
                {
                    "name": "\u76d0\u7530\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,16,85)"
                        }
                    }
                },
                {
                    "name": "\u592a\u9633\u5bab",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,98,37)"
                        }
                    }
                },
                {
                    "name": "\u8f66\u516c\u5e99",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,11,24)"
                        }
                    }
                },
                {
                    "name": "\u592a\u548c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,71,78)"
                        }
                    }
                },
                {
                    "name": "\u7ea2\u5e99",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,63,116)"
                        }
                    }
                },
                {
                    "name": "\u9547\u5b81\u8def",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,155,25)"
                        }
                    }
                },
                {
                    "name": "\u897f\u57ce\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,91,133)"
                        }
                    }
                },
                {
                    "name": "\u6885\u56ed",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,62,89)"
                        }
                    }
                },
                {
                    "name": "\u5510\u9547",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,125,112)"
                        }
                    }
                },
                {
                    "name": "\u841d\u5c97\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,53,27)"
                        }
                    }
                },
                {
                    "name": "\u767d\u6768",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,19,97)"
                        }
                    }
                },
                {
                    "name": "\u6c5f\u5cb8\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,142,133)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u57ce\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,102,3)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u56db",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,3,18)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u8857",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,106,74)"
                        }
                    }
                },
                {
                    "name": "\u5357\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,116,18)"
                        }
                    }
                },
                {
                    "name": "\u6e1d\u5317\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,152,80)"
                        }
                    }
                },
                {
                    "name": "\u6d66\u53e3\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,120,12)"
                        }
                    }
                },
                {
                    "name": "\u5386\u57ce\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,86,53)"
                        }
                    }
                },
                {
                    "name": "\u5cad\u5357",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,12,93)"
                        }
                    }
                },
                {
                    "name": "\u957f\u5f81",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,94,138)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u6d41\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,12,39)"
                        }
                    }
                },
                {
                    "name": "\u6816\u971e\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,139,118)"
                        }
                    }
                },
                {
                    "name": "\u8f66\u7ad9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,157,21)"
                        }
                    }
                },
                {
                    "name": "\u660c\u5c97",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,50,89)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u6d32",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,105,104)"
                        }
                    }
                },
                {
                    "name": "\u53e4\u8361",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,145,35)"
                        }
                    }
                },
                {
                    "name": "\u9a6c\u8fde\u6d3c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,139,26)"
                        }
                    }
                },
                {
                    "name": "\u7436\u6d32",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,137,87)"
                        }
                    }
                },
                {
                    "name": "\u5434\u6cfe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,67,25)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u6ca7\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,85,130)"
                        }
                    }
                },
                {
                    "name": "\u96e8\u82b1\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,29,20)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5434\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,17,17)"
                        }
                    }
                },
                {
                    "name": "\u6d0b\u6cfe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,151,82)"
                        }
                    }
                },
                {
                    "name": "\u5458\u6751",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,64,38)"
                        }
                    }
                },
                {
                    "name": "\u6c5f\u5357",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,14,33)"
                        }
                    }
                },
                {
                    "name": "\u6f58\u5bb6\u56ed",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,145,13)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u5fb7\u95e8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,113,34)"
                        }
                    }
                },
                {
                    "name": "\u534e\u4fa8\u57ce",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,7,105)"
                        }
                    }
                },
                {
                    "name": "\u897f\u5c71",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,45,82)"
                        }
                    }
                },
                {
                    "name": "\u5343\u5cf0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,3,120)"
                        }
                    }
                },
                {
                    "name": "\u987a\u4e49\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,116,130)"
                        }
                    }
                },
                {
                    "name": "\u6f4d\u574a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,33,92)"
                        }
                    }
                },
                {
                    "name": "\u8857\u9053\u53e3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,11,43)"
                        }
                    }
                },
                {
                    "name": "\u822a\u7a7a\u6e2f\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,25,80)"
                        }
                    }
                },
                {
                    "name": "\u8096\u5bb6\u6cb3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,119,45)"
                        }
                    }
                },
                {
                    "name": "\u6587\u4e00\u8def",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,43,82)"
                        }
                    }
                },
                {
                    "name": "\u7acb\u6c34\u6865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,50,144)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u7ed3\u6e56",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,142,122)"
                        }
                    }
                },
                {
                    "name": "\u51bc\u6751",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,58,154)"
                        }
                    }
                },
                {
                    "name": "\u5e02\u5357\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,131,38)"
                        }
                    }
                },
                {
                    "name": "\u56db\u5b63\u9752",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,27,129)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u5927\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,82,82)"
                        }
                    }
                },
                {
                    "name": "\u4e5d\u9f99\u5761\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,102,78)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u884c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,151,75)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u6986\u6811",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,25,140)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u839e\u5e02",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,100,29)"
                        }
                    }
                },
                {
                    "name": "\u90d1\u4e1c\u65b0\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,92,88)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u6167\u5bfa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,84,91)"
                        }
                    }
                },
                {
                    "name": "\u5e38\u8425",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,12,112)"
                        }
                    }
                },
                {
                    "name": "\u5357\u5c71\u533b\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,80,97)"
                        }
                    }
                },
                {
                    "name": "\u5c55\u89c8\u8def",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,51,158)"
                        }
                    }
                },
                {
                    "name": "\u73e0\u6c5f\u65b0\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,158,89)"
                        }
                    }
                },
                {
                    "name": "\u5357\u4eac",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,38,144)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7891\u5e97",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,21,34)"
                        }
                    }
                },
                {
                    "name": "\u5cb3\u9e93\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,34,44)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u6280\u56ed\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,96,12)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u6c5f\u6e7e\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,151,152)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u76f4\u95e8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,151,33)"
                        }
                    }
                },
                {
                    "name": "\u9f13\u697c\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,97,124)"
                        }
                    }
                },
                {
                    "name": "\u4e07\u67f3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,63,42)"
                        }
                    }
                },
                {
                    "name": "\u897f\u5173",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,39,32)"
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
                "\u6d77\u6dc0\u533a",
                "\u671d\u9633\u533a",
                "\u5357\u5c71\u533a",
                "\u6d66\u4e1c\u65b0\u2026",
                "\u671b\u4eac",
                "\u4f59\u676d\u533a",
                "\u79d1\u6280\u56ed",
                "\u95f5\u884c\u533a",
                "\u897f\u5317\u65fa",
                "\u4e2d\u5173\u6751"
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
        chart_8b94b28c8104489e912febe0e4b518ae.setOption(option_8b94b28c8104489e912febe0e4b518ae);
    </script>
                <div id="52beb97995c649be956bd359b66fe9a4" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_52beb97995c649be956bd359b66fe9a4 = echarts.init(
            document.getElementById('52beb97995c649be956bd359b66fe9a4'), 'white', {renderer: 'canvas'});
        var option_52beb97995c649be956bd359b66fe9a4 = {
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
                    "value": 178,
                    "name": "\u6d77\u6dc0\u533a"
                },
                {
                    "value": 171,
                    "name": "\u671d\u9633\u533a"
                },
                {
                    "value": 136,
                    "name": "\u5357\u5c71\u533a"
                },
                {
                    "value": 48,
                    "name": "\u6d66\u4e1c\u65b0\u2026"
                },
                {
                    "value": 46,
                    "name": "\u671b\u4eac"
                },
                {
                    "value": 43,
                    "name": "\u4f59\u676d\u533a"
                },
                {
                    "value": 38,
                    "name": "\u79d1\u6280\u56ed"
                },
                {
                    "value": 35,
                    "name": "\u95f5\u884c\u533a"
                },
                {
                    "value": 35,
                    "name": "\u897f\u5317\u65fa"
                },
                {
                    "value": 32,
                    "name": "\u4e2d\u5173\u6751"
                },
                {
                    "value": 32,
                    "name": "\u5f90\u6c47\u533a"
                },
                {
                    "value": 31,
                    "name": "\u5f20\u6c5f"
                },
                {
                    "value": 30,
                    "name": "\u4e94\u9053\u53e3"
                },
                {
                    "value": 29,
                    "name": "\u9ad8\u65b0\u533a"
                },
                {
                    "value": 27,
                    "name": "\u5b9d\u5b89\u533a"
                },
                {
                    "value": 27,
                    "name": "\u798f\u7530\u533a"
                },
                {
                    "value": 27,
                    "name": "\u6768\u6d66\u533a"
                },
                {
                    "value": 23,
                    "name": "\u897f\u6eaa"
                },
                {
                    "value": 21,
                    "name": "\u897f\u6e56\u533a"
                },
                {
                    "value": 21,
                    "name": "\u8679\u53e3\u533a"
                },
                {
                    "value": 20,
                    "name": "\u6b66\u4faf\u533a"
                },
                {
                    "value": 17,
                    "name": "\u8d8a\u79c0\u533a"
                },
                {
                    "value": 17,
                    "name": "\u6ee8\u6c5f\u533a"
                },
                {
                    "value": 16,
                    "name": "\u957f\u5b81\u533a"
                },
                {
                    "value": 15,
                    "name": "\u77e5\u6625\u8def"
                },
                {
                    "value": 14,
                    "name": "\u5927\u5174\u533a"
                },
                {
                    "value": 13,
                    "name": "\u5927\u51b2"
                },
                {
                    "value": 13,
                    "name": "\u5929\u6cb3\u533a"
                },
                {
                    "value": 13,
                    "name": "\u897f\u4e8c\u65d7"
                },
                {
                    "value": 13,
                    "name": "\u62f1\u5885\u533a"
                },
                {
                    "value": 11,
                    "name": "\u8679\u6885\u8def"
                },
                {
                    "value": 11,
                    "name": "\u9752\u6d66\u533a"
                },
                {
                    "value": 10,
                    "name": "\u987a\u5fb7\u533a"
                },
                {
                    "value": 10,
                    "name": "\u9759\u5b89\u533a"
                },
                {
                    "value": 10,
                    "name": "\u897f\u5174"
                },
                {
                    "value": 10,
                    "name": "\u897f\u4e09\u65d7"
                },
                {
                    "value": 10,
                    "name": "\u4e1c\u57ce\u533a"
                },
                {
                    "value": 9,
                    "name": "\u677e\u6c5f\u533a"
                },
                {
                    "value": 9,
                    "name": "\u4e1c\u6e56\u65b0\u2026"
                },
                {
                    "value": 9,
                    "name": "\u5de5\u4e1a\u56ed\u2026"
                },
                {
                    "value": 9,
                    "name": "\u4e0a\u5730"
                },
                {
                    "value": 8,
                    "name": "\u5317\u4eac"
                },
                {
                    "value": 8,
                    "name": "\u6df1\u5733\u6e7e"
                },
                {
                    "value": 8,
                    "name": "\u6d77\u73e0\u533a"
                },
                {
                    "value": 8,
                    "name": "\u9f99\u534e"
                },
                {
                    "value": 8,
                    "name": "\u9f99\u534e\u65b0\u2026"
                },
                {
                    "value": 8,
                    "name": "\u77f3\u666f\u5c71\u2026"
                },
                {
                    "value": 8,
                    "name": "\u957f\u6cb3"
                },
                {
                    "value": 7,
                    "name": "\u5357\u6c99\u533a"
                },
                {
                    "value": 7,
                    "name": "\u4ed3\u524d"
                },
                {
                    "value": 7,
                    "name": "\u666e\u9640\u533a"
                },
                {
                    "value": 6,
                    "name": "\u6d2a\u5c71\u533a"
                },
                {
                    "value": 6,
                    "name": "\u6765\u5e7f\u8425"
                },
                {
                    "value": 6,
                    "name": "\u9ec4\u57d4\u533a"
                },
                {
                    "value": 6,
                    "name": "\u5173\u5c71"
                },
                {
                    "value": 6,
                    "name": "\u756a\u79ba\u533a"
                },
                {
                    "value": 6,
                    "name": "\u5f90\u5bb6\u6c47"
                },
                {
                    "value": 6,
                    "name": "\u5929\u5c71\u8def"
                },
                {
                    "value": 6,
                    "name": "\u9ec4\u6d66\u533a"
                },
                {
                    "value": 6,
                    "name": "\u5927\u671b\u8def"
                },
                {
                    "value": 6,
                    "name": "\u4e0a\u6d77"
                },
                {
                    "value": 5,
                    "name": "\u4e9a\u8fd0\u6751"
                },
                {
                    "value": 5,
                    "name": "\u9999\u6d32\u533a"
                },
                {
                    "value": 5,
                    "name": "\u6587\u4e09\u8def"
                },
                {
                    "value": 5,
                    "name": "\u5b66\u9662\u8def"
                },
                {
                    "value": 5,
                    "name": "\u601d\u660e\u533a"
                },
                {
                    "value": 4,
                    "name": "\u5927\u5c71\u5b50"
                },
                {
                    "value": 4,
                    "name": "\u897f\u6e56"
                },
                {
                    "value": 4,
                    "name": "\u5357\u6cb9"
                },
                {
                    "value": 4,
                    "name": "\u9152\u4ed9\u6865"
                },
                {
                    "value": 4,
                    "name": "\u524d\u6d77"
                },
                {
                    "value": 4,
                    "name": "\u5317\u4eac\u5927\u2026"
                },
                {
                    "value": 4,
                    "name": "\u68e0\u4e0b"
                },
                {
                    "value": 4,
                    "name": "\u4ea6\u5e84"
                },
                {
                    "value": 4,
                    "name": "\u96e8\u82b1\u53f0\u2026"
                },
                {
                    "value": 4,
                    "name": "\u4e1c\u5703"
                },
                {
                    "value": 4,
                    "name": "\u897f\u4e3d"
                },
                {
                    "value": 4,
                    "name": "\u6e1d\u4e2d\u533a"
                },
                {
                    "value": 4,
                    "name": "\u53e4\u58a9\u8def"
                },
                {
                    "value": 4,
                    "name": "\u65b0\u5b89"
                },
                {
                    "value": 4,
                    "name": "\u4e94\u89d2\u573a"
                },
                {
                    "value": 3,
                    "name": "\u96c1\u5854\u533a"
                },
                {
                    "value": 3,
                    "name": "\u4e09\u58a9"
                },
                {
                    "value": 3,
                    "name": "\u7f57\u6e56\u533a"
                },
                {
                    "value": 3,
                    "name": "\u5c0f\u5173"
                },
                {
                    "value": 3,
                    "name": "\u671b\u6c5f\u8def"
                },
                {
                    "value": 3,
                    "name": "\u4e94\u5c71"
                },
                {
                    "value": 3,
                    "name": "\u53cc\u6d41\u53bf"
                },
                {
                    "value": 3,
                    "name": "\u671d\u9633\u95e8"
                },
                {
                    "value": 3,
                    "name": "\u76f8\u57ce\u533a"
                },
                {
                    "value": 3,
                    "name": "\u5317\u5916\u6ee9"
                },
                {
                    "value": 3,
                    "name": "\u9526\u6c5f\u533a"
                },
                {
                    "value": 3,
                    "name": "\u4e0b\u57ce\u533a"
                },
                {
                    "value": 3,
                    "name": "\u91d1\u725b\u533a"
                },
                {
                    "value": 3,
                    "name": "\u660c\u5e73\u533a"
                },
                {
                    "value": 3,
                    "name": "\u5efa\u56fd\u95e8"
                },
                {
                    "value": 3,
                    "name": "\u56db\u60e0"
                },
                {
                    "value": 3,
                    "name": "\u8427\u5c71\u533a"
                },
                {
                    "value": 3,
                    "name": "\u56de\u9f99\u89c2"
                },
                {
                    "value": 3,
                    "name": "\u6ee8\u6e56\u533a"
                },
                {
                    "value": 3,
                    "name": "\u676d\u5dde"
                },
                {
                    "value": 3,
                    "name": "\u5929\u6cb3\u57ce"
                },
                {
                    "value": 3,
                    "name": "\u56db\u5e73\u8def"
                },
                {
                    "value": 3,
                    "name": "\u5317\u65b0\u6cfe"
                },
                {
                    "value": 3,
                    "name": "\u5f90\u6cfe"
                },
                {
                    "value": 3,
                    "name": "\u540e\u6d77"
                },
                {
                    "value": 3,
                    "name": "\u547c\u5bb6\u697c"
                },
                {
                    "value": 3,
                    "name": "\u897f\u4e61"
                },
                {
                    "value": 3,
                    "name": "\u5b9a\u798f\u5e84"
                },
                {
                    "value": 3,
                    "name": "\u548c\u5e73\u91cc"
                },
                {
                    "value": 3,
                    "name": "\u5317\u82d1"
                },
                {
                    "value": 2,
                    "name": "\u5ef6\u5409"
                },
                {
                    "value": 2,
                    "name": "\u4e2d\u5c71\u516c\u2026"
                },
                {
                    "value": 2,
                    "name": "\u6c5f\u5b81\u8def"
                },
                {
                    "value": 2,
                    "name": "\u65b0\u6e2f"
                },
                {
                    "value": 2,
                    "name": "\u4e30\u53f0\u533a"
                },
                {
                    "value": 2,
                    "name": "\u897f\u82d1"
                },
                {
                    "value": 2,
                    "name": "\u5f00\u53d1\u533a"
                },
                {
                    "value": 2,
                    "name": "\u5149\u660e\u65b0\u2026"
                },
                {
                    "value": 2,
                    "name": "\u4e09\u5143\u6865"
                },
                {
                    "value": 2,
                    "name": "\u6f15\u6cb3\u6cfe"
                },
                {
                    "value": 2,
                    "name": "\u6253\u6d66\u6865"
                },
                {
                    "value": 2,
                    "name": "\u6797\u548c"
                },
                {
                    "value": 2,
                    "name": "\u9ad8\u65b0\u6280\u2026"
                },
                {
                    "value": 2,
                    "name": "\u9f99\u5c97\u533a"
                },
                {
                    "value": 2,
                    "name": "\u9f99\u6cc9\u9a7f\u2026"
                },
                {
                    "value": 2,
                    "name": "\u5609\u5b9a\u533a"
                },
                {
                    "value": 2,
                    "name": "\u673a\u6295\u6865"
                },
                {
                    "value": 2,
                    "name": "\u5efa\u5916\u5927\u2026"
                },
                {
                    "value": 2,
                    "name": "\u6d66\u6cbf"
                },
                {
                    "value": 2,
                    "name": "\u57ce\u968d\u5e99"
                },
                {
                    "value": 2,
                    "name": "\u897f\u76f4\u95e8"
                },
                {
                    "value": 2,
                    "name": "\u5742\u7530"
                },
                {
                    "value": 2,
                    "name": "\u65e0"
                },
                {
                    "value": 2,
                    "name": "\u576a\u5c71\u65b0\u2026"
                },
                {
                    "value": 2,
                    "name": "\u534e\u6f15"
                },
                {
                    "value": 2,
                    "name": "\u6c5f\u5e72\u533a"
                },
                {
                    "value": 2,
                    "name": "\u5efa\u90ba\u533a"
                },
                {
                    "value": 2,
                    "name": "\u6df1\u5733"
                },
                {
                    "value": 2,
                    "name": "\u5929\u76ee\u5c71\u2026"
                },
                {
                    "value": 2,
                    "name": "\u8398\u5e84"
                },
                {
                    "value": 2,
                    "name": "\u4e07\u6cc9\u6cb3"
                },
                {
                    "value": 2,
                    "name": "\u60e0\u9633\u533a"
                },
                {
                    "value": 2,
                    "name": "\u71d5\u838e"
                },
                {
                    "value": 2,
                    "name": "\u5de6\u5bb6\u5e84"
                },
                {
                    "value": 2,
                    "name": "\u6c5f\u5b81\u533a"
                },
                {
                    "value": 1,
                    "name": "\u5965\u4f53"
                },
                {
                    "value": 1,
                    "name": "\u5149\u8c37"
                },
                {
                    "value": 1,
                    "name": "\u5b89\u4ead"
                },
                {
                    "value": 1,
                    "name": "\u9646\u5bb6\u5634"
                },
                {
                    "value": 1,
                    "name": "\u911e\u5dde\u533a"
                },
                {
                    "value": 1,
                    "name": "\u6e2d\u5858"
                },
                {
                    "value": 1,
                    "name": "\u65b0\u6e2f\u4e1c"
                },
                {
                    "value": 1,
                    "name": "\u8700\u6c49\u8def"
                },
                {
                    "value": 1,
                    "name": "\u901a\u5dde\u533a"
                },
                {
                    "value": 1,
                    "name": "\u6c5f\u590f\u533a"
                },
                {
                    "value": 1,
                    "name": "\u767d\u77f3\u6d32"
                },
                {
                    "value": 1,
                    "name": "\u6b66\u6c49\u7ecf\u2026"
                },
                {
                    "value": 1,
                    "name": "\u576a\u5c71\u533a"
                },
                {
                    "value": 1,
                    "name": "\u6a2a\u5c97"
                },
                {
                    "value": 1,
                    "name": "\u4eba\u548c"
                },
                {
                    "value": 1,
                    "name": "\u6f15\u5b9d\u8def"
                },
                {
                    "value": 1,
                    "name": "\u6d41\u82b3"
                },
                {
                    "value": 1,
                    "name": "\u76d0\u7530\u533a"
                },
                {
                    "value": 1,
                    "name": "\u592a\u9633\u5bab"
                },
                {
                    "value": 1,
                    "name": "\u8f66\u516c\u5e99"
                },
                {
                    "value": 1,
                    "name": "\u592a\u548c"
                },
                {
                    "value": 1,
                    "name": "\u7ea2\u5e99"
                },
                {
                    "value": 1,
                    "name": "\u9547\u5b81\u8def"
                },
                {
                    "value": 1,
                    "name": "\u897f\u57ce\u533a"
                },
                {
                    "value": 1,
                    "name": "\u6885\u56ed"
                },
                {
                    "value": 1,
                    "name": "\u5510\u9547"
                },
                {
                    "value": 1,
                    "name": "\u841d\u5c97\u533a"
                },
                {
                    "value": 1,
                    "name": "\u767d\u6768"
                },
                {
                    "value": 1,
                    "name": "\u6c5f\u5cb8\u533a"
                },
                {
                    "value": 1,
                    "name": "\u4e0a\u57ce\u533a"
                },
                {
                    "value": 1,
                    "name": "\u4e1c\u56db"
                },
                {
                    "value": 1,
                    "name": "\u91d1\u878d\u8857"
                },
                {
                    "value": 1,
                    "name": "\u5357\u5927"
                },
                {
                    "value": 1,
                    "name": "\u6e1d\u5317\u533a"
                },
                {
                    "value": 1,
                    "name": "\u6d66\u53e3\u533a"
                },
                {
                    "value": 1,
                    "name": "\u5386\u57ce\u533a"
                },
                {
                    "value": 1,
                    "name": "\u5cad\u5357"
                },
                {
                    "value": 1,
                    "name": "\u957f\u5f81"
                },
                {
                    "value": 1,
                    "name": "\u53cc\u6d41\u533a"
                },
                {
                    "value": 1,
                    "name": "\u6816\u971e\u533a"
                },
                {
                    "value": 1,
                    "name": "\u8f66\u7ad9"
                },
                {
                    "value": 1,
                    "name": "\u660c\u5c97"
                },
                {
                    "value": 1,
                    "name": "\u65b0\u6d32"
                },
                {
                    "value": 1,
                    "name": "\u53e4\u8361"
                },
                {
                    "value": 1,
                    "name": "\u9a6c\u8fde\u6d3c"
                },
                {
                    "value": 1,
                    "name": "\u7436\u6d32"
                },
                {
                    "value": 1,
                    "name": "\u5434\u6cfe"
                },
                {
                    "value": 1,
                    "name": "\u6d77\u6ca7\u533a"
                },
                {
                    "value": 1,
                    "name": "\u96e8\u82b1\u533a"
                },
                {
                    "value": 1,
                    "name": "\u65b0\u5434\u533a"
                },
                {
                    "value": 1,
                    "name": "\u6d0b\u6cfe"
                },
                {
                    "value": 1,
                    "name": "\u5458\u6751"
                },
                {
                    "value": 1,
                    "name": "\u6c5f\u5357"
                },
                {
                    "value": 1,
                    "name": "\u6f58\u5bb6\u56ed"
                },
                {
                    "value": 1,
                    "name": "\u5b89\u5fb7\u95e8"
                },
                {
                    "value": 1,
                    "name": "\u534e\u4fa8\u57ce"
                },
                {
                    "value": 1,
                    "name": "\u897f\u5c71"
                },
                {
                    "value": 1,
                    "name": "\u5343\u5cf0"
                },
                {
                    "value": 1,
                    "name": "\u987a\u4e49\u533a"
                },
                {
                    "value": 1,
                    "name": "\u6f4d\u574a"
                },
                {
                    "value": 1,
                    "name": "\u8857\u9053\u53e3"
                },
                {
                    "value": 1,
                    "name": "\u822a\u7a7a\u6e2f\u2026"
                },
                {
                    "value": 1,
                    "name": "\u8096\u5bb6\u6cb3"
                },
                {
                    "value": 1,
                    "name": "\u6587\u4e00\u8def"
                },
                {
                    "value": 1,
                    "name": "\u7acb\u6c34\u6865"
                },
                {
                    "value": 1,
                    "name": "\u56e2\u7ed3\u6e56"
                },
                {
                    "value": 1,
                    "name": "\u51bc\u6751"
                },
                {
                    "value": 1,
                    "name": "\u5e02\u5357\u533a"
                },
                {
                    "value": 1,
                    "name": "\u56db\u5b63\u9752"
                },
                {
                    "value": 1,
                    "name": "\u4ea4\u901a\u5927\u2026"
                },
                {
                    "value": 1,
                    "name": "\u4e5d\u9f99\u5761\u2026"
                },
                {
                    "value": 1,
                    "name": "\u5c0f\u884c"
                },
                {
                    "value": 1,
                    "name": "\u53cc\u6986\u6811"
                },
                {
                    "value": 1,
                    "name": "\u4e1c\u839e\u5e02"
                },
                {
                    "value": 1,
                    "name": "\u90d1\u4e1c\u65b0\u2026"
                },
                {
                    "value": 1,
                    "name": "\u5b9a\u6167\u5bfa"
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
                    "name": "\u5c55\u89c8\u8def"
                },
                {
                    "value": 1,
                    "name": "\u73e0\u6c5f\u65b0\u2026"
                },
                {
                    "value": 1,
                    "name": "\u5357\u4eac"
                },
                {
                    "value": 1,
                    "name": "\u9ad8\u7891\u5e97"
                },
                {
                    "value": 1,
                    "name": "\u5cb3\u9e93\u533a"
                },
                {
                    "value": 1,
                    "name": "\u79d1\u6280\u56ed\u2026"
                },
                {
                    "value": 1,
                    "name": "\u65b0\u6c5f\u6e7e\u2026"
                },
                {
                    "value": 1,
                    "name": "\u4e1c\u76f4\u95e8"
                },
                {
                    "value": 1,
                    "name": "\u9f13\u697c\u533a"
                },
                {
                    "value": 1,
                    "name": "\u4e07\u67f3"
                },
                {
                    "value": 1,
                    "name": "\u897f\u5173"
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
        chart_52beb97995c649be956bd359b66fe9a4.setOption(option_52beb97995c649be956bd359b66fe9a4);
    </script>
                <div id="2bf0758cf0af401d9e4a7030b27371a3" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_2bf0758cf0af401d9e4a7030b27371a3 = echarts.init(
            document.getElementById('2bf0758cf0af401d9e4a7030b27371a3'), 'white', {renderer: 'canvas'});
        var option_2bf0758cf0af401d9e4a7030b27371a3 = {
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
                446,
                352,
                217,
                201,
                184,
                135,
                129,
                96
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
                    "value": 446
                },
                {
                    "name": "\u4e0d\u9700\u8981\u878d\u8d44",
                    "value": 352
                },
                {
                    "name": "A\u8f6e",
                    "value": 217
                },
                {
                    "name": "B\u8f6e",
                    "value": 201
                },
                {
                    "name": "D\u8f6e\u53ca\u4ee5\u4e0a",
                    "value": 184
                },
                {
                    "name": "\u672a\u878d\u8d44",
                    "value": 135
                },
                {
                    "name": "C\u8f6e",
                    "value": 129
                },
                {
                    "name": "\u5929\u4f7f\u8f6e",
                    "value": 96
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
                    "value": 446
                },
                {
                    "name": "\u4e0d\u9700\u8981\u878d\u8d44",
                    "value": 352
                },
                {
                    "name": "A\u8f6e",
                    "value": 217
                },
                {
                    "name": "B\u8f6e",
                    "value": 201
                },
                {
                    "name": "D\u8f6e\u53ca\u4ee5\u4e0a",
                    "value": 184
                },
                {
                    "name": "\u672a\u878d\u8d44",
                    "value": 135
                },
                {
                    "name": "C\u8f6e",
                    "value": 129
                },
                {
                    "name": "\u5929\u4f7f\u8f6e",
                    "value": 96
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
        chart_2bf0758cf0af401d9e4a7030b27371a3.setOption(option_2bf0758cf0af401d9e4a7030b27371a3);
    </script>
                <div id="9fbfcbb90c6a40798531be2419d1fa57" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_9fbfcbb90c6a40798531be2419d1fa57 = echarts.init(
            document.getElementById('9fbfcbb90c6a40798531be2419d1fa57'), 'white', {renderer: 'canvas'});
        var option_9fbfcbb90c6a40798531be2419d1fa57 = {
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
                486,
                421,
                342,
                320,
                166,
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
            "type": "pie",
            "clockwise": true,
            "data": [
                {
                    "name": "2000\u4eba\u4ee5\u4e0a",
                    "value": 486
                },
                {
                    "name": "500-2000\u4eba",
                    "value": 421
                },
                {
                    "name": "150-500\u4eba",
                    "value": 342
                },
                {
                    "name": "50-150\u4eba",
                    "value": 320
                },
                {
                    "name": "15-50\u4eba",
                    "value": 166
                },
                {
                    "name": "\u5c11\u4e8e15\u4eba",
                    "value": 25
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
                    "value": 486
                },
                {
                    "name": "500-2000\u4eba",
                    "value": 421
                },
                {
                    "name": "150-500\u4eba",
                    "value": 342
                },
                {
                    "name": "50-150\u4eba",
                    "value": 320
                },
                {
                    "name": "15-50\u4eba",
                    "value": 166
                },
                {
                    "name": "\u5c11\u4e8e15\u4eba",
                    "value": 25
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
                "500-2000\u4eba",
                "150-500\u4eba",
                "50-150\u4eba",
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
                "2000\u4eba\u4ee5\u4e0a",
                "500-2000\u4eba",
                "150-500\u4eba",
                "50-150\u4eba",
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
        chart_9fbfcbb90c6a40798531be2419d1fa57.setOption(option_9fbfcbb90c6a40798531be2419d1fa57);
    </script>
                <div id="f3b6ba5499ce4bc5b66b3b3bf2dfd207" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_f3b6ba5499ce4bc5b66b3b3bf2dfd207 = echarts.init(
            document.getElementById('f3b6ba5499ce4bc5b66b3b3bf2dfd207'), 'white', {renderer: 'canvas'});
        var option_f3b6ba5499ce4bc5b66b3b3bf2dfd207 = {
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
                619,
                331,
                204,
                188,
                183,
                154,
                124
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
                    "value": 619,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,120,106)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u670d\u52a1",
                    "value": 331,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,135,34)"
                        }
                    }
                },
                {
                    "name": "\u8f6f\u4ef6\u670d\u52a1",
                    "value": 204,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,160,88)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u670d\u52a1",
                    "value": 188,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,69,18)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u786c\u4ef6",
                    "value": 183,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,95,29)"
                        }
                    }
                },
                {
                    "name": "IT\u6280\u672f\u670d\u52a1",
                    "value": 154,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,98,36)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u5177\u7c7b\u4ea7\u54c1",
                    "value": 124,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,144,134)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u6280\u91d1\u878d",
                    "value": 94,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,122,145)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u4e1a\u670d\u52a1",
                    "value": 91,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,160,132)"
                        }
                    }
                },
                {
                    "name": "\u6d88\u8d39\u751f\u6d3b",
                    "value": 76,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,33,73)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u8d44\u8baf",
                    "value": 73,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,13,45)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd",
                    "value": 68,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,83,116)"
                        }
                    }
                },
                {
                    "name": "\u79fb\u52a8\u4e92\u8054\u7f51",
                    "value": 66,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,104,145)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u9891",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,32,87)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u5a92\u4f53",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,0,65)"
                        }
                    }
                },
                {
                    "name": "\u77ed\u89c6\u9891",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,5,8)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546\u5e73\u53f0",
                    "value": 60,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,97,65)"
                        }
                    }
                },
                {
                    "name": "\u7269\u8054\u7f51",
                    "value": 59,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,25,68)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4ea4\u5e73\u53f0",
                    "value": 53,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,160,1)"
                        }
                    }
                },
                {
                    "name": "\u6e38\u620f",
                    "value": 49,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,30,53)"
                        }
                    }
                },
                {
                    "name": "\u5728\u7ebf\u6559\u80b2",
                    "value": 47,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,74,68)"
                        }
                    }
                },
                {
                    "name": "\u5176\u4ed6",
                    "value": 46,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,145,46)"
                        }
                    }
                },
                {
                    "name": "\u4f01\u4e1a\u670d\u52a1",
                    "value": 45,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,36,93)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u793e\u533a",
                    "value": 42,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,37,66)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u5b89\u5168",
                    "value": 33,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,4,62)"
                        }
                    }
                },
                {
                    "name": "\u8425\u9500\u670d\u52a1",
                    "value": 33,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,36,0)"
                        }
                    }
                },
                {
                    "name": "\u5728\u7ebf\u533b\u7597",
                    "value": 33,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,15,4)"
                        }
                    }
                },
                {
                    "name": "\u6559\u80b2",
                    "value": 32,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,78,10)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u6e38",
                    "value": 28,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,26,152)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u4e1a",
                    "value": 28,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,134,133)"
                        }
                    }
                },
                {
                    "name": "\u51fa\u884c",
                    "value": 27,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,14,108)"
                        }
                    }
                },
                {
                    "name": "\u5236\u9020\u4e1a",
                    "value": 26,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,26,117)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4ea4\u5a92\u4f53",
                    "value": 25,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,12,102)"
                        }
                    }
                },
                {
                    "name": "\u57f9\u8bad",
                    "value": 25,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,30,45)"
                        }
                    }
                },
                {
                    "name": "\u8f6f\u4ef6\u5f00\u53d1",
                    "value": 22,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,144,36)"
                        }
                    }
                },
                {
                    "name": "\u786c\u4ef6",
                    "value": 18,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,4,33)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u4e28\u5065\u5eb7",
                    "value": 18,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,117,65)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u68c0\u7d22",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,26,103)"
                        }
                    }
                },
                {
                    "name": "\u7269\u6d41",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,78,9)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u8f93",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,1,56)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,156,54)"
                        }
                    }
                },
                {
                    "name": "\u5c45\u4f4f\u670d\u52a1",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,60,7)"
                        }
                    }
                },
                {
                    "name": "\u76f4\u64ad\u5e73\u53f0",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,144,17)"
                        }
                    }
                },
                {
                    "name": "MCN",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,157,53)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u5bb9",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,59,80)"
                        }
                    }
                },
                {
                    "name": "\u4fdd\u5065",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,84,106)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u96f6\u552e",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,34,25)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,70,63)"
                        }
                    }
                },
                {
                    "name": "\u8d38\u6613",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,19,96)"
                        }
                    }
                },
                {
                    "name": "\u6c7d\u8f66\u4e28\u51fa\u884c",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,79,9)"
                        }
                    }
                },
                {
                    "name": "\u8fdb\u51fa\u53e3",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,98,52)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u552e",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,90,50)"
                        }
                    }
                },
                {
                    "name": "\u6279\u53d1",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,36,157)"
                        }
                    }
                },
                {
                    "name": "\u751f\u6d3b\u670d\u52a1",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,78,9)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,27,103)"
                        }
                    }
                },
                {
                    "name": "\u7269\u4e1a",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,129,111)"
                        }
                    }
                },
                {
                    "name": "\u623f\u5730\u4ea7",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,65,31)"
                        }
                    }
                },
                {
                    "name": "\u5efa\u7b51",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,65,17)"
                        }
                    }
                },
                {
                    "name": "\u7269\u6d41\u4e28\u8fd0\u8f93",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,80,91)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4ea4",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,139,113)"
                        }
                    }
                },
                {
                    "name": "\u6587\u5a31\u4e28\u5185\u5bb9",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,63,138)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u7edc\u901a\u4fe1",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,52,53)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u5177",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,6,97)"
                        }
                    }
                },
                {
                    "name": "\u80fd\u6e90",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,115,5)"
                        }
                    }
                },
                {
                    "name": "\u73af\u4fdd",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,102,109)"
                        }
                    }
                },
                {
                    "name": "\u5f71\u89c6",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,28,24)"
                        }
                    }
                },
                {
                    "name": "\u77ff\u4ea7",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,123,109)"
                        }
                    }
                },
                {
                    "name": "\u52a8\u6f2b",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,33,56)"
                        }
                    }
                },
                {
                    "name": "\u533a\u5757\u94fe",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,50,19)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u8425\u9500",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,0,18)"
                        }
                    }
                },
                {
                    "name": "\u7269\u6d41\u5e73\u53f0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,9,36)"
                        }
                    }
                },
                {
                    "name": "\u519c\u6797\u7267\u6e14",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,78,97)"
                        }
                    }
                },
                {
                    "name": "\u4e0d\u9650",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,154,28)"
                        }
                    }
                },
                {
                    "name": "\u6587\u5316\u4f20\u5a92",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,70,95)"
                        }
                    }
                },
                {
                    "name": "\u4f11\u95f2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,8,36)"
                        }
                    }
                },
                {
                    "name": "\u5a31\u4e50",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,23,108)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u3001\u8f6f\u4ef6\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,92,30)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5a92\u4f53",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,80,109)"
                        }
                    }
                },
                {
                    "name": "\u6c7d\u8f66\u4ea4\u6613\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,89,16)"
                        }
                    }
                },
                {
                    "name": "\u623f\u4ea7\u5bb6\u5c45",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,97,151)"
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
                "\u54a8\u8be2",
                "\u4eba\u5de5\u667a\u80fd\u670d\u52a1",
                "\u8f6f\u4ef6\u670d\u52a1",
                "\u6570\u636e\u670d\u52a1",
                "\u667a\u80fd\u786c\u4ef6",
                "IT\u6280\u672f\u670d\u52a1",
                "\u5de5\u5177\u7c7b\u4ea7\u54c1"
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
        chart_f3b6ba5499ce4bc5b66b3b3bf2dfd207.setOption(option_f3b6ba5499ce4bc5b66b3b3bf2dfd207);
    </script>
                <div id="7da50258cf3e46f9bef8dee4d9ae64bd" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_7da50258cf3e46f9bef8dee4d9ae64bd = echarts.init(
            document.getElementById('7da50258cf3e46f9bef8dee4d9ae64bd'), 'white', {renderer: 'canvas'});
        var option_7da50258cf3e46f9bef8dee4d9ae64bd = {
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
                503,
                111,
                97,
                50,
                47,
                33,
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
                    "value": 503,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,120,145)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u7b97\u6cd5",
                    "value": 111,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,36,102)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u7b97\u6cd5",
                    "value": 97,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,104,134)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5",
                    "value": 50,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,47,149)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 47,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,142,103)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                    "value": 33,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,5,3)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9\u7b97\u6cd5",
                    "value": 29,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,136,75)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u673a\u89c6\u89c9\u7b97\u6cd5",
                    "value": 25,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,93,29)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u7b97\u6cd5",
                    "value": 23,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,130,9)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u7b97\u6cd5",
                    "value": 23,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,96,36)"
                        }
                    }
                },
                {
                    "name": "slam\u7b97\u6cd5",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,157,147)"
                        }
                    }
                },
                {
                    "name": "ai\u7b97\u6cd5",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,52,21)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u8bc6\u522b\u7b97\u6cd5",
                    "value": 18,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,62,129)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u7b97\u6cd5",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,68,54)"
                        }
                    }
                },
                {
                    "name": "AI\u7b97\u6cd5",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,149,8)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u7b97\u6cd5",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,85,72)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u63a8\u8350\u7b97\u6cd5",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,93,143)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u9891\u7b97\u6cd5",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,71,128)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7136\u8bed\u8a00\u5904\u7406\u7b97\u6cd5",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,48,153)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u56fe\u50cf\u7b97\u6cd5",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,26,130)"
                        }
                    }
                },
                {
                    "name": "\u63a7\u5236\u7b97\u6cd5",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,0,77)"
                        }
                    }
                },
                {
                    "name": "\u611f\u77e5\u7b97\u6cd5",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,82,51)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u8bc6\u522b\u7b97\u6cd5",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,48,29)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u7b97\u6cd5",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,65,91)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u89c6\u89c9\u7b97\u6cd5",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,21,65)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7\u7b97\u6cd5",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,138,148)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6316\u6398\u7b97\u6cd5",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,59,108)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u63a8\u8350\u7b97\u6cd5",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,70,3)"
                        }
                    }
                },
                {
                    "name": "\u51e0\u4f55\u7b97\u6cd5",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,141,148)"
                        }
                    }
                },
                {
                    "name": "ocr\u7b97\u6cd5",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,92,61)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5904\u7406\u7b97\u6cd5",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,101,19)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u7814\u7b97\u6cd5",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,104,70)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u4f4d\u7b97\u6cd5",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,12,94)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7AI\u7b97\u6cd5",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,112,87)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u7b97\u6cd5",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,157,145)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7b97\u6cd5",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,19,132)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62\u7b97\u6cd5",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,79,92)"
                        }
                    }
                },
                {
                    "name": "CV\u7b97\u6cd5",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,152,69)"
                        }
                    }
                },
                {
                    "name": "SLAM\u7b97\u6cd5",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,155,66)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u7b97\u6cd5",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,123,141)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7cbe\u5730\u56fe\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,121,153)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,3,113)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7/\u8d44\u6df1\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,72,5)"
                        }
                    }
                },
                {
                    "name": "\u5f3a\u5316\u5b66\u4e60\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,112,142)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u611f\u77e5\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,52,127)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,20,9)"
                        }
                    }
                },
                {
                    "name": "\u51b3\u7b56\u89c4\u5212\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,134,136)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u8bc6\u56fe\u8c31\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,147,150)"
                        }
                    }
                },
                {
                    "name": "\u9065\u611f\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,160,112)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62\u56fe\u50cf\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,125,122)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u5168\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,103,29)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7f16\u7801\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,69,108)"
                        }
                    }
                },
                {
                    "name": "\u6fc0\u5149SLAM\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,109,106)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u589e\u957f\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,52,100)"
                        }
                    }
                },
                {
                    "name": "\u89c4\u5212\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,137,32)"
                        }
                    }
                },
                {
                    "name": "\u901a\u4fe1\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,134,67)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u63a8\u8350\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,10,142)"
                        }
                    }
                },
                {
                    "name": "\u8682\u8681\u96c6\u56e2-\u63a8\u8350\u641c\u7d22\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,96,98)"
                        }
                    }
                },
                {
                    "name": "GNSS\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,34,154)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79\u4f18\u5316\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,58,64)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u5408\u6210\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,24,1)"
                        }
                    }
                },
                {
                    "name": "\u5d4c\u5165\u5f0f\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,137,84)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u52a8\u63a7\u5236\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,25,127)"
                        }
                    }
                },
                {
                    "name": "\u7b56\u7565\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,89,141)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u97f3\u9891\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,109,28)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79\u5b66\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,20,93)"
                        }
                    }
                },
                {
                    "name": "CT\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,4,65)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,116,18)"
                        }
                    }
                },
                {
                    "name": "\u8def\u5f84\u89c4\u5212\u4e0e\u63a7\u5236\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,101,28)"
                        }
                    }
                },
                {
                    "name": "\u5b9e\u4e60\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,81,3)"
                        }
                    }
                },
                {
                    "name": "\u5171\u8bc6\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,72,157)"
                        }
                    }
                },
                {
                    "name": "\u91cf\u5316\u4ea4\u6613\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,14,147)"
                        }
                    }
                },
                {
                    "name": "\u9065\u611f\u56fe\u50cf\u5904\u7406\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,39,149)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u8bed\u97f3\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,79,41)"
                        }
                    }
                },
                {
                    "name": "\u6fc0\u5149\u96f7\u8fbe\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,80,9)"
                        }
                    }
                },
                {
                    "name": "\u6821\u62db-\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,18,20)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u611f\u77e5\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,144,149)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u5b66\u4e60/\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,154,151)"
                        }
                    }
                },
                {
                    "name": "3D\u89c6\u89c9\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,94,90)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u91cd\u5efa\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,131,38)"
                        }
                    }
                },
                {
                    "name": "\u521d\u7ea7\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,112,53)"
                        }
                    }
                },
                {
                    "name": "\u8def\u5f84\u89c4\u5212\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,47,22)"
                        }
                    }
                },
                {
                    "name": "\u9884\u6d4b\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,111,41)"
                        }
                    }
                },
                {
                    "name": "\u6210\u50cf\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,111,105)"
                        }
                    }
                },
                {
                    "name": "AI \u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,103,109)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u9875\u641c\u7d22-\u591a\u6a21\u6001\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,41,149)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u8c03\u5ea6\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,58,58)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u5546\u54c1\u641c\u7d22\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,156,39)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7f16\u89e3\u7801\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,115,55)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,9,82)"
                        }
                    }
                },
                {
                    "name": "OCR\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,43,48)"
                        }
                    }
                },
                {
                    "name": "SK6563-PTBU-\u4e2a\u6027\u5316\u63a8\u8350\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,92,146)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u68c0\u7d22\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,94,86)"
                        }
                    }
                },
                {
                    "name": "GJ2127-SPBU-\u7f8e\u989c\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,108,146)"
                        }
                    }
                },
                {
                    "name": "\u533a\u5757\u94fe\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,137,115)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u53f7\u5904\u7406\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,101,108)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u8d37\u6a21\u578b\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,11,117)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u56fe\u50cf\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,106,66)"
                        }
                    }
                },
                {
                    "name": "\u533b\u5b66\u5f71\u50cf\u5904\u7406\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,70,117)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u97f3\u9891\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,78,52)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u7ea7\u56fe\u50cf\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,64,16)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u641c\u7d22\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,66,12)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u5f0f\u8bc6\u522b\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,95,136)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u5bfc\u822a\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,137,61)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u3001\u56fe\u50cf\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,132,35)"
                        }
                    }
                },
                {
                    "name": "\u5bfc\u822a\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,54,113)"
                        }
                    }
                },
                {
                    "name": "\u4e2a\u6027\u5316\u63a8\u8350\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,94,24)"
                        }
                    }
                },
                {
                    "name": "NLP\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,28,63)"
                        }
                    }
                },
                {
                    "name": "\u7b56\u7565\u67b6\u6784\u7814\u53d1\u5de5\u7a0b\u5e08\uff08\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,0,44)"
                        }
                    }
                },
                {
                    "name": "\u6fc0\u5149\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,67,60)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u56e2\u914d\u9001-\u5730\u56fe\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,30,45)"
                        }
                    }
                },
                {
                    "name": "VU1966-SPBU-AI\u5de5\u7a0b\u5316\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,37,108)"
                        }
                    }
                },
                {
                    "name": "\u63a5\u7ba1\u9884\u8b66\u7b56\u7565\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,49,136)"
                        }
                    }
                },
                {
                    "name": "0232S5-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,101,151)"
                        }
                    }
                },
                {
                    "name": "RTK\u5b9a\u4f4d\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,68,69)"
                        }
                    }
                },
                {
                    "name": "113195-\u97f3\u89c6\u9891\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,144,60)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u63a7\u5236\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,38,148)"
                        }
                    }
                },
                {
                    "name": "ADAS\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,98,111)"
                        }
                    }
                },
                {
                    "name": "PCG-\u5e7f\u544a\u589e\u957f\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,114,151)"
                        }
                    }
                },
                {
                    "name": "3D \u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,34,1)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62\u5b66\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,80,131)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u5e94\u7528\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,60,110)"
                        }
                    }
                },
                {
                    "name": "11318V-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,146,18)"
                        }
                    }
                },
                {
                    "name": "\u8f66\u8f86\u52a8\u529b\u5b66\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,71,45)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u8f6f\u5185\u63a8 - \u5f00\u53d1/\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,36,36)"
                        }
                    }
                },
                {
                    "name": "TTS\u8bed\u97f3\u5408\u6210\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,20,40)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5206\u6790\uff08\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,13,151)"
                        }
                    }
                },
                {
                    "name": "\u533b\u5b66\u5149\u8c31\u5b66\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,95,69)"
                        }
                    }
                },
                {
                    "name": "\u96c6\u7fa4\u8c03\u5ea6\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,10,154)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u5de5\u7a0b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,52,130)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u538b\u7f29\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,82,143)"
                        }
                    }
                },
                {
                    "name": "\u5168\u6c11K\u6b4c\u5185\u5bb9\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,130,130)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7\u53cd\u6b3a\u8bc8\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,45,95)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60/\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,75,97)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u7ed3\u6784\u5316\u6570\u636e\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,24,10)"
                        }
                    }
                },
                {
                    "name": "2021\u6821\u62db-\u5927\u6570\u636e\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,28,18)"
                        }
                    }
                },
                {
                    "name": "\u6e32\u67d3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,69,58)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u8bed\u97f3\u8bc6\u522b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,75,52)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,90,37)"
                        }
                    }
                },
                {
                    "name": "2021\u6821\u62db-GNSS\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,44,110)"
                        }
                    }
                },
                {
                    "name": "LJ5001-SPBU-\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,47,89)"
                        }
                    }
                },
                {
                    "name": "\u533b\u5b66\u5f71\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,27,32)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5206\u6790\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,22,133)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u8a00\u6a21\u578b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,47,17)"
                        }
                    }
                },
                {
                    "name": "\u70b9\u4e91\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,141,16)"
                        }
                    }
                },
                {
                    "name": "2021\u6821\u62db-\u5b8c\u597d\u6027\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,59,119)"
                        }
                    }
                },
                {
                    "name": "024208-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,113,11)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u89c6\u9891\u7f16\u89e3\u7801\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,33,15)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7Gnss\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,88,134)"
                        }
                    }
                },
                {
                    "name": "25317O-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,51,158)"
                        }
                    }
                },
                {
                    "name": "SG8103-SPBU-\u89c6\u9891\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,62,62)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u5f00\u53d1\u5de5\u7a0b\u5e08\uff08\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,108,128)"
                        }
                    }
                },
                {
                    "name": "0241QC-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,39,52)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u56e2App-\u7f8e\u56e2\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,110,46)"
                        }
                    }
                },
                {
                    "name": "\u5546\u54c1\u7ecf\u8425\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,142,4)"
                        }
                    }
                },
                {
                    "name": "\u30102021\u79cb\u62db\u3011\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,86,111)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6316\u6398\u5de5\u7a0b\u5e08/AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,63,68)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u5b89\u5168\u53ca\u5bc6\u7801\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,82,118)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u5206\u6790\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,95,45)"
                        }
                    }
                },
                {
                    "name": "11122K-LT-310-\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,64,105)"
                        }
                    }
                },
                {
                    "name": "AR\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,143,46)"
                        }
                    }
                },
                {
                    "name": "RU0112-SPBU-\u89c6\u9891\u7f16\u89e3\u7801\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,72,108)"
                        }
                    }
                },
                {
                    "name": "\u751f\u6001\u94fe-Slam\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,42,28)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u7406\u89e3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,55,88)"
                        }
                    }
                },
                {
                    "name": "\u4f9b\u5e94\u94fe\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,91,33)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf/\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,46,94)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u8425\u9500\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,25,139)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u6d41\u5e7f\u544a-\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,79,112)"
                        }
                    }
                },
                {
                    "name": "\u641c\u72d7\u6570\u5b57\u4eba-3D\u4eba\u8138\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,59,61)"
                        }
                    }
                },
                {
                    "name": "BK32CA-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,81,43)"
                        }
                    }
                },
                {
                    "name": "11414F-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,1,23)"
                        }
                    }
                },
                {
                    "name": "\u753b\u8d28\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,148,8)"
                        }
                    }
                },
                {
                    "name": "3D\u91cd\u5efa\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,9,136)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u7ade\u4ef7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,57,106)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u4eba\u9a7e\u9a76\u8f66\u8f86\u63a7\u5236\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,21,152)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u8bed\u97f3\u8bc6\u522b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,77,133)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7136\u8bed\u8a00\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,78,10)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u56fe\u5f62\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,18,150)"
                        }
                    }
                },
                {
                    "name": "\u3010\u7f8e\u56e2\u4f18\u9009\u3011-\u8425\u9500\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,20,121)"
                        }
                    }
                },
                {
                    "name": "\u3010\u6821\u62db\u3011\u641c\u7d22\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,126,100)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u5524\u9192\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,130,89)"
                        }
                    }
                },
                {
                    "name": "\u641c\u72d7\u5730\u56fe-SLAM\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,148,137)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,25,84)"
                        }
                    }
                },
                {
                    "name": "\u58f0\u7eb9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,37,157)"
                        }
                    }
                },
                {
                    "name": "BK4658-SPBU-NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,10,70)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,118,13)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u95fb\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,9,59)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,2,22)"
                        }
                    }
                },
                {
                    "name": "26310R-\u81ea\u7136\u8bed\u8a00\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,142,105)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,7,130)"
                        }
                    }
                },
                {
                    "name": "MIG-\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,145,81)"
                        }
                    }
                },
                {
                    "name": "254151-\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,47,45)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,88,62)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u7ea7AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,66,68)"
                        }
                    }
                },
                {
                    "name": "\u51b3\u7b56\u548c\u8fd0\u52a8\u89c4\u5212\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,73,117)"
                        }
                    }
                },
                {
                    "name": "11312G-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,43,2)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u9690\u79c1\u8ba1\u7b97\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,47,21)"
                        }
                    }
                },
                {
                    "name": "SPBU-\u9ad8\u7ea7\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,7,14)"
                        }
                    }
                },
                {
                    "name": "OP2255-PTBU-\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,66,4)"
                        }
                    }
                },
                {
                    "name": "254138-NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,94,117)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u7ffb\u8bd1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,117,68)"
                        }
                    }
                },
                {
                    "name": "0341DN-\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,7,35)"
                        }
                    }
                },
                {
                    "name": "1131OJ-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,61,78)"
                        }
                    }
                },
                {
                    "name": "LJ5001-\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,35,54)"
                        }
                    }
                },
                {
                    "name": "\u5b9e\u65f6\u8def\u51b5\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,101,71)"
                        }
                    }
                },
                {
                    "name": "00206-NLP\u9ad8\u7ea7\u5de5\u7a0b\u5e08/\u8d44\u6df1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,47,56)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u5b89\u5168-\u97f3\u9891\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,17,79)"
                        }
                    }
                },
                {
                    "name": "\u5343\u5bfb\u4f4d\u7f6e-RTK\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,112,29)"
                        }
                    }
                },
                {
                    "name": "SW-\u673a\u5668\u4eba\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,59,146)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u5de5\u7a0b\u5e08-\u56fe\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,122,61)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,146,57)"
                        }
                    }
                },
                {
                    "name": "1141DK-\u8d44\u6df1\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,126,80)"
                        }
                    }
                },
                {
                    "name": "\u3010\u4e0a\u6d77\u677e\u6c5f\u533a\u3011\u6545\u969c\u9884\u6d4b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,7,158)"
                        }
                    }
                },
                {
                    "name": "\u5546\u4e1a\u641c\u7d22-\u5e7f\u544a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,69,110)"
                        }
                    }
                },
                {
                    "name": "KHQ-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,112,65)"
                        }
                    }
                },
                {
                    "name": "AIOPs\u5e94\u7528\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,119,141)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u5e7f\u544a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,90,9)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u8bc4\u6d4b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,85,112)"
                        }
                    }
                },
                {
                    "name": "AI\u8d44\u6df1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,10,76)"
                        }
                    }
                },
                {
                    "name": "FF2824-\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,52,141)"
                        }
                    }
                },
                {
                    "name": "TX2980-SPBU-\u9ad8\u7ea7\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,126,14)"
                        }
                    }
                },
                {
                    "name": "11413B-NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,130,87)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u56e2APP\u90e8-\u5e7f\u544a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,2,46)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u7ebf\u7535\u4fe1\u53f7\u8bc6\u522b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,2,144)"
                        }
                    }
                },
                {
                    "name": "\u5546\u4e1a\u5e7f\u544a-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,160,69)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6316\u6398\u4e0e\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,134,103)"
                        }
                    }
                },
                {
                    "name": "WMPS-\u7f8e\u56e2\u914d\u9001-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,3,134)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9\u4e09\u7ef4\u9ad8\u7cbe\u5efa\u56fe\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,82,143)"
                        }
                    }
                },
                {
                    "name": "\u5730\u56fe\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,124,111)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u5e7f\u544a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,97,91)"
                        }
                    }
                },
                {
                    "name": "\u89c4\u5212\u5bfc\u822a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,130,118)"
                        }
                    }
                },
                {
                    "name": "11412I-\u8d44\u6df1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,147,130)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u89c6\u9891\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,121,14)"
                        }
                    }
                },
                {
                    "name": "\u51b3\u7b56\u4e0e\u8fd0\u52a8\u89c4\u5212\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,67,78)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,133,119)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7/\u8d44\u6df1\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,134,128)"
                        }
                    }
                },
                {
                    "name": "\u817e\u8baf\u770b\u70b9\u5546\u4e1a\u5316\u5e7f\u544a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,78,32)"
                        }
                    }
                },
                {
                    "name": "\u3010\u5357\u4eac\u3011\u56fe\u5f62\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,115,139)"
                        }
                    }
                },
                {
                    "name": "\u7f16\u8bd1\u5668\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,105,105)"
                        }
                    }
                },
                {
                    "name": "\u79fb\u52a8\u7aef\u63a8\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,72,143)"
                        }
                    }
                },
                {
                    "name": "1141BC-\u673a\u5668\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,112,5)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u70b9\u4e91\u5206\u6790\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,102,8)"
                        }
                    }
                },
                {
                    "name": "\u30102021\u6821\u62db\u3011\u5e7f\u544a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,119,144)"
                        }
                    }
                },
                {
                    "name": "\u3010\u7d27\u6025\u5c97\u4f4d\u3011\u301095\u5206\u3011\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,85,153)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u603b\u76d1\uff08\u6570\u636e\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,136,124)"
                        }
                    }
                },
                {
                    "name": "024294-AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,134,152)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350/\u5e7f\u544a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,73,98)"
                        }
                    }
                },
                {
                    "name": "11122N-LT-311-\u8bed\u97f3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,33,152)"
                        }
                    }
                },
                {
                    "name": "\u5b9e\u4e60\u751f-\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,133,106)"
                        }
                    }
                },
                {
                    "name": "55413O-AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,126,17)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,76,57)"
                        }
                    }
                },
                {
                    "name": "AI/\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,97,17)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u98ce\u63a7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,123,138)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,90,75)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9/\u70b9\u4e91\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,81,5)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7/\u4e2d\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,89,24)"
                        }
                    }
                },
                {
                    "name": "1141BI-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,55,99)"
                        }
                    }
                },
                {
                    "name": "\u7f16\u89e3\u7801\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,144,41)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u5b66\u4e60\u5e73\u53f0&\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,69,158)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u6c7d\u8f66\u4e8b\u4e1a\u90e8_\u611f\u77e5\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,131,49)"
                        }
                    }
                },
                {
                    "name": "02416A-NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,136,144)"
                        }
                    }
                },
                {
                    "name": "11122I-LT-312-NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,109,91)"
                        }
                    }
                },
                {
                    "name": "\u533a\u5757\u94fe\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,50,64)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,117,68)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u9875\u641c\u7d22-\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,145,2)"
                        }
                    }
                },
                {
                    "name": "\u76ee\u6807\u68c0\u6d4b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,55,117)"
                        }
                    }
                },
                {
                    "name": "324121-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,155,13)"
                        }
                    }
                },
                {
                    "name": "SS1060-SPBU-\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,153,134)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u7edc\u56fe\u8c31\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,71,120)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u6c7d\u8f66\u4e8b\u4e1a\u90e8_\u8f66\u8f86\u63a7\u5236\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,29,44)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u9669\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,68,6)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u8138\u8bc6\u522b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,148,88)"
                        }
                    }
                },
                {
                    "name": "\u5a92\u4f53\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,39,131)"
                        }
                    }
                },
                {
                    "name": "AR\u56fe\u5f62\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,127,134)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\uff08\u56fe\u50cf\u8bc6\u522b\uff09\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,104,16)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5e94\u7528\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,126,49)"
                        }
                    }
                },
                {
                    "name": "\u57ce\u5e02\u8ba1\u7b97\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,146,82)"
                        }
                    }
                },
                {
                    "name": "2D/3D\u56fe\u5f62\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,7,121)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u4eba\u4f53/\u4e09\u7ef4\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,117,77)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u722c\u866b\u7b56\u7565\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,77,110)"
                        }
                    }
                },
                {
                    "name": "114125-\u8d44\u6df1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,60,53)"
                        }
                    }
                },
                {
                    "name": "\u533b\u5b66\u5f71\u50cf\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,18,44)"
                        }
                    }
                },
                {
                    "name": "0241VZ-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,126,39)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u6570\u636e\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,102,158)"
                        }
                    }
                },
                {
                    "name": "\u8def\u7f51\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,48,143)"
                        }
                    }
                },
                {
                    "name": "[\u6025]\u7f51\u5b89\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,114,132)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u6570\u636e\u6316\u6398\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,93,24)"
                        }
                    }
                },
                {
                    "name": "\u8f66\u8f86\u5b9a\u4f4d\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,130,110)"
                        }
                    }
                },
                {
                    "name": "29912-\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,106,80)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7\u7b56\u7565\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,136,92)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1(\u63a8\u8350)\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,30,140)"
                        }
                    }
                },
                {
                    "name": "55414C-AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,145,159)"
                        }
                    }
                },
                {
                    "name": "CG8005-SPBU-3D\u6e32\u67d3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,102,25)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u8ba1\u7b97\u673a\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,107,107)"
                        }
                    }
                },
                {
                    "name": "2021\u6821\u62db-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,117,74)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,130,102)"
                        }
                    }
                },
                {
                    "name": "\u91cf\u5316\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,38,86)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u56e2APP\u2014\u9ad8\u7ea7\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,17,151)"
                        }
                    }
                },
                {
                    "name": "AF\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,106,124)"
                        }
                    }
                },
                {
                    "name": "\u589e\u5f3a\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,51,39)"
                        }
                    }
                },
                {
                    "name": "02426A-NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,112,131)"
                        }
                    }
                },
                {
                    "name": "ARVR/\u673a\u5668\u89c6\u89c9/\u56fe\u50cf\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,36,25)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u7814\u53d1\u5de5\u7a0b\u5e08-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,135,113)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u5316\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,8,123)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u989c\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,69,147)"
                        }
                    }
                },
                {
                    "name": "\u30102021\u6821\u62db\u3011\u8bed\u97f3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,41,76)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,114,112)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6316\u6398/\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,13,152)"
                        }
                    }
                },
                {
                    "name": "1141BD-\u81ea\u7136\u8bed\u8a00\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,88,69)"
                        }
                    }
                },
                {
                    "name": "39318E-\u8ba1\u7b97\u673a\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,82,102)"
                        }
                    }
                },
                {
                    "name": "1131HA-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,151,99)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u53ca\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,145,64)"
                        }
                    }
                },
                {
                    "name": "11413S-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,134,133)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5206\u6790\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,111,82)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u56e2\u9a91\u884c-\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,132,15)"
                        }
                    }
                },
                {
                    "name": "\u3010\u6df1\u5733\u3011GNSS\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,46,111)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u4fe1\u53f7\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,138,133)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u89c6\u9891/\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,117,19)"
                        }
                    }
                },
                {
                    "name": "\u7ec4\u5408\u5bfc\u822a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,34,142)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u89c4\u5212\u4e0e\u51b3\u7b56\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,104,46)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u9645\u5316\u5b9a\u4ef7\u8865\u8d34\u4e13\u5bb6\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,159,126)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,141,38)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u641c\u7d22\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,89,33)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u77e5\u8bc6\u56fe\u8c31\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,81,76)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,84,65)"
                        }
                    }
                },
                {
                    "name": "11416Z-AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,137,126)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u5e73\u53f0-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,16,85)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,34,113)"
                        }
                    }
                },
                {
                    "name": "SJY-\u81ea\u7136\u8bed\u8a00\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,87,105)"
                        }
                    }
                },
                {
                    "name": "\u5929\u773c\u67e5 \u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,126,128)"
                        }
                    }
                },
                {
                    "name": "39314F-\u901a\u7528\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,63,94)"
                        }
                    }
                },
                {
                    "name": "\u6316\u6398\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,115,117)"
                        }
                    }
                },
                {
                    "name": "\u6fc0\u5149\u5b9a\u4f4d\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,20,31)"
                        }
                    }
                },
                {
                    "name": "\u5e94\u7528\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,68,24)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u56e2App-\u4ea4\u6613\u94fe\u8def\u63a8\u8350-\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,140,78)"
                        }
                    }
                },
                {
                    "name": "55413N-AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,50,72)"
                        }
                    }
                },
                {
                    "name": "PCG09-\u7528\u6237\u589e\u957f\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,150,54)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u56e2APP\u2014\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,104,26)"
                        }
                    }
                },
                {
                    "name": "05415O-AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,86,146)"
                        }
                    }
                },
                {
                    "name": "Vslam\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,5,117)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,151,81)"
                        }
                    }
                },
                {
                    "name": "\u5b9e\u4e60\u9065\u611f\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,141,83)"
                        }
                    }
                },
                {
                    "name": "BL5944-SPBU-\u7f8e\u989c\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,80,76)"
                        }
                    }
                },
                {
                    "name": "\u663e\u793a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,113,151)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,95,92)"
                        }
                    }
                },
                {
                    "name": "11122J-LT-312-NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,43,76)"
                        }
                    }
                },
                {
                    "name": "\u5bf9\u8bdd\u63a8\u8350\u8d44\u6df1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,41,56)"
                        }
                    }
                },
                {
                    "name": "024168-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,72,88)"
                        }
                    }
                },
                {
                    "name": "\u3010\u6821\u62db\u3011\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,158,111)"
                        }
                    }
                },
                {
                    "name": "\u751f\u7269\u4fe1\u606f\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,36,151)"
                        }
                    }
                },
                {
                    "name": "11417L-NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,95,40)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u5168\u7b56\u7565\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,24,129)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u673a\u56fe\u5f62\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,59,155)"
                        }
                    }
                },
                {
                    "name": "\u7814\u7a76\u578b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,138,135)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u6392\u5e8f\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,133,3)"
                        }
                    }
                },
                {
                    "name": "\u3010\u5357\u4eac\u3011\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,68,47)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u9875\u641c\u7d22-\u641c\u7d22\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,92,157)"
                        }
                    }
                },
                {
                    "name": "\u5916\u5356\u6280\u672f\u90e8-\u8d44\u6df1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,89,3)"
                        }
                    }
                },
                {
                    "name": "55413P-AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,26,155)"
                        }
                    }
                },
                {
                    "name": "\u878d\u5408\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,2,149)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u667a\u80fd\u7ec4-\u98ce\u63a7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,129,14)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u6280\u672f\u5e73\u53f0\u90e8-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,33,5)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u4e0e\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,71,151)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7GNSS\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,19,77)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u4f533D\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,11,55)"
                        }
                    }
                },
                {
                    "name": "AY0300-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,20,91)"
                        }
                    }
                },
                {
                    "name": "Soul App-\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,47,11)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u70b9\u4e91\u5206\u6790\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,28,103)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u8ba1\u7b97\u673a\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,40,3)"
                        }
                    }
                },
                {
                    "name": "0232KT-\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,130,2)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,155,156)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7\u6a21\u578b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,21,58)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u56e2App\u90e8-\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,160,55)"
                        }
                    }
                },
                {
                    "name": "\u30102021\u6821\u62db\u3011\u8ba1\u7b97\u673a\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,102,115)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u4ea7\u54c1\u7ecf\u7406(\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,129,70)"
                        }
                    }
                },
                {
                    "name": "1121PC-LT-354-\u5927\u6570\u636e\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,152,127)"
                        }
                    }
                },
                {
                    "name": "1121XJ-\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,122,44)"
                        }
                    }
                },
                {
                    "name": "XH4713-\u6d41\u5a92\u4f53\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,122,68)"
                        }
                    }
                },
                {
                    "name": "\u5730\u56fe\u5b9a\u4f4d\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,96,38)"
                        }
                    }
                },
                {
                    "name": "\u5929\u732b\u597d\u623f-\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,75,73)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u4fe1\u53f7\u5904\u7406/\u8bed\u97f3\u8bc6\u522b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,121,97)"
                        }
                    }
                },
                {
                    "name": "\u98de\u63a7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,47,33)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u81ea\u7136\u8bed\u8a00\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,78,127)"
                        }
                    }
                },
                {
                    "name": "5G\u57fa\u5e26\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,92,36)"
                        }
                    }
                },
                {
                    "name": "0241UC-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,87,110)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,80,73)"
                        }
                    }
                },
                {
                    "name": "\u30102021\u6821\u62db\u3011\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,134,105)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5206\u6790/\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,57,78)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u4fe1\u53f7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,125,24)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u5e7f\u544a\u6295\u653e\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,131,30)"
                        }
                    }
                },
                {
                    "name": "\u8c03\u5ea6\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,29,95)"
                        }
                    }
                },
                {
                    "name": "00233-\u5d4c\u5165\u5f0f\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,19,153)"
                        }
                    }
                },
                {
                    "name": "\u5168\u6c11K\u6b4c\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,123,151)"
                        }
                    }
                },
                {
                    "name": "\u58f0\u5b66\u6a21\u578b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,76,106)"
                        }
                    }
                },
                {
                    "name": "\u89c4\u5212\u8c03\u5ea6\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,42,69)"
                        }
                    }
                },
                {
                    "name": "0341DO-NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,141,121)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9\u5b9a\u4f4d\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,77,43)"
                        }
                    }
                },
                {
                    "name": "114114-\u9ad8\u7ea7/\u8d44\u6df1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,4,132)"
                        }
                    }
                },
                {
                    "name": "\u30102021\u79cb\u62db\u3011\u97f3\u89c6\u9891\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,158,102)"
                        }
                    }
                },
                {
                    "name": "\u641c\u72d7\u533b\u7597\u641c\u7d22-\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,126,152)"
                        }
                    }
                },
                {
                    "name": "EIG-\u9065\u611f\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,157,62)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u89c6\u9891\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,11,79)"
                        }
                    }
                },
                {
                    "name": "\u5bc6\u7801\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,84,81)"
                        }
                    }
                },
                {
                    "name": "\u878d\u5408\u5b9a\u4f4d\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,118,132)"
                        }
                    }
                },
                {
                    "name": "00239-\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,152,46)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u6d6a\u8d22\u7ecf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,126,129)"
                        }
                    }
                },
                {
                    "name": "[\u6025]\u7f51\u5b89\u8d44\u6df1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,35,144)"
                        }
                    }
                },
                {
                    "name": "\u672c\u5730\u751f\u6d3b-\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,9,127)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u56e2App-\u7528\u6237\u589e\u957f\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,34,79)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u4e0eNLP\u90e8-\u641c\u7d22\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,27,122)"
                        }
                    }
                },
                {
                    "name": "\u58f0\u5b66\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,9,70)"
                        }
                    }
                },
                {
                    "name": "\u4eca\u65e5\u5934\u6761-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,28,50)"
                        }
                    }
                },
                {
                    "name": "09412L-NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,120,129)"
                        }
                    }
                },
                {
                    "name": "\u8bca\u65ad\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,47,94)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u56e2\u4f18\u9009-\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,112,134)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9\u56fe\u50cf\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,33,51)"
                        }
                    }
                },
                {
                    "name": "Feed\u6d41\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,37,15)"
                        }
                    }
                },
                {
                    "name": "11122M-LT-311-\u8bed\u97f3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,86,89)"
                        }
                    }
                },
                {
                    "name": "DL5011-nlp\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,8,48)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5f81\u4fe1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,149,84)"
                        }
                    }
                },
                {
                    "name": "3D\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,79,95)"
                        }
                    }
                },
                {
                    "name": "\u6fc0\u5149SLAM/\u591a\u4f20\u611f\u5668\u878d\u5408\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,150,132)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u548c\u89c6\u9891\u7406\u89e3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,76,64)"
                        }
                    }
                },
                {
                    "name": "npu\u67b6\u6784\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,100,34)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6a21\u578b\u5de5\u7a0b\u5e08\uff08\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,17,129)"
                        }
                    }
                },
                {
                    "name": "AI\u5730\u56fe\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,128,71)"
                        }
                    }
                },
                {
                    "name": "\u5546\u4e1a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,43,48)"
                        }
                    }
                },
                {
                    "name": "2021\u6821\u56ed\u62db\u8058-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,62,159)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u53f7/\u97f3\u4e50\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,148,112)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u63a7\u5236\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,140,116)"
                        }
                    }
                },
                {
                    "name": "AEB/LKA/ACC\u7814\u53d1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,16,6)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5916\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,27,65)"
                        }
                    }
                },
                {
                    "name": "\u6821\u62db-\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,14,145)"
                        }
                    }
                },
                {
                    "name": "1141CU-\u8d44\u6df1\u81ea\u7136\u8bed\u8a00\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,87,39)"
                        }
                    }
                },
                {
                    "name": "113154-\u8d44\u6df1/\u4e13\u5bb6\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,93,15)"
                        }
                    }
                },
                {
                    "name": "\u591a\u5a92\u4f53\u89c6\u9891\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,148,33)"
                        }
                    }
                },
                {
                    "name": "\u591a\u6a21\u6001\u8d44\u6df1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,29,66)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u81ea\u7136\u8bed\u8a00\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,102,128)"
                        }
                    }
                },
                {
                    "name": "\u589e\u957f\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,16,120)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,117,10)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u6280\u53d1\u5c55\u90e8-AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,44,132)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7/\u8d44\u6df1\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,16,147)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,84,95)"
                        }
                    }
                },
                {
                    "name": "\u591a\u4f20\u611f\u5668\u878d\u5408\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,40,35)"
                        }
                    }
                },
                {
                    "name": "02429L-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,18,70)"
                        }
                    }
                },
                {
                    "name": "nlp/cv \u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,116,157)"
                        }
                    }
                },
                {
                    "name": "Slam\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,32,135)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u63a8\u8350\u5f00\u53d1\uff08\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,34,140)"
                        }
                    }
                },
                {
                    "name": "SJY-\u9ad8\u7ea7\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,75,112)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u56e2\u914d\u9001-\u667a\u80fd\u5b9a\u4ef7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,70,56)"
                        }
                    }
                },
                {
                    "name": "\u6c14\u8c61\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,4,102)"
                        }
                    }
                },
                {
                    "name": "\u9910\u996eSaaS\u6280\u672f\u90e8-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,72,151)"
                        }
                    }
                },
                {
                    "name": "0341ET-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,28,21)"
                        }
                    }
                },
                {
                    "name": "024254-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,67,82)"
                        }
                    }
                },
                {
                    "name": "\u7acb\u4f53\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,50,93)"
                        }
                    }
                },
                {
                    "name": "\u5929\u732b\u7cbe\u7075\u4e8b\u4e1a\u90e8-\u8bed\u97f3\u5408\u6210\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,47,79)"
                        }
                    }
                },
                {
                    "name": "\uff08\u6821\u62db\uff09\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,38,49)"
                        }
                    }
                },
                {
                    "name": "\u58f0\u7eb9\u8bc6\u522b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,148,15)"
                        }
                    }
                },
                {
                    "name": "11312H-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,66,149)"
                        }
                    }
                },
                {
                    "name": "\u641c\u72d7\u624b\u5199\u8bc6\u522b-\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,76,153)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u7cfb\u7edf\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,78,139)"
                        }
                    }
                },
                {
                    "name": "11312J-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,81,7)"
                        }
                    }
                },
                {
                    "name": "SLAM/VIO/\u4e09\u7ef4\u91cd\u5efa\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,31,68)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9slam/vslam\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,118,152)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u5e73\u53f0-\u8d44\u6df1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,69,70)"
                        }
                    }
                },
                {
                    "name": "\u6d41\u5a92\u4f53\u4f20\u8f93\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,4,44)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5916\u6d4f\u89c8\u5668\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,76,9)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u52a8\u5065\u5eb7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,160,137)"
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
                "\u7b97\u6cd5",
                "\u63a8\u8350\u7b97\u6cd5",
                "\u56fe\u50cf\u7b97\u6cd5",
                "\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5",
                "\u9ad8\u7ea7\u7b97\u6cd5",
                "\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                "\u89c6\u89c9\u7b97\u6cd5"
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
        chart_7da50258cf3e46f9bef8dee4d9ae64bd.setOption(option_7da50258cf3e46f9bef8dee4d9ae64bd);
    </script>
                <div id="860a1b78649e4a07bcc3bb4fbe0bedac" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_860a1b78649e4a07bcc3bb4fbe0bedac = echarts.init(
            document.getElementById('860a1b78649e4a07bcc3bb4fbe0bedac'), 'white', {renderer: 'canvas'});
            
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
    
        var option_860a1b78649e4a07bcc3bb4fbe0bedac = {
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
                    "value": 245,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,131,36)"
                        }
                    }
                },
                {
                    "name": "\u516d\u9669\u4e00\u91d1",
                    "value": 125,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,147,76)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u5e74\u5047",
                    "value": 113,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,37,143)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u7a7a\u95f4\u5927",
                    "value": 107,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,126,30)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u5de5\u4f5c",
                    "value": 85,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,141,155)"
                        }
                    }
                },
                {
                    "name": "\u5468\u672b\u53cc\u4f11",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,74,7)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u4f11",
                    "value": 67,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,106,68)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4\u597d",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,22,121)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5e73\u53f0",
                    "value": 62,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,59,44)"
                        }
                    }
                },
                {
                    "name": "\u8282\u65e5\u798f\u5229",
                    "value": 62,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,148,106)"
                        }
                    }
                },
                {
                    "name": "\u4e0b\u5348\u8336",
                    "value": 59,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,140,13)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u5316\u7ba1\u7406",
                    "value": 53,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,56,15)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956",
                    "value": 52,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,132,7)"
                        }
                    }
                },
                {
                    "name": "\u7ee9\u6548\u5956\u91d1",
                    "value": 51,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,136,115)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u725b",
                    "value": 47,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,5,24)"
                        }
                    }
                },
                {
                    "name": "\u80a1\u7968\u671f\u6743",
                    "value": 46,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,43,46)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5e02\u516c\u53f8",
                    "value": 45,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,71,83)"
                        }
                    }
                },
                {
                    "name": "\u9910\u8865",
                    "value": 43,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,8,47)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4\u597d",
                    "value": 41,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,73,160)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f",
                    "value": 40,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,18,59)"
                        }
                    }
                },
                {
                    "value": 39,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,12,62)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u671f\u4f53\u68c0",
                    "value": 39,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,55,83)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u7ba1\u7406",
                    "value": 38,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,98,47)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u597d",
                    "value": 37,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,13,135)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u4e91\u96c6",
                    "value": 36,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,40,35)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u597d",
                    "value": 36,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,69,109)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u597d",
                    "value": 31,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,128,89)"
                        }
                    }
                },
                {
                    "name": "\u9886\u5bfcnice",
                    "value": 28,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,79,78)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u5e26\u961f",
                    "value": 27,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,70,14)"
                        }
                    }
                },
                {
                    "name": "\u5065\u8eab\u745c\u4f3d",
                    "value": 24,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,127,82)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u56e2\u961f",
                    "value": 22,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,107,56)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u524d\u666f\u597d",
                    "value": 22,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,79,99)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u7a7a\u95f4\u5927",
                    "value": 21,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,55,99)"
                        }
                    }
                },
                {
                    "name": "\u725b\u4eba\u56e2\u961f",
                    "value": 21,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,16,65)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u5316",
                    "value": 21,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,22,117)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u901f\u53d1\u5c55",
                    "value": 20,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,49,49)"
                        }
                    }
                },
                {
                    "name": "\u671f\u6743\u6fc0\u52b1",
                    "value": 20,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,98,70)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u5de5\u4f5c\u5236",
                    "value": 18,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,75,86)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u5927",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,71,151)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,143,22)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u6c1b\u56f4\u597d",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,59,122)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u591a",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,99,4)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u4e09\u9910",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,39,121)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u73ed\u8f66",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,37,43)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u5956\u91d1",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,64,149)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f\u7a7a\u95f4\u5927",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,114,1)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6c1b\u56f4\u597d",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,17,120)"
                        }
                    }
                },
                {
                    "name": "\u671f\u6743",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,117,88)"
                        }
                    }
                },
                {
                    "name": "\u9886\u5bfc\u597d",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,17,14)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u5de5\u65f6",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,138,14)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u4f11\u5047",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,131,56)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u91d1",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,23,62)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u4e1a\u52a1",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,88,110)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5382",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,51,68)"
                        }
                    }
                },
                {
                    "name": "\u8282\u5047\u65e5\u798f\u5229",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,34,45)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u5feb",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,89,81)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u9ad8\u5165\u804c\u5feb",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,90,45)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u56e2\u961f",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,7,29)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5e95\u53cc\u85aa",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,141,25)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u90e8\u95e8",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,14,111)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5b9e\u529b\u5f3a",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,89,52)"
                        }
                    }
                },
                {
                    "name": "\u6781\u5ba2\u6587\u5316",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,64,107)"
                        }
                    }
                },
                {
                    "name": "\u7ee9\u6548\u5956",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,121,89)"
                        }
                    }
                },
                {
                    "name": "\u4e0d\u6253\u5361",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,134,137)"
                        }
                    }
                },
                {
                    "name": "16\u85aa",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,137,89)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u524d\u6cbf",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,113,88)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u5927",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,149,11)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u5efa",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,14,116)"
                        }
                    }
                },
                {
                    "name": "\u4e03\u9669\u4e00\u91d1",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,37,23)"
                        }
                    }
                },
                {
                    "name": "\u7cbe\u82f1\u56e2\u961f",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,149,136)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,88,119)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u80cc\u666f\u4f18\u79c0",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,31,90)"
                        }
                    }
                },
                {
                    "name": "\u7269\u8054\u7f51",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,115,5)"
                        }
                    }
                },
                {
                    "name": "\u5c97\u4f4d\u664b\u5347",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,124,10)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f\u7a7a\u95f4",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,112,27)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u597d",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,60,136)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u7ed9\u529b",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,1,77)"
                        }
                    }
                },
                {
                    "name": "\u80a1\u6743\u6fc0\u52b1",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,128,38)"
                        }
                    }
                },
                {
                    "name": "\u524d\u666f\u597d",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,69,60)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u85aa",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,114,64)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u7a7a\u95f4",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,37,23)"
                        }
                    }
                },
                {
                    "name": "\u98de\u901f\u53d1\u5c55",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,122,90)"
                        }
                    }
                },
                {
                    "name": "\u79df\u623f\u8865\u8d34",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,43,93)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7\u72ec\u89d2\u517d",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,139,160)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5ea6\u4f53\u68c0",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,23,33)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u539a\u5e74\u7ec8\u5956",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,122,160)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5347\u7a7a\u95f4\u5927",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,146,141)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u4f18\u79c0",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,88,98)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961fnice",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,96,18)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u4e30\u539a",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,42,70)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u79c0\u56e2\u961f",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,50,37)"
                        }
                    }
                },
                {
                    "name": "\u660e\u661f\u56e2\u961f",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,153,150)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u9645\u5316\u6c1b\u56f4",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,60,160)"
                        }
                    }
                },
                {
                    "name": "AI",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,93,132)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u725b\u591a",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,14,140)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,154,90)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5347\u7a7a\u95f4",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,42,83)"
                        }
                    }
                },
                {
                    "name": "\u529e\u516c\u73af\u5883\u597d",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,13,115)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f\u5feb",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,95,121)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u5feb",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,7,76)"
                        }
                    }
                },
                {
                    "name": "\u524d\u6cbf\u6280\u672f",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,133,14)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u9886\u5148",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,136,61)"
                        }
                    }
                },
                {
                    "name": "\u7a7a\u95f4\u5927",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,52,63)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u4e0a\u73ed",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,125,1)"
                        }
                    }
                },
                {
                    "name": "\u6709\u8f6c\u6b63\u673a\u4f1a",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,9,6)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u529e\u516c",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,110,137)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u7a7a\u95f4",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,80,126)"
                        }
                    }
                },
                {
                    "name": "\u8bd5\u7528\u671f\u5168\u85aa",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,25,106)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u4e0b\u5348\u8336",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,14,26)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u5927\u725b\u591a",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,44,70)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u6f5c\u529b\u5927",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,134,12)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u591a",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,17,159)"
                        }
                    }
                },
                {
                    "name": "\u804c\u4f4d\u664b\u5347",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,112,79)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u4fbf\u5229",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,3,5)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u9a71\u52a8",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,109,118)"
                        }
                    }
                },
                {
                    "name": "\u72ec\u89d2\u517d",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,29,114)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u6c1b\u56f4\u597d",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,156,119)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u91cf\u6570\u636e",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,149,1)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u5185\u6280\u672f\u9886",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,105,27)"
                        }
                    }
                },
                {
                    "name": "\u5927\u843d\u5730\u573a\u666f",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,51,63)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u989d\u5e74\u7ec8",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,99,148)"
                        }
                    }
                },
                {
                    "name": "\u5065\u5168\u664b\u5347\u673a\u5236",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,73,160)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u9f50\u5168",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,90,97)"
                        }
                    }
                },
                {
                    "name": "\u5168\u989d\u4e94\u9669\u4e00\u91d1",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,79,130)"
                        }
                    }
                },
                {
                    "name": "\u9886\u5bfcNICE",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,97,133)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u7a33\u5b9a",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,71,149)"
                        }
                    }
                },
                {
                    "name": "\u5065\u8eab\u623f",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,111,152)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u798f\u5229",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,112,52)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u53d1\u5c55\u597d",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,125,88)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u4eba\u9a7e\u9a76",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,109,32)"
                        }
                    }
                },
                {
                    "name": "\u8865\u5145\u5546\u4e1a\u4fdd\u9669",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,30,37)"
                        }
                    }
                },
                {
                    "name": "12\u5929\u5e74\u5047",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,86,0)"
                        }
                    }
                },
                {
                    "name": "\u9910\u8865\u7b49",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,156,64)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u72ec\u89d2\u517d",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,62,154)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u597d",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,15,112)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u597d",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,15,53)"
                        }
                    }
                },
                {
                    "name": "\u524d\u666f\u5e7f\u9614",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,12,116)"
                        }
                    }
                },
                {
                    "name": "\u5546\u4e1a\u822a\u5929\u884c\u4e1a\u524d\u666f\u826f\u597d",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,156,95)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u591a\u591a",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,107,54)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u5bfc\u5e08",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,110,11)"
                        }
                    }
                },
                {
                    "name": "\u51fa\u56fd\u65c5\u6e38",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,98,35)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1\u5168\u989d",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,29,17)"
                        }
                    }
                },
                {
                    "name": "\u826f\u597d\u53d1\u5c55\u8d8b\u52bf\u4e0e\u53d1\u5c55\u7a7a\u95f4",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,57,127)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5168",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,148,58)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5b8c\u5584",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,70,33)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u597d",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,142,149)"
                        }
                    }
                },
                {
                    "name": "\u4f4f\u623f\u8865\u8d34",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,27,38)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u4e0e\u5b66\u4e60\u6c1b\u56f4\u3002",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,125,64)"
                        }
                    }
                },
                {
                    "name": "\u5927\u516c\u53f8",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,109,98)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5927\u725b",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,144,139)"
                        }
                    }
                },
                {
                    "name": "\u5168\u989d\u793e\u4fdd\u516c\u79ef\u91d1",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,63,33)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u671f\u56e2\u5efa",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,110,124)"
                        }
                    }
                },
                {
                    "name": "\u91cd\u70b9\u9879\u76ee",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,102,103)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u5e7f\u9614",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,81,97)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u5de5\u4f5c\u65f6\u95f4",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,87,69)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u8865\u5145",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,36,60)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,81,49)"
                        }
                    }
                },
                {
                    "name": "\u725b\u4eba\u4e91\u96c6",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,92,50)"
                        }
                    }
                },
                {
                    "name": "\u5730\u94c1\u5468\u8fb9",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,38,43)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u5927\u725b",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,40,38)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u989d\u5956\u91d1",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,92,60)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u91d12-6\u4e2a\u6708",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,126,97)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u8fdc\u7a0b\u529e\u516c",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,79,29)"
                        }
                    }
                },
                {
                    "name": "\u6709\u517c\u804c\u5c97\u4f4d",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,42,116)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u6c14\u5341\u8db3",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,24,42)"
                        }
                    }
                },
                {
                    "name": "\u843d\u6237\u5feb",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,10,20)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4nice",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,131,85)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5ea6\u65c5\u6e38",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,75,0)"
                        }
                    }
                },
                {
                    "name": "\u7a7a\u95f4\u65e0\u9650",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,135,31)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u4e13\u4e1a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,80,126)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u4e0d\u9519",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,67,38)"
                        }
                    }
                },
                {
                    "name": "\u8865\u5145\u533b\u7597",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,140,48)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u9ad8",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,22,103)"
                        }
                    }
                },
                {
                    "name": "\u73ed\u8f66",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,38,6)"
                        }
                    }
                },
                {
                    "name": "\u660e\u661f\u4ea7\u54c1",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,74,94)"
                        }
                    }
                },
                {
                    "name": "8\u5929\u5e74\u5047",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,109,77)"
                        }
                    }
                },
                {
                    "name": "\u6253\u8f66\u62a5\u9500",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,122,134)"
                        }
                    }
                },
                {
                    "name": "\u4e0d\u52a0\u73ed",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,77,80)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u901f\u53d1\u5c55",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,47,92)"
                        }
                    }
                },
                {
                    "name": "\u5404\u79cd\u798f\u5229",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,49,93)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u624d\u623f\u7968",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,95,40)"
                        }
                    }
                },
                {
                    "name": "\u673a\u4f1a\u591a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,91,71)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u901f\u6210\u957f",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,86,157)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4\u8f7b\u677e",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,159,98)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5b9e\u529b",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,125,70)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u65e9\u9910",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,99,73)"
                        }
                    }
                },
                {
                    "name": "\u623f\u8865",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,77,7)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u5c97\u4f4d",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,107,143)"
                        }
                    }
                },
                {
                    "name": "\u7814\u53d1\u4e2d\u5fc3",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,144,28)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u7ebf\u5e7f",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,22,56)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6c1b\u56f4\u6d53\u539a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,69,99)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u65c5\u6e38",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,126,129)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u53d1\u5c55\u5f3a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,96,143)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u673a\u4f1a\u591a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,67,104)"
                        }
                    }
                },
                {
                    "name": "\u671d\u9633\u884c\u4e1a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,103,34)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u540d\u592e\u4f01",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,0,55)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u665a\u9910",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,18,40)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u65f6\u95f4",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,52,133)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u5b66\u4e60",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,142,94)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4\u4f73",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,43,80)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u80a1\u4e0a\u5e02",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,22,66)"
                        }
                    }
                },
                {
                    "name": "\u9910\u8d39\u8865\u8d34",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,57,7)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u4e0a\u4e0b\u73ed",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,133,87)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u6f5c\u529b",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,119,59)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c14\u6c1b\u597d",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,139,17)"
                        }
                    }
                },
                {
                    "name": "\u751f\u65e5\u4f1a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,0,115)"
                        }
                    }
                },
                {
                    "name": "AI\u673a\u5668\u4eba",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,48,106)"
                        }
                    }
                },
                {
                    "name": "\u996d\u8865",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,14,20)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7814\u56e2\u961f",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,47,59)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u5bb6\u5c45",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,1,75)"
                        }
                    }
                },
                {
                    "name": "\u8f66\u5382\u5408\u4f5c",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,13,67)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u8f6c\u6b63",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,130,26)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u6210\u957f",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,76,11)"
                        }
                    }
                },
                {
                    "name": "\u4e0d996",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,59,151)"
                        }
                    }
                },
                {
                    "name": "\u80a1\u4efd\u671f\u6743",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,77,94)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5e95\u5956\u91d1",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,31,70)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u53e3\u884c\u4e1a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,11,2)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4\u73af\u5883\u597d",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,66,72)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u6709\u524d\u666f",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,106,83)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u8fc7\u4ebf",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,14,64)"
                        }
                    }
                },
                {
                    "name": "\u671f\u6743\u80a1\u7968",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,34,113)"
                        }
                    }
                },
                {
                    "name": "\u6e05\u534e\u56e2\u961f",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,127,67)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u524d\u6cbf",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,55,160)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u4f18\u539a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,22,106)"
                        }
                    }
                },
                {
                    "name": "\u72ec\u89d2\u517d\u4f01\u4e1a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,67,86)"
                        }
                    }
                },
                {
                    "name": "\u516c\u5f00\u516c\u6b63",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,77,106)"
                        }
                    }
                },
                {
                    "name": "\u594b\u6597\u5956",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,123,30)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c\u798f\u5229\u597d",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,112,152)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u578b\u7814\u7a76\u9662",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,41,18)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u6587\u5316\u597d",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,47,30)"
                        }
                    }
                },
                {
                    "name": "\u521b\u4e1a\u56e2\u961f",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,24,107)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u8f7b\u56e2\u961f",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,55,92)"
                        }
                    }
                },
                {
                    "name": "\u671f\u6743\u5956\u52b1",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,61,119)"
                        }
                    }
                },
                {
                    "name": "\u671d\u4e5d\u665a\u516d",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,64,121)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u80fd\u529b\u5f3a\u3002",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,84,1)"
                        }
                    }
                },
                {
                    "name": "\u516d\u9669\u4e8c\u91d1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,44,97)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u5e74\u4f11\u5047",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,21,77)"
                        }
                    }
                },
                {
                    "name": "\u524d\u666f\u53ef\u89c2",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,106,131)"
                        }
                    }
                },
                {
                    "name": "\uff0858\uff09\u730e\u5934\u804c\u4f4d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,77,68)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,97,43)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u652f\u6301\u7ed9\u529b",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,48,113)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6c1b\u56f4\u6d53",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,19,34)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u5e76\u53d1\u7cfb\u7edf",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,75,77)"
                        }
                    }
                },
                {
                    "name": "\u591f\u6311\u6218\u591f\u523a\u6fc0",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,74,66)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5047",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,27,46)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,62,154)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,42,142)"
                        }
                    }
                },
                {
                    "name": "\u4f53\u68c0",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,133,114)"
                        }
                    }
                },
                {
                    "name": "\u6cd5\u5b9a\u8282\u5047\u65e5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,115,79)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1\u5168\u989d\u7f34\u7eb3",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,25,93)"
                        }
                    }
                },
                {
                    "name": "\u7cbe\u6e5b\u7684\u56e2\u961f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,11,1)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u884c\u4e1a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,119,146)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u4e1a\u52a1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,62,126)"
                        }
                    }
                },
                {
                    "name": "\u5343\u4e07\u7ea7\u7528\u6237",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,52,1)"
                        }
                    }
                },
                {
                    "name": "\u5165\u804c\u80a1\u7968",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,80,29)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u9ad8",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,13,106)"
                        }
                    }
                },
                {
                    "name": "\u5168\u52e4\u5956",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,89,124)"
                        }
                    }
                },
                {
                    "name": "\u5168\u989d\u516c\u79ef\u91d1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,68,45)"
                        }
                    }
                },
                {
                    "name": "\u7a33\u5b9a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,31,14)"
                        }
                    }
                },
                {
                    "name": "base",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,130,45)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u75c5\u5047",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,61,80)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u65b9\u4fbf",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,3,36)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c\u6fc0\u52b1\u8ba1\u5212",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,83,56)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u80fd\u529b\u5f3a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,41,133)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5bfc\u5411",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,40,43)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6709\u7231",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,103,1)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u901f\u6210\u957f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,135,159)"
                        }
                    }
                },
                {
                    "name": "\u9910\u996e\u8865\u8d34",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,148,58)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u7ebf\u798f\u5229",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,66,60)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,30,119)"
                        }
                    }
                },
                {
                    "name": "\u91cd\u70b9\u4e1a\u52a1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,82,21)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u68d2\u7684\u9886\u5bfc",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,134,20)"
                        }
                    }
                },
                {
                    "name": "\u4f9b\u5e94\u94fe",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,0,26)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4fdd\u516c\u79ef\u91d1\u5b9e\u4ea4",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,24,40)"
                        }
                    }
                },
                {
                    "name": "\u6280\u80fd\u57f9\u8bad",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,84,128)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u725b\u7684\u6280\u672f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,158,90)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u8fdb\u597d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,56,137)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u574718\u85aa",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,72,150)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u7a0b\u5e08\u6587\u5316",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,128,14)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u4e1a\u56e2\u961f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,57,4)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u96f6\u98df",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,129,14)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5348\u9910",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,108,45)"
                        }
                    }
                },
                {
                    "name": "**\u56e2\u961f+\u53d1\u5c55\u7a7a\u95f4\u5927",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,100,144)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u6709\u5927\u884c\u76f4\u9500\u94f6\u884c",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,67,109)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,58,38)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6280\u672f\u884c\u4e1a\u9886\u5148",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,19,9)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,45,120)"
                        }
                    }
                },
                {
                    "name": "\u7814\u53d1\u5f00\u653e\u73af\u5883",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,106,158)"
                        }
                    }
                },
                {
                    "name": "\u7b7e\u5b57\u73b0\u91d1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,74,119)"
                        }
                    }
                },
                {
                    "name": "15\u85aa",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,121,4)"
                        }
                    }
                },
                {
                    "name": "\u7ade\u4e89\u529b\u85aa\u916c",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,30,62)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4\u6d3b\u8dc3",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,106,134)"
                        }
                    }
                },
                {
                    "name": "\u8865\u5145\u5546\u4fdd",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,157,30)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u52b1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,59,111)"
                        }
                    }
                },
                {
                    "name": "\u8fc7\u8282\u8d39",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,79,46)"
                        }
                    }
                },
                {
                    "name": "\u51fa\u56fd\u57f9\u8bad",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,133,30)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u9645\u5316\u56e2\u961f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,84,46)"
                        }
                    }
                },
                {
                    "name": "\u52a0\u73ed\u5c11",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,158,85)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u65b0",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,52,133)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u7cbe\u6e5b",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,79,146)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u524d\u666f\u597d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,122,66)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u5bcc\u9879\u76ee\u7ecf\u9a8c",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,88,43)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u4f1a\u7a7a\u95f4\u5927",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,116,134)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e8c\u91d1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,46,138)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u9614\u53d1\u5c55\u7a7a\u95f4",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,156,103)"
                        }
                    }
                },
                {
                    "name": "\u72ec\u5f53\u4e00\u9762",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,153,50)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u524d\u666f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,46,149)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u4f01",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,120,52)"
                        }
                    }
                },
                {
                    "name": "\u4e16\u754c\u4e94\u767e\u5f3a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,20,77)"
                        }
                    }
                },
                {
                    "name": "\u4e0d\u5f3a\u5236\u52a0\u73ed",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,103,11)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5f52\u56e2\u961f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,72,115)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u5e73\u53f0",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,23,110)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c\u798f\u5229\u4f73",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,131,16)"
                        }
                    }
                },
                {
                    "name": "\u72ec\u89d2\u517d\u516c\u53f8",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,125,121)"
                        }
                    }
                },
                {
                    "name": "\u98df\u5802",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,119,53)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u68d2",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,142,59)"
                        }
                    }
                },
                {
                    "name": "\u521b\u65b0\u4e1a\u52a1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,128,66)"
                        }
                    }
                },
                {
                    "name": "\u5348\u9910\u8865\u52a9",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,29,80)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u9879\u76ee",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,68,43)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u9ad8",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,85,108)"
                        }
                    }
                },
                {
                    "name": "\u8001\u677fNice",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,0,140)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u6325\u6240\u957f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,46,147)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u989d\u9910\u8865",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,125,24)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u9ad8",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,123,136)"
                        }
                    }
                },
                {
                    "name": "\u5e02\u573a\u5316\u85aa\u916c",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,126,2)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u4f18\u539a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,52,25)"
                        }
                    }
                },
                {
                    "name": "\u611f\u77e5\u9636\u8dc3\u730e\u5934\u804c\u4f4d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,116,36)"
                        }
                    }
                },
                {
                    "name": "\u7ee9\u6548\u80a1\u7968",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,51,0)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c\u798f\u5229",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,99,110)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u4f18",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,84,18)"
                        }
                    }
                },
                {
                    "name": "\u6bcf\u5468\u56e2\u5efa",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,122,100)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u7a33\u5b9a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,123,146)"
                        }
                    }
                },
                {
                    "name": "\u8f6c\u6b63\u673a\u4f1a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,125,90)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u5185TOP3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,38,2)"
                        }
                    }
                },
                {
                    "name": "\u7ba1\u7406\u89c4\u8303",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,74,64)"
                        }
                    }
                },
                {
                    "name": "\u65e9\u9910\u52a0\u73ed\u9910",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,102,158)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u5956\u91d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,149,1)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u9910",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,139,45)"
                        }
                    }
                },
                {
                    "name": "\u6e05\u534e\u5927\u5b66\u7684\u667a\u80fd\u8fd0\u7ef4\u5b9e\u9a8c\u5ba4",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,33,29)"
                        }
                    }
                },
                {
                    "name": "\u901a\u8baf\u8865\u8d34",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,26,15)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u7a33\u5b9a+\u6210\u957f\u664b\u5347+\u6280\u672f\u9a71\u52a8+\u80a1\u7968\u6fc0\u52b1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,100,160)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u725b\u56e2\u961f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,135,67)"
                        }
                    }
                },
                {
                    "name": "\u4e24\u9910\u8865\u8d34",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,62,69)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7531",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,119,115)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6280\u672f\u6c1b\u56f4\u597d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,140,31)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u7a7a\u95f4\u597d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,52,115)"
                        }
                    }
                },
                {
                    "name": "\u6301\u724c\u673a\u6784",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,107,48)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4\u4f73",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,133,76)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u5185\u77e5\u540d\u4e0a\u5e02\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,76,102)"
                        }
                    }
                },
                {
                    "name": "\u521b\u65b0\u4e1a\u52a1\u573a\u666f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,9,43)"
                        }
                    }
                },
                {
                    "name": "\u521b\u4e1a\u6fc0\u60c5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,120,1)"
                        }
                    }
                },
                {
                    "name": "\u5b63\u5ea6\u5168\u85aa\u75c5\u5047",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,134,86)"
                        }
                    }
                },
                {
                    "name": "\u6709\u671f\u6743",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,150,6)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,144,123)"
                        }
                    }
                },
                {
                    "name": "\u5177\u6709\u7ade\u4e89\u529b\u7684\u85aa\u8d44\u6c34\u5e73",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,82,63)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u5bcc\u4e0b\u5348\u8336",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,13,86)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u524d\u666f\u597d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,157,24)"
                        }
                    }
                },
                {
                    "name": "\u672a\u6765\u8d8b\u52bf",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,87,43)"
                        }
                    }
                },
                {
                    "name": "\u6d25\u8d34\u8865\u52a9",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,147,148)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u798f\u5229",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,156,41)"
                        }
                    }
                },
                {
                    "name": "\u5065\u8eab\u798f\u5229",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,119,56)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u4f4f\u5bbf",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,75,82)"
                        }
                    }
                },
                {
                    "name": "\u66f9\u64cd\u51fa\u884c",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,157,141)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u5168\u9762",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,56,131)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u524d\u77bb\u6280\u672f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,101,90)"
                        }
                    }
                },
                {
                    "name": "\u96c6\u56e2\u80cc\u666f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,61,85)"
                        }
                    }
                },
                {
                    "name": "\u8282\u5047\u65e5\u798f\u5229\u7b49",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,34,21)"
                        }
                    }
                },
                {
                    "name": "\u524d\u6cbf\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,51,151)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u751f\u65e5\u798f\u5229",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,38,97)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u5927\u4e0a\u73af\u5883",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,128,18)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u641c\u7d22\u7b97\u6cd5\u6838\u5fc3\u56e2\u961f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,130,125)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6210\u957f\u671f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,82,29)"
                        }
                    }
                },
                {
                    "name": "AI\u82af\u7247",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,60,34)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u5916\u5408\u8d44",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,109,70)"
                        }
                    }
                },
                {
                    "name": "\u8f7b\u677e\u6d3b\u8dc3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,52,18)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u7ade\u4e89\u529b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,111,109)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4nice",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,112,9)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u8865\u8d34",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,45,110)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4\u878d\u6d3d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,77,105)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u4e0a\u5e02\u9884\u671f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,73,86)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u65e0\u9650",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,59,91)"
                        }
                    }
                },
                {
                    "name": "\u5065\u5eb7\u4f53\u68c0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,146,21)"
                        }
                    }
                },
                {
                    "name": "\u5468\u672b\u52a0\u73ed\u53cc\u500d\u5de5\u8d44",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,44,79)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u665a\u9910",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,1,43)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79\u5b66",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,18,36)"
                        }
                    }
                },
                {
                    "name": "\u963f\u91cc\u5e73\u53f0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,138,56)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u5973\u591a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,160,55)"
                        }
                    }
                },
                {
                    "name": "\u529e\u516c\u73af\u5883\u4f18\u8d8a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,89,55)"
                        }
                    }
                },
                {
                    "name": "\u524d\u666f\u5e7f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,24,56)"
                        }
                    }
                },
                {
                    "name": "AI\u97f3\u4e50",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,81,99)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5ea6\u664b\u5347",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,58,89)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u9879\u76ee",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,42,52)"
                        }
                    }
                },
                {
                    "name": "\u9760\u8c31\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,55,85)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u5e7f\u9614",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,39,113)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u85aa\u8d44",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,64,156)"
                        }
                    }
                },
                {
                    "name": "\u6587\u5316\u81ea\u7531",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,64,103)"
                        }
                    }
                },
                {
                    "name": "14\u85aa",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,56,86)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5f3a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,92,136)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5348\u665a\u9910",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,0,140)"
                        }
                    }
                },
                {
                    "name": "\u989c\u503c\u9ad8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,49,57)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u5236\u5ea6\u5b8c\u5584",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,152,154)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u7a7a\u95f4\u5927\u3002",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,98,114)"
                        }
                    }
                },
                {
                    "name": "\u793e\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,102,75)"
                        }
                    }
                },
                {
                    "name": "\u73ed\u8f66\u63a5\u9001",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,34,64)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u7a7a\u95f4\u5927",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,95,139)"
                        }
                    }
                },
                {
                    "name": "\u9e45\u5382\u798f\u5229/\u5065\u8eab\u623f/\u73ed\u8f66/\u5468\u672b\u53cc\u4f11",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,117,28)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5e95\u591a\u85aa",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,113,20)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u98df\u5802",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,122,108)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u591a\u5927\u725b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,90,101)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u98df\u996e\u6599",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,15,26)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u53e3\u6d6a\u5c16",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,129,67)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u65c5\u6e38",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,89,36)"
                        }
                    }
                },
                {
                    "name": "\u8865\u5145\u516c\u79ef\u91d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,125,37)"
                        }
                    }
                },
                {
                    "name": "\u521b\u65b0\u9879\u76ee",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,89,138)"
                        }
                    }
                },
                {
                    "name": "3D\u89c6\u89c9\u6210\u50cf",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,2,27)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u6709\u7ade\u4e89\u529b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,45,57)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u4e0a\u5e02\u671f\u6743\u591a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,0,98)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u878d\u6d3d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,72,41)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f\u5feb\u901f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,152,107)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u6027\u5316\u7ba1\u7406",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,109,127)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,94,60)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u5956",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,146,44)"
                        }
                    }
                },
                {
                    "name": "\u73af\u5883\u597d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,38,78)"
                        }
                    }
                },
                {
                    "name": "14-20\u85aa",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,15,155)"
                        }
                    }
                },
                {
                    "name": "\u7814\u53d1\u521b\u65b0\u5956",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,33,11)"
                        }
                    }
                },
                {
                    "name": "\u5317\u5927\u540d\u6821\u540c\u4e8b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,26,14)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u91cf\u5927",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,122,13)"
                        }
                    }
                },
                {
                    "name": "\u94f6\u884c\u80cc\u666f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,43,73)"
                        }
                    }
                },
                {
                    "name": "IOT\u9886\u5148\u4f01\u4e1a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,74,127)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u6e38\u57fa\u91d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,36,55)"
                        }
                    }
                },
                {
                    "name": "AI\u91d1\u878d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,151,52)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u6c11APP",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,52,59)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u4e09\u9910",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,63,67)"
                        }
                    }
                },
                {
                    "name": "\u505a\u4e94\u4f11\u4e8c",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,33,148)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u65b0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,105,13)"
                        }
                    }
                },
                {
                    "name": "\u5168\u7403\u5316",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,138,85)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u6548\u56e2\u961f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,96,118)"
                        }
                    }
                },
                {
                    "name": "\u817e\u8baf\u4e91",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,99,116)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5065\u8eab\u623f\u7406\u53d1\u5e97",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,72,135)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f/\u85aa\u8d44\u798f\u5229",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,1,43)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u7ebf\u98ce\u6295",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,67,93)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u5e76\u53d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,94,13)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u589e\u957f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,18,154)"
                        }
                    }
                },
                {
                    "name": "\u516d\u65e5\u53cc\u4f11",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,17,58)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5496\u5e26\u961f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,53,132)"
                        }
                    }
                },
                {
                    "name": "\u5730\u94c1\u4e0a\u76d6",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,84,45)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u8fc5\u901f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,77,40)"
                        }
                    }
                },
                {
                    "name": "\u6ef4\u6ef4\u6253\u8f66",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,50,138)"
                        }
                    }
                },
                {
                    "name": "\u54e5\u5927",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,134,55)"
                        }
                    }
                },
                {
                    "name": "\u51fa\u56fd\u6e38",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,12,19)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u5185\u9886\u5148\u91d1\u878d\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,65,53)"
                        }
                    }
                },
                {
                    "name": "\u9910\u8865\u4ea4\u8865",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,64,38)"
                        }
                    }
                },
                {
                    "name": "\u73af\u5883\u8212\u9002",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,134,23)"
                        }
                    }
                },
                {
                    "name": "\u8bdd\u8865",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,46,28)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5e74\u8f7b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,43,154)"
                        }
                    }
                },
                {
                    "name": "\u591a\u6b21\u8c03\u85aa",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,78,2)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u8f7b\u5316",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,107,55)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u5bbf\u820d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,89,16)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u5e73\u53f0\u5927",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,24,70)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u6280\u672f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,142,88)"
                        }
                    }
                },
                {
                    "name": "\u5546\u4e1a\u4fdd\u9669",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,93,151)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u5f85\u9047\u4f18\u8d8a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,127,116)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u524d\u666f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,90,144)"
                        }
                    }
                },
                {
                    "name": "\u6e05\u534e\u6d59\u5927",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,65,119)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u4e30\u539a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,145,3)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u4e2d\u53f0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,14,1)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u900f\u660e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,153,60)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u5f85\u9047\u597d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,3,139)"
                        }
                    }
                },
                {
                    "name": "\u826f\u597d\u7684\u6280\u672f\u6c1b\u56f4",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,48,97)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u53d1\u5c55\u5feb",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,66,83)"
                        }
                    }
                },
                {
                    "name": "13\u85aa",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,17,12)"
                        }
                    }
                },
                {
                    "name": "\u8fd1\u5730\u94c1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,61,150)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5206\u7ea2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,83,116)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u673a\u4f1a\u591a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,16,4)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u4f73",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,93,61)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u91d1+\u5b63\u5ea6\u5956\u91d1+\u597d\u5fc3\u60c5+\u798f\u5229\u591a\u591a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,135,17)"
                        }
                    }
                },
                {
                    "name": "\u8d8b\u52bf\u8d5b\u9053",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,36,87)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u5f8b\u5185\u9a71",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,98,94)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u5e73\u53f0\u53d1\u5c55\u5feb",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,84,34)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5ea6\u52a0\u85aa",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,134,31)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u9645\u5316",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,52,70)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u8865",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,46,116)"
                        }
                    }
                },
                {
                    "name": "\u5404\u9879\u8865\u8d34",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,159,59)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44OPEN",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,16,126)"
                        }
                    }
                },
                {
                    "name": "\u5f3a\u52b2\u535a\u58eb\u56e2\u961f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,20,18)"
                        }
                    }
                },
                {
                    "name": "\u3010\u5929\u773c\u67e5\u3011\u730e\u5934\u804c\u4f4d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,9,51)"
                        }
                    }
                },
                {
                    "name": "\u6e05\u534e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,118,134)"
                        }
                    }
                },
                {
                    "name": "\u516c\u5e73\u516c\u6b63",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,0,95)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u843d\u5730",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,17,145)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u9886\u5148",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,125,45)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5496\u4e91\u96c6",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,101,59)"
                        }
                    }
                },
                {
                    "name": "D\u8f6e\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,20,106)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u901a\u9053",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,66,70)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u5021\u8ffd\u6c42\u5353\u8d8a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,133,97)"
                        }
                    }
                },
                {
                    "name": "\u6781\u5177\u7ade\u4e89\u529b\u7684\u85aa\u8d44\u5f85\u9047",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,111,47)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u5e73\u53f0\u5927",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,26,24)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u7814\u7a76",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,109,64)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5b9e\u529b\u96c4\u539a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,145,72)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c\u5f85\u9047\u4f18",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,153,137)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u6280\u672f\u9886\u5148",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,9,126)"
                        }
                    }
                },
                {
                    "name": "\u65af\u5766\u798f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,10,103)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u901a\u9053\u5b8c\u5584",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,63,145)"
                        }
                    }
                },
                {
                    "name": "\u4e16\u754c500\u5f3a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,4,56)"
                        }
                    }
                },
                {
                    "name": "2D",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,119,24)"
                        }
                    }
                },
                {
                    "name": "\u5305\u4e09\u9910",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,115,11)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u822c16\u85aa\u4ee5\u4e0a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,55,87)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u957f\u5e74\u5047",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,68,108)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u591a\u591a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,140,49)"
                        }
                    }
                },
                {
                    "name": "2-6\u4e2a\u6708\u5e74\u7ec8\u5956",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,16,95)"
                        }
                    }
                },
                {
                    "name": "offer14\u85aa",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,128,25)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5065\u8eab/\u96f6\u98df",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,51,148)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u540d\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,113,157)"
                        }
                    }
                },
                {
                    "name": "\u516d\u9669\u4e00\u91d1\u5168\u989d\u7f34\u7eb3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,55,120)"
                        }
                    }
                },
                {
                    "name": "base*13+0-6\u4e2a\u6708\u5e74\u7ec8\u5956\u91d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,58,127)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u597d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,130,131)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u7a33\u5b9a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,116,128)"
                        }
                    }
                },
                {
                    "name": "\u9910\u8865\u8bdd\u8865",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,129,15)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5065\u8eab\u623f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,65,106)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6311\u6218",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,84,108)"
                        }
                    }
                },
                {
                    "name": "\u6311\u6218\u5927",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,147,138)"
                        }
                    }
                },
                {
                    "name": "\u672a\u6765\u53ef\u671f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,14,47)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u7ea2\u4e66",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,67,26)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u9f99\u5934",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,114,27)"
                        }
                    }
                },
                {
                    "name": "\u5404\u79cd\u8865\u8d34",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,139,81)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u9645\u5316\u5e73\u53f0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,118,101)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5927\u725b\u4f17\u591a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,57,87)"
                        }
                    }
                },
                {
                    "name": "6\u96692\u91d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,49,123)"
                        }
                    }
                },
                {
                    "name": "P7+\u53ef\u4eab\u53d7\u963f\u91cc\u80a1\u7968",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,98,131)"
                        }
                    }
                },
                {
                    "name": "\u5c11\u52a0\u73ed",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,93,26)"
                        }
                    }
                },
                {
                    "name": "\u5173\u6ce8\u5458\u5de5\u53d1\u5c55",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,146,1)"
                        }
                    }
                },
                {
                    "name": "\u7b80\u5355\u771f\u8bda",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,73,153)"
                        }
                    }
                },
                {
                    "name": "\u6625\u8282\u5047\u671f\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,150,103)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6210\u5458\u6765\u81eaBATJ\u7b49\u4e00\u7ebf\u5927\u5382",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,16,73)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1\u3002\u5e26\u85aa\u5e74\u5047\u3002\u798f\u5229\u597d\u5f85\u9047\u4f73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,6,19)"
                        }
                    }
                },
                {
                    "name": "\u9876\u914dMac\u7b49",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,112,36)"
                        }
                    }
                },
                {
                    "name": "\u573a\u666f\u4e30\u5bcc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,35,74)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u9760\u8c31",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,67,71)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u4e2a\u5c97\u4f4d\u6210\u5c31\u4e00\u756a\u4e8b\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,24,58)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f\u6c1b\u56f4\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,9,71)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u91cf\u6d41\u91cf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,38,72)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5f52\u79d1\u7814\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,59,126)"
                        }
                    }
                },
                {
                    "name": "\u6709\u671f\u6743\u6388\u4e88",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,143,47)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u5e7416\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,12,49)"
                        }
                    }
                },
                {
                    "name": "\u7cbe\u82f1\u6587\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,58,10)"
                        }
                    }
                },
                {
                    "name": "\u5e05\u54e5\u7f8e\u5973",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,50,45)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u63d0\u5347",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,61,153)"
                        }
                    }
                },
                {
                    "name": "\u536b\u74f4\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,48,22)"
                        }
                    }
                },
                {
                    "name": "\u505a\u6700\u524d\u6cbf\u7684\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,9,64)"
                        }
                    }
                },
                {
                    "name": "\u540d\u6821\u5927\u5382",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,124,91)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6280\u672f\u7cbe\u6e5b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,51,90)"
                        }
                    }
                },
                {
                    "name": "\u521b\u4e1aAI\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,155,119)"
                        }
                    }
                },
                {
                    "name": "\u975e\u5e38\u4eba\u6027\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,81,131)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u8d1f\u8d23\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,145,160)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5c0f\u800c\u7cbe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,118,151)"
                        }
                    }
                },
                {
                    "name": "\u516d\u9669\u4e00\u91d1\u5e26\u85aa\u4e8b\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,59,7)"
                        }
                    }
                },
                {
                    "name": "\u91cd\u70b9\u53d1\u5c55\u7684\u53d8\u73b0\u9879\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,12,40)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,17,86)"
                        }
                    }
                },
                {
                    "name": "\u5185\u90e8\u5b75\u5316\u9879\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,109,154)"
                        }
                    }
                },
                {
                    "name": "\u671f\u6743\u80a1\u6743",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,5,160)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,59,36)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,127,150)"
                        }
                    }
                },
                {
                    "name": "AI\u533b\u7597\u9886\u57df\u72ec\u89d2\u517d\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,15,117)"
                        }
                    }
                },
                {
                    "name": "NLP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,158,88)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u56fe\u50cf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,77,151)"
                        }
                    }
                },
                {
                    "name": "\u8bd5\u7528\u671f\u4ea4\u4e94\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,154,115)"
                        }
                    }
                },
                {
                    "name": "\u6709\u5348\u4f11",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,18,48)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u8f7b\u56e2\u961f\u5e26\u85aa\u5e74\u5047\u505a\u4e94\u4f11\u4e8c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,21,113)"
                        }
                    }
                },
                {
                    "name": "\u6ca1\u6709KPI",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,51,135)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u6c1b\u56f4\u6d3b\u8dc3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,32,107)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1\u8282\u65e5\u798f\u5229\u5e74\u5ea6\u4f53\u68c0\u52a0\u73ed\u8865\u52a9\u5e26\u85aa\u5e74\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,50,117)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u56e2\u961f\u4f18\u79c0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,97,119)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51\u51fa\u6d77\u4f01\u4e1a\u6807\u6746",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,54,88)"
                        }
                    }
                },
                {
                    "name": "\u5168\u7403\u5316\u89c6\u91ce",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,106,56)"
                        }
                    }
                },
                {
                    "name": "\u7ec6\u5206\u9886\u57df\u884c\u4e1a**",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,148,46)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u53d1\u5c55\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,7,94)"
                        }
                    }
                },
                {
                    "name": "\u6bcf\u5e74\u6da8\u5de5\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,33,18)"
                        }
                    }
                },
                {
                    "name": "\u57f9\u8bad\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,87,145)"
                        }
                    }
                },
                {
                    "name": "\u8282\u65e5\u798f\u5229\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,113,95)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,44,152)"
                        }
                    }
                },
                {
                    "name": "\u6253\u9020\u4e16\u754c**\u7684\u6df7\u6c8c\u5de5\u7a0b\u4e50\u56ed",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,110,27)"
                        }
                    }
                },
                {
                    "name": "\u5c97\u4f4d\u5408\u540c\u4e0e\u5317\u4eac\u4eac\u4e1c\u4e16\u7eaa\u6709\u9650\u516c\u53f8\u7b7e\u8ba2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,132,136)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,160,98)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u4e1a\u57f9\u8bad",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,93,135)"
                        }
                    }
                },
                {
                    "name": "\u6d59\u5927\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,86,98)"
                        }
                    }
                },
                {
                    "name": "\u73af\u5883\u5bbd\u677e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,83,109)"
                        }
                    }
                },
                {
                    "name": "CBA\u660e\u661f\u521b\u4e1a\u9879\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,39,0)"
                        }
                    }
                },
                {
                    "name": "\u80a1\u6743\u8ba1\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,7,4)"
                        }
                    }
                },
                {
                    "name": ".",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,18,47)"
                        }
                    }
                },
                {
                    "name": "\u805a\u96c6\u9ad8\u6d45\u4eba\u624d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,160,47)"
                        }
                    }
                },
                {
                    "name": "\u798f\u7530CBD",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,109,114)"
                        }
                    }
                },
                {
                    "name": "\uff08\u77f3\u5934\u79d1\u6280\uff09\u730e\u5934\u804c\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,22,1)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u8fd8\u4e0d\u9519",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,89,8)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u80cc\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,90,159)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5e95\u635e\u534a\u4ef7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,135,62)"
                        }
                    }
                },
                {
                    "name": "\u5916\u4f01\u98ce\u683c\u7b49",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,90,61)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u98df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,142,87)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u6e38\u56e2\u5efa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,32,33)"
                        }
                    }
                },
                {
                    "name": "\u4fdd\u5e9513\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,148,19)"
                        }
                    }
                },
                {
                    "name": "\u804c\u4e1a\u5927\u725b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,141,114)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u529e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,80,68)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u79c0\u5019\u9009\u4eba\u53ef\u4ee5\u6210\u4e3a\u6280\u672f\u5408\u4f19\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,77,143)"
                        }
                    }
                },
                {
                    "name": "\u6e05\u534e\u59da\u73edleader\u5e26\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,105,77)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u53d1\u5c55\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,113,85)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4\u68d2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,102,159)"
                        }
                    }
                },
                {
                    "name": "\u6574\u4f53\u89e3\u51b3\u65b9\u6848\u80fd\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,83,153)"
                        }
                    }
                },
                {
                    "name": "LayaAir\u5f15\u64ce\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,138,37)"
                        }
                    }
                },
                {
                    "name": "\u963f\u91cc+\u4e2d\u5175\u5408\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,41,144)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4\u5411\u4e0a\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,15,124)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5382\u6838\u5fc3\u90e8\u95e8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,34,80)"
                        }
                    }
                },
                {
                    "name": "Top\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,6,41)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u96f6\u552e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,148,85)"
                        }
                    }
                },
                {
                    "name": "\u4f4f\u623f\u514d\u606f\u8d37",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,54,5)"
                        }
                    }
                },
                {
                    "name": "\u90e8\u95e8\u8bc4\u4f18\u5956",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,154,159)"
                        }
                    }
                },
                {
                    "name": "\u4f60\u7684\u4ee3\u7801\u5c06\u5f71\u54cd\u6570\u4ebf\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,94,113)"
                        }
                    }
                },
                {
                    "name": "AI+\u6559\u80b2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,4,36)"
                        }
                    }
                },
                {
                    "name": "\u6d41\u91cf\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,37,140)"
                        }
                    }
                },
                {
                    "name": "AI\u72ec\u89d2\u517d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,83,33)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,89,72)"
                        }
                    }
                },
                {
                    "name": "\u80fd\u529b\u7a81\u51fa\u8005\u664b\u5347\u5feb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,112,54)"
                        }
                    }
                },
                {
                    "name": "\u5927\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,55,92)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u98df\u5bbf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,104,11)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u7a33\u5b9a\u5feb\u901f\u589e\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,139,33)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,115,152)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u53d1\u5c55\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,115,130)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,159,79)"
                        }
                    }
                },
                {
                    "name": "\u6d41\u7a0b\u5feb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,62,8)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u5b9e\u529b\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,145,91)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5b9e\u529b\uff1a\u957f\u671f\u6280\u672f\u79ef\u6dc0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,112,28)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u53d1\u5c55\u7a7a\u95f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,85,24)"
                        }
                    }
                },
                {
                    "name": "\u5b9e\u529b\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,127,15)"
                        }
                    }
                },
                {
                    "name": "\u7eaf\u6280\u672f\u80cc\u4e66\u7684\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,151,30)"
                        }
                    }
                },
                {
                    "name": "\u767e\u4e07DAU",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,75,159)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u4e0a\u4e0b\u73ed\u53cc\u4f11",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,24,9)"
                        }
                    }
                },
                {
                    "name": "2012\u5b9e\u9a8c\u5ba4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,40,113)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u4f53\u68c0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,35,31)"
                        }
                    }
                },
                {
                    "name": "\u4e8b\u4e1a\u5355\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,61,117)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u9ad8P",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,7,24)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u4e13\u5bb6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,131,130)"
                        }
                    }
                },
                {
                    "name": "\u878d\u8d44\u8fc7\u4ebf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,133,66)"
                        }
                    }
                },
                {
                    "name": "\u725b\u4eba\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,101,57)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5f71\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,26,138)"
                        }
                    }
                },
                {
                    "name": "\u7ed3\u679c\u5bfc\u5411",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,86,147)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u9910\u514d\u8d39",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,81,126)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u65b0\u6280\u672f\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,127,81)"
                        }
                    }
                },
                {
                    "name": "\u817e\u8baf\u6295\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,10,55)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,95,119)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u5efa\u65c5\u6e38\u7b49",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,39,107)"
                        }
                    }
                },
                {
                    "name": "\u76c8\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,49,71)"
                        }
                    }
                },
                {
                    "name": "\u5145\u6ee1\u6d3b\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,10,70)"
                        }
                    }
                },
                {
                    "name": "\u592e\u4f01\u63a7\u80a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,39,127)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u4f11\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,91,148)"
                        }
                    }
                },
                {
                    "name": "\u5177\u6709\u5e02\u573a\u7ade\u4e89\u529b\u7684\u85aa\u916c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,77,9)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5347\u5e73\u53f0\u6253\u901a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,31,124)"
                        }
                    }
                },
                {
                    "name": "\u4f30\u503c\u8fd1\u767e\u4ebf\u7f8e\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,87,149)"
                        }
                    }
                },
                {
                    "name": "0-1\u65b0\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,21,78)"
                        }
                    }
                },
                {
                    "name": "bat\u5927\u725b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,77,28)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5927\u725b\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,142,14)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u53d1\u5c55\u7a7a\u95f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,17,126)"
                        }
                    }
                },
                {
                    "name": "\u5341\u4e94\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,143,84)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u65b0\u6210\u7acb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,159,115)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u5f85\u9047\u5f88\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,38,31)"
                        }
                    }
                },
                {
                    "name": "\u5165\u804c\u57f9\u8bad",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,13,110)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u56e2\u961f\u5747\u4e3a\u81ea\u52a8\u9a7e\u9a76",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,145,43)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5347\u7a7a\u95f4\u5de8\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,7,72)"
                        }
                    }
                },
                {
                    "name": "\u529f\u8bfe\u6280\u672f\u524d\u6cbf\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,50,105)"
                        }
                    }
                },
                {
                    "name": "\u7814\u53d1\u4eba\u5458300\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,92,129)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u957f\u5e26\u85aa\u5e74\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,24,158)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u4f18\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,20,120)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u62ff\u9f50\u805a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,70,143)"
                        }
                    }
                },
                {
                    "name": "\u5168\u6808\u6280\u672f\u5927\u725b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,132,89)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6210\u5458\u6765\u81ea\u56fd\u5185\u5916\u540d\u6821",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,15,99)"
                        }
                    }
                },
                {
                    "name": "\u5e02\u573a\u8d44\u6e90\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,29,117)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u4f17\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,110,150)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u7814\u53d1\u5b9e\u529b\u96c4\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,11,103)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5047\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,75,5)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u7ea2\u5305",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,137,82)"
                        }
                    }
                },
                {
                    "name": "\u505a\u4e8b\u81ea\u7531\u5ea6\u8db3\u591f\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,47,23)"
                        }
                    }
                },
                {
                    "name": "\u522b\u518d\u9519\u8fc7Lazada",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,36,49)"
                        }
                    }
                },
                {
                    "name": "\u5f3a\u5927\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,156,98)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u8d5b\u9053",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,64,25)"
                        }
                    }
                },
                {
                    "name": "\u5927\u516c\u53f8\u5e73\u53f0\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,41,14)"
                        }
                    }
                },
                {
                    "name": "NICE\u7684\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,14,20)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u89c4\u6a21\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,128,12)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u53d1\u5c55\u524d\u666f\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,116,89)"
                        }
                    }
                },
                {
                    "name": "\u8282\u65e5\u793c\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,114,93)"
                        }
                    }
                },
                {
                    "name": "\u8f85\u52a9\u9a7e\u9a76",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,84,70)"
                        }
                    }
                },
                {
                    "name": "\u62e5\u6709TB\u7ea7\u6570\u636e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,49,34)"
                        }
                    }
                },
                {
                    "name": "3\u4f4d\u535a\u58eb\u751f\u5bfc\u5e08\u6302\u5e05\u7684\u79d1\u5b66\u5bb6\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,129,146)"
                        }
                    }
                },
                {
                    "name": "Geek\u6587\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,18,97)"
                        }
                    }
                },
                {
                    "name": "\u516d\u9669\u4e00\u91d1+\u5b63\u5ea6\u7ee9\u6548\u5956\u91d1/\u5e74\u7ec8\u5956",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,54,40)"
                        }
                    }
                },
                {
                    "name": "A\u8f6e\u878d\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,124,74)"
                        }
                    }
                },
                {
                    "name": "\u8fdc\u7a0b\u529e\u516c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,97,47)"
                        }
                    }
                },
                {
                    "name": "\u9519\u8fc7\u4e8610\u5e74\u7684\u624b\u6dd8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,48,51)"
                        }
                    }
                },
                {
                    "name": "\u5916\u5305",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,13,151)"
                        }
                    }
                },
                {
                    "name": "\u610f\u5916\u8865\u52a9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,43,134)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u5316\u7ba1\u7406\u5de5\u4f5c\u6c1b\u56f4\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,156,149)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u5496\u4e91\u96c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,66,111)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u81ea\u52a9\u5348\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,123,49)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u7ed9\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,142,160)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44open",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,103,53)"
                        }
                    }
                },
                {
                    "name": "\u90e8\u95e8\u4f18\u80dc\u5956",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,136,22)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u901f\u53d1\u5c55\u4e2d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,154,74)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u665a\u9910&\u5348\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,4,123)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5e02\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,38,71)"
                        }
                    }
                },
                {
                    "name": "B2B\u91d1\u878d\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,75,4)"
                        }
                    }
                },
                {
                    "name": "\u5b5d\u987a\u57fa\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,131,131)"
                        }
                    }
                },
                {
                    "name": "\u5b63\u5ea6\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,62,70)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u53d1\u5c55\u524d\u666f\u5e7f\u9614",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,9,125)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5165\u63a5\u89e6\u4e1a\u754c\u6700\u524d\u6cbf\u4eba\u5de5\u667a\u80fd\u6838\u5fc3\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,25,20)"
                        }
                    }
                },
                {
                    "name": "\u4e0d\u8bbe\u9650",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,80,39)"
                        }
                    }
                },
                {
                    "name": "\u826f\u597d\u7684\u884c\u4e1a\u524d\u666f\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,69,119)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546\u573a\u666f\u5546\u54c1\u63a8\u8350\u7b49",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,136,23)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u5fc3\u7814\u7a76\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,100,14)"
                        }
                    }
                },
                {
                    "name": "\u591a\u6837\u5316\u7684\u5b66\u4e60\u73af\u5883",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,120,153)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u98df\u65e0\u9650\u91cf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,56,39)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u5de8\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,130,37)"
                        }
                    }
                },
                {
                    "name": "\u6709\u5229\u4e8e\u53d1\u8bba\u6587",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,121,55)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u98ce\u53e3\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,9,67)"
                        }
                    }
                },
                {
                    "name": "\u7ee9\u6548\u85aa\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,119,139)"
                        }
                    }
                },
                {
                    "name": "\u8fd1\u4e07\u4eba\u89c4\u6a21",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,140,73)"
                        }
                    }
                },
                {
                    "name": "\u5c31\u6765\u641c\u72d7\u5546\u4e1a\u641c\u7d22\u5427\uff01",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,80,46)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u63a8\u8350\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,99,20)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u524d\u666f\u5e7f\u9614",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,44,121)"
                        }
                    }
                },
                {
                    "name": "\u6fc0\u52b1\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,10,67)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u6ce8\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,11,10)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u805a\u96c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,80,127)"
                        }
                    }
                },
                {
                    "name": "\u65e9\u4e5d\u665a\u516d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,82,107)"
                        }
                    }
                },
                {
                    "name": "\u8be5\u804c\u4f4d\u76f4\u63a5\u4e0e\u7528\u4eba\u5355\u4f4d\u7b7e\u8ba2\u52b3\u52a8\u5408\u540c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,155,10)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u4ea7\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,67,97)"
                        }
                    }
                },
                {
                    "name": "\u9f13\u52b1\u7814\u7a76\u65b0\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,124,151)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,88,70)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4up",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,47,85)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u8425\u98df\u5802",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,19,143)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u4e1a\u52a1\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,33,57)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u5927\u6570\u636e\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,134,22)"
                        }
                    }
                },
                {
                    "name": "\u597d\u73a9\u7684\u6e38\u620f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,154,141)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u914d\u7f6e\u671f\u6743",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,142,93)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u73ed\u5f00\u5fc3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,131,22)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u4e1a\u8def",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,10,95)"
                        }
                    }
                },
                {
                    "name": "\u5927\u4f6c\u5e26\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,33,116)"
                        }
                    }
                },
                {
                    "name": "\u6bcf\u5e74\u8c03\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,82,25)"
                        }
                    }
                },
                {
                    "name": "\u5b63\u5ea6\u5956",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,54,67)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5e9514\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,78,5)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5efa\u8bbe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,88,96)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u5927\u725b\u5e26\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,144,116)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u6027\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,159,159)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u4e2d\u575a\u529b\u91cf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,63,84)"
                        }
                    }
                },
                {
                    "name": "AI\u4ea7\u54c1\u7814\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,43,109)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51\u533b\u7597\u9886\u5934\u7f8a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,4,97)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,151,45)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u7a7a\u95f4\u53ca\u85aa\u916c\u9ad8\u4e8e\u540c\u884c\u4e1a\u6c34\u5e73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,106,115)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e24\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,8,69)"
                        }
                    }
                },
                {
                    "name": "\u80a1\u7968",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,12,88)"
                        }
                    }
                },
                {
                    "name": "\u5728\u8fd9\u91cc\u4f60\u6709\u66f4\u591a\u7684\u81ea\u7531\u53d1\u6325\u548c\u5c55\u793a\u81ea\u5df1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,135,29)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u80cc\u666f\u5f3a\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,23,35)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u7814\u53d1\u4eba\u6570\u5360\u6bd470%",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,134,85)"
                        }
                    }
                },
                {
                    "name": "\u8d1f\u8d23\u4eba\u5e26\u65b0\u624b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,72,13)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u80a1\u4e1c\u9760\u8c31",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,17,65)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c\u798f\u5229\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,16,127)"
                        }
                    }
                },
                {
                    "name": "\u7cbe\u81f4\u8212\u9002\u7684\u529e\u516c\u73af\u5883",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,11,4)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u89c4\u8303",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,36,50)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5e0212\u5e74",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,116,45)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4\u4f73\u7b49\u7b49",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,64,141)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u9614\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,64,101)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5382\u53d1\u5c55\u524d\u666f\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,152,39)"
                        }
                    }
                },
                {
                    "name": "\u725b\u4eba\u56e2\u961f\u80cc\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,37,93)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u524d\u6cbf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,88,148)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6167\u57ce\u5e02",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,115,131)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5927\u795e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,102,39)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u505c\u8f66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,151,65)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u7ba1\u7406\u9f13\u52b1\u8bd5\u9519",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,76,58)"
                        }
                    }
                },
                {
                    "name": "\u4ff1\u4e50\u90e8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,41,90)"
                        }
                    }
                },
                {
                    "name": "\u5341\u56db\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,154,63)"
                        }
                    }
                },
                {
                    "name": "\u4f9b\u5e94\u94fe\u91d1\u878d\u79d1\u6280\u5934\u90e8\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,23,146)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5bbf\u820d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,4,128)"
                        }
                    }
                },
                {
                    "name": "\u624e\u624e\u5b9e\u5b9e\u505a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,108,52)"
                        }
                    }
                },
                {
                    "name": "\u771f\u5b9e\u4e30\u5bcc\u7684\u5e94\u7528\u573a\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,71,44)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u7ebf\u98ce\u6295\u52a0\u6301",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,159,94)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u901f\u53d1\u5c55\u9636\u6bb5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,84,91)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u5c97\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,147,84)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u6ee1\u5206",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,87,144)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u6f5c\u529b\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,107,54)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u5e7f\u544a\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,65,39)"
                        }
                    }
                },
                {
                    "name": "\u4e0e\u901a\u8054\u6570\u636e\u8054\u5408\u62db\u8058",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,157,100)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u91cf\u533b\u7597\u6570\u636e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,21,156)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u524d\u666f\u53ef\u89c2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,2,17)"
                        }
                    }
                },
                {
                    "name": "2\u4f4d\u9662\u58eb\u9886\u8854",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,25,21)"
                        }
                    }
                },
                {
                    "name": "\u6d53\u539a\u7684\u6280\u672f\u5b66\u4e60\u6c1b\u56f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,73,87)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u80cc\u666f\u5f3a\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,55,90)"
                        }
                    }
                },
                {
                    "name": "\u4f30\u503c\u767e\u4ebf\u7f8e\u5143",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,129,28)"
                        }
                    }
                },
                {
                    "name": "\u573a\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,158,98)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1atop",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,92,98)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,1,109)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,146,6)"
                        }
                    }
                },
                {
                    "name": "\u8212\u5fc3\u4f01\u4e1a\u6587\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,31,8)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u6742\u4e8b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,90,82)"
                        }
                    }
                },
                {
                    "name": "\u6ce8\u91cd\u4e2a\u4eba\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,51,82)"
                        }
                    }
                },
                {
                    "name": "\u52a0\u73ed\u9910\u8865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,131,140)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u9910\u98df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,98,157)"
                        }
                    }
                },
                {
                    "name": "\u9f13\u52b1\u521b\u65b0\u7684\u5de5\u4f5c\u73af\u5883",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,40,70)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u5de5\u7a0b\u5e08-\u6570\u636e\u6316\u6398\u65b9\u5411",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,42,40)"
                        }
                    }
                },
                {
                    "name": "CTO\u7b97\u6cd5\u5927\u725b\u5e26\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,121,56)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u65e0\u4e0a\u9650",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,71,42)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u4f01\u80cc\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,24,124)"
                        }
                    }
                },
                {
                    "name": "\u72ec\u7acb\u5e26\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,129,49)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4Nice",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,98,41)"
                        }
                    }
                },
                {
                    "name": "\u5168\u7403\u51fa\u56fd\u6e38",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,126,34)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u7a33\u5b9a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,41,102)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u901f\u5ea6\u5feb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,49,99)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u4e0b\u5348\u8336\u968f\u65f6\u51c6\u5907\u8d77\u7684",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,82,67)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u65b0\u9896",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,77,67)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u91cf\u7ea7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,144,160)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1;\u8282\u65e5\u8865\u8d34;\u7ee9\u6548\u5956\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,56,2)"
                        }
                    }
                },
                {
                    "name": "1.\u56e2\u961f\u4e1a\u52a1\u7d27\u8ddf\u96c6\u56e2\u7684\u4e1a\u52a1\u76ee\u6807",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,141,143)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u4f73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,125,2)"
                        }
                    }
                },
                {
                    "name": "\u5168\u7403\u9886\u5148",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,103,111)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7d20\u8d28\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,55,2)"
                        }
                    }
                },
                {
                    "name": "\u65bd\u5c55\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,33,36)"
                        }
                    }
                },
                {
                    "name": "\u8282\u5047\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,36,138)"
                        }
                    }
                },
                {
                    "name": "\u516c\u79ef\u91d1\u5168\u989d\u6700\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,113,37)"
                        }
                    }
                },
                {
                    "name": "\u65e5\u6570\u636e\u767e\u4ebf\u7ea7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,39,38)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u798f\u5229\u5f85\u9047\u4f18\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,1,98)"
                        }
                    }
                },
                {
                    "name": "\u5305\u4f4f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,6,38)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,50,69)"
                        }
                    }
                },
                {
                    "name": "\u9910\u901a\u8baf\u4ea4\u901a\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,34,48)"
                        }
                    }
                },
                {
                    "name": "\u5bfc\u5e08\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,139,127)"
                        }
                    }
                },
                {
                    "name": "\u5343\u4eba\u89c4\u6a21",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,105,146)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u5feb\u901f\u53d1\u5c55",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,76,9)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u6e29\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,52,127)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6c1b\u56f4\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,49,55)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u9614\u7a7a\u95f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,108,135)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u540d\u667a\u80fd\u9a7e\u9a76\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,34,124)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u53d1\u5c55\u5feb\u901f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,62,88)"
                        }
                    }
                },
                {
                    "name": "5\u59297\u5c0f\u65f6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,82,41)"
                        }
                    }
                },
                {
                    "name": "\u4e0e\u559c\u9a6c\u62c9\u96c5APP\u8054\u5408\u62db\u8058",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,52,39)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u7a33\u5b9a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,98,33)"
                        }
                    }
                },
                {
                    "name": "\u811a\u8e0f\u5b9e\u5730",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,77,86)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u4f18\u52bf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,85,129)"
                        }
                    }
                },
                {
                    "name": "\u521b\u65b0\u4e0e\u6311\u6218",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,137,34)"
                        }
                    }
                },
                {
                    "name": "\u6709\u7528\u6237\u57fa\u7840",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,64,49)"
                        }
                    }
                },
                {
                    "name": "\u5546\u4e1a\u6c14\u8c61\u5934\u90e8\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,155,89)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u4e3a\u4e3b\u5bfc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,76,105)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u901f\u589e\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,8,125)"
                        }
                    }
                },
                {
                    "name": "\u7ba1\u7406\u6241\u5e73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,29,132)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4fdd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,90,25)"
                        }
                    }
                },
                {
                    "name": "\u5bfc\u5e081v1\u5e26",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,62,30)"
                        }
                    }
                },
                {
                    "name": "\u9876\u683c\u4f4f\u623f\u516c\u79ef\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,40,152)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u540d\u4e92\u8054\u7f51\u516c\u53f8\u80cc\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,31,13)"
                        }
                    }
                },
                {
                    "name": "AI\u672a\u6765",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,85,61)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u73af\u5883\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,129,6)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u672f\u548c\u5e94\u7528\u7ed3\u5408",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,106,101)"
                        }
                    }
                },
                {
                    "name": "\u5165\u804c\u5373\u4e0a\u4e94\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,21,83)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u4e30\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,110,52)"
                        }
                    }
                },
                {
                    "name": "\u52a0\u73ed\u4ea4\u8865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,29,127)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u5185**\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,121,159)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c\u798f\u5229\u4f18\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,5,139)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f\u7a7a\u95f4\u5de8\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,26,160)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u7ebf\u4e92\u8054\u7f51\u516c\u53f8\u7d27\u6025\u804c\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,18,107)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u5b9a\u8282\u5047\u65e5\u653e\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,64,72)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,86,62)"
                        }
                    }
                },
                {
                    "name": "\u80cc\u666f\u6280\u672f\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,10,25)"
                        }
                    }
                },
                {
                    "name": "\u535a\u58eb\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,158,125)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u4e00\u6d41",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,83,155)"
                        }
                    }
                },
                {
                    "name": "\u5fd7\u540c\u9053\u5408\u7684\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,59,80)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u798f\u5229\u4f18",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,89,71)"
                        }
                    }
                },
                {
                    "name": "\u80a1\u4e1c\u80cc\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,155,64)"
                        }
                    }
                },
                {
                    "name": "\u817e\u8baf\u97f3\u4e50\u730e\u5934\u804c\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,88,47)"
                        }
                    }
                },
                {
                    "name": "\u8ddf\u725b\u4eba\u4e00\u8d77\u5de5\u4f5c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,36,35)"
                        }
                    }
                },
                {
                    "name": "\u804c\u4e1a\u53d1\u5c55\u826f\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,20,131)"
                        }
                    }
                },
                {
                    "name": "500\u5f3a\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,10,115)"
                        }
                    }
                },
                {
                    "name": "E\u8f6e\u878d\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,108,53)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u9910\u8865\u52a9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,85,97)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u672f\u548c\u5de5\u4f5c\u80cc\u666f\u725b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,137,130)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,54,81)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u5357\u4e9a\u5e02\u573a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,96,90)"
                        }
                    }
                },
                {
                    "name": "5\u59298\u5c0f\u65f6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,70,34)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u90e8\u95e8\u6838\u5fc3\u5c97\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,73,138)"
                        }
                    }
                },
                {
                    "name": "**\u533b\u9662\u5408\u4f5c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,152,86)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u9886\u519b\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,43,69)"
                        }
                    }
                },
                {
                    "name": "\u805a\u4e00\u7fa4\u6709\u60c5\u4e49\u7684\u4eba\u505a\u6210\u6709\u610f\u4e49\u7684\u4e8b\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,44,53)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u4ea7\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,109,121)"
                        }
                    }
                },
                {
                    "name": "\u5e02\u573a\u7ade\u4e89\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,79,121)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u4f4f\u5bbf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,69,21)"
                        }
                    }
                },
                {
                    "name": "ai\u533b\u7597\u72ec\u89d2\u517d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,139,55)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1aTOP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,24,154)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u52a8\u578b\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,45,23)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u4eba\u914d\u9001",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,13,54)"
                        }
                    }
                },
                {
                    "name": "\u79fb\u52a8\u4e92\u8054\u7f51\u5e7f\u544a\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,15,144)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,31,122)"
                        }
                    }
                },
                {
                    "name": "\u5229\u7528\u6700\u524d\u6cbf\u7684\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,133,42)"
                        }
                    }
                },
                {
                    "name": "\u63a2\u7d22\u524d\u6cbf\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,111,76)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5916\u9879\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,140,24)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5496\u6307\u5bfc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,81,48)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u4e0d\u9519",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,94,150)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u597d\u5f85\u9047\u4f18",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,123,65)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,94,27)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u5feb\u901f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,52,157)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u5185\u540d\u5217\u524d\u8305",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,22,54)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u6c1b\u56f4\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,49,37)"
                        }
                    }
                },
                {
                    "name": "\u82f1\u96c4\u6587\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,144,48)"
                        }
                    }
                },
                {
                    "name": "\u5916\u4f01\u6c1b\u56f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,159,123)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4fdd\u516c\u79ef\u91d1\u60c5\u51b5\uff1a\u516d\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,148,17)"
                        }
                    }
                },
                {
                    "name": "90\u540e\u5e74\u8f7b\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,70,40)"
                        }
                    }
                },
                {
                    "name": "\u521b\u4e1a\u578b\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,75,66)"
                        }
                    }
                },
                {
                    "name": "\u662f\u6781\u5177\u6f5c\u529b\u7684AI\u5e94\u7528\u65b9\u5411",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,93,157)"
                        }
                    }
                },
                {
                    "name": "\u5b9e\u4e60\u751f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,126,90)"
                        }
                    }
                },
                {
                    "name": "\u521b\u4e1a\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,25,147)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u5236\u9020",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,45,56)"
                        }
                    }
                },
                {
                    "name": "\u9f99\u5934\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,50,103)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u53d1\u5c55\u5feb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,24,78)"
                        }
                    }
                },
                {
                    "name": "\u7ee9\u6548\u5956\u91d1\u4e30\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,82,93)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u9ad8\u6210\u957f\u671f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,105,44)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u79c0\u7684\u6280\u672f\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,122,146)"
                        }
                    }
                },
                {
                    "name": "\u76f4\u63a5\u8ddf\u9879\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,113,68)"
                        }
                    }
                },
                {
                    "name": "\u5173\u952e\u5c97\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,104,127)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u65b9\u5f0f\u7075\u6d3b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,155,69)"
                        }
                    }
                },
                {
                    "name": "\u6709\u73ed\u8f66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,135,50)"
                        }
                    }
                },
                {
                    "name": "\u5b8c\u5584\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,75,73)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u4f01\u6ce8\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,109,59)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u53e3\u7891\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,58,113)"
                        }
                    }
                },
                {
                    "name": "\u4f60\u7684\u6bcf\u4e00",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,143,6)"
                        }
                    }
                },
                {
                    "name": "\u5b8c\u5584\u7684\u664b\u5347\u901a\u9053",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,121,29)"
                        }
                    }
                },
                {
                    "name": "\u4e0e\u54c8\u5570\u51fa\u884c\u8054\u5408\u62db\u8058",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,65,16)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6269\u62db",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,143,23)"
                        }
                    }
                },
                {
                    "name": "\u5168\u989d\u8d2d\u4e70\u4e94\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,149,60)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u664b\u5347\u5feb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,15,129)"
                        }
                    }
                },
                {
                    "name": "\u8d1f\u8d23\u641c\u72d7\u6570\u5b57\u4eba\u76843D\u4eba\u8138\u7b97\u6cd5\u65b9\u9762\u7684\u7814\u7a76",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,94,28)"
                        }
                    }
                },
                {
                    "name": "7\u5c0f\u65f6\u5de5\u4f5c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,52,56)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u516d\u9669\u4e00\u91d1\u996d\u8d34\u8f66\u8d34\u7ee9\u6548\u5956\u5b9a\u671f\u4f53\u68c0\u805a\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,132,151)"
                        }
                    }
                },
                {
                    "name": "\u524d\u6cbfAR\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,29,157)"
                        }
                    }
                },
                {
                    "name": "\u524d\u666f\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,34,143)"
                        }
                    }
                },
                {
                    "name": "\u6311\u6218\u4e0e\u521b\u65b0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,149,140)"
                        }
                    }
                },
                {
                    "name": "\u6625\u8282\u957f\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,136,77)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u516d\u9669\u4e00\u91d1\u996d\u8d34\u8f66\u8d34\u7ee9\u6548\u5956\u5b9a\u671f\u4f53\u68c0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,45,141)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u5e7f\u9614\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,130,75)"
                        }
                    }
                },
                {
                    "name": "\u6301\u7eed\u521b\u65b0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,114,91)"
                        }
                    }
                },
                {
                    "name": "\u5305\u5403\u5305\u4f4f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,142,91)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u5de5\u4f5c\u673a\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,110,29)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u6613\u6709\u9053",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,82,2)"
                        }
                    }
                },
                {
                    "name": "\u4ebf\u7ea7\u6570\u636e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,78,140)"
                        }
                    }
                },
                {
                    "name": "\u7d2b\u5149\u96c6\u56e2\u65d7\u4e0b\u6559\u80b2\u4fe1\u606f\u5316\u5934\u90e8\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,129,3)"
                        }
                    }
                },
                {
                    "name": "\u4e03\u9669\u4e8c\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,140,49)"
                        }
                    }
                },
                {
                    "name": "\u5305\u4e09\u9910\u96f6\u98df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,0,151)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u5bcc\u7684\u5458\u5de5\u6d3b\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,122,151)"
                        }
                    }
                },
                {
                    "name": "\u5305\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,9,125)"
                        }
                    }
                },
                {
                    "name": "\u805a\u7126\u524d\u6cbf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,41,34)"
                        }
                    }
                },
                {
                    "name": "\u5168\u7403\u6700\u5927\u4e09\u65b9\u5e7f\u544a\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,138,15)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u5e26\u961f\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,138,112)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u6027\u5316\u7684\u4f01\u4e1a\u7ba1\u7406\u65b9\u5f0f\u548c\u8f7b\u677e\u6d3b\u6cfc\u7684\u5de5\u4f5c\u6c1b\u56f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,84,98)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u79d1\u6280\u884c\u4e1aTOP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,53,116)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6167\u533b\u7597",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,2,141)"
                        }
                    }
                },
                {
                    "name": "\u4e0e\u5f97\u7269APP\u8054\u5408\u62db\u8058",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,42,155)"
                        }
                    }
                },
                {
                    "name": "\u591a\u4e2a\u529e\u516c\u5730\u70b9\u53ef\u9009",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,47,126)"
                        }
                    }
                },
                {
                    "name": "\u843d\u5730\u573a\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,30,120)"
                        }
                    }
                },
                {
                    "name": "12\u5929\u5e74\u5047\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,58,134)"
                        }
                    }
                },
                {
                    "name": "\u4f53\u68c0/\u5f39\u6027\u4e0a\u4e0b\u73ed/\u5e74\u7ec8\u7ee9\u6548/\u514d\u8d39\u5348\u665a\u9910\u4e0b\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,133,96)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u5e74\u5047\u8bd5\u7528\u671f\u540c\u85aa\u4e94\u9669\u4e00\u91d1\u957f\u671f\u6fc0\u52b1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,8,73)"
                        }
                    }
                },
                {
                    "name": "\u6c14\u6c1b\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,14,142)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u4e1a\u4e13\u5fc3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,118,142)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5185\u4e00\u534a\u6765\u81ea\u6e05\u534e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,49,72)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u63a8\u8350",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,154,154)"
                        }
                    }
                },
                {
                    "name": "\u8c03\u85aa\u673a\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,135,41)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u7ea2\u4e66\u7b49\u516c\u53f8\u7b7e\u8ba2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,154,120)"
                        }
                    }
                },
                {
                    "name": "\u7a33\u5b9a\u53d1\u5c55",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,83,147)"
                        }
                    }
                },
                {
                    "name": "\u7ee9\u6548\u5956\u52b1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,43,64)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u6838\u5fc3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,27,157)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u7a7a\u95f4\u5e7f\u9614",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,127,53)"
                        }
                    }
                },
                {
                    "name": "\u7a7a\u95f4\u5de8\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,61,143)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u8c03\u5ea6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,127,7)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u5e72\u9884\u662f\u7f8e\u56e2\u9a91\u884c\u4e1a\u52a1\u6838\u5fc3\u90e8\u5206",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,77,146)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546\u5bfc\u8d2d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,85,69)"
                        }
                    }
                },
                {
                    "name": "\u9886\u5148\u7684\u4eba\u5de5\u667a\u80fd\u5b66\u4e60\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,101,127)"
                        }
                    }
                },
                {
                    "name": "\u9910\u8865\u623f\u8865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,85,42)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u8f7b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,70,102)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u901f\u53d1\u5c55\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,107,58)"
                        }
                    }
                },
                {
                    "name": "\u5782\u76f4\u7535\u5546",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,70,151)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u725b\u6307\u5bfc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,20,141)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u540d\u5927\u5382\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,12,18)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u91d1\u96c4\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,116,18)"
                        }
                    }
                },
                {
                    "name": "\u5f15\u9886\u884c\u4e1a\u8d70\u52bf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,137,7)"
                        }
                    }
                },
                {
                    "name": "\u5168\u989d\u516d\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,8,26)"
                        }
                    }
                },
                {
                    "name": "10\u5929\u6625\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,33,36)"
                        }
                    }
                },
                {
                    "name": "\u7eff\u8c37\u5236\u836f\u5b50\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,24,77)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5382\u4f18\u79c0\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,128,6)"
                        }
                    }
                },
                {
                    "name": "Mac",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,82,102)"
                        }
                    }
                },
                {
                    "name": "\u72ec\u7acb\u8d1f\u8d23",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,95,37)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4OPEN",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,11,101)"
                        }
                    }
                },
                {
                    "name": "\u51c6\u72ec\u89d2\u517d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,104,86)"
                        }
                    }
                },
                {
                    "name": "\u8db3\u989d\u4fdd\u9669\u516c\u79ef\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,81,133)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u5b66\u4e60\u7b97\u6cd5\u5de5\u7a0b\u5e08",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,111,39)"
                        }
                    }
                },
                {
                    "name": "open",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,101,7)"
                        }
                    }
                },
                {
                    "name": "\u96c6\u4f53\u51fa\u6e38",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,15,65)"
                        }
                    }
                },
                {
                    "name": "\u5f00\u653e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,133,48)"
                        }
                    }
                },
                {
                    "name": "AI\u56e2\u961f\u7b79\u5efa\u4e2d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,13,98)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6709\u4f18\u5f02\u7684\u6280\u672f\u6df1\u5ea6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,3,115)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5e95\u635e\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,28,59)"
                        }
                    }
                },
                {
                    "name": "\u6e05\u534e\u7814\u7a76\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,82,157)"
                        }
                    }
                },
                {
                    "name": "\u504f\u5e73\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,86,156)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u6c1b\u56f4\u878d\u6d3d\u53d1\u5c55\u6f5c\u529b\u5de8\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,8,55)"
                        }
                    }
                },
                {
                    "name": "\u5177\u6709",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,84,146)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u98df\u996e\u6599\u4e0b\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,141,50)"
                        }
                    }
                },
                {
                    "name": "\u751f\u65e5\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,17,156)"
                        }
                    }
                },
                {
                    "name": "\u6f5c\u529b\u65e0\u9650",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,76,86)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u4ea7\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,67,112)"
                        }
                    }
                },
                {
                    "name": "500\u5f3a\u7814\u53d1\u4e2d\u5fc3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,97,131)"
                        }
                    }
                },
                {
                    "name": "\u6253\u8f66\u514d\u8d39",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,55,56)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u4f9b\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,127,127)"
                        }
                    }
                },
                {
                    "name": "\u5f00\u653e\u900f\u660e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,2,19)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5f52\u79d1\u7814\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,60,3)"
                        }
                    }
                },
                {
                    "name": "\u5927\u878d\u8d44\u80cc\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,124,28)"
                        }
                    }
                },
                {
                    "name": "\u4f01\u4e1a\u5feb\u901f\u6210\u957f\u671f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,155,43)"
                        }
                    }
                },
                {
                    "name": "\u96c6\u56e2\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,113,57)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u9910\u8865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,43,39)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u5047\u65e5\u4e94\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,60,46)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6e90\u5e73\u53f0\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,13,121)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u85aa\uff0b\u671f\u6743",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,96,41)"
                        }
                    }
                },
                {
                    "name": "\u51fa\u56fd\u56e2\u5efa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,91,45)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u4ece\u4f18",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,108,32)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,54,84)"
                        }
                    }
                },
                {
                    "name": "AI\u884c\u4e1a\u524d\u6cbf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,28,100)"
                        }
                    }
                },
                {
                    "name": "\u5927\u4f6c\u5e26",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,118,32)"
                        }
                    }
                },
                {
                    "name": "\u52a0\u73ed\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,59,128)"
                        }
                    }
                },
                {
                    "name": "\u8001\u677fnice",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,14,73)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u5b9e\u4e60\u8bc1\u660e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,87,113)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u8c08\u671f\u6743",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,158,148)"
                        }
                    }
                },
                {
                    "name": "\u7a7a\u95f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,120,115)"
                        }
                    }
                },
                {
                    "name": "14-15\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,76,43)"
                        }
                    }
                },
                {
                    "name": "\u6709\u6d3b\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,88,51)"
                        }
                    }
                },
                {
                    "name": "\u592e\u4f01\u5355\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,20,35)"
                        }
                    }
                },
                {
                    "name": "\u5f00\u653e\u578b\u6587\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,15,140)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u5185\u53e3\u7891",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,28,50)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u957f\u5047\u671f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,60,131)"
                        }
                    }
                },
                {
                    "name": "\u822a\u7a7aIT\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,32,120)"
                        }
                    }
                },
                {
                    "name": "\u9662\u58eb\u5e26\u961f\u53c2\u4e0e\u9ad8\u6821\u8054\u5408\u7814\u7a76",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,123,4)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u4e8b\u5047\u4e94\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,63,23)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u9645\u5316\u4ea7\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,80,56)"
                        }
                    }
                },
                {
                    "name": "\u5496\u5561\u5385",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,52,43)"
                        }
                    }
                },
                {
                    "name": "\u73af\u5883\u4f73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,52,14)"
                        }
                    }
                },
                {
                    "name": "\u4ece0\u52301",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,1,90)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u540d\u7535\u5546",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,19,90)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u6311\u6218",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,139,147)"
                        }
                    }
                },
                {
                    "name": "\u963f\u91cc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,100,120)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5916\u5e02\u573a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,48,158)"
                        }
                    }
                },
                {
                    "name": "\u98df\u5802\u7528\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,78,7)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u673a\u4f1a\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,21,105)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u9760",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,46,146)"
                        }
                    }
                },
                {
                    "name": "\u821e\u53f0\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,75,104)"
                        }
                    }
                },
                {
                    "name": "\u6e38\u620fUGC",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,55,100)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u80fd\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,55,12)"
                        }
                    }
                },
                {
                    "name": "\u5982\u679c\u4f60\u6b63\u5728\u8ffd\u68a6\u7684\u8def\u4e0a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,99,93)"
                        }
                    }
                },
                {
                    "name": "\u6211\u53f8\u4e0e\u4eac\u4e1c\u96f6\u552e\u5408\u4f5c\u62db\u52df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,113,68)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5916\u56e2\u5efa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,108,68)"
                        }
                    }
                },
                {
                    "name": "\u5173\u7cfb\u548c\u8c10",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,156,4)"
                        }
                    }
                },
                {
                    "name": "\u5185\u90e8\u521b\u4e1a\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,49,40)"
                        }
                    }
                },
                {
                    "name": "\u7ec6\u5206\u9886\u57df\u9690\u5f62**",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,32,77)"
                        }
                    }
                },
                {
                    "name": "\u4f01\u4e1a\u6c1b\u56f4\u7b80\u5355",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,149,8)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u521b\u65b0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,105,56)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u4f11\u4e94\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,116,45)"
                        }
                    }
                },
                {
                    "name": "\u91cd\u70b9\u90e8\u95e8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,99,36)"
                        }
                    }
                },
                {
                    "name": "\u805a\u96c6\u540c\u884c\u4e1a\u9ad8\u6d45\u4eba\u624d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,17,120)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,71,135)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u7814\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,27,32)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u7a33\u5b9a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,102,42)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u671f\u65c5\u6e38",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,94,95)"
                        }
                    }
                },
                {
                    "name": "\u5065\u8eab\u623f\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,15,30)"
                        }
                    }
                },
                {
                    "name": "\u767e\u4eba\u6280\u672f\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,44,33)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7814\u7b97\u6cd5\u4ea7\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,6,11)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u5efa\u65c5\u6e38",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,118,5)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u7b97\u6cd5\u9a71\u52a8\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,63,20)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u53d1\u5c55\u524d\u666f\u5e7f\u9614",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,102,56)"
                        }
                    }
                },
                {
                    "name": "**\u751f\u7269\u533b\u5b66\u4fe1\u606f\u4e13\u5bb6\u5e26\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,47,70)"
                        }
                    }
                },
                {
                    "name": "\u6bcf\u5e74\u591a\u6b21\u8c03\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,140,147)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u4eba\u5de5\u667a\u80fd\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,147,143)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u6280\u672f\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,145,94)"
                        }
                    }
                },
                {
                    "name": "\u521b\u9020\u524d\u6cbfAI\u4ea7\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,92,144)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u5e7f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,102,136)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u540c\u4e8bnice",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,27,57)"
                        }
                    }
                },
                {
                    "name": "\u9f13\u52b1\u8bd5\u9519",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,10,98)"
                        }
                    }
                },
                {
                    "name": "\u529f\u8bfe\u524d\u6cbf\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,140,38)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5b9e\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,71,68)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u6587\u5316\u56e2\u961fnice",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,70,159)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u725b\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,11,24)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5065\u5168",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,34,32)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u5e73\u53f0\u53d1\u5c55\u524d\u666f\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,76,9)"
                        }
                    }
                },
                {
                    "name": "\u6253\u8f66\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,27,147)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6210\u957f\u5feb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,129,9)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u4e60\u6c1b\u56f4\u6d53\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,147,104)"
                        }
                    }
                },
                {
                    "name": "\u5076\u5c14\u52a0\u73ed\u8c03\u4f11",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,35,144)"
                        }
                    }
                },
                {
                    "name": "\u6587\u827a\u6c1b\u56f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,151,92)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u9650\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,135,66)"
                        }
                    }
                },
                {
                    "name": "\u6536\u5165\u548c\u80fd\u529b\u6210\u957f\u6027\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,109,112)"
                        }
                    }
                },
                {
                    "name": "\u5404\u79cd\u4e0b\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,135,43)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u65c5\u6e38\u4e0b\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,63,20)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u989d\u9910\u8865/TB\u8d39\u7528",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,108,87)"
                        }
                    }
                },
                {
                    "name": "AI\u7b97\u6cd5\u843d\u5730",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,18,16)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c\u798f\u5229\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,148,146)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u6e38\u6216\u6237\u5916\u62d3\u5c55\u57f9\u8bad",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,89,142)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u5b9e\u529b\u96c4\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,84,60)"
                        }
                    }
                },
                {
                    "name": "\u5348\u9910\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,130,44)"
                        }
                    }
                },
                {
                    "name": "\u5305\u5403\u4f4f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,115,82)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5382\u798f\u5229\u5f85\u9047\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,125,16)"
                        }
                    }
                },
                {
                    "name": "\u529e\u516c\u73af\u5883\u4f73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,85,49)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u7b97\u6cd5\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,60,104)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u73af\u7ed5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,52,53)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u53d1\u5c55\u524d\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,69,135)"
                        }
                    }
                },
                {
                    "name": "\u8d5b\u9053\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,129,66)"
                        }
                    }
                },
                {
                    "name": "\u804c\u4e1a\u53d1\u5c55\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,66,7)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u524d\u666f\u8d5e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,132,134)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u699c****",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,15,130)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u9760\u8c31",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,66,26)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u7814\u548c\u5e94\u7528\u7ed3\u5408",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,42,115)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u6325\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,52,152)"
                        }
                    }
                },
                {
                    "name": "\u56fa\u5b9a\u53cc\u4f11",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,10,119)"
                        }
                    }
                },
                {
                    "name": "\u7ba1\u7406\u6241\u5e73\u900f\u660e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,77,58)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6280\u672f\u5927\u725b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,55,116)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,20,16)"
                        }
                    }
                },
                {
                    "name": "\u5bfc\u5e08\u4e00\u5e26\u4e00",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,55,112)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u9886\u57df\u5927\u725b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,107,8)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5177\u6709\u6559\u80b2\u548c\u91d1\u878d\u4e24\u4e2a\u65b9\u5411\u843d\u5730\u573a\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,150,52)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a**",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,129,14)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5ea6\u7ee9\u6548",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,112,154)"
                        }
                    }
                },
                {
                    "name": "\u7269\u6d41",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,138,160)"
                        }
                    }
                },
                {
                    "name": "\u5927\u4f6c\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,145,54)"
                        }
                    }
                },
                {
                    "name": "\u73af\u5883open",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,14,57)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u8f6e\u5c97\u6216\u8f6c\u5c97\u664b\u5347",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,126,79)"
                        }
                    }
                },
                {
                    "name": "\u5929\u773c\u67e5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,97,138)"
                        }
                    }
                },
                {
                    "name": "\u7d2b\u5149\u96c6\u56e2\u65d7\u4e0b\u6559\u80b2\u4fe1\u606f\u5316\u884c\u4e1a\u5934\u90e8\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,7,113)"
                        }
                    }
                },
                {
                    "name": "\u4e3b\u52a8\u52a0\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,51,137)"
                        }
                    }
                },
                {
                    "name": "\u5927\u91cf\u671f\u6743\u6c60",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,34,53)"
                        }
                    }
                },
                {
                    "name": "\u804c\u4f4d\u664b\u5347\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,130,105)"
                        }
                    }
                },
                {
                    "name": "\u90e8\u95e8\u53d1\u5c55\u7a33\u5065",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,129,151)"
                        }
                    }
                },
                {
                    "name": "\u5168\u5e7416-18\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,27,56)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5b9e\u4e60\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,90,113)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u4e09\u9910\u4e0b\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,44,69)"
                        }
                    }
                },
                {
                    "name": "\u9ed1\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,73,86)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u59561-3\u4e2a\u6708",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,17,81)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77/\u6b66\u6c49",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,141,75)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u4e60\u578b\u7ec4\u7ec7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,124,60)"
                        }
                    }
                },
                {
                    "name": "A\u8f6e\u5feb\u624b\u878d\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,106,46)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u53d1\u5c55\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,71,121)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u5e26\u9886",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,78,34)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,154,122)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7531\u5f00\u653e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,129,154)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u98df\u81ea\u7531",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,152,139)"
                        }
                    }
                },
                {
                    "name": "\u90e8\u95e8\u65c5\u6e38",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,59,15)"
                        }
                    }
                },
                {
                    "name": "\u521b\u4e1a\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,120,38)"
                        }
                    }
                },
                {
                    "name": "\u524d\u9014\u9886\u57df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,64,31)"
                        }
                    }
                },
                {
                    "name": "\u6784\u5efa\u4eba\u7c7b\u865a\u62df\u4e16\u754c\u65b0\u4f53\u9a8c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,59,19)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u9650\u6210\u957f\uff01",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,144,16)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956+\u53cc\u4f11+\u516d\u9669\u4e00\u91d1+\u665a\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,145,156)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u7ebf\u6e38\u620f\u5927\u5382",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,23,138)"
                        }
                    }
                },
                {
                    "name": "\u5468\u672b\u53cc\u4f11/\u5f39\u6027\u5de5\u4f5c/\u548c\u8c10\u7684\u529e\u516c\u6c1b\u56f4/1\u5bf91\u5e2e\u5e26",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,32,152)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u5e74\u4e24\u6b21\u8c03\u85aa\u673a\u4f1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,58,64)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u7fd8\u695a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,145,151)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u53d1\u5c55\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,64,91)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u4eba\u8f66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,15,152)"
                        }
                    }
                },
                {
                    "name": "\u6709\u80a1\u7968\u671f\u6743\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,144,148)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u89c6\u9891",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,145,57)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u798f\u5229\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,75,145)"
                        }
                    }
                },
                {
                    "name": "\u516d\u9669\u4e00\u91d1\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,154,135)"
                        }
                    }
                },
                {
                    "name": "\u5bbd\u5e7f\u7684\u53d1\u5c55\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,77,148)"
                        }
                    }
                },
                {
                    "name": "\u8865\u5145\u533b\u7597\u4fdd\u9669",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,75,119)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u9886\u57df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,149,77)"
                        }
                    }
                },
                {
                    "name": "\u4e0e\u676d\u5dde\u5b9e\u5728\u667a\u80fd\u79d1\u6280\u6709\u9650\u516c\u53f8\u8054\u5408\u62db\u8058",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,110,64)"
                        }
                    }
                },
                {
                    "name": "\u5404\u79cd\u56e2\u5efa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,21,83)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u5185\u9886\u5148",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,80,155)"
                        }
                    }
                },
                {
                    "name": "\u826f\u597d\u53d1\u5c55\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,155,47)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u597d\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,20,45)"
                        }
                    }
                },
                {
                    "name": "500\u5f3a\u7814\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,13,1)"
                        }
                    }
                },
                {
                    "name": "500\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,144,14)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u62ff\u4eb2\u81ea\u5e26",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,52,71)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6709\u4f5c\u4e3a\uff01",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,148,64)"
                        }
                    }
                },
                {
                    "name": "\u535a\u5bfc\u5e26\u961f\u7684\u6df1\u5ea6\u5b66\u4e60\u4eba\u5de5\u667a\u80fd\u7814\u7a76\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,106,117)"
                        }
                    }
                },
                {
                    "name": "\u5e02\u573a\u524d\u666f\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,72,79)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c\u5f85\u9047\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,113,115)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u5316\u5f15\u64ce\u7684\u7cfb\u7edf\u67b6\u6784",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,61,116)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5916\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,115,25)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u5e74\u4e24\u6b21\u8c03\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,43,135)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u5bf9\u4e00\u5e26\u6559",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,143,145)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u5927\u725b\u4e91\u96c6\u9879\u76ee\u5956\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,15,106)"
                        }
                    }
                },
                {
                    "name": "9\u70b9\u6253\u8f66\u62a5\u9500",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,127,11)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u98df\u4e0b\u5348\u8336outing\u4e0d\u505c\u6b47",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,72,100)"
                        }
                    }
                },
                {
                    "name": "\u6d3b\u529b\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,39,132)"
                        }
                    }
                },
                {
                    "name": "AI\u4ea7\u54c1\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,107,138)"
                        }
                    }
                },
                {
                    "name": "\u521d\u521b\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,50,160)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u5b9e\u6218",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,48,140)"
                        }
                    }
                },
                {
                    "name": "Pro\u529e\u516c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,70,134)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u5feb\u901f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,68,132)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u5168",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,144,117)"
                        }
                    }
                },
                {
                    "name": "\u653f\u5e9c\u91cd\u70b9\u652f\u6301\u9879\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,74,85)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u4e60\u673a\u4f1a\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,120,65)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5ea6\u8c03\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,71,114)"
                        }
                    }
                },
                {
                    "name": "Mac\u529e\u516c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,89,29)"
                        }
                    }
                },
                {
                    "name": "\u671f\u6743\u6fc0\u52b1\u5e26\u85aa\u5e74\u5047\u4e94\u9669\u4e00\u91d1\u8282\u65e5\u793c\u7269\u5e74\u5ea6\u65c5\u6e38",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,127,30)"
                        }
                    }
                },
                {
                    "name": "\u826f\u597d\u7684\u5de5\u4f5c\u73af\u5883",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,40,105)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,20,148)"
                        }
                    }
                },
                {
                    "name": "\u53cd\u9988\u5feb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,135,9)"
                        }
                    }
                },
                {
                    "name": "\u540c\u4e8b\u597d\u76f8\u5904",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,56,131)"
                        }
                    }
                },
                {
                    "name": "\u540c\u4e8bnice",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,3,25)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,65,98)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u9738",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,53,130)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u73af\u5883\u8f7b\u677e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,135,16)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u53d1\u5c55\u5feb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,32,94)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5496\u5561",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,110,16)"
                        }
                    }
                },
                {
                    "name": "\u7d27\u6025\u804c\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,96,156)"
                        }
                    }
                },
                {
                    "name": "\u535a\u58eb\u843d\u6237",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,90,72)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u85aa+\u80a1\u6743",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,63,90)"
                        }
                    }
                },
                {
                    "name": "\u5305\u4f4f\u5bbf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,152,10)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u7f8e\u5473\u4e09\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,18,126)"
                        }
                    }
                },
                {
                    "name": "\u73af\u5883\u8d85\u68d2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,93,42)"
                        }
                    }
                },
                {
                    "name": "\u641c\u72d7\u5730\u56fe\u6838\u5fc3\u4e1a\u52a1\u65b9\u5411",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,25,88)"
                        }
                    }
                },
                {
                    "name": "\u8be5\u804c\u4f4d\u4e0e\u733f\u8f85\u5bfc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,36,24)"
                        }
                    }
                },
                {
                    "name": "\u975e\u5916\u5305",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,10,64)"
                        }
                    }
                },
                {
                    "name": "\u5b9e\u64cd\u5386\u7ec3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,77,100)"
                        }
                    }
                },
                {
                    "name": "\u7855\u58eb\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,117,77)"
                        }
                    }
                },
                {
                    "name": "\u5343\u4e07\u7ea7\u7528\u6237\u7684\u4ea7\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,43,103)"
                        }
                    }
                },
                {
                    "name": "\u878d\u8d44\u8d8510\u4ebf\u7f8e\u5143",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,84,120)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u4e60\u7a7a\u95f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,135,157)"
                        }
                    }
                },
                {
                    "name": "\u524d\u6cbf\u9886\u57df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,125,132)"
                        }
                    }
                },
                {
                    "name": "\u5168\u9762\u8f6c\u578bAI",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,109,153)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,104,132)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u56e2\u961f20\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,153,91)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u5bb6\u91cd\u70b9\u65b9\u5411",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,83,12)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u9910\u4e0b\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,1,66)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u73af\u5883",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,152,123)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u4e30\u5bcc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,24,133)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u7814\u53d1\u5b9e\u529b\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,35,68)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u4f53\u7cfb\u5b8c\u5584",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,156,34)"
                        }
                    }
                },
                {
                    "name": "\u6709\u7ade\u4e89\u529b\u7684\u85aa\u916c\u5f85\u9047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,61,39)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u4f53\u68c0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,146,58)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u5e26\u961f\uff01\uff01",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,118,83)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u9886\u5148\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,100,105)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6280\u672f\u5927\u5496\u4e91\u96c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,155,49)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u5f85\u9047\u4f18",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,72,21)"
                        }
                    }
                },
                {
                    "name": "\u5468\u672b\u53cc\u4f11/\u5e26\u85aa\u5e74\u5047/\u5168\u989d\u4e94\u9669\u4e00\u91d1/\u4e0a\u5e02\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,57,146)"
                        }
                    }
                },
                {
                    "name": "\u4e24\u4f4d\u9662\u58eb\u4e09\u4f4d\u535a\u58eb\u9886\u8854\u7684\u521d\u521b\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,17,19)"
                        }
                    }
                },
                {
                    "name": "\u5168\u5458mac",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,153,120)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u5916\u5408\u8d44\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,151,150)"
                        }
                    }
                },
                {
                    "name": "\u6709\u826f\u597d\u7684\u53d1\u5c55\u7a7a\u95f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,66,86)"
                        }
                    }
                },
                {
                    "name": "AI\u573a\u666f\u4e30\u5bcc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,91,79)"
                        }
                    }
                },
                {
                    "name": "\u7a33\u5065\u589e\u957f\u7684\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,82,55)"
                        }
                    }
                },
                {
                    "name": "\u4eab\u6709\u80a1\u6743\u6fc0\u52b1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,18,67)"
                        }
                    }
                },
                {
                    "name": "\u8f83\u5927\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,130,115)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u4e0d\u5dee\u94b1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,27,107)"
                        }
                    }
                },
                {
                    "name": "***\u9879\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,159,11)"
                        }
                    }
                },
                {
                    "name": "\u5730\u7406\u4f4d\u7f6e\u4fbf\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,45,130)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5e74\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,12,65)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5206\u4eab",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,108,35)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u81ea\u7531\u5ea6\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,108,57)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u53d1\u5c55\u524d\u666f\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,17,104)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u8d28\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,17,135)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u9a71\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,24,46)"
                        }
                    }
                },
                {
                    "name": "\u5c97\u4f4d\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,153,79)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u4e8b\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,78,139)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u798f\u5229\u5f85\u9047\u597d\u4f11\u606f\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,25,4)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u4e30\u5bcc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,53,98)"
                        }
                    }
                },
                {
                    "name": "\u6311\u6218\u6027\u7684\u5de5\u4f5c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,101,136)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,20,57)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u53d1\u5c55\u5feb\u901f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,72,125)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u56e2\u961f\u5e26\u6559",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,107,63)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u573a\u9762\u8bd5\u6d41\u7a0b\u4e00\u6b21\u8d70\u5b8c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,114,131)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u6e38",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,9,54)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u8f7b\u6241\u5e73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,115,26)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u4f18\u6e25",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,80,121)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,135,87)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6311\u6218\u548c\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,148,26)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u57fa\u5efa\u9886\u57df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,130,45)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5e74\u8f7b\u6709\u6d3b\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,43,87)"
                        }
                    }
                },
                {
                    "name": "\u52a0\u73ed\u8d39\u53e6\u7b97",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,125,36)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5065\u8eab\u623f\u7b49\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,66,11)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7814\u4ea7\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,69,51)"
                        }
                    }
                },
                {
                    "name": "\u5404\u7c7b\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,10,158)"
                        }
                    }
                },
                {
                    "name": "15-20\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,158,105)"
                        }
                    }
                },
                {
                    "name": "\u9910\u996e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,27,45)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u7ebf\u4e92\u8054\u7f51\u516c\u53f8\u804c\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,35,120)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u98df\u4e0b\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,155,95)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u5bfc\u5e08\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,153,30)"
                        }
                    }
                },
                {
                    "name": "\u521b\u65b0\u5e94\u7528",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,58,8)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u901f\u7684\u53d1\u5c55\u524d\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,21,46)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5e74\u8f7b\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,19,155)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u9a71\u52a8\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,153,16)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u9971\u6ee1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,67,117)"
                        }
                    }
                },
                {
                    "name": "\u5185\u90e8\u53d1\u5c55\u7a7a\u95f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,128,59)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u725b\u6587\u6863\u968f\u4fbf\u770b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,95,2)"
                        }
                    }
                },
                {
                    "name": "AI\u667a\u80fd\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,4,6)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u798f\u5229\u4f73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,41,11)"
                        }
                    }
                },
                {
                    "name": "\u6709XLNet\u4e00\u4f5c\u5927\u795e\u5e26\u60a8\u5728\u7b97\u6cd5\u91cc\u6df1\u8015",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,33,69)"
                        }
                    }
                },
                {
                    "name": "\u6bcf\u5e742\u6b21\u8c03\u85aa\u7a97\u53e3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,143,84)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u6210\u719f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,74,136)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u5e7f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,145,57)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u8bc6\u56fe\u8c31\u63a8\u8350",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,81,32)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u524d\u666f\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,4,64)"
                        }
                    }
                },
                {
                    "name": "\u5168\u7403\u9886\u5148\u7684\u5546\u7528\u670d\u52a1\u673a\u5668\u4eba\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,69,107)"
                        }
                    }
                },
                {
                    "name": "\u7814\u7a76\u548c\u5b9e\u9645\u5e94\u7528\u7ed3\u5408",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,84,65)"
                        }
                    }
                },
                {
                    "name": "\u745c\u4f3d\u5065\u8eab",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,34,84)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u52bf\u65b9\u5411\u6280\u672f\u7814\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,133,156)"
                        }
                    }
                },
                {
                    "name": "OCR/\u56fe\u50cf\u5904\u7406\u4e16\u754c\u9886\u5148\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,116,47)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f\u671f\u521b\u4e1a\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,22,27)"
                        }
                    }
                },
                {
                    "name": "\u7a33\u5b9a\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,49,63)"
                        }
                    }
                },
                {
                    "name": "\u521b\u59cb\u56e2\u961f\u725b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,73,8)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u6807\u6746",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,96,137)"
                        }
                    }
                },
                {
                    "name": "\u6280\u80fd\u63d0\u5347",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,26,20)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u6253\u5361",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,145,125)"
                        }
                    }
                },
                {
                    "name": "13\u85aa+\u5956\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,154,137)"
                        }
                    }
                },
                {
                    "name": "\u6b22\u8fce\u60a8\u52a0\u5165\u4e00\u70b9\u5927\u5bb6\u5ead~",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,24,128)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u7d20\u8d28\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,14,103)"
                        }
                    }
                },
                {
                    "name": "\u9910\u996e\u8865\u52a9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,94,75)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5065\u8eab",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,41,42)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,63,106)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u524d\u6cbf\u7814\u7a76\u53ca\u5e94\u7528",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,23,4)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u9886\u57df\u7684\u4eba\u5de5\u667a\u80fd\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,127,20)"
                        }
                    }
                },
                {
                    "name": "\u725b\u4eba\u5e26\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,111,99)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6709\u53ef\u4e3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,83,37)"
                        }
                    }
                },
                {
                    "name": "\u72ec\u7acbAI\u5b9e\u9a8c\u5ba4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,93,139)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u81ea\u7531",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,18,4)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u98de\u901f\u53d1\u5c55",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,157,20)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5e02\u51c6\u5907\u671f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,38,108)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u804c\u7ea7\u664b\u5347",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,124,19)"
                        }
                    }
                },
                {
                    "name": "\u5165\u804c\u5373\u7f34\u4e94\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,102,134)"
                        }
                    }
                },
                {
                    "name": "\u9633\u5149\u900f\u660e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,15,3)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u5347\u4e2a\u4eba\u4ef7\u503c\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,54,57)"
                        }
                    }
                },
                {
                    "name": "\u4f20\u97f3\u63a7\u80a1\u5168\u8d44\u5b50\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,145,84)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7528\u8fd0\u7b79\u4f18\u5316\u77e5\u8bc6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,106,111)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u7814\u7ecf\u8d39",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,56,60)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u6548\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,34,62)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6d3b\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,114,36)"
                        }
                    }
                },
                {
                    "name": "\u4e0b\u5348\u8336\u96f6\u98df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,94,138)"
                        }
                    }
                },
                {
                    "name": "\u8c37\u6b4c\u7b49\u884c\u4e1a\u6700\u4f18\u79c0\u4eba\u624d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,20,54)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u6210\u957f\u6027",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,3,17)"
                        }
                    }
                },
                {
                    "name": "\u8ddf\u5927\u4f6c\u4e00\u8d77\u53c2\u52a0\u56fd\u9645\u9876\u4f1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,141,18)"
                        }
                    }
                },
                {
                    "name": "\u957f\u671f\u7a33\u5b9a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,52,123)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u5496\u5e26\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,116,45)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5382\u5b9e\u4e60",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,127,82)"
                        }
                    }
                },
                {
                    "name": "\u8282\u65e5\u7ea2\u5305",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,89,45)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u539a\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,64,36)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u5efa\u7b49",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,91,50)"
                        }
                    }
                },
                {
                    "name": "\u6b22\u8fce\u52a0\u5165",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,16,12)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u4e60\u73af\u5883\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,152,107)"
                        }
                    }
                },
                {
                    "name": "B\u8f6e\u878d\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,18,152)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u6211\u53d1\u6398",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,43,109)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5382\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,95,128)"
                        }
                    }
                },
                {
                    "name": "\u7ade\u4e89\u529b\u7684\u85aa\u916c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,66,41)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5e95\u53cc\u85aa-\u5e74\u7ec8\u5956-\u6241\u5e73\u5316\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,160,9)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1(\u6700\u9ad8\u6bd4\u4f8b)",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,100,60)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u53d1\u5c55\u5f85\u9047\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,141,133)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u989c\u503c\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,26,42)"
                        }
                    }
                },
                {
                    "name": "\u4e2a\u4eba\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,4,86)"
                        }
                    }
                },
                {
                    "name": "\u4e0e\u4e16\u754c\u9886\u5148\u7684AI\u7814\u53d1\u56e2\u961f\u5408\u4f5c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,129,44)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5e02",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,54,157)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u5f71\u50cf\u884c\u4e1a\u7fd8\u695a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,74,16)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u539a\u5e74\u7ec8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,16,14)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u8c03\u5ea6\u4f18\u5316\u5f15\u64ce\u7684\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,147,157)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u524d\u666f\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,110,110)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u884c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,10,160)"
                        }
                    }
                },
                {
                    "name": "\u96c6\u56e2\u5e73\u53f0\u80cc\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,127,81)"
                        }
                    }
                },
                {
                    "name": "\u521b\u65b0\u6c1b\u56f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,113,129)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u6cdb\u6210\u957f\u7a7a\u95f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,88,3)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5347\u671f\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,8,17)"
                        }
                    }
                },
                {
                    "name": "\u4e0e\u4e0a\u6d77\u91d1\u5353\u79d1\u6280\u6709\u9650\u516c\u53f8\u8054\u5408\u62db\u8058",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,104,121)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u989d\u5e74\u7ec8\u5956",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,31,81)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4\u68d2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,103,91)"
                        }
                    }
                },
                {
                    "name": "\u5b9e\u4e60\u8bc1\u660e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,8,20)"
                        }
                    }
                },
                {
                    "name": "\u65e5\u6d3b\u5343\u4e07",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,37,135)"
                        }
                    }
                },
                {
                    "name": "\u4f9b\u5e94\u4e09\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,111,127)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u8f6f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,123,12)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u4e1a\u56fe\u8c31",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,156,57)"
                        }
                    }
                },
                {
                    "name": "\u4ebf\u7ea7\u7528\u6237",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,100,17)"
                        }
                    }
                },
                {
                    "name": "\u9910\u8865\u4ea4\u901a\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,137,8)"
                        }
                    }
                },
                {
                    "name": "\u8be5\u804c\u4f4d\u76f4\u63a5\u4e0e\u7528\u4eba\u5355\u4f4d\u7b7e\u8ba2\u5408\u540c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,69,96)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u5185\u4ea7\u54c1\u5f71\u54cd\u529b\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,149,48)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6167\u73af\u4fdd\u9886\u519b\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,49,62)"
                        }
                    }
                },
                {
                    "name": "\u524d\u6cbf\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,101,6)"
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
        chart_860a1b78649e4a07bcc3bb4fbe0bedac.setOption(option_860a1b78649e4a07bcc3bb4fbe0bedac);
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
