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

<h2>（2021-06-07更新）</h2>

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
            <button class="tablinks" onclick="showChart(event, 'fdbbd293cfe544b0a3122b2973c2d355')">公司</button>
            <button class="tablinks" onclick="showChart(event, 'e0bd1f5c3a2c4fe4a0ae23ad7a85c74c')">城市</button>
            <button class="tablinks" onclick="showChart(event, '9388591d315f443a8f51817da0d930f1')">城市占比</button>
            <button class="tablinks" onclick="showChart(event, '2ed31d84cb33485da041f59b455feb6b')">招聘地图</button>
            <button class="tablinks" onclick="showChart(event, 'f7edf95b04a54922a82410c66f69bdca')">区域</button>
            <button class="tablinks" onclick="showChart(event, '300a20550e464eb89d8e76d982f19cab')">区域占比</button>
            <button class="tablinks" onclick="showChart(event, '0b26ec817b8e4c04b72483141c18795e')">公司规模</button>
            <button class="tablinks" onclick="showChart(event, '70a57f8fb4ab44f49a908fa5274dba1b')">人员规模</button>
            <button class="tablinks" onclick="showChart(event, '1a360e90a8494d30a29ff8059267b915')">行业</button>
            <button class="tablinks" onclick="showChart(event, 'd7721ad103e34051ab6322df22ea5d07')">招聘方向</button>
            <button class="tablinks" onclick="showChart(event, '15c175c931ae472da08560676b8d5a86')">公司福利</button>
    </div>

    <div class="box">
                <div id="fdbbd293cfe544b0a3122b2973c2d355" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_fdbbd293cfe544b0a3122b2973c2d355 = echarts.init(
            document.getElementById('fdbbd293cfe544b0a3122b2973c2d355'), 'white', {renderer: 'canvas'});
            
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
    
        var option_fdbbd293cfe544b0a3122b2973c2d355 = {
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
                59,
                43,
                32,
                28,
                21,
                18,
                16,
                15,
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
                    "value": 59,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,128,88)"
                        }
                    }
                },
                {
                    "name": "\u5b57\u8282\u8df3\u52a8",
                    "value": 43,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,137,116)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u5982\u79c4",
                    "value": 32,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,28,24)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u79d1\u6280",
                    "value": 28,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,139,120)"
                        }
                    }
                },
                {
                    "name": "\u597d\u897f\u67da\u6559\u80b2",
                    "value": 21,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,120,66)"
                        }
                    }
                },
                {
                    "name": "\u6ef4\u6ef4",
                    "value": 18,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,106,109)"
                        }
                    }
                },
                {
                    "name": "\u9177\u72d7\u97f3\u4e50",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,140,112)"
                        }
                    }
                },
                {
                    "name": "\u9177\u5bb6\u4e50",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,27,99)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u8d4b\u667a",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,112,148)"
                        }
                    }
                },
                {
                    "name": "\u964c\u964c",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,148,125)"
                        }
                    }
                },
                {
                    "name": "\u5929\u773c\u67e5",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,157,60)"
                        }
                    }
                },
                {
                    "name": "\u5357\u6e56\u9662",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,110,68)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u6613",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,59,129)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u4eba\u5bff",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,37,120)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u6d6a\u7f51",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,83,158)"
                        }
                    }
                },
                {
                    "name": "Insta360\u5f71\u77f3",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,95,51)"
                        }
                    }
                },
                {
                    "name": "\u641c\u72d7",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,152,24)"
                        }
                    }
                },
                {
                    "name": "\u62fc\u591a\u591a",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,2,79)"
                        }
                    }
                },
                {
                    "name": "\u5546\u6c64\u79d1\u6280",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,148,7)"
                        }
                    }
                },
                {
                    "name": "MINIEYE",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,34,18)"
                        }
                    }
                },
                {
                    "name": "\u7231\u5947\u827a",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,56,29)"
                        }
                    }
                },
                {
                    "name": "\u666e\u6e21\u79d1\u6280",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,74,18)"
                        }
                    }
                },
                {
                    "name": "\u643a\u7a0b\u96c6\u56e2",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,41,147)"
                        }
                    }
                },
                {
                    "name": "\u6570\u7f8e",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,41,49)"
                        }
                    }
                },
                {
                    "name": "\u817e\u8baf",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,71,122)"
                        }
                    }
                },
                {
                    "name": "\u9b54\u65b9\u706b\u79cd\u4f01\u4e1a\u7ba1\u7406\u54a8\u8be2",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,153,118)"
                        }
                    }
                },
                {
                    "name": "\u6d82\u9e26\u667a\u80fd",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,29,98)"
                        }
                    }
                },
                {
                    "name": "\u76c8\u5609\u4e92\u8054",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,116,114)"
                        }
                    }
                },
                {
                    "name": "\u901a\u8054\u6570\u636e",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,152,15)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u78c1\u77f3",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,134,112)"
                        }
                    }
                },
                {
                    "name": "\u8c31\u65f6\u660a\u552f\u6570\u636e",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,8,138)"
                        }
                    }
                },
                {
                    "name": "Versa",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,127,122)"
                        }
                    }
                },
                {
                    "name": "\u4e07\u79d1",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,30,58)"
                        }
                    }
                },
                {
                    "name": "\u7693\u884c\u79d1\u6280",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,126,20)"
                        }
                    }
                },
                {
                    "name": "\u6167\u5b89\u91d1\u79d1",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,69,122)"
                        }
                    }
                },
                {
                    "name": "\u767e\u5ea6",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,138,40)"
                        }
                    }
                },
                {
                    "name": "\u732b\u5c90\u667a\u80fd",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,82,6)"
                        }
                    }
                },
                {
                    "name": "\u5fc5\u793a\u79d1\u6280",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,86,105)"
                        }
                    }
                },
                {
                    "name": "DMAI\u667a\u80fd\u79d1\u6280",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,151,155)"
                        }
                    }
                },
                {
                    "name": "360os",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,14,152)"
                        }
                    }
                },
                {
                    "name": "\u631a\u9014\u79d1\u6280",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,58,159)"
                        }
                    }
                },
                {
                    "name": "\u5343\u5bfb\u4f4d\u7f6e",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,87,99)"
                        }
                    }
                },
                {
                    "name": "\u8054\u5408\u96c6\u56e2",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,57,51)"
                        }
                    }
                },
                {
                    "name": "\u5f97\u7269App",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,56,8)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5730\u91cf\u5b50",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,49,15)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u6052\u4fe1\u606f",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,45,81)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u56fe\u79d1\u6280",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,46,158)"
                        }
                    }
                },
                {
                    "name": "Soul",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,129,143)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u4ed9\u673a\u5668\u4eba",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,25,52)"
                        }
                    }
                },
                {
                    "name": "\u827a\u6570\u672a\u6765",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,66,60)"
                        }
                    }
                },
                {
                    "name": "\u8363\u8000\u7ec8\u7aef",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,50,55)"
                        }
                    }
                },
                {
                    "name": "\u5f71\u521b\u79d1\u6280",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,10,39)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u5c45\u5ba2",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,148,44)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u51b0",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,74,29)"
                        }
                    }
                },
                {
                    "name": "\u65f7\u89c6MEGVII",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,54,10)"
                        }
                    }
                },
                {
                    "name": "\u5faa\u73af\u667a\u80fd",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,38,95)"
                        }
                    }
                },
                {
                    "name": "\u8f7b\u821f\u667a\u822a",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,107,97)"
                        }
                    }
                },
                {
                    "name": "\u53c2\u6570",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,157,157)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u597d\u5b66",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,39,142)"
                        }
                    }
                },
                {
                    "name": "360",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,27,107)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u624b",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,149,123)"
                        }
                    }
                },
                {
                    "name": "\u9605\u6587\u96c6\u56e2",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,120,57)"
                        }
                    }
                },
                {
                    "name": "\u8d5b\u76ee\u79d1\u6280",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,74,75)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u5e02\u6bd4\u4e00\u6bd4\u7f51\u7edc\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,120,79)"
                        }
                    }
                },
                {
                    "name": "\u667a\u62d3\u89c6\u754c",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,89,85)"
                        }
                    }
                },
                {
                    "name": "OPPO",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,119,103)"
                        }
                    }
                },
                {
                    "name": "\u6587\u5411\u4e7e",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,60,101)"
                        }
                    }
                },
                {
                    "name": "\u5600\u55d2\u51fa\u884c",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,68,127)"
                        }
                    }
                },
                {
                    "name": "Aibee",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,29,108)"
                        }
                    }
                },
                {
                    "name": "\u5efa\u4fe1\u91d1\u79d1",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,153,74)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u667a\u6167",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,126,51)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u7c73\u96c6\u56e2",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,119,141)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u4ed3\u667a\u80fd\u4ed3\u50a8",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,91,74)"
                        }
                    }
                },
                {
                    "name": "\u8fbe\u89c2\u6570\u636e",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,136,138)"
                        }
                    }
                },
                {
                    "name": "\u638c\u95e8\u6559\u80b2",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,8,21)"
                        }
                    }
                },
                {
                    "name": "\u4eac\u4e1c\u96c6\u56e2",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,45,141)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5c1a\u79d1\u6280",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,56,118)"
                        }
                    }
                },
                {
                    "name": "Gostudy",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,58,79)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u81f4",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,122,68)"
                        }
                    }
                },
                {
                    "name": "\u4eac\u4e1c\u7269\u6d41",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,72,14)"
                        }
                    }
                },
                {
                    "name": "\u8fc5\u96f7",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,159,43)"
                        }
                    }
                },
                {
                    "name": "\u54d4\u54e9\u54d4\u54e9",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,45,125)"
                        }
                    }
                },
                {
                    "name": "\u683c\u7075\u6df1\u77b3",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,21,108)"
                        }
                    }
                },
                {
                    "name": "\u6749\u6570\u79d1\u6280",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,15,48)"
                        }
                    }
                },
                {
                    "name": "\u6765\u672a\u6765",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,78,15)"
                        }
                    }
                },
                {
                    "name": "\u5927\u540d\u8f6f\u4ef6",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,79,143)"
                        }
                    }
                },
                {
                    "name": "\u660e\u7565\u79d1\u6280\u96c6\u56e2",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,115,73)"
                        }
                    }
                },
                {
                    "name": "\u84dd\u6e56",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,135,137)"
                        }
                    }
                },
                {
                    "name": "\u5b9d\u5b9d\u6811",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,158,37)"
                        }
                    }
                },
                {
                    "name": "\u6155\u601d\u5065\u5eb7\u7761\u7720",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,121,148)"
                        }
                    }
                },
                {
                    "name": "\u5929\u55bb\u4fe1\u606f",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,102,72)"
                        }
                    }
                },
                {
                    "name": "\u534e\u4e3a\u6280\u672f\u6709\u9650\u516c\u53f8",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,91,69)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u4e1c\u4e09\u7ef4\u5bb6\u4fe1\u606f\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,55,125)"
                        }
                    }
                },
                {
                    "name": "TalkingData",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,128,105)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77\u6cdb\u89c6\u89d2",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,121,147)"
                        }
                    }
                },
                {
                    "name": "\u987a\u4e30\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,114,42)"
                        }
                    }
                },
                {
                    "name": "\u5cb1\u609f\u667a\u80fd",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,140,129)"
                        }
                    }
                },
                {
                    "name": "\u706b\u773c\u4e91",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,135,18)"
                        }
                    }
                },
                {
                    "name": "Roborock",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,67,64)"
                        }
                    }
                },
                {
                    "name": "GYENNO",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,96,77)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u5b8f\u74f4\u79d1\u6280\u53d1\u5c55\u6709\u9650...",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,151,38)"
                        }
                    }
                },
                {
                    "name": "\u7279\u65af\u8054",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,40,67)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77\u6c38\u8f89\u8d85\u5e02\u6709\u9650\u516c\u53f8",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,147,84)"
                        }
                    }
                },
                {
                    "name": "\u5706\u901a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,129,142)"
                        }
                    }
                },
                {
                    "name": "\u9890\u90a6\u79d1\u6280",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,3,79)"
                        }
                    }
                },
                {
                    "name": "\u5c71\u666f\u667a\u80fd",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,62,0)"
                        }
                    }
                },
                {
                    "name": "\u4f2f\u6069\u5149\u5b66",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,16,7)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u6df1\u79d1\u6280",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,90,51)"
                        }
                    }
                },
                {
                    "name": "\u56db\u5408\u5929\u5730",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,17,16)"
                        }
                    }
                },
                {
                    "name": "\u597d\u5927\u592b\u5728\u7ebf",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,153,98)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u6da6\u5bcc\u8054",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,45,21)"
                        }
                    }
                },
                {
                    "name": "\u55b5\u661f\u63a2\u7d22",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,97,46)"
                        }
                    }
                },
                {
                    "name": "\u5916\u8111\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,77,101)"
                        }
                    }
                },
                {
                    "name": "Moka",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,72,138)"
                        }
                    }
                },
                {
                    "name": "\u4eac\u4e1c\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,89,32)"
                        }
                    }
                },
                {
                    "name": "\u827e\u8fc8\u79d1\u65af\u5a92\u4f53\u79d1\u6280\uff08\u5317\u4eac\uff09\u6709\u9650\u516c\u53f8",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,10,123)"
                        }
                    }
                },
                {
                    "name": "\u534e\u5927\u7814\u7a76\u9662",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,96,14)"
                        }
                    }
                },
                {
                    "name": "\u676d\u5dde\u667a\u56e2",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,42,49)"
                        }
                    }
                },
                {
                    "name": "\u8d1d\u58f3",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,48,82)"
                        }
                    }
                },
                {
                    "name": "\u53ee\u549a\u4e70\u83dc",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,107,61)"
                        }
                    }
                },
                {
                    "name": "\u4eb2\u5b9d\u5b9d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,115,5)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u76c8\u745e\u6052",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,1,50)"
                        }
                    }
                },
                {
                    "name": "\u521b\u65b0\u5947\u667a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,48,31)"
                        }
                    }
                },
                {
                    "name": "\u9a6c\u4e0a\u8d62",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,30,1)"
                        }
                    }
                },
                {
                    "name": "\u6d3e\u5ba2\u6734\u98df",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,111,27)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u79d1\u5f18\u4e91",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,66,57)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e4b\u6613",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,76,144)"
                        }
                    }
                },
                {
                    "name": "\u539a\u6734\u6c47\u667a\u54a8\u8be2",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,124,48)"
                        }
                    }
                },
                {
                    "name": "\u6570\u6f9c\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,148,59)"
                        }
                    }
                },
                {
                    "name": "\u6570\u5764\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,22,128)"
                        }
                    }
                },
                {
                    "name": "\u5168\u65f6",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,23,98)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5c1a\u535a\u745e",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,107,54)"
                        }
                    }
                },
                {
                    "name": "\u4f73\u987a\u667a\u80fd\u673a\u5668\u4eba",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,115,127)"
                        }
                    }
                },
                {
                    "name": "\u641c\u624d\u4eba\u529b\u8d44\u6e90",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,52,140)"
                        }
                    }
                },
                {
                    "name": "\u8354\u679d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,41,96)"
                        }
                    }
                },
                {
                    "name": "\u9646\u91d1\u6240",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,112,24)"
                        }
                    }
                },
                {
                    "name": "\u7269\u754c\uff08\u4e0a\u6d77\uff09\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,104,30)"
                        }
                    }
                },
                {
                    "name": "\u6210\u90fd\u62df\u5408\u672a\u6765\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,127,118)"
                        }
                    }
                },
                {
                    "name": "\u6ef4\u666e\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,121,143)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u56fd\u90ae\u653f\u50a8\u84c4\u94f6\u884c",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,71,59)"
                        }
                    }
                },
                {
                    "name": "\u8611\u83c7\u8857",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,141,53)"
                        }
                    }
                },
                {
                    "name": "\u58f0\u667a\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,60,140)"
                        }
                    }
                },
                {
                    "name": "\u54c1\u89c8Pinlan",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,82,117)"
                        }
                    }
                },
                {
                    "name": "\u73e0\u6d77\u4f18\u7279\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,56,83)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u533b\u7597",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,137,79)"
                        }
                    }
                },
                {
                    "name": "\u767e\u878d\u4e91\u521b",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,52,51)"
                        }
                    }
                },
                {
                    "name": "ZOOM",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,73,89)"
                        }
                    }
                },
                {
                    "name": "AKULAKU",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,148,113)"
                        }
                    }
                },
                {
                    "name": "\u58a8\u4e91\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,70,19)"
                        }
                    }
                },
                {
                    "name": "\u6781\u5149",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,155,38)"
                        }
                    }
                },
                {
                    "name": "\u8d5b\u601d\u4fe1\u5b89",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,93,13)"
                        }
                    }
                },
                {
                    "name": "\u89c2\u8fdc\u6570\u636e",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,140,114)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u5c71\u529e\u516c\u8f6f\u4ef6",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,135,65)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u9c7c\u6613\u8fde",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,152,20)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u6d6a\u91d1\u878d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,102,130)"
                        }
                    }
                },
                {
                    "name": "\u601d\u7ef4\u9020\u7269",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,76,31)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u4ea7\u9669",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,8,141)"
                        }
                    }
                },
                {
                    "name": "\u888b\u9f20\u4e91",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,140,103)"
                        }
                    }
                },
                {
                    "name": "\u9cb2\u9e4f\u4e91\u667a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,55,76)"
                        }
                    }
                },
                {
                    "name": "\u835f\u8bda\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,158,71)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6167\u82bd",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,111,23)"
                        }
                    }
                },
                {
                    "name": "\u5143\u6a61\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,131,97)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u77e5\u672a\u6765",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,16,119)"
                        }
                    }
                },
                {
                    "name": "\u6210\u90fd\u4e3b\u5bfc",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,98,63)"
                        }
                    }
                },
                {
                    "name": "westwell\u897f\u4e95\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,103,148)"
                        }
                    }
                },
                {
                    "name": "FunPlus \u8da3\u52a0\u6e38\u620f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,17,143)"
                        }
                    }
                },
                {
                    "name": "\u4e50\u6211\u65e0\u9650",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,22,95)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u97f3\u667a\u80fd\u79d1\u6280  SpeakIn",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,151,124)"
                        }
                    }
                },
                {
                    "name": "\u9cb8\u822a\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,72,89)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u5065\u5eb7",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,76,62)"
                        }
                    }
                },
                {
                    "name": "Disney+Hotstar",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,8,26)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u89c6\u521b\u65b0",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,134,156)"
                        }
                    }
                },
                {
                    "name": "Keep",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,53,136)"
                        }
                    }
                },
                {
                    "name": "\u8304\u5b50\u5feb\u4f20",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,95,126)"
                        }
                    }
                },
                {
                    "name": "vivo",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,142,102)"
                        }
                    }
                },
                {
                    "name": "Rokid",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,19,55)"
                        }
                    }
                },
                {
                    "name": "\u71e7\u4eba\u533b\u7597",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,96,152)"
                        }
                    }
                },
                {
                    "name": "\u5fb7\u9002\u751f\u7269",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,97,147)"
                        }
                    }
                },
                {
                    "name": "LinkDoc",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,3,63)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5927\u701a\u4eba\u529b\u8d44\u6e90\u7ba1\u7406",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,147,132)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u4fe1\u65f6\u4ee3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,24,86)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77\u835f\u529b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,136,104)"
                        }
                    }
                },
                {
                    "name": "\u7c89\u8c61\u751f\u6d3b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,130,50)"
                        }
                    }
                },
                {
                    "name": "BLUE",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,78,156)"
                        }
                    }
                },
                {
                    "name": "\u8389\u8389\u4e1d\u6e38\u620f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,101,135)"
                        }
                    }
                },
                {
                    "name": "\u6e56\u5317\u4e5d\u540c\u65b9\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,37,66)"
                        }
                    }
                },
                {
                    "name": "\u777f\u9b54\u667a\u80fd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,147,79)"
                        }
                    }
                },
                {
                    "name": "\u8da3\u94fe\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,25,21)"
                        }
                    }
                },
                {
                    "name": "\u534e\u6d4b\u5bfc\u822a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,5,35)"
                        }
                    }
                },
                {
                    "name": "\u534e\u91cc\u7f51\u7edc",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,19,75)"
                        }
                    }
                },
                {
                    "name": "\u89e6\u5b9d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,54,100)"
                        }
                    }
                },
                {
                    "name": "\u7ecf\u4f20\u591a\u8d62",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,32,116)"
                        }
                    }
                },
                {
                    "name": "\u8da3\u5934\u6761",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,120,133)"
                        }
                    }
                },
                {
                    "name": "\u7075\u52a8\u97f3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,24,40)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u770b\u6f2b\u753b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,18,92)"
                        }
                    }
                },
                {
                    "name": "\u84dd\u9e3d\u96c6\u56e2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,142,123)"
                        }
                    }
                },
                {
                    "name": "\u817e\u4e91\u60a6\u667a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,136,0)"
                        }
                    }
                },
                {
                    "name": "\u878d360",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,112,146)"
                        }
                    }
                },
                {
                    "name": "\u51e4\u51f0\u7f51",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,130,10)"
                        }
                    }
                },
                {
                    "name": "\u521d\u7075\u4fe1\u606f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,27,81)"
                        }
                    }
                },
                {
                    "name": "\u8206\u9686\u5174\u8fbe",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,147,95)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u5e02\u5a01\u5bcc\u89c6\u754c\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,40,98)"
                        }
                    }
                },
                {
                    "name": "\u6781\u89c6\u89d2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,21,2)"
                        }
                    }
                },
                {
                    "name": "\u6dfb\u624d\u4f01\u4e1a\u7ba1\u7406\u54a8\u8be2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,142,139)"
                        }
                    }
                },
                {
                    "name": "YY",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,158,21)"
                        }
                    }
                },
                {
                    "name": "eBrain",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,13,22)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u67d4\u521b\u65b0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,12,146)"
                        }
                    }
                },
                {
                    "name": "Ximmerse",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,110,21)"
                        }
                    }
                },
                {
                    "name": "\u8ff7\u9e7f\u97f3\u4e50",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,51,119)"
                        }
                    }
                },
                {
                    "name": "\u8c61\u8f91\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,103,108)"
                        }
                    }
                },
                {
                    "name": "\u76db\u4e16\u9e92\u9e9f\u519c\u4e1a\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,122,132)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u8863\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,63,31)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u5dde\u5c0f\u8fc8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,32,65)"
                        }
                    }
                },
                {
                    "name": "nice",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,40,150)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u65b9\u660e\u73e0\u65b0\u5a92\u4f53",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,15,120)"
                        }
                    }
                },
                {
                    "name": "\u8de8\u8d8a\u901f\u8fd0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,123,157)"
                        }
                    }
                },
                {
                    "name": "\u6613\u822a\u667a\u80fd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,62,16)"
                        }
                    }
                },
                {
                    "name": "\u90bb\u6c47\u5427",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,14,51)"
                        }
                    }
                },
                {
                    "name": "LAYABOX",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,13,149)"
                        }
                    }
                },
                {
                    "name": "\u661f\u5c18\u6570\u636e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,49,157)"
                        }
                    }
                },
                {
                    "name": "Uni-Ubi",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,124,28)"
                        }
                    }
                },
                {
                    "name": "StepBeats",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,87,49)"
                        }
                    }
                },
                {
                    "name": "\u6765\u4e5f\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,73,12)"
                        }
                    }
                },
                {
                    "name": "\u65f6\u8da3social-touch",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,13,34)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u90ae\u4fe1\u606f\u79d1\u6280\uff08\u5317\u4eac\uff09\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,114,14)"
                        }
                    }
                },
                {
                    "name": "\u9ea6\u5b50\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,46,146)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u65b0\u6c27\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,142,127)"
                        }
                    }
                },
                {
                    "name": "\u6807\u8d1d\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,16,54)"
                        }
                    }
                },
                {
                    "name": "RealAI",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,155,99)"
                        }
                    }
                },
                {
                    "name": "\u661f\u8206\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,126,71)"
                        }
                    }
                },
                {
                    "name": "\u67cf\u7f8e\u8fea\u5eb7\u4e0a\u6d77",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,110,119)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u6e90\u6052\u9645",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,21,30)"
                        }
                    }
                },
                {
                    "name": "PowerVision",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,23,5)"
                        }
                    }
                },
                {
                    "name": "\u9053\u8fbe\u5929\u9645",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,105,160)"
                        }
                    }
                },
                {
                    "name": "\u6cfd\u97f6\u667a\u80fd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,10,32)"
                        }
                    }
                },
                {
                    "name": "\u6709\u4e3a\u4fe1\u606f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,24,43)"
                        }
                    }
                },
                {
                    "name": "\u572d\u76ee\u673a\u5668\u4eba",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,99,31)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u7684\u96c6\u56e2IT",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,73,58)"
                        }
                    }
                },
                {
                    "name": "\u7d2b\u5149\u6559\u80b2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,21,21)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u7535\u6167\u5b89",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,11,51)"
                        }
                    }
                },
                {
                    "name": "\u534e\u98de\u6570\u636e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,83,18)"
                        }
                    }
                },
                {
                    "name": "\u5151\u5427",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,122,103)"
                        }
                    }
                },
                {
                    "name": "\u89c5\u777f\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,101,55)"
                        }
                    }
                },
                {
                    "name": "Walmart China",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,112,43)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u8bc1\u80a1\u4efd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,106,79)"
                        }
                    }
                },
                {
                    "name": "\u6cf0\u5766\u667a\u6167",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,38,87)"
                        }
                    }
                },
                {
                    "name": "\u6c47\u667a\u4f17\u5fc3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,155,5)"
                        }
                    }
                },
                {
                    "name": "\u534e\u6c49\u4f1f\u4e1a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,157,35)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u65b9\u76db\u884c",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,77,85)"
                        }
                    }
                },
                {
                    "name": "\u638c\u9605",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,109,18)"
                        }
                    }
                },
                {
                    "name": "\u6d3e\u8fe9",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,4,137)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u56fe\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,20,135)"
                        }
                    }
                },
                {
                    "name": "\u54d7\u5566\u5566",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,64,88)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u7f8e\u63a7\u80a1\u96c6\u56e2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,40,97)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u96f6\u8dc3\u52a8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,14,3)"
                        }
                    }
                },
                {
                    "name": "\u7279\u9e4f\u7f51\u7edc",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,86,2)"
                        }
                    }
                },
                {
                    "name": "\u64ce\u76fe\u6570\u636e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,42,104)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u65b9\u548c\u5317\u4eac",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,7,106)"
                        }
                    }
                },
                {
                    "name": "\u6c5f\u884c\u667a\u80fd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,47,60)"
                        }
                    }
                },
                {
                    "name": "\u5408\u5408\u4fe1\u606f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,75,11)"
                        }
                    }
                },
                {
                    "name": "\u89c6+AR",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,91,133)"
                        }
                    }
                },
                {
                    "name": "\u536b\u74f4\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,76,63)"
                        }
                    }
                },
                {
                    "name": "\u5929\u667a\u822a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,158,32)"
                        }
                    }
                },
                {
                    "name": "\u8fc8\u6da6\u667a\u80fd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,34,6)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u5e02\u9510\u660e\u6280\u672f\u80a1\u4efd\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,141,82)"
                        }
                    }
                },
                {
                    "name": "\u6587\u5b89\u667a\u80fd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,58,23)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u8111\u94f6\u6cb3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,67,149)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u65b9\u56fd\u4fe1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,73,133)"
                        }
                    }
                },
                {
                    "name": "\u7b2c\u4e09\u77f3\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,13,144)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u5f71APP",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,70,60)"
                        }
                    }
                },
                {
                    "name": "\u4e5d\u53f7\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,24,148)"
                        }
                    }
                },
                {
                    "name": "\u51cc\u5b87\u667a\u63a7\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,123,140)"
                        }
                    }
                },
                {
                    "name": "Mobvista",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,100,31)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u9910",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,100,117)"
                        }
                    }
                },
                {
                    "name": "\u6613\u6d41",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,38,7)"
                        }
                    }
                },
                {
                    "name": "\u5341\u4e5d\u8857\u4eba\u529b\u8d44\u6e90\u7ba1\u7406",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,132,152)"
                        }
                    }
                },
                {
                    "name": "\u57c3\u6469\u68ee",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,156,77)"
                        }
                    }
                },
                {
                    "name": "\u901f\u611f\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,31,119)"
                        }
                    }
                },
                {
                    "name": "\u97e9\u521b\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,137,158)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u7586\u667a\u80fd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,120,154)"
                        }
                    }
                },
                {
                    "name": "\u676d\u5dde\u9886\u89c1\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,23,103)"
                        }
                    }
                },
                {
                    "name": "\u997f\u4e86\u4e48",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,58,97)"
                        }
                    }
                },
                {
                    "name": "\u817e\u8baf\u97f3\u4e50",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,67,108)"
                        }
                    }
                },
                {
                    "name": "\u661f\u836f\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,113,21)"
                        }
                    }
                },
                {
                    "name": "\u7fcc\u65e5\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,38,66)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u91ce\u91d1\u878d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,65,104)"
                        }
                    }
                },
                {
                    "name": "Long Bridge",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,85,144)"
                        }
                    }
                },
                {
                    "name": "\u5929\u6e90\u8fea\u79d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,71,16)"
                        }
                    }
                },
                {
                    "name": "\u683c\u6717\u5bb6",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,73,92)"
                        }
                    }
                },
                {
                    "name": "\u601d\u56fe\u573a\u666f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,13,40)"
                        }
                    }
                },
                {
                    "name": "\u6653\u6a3e\u667a\u80fd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,97,43)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u539f\u6d88\u8d39\u91d1\u878d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,25,93)"
                        }
                    }
                },
                {
                    "name": "\u5f71\u7b11\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,29,136)"
                        }
                    }
                },
                {
                    "name": "\u56db\u5ddd\u5f18\u548c\u96c6\u56e2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,116,54)"
                        }
                    }
                },
                {
                    "name": "\u6d6a\u6dd8\u91d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,85,32)"
                        }
                    }
                },
                {
                    "name": "\u4e07\u751f\u534e\u6001",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,142,155)"
                        }
                    }
                },
                {
                    "name": "\u6dfb\u624d\u7ff0\u683c",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,140,41)"
                        }
                    }
                },
                {
                    "name": "\u817e\u5c55\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,130,2)"
                        }
                    }
                },
                {
                    "name": "\u8861\u660a\u6570\u636e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,42,64)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u5a31\u65f6\u5149",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,127,141)"
                        }
                    }
                },
                {
                    "name": "\u84dd\u6708\u4eae",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,32,96)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u5c71\u4e16\u6e38",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,128,94)"
                        }
                    }
                },
                {
                    "name": "\u6676\u6cf0\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,123,63)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u5dde\u9ed1\u683c\u667a\u9020\u4fe1\u606f\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,143,68)"
                        }
                    }
                },
                {
                    "name": "\u6700\u6709\u6599",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,63,27)"
                        }
                    }
                },
                {
                    "name": "\u957f\u6295\u5b66\u5802",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,79,3)"
                        }
                    }
                },
                {
                    "name": "\u4f17\u4eab\u5929\u5730",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,123,107)"
                        }
                    }
                },
                {
                    "name": "\u57c3\u514b\u65af\u5de5\u4e1a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,94,121)"
                        }
                    }
                },
                {
                    "name": "\u521b\u90bb\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,10,13)"
                        }
                    }
                },
                {
                    "name": "\u7384\u6b66\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,156,60)"
                        }
                    }
                },
                {
                    "name": "INDEMIND",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,147,142)"
                        }
                    }
                },
                {
                    "name": "\u8eba\u5e73\u8bbe\u8ba1\u5bb6",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,14,147)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u91cf\u8d28\u5b50",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,20,31)"
                        }
                    }
                },
                {
                    "name": "\u65f6\u7a7a\u9053\u5b87",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,19,17)"
                        }
                    }
                },
                {
                    "name": "\u5927\u7bb4\uff08\u676d\u5dde\uff09\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,45,72)"
                        }
                    }
                },
                {
                    "name": "\u534e\u4fe1\u96c6\u56e2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,64,119)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u5e02\u6709\u4f20\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,61,91)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u58f0\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,42,152)"
                        }
                    }
                },
                {
                    "name": "\u677e\u7acb\u63a7\u80a1\u96c6\u56e2\u80a1\u4efd\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,140,5)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u64ad\u7535\u89c6\u7814\u7a76\u6240",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,10,103)"
                        }
                    }
                },
                {
                    "name": "\u4f34\u9c7c",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,47,22)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u901a\u5feb\u9012",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,78,126)"
                        }
                    }
                },
                {
                    "name": "\u886b\u6570\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,59,20)"
                        }
                    }
                },
                {
                    "name": "\u521b\u6cf0\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,44,54)"
                        }
                    }
                },
                {
                    "name": "\u53ca\u672a\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,116,51)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5e0c\u671b\u516d\u548c",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,44,69)"
                        }
                    }
                },
                {
                    "name": "\u8d5b\u9c81\u73ed",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,91,16)"
                        }
                    }
                },
                {
                    "name": "\u9f99\u6e56\u96c6\u56e2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,19,110)"
                        }
                    }
                },
                {
                    "name": "\u7d2b\u8346\u6843\u674e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,18,16)"
                        }
                    }
                },
                {
                    "name": "\u7d2b\u5149\u534e\u667a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,146,1)"
                        }
                    }
                },
                {
                    "name": "\u8fc1\u79fb\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,26,84)"
                        }
                    }
                },
                {
                    "name": "\u683c\u5170\u4ed5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,129,32)"
                        }
                    }
                },
                {
                    "name": "\u7279\u8d5e|Tezign",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,12,13)"
                        }
                    }
                },
                {
                    "name": "Flash express",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,2,95)"
                        }
                    }
                },
                {
                    "name": "\u601d\u8d24\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,122,30)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u6cf0\u661f\u4e91",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,51,80)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u8ff9\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,147,54)"
                        }
                    }
                },
                {
                    "name": "\u73cd\u7231\u7f51",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,94,56)"
                        }
                    }
                },
                {
                    "name": "\u8bc1\u901a\u7535\u5b50",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,57,104)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u5965\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,131,153)"
                        }
                    }
                },
                {
                    "name": "Sigmob",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,123,101)"
                        }
                    }
                },
                {
                    "name": "\u521b\u5fc5\u627f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,36,137)"
                        }
                    }
                },
                {
                    "name": "\u7231\u7acb\u5eb7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,75,54)"
                        }
                    }
                },
                {
                    "name": "\u4e3a\u534e\u7f51\u7edc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,58,77)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u7ea7\u7329\u7329\u5065\u8eab",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,110,159)"
                        }
                    }
                },
                {
                    "name": "\u9b54\u98de\u7f51\u7edc-\u8f66\u8f7d\u5a31\u4e50",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,9,158)"
                        }
                    }
                },
                {
                    "name": "\u84dd\u706f\u9c7c\u667a\u80fd\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,108,35)"
                        }
                    }
                },
                {
                    "name": "\u9038\u4eab\u7535\u5b50\u5546\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,56,67)"
                        }
                    }
                },
                {
                    "name": "\u963f\u91cc\u5df4\u5df4-\u9ad8\u5fb7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,21,106)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u839e\u7f8e\u5b9c\u4f73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,11,118)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77\u5594\u8da3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,61,43)"
                        }
                    }
                },
                {
                    "name": "\u8da3\u4e38",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,2,106)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u534e\u7814\u7a76\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,73,17)"
                        }
                    }
                },
                {
                    "name": "\u534e\u4e91\u4e2d\u76db",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,134,131)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u5f99\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,131,32)"
                        }
                    }
                },
                {
                    "name": "\u8f7b\u8f7b\u6559\u80b2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,109,113)"
                        }
                    }
                },
                {
                    "name": "\u7545\u804a\u5929\u4e0b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,138,10)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u7535\u79d1\u98ce\u534e\u4fe1\u606f\u88c5\u5907\u80a1\u4efd\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,155,146)"
                        }
                    }
                },
                {
                    "name": "\u4e07\u5174\u79d1\u6280\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,20,36)"
                        }
                    }
                },
                {
                    "name": "\u535a\u4f9d\u7279",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,147,4)"
                        }
                    }
                },
                {
                    "name": "\u6cf0\u5eb7\u4fdd\u9669\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,127,51)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5eb7\u5a01\u89c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,27,86)"
                        }
                    }
                },
                {
                    "name": "\u7279\u65af\u62c9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,37,39)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u4e50\u79cd\u5b50",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,19,144)"
                        }
                    }
                },
                {
                    "name": "\u963f\u91cc\u5df4\u5df4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,68,85)"
                        }
                    }
                },
                {
                    "name": "\u667a\u8f85\u7279\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,47,46)"
                        }
                    }
                },
                {
                    "name": "\u5353\u725b\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,141,118)"
                        }
                    }
                },
                {
                    "name": "Riley Cillian\u83b1\u7199\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,34,102)"
                        }
                    }
                },
                {
                    "name": "\u6613\u79d1\u5947\u901a\u4fe1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,106,121)"
                        }
                    }
                },
                {
                    "name": "\u5927\u519c\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,12,129)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77\u91d1\u5927\u5e08\u7f51\u7edc\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,143,70)"
                        }
                    }
                },
                {
                    "name": "\u6676\u786e\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,15,40)"
                        }
                    }
                },
                {
                    "name": "\u8baf\u6c47\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,44,7)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u83dc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,85,101)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u6f14\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,154,79)"
                        }
                    }
                },
                {
                    "name": "\u8054\u6613\u878dlinklogis",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,10,128)"
                        }
                    }
                },
                {
                    "name": "\u90a6\u5b9a\u667a\u6167",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,142,57)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u521b\u661f\u7a7a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,130,0)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u949b\u673a\u5668\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,69,112)"
                        }
                    }
                },
                {
                    "name": "\u5353\u671b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,159,62)"
                        }
                    }
                },
                {
                    "name": "\u878d\u6613\u63a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,147,87)"
                        }
                    }
                },
                {
                    "name": "\u770b\u623f\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,146,131)"
                        }
                    }
                },
                {
                    "name": "\u711c\u8000\u7f51\u7edc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,71,116)"
                        }
                    }
                },
                {
                    "name": "\u63a2\u9488\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,129,64)"
                        }
                    }
                },
                {
                    "name": "\u767e\u7ef4\u91d1\u79d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,10,6)"
                        }
                    }
                },
                {
                    "name": "\u5c0fi\u673a\u5668\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,73,118)"
                        }
                    }
                },
                {
                    "name": "\u592a\u5b57\u6d41\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,90,17)"
                        }
                    }
                },
                {
                    "name": "\u5915\u5915\u65f6\u4ee3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,128,52)"
                        }
                    }
                },
                {
                    "name": "\u55b5\u67da\u7f51\u7edc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,102,143)"
                        }
                    }
                },
                {
                    "name": "\u9884\u7b56\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,156,105)"
                        }
                    }
                },
                {
                    "name": "MetaApp",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,36,12)"
                        }
                    }
                },
                {
                    "name": "\u5341\u835f\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,117,148)"
                        }
                    }
                },
                {
                    "name": "\u535a\u5353\u4f01\u4e1a\u7ba1\u7406\u54a8\u8be2\u670d\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,49,149)"
                        }
                    }
                },
                {
                    "name": "\u6f2b\u5fae\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,142,108)"
                        }
                    }
                },
                {
                    "name": "Xeno Dynamics",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,76,51)"
                        }
                    }
                },
                {
                    "name": "\u767e\u70bc\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,16,55)"
                        }
                    }
                },
                {
                    "name": "\u9cb8\u7b97\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,92,110)"
                        }
                    }
                },
                {
                    "name": "\u667a\u610f\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,29,28)"
                        }
                    }
                },
                {
                    "name": "\u6211\u7231\u6211\u5bb6\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,49,150)"
                        }
                    }
                },
                {
                    "name": "\u65b9\u4ed5\u8fbe\u4f01\u4e1a\u7ba1\u7406\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,88,158)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u5370\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,100,116)"
                        }
                    }
                },
                {
                    "name": "\u8f66\u597d\u591a\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,55,44)"
                        }
                    }
                },
                {
                    "name": "\u5219\u4e00\u4f9b\u5e94\u94fe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,10,95)"
                        }
                    }
                },
                {
                    "name": "Micagent",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,136,15)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5965\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,97,7)"
                        }
                    }
                },
                {
                    "name": "\u5a31\u516c\u4e92\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,27,42)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u5e02\u865a\u62df\u73b0\u5b9e\u6280\u672f\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,22,59)"
                        }
                    }
                },
                {
                    "name": "\u96f7\u5ea6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,60,149)"
                        }
                    }
                },
                {
                    "name": "\u6c49\u4eea\u5b57\u5e93",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,131,125)"
                        }
                    }
                },
                {
                    "name": "\u8054\u901a\u4e91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,40,17)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u8c61\u4f18\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,0,63)"
                        }
                    }
                },
                {
                    "name": "\u701a\u4ed5\u8fbe\u4eba\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,33,88)"
                        }
                    }
                },
                {
                    "name": "\u9e4f\u5143\u5f81\u4fe1\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,110,147)"
                        }
                    }
                },
                {
                    "name": "\u8d1d\u601d\u79d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,43,132)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u667a\u6e90\u4eba\u5de5\u667a\u80fd\u7814\u7a76\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,147,46)"
                        }
                    }
                },
                {
                    "name": "\u6ef4\u6ef4\u4f18\u70b9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,81,0)"
                        }
                    }
                },
                {
                    "name": "\u6bcf\u65e5\u4f18\u9c9c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,82,6)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u777f\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,92,145)"
                        }
                    }
                },
                {
                    "name": "\u638c\u4e0a\u5148\u673a-\u65fa\u5e97\u901aERP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,93,122)"
                        }
                    }
                },
                {
                    "name": "Kika Tech(\u65b0\u7f8e\u4e92\u901a)",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,100,45)"
                        }
                    }
                },
                {
                    "name": "\u5b8f\u7131\u7f51\u7edc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,120,11)"
                        }
                    }
                },
                {
                    "name": "\u4f5c\u4e1a\u5e2e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,28,73)"
                        }
                    }
                },
                {
                    "name": "\u660e\u671d\u4e07\u8fbe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,93,144)"
                        }
                    }
                },
                {
                    "name": "iSpeak",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,9,130)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u79d1\u4e16\u901a\u4ea8\u5947",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,30,73)"
                        }
                    }
                },
                {
                    "name": "\u6cf0\u5c14\u80a1\u4efd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,115,45)"
                        }
                    }
                },
                {
                    "name": "\u9752\u56e2\u793e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,46,149)"
                        }
                    }
                },
                {
                    "name": "\u6e05\u534e\u540c\u65b9\u7269\u8054\u7f51\u672c\u90e8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,155,20)"
                        }
                    }
                },
                {
                    "name": "\u5a5a\u793c\u7eaa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,78,46)"
                        }
                    }
                },
                {
                    "name": "\u8c6a\u732a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,60,10)"
                        }
                    }
                },
                {
                    "name": "\u864e\u7259\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,19,9)"
                        }
                    }
                },
                {
                    "name": "\u73de\u73c8\u4f17\u6052",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,57,146)"
                        }
                    }
                },
                {
                    "name": "\u8d5b\u5427\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,51,55)"
                        }
                    }
                },
                {
                    "name": "\u5bd3\u8a00\u901a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,159,156)"
                        }
                    }
                },
                {
                    "name": "WeLab\u536b\u76c8\u8054",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,152,13)"
                        }
                    }
                },
                {
                    "name": "Trusfort\u82af\u76fe\u65f6\u4ee3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,117,138)"
                        }
                    }
                },
                {
                    "name": "roobo",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,70,124)"
                        }
                    }
                },
                {
                    "name": "\u9cb8\u6984\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,134,106)"
                        }
                    }
                },
                {
                    "name": "\u6cf0\u5eb7\u5728\u7ebf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,147,146)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u9f9f\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,122,139)"
                        }
                    }
                },
                {
                    "name": "\u8fde\u4fe1\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,61,25)"
                        }
                    }
                },
                {
                    "name": "\u897f\u6e56\u5927\u5b66\u667a\u80fd\u4ea7\u4e1a\u7814\u7a76\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,92,129)"
                        }
                    }
                },
                {
                    "name": "\u667a\u8d1d\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,152,43)"
                        }
                    }
                },
                {
                    "name": "\u5927\u4e13\u5bb6.COM",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,39,67)"
                        }
                    }
                },
                {
                    "name": "\u7eff\u6f2b\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,73,85)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u6717\u9053\u667a\u901a\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,17,113)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u5e02\u667a\u80fd\u5236\u9020\u8f6f\u4ef6\u5f00\u53d1\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,60,105)"
                        }
                    }
                },
                {
                    "name": "GALASPORTS",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,133,97)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u8054\u82f1\u8bed",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,81,65)"
                        }
                    }
                },
                {
                    "name": "\u4e16\u7eaa\u4f73\u7f18",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,27,148)"
                        }
                    }
                },
                {
                    "name": "\u71b5\u7b80\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,123,95)"
                        }
                    }
                },
                {
                    "name": "\u5b9d\u5c0a\u7535\u5546",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,77,0)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u91d1\u8bc1\u5238",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,99,24)"
                        }
                    }
                },
                {
                    "name": "Mai",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,101,153)"
                        }
                    }
                },
                {
                    "name": "\u4e50\u5176\u7535\u5546",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,49,103)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u79d1\u667a\u52a0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,93,39)"
                        }
                    }
                },
                {
                    "name": "\u534e\u783a\u667a\u884c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,121,82)"
                        }
                    }
                },
                {
                    "name": "\u61d2\u4eba\u7545\u542c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,88,80)"
                        }
                    }
                },
                {
                    "name": "\u730e\u6237\u661f\u7a7a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,30,29)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u8d62\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,151,24)"
                        }
                    }
                },
                {
                    "name": "\u8def\u884c\u901a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,26,4)"
                        }
                    }
                },
                {
                    "name": "\u4e5d\u7ae0\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,110,4)"
                        }
                    }
                },
                {
                    "name": "\u9c81\u73ed\u5ae1\u7cfb\u673a\u5668\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,31,152)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u7535\u535a\u4e9a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,9,68)"
                        }
                    }
                },
                {
                    "name": "\u7545\u6377\u901a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,58,150)"
                        }
                    }
                },
                {
                    "name": "\u8ffd\u52bf\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,54,4)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u6d4e\u533b\u7597",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,47,87)"
                        }
                    }
                },
                {
                    "name": "\u8d28\u5b50\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,86,20)"
                        }
                    }
                },
                {
                    "name": "\u5341\u624d\u730e\u5934",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,35,31)"
                        }
                    }
                },
                {
                    "name": "\u7535\u9cb8\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,91,63)"
                        }
                    }
                },
                {
                    "name": "\u4f9d\u777f\u8fea\u4e9a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,79,132)"
                        }
                    }
                },
                {
                    "name": "\u7ea2\u84ddCP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,105,40)"
                        }
                    }
                },
                {
                    "name": "Camera360",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,10,15)"
                        }
                    }
                },
                {
                    "name": "\u540d\u7af9\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,115,88)"
                        }
                    }
                },
                {
                    "name": "\u96c5\u65af\u59ae",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,42,12)"
                        }
                    }
                },
                {
                    "name": "\u667a\u4e91\u5065\u5eb7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,37,56)"
                        }
                    }
                },
                {
                    "name": "\u8682\u8681\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,106,40)"
                        }
                    }
                },
                {
                    "name": "\u6613\u5c45\u4e2d\u56fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,107,27)"
                        }
                    }
                },
                {
                    "name": "\u6c38\u8f89\u4e91\u521b\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,132,14)"
                        }
                    }
                },
                {
                    "name": "\u767b\u8679",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,49,57)"
                        }
                    }
                },
                {
                    "name": "\u81f3\u771f\u4e92\u8054",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,39,110)"
                        }
                    }
                },
                {
                    "name": "Stepone",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,82,99)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u4e4e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,124,16)"
                        }
                    }
                },
                {
                    "name": "KLOOK \u5ba2\u8def\u65c5\u884c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,106,35)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u4e03\u4e92\u5a31",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,23,61)"
                        }
                    }
                },
                {
                    "name": "\u8054\u901a\u65f6\u79d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,138,150)"
                        }
                    }
                },
                {
                    "name": "\u667a\u795e\u4fe1\u606f\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,127,2)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u4e1c\u5e7f\u4fe1\u901a\u4fe1\u670d\u52a1\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,97,79)"
                        }
                    }
                },
                {
                    "name": "\u7280\u8bed\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,13,25)"
                        }
                    }
                },
                {
                    "name": "Yeahmobi",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,121,79)"
                        }
                    }
                },
                {
                    "name": "\u5047\u9762\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,127,134)"
                        }
                    }
                },
                {
                    "name": "\u6cb3\u5317\u6625\u6cfd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,132,160)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u9510\u56fd\u9645",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,147,68)"
                        }
                    }
                },
                {
                    "name": "\u540c\u82b1\u987a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,50,113)"
                        }
                    }
                },
                {
                    "name": "Lazada",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,105,24)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u94f6\u884c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,2,2)"
                        }
                    }
                },
                {
                    "name": "\u540c\u4e3a\u6570\u7801",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,116,73)"
                        }
                    }
                },
                {
                    "name": "\u6708\u76db\u658b\u6295\u8d44\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,129,55)"
                        }
                    }
                },
                {
                    "name": "FREE BRIO",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,56,89)"
                        }
                    }
                },
                {
                    "name": "AfterShip",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,135,130)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5723\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,70,151)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u5065\u5eb7\u4fdd\u9669",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,2,49)"
                        }
                    }
                },
                {
                    "name": "\u827e\u8015\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,19,3)"
                        }
                    }
                },
                {
                    "name": "\u96ea\u8c79\u9ad8\u79d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,56,111)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u7280\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,41,160)"
                        }
                    }
                },
                {
                    "name": "\u6e05\u534e\u5927\u5b66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,144,97)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u901a\u8f6f\u4ef6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,23,58)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u5168\u751f\u4ea7\u79d1\u5b66\u7814\u7a76\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,155,36)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u7ea2\u4e66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,42,111)"
                        }
                    }
                },
                {
                    "name": "\u4f9d\u56fe\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,145,18)"
                        }
                    }
                },
                {
                    "name": "InMobi",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,59,25)"
                        }
                    }
                },
                {
                    "name": "\u7ef4\u4fe1\u91d1\u79d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,141,61)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u70b9\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,52,12)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u516b\u7ef4\u7814\u4fee\u5b66\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,83,118)"
                        }
                    }
                },
                {
                    "name": "\u70ed\u4e91\u6570\u636e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,24,65)"
                        }
                    }
                },
                {
                    "name": "\u5357\u5a01\u8f6f\u4ef6\u80a1\u4efd\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,7,131)"
                        }
                    }
                },
                {
                    "name": "\u6da6\u5efa\u80a1\u4efd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,40,96)"
                        }
                    }
                },
                {
                    "name": "\u6167\u62e9\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,13,105)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u777f\u533b\u7597",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,112,159)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u6728\u667a\u80fd\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,9,50)"
                        }
                    }
                },
                {
                    "name": "\u6570\u5b57\u4ea7\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,86,13)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u91cd\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,98,143)"
                        }
                    }
                },
                {
                    "name": "\u6a59\u5b50\u6570\u5b57\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,65,73)"
                        }
                    }
                },
                {
                    "name": "\u661f\u9645\u5927\u9646",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,31,33)"
                        }
                    }
                },
                {
                    "name": "Nox\u591c\u795e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,6,53)"
                        }
                    }
                },
                {
                    "name": "\u503c\u5f97\u4e70\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,50,35)"
                        }
                    }
                },
                {
                    "name": "\u6155\u8bfe\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,82,58)"
                        }
                    }
                },
                {
                    "name": "\u667a\u751f\u9053\u4eba\u624d\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,55,137)"
                        }
                    }
                },
                {
                    "name": "\u51b0\u6cb3\u4e91\u5b58\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,8,100)"
                        }
                    }
                },
                {
                    "name": "\u76ca\u76df\u64cd\u76d8\u624b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,108,116)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u9ad8\u63a7\u80a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,94,54)"
                        }
                    }
                },
                {
                    "name": "\u82cf\u7f19\u4f01\u4e1a\u7ba1\u7406\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,8,58)"
                        }
                    }
                },
                {
                    "name": "\u7aef\u70c1\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,51,154)"
                        }
                    }
                },
                {
                    "name": "\u6e05\u51cc\u6587\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,45,105)"
                        }
                    }
                },
                {
                    "name": "\u987a\u4e30\u540c\u57ce",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,48,50)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u8fbe\u8f6f\u4ef6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,157,57)"
                        }
                    }
                },
                {
                    "name": "\u660e\u4e4b\u6570\u636e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,37,74)"
                        }
                    }
                },
                {
                    "name": "\u6cf0\u5eb7\u4eba\u5bff",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,47,85)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u987e\u4eba\u529b\u8d44\u6e90",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,64,56)"
                        }
                    }
                },
                {
                    "name": "\u949b\u6c2a\u65b0\u5a92\u4f53\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,34,118)"
                        }
                    }
                },
                {
                    "name": "\u777f\u8c61\u4e91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,108,10)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6167\u732b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,158,105)"
                        }
                    }
                },
                {
                    "name": "\u76ef\u76ef\u62cd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,73,118)"
                        }
                    }
                },
                {
                    "name": "\u524d\u6d77\u4e91\u4e1c\u5bb6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,9,52)"
                        }
                    }
                },
                {
                    "name": "\u827e\u5fb7\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,34,141)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u5e93\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,91,95)"
                        }
                    }
                },
                {
                    "name": "\u60e0\u84c9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,103,56)"
                        }
                    }
                },
                {
                    "name": "\u6210\u90fd\u5927\u6570\u636e\u4ea7\u4e1a\u6280\u672f\u7814\u7a76\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,139,45)"
                        }
                    }
                },
                {
                    "name": "Anker",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,107,25)"
                        }
                    }
                },
                {
                    "name": "\u6210\u90fd\u8086\u96f6\u8086",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,77,137)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u5173\u6751\u6613\u521b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,48,120)"
                        }
                    }
                },
                {
                    "name": "\u963f\u91cc\u4e92\u52a8\u5a31\u4e50\u4e8b\u4e1a\u7fa4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,34,44)"
                        }
                    }
                },
                {
                    "name": "\u542c\u4e91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,54,15)"
                        }
                    }
                },
                {
                    "name": "\u9e70\u4e4b\u773c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,2,109)"
                        }
                    }
                },
                {
                    "name": "\u745b\u592a\u83b1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,19,130)"
                        }
                    }
                },
                {
                    "name": "\u79cd\u68a6\u5ba2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,143,62)"
                        }
                    }
                },
                {
                    "name": "\u597d\u672a\u6765",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,45,131)"
                        }
                    }
                },
                {
                    "name": "\u6570\u777f\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,53,48)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u79d8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,93,7)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u56fd\u77f3\u6cb9\u5929\u7136\u6c14\u7ba1\u9053\u5de5\u7a0b\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,48,70)"
                        }
                    }
                },
                {
                    "name": "\u6c47\u4fe1\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,160,103)"
                        }
                    }
                },
                {
                    "name": "\u8d2d\u7269\u515a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,55,6)"
                        }
                    }
                },
                {
                    "name": "\u987a\u4e30\u56fd\u9645",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,129,127)"
                        }
                    }
                },
                {
                    "name": "\u63a2\u9a6c\u4f01\u670d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,25,56)"
                        }
                    }
                },
                {
                    "name": "\u73af\u7403\u8f66\u4eab",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,139,63)"
                        }
                    }
                },
                {
                    "name": "\u6930\u5b50\u4f20\u5a92",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,43,64)"
                        }
                    }
                },
                {
                    "name": "\u4ebf\u8058\u4e16\u7eaa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,115,87)"
                        }
                    }
                },
                {
                    "name": "\u6b66\u6c49\u8fea\u8d5b\u5a01\u667a\u80fd\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,5,27)"
                        }
                    }
                },
                {
                    "name": "\u6f8e\u601d\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,50,65)"
                        }
                    }
                },
                {
                    "name": "\u623f\u8f66\u5b9d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,12,129)"
                        }
                    }
                },
                {
                    "name": "\u592a\u5e73\u6d0b\u623f\u5730\u4ea7\u7ecf\u7eaa\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,71,138)"
                        }
                    }
                },
                {
                    "name": "\u9518\u5d34\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,132,11)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u8f6f\uff08\u4e2d\u56fd\uff09\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,61,144)"
                        }
                    }
                },
                {
                    "name": "\u662f\u5fb7\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,3,116)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u8bed",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,154,128)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u8bc1\u5238",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,75,138)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u6cf0\u4ea7\u9669",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,130,25)"
                        }
                    }
                },
                {
                    "name": "Shopee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,159,133)"
                        }
                    }
                },
                {
                    "name": "\u96ea\u7403",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,85,127)"
                        }
                    }
                },
                {
                    "name": "\u878d\u4e3a\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,32,93)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u6b65\u5728\u5bb6\u65e9\u6559",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,108,60)"
                        }
                    }
                },
                {
                    "name": "\u5343\u91cc\u773c\u7ba1\u7406\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,15,11)"
                        }
                    }
                },
                {
                    "name": "\u5f53\u5f53\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,112,9)"
                        }
                    }
                },
                {
                    "name": "\u5495\u549a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,92,47)"
                        }
                    }
                },
                {
                    "name": "\u96c5\u4e50\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,94,78)"
                        }
                    }
                },
                {
                    "name": "\u751f\u547d\u5947\u70b9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,153,17)"
                        }
                    }
                },
                {
                    "name": "\u72ee\u6865\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,90,4)"
                        }
                    }
                },
                {
                    "name": "\u8c46\u679c\u7f8e\u98df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,26,113)"
                        }
                    }
                },
                {
                    "name": "\u827e\u7f8e\u7f51\u7edc\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,21,44)"
                        }
                    }
                },
                {
                    "name": "\u8c61\u5fc3\u529b\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,104,59)"
                        }
                    }
                },
                {
                    "name": "\u5c11\u5e74\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,159,100)"
                        }
                    }
                },
                {
                    "name": "\u8da3\u9014\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,25,46)"
                        }
                    }
                },
                {
                    "name": "\u534e\u5f55\u8d85\u6e05\u6587\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,11,120)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77\u745e\u72ee\u7f51\u7edc\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,142,95)"
                        }
                    }
                },
                {
                    "name": "\u5929\u6cfd\u667a\u4e91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,32,3)"
                        }
                    }
                },
                {
                    "name": "e\u7b7e\u5b9d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,3,63)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u70b9\u8d44\u8baf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,72,32)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u667a\u7c73\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,148,78)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u5219\u4f18",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,127,68)"
                        }
                    }
                },
                {
                    "name": "\u73af\u7403\u7f51\u6821",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,105,23)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u72d7\u6253\u8f66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,61,96)"
                        }
                    }
                },
                {
                    "name": "\u82f1\u8bed\u8da3\u914d\u97f3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,153,48)"
                        }
                    }
                },
                {
                    "name": "\u4e45\u90a6GOMO",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,46,55)"
                        }
                    }
                },
                {
                    "name": "\u5e93\u73c0\u6052\u5b89",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,80,114)"
                        }
                    }
                },
                {
                    "name": "\u4f0a\u6fb3\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,105,62)"
                        }
                    }
                },
                {
                    "name": "\u5357\u4eac\u6c47\u5ddd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,90,111)"
                        }
                    }
                },
                {
                    "name": "\u9b54\u7b77\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,144,37)"
                        }
                    }
                },
                {
                    "name": "\u6781\u777f\u533b\u7597",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,55,90)"
                        }
                    }
                },
                {
                    "name": "\u8f7b\u677e\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,74,77)"
                        }
                    }
                },
                {
                    "name": "\u5a01\u661f\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,107,44)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u6444",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,8,130)"
                        }
                    }
                },
                {
                    "name": "\u7d2b\u71d5\u65e0\u4eba\u98de\u884c\u5668",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,71,80)"
                        }
                    }
                },
                {
                    "name": "\u5fb7\u805a\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,42,132)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u79d1\u777f\u89c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,94,132)"
                        }
                    }
                },
                {
                    "name": "\u548c\u7f8e\u4fe1\u606f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,156,48)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u7814\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,71,13)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u60f3\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,91,7)"
                        }
                    }
                },
                {
                    "name": "\u84dd\u8bfa\u5fae\u94f6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,36,154)"
                        }
                    }
                },
                {
                    "name": "deepcam",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,13,3)"
                        }
                    }
                },
                {
                    "name": "\u9752\u5cb3\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,159,58)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u9536\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,38,159)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u7535",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,103,143)"
                        }
                    }
                },
                {
                    "name": "\u4f20\u5174\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,34,159)"
                        }
                    }
                },
                {
                    "name": "\u6210\u90fd\u8d28\u6570\u65af\u8fbe\u514b\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,88,102)"
                        }
                    }
                },
                {
                    "name": "\u53f8\u5357\u6570\u636e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,91,44)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u5929\u52b1\u98de",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,18,93)"
                        }
                    }
                },
                {
                    "name": "\u6253\u626e\u5bb6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,62,64)"
                        }
                    }
                },
                {
                    "name": "\u6c85\u9038\u65b9\u8fbe\u7ba1\u7406\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,123,119)"
                        }
                    }
                },
                {
                    "name": "\u5373\u523b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,18,30)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u7280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,6,26)"
                        }
                    }
                },
                {
                    "name": "\u5531\u5427-\u73a9\u97f3\u4e50\uff0c\u5c31\u4e0a\u5531\u5427\uff01",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,72,110)"
                        }
                    }
                },
                {
                    "name": "\u51ef\u53d4\u8bb2\u6545\u4e8b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,29,92)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u79df\u8d41",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,122,108)"
                        }
                    }
                },
                {
                    "name": "\u7384\u5173\u5065\u5eb7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,43,132)"
                        }
                    }
                },
                {
                    "name": "\u95ea\u5e03\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,36,101)"
                        }
                    }
                },
                {
                    "name": "AutoX",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,123,25)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u7ec7\u7b97\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,131,21)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u535a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,151,9)"
                        }
                    }
                },
                {
                    "name": "\u4e70\u4e70\u53cb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,148,81)"
                        }
                    }
                },
                {
                    "name": "\u6c47\u82f1\u8fbe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,159,10)"
                        }
                    }
                },
                {
                    "name": "\u540c\u6e29\u5c42",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,51,94)"
                        }
                    }
                },
                {
                    "name": "Gridsum \u56fd\u53cc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,140,7)"
                        }
                    }
                },
                {
                    "name": "\u8d1d\u53f6\u65af\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,136,155)"
                        }
                    }
                },
                {
                    "name": "\u7ec7\u70b9\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,63,75)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u987f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,136,25)"
                        }
                    }
                },
                {
                    "name": "\u6469\u822a\u65f6\u4ee3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,122,113)"
                        }
                    }
                },
                {
                    "name": "\u6444\u661f\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,86,53)"
                        }
                    }
                },
                {
                    "name": "\u8001\u864e\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,11,144)"
                        }
                    }
                },
                {
                    "name": "\u822a\u7a7a\u5927\u90fd\u5e02\u7814\u7a76\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,123,55)"
                        }
                    }
                },
                {
                    "name": "\u5965\u7279\u7ef4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,64,131)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u79d1\u805a\u4fe1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,157,138)"
                        }
                    }
                },
                {
                    "name": "\u6765\u56de\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,135,85)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u89c8\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,140,54)"
                        }
                    }
                },
                {
                    "name": "\u60e0\u5408",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,139,157)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u5f84\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,5,112)"
                        }
                    }
                },
                {
                    "name": "\u963f\u5361\u7d22\u5916\u6559\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,150,73)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u4e07\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,45,139)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5c14\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,140,140)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u9886\u4eba\u624d\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,4,126)"
                        }
                    }
                },
                {
                    "name": "\u7c73\u96c5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,38,129)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u4e1a\u989c\u7a76\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,157,38)"
                        }
                    }
                },
                {
                    "name": "\u65b9\u6b63\u624b\u8ff9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,115,42)"
                        }
                    }
                },
                {
                    "name": "\u8d5b\u8235\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,58,127)"
                        }
                    }
                },
                {
                    "name": "\u8682\u8681\u805a\u5b9d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,82,126)"
                        }
                    }
                },
                {
                    "name": "\u8fdc\u7738\u8f6f\u4ef6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,147,22)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u540c\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,1,154)"
                        }
                    }
                },
                {
                    "name": "\u6613\u9274\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,117,69)"
                        }
                    }
                },
                {
                    "name": "\u540c\u76fe\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,60,60)"
                        }
                    }
                },
                {
                    "name": "\u5317\u660e\u6570\u79d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,160,91)"
                        }
                    }
                },
                {
                    "name": "\u76c8\u4f73\u4fe1\u8054",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,124,131)"
                        }
                    }
                },
                {
                    "name": "\u4f73\u5146\u4e1a\u6295\u8d44\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,122,95)"
                        }
                    }
                },
                {
                    "name": "\u7545\u884c\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,3,93)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u4e91\u5929\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,29,19)"
                        }
                    }
                },
                {
                    "name": "\u5370\u8c61\u7b14\u8bb0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,81,115)"
                        }
                    }
                },
                {
                    "name": "\u8d62\u706b\u866b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,151,25)"
                        }
                    }
                },
                {
                    "name": "\u591a\u70b9\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,20,5)"
                        }
                    }
                },
                {
                    "name": "\u745e\u5a01\u76db",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,131,18)"
                        }
                    }
                },
                {
                    "name": "\u5373\u6784\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,120,95)"
                        }
                    }
                },
                {
                    "name": "\u8fc8\u7279\u56fd\u9645\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,150,83)"
                        }
                    }
                },
                {
                    "name": "\u8bfa\u535a\u533b\u7597",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,119,44)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u5e2e\u7535\u5b50",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,106,14)"
                        }
                    }
                },
                {
                    "name": "\u797a\u9cb8\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,117,70)"
                        }
                    }
                },
                {
                    "name": "\u592a\u521d\u5f08\u5baa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,128,16)"
                        }
                    }
                },
                {
                    "name": "\u5bfa\u5e93",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,67,30)"
                        }
                    }
                },
                {
                    "name": "\u9014\u864e\u517b\u8f66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,47,99)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u5730\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,99,58)"
                        }
                    }
                },
                {
                    "name": "\u82ac\u4ee5\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,135,94)"
                        }
                    }
                },
                {
                    "name": "\u7c73\u7edc\u661f\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,132,16)"
                        }
                    }
                },
                {
                    "name": "\u732b\u773c\u7535\u5f71",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,28,27)"
                        }
                    }
                },
                {
                    "name": "\u5343\u5bfb\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,83,123)"
                        }
                    }
                },
                {
                    "name": "\u5988\u5988\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,2,27)"
                        }
                    }
                },
                {
                    "name": "Udesk\uff0d\u4f01\u4e1a\u7ea7\u667a\u80fd\u5ba2\u670d\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,160,5)"
                        }
                    }
                },
                {
                    "name": "\u535a\u5f66\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,78,70)"
                        }
                    }
                },
                {
                    "name": "\u667a\u9f7f\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,106,32)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u6b65\u7f51\u7edc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,48,89)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u5dde\u7075\u611f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,26,86)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u6269\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,12,83)"
                        }
                    }
                },
                {
                    "name": "\u7a0e\u53cb\u8f6f\u4ef6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,44,28)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u79ef\u4e92\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,117,102)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u8003\u76f4\u901a\u8f66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,48,38)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u6c11\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,25,61)"
                        }
                    }
                },
                {
                    "name": "\u8054\u8fd0\u77e5\u6167\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,24,58)"
                        }
                    }
                },
                {
                    "name": "\u672a\u6765\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,77,51)"
                        }
                    }
                },
                {
                    "name": "\u5357\u74dc\u7535\u5f71",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,40,34)"
                        }
                    }
                },
                {
                    "name": "\u4f0a\u5bf9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,55,24)"
                        }
                    }
                },
                {
                    "name": "\u8f6f\u725b\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,55,25)"
                        }
                    }
                },
                {
                    "name": "\u9a6c\u8702\u7a9d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,38,97)"
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
                "\u6ef4\u6ef4",
                "\u9177\u72d7\u97f3\u4e50",
                "\u9177\u5bb6\u4e50",
                "\u6df1\u5ea6\u8d4b\u667a",
                "\u964c\u964c"
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
        chart_fdbbd293cfe544b0a3122b2973c2d355.setOption(option_fdbbd293cfe544b0a3122b2973c2d355);
    </script>
                <div id="e0bd1f5c3a2c4fe4a0ae23ad7a85c74c" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_e0bd1f5c3a2c4fe4a0ae23ad7a85c74c = echarts.init(
            document.getElementById('e0bd1f5c3a2c4fe4a0ae23ad7a85c74c'), 'white', {renderer: 'canvas'});
        var option_e0bd1f5c3a2c4fe4a0ae23ad7a85c74c = {
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
                701,
                333,
                301,
                178,
                91,
                68,
                22,
                14,
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
                    "value": 701,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,55,120)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77",
                    "value": 333,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,82,158)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733",
                    "value": 301,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,2,159)"
                        }
                    }
                },
                {
                    "name": "\u676d\u5dde",
                    "value": 178,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,153,97)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u5dde",
                    "value": 91,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,106,159)"
                        }
                    }
                },
                {
                    "name": "\u6210\u90fd",
                    "value": 68,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,34,97)"
                        }
                    }
                },
                {
                    "name": "\u6b66\u6c49",
                    "value": 22,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,52,143)"
                        }
                    }
                },
                {
                    "name": "\u5357\u4eac",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,148,119)"
                        }
                    }
                },
                {
                    "name": "\u82cf\u5dde",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,39,54)"
                        }
                    }
                },
                {
                    "name": "\u4f5b\u5c71",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,61,93)"
                        }
                    }
                },
                {
                    "name": "\u91cd\u5e86",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,29,5)"
                        }
                    }
                },
                {
                    "name": "\u53a6\u95e8",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,159,45)"
                        }
                    }
                },
                {
                    "name": "\u897f\u5b89",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,159,66)"
                        }
                    }
                },
                {
                    "name": "\u73e0\u6d77",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,64,69)"
                        }
                    }
                },
                {
                    "name": "\u5408\u80a5",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,146,36)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u9521",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,36,150)"
                        }
                    }
                },
                {
                    "name": "\u5b81\u6ce2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,116,99)"
                        }
                    }
                },
                {
                    "name": "\u60e0\u5dde",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,4,85)"
                        }
                    }
                },
                {
                    "name": "\u957f\u6c99",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,38,114)"
                        }
                    }
                },
                {
                    "name": "\u90d1\u5dde",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,92,29)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u839e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,16,18)"
                        }
                    }
                },
                {
                    "name": "\u592a\u539f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,7,38)"
                        }
                    }
                },
                {
                    "name": "\u6d4e\u5357",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,70,19)"
                        }
                    }
                },
                {
                    "name": "\u9752\u5c9b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,61,2)"
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
        chart_e0bd1f5c3a2c4fe4a0ae23ad7a85c74c.setOption(option_e0bd1f5c3a2c4fe4a0ae23ad7a85c74c);
    </script>
                <div id="9388591d315f443a8f51817da0d930f1" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_9388591d315f443a8f51817da0d930f1 = echarts.init(
            document.getElementById('9388591d315f443a8f51817da0d930f1'), 'white', {renderer: 'canvas'});
        var option_9388591d315f443a8f51817da0d930f1 = {
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
                    "value": 701,
                    "name": "\u5317\u4eac"
                },
                {
                    "value": 333,
                    "name": "\u4e0a\u6d77"
                },
                {
                    "value": 301,
                    "name": "\u6df1\u5733"
                },
                {
                    "value": 178,
                    "name": "\u676d\u5dde"
                },
                {
                    "value": 91,
                    "name": "\u5e7f\u5dde"
                },
                {
                    "value": 68,
                    "name": "\u6210\u90fd"
                },
                {
                    "value": 22,
                    "name": "\u6b66\u6c49"
                },
                {
                    "value": 14,
                    "name": "\u5357\u4eac"
                },
                {
                    "value": 12,
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
                    "value": 7,
                    "name": "\u53a6\u95e8"
                },
                {
                    "value": 6,
                    "name": "\u897f\u5b89"
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
                    "value": 4,
                    "name": "\u65e0\u9521"
                },
                {
                    "value": 2,
                    "name": "\u5b81\u6ce2"
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
                    "value": 2,
                    "name": "\u90d1\u5dde"
                },
                {
                    "value": 1,
                    "name": "\u4e1c\u839e"
                },
                {
                    "value": 1,
                    "name": "\u592a\u539f"
                },
                {
                    "value": 1,
                    "name": "\u6d4e\u5357"
                },
                {
                    "value": 1,
                    "name": "\u9752\u5c9b"
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
        chart_9388591d315f443a8f51817da0d930f1.setOption(option_9388591d315f443a8f51817da0d930f1);
    </script>
                <div id="2ed31d84cb33485da041f59b455feb6b" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_2ed31d84cb33485da041f59b455feb6b = echarts.init(
            document.getElementById('2ed31d84cb33485da041f59b455feb6b'), 'white', {renderer: 'canvas'});
            
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
    
        var option_2ed31d84cb33485da041f59b455feb6b = {
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
                        701
                    ]
                },
                {
                    "name": "\u4e0a\u6d77",
                    "value": [
                        121.473701,
                        31.230416,
                        333
                    ]
                },
                {
                    "name": "\u6df1\u5733",
                    "value": [
                        114.07,
                        22.62,
                        301
                    ]
                },
                {
                    "name": "\u676d\u5dde",
                    "value": [
                        120.19,
                        30.26,
                        178
                    ]
                },
                {
                    "name": "\u5e7f\u5dde",
                    "value": [
                        113.23,
                        23.16,
                        91
                    ]
                },
                {
                    "name": "\u6210\u90fd",
                    "value": [
                        104.06,
                        30.67,
                        68
                    ]
                },
                {
                    "name": "\u6b66\u6c49",
                    "value": [
                        114.31,
                        30.52,
                        22
                    ]
                },
                {
                    "name": "\u5357\u4eac",
                    "value": [
                        118.78,
                        32.04,
                        14
                    ]
                },
                {
                    "name": "\u82cf\u5dde",
                    "value": [
                        120.62,
                        31.32,
                        12
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
                        7
                    ]
                },
                {
                    "name": "\u897f\u5b89",
                    "value": [
                        108.95,
                        34.27,
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
                    "name": "\u90d1\u5dde",
                    "value": [
                        113.65,
                        34.76,
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
                    "name": "\u592a\u539f",
                    "value": [
                        112.53,
                        37.87,
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
                    "name": "\u9752\u5c9b",
                    "value": [
                        120.33,
                        36.07,
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
        chart_2ed31d84cb33485da041f59b455feb6b.setOption(option_2ed31d84cb33485da041f59b455feb6b);
    </script>
                <div id="f7edf95b04a54922a82410c66f69bdca" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_f7edf95b04a54922a82410c66f69bdca = echarts.init(
            document.getElementById('f7edf95b04a54922a82410c66f69bdca'), 'white', {renderer: 'canvas'});
        var option_f7edf95b04a54922a82410c66f69bdca = {
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
                177,
                176,
                131,
                49,
                49,
                46,
                40,
                38,
                34,
                34
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
                    "value": 177,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,53,130)"
                        }
                    }
                },
                {
                    "name": "\u671d\u9633\u533a",
                    "value": 176,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,55,103)"
                        }
                    }
                },
                {
                    "name": "\u5357\u5c71\u533a",
                    "value": 131,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,102,90)"
                        }
                    }
                },
                {
                    "name": "\u671b\u4eac",
                    "value": 49,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,126,29)"
                        }
                    }
                },
                {
                    "name": "\u6d66\u4e1c\u65b0\u2026",
                    "value": 49,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,36,126)"
                        }
                    }
                },
                {
                    "name": "\u4f59\u676d\u533a",
                    "value": 46,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,139,27)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u6280\u56ed",
                    "value": 40,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,55,69)"
                        }
                    }
                },
                {
                    "name": "\u897f\u5317\u65fa",
                    "value": 38,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,48,113)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u65b0\u533a",
                    "value": 34,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,70,17)"
                        }
                    }
                },
                {
                    "name": "\u95f5\u884c\u533a",
                    "value": 34,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,21,54)"
                        }
                    }
                },
                {
                    "name": "\u5f90\u6c47\u533a",
                    "value": 32,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,122,85)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u5173\u6751",
                    "value": 31,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,68,30)"
                        }
                    }
                },
                {
                    "name": "\u6768\u6d66\u533a",
                    "value": 29,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,21,100)"
                        }
                    }
                },
                {
                    "name": "\u798f\u7530\u533a",
                    "value": 29,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,133,129)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9053\u53e3",
                    "value": 29,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,136,111)"
                        }
                    }
                },
                {
                    "name": "\u5f20\u6c5f",
                    "value": 25,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,87,8)"
                        }
                    }
                },
                {
                    "name": "\u5b9d\u5b89\u533a",
                    "value": 23,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,9,25)"
                        }
                    }
                },
                {
                    "name": "\u897f\u6eaa",
                    "value": 21,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,136,14)"
                        }
                    }
                },
                {
                    "name": "\u8679\u53e3\u533a",
                    "value": 21,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,105,60)"
                        }
                    }
                },
                {
                    "name": "\u897f\u6e56\u533a",
                    "value": 18,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,16,131)"
                        }
                    }
                },
                {
                    "name": "\u6b66\u4faf\u533a",
                    "value": 18,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,71,104)"
                        }
                    }
                },
                {
                    "name": "\u957f\u5b81\u533a",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,87,6)"
                        }
                    }
                },
                {
                    "name": "\u5929\u6cb3\u533a",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,149,13)"
                        }
                    }
                },
                {
                    "name": "\u5927\u51b2",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,126,12)"
                        }
                    }
                },
                {
                    "name": "\u8d8a\u79c0\u533a",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,92,58)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5174\u533a",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,136,23)"
                        }
                    }
                },
                {
                    "name": "\u6ee8\u6c5f\u533a",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,74,69)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u6625\u8def",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,69,15)"
                        }
                    }
                },
                {
                    "name": "\u897f\u4e8c\u65d7",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,22,26)"
                        }
                    }
                },
                {
                    "name": "\u62f1\u5885\u533a",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,103,149)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u57ce\u533a",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,0,26)"
                        }
                    }
                },
                {
                    "name": "\u8679\u6885\u8def",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,17,146)"
                        }
                    }
                },
                {
                    "name": "\u897f\u4e09\u65d7",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,113,30)"
                        }
                    }
                },
                {
                    "name": "\u9759\u5b89\u533a",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,59,2)"
                        }
                    }
                },
                {
                    "name": "\u897f\u5174",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,12,156)"
                        }
                    }
                },
                {
                    "name": "\u987a\u5fb7\u533a",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,131,43)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u6e56\u65b0\u2026",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,62,138)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u6e7e",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,108,62)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5730",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,44,36)"
                        }
                    }
                },
                {
                    "name": "\u677e\u6c5f\u533a",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,93,91)"
                        }
                    }
                },
                {
                    "name": "\u9ec4\u6d66\u533a",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,114,72)"
                        }
                    }
                },
                {
                    "name": "\u9f99\u534e\u65b0\u2026",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,86,23)"
                        }
                    }
                },
                {
                    "name": "\u77f3\u666f\u5c71\u2026",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,17,126)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u56ed\u2026",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,44,77)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,115,69)"
                        }
                    }
                },
                {
                    "name": "\u4ed3\u524d",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,64,147)"
                        }
                    }
                },
                {
                    "name": "\u957f\u6cb3",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,92,20)"
                        }
                    }
                },
                {
                    "name": "\u666e\u9640\u533a",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,66,77)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u73e0\u533a",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,112,42)"
                        }
                    }
                },
                {
                    "name": "\u9752\u6d66\u533a",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,150,92)"
                        }
                    }
                },
                {
                    "name": "\u9f99\u534e",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,59,46)"
                        }
                    }
                },
                {
                    "name": "\u5357\u6c99\u533a",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,133,135)"
                        }
                    }
                },
                {
                    "name": "\u9ec4\u57d4\u533a",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,125,44)"
                        }
                    }
                },
                {
                    "name": "\u5929\u5c71\u8def",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,22,99)"
                        }
                    }
                },
                {
                    "name": "\u601d\u660e\u533a",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,118,50)"
                        }
                    }
                },
                {
                    "name": "\u756a\u79ba\u533a",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,117,89)"
                        }
                    }
                },
                {
                    "name": "\u5f90\u5bb6\u6c47",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,0,79)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,111,31)"
                        }
                    }
                },
                {
                    "name": "\u6765\u5e7f\u8425",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,129,114)"
                        }
                    }
                },
                {
                    "name": "\u5927\u671b\u8def",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,28,66)"
                        }
                    }
                },
                {
                    "name": "\u5317\u65b0\u6cfe",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,143,137)"
                        }
                    }
                },
                {
                    "name": "\u68e0\u4e0b",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,93,130)"
                        }
                    }
                },
                {
                    "name": "\u9152\u4ed9\u6865",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,53,121)"
                        }
                    }
                },
                {
                    "name": "\u9999\u6d32\u533a",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,65,138)"
                        }
                    }
                },
                {
                    "name": "\u6587\u4e09\u8def",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,16,146)"
                        }
                    }
                },
                {
                    "name": "\u4e9a\u8fd0\u6751",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,130,134)"
                        }
                    }
                },
                {
                    "name": "\u901a\u5dde\u533a",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,96,6)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,150,107)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u9662\u8def",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,14,128)"
                        }
                    }
                },
                {
                    "name": "\u5357\u6cb9",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,25,59)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u5703",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,127,19)"
                        }
                    }
                },
                {
                    "name": "\u96c1\u5854\u533a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,131,82)"
                        }
                    }
                },
                {
                    "name": "\u6d2a\u5c71\u533a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,55,62)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5c71\u5b50",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,154,118)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u5927\u2026",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,142,102)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5b89",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,78,45)"
                        }
                    }
                },
                {
                    "name": "\u897f\u4e3d",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,3,45)"
                        }
                    }
                },
                {
                    "name": "\u96e8\u82b1\u53f0\u2026",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,38,11)"
                        }
                    }
                },
                {
                    "name": "\u6e1d\u4e2d\u533a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,97,129)"
                        }
                    }
                },
                {
                    "name": "\u53e4\u58a9\u8def",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,14,15)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u89d2\u573a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,114,151)"
                        }
                    }
                },
                {
                    "name": "\u4ea6\u5e84",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,157,9)"
                        }
                    }
                },
                {
                    "name": "\u5f90\u6cfe",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,19,153)"
                        }
                    }
                },
                {
                    "name": "\u5317\u5916\u6ee9",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,5,58)"
                        }
                    }
                },
                {
                    "name": "\u8427\u5c71\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,145,107)"
                        }
                    }
                },
                {
                    "name": "\u6ee8\u6e56\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,150,149)"
                        }
                    }
                },
                {
                    "name": "\u5317\u82d1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,94,100)"
                        }
                    }
                },
                {
                    "name": "\u5efa\u56fd\u95e8",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,147,108)"
                        }
                    }
                },
                {
                    "name": "\u71d5\u838e",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,15,142)"
                        }
                    }
                },
                {
                    "name": "\u547c\u5bb6\u697c",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,77,131)"
                        }
                    }
                },
                {
                    "name": "\u56de\u9f99\u89c2",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,121,154)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u725b\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,143,57)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u6d41\u53bf",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,117,58)"
                        }
                    }
                },
                {
                    "name": "\u671b\u6c5f\u8def",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,65,157)"
                        }
                    }
                },
                {
                    "name": "\u5929\u6cb3\u57ce",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,22,35)"
                        }
                    }
                },
                {
                    "name": "\u9526\u6c5f\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,17,95)"
                        }
                    }
                },
                {
                    "name": "\u540e\u6d77",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,110,111)"
                        }
                    }
                },
                {
                    "name": "\u676d\u5dde",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,78,48)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u798f\u5e84",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,63,139)"
                        }
                    }
                },
                {
                    "name": "\u76f8\u57ce\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,67,55)"
                        }
                    }
                },
                {
                    "name": "\u897f\u6e56",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,35,156)"
                        }
                    }
                },
                {
                    "name": "\u897f\u76f4\u95e8",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,35,56)"
                        }
                    }
                },
                {
                    "name": "\u6587\u5bb6",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,74,135)"
                        }
                    }
                },
                {
                    "name": "\u671d\u9633\u95e8",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,12,97)"
                        }
                    }
                },
                {
                    "name": "\u56db\u5e73\u8def",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,101,45)"
                        }
                    }
                },
                {
                    "name": "\u7f57\u6e56\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,78,110)"
                        }
                    }
                },
                {
                    "name": "\u660c\u5e73\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,48,115)"
                        }
                    }
                },
                {
                    "name": "\u897f\u4e61",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,90,40)"
                        }
                    }
                },
                {
                    "name": "\u4e0b\u57ce\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,157,17)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u5c71",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,48,69)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u58a9",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,49,147)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u5173",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,25,84)"
                        }
                    }
                },
                {
                    "name": "\u6f15\u6cb3\u6cfe",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,138,51)"
                        }
                    }
                },
                {
                    "name": "\u6d66\u6cbf",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,97,15)"
                        }
                    }
                },
                {
                    "name": "\u5149\u660e\u65b0\u2026",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,105,42)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u65b0\u6280\u2026",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,145,82)"
                        }
                    }
                },
                {
                    "name": "\u57ce\u968d\u5e99",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,155,115)"
                        }
                    }
                },
                {
                    "name": "\u8398\u5e84",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,48,76)"
                        }
                    }
                },
                {
                    "name": "\u5929\u76ee\u5c71\u2026",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,112,91)"
                        }
                    }
                },
                {
                    "name": "\u576a\u5c71\u65b0\u2026",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,44,55)"
                        }
                    }
                },
                {
                    "name": "\u5de6\u5bb6\u5e84",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,28,84)"
                        }
                    }
                },
                {
                    "name": "\u524d\u6d77",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,103,129)"
                        }
                    }
                },
                {
                    "name": "\u548c\u5e73\u91cc",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,99,0)"
                        }
                    }
                },
                {
                    "name": "\u6c5f\u5b81\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,113,138)"
                        }
                    }
                },
                {
                    "name": "\u5efa\u5916\u5927\u2026",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,103,54)"
                        }
                    }
                },
                {
                    "name": "\u5f00\u53d1\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,147,85)"
                        }
                    }
                },
                {
                    "name": "\u7acb\u6c34\u6865",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,0,16)"
                        }
                    }
                },
                {
                    "name": "\u5742\u7530",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,41,10)"
                        }
                    }
                },
                {
                    "name": "\u4e07\u6cc9\u6cb3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,143,105)"
                        }
                    }
                },
                {
                    "name": "\u5173\u5c71",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,88,151)"
                        }
                    }
                },
                {
                    "name": "\u9f99\u6cc9\u9a7f\u2026",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,133,160)"
                        }
                    }
                },
                {
                    "name": "\u673a\u6295\u6865",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,151,0)"
                        }
                    }
                },
                {
                    "name": "\u987a\u4e49\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,38,84)"
                        }
                    }
                },
                {
                    "name": "\u6797\u548c",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,67,59)"
                        }
                    }
                },
                {
                    "name": "\u9f99\u5c97\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,92,43)"
                        }
                    }
                },
                {
                    "name": "\u56db\u60e0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,79,98)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u5143\u6865",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,61,128)"
                        }
                    }
                },
                {
                    "name": "\u6c5f\u5e72\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,146,115)"
                        }
                    }
                },
                {
                    "name": "\u5609\u5b9a\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,136,58)"
                        }
                    }
                },
                {
                    "name": "\u6253\u6d66\u6865",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,90,88)"
                        }
                    }
                },
                {
                    "name": "\u60e0\u9633\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,128,25)"
                        }
                    }
                },
                {
                    "name": "\u534e\u6f15",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,67,76)"
                        }
                    }
                },
                {
                    "name": "\u65e0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,140,111)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u6e2f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,110,119)"
                        }
                    }
                },
                {
                    "name": "\u5ef6\u5409",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,23,149)"
                        }
                    }
                },
                {
                    "name": "\u897f\u82d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,137,123)"
                        }
                    }
                },
                {
                    "name": "\u767d\u6768",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,13,90)"
                        }
                    }
                },
                {
                    "name": "\u6b66\u6c49\u7ecf\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,116,50)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u76f4\u95e8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,138,26)"
                        }
                    }
                },
                {
                    "name": "\u592a\u548c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,128,129)"
                        }
                    }
                },
                {
                    "name": "\u6c5f\u5cb8\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,75,79)"
                        }
                    }
                },
                {
                    "name": "\u7ea2\u5e99",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,89,32)"
                        }
                    }
                },
                {
                    "name": "\u5e38\u8425",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,26,99)"
                        }
                    }
                },
                {
                    "name": "\u90d1\u4e1c\u65b0\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,54,59)"
                        }
                    }
                },
                {
                    "name": "\u6a2a\u5c97",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,134,97)"
                        }
                    }
                },
                {
                    "name": "\u4e03\u5b9d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,150,133)"
                        }
                    }
                },
                {
                    "name": "\u8096\u5bb6\u6cb3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,101,0)"
                        }
                    }
                },
                {
                    "name": "\u841d\u5c97\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,116,44)"
                        }
                    }
                },
                {
                    "name": "\u5343\u5cf0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,23,4)"
                        }
                    }
                },
                {
                    "name": "\u56db\u5ddd\u5317\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,107,40)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u53f0\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,148,140)"
                        }
                    }
                },
                {
                    "name": "\u822a\u7a7a\u6e2f\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,42,57)"
                        }
                    }
                },
                {
                    "name": "\u76d0\u7530\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,82,126)"
                        }
                    }
                },
                {
                    "name": "\u4eae\u9a6c\u6865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,64,28)"
                        }
                    }
                },
                {
                    "name": "\u5cad\u5357",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,64,24)"
                        }
                    }
                },
                {
                    "name": "\u73e0\u6c5f\u65b0\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,98,6)"
                        }
                    }
                },
                {
                    "name": "\u53e4\u8361",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,59,58)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u57ce\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,38,38)"
                        }
                    }
                },
                {
                    "name": "\u56db\u5b63\u9752",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,83,159)"
                        }
                    }
                },
                {
                    "name": "\u6d66\u53e3\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,138,126)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5434\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,131,70)"
                        }
                    }
                },
                {
                    "name": "\u5149\u8c37",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,117,86)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u839e\u5e02",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,6,21)"
                        }
                    }
                },
                {
                    "name": "\u6885\u56ed",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,111,115)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u6d41\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,121,137)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u56db",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,40,104)"
                        }
                    }
                },
                {
                    "name": "\u534e\u4fa8\u57ce",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,146,26)"
                        }
                    }
                },
                {
                    "name": "\u5434\u6cfe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,111,55)"
                        }
                    }
                },
                {
                    "name": "\u5357\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,15,40)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u5927\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,11,87)"
                        }
                    }
                },
                {
                    "name": "\u5e02\u5357\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,82,37)"
                        }
                    }
                },
                {
                    "name": "\u911e\u5dde\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,102,72)"
                        }
                    }
                },
                {
                    "name": "\u957f\u5f81",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,93,6)"
                        }
                    }
                },
                {
                    "name": "\u5965\u4f53",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,14,103)"
                        }
                    }
                },
                {
                    "name": "\u6587\u4e00\u8def",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,5,132)"
                        }
                    }
                },
                {
                    "name": "\u5b81\u56f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,95,9)"
                        }
                    }
                },
                {
                    "name": "\u6f15\u5b9d\u8def",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,100,108)"
                        }
                    }
                },
                {
                    "name": "\u897f\u5c71",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,19,14)"
                        }
                    }
                },
                {
                    "name": "\u6d0b\u6cfe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,138,45)"
                        }
                    }
                },
                {
                    "name": "\u576a\u5c71\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,66,34)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u6986\u6811",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,60,69)"
                        }
                    }
                },
                {
                    "name": "\u6d41\u82b3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,44,19)"
                        }
                    }
                },
                {
                    "name": "\u96e8\u82b1\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,2,143)"
                        }
                    }
                },
                {
                    "name": "\u9a6c\u8fde\u6d3c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,3,95)"
                        }
                    }
                },
                {
                    "name": "\u6816\u971e\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,70,28)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u884c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,59,93)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u5c71\u516c\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,83,12)"
                        }
                    }
                },
                {
                    "name": "\u6e1d\u5317\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,138,0)"
                        }
                    }
                },
                {
                    "name": "\u897f\u5173",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,132,41)"
                        }
                    }
                },
                {
                    "name": "\u4e5d\u9f99\u5761\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,138,23)"
                        }
                    }
                },
                {
                    "name": "\u6e2d\u5858",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,142,8)"
                        }
                    }
                },
                {
                    "name": "\u5efa\u90ba\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,120,159)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u8857",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,63,40)"
                        }
                    }
                },
                {
                    "name": "\u4e07\u67f3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,50,105)"
                        }
                    }
                },
                {
                    "name": "\u8857\u9053\u53e3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,157,104)"
                        }
                    }
                },
                {
                    "name": "\u5386\u57ce\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,87,93)"
                        }
                    }
                },
                {
                    "name": "\u9547\u5b81\u8def",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,111,57)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u6c5f\u6e7e\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,59,123)"
                        }
                    }
                },
                {
                    "name": "\u7436\u6d32",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,144,16)"
                        }
                    }
                },
                {
                    "name": "\u6c5f\u5357",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,92,100)"
                        }
                    }
                },
                {
                    "name": "\u767d\u77f3\u6d32",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,89,50)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u6d32",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,145,97)"
                        }
                    }
                },
                {
                    "name": "\u660c\u5c97",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,48,146)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u6280\u56ed\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,123,103)"
                        }
                    }
                },
                {
                    "name": "\u592a\u9633\u5bab",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,24,65)"
                        }
                    }
                },
                {
                    "name": "\u8f66\u7ad9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,129,112)"
                        }
                    }
                },
                {
                    "name": "\u5c55\u89c8\u8def",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,12,20)"
                        }
                    }
                },
                {
                    "name": "\u6f4d\u574a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,95,127)"
                        }
                    }
                },
                {
                    "name": "\u5357\u4eac",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,8,74)"
                        }
                    }
                },
                {
                    "name": "\u5510\u9547",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,45,121)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u4ead",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,34,115)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u6167\u5bfa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,22,31)"
                        }
                    }
                },
                {
                    "name": "\u6c5f\u590f\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,4,119)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u6e2f\u4e1c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,41,60)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u7ed3\u6e56",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,59,41)"
                        }
                    }
                },
                {
                    "name": "\u5458\u6751",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,103,148)"
                        }
                    }
                },
                {
                    "name": "\u897f\u57ce\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,4,67)"
                        }
                    }
                },
                {
                    "name": "\u51bc\u6751",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,136,28)"
                        }
                    }
                },
                {
                    "name": "\u8f66\u516c\u5e99",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,53,37)"
                        }
                    }
                },
                {
                    "name": "\u5cb3\u9e93\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,159,32)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u6ca7\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,131,69)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u548c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,4,126)"
                        }
                    }
                },
                {
                    "name": "\u5357\u5c71\u533b\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,26,76)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u5fb7\u95e8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,12,146)"
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
                "\u671b\u4eac",
                "\u6d66\u4e1c\u65b0\u2026",
                "\u4f59\u676d\u533a",
                "\u79d1\u6280\u56ed",
                "\u897f\u5317\u65fa",
                "\u9ad8\u65b0\u533a",
                "\u95f5\u884c\u533a"
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
        chart_f7edf95b04a54922a82410c66f69bdca.setOption(option_f7edf95b04a54922a82410c66f69bdca);
    </script>
                <div id="300a20550e464eb89d8e76d982f19cab" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_300a20550e464eb89d8e76d982f19cab = echarts.init(
            document.getElementById('300a20550e464eb89d8e76d982f19cab'), 'white', {renderer: 'canvas'});
        var option_300a20550e464eb89d8e76d982f19cab = {
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
                    "value": 177,
                    "name": "\u6d77\u6dc0\u533a"
                },
                {
                    "value": 176,
                    "name": "\u671d\u9633\u533a"
                },
                {
                    "value": 131,
                    "name": "\u5357\u5c71\u533a"
                },
                {
                    "value": 49,
                    "name": "\u671b\u4eac"
                },
                {
                    "value": 49,
                    "name": "\u6d66\u4e1c\u65b0\u2026"
                },
                {
                    "value": 46,
                    "name": "\u4f59\u676d\u533a"
                },
                {
                    "value": 40,
                    "name": "\u79d1\u6280\u56ed"
                },
                {
                    "value": 38,
                    "name": "\u897f\u5317\u65fa"
                },
                {
                    "value": 34,
                    "name": "\u9ad8\u65b0\u533a"
                },
                {
                    "value": 34,
                    "name": "\u95f5\u884c\u533a"
                },
                {
                    "value": 32,
                    "name": "\u5f90\u6c47\u533a"
                },
                {
                    "value": 31,
                    "name": "\u4e2d\u5173\u6751"
                },
                {
                    "value": 29,
                    "name": "\u6768\u6d66\u533a"
                },
                {
                    "value": 29,
                    "name": "\u798f\u7530\u533a"
                },
                {
                    "value": 29,
                    "name": "\u4e94\u9053\u53e3"
                },
                {
                    "value": 25,
                    "name": "\u5f20\u6c5f"
                },
                {
                    "value": 23,
                    "name": "\u5b9d\u5b89\u533a"
                },
                {
                    "value": 21,
                    "name": "\u897f\u6eaa"
                },
                {
                    "value": 21,
                    "name": "\u8679\u53e3\u533a"
                },
                {
                    "value": 18,
                    "name": "\u897f\u6e56\u533a"
                },
                {
                    "value": 18,
                    "name": "\u6b66\u4faf\u533a"
                },
                {
                    "value": 17,
                    "name": "\u957f\u5b81\u533a"
                },
                {
                    "value": 17,
                    "name": "\u5929\u6cb3\u533a"
                },
                {
                    "value": 17,
                    "name": "\u5927\u51b2"
                },
                {
                    "value": 17,
                    "name": "\u8d8a\u79c0\u533a"
                },
                {
                    "value": 15,
                    "name": "\u5927\u5174\u533a"
                },
                {
                    "value": 15,
                    "name": "\u6ee8\u6c5f\u533a"
                },
                {
                    "value": 15,
                    "name": "\u77e5\u6625\u8def"
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
                    "value": 12,
                    "name": "\u4e1c\u57ce\u533a"
                },
                {
                    "value": 11,
                    "name": "\u8679\u6885\u8def"
                },
                {
                    "value": 10,
                    "name": "\u897f\u4e09\u65d7"
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
                    "name": "\u987a\u5fb7\u533a"
                },
                {
                    "value": 9,
                    "name": "\u4e1c\u6e56\u65b0\u2026"
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
                    "name": "\u677e\u6c5f\u533a"
                },
                {
                    "value": 8,
                    "name": "\u9ec4\u6d66\u533a"
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
                    "name": "\u5de5\u4e1a\u56ed\u2026"
                },
                {
                    "value": 8,
                    "name": "\u5317\u4eac"
                },
                {
                    "value": 8,
                    "name": "\u4ed3\u524d"
                },
                {
                    "value": 8,
                    "name": "\u957f\u6cb3"
                },
                {
                    "value": 8,
                    "name": "\u666e\u9640\u533a"
                },
                {
                    "value": 8,
                    "name": "\u6d77\u73e0\u533a"
                },
                {
                    "value": 8,
                    "name": "\u9752\u6d66\u533a"
                },
                {
                    "value": 8,
                    "name": "\u9f99\u534e"
                },
                {
                    "value": 7,
                    "name": "\u5357\u6c99\u533a"
                },
                {
                    "value": 7,
                    "name": "\u9ec4\u57d4\u533a"
                },
                {
                    "value": 7,
                    "name": "\u5929\u5c71\u8def"
                },
                {
                    "value": 6,
                    "name": "\u601d\u660e\u533a"
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
                    "name": "\u4e0a\u6d77"
                },
                {
                    "value": 6,
                    "name": "\u6765\u5e7f\u8425"
                },
                {
                    "value": 6,
                    "name": "\u5927\u671b\u8def"
                },
                {
                    "value": 5,
                    "name": "\u5317\u65b0\u6cfe"
                },
                {
                    "value": 5,
                    "name": "\u68e0\u4e0b"
                },
                {
                    "value": 5,
                    "name": "\u9152\u4ed9\u6865"
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
                    "name": "\u4e9a\u8fd0\u6751"
                },
                {
                    "value": 5,
                    "name": "\u901a\u5dde\u533a"
                },
                {
                    "value": 5,
                    "name": "\u6df1\u5733"
                },
                {
                    "value": 5,
                    "name": "\u5b66\u9662\u8def"
                },
                {
                    "value": 4,
                    "name": "\u5357\u6cb9"
                },
                {
                    "value": 4,
                    "name": "\u4e1c\u5703"
                },
                {
                    "value": 4,
                    "name": "\u96c1\u5854\u533a"
                },
                {
                    "value": 4,
                    "name": "\u6d2a\u5c71\u533a"
                },
                {
                    "value": 4,
                    "name": "\u5927\u5c71\u5b50"
                },
                {
                    "value": 4,
                    "name": "\u5317\u4eac\u5927\u2026"
                },
                {
                    "value": 4,
                    "name": "\u65b0\u5b89"
                },
                {
                    "value": 4,
                    "name": "\u897f\u4e3d"
                },
                {
                    "value": 4,
                    "name": "\u96e8\u82b1\u53f0\u2026"
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
                    "name": "\u4e94\u89d2\u573a"
                },
                {
                    "value": 4,
                    "name": "\u4ea6\u5e84"
                },
                {
                    "value": 3,
                    "name": "\u5f90\u6cfe"
                },
                {
                    "value": 3,
                    "name": "\u5317\u5916\u6ee9"
                },
                {
                    "value": 3,
                    "name": "\u8427\u5c71\u533a"
                },
                {
                    "value": 3,
                    "name": "\u6ee8\u6e56\u533a"
                },
                {
                    "value": 3,
                    "name": "\u5317\u82d1"
                },
                {
                    "value": 3,
                    "name": "\u5efa\u56fd\u95e8"
                },
                {
                    "value": 3,
                    "name": "\u71d5\u838e"
                },
                {
                    "value": 3,
                    "name": "\u547c\u5bb6\u697c"
                },
                {
                    "value": 3,
                    "name": "\u56de\u9f99\u89c2"
                },
                {
                    "value": 3,
                    "name": "\u91d1\u725b\u533a"
                },
                {
                    "value": 3,
                    "name": "\u53cc\u6d41\u53bf"
                },
                {
                    "value": 3,
                    "name": "\u671b\u6c5f\u8def"
                },
                {
                    "value": 3,
                    "name": "\u5929\u6cb3\u57ce"
                },
                {
                    "value": 3,
                    "name": "\u9526\u6c5f\u533a"
                },
                {
                    "value": 3,
                    "name": "\u540e\u6d77"
                },
                {
                    "value": 3,
                    "name": "\u676d\u5dde"
                },
                {
                    "value": 3,
                    "name": "\u5b9a\u798f\u5e84"
                },
                {
                    "value": 3,
                    "name": "\u76f8\u57ce\u533a"
                },
                {
                    "value": 3,
                    "name": "\u897f\u6e56"
                },
                {
                    "value": 3,
                    "name": "\u897f\u76f4\u95e8"
                },
                {
                    "value": 3,
                    "name": "\u6587\u5bb6"
                },
                {
                    "value": 3,
                    "name": "\u671d\u9633\u95e8"
                },
                {
                    "value": 3,
                    "name": "\u56db\u5e73\u8def"
                },
                {
                    "value": 3,
                    "name": "\u7f57\u6e56\u533a"
                },
                {
                    "value": 3,
                    "name": "\u660c\u5e73\u533a"
                },
                {
                    "value": 3,
                    "name": "\u897f\u4e61"
                },
                {
                    "value": 3,
                    "name": "\u4e0b\u57ce\u533a"
                },
                {
                    "value": 3,
                    "name": "\u4e94\u5c71"
                },
                {
                    "value": 3,
                    "name": "\u4e09\u58a9"
                },
                {
                    "value": 3,
                    "name": "\u5c0f\u5173"
                },
                {
                    "value": 2,
                    "name": "\u6f15\u6cb3\u6cfe"
                },
                {
                    "value": 2,
                    "name": "\u6d66\u6cbf"
                },
                {
                    "value": 2,
                    "name": "\u5149\u660e\u65b0\u2026"
                },
                {
                    "value": 2,
                    "name": "\u9ad8\u65b0\u6280\u2026"
                },
                {
                    "value": 2,
                    "name": "\u57ce\u968d\u5e99"
                },
                {
                    "value": 2,
                    "name": "\u8398\u5e84"
                },
                {
                    "value": 2,
                    "name": "\u5929\u76ee\u5c71\u2026"
                },
                {
                    "value": 2,
                    "name": "\u576a\u5c71\u65b0\u2026"
                },
                {
                    "value": 2,
                    "name": "\u5de6\u5bb6\u5e84"
                },
                {
                    "value": 2,
                    "name": "\u524d\u6d77"
                },
                {
                    "value": 2,
                    "name": "\u548c\u5e73\u91cc"
                },
                {
                    "value": 2,
                    "name": "\u6c5f\u5b81\u533a"
                },
                {
                    "value": 2,
                    "name": "\u5efa\u5916\u5927\u2026"
                },
                {
                    "value": 2,
                    "name": "\u5f00\u53d1\u533a"
                },
                {
                    "value": 2,
                    "name": "\u7acb\u6c34\u6865"
                },
                {
                    "value": 2,
                    "name": "\u5742\u7530"
                },
                {
                    "value": 2,
                    "name": "\u4e07\u6cc9\u6cb3"
                },
                {
                    "value": 2,
                    "name": "\u5173\u5c71"
                },
                {
                    "value": 2,
                    "name": "\u9f99\u6cc9\u9a7f\u2026"
                },
                {
                    "value": 2,
                    "name": "\u673a\u6295\u6865"
                },
                {
                    "value": 2,
                    "name": "\u987a\u4e49\u533a"
                },
                {
                    "value": 2,
                    "name": "\u6797\u548c"
                },
                {
                    "value": 2,
                    "name": "\u9f99\u5c97\u533a"
                },
                {
                    "value": 2,
                    "name": "\u56db\u60e0"
                },
                {
                    "value": 2,
                    "name": "\u4e09\u5143\u6865"
                },
                {
                    "value": 2,
                    "name": "\u6c5f\u5e72\u533a"
                },
                {
                    "value": 2,
                    "name": "\u5609\u5b9a\u533a"
                },
                {
                    "value": 2,
                    "name": "\u6253\u6d66\u6865"
                },
                {
                    "value": 2,
                    "name": "\u60e0\u9633\u533a"
                },
                {
                    "value": 2,
                    "name": "\u534e\u6f15"
                },
                {
                    "value": 2,
                    "name": "\u65e0"
                },
                {
                    "value": 2,
                    "name": "\u65b0\u6e2f"
                },
                {
                    "value": 2,
                    "name": "\u5ef6\u5409"
                },
                {
                    "value": 2,
                    "name": "\u897f\u82d1"
                },
                {
                    "value": 1,
                    "name": "\u767d\u6768"
                },
                {
                    "value": 1,
                    "name": "\u6b66\u6c49\u7ecf\u2026"
                },
                {
                    "value": 1,
                    "name": "\u4e1c\u76f4\u95e8"
                },
                {
                    "value": 1,
                    "name": "\u592a\u548c"
                },
                {
                    "value": 1,
                    "name": "\u6c5f\u5cb8\u533a"
                },
                {
                    "value": 1,
                    "name": "\u7ea2\u5e99"
                },
                {
                    "value": 1,
                    "name": "\u5e38\u8425"
                },
                {
                    "value": 1,
                    "name": "\u90d1\u4e1c\u65b0\u2026"
                },
                {
                    "value": 1,
                    "name": "\u6a2a\u5c97"
                },
                {
                    "value": 1,
                    "name": "\u4e03\u5b9d"
                },
                {
                    "value": 1,
                    "name": "\u8096\u5bb6\u6cb3"
                },
                {
                    "value": 1,
                    "name": "\u841d\u5c97\u533a"
                },
                {
                    "value": 1,
                    "name": "\u5343\u5cf0"
                },
                {
                    "value": 1,
                    "name": "\u56db\u5ddd\u5317\u2026"
                },
                {
                    "value": 1,
                    "name": "\u4e30\u53f0\u533a"
                },
                {
                    "value": 1,
                    "name": "\u822a\u7a7a\u6e2f\u2026"
                },
                {
                    "value": 1,
                    "name": "\u76d0\u7530\u533a"
                },
                {
                    "value": 1,
                    "name": "\u4eae\u9a6c\u6865"
                },
                {
                    "value": 1,
                    "name": "\u5cad\u5357"
                },
                {
                    "value": 1,
                    "name": "\u73e0\u6c5f\u65b0\u2026"
                },
                {
                    "value": 1,
                    "name": "\u53e4\u8361"
                },
                {
                    "value": 1,
                    "name": "\u4e0a\u57ce\u533a"
                },
                {
                    "value": 1,
                    "name": "\u56db\u5b63\u9752"
                },
                {
                    "value": 1,
                    "name": "\u6d66\u53e3\u533a"
                },
                {
                    "value": 1,
                    "name": "\u65b0\u5434\u533a"
                },
                {
                    "value": 1,
                    "name": "\u5149\u8c37"
                },
                {
                    "value": 1,
                    "name": "\u4e1c\u839e\u5e02"
                },
                {
                    "value": 1,
                    "name": "\u6885\u56ed"
                },
                {
                    "value": 1,
                    "name": "\u53cc\u6d41\u533a"
                },
                {
                    "value": 1,
                    "name": "\u4e1c\u56db"
                },
                {
                    "value": 1,
                    "name": "\u534e\u4fa8\u57ce"
                },
                {
                    "value": 1,
                    "name": "\u5434\u6cfe"
                },
                {
                    "value": 1,
                    "name": "\u5357\u5927"
                },
                {
                    "value": 1,
                    "name": "\u4ea4\u901a\u5927\u2026"
                },
                {
                    "value": 1,
                    "name": "\u5e02\u5357\u533a"
                },
                {
                    "value": 1,
                    "name": "\u911e\u5dde\u533a"
                },
                {
                    "value": 1,
                    "name": "\u957f\u5f81"
                },
                {
                    "value": 1,
                    "name": "\u5965\u4f53"
                },
                {
                    "value": 1,
                    "name": "\u6587\u4e00\u8def"
                },
                {
                    "value": 1,
                    "name": "\u5b81\u56f4"
                },
                {
                    "value": 1,
                    "name": "\u6f15\u5b9d\u8def"
                },
                {
                    "value": 1,
                    "name": "\u897f\u5c71"
                },
                {
                    "value": 1,
                    "name": "\u6d0b\u6cfe"
                },
                {
                    "value": 1,
                    "name": "\u576a\u5c71\u533a"
                },
                {
                    "value": 1,
                    "name": "\u53cc\u6986\u6811"
                },
                {
                    "value": 1,
                    "name": "\u6d41\u82b3"
                },
                {
                    "value": 1,
                    "name": "\u96e8\u82b1\u533a"
                },
                {
                    "value": 1,
                    "name": "\u9a6c\u8fde\u6d3c"
                },
                {
                    "value": 1,
                    "name": "\u6816\u971e\u533a"
                },
                {
                    "value": 1,
                    "name": "\u5c0f\u884c"
                },
                {
                    "value": 1,
                    "name": "\u4e2d\u5c71\u516c\u2026"
                },
                {
                    "value": 1,
                    "name": "\u6e1d\u5317\u533a"
                },
                {
                    "value": 1,
                    "name": "\u897f\u5173"
                },
                {
                    "value": 1,
                    "name": "\u4e5d\u9f99\u5761\u2026"
                },
                {
                    "value": 1,
                    "name": "\u6e2d\u5858"
                },
                {
                    "value": 1,
                    "name": "\u5efa\u90ba\u533a"
                },
                {
                    "value": 1,
                    "name": "\u91d1\u878d\u8857"
                },
                {
                    "value": 1,
                    "name": "\u4e07\u67f3"
                },
                {
                    "value": 1,
                    "name": "\u8857\u9053\u53e3"
                },
                {
                    "value": 1,
                    "name": "\u5386\u57ce\u533a"
                },
                {
                    "value": 1,
                    "name": "\u9547\u5b81\u8def"
                },
                {
                    "value": 1,
                    "name": "\u65b0\u6c5f\u6e7e\u2026"
                },
                {
                    "value": 1,
                    "name": "\u7436\u6d32"
                },
                {
                    "value": 1,
                    "name": "\u6c5f\u5357"
                },
                {
                    "value": 1,
                    "name": "\u767d\u77f3\u6d32"
                },
                {
                    "value": 1,
                    "name": "\u65b0\u6d32"
                },
                {
                    "value": 1,
                    "name": "\u660c\u5c97"
                },
                {
                    "value": 1,
                    "name": "\u79d1\u6280\u56ed\u2026"
                },
                {
                    "value": 1,
                    "name": "\u592a\u9633\u5bab"
                },
                {
                    "value": 1,
                    "name": "\u8f66\u7ad9"
                },
                {
                    "value": 1,
                    "name": "\u5c55\u89c8\u8def"
                },
                {
                    "value": 1,
                    "name": "\u6f4d\u574a"
                },
                {
                    "value": 1,
                    "name": "\u5357\u4eac"
                },
                {
                    "value": 1,
                    "name": "\u5510\u9547"
                },
                {
                    "value": 1,
                    "name": "\u5b89\u4ead"
                },
                {
                    "value": 1,
                    "name": "\u5b9a\u6167\u5bfa"
                },
                {
                    "value": 1,
                    "name": "\u6c5f\u590f\u533a"
                },
                {
                    "value": 1,
                    "name": "\u65b0\u6e2f\u4e1c"
                },
                {
                    "value": 1,
                    "name": "\u56e2\u7ed3\u6e56"
                },
                {
                    "value": 1,
                    "name": "\u5458\u6751"
                },
                {
                    "value": 1,
                    "name": "\u897f\u57ce\u533a"
                },
                {
                    "value": 1,
                    "name": "\u51bc\u6751"
                },
                {
                    "value": 1,
                    "name": "\u8f66\u516c\u5e99"
                },
                {
                    "value": 1,
                    "name": "\u5cb3\u9e93\u533a"
                },
                {
                    "value": 1,
                    "name": "\u6d77\u6ca7\u533a"
                },
                {
                    "value": 1,
                    "name": "\u4eba\u548c"
                },
                {
                    "value": 1,
                    "name": "\u5357\u5c71\u533b\u2026"
                },
                {
                    "value": 1,
                    "name": "\u5b89\u5fb7\u95e8"
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
        chart_300a20550e464eb89d8e76d982f19cab.setOption(option_300a20550e464eb89d8e76d982f19cab);
    </script>
                <div id="0b26ec817b8e4c04b72483141c18795e" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_0b26ec817b8e4c04b72483141c18795e = echarts.init(
            document.getElementById('0b26ec817b8e4c04b72483141c18795e'), 'white', {renderer: 'canvas'});
        var option_0b26ec817b8e4c04b72483141c18795e = {
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
                452,
                374,
                213,
                193,
                188,
                139,
                123,
                94
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
                    "value": 452
                },
                {
                    "name": "\u4e0d\u9700\u8981\u878d\u8d44",
                    "value": 374
                },
                {
                    "name": "A\u8f6e",
                    "value": 213
                },
                {
                    "name": "B\u8f6e",
                    "value": 193
                },
                {
                    "name": "D\u8f6e\u53ca\u4ee5\u4e0a",
                    "value": 188
                },
                {
                    "name": "\u672a\u878d\u8d44",
                    "value": 139
                },
                {
                    "name": "C\u8f6e",
                    "value": 123
                },
                {
                    "name": "\u5929\u4f7f\u8f6e",
                    "value": 94
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
                    "value": 452
                },
                {
                    "name": "\u4e0d\u9700\u8981\u878d\u8d44",
                    "value": 374
                },
                {
                    "name": "A\u8f6e",
                    "value": 213
                },
                {
                    "name": "B\u8f6e",
                    "value": 193
                },
                {
                    "name": "D\u8f6e\u53ca\u4ee5\u4e0a",
                    "value": 188
                },
                {
                    "name": "\u672a\u878d\u8d44",
                    "value": 139
                },
                {
                    "name": "C\u8f6e",
                    "value": 123
                },
                {
                    "name": "\u5929\u4f7f\u8f6e",
                    "value": 94
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
        chart_0b26ec817b8e4c04b72483141c18795e.setOption(option_0b26ec817b8e4c04b72483141c18795e);
    </script>
                <div id="70a57f8fb4ab44f49a908fa5274dba1b" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_70a57f8fb4ab44f49a908fa5274dba1b = echarts.init(
            document.getElementById('70a57f8fb4ab44f49a908fa5274dba1b'), 'white', {renderer: 'canvas'});
        var option_70a57f8fb4ab44f49a908fa5274dba1b = {
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
                501,
                410,
                355,
                317,
                169,
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
            "type": "pie",
            "clockwise": true,
            "data": [
                {
                    "name": "2000\u4eba\u4ee5\u4e0a",
                    "value": 501
                },
                {
                    "name": "500-2000\u4eba",
                    "value": 410
                },
                {
                    "name": "150-500\u4eba",
                    "value": 355
                },
                {
                    "name": "50-150\u4eba",
                    "value": 317
                },
                {
                    "name": "15-50\u4eba",
                    "value": 169
                },
                {
                    "name": "\u5c11\u4e8e15\u4eba",
                    "value": 24
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
                    "value": 501
                },
                {
                    "name": "500-2000\u4eba",
                    "value": 410
                },
                {
                    "name": "150-500\u4eba",
                    "value": 355
                },
                {
                    "name": "50-150\u4eba",
                    "value": 317
                },
                {
                    "name": "15-50\u4eba",
                    "value": 169
                },
                {
                    "name": "\u5c11\u4e8e15\u4eba",
                    "value": 24
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
        chart_70a57f8fb4ab44f49a908fa5274dba1b.setOption(option_70a57f8fb4ab44f49a908fa5274dba1b);
    </script>
                <div id="1a360e90a8494d30a29ff8059267b915" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_1a360e90a8494d30a29ff8059267b915 = echarts.init(
            document.getElementById('1a360e90a8494d30a29ff8059267b915'), 'white', {renderer: 'canvas'});
        var option_1a360e90a8494d30a29ff8059267b915 = {
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
                616,
                343,
                205,
                187,
                178,
                151,
                118
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
                    "value": 616,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,43,137)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u670d\u52a1",
                    "value": 343,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,101,69)"
                        }
                    }
                },
                {
                    "name": "\u8f6f\u4ef6\u670d\u52a1",
                    "value": 205,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,37,59)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u670d\u52a1",
                    "value": 187,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,45,39)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u786c\u4ef6",
                    "value": 178,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,73,124)"
                        }
                    }
                },
                {
                    "name": "IT\u6280\u672f\u670d\u52a1",
                    "value": 151,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,19,20)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u5177\u7c7b\u4ea7\u54c1",
                    "value": 118,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,160,2)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u6280\u91d1\u878d",
                    "value": 92,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,142,55)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u4e1a\u670d\u52a1",
                    "value": 86,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,60,37)"
                        }
                    }
                },
                {
                    "name": "\u6d88\u8d39\u751f\u6d3b",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,31,77)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u8d44\u8baf",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,6,61)"
                        }
                    }
                },
                {
                    "name": "\u77ed\u89c6\u9891",
                    "value": 67,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,56,70)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u5a92\u4f53",
                    "value": 66,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,85,145)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u9891",
                    "value": 66,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,11,105)"
                        }
                    }
                },
                {
                    "name": "\u79fb\u52a8\u4e92\u8054\u7f51",
                    "value": 66,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,33,35)"
                        }
                    }
                },
                {
                    "name": "\u7269\u8054\u7f51",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,83,50)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,133,60)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4ea4\u5e73\u53f0",
                    "value": 61,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,125,80)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546\u5e73\u53f0",
                    "value": 58,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,152,21)"
                        }
                    }
                },
                {
                    "name": "\u6e38\u620f",
                    "value": 49,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,59,41)"
                        }
                    }
                },
                {
                    "name": "\u5728\u7ebf\u6559\u80b2",
                    "value": 47,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,144,100)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u793e\u533a",
                    "value": 47,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,157,144)"
                        }
                    }
                },
                {
                    "name": "\u4f01\u4e1a\u670d\u52a1",
                    "value": 45,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,98,140)"
                        }
                    }
                },
                {
                    "name": "\u5176\u4ed6",
                    "value": 41,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,51,81)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u6e38",
                    "value": 39,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,80,117)"
                        }
                    }
                },
                {
                    "name": "\u51fa\u884c",
                    "value": 38,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,148,93)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u5b89\u5168",
                    "value": 35,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,4,158)"
                        }
                    }
                },
                {
                    "name": "\u5236\u9020\u4e1a",
                    "value": 32,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,77,86)"
                        }
                    }
                },
                {
                    "name": "\u8425\u9500\u670d\u52a1",
                    "value": 32,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,40,5)"
                        }
                    }
                },
                {
                    "name": "\u6559\u80b2",
                    "value": 30,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,26,21)"
                        }
                    }
                },
                {
                    "name": "\u5728\u7ebf\u533b\u7597",
                    "value": 29,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,23,26)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u4e1a",
                    "value": 29,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,141,59)"
                        }
                    }
                },
                {
                    "name": "\u57f9\u8bad",
                    "value": 25,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,61,110)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4ea4\u5a92\u4f53",
                    "value": 24,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,109,98)"
                        }
                    }
                },
                {
                    "name": "\u8f6f\u4ef6\u5f00\u53d1",
                    "value": 23,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,124,157)"
                        }
                    }
                },
                {
                    "name": "\u786c\u4ef6",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,155,134)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u4e28\u5065\u5eb7",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,52,15)"
                        }
                    }
                },
                {
                    "name": "\u7269\u6d41",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,89,51)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u8f93",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,138,60)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,19,145)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u68c0\u7d22",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,25,118)"
                        }
                    }
                },
                {
                    "name": "\u5efa\u7b51",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,112,34)"
                        }
                    }
                },
                {
                    "name": "\u623f\u5730\u4ea7",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,58,130)"
                        }
                    }
                },
                {
                    "name": "\u7269\u4e1a",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,30,95)"
                        }
                    }
                },
                {
                    "name": "\u5c45\u4f4f\u670d\u52a1",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,35,62)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,121,145)"
                        }
                    }
                },
                {
                    "name": "\u4fdd\u5065",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,0,52)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u96f6\u552e",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,115,138)"
                        }
                    }
                },
                {
                    "name": "\u8d38\u6613",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,160,59)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u5bb9",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,97,5)"
                        }
                    }
                },
                {
                    "name": "\u8fdb\u51fa\u53e3",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,79,131)"
                        }
                    }
                },
                {
                    "name": "\u6c7d\u8f66\u4e28\u51fa\u884c",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,21,137)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,44,135)"
                        }
                    }
                },
                {
                    "name": "\u6279\u53d1",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,154,18)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u552e",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,3,30)"
                        }
                    }
                },
                {
                    "name": "MCN",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,97,158)"
                        }
                    }
                },
                {
                    "name": "\u751f\u6d3b\u670d\u52a1",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,130,110)"
                        }
                    }
                },
                {
                    "name": "\u76f4\u64ad\u5e73\u53f0",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,128,57)"
                        }
                    }
                },
                {
                    "name": "\u7269\u6d41\u4e28\u8fd0\u8f93",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,8,116)"
                        }
                    }
                },
                {
                    "name": "\u80fd\u6e90",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,122,41)"
                        }
                    }
                },
                {
                    "name": "\u77ff\u4ea7",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,80,108)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u5177",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,159,46)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u7edc\u901a\u4fe1",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,150,102)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4ea4",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,27,136)"
                        }
                    }
                },
                {
                    "name": "\u533a\u5757\u94fe",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,14,4)"
                        }
                    }
                },
                {
                    "name": "\u6587\u5a31\u4e28\u5185\u5bb9",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,71,160)"
                        }
                    }
                },
                {
                    "name": "\u73af\u4fdd",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,88,27)"
                        }
                    }
                },
                {
                    "name": "\u52a8\u6f2b",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,132,82)"
                        }
                    }
                },
                {
                    "name": "\u5f71\u89c6",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,109,94)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5a92\u4f53",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,148,59)"
                        }
                    }
                },
                {
                    "name": "\u4f11\u95f2",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,67,29)"
                        }
                    }
                },
                {
                    "name": "\u5a31\u4e50",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,152,0)"
                        }
                    }
                },
                {
                    "name": "\u6587\u5316\u4f20\u5a92",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,4,36)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u8425\u9500",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,48,147)"
                        }
                    }
                },
                {
                    "name": "\u519c\u6797\u7267\u6e14",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,58,22)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u3001\u8f6f\u4ef6\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,138,43)"
                        }
                    }
                },
                {
                    "name": "\u6c7d\u8f66\u4ea4\u6613\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,73,83)"
                        }
                    }
                },
                {
                    "name": "\u623f\u4ea7\u5bb6\u5c45",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,148,105)"
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
        chart_1a360e90a8494d30a29ff8059267b915.setOption(option_1a360e90a8494d30a29ff8059267b915);
    </script>
                <div id="d7721ad103e34051ab6322df22ea5d07" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_d7721ad103e34051ab6322df22ea5d07 = echarts.init(
            document.getElementById('d7721ad103e34051ab6322df22ea5d07'), 'white', {renderer: 'canvas'});
        var option_d7721ad103e34051ab6322df22ea5d07 = {
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
                109,
                94,
                51,
                48,
                33,
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
                            "color": "rgb(17,91,105)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u7b97\u6cd5",
                    "value": 109,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,46,73)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u7b97\u6cd5",
                    "value": 94,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,58,89)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 51,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,60,139)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5",
                    "value": 48,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,1,7)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                    "value": 33,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,48,82)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9\u7b97\u6cd5",
                    "value": 32,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,101,68)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u673a\u89c6\u89c9\u7b97\u6cd5",
                    "value": 27,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,10,88)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u7b97\u6cd5",
                    "value": 23,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,148,133)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u7b97\u6cd5",
                    "value": 21,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,27,137)"
                        }
                    }
                },
                {
                    "name": "ai\u7b97\u6cd5",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,80,53)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u7b97\u6cd5",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,103,34)"
                        }
                    }
                },
                {
                    "name": "slam\u7b97\u6cd5",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,140,75)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u7b97\u6cd5",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,45,139)"
                        }
                    }
                },
                {
                    "name": "AI\u7b97\u6cd5",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,71,129)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u8bc6\u522b\u7b97\u6cd5",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,83,39)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u63a8\u8350\u7b97\u6cd5",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,9,93)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7136\u8bed\u8a00\u5904\u7406\u7b97\u6cd5",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,47,64)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u56fe\u50cf\u7b97\u6cd5",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,132,107)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u9891\u7b97\u6cd5",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,7,61)"
                        }
                    }
                },
                {
                    "name": "\u611f\u77e5\u7b97\u6cd5",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,27,140)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u7b97\u6cd5",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,125,47)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u8bc6\u522b\u7b97\u6cd5",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,38,86)"
                        }
                    }
                },
                {
                    "name": "\u63a7\u5236\u7b97\u6cd5",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,92,116)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u89c6\u89c9\u7b97\u6cd5",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,20,74)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6316\u6398\u7b97\u6cd5",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,88,121)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7\u7b97\u6cd5",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,36,17)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u63a8\u8350\u7b97\u6cd5",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,76,139)"
                        }
                    }
                },
                {
                    "name": "\u51e0\u4f55\u7b97\u6cd5",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,71,156)"
                        }
                    }
                },
                {
                    "name": "ocr\u7b97\u6cd5",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,146,74)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u4f4d\u7b97\u6cd5",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,61,55)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u7b97\u6cd5",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,127,123)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u7814\u7b97\u6cd5",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,98,110)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5904\u7406\u7b97\u6cd5",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,116,37)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u53f7\u5904\u7406 \u7b97\u6cd5",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,61,120)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7/\u8d44\u6df1\u7b97\u6cd5",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,108,101)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u7b97\u6cd5",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,67,160)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62\u7b97\u6cd5",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,45,19)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7b97\u6cd5",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,87,116)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u611f\u77e5\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,142,146)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u589e\u957f\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,122,92)"
                        }
                    }
                },
                {
                    "name": "\u5f3a\u5316\u5b66\u4e60\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,118,61)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7AI\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,4,39)"
                        }
                    }
                },
                {
                    "name": "SLAM\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,109,99)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7cbe\u5730\u56fe\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,156,65)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,110,8)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,15,102)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62\u56fe\u50cf\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,113,42)"
                        }
                    }
                },
                {
                    "name": "\u9065\u611f\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,78,38)"
                        }
                    }
                },
                {
                    "name": "\u7b56\u7565\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,88,68)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u52a8\u63a7\u5236\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,103,153)"
                        }
                    }
                },
                {
                    "name": "OCR\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,20,159)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u8bc6\u56fe\u8c31\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,125,3)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7f16\u7801\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,35,68)"
                        }
                    }
                },
                {
                    "name": "\u6fc0\u5149SLAM\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,28,23)"
                        }
                    }
                },
                {
                    "name": "\u51b3\u7b56\u89c4\u5212\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,97,138)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u97f3\u9891\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,156,116)"
                        }
                    }
                },
                {
                    "name": "\u901a\u4fe1\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,21,6)"
                        }
                    }
                },
                {
                    "name": "GNSS\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,90,16)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u63a8\u8350\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,26,2)"
                        }
                    }
                },
                {
                    "name": "\u5d4c\u5165\u5f0f\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,89,127)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u5408\u6210\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,145,28)"
                        }
                    }
                },
                {
                    "name": "CV\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,100,147)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u5168\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,26,1)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79\u4f18\u5316\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,75,141)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u7ea7\u56fe\u50cf\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,89,38)"
                        }
                    }
                },
                {
                    "name": "\u89c4\u5212\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,67,93)"
                        }
                    }
                },
                {
                    "name": "3D\u89c6\u89c9\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,34,135)"
                        }
                    }
                },
                {
                    "name": "CT\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,39,131)"
                        }
                    }
                },
                {
                    "name": "\u7b56\u7565\u67b6\u6784\u7814\u53d1\u5de5\u7a0b\u5e08\uff08\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,41,24)"
                        }
                    }
                },
                {
                    "name": "\u533b\u5b66\u5f71\u50cf\u5904\u7406\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,91,7)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u3001\u56fe\u50cf\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,41,19)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u5bfc\u822a\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,101,53)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u641c\u7d22\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,12,29)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u91cd\u5efa\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,100,157)"
                        }
                    }
                },
                {
                    "name": "\u5b9e\u4e60\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,131,119)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u56fe\u50cf\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,63,135)"
                        }
                    }
                },
                {
                    "name": "GJ2127-SPBU-\u7f8e\u989c\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,124,136)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,45,148)"
                        }
                    }
                },
                {
                    "name": "\u6821\u62db-\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,127,123)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u53f7\u5904\u7406\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,39,40)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7f16\u89e3\u7801\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,120,153)"
                        }
                    }
                },
                {
                    "name": "\u8def\u5f84\u89c4\u5212\u4e0e\u63a7\u5236\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,85,69)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u9875\u641c\u7d22-\u591a\u6a21\u6001\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,23,83)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u8d37\u6a21\u578b\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,109,37)"
                        }
                    }
                },
                {
                    "name": "NLP\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,8,103)"
                        }
                    }
                },
                {
                    "name": "\u5171\u8bc6\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,95,132)"
                        }
                    }
                },
                {
                    "name": "\u6fc0\u5149\u96f7\u8fbe\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,32,157)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u611f\u77e5\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,93,53)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7\u53cd\u6b3a\u8bc8\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,34,61)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u8c03\u5ea6\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,37,120)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7/\u8d44\u6df1\u56fe\u50cf\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,22,34)"
                        }
                    }
                },
                {
                    "name": "\u91cf\u5316\u4ea4\u6613\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,126,35)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u5f0f\u8bc6\u522b\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,9,147)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u5b66\u4e60/\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,88,17)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u89c6\u89c9\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,52,136)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u89c6\u9891/\u56fe\u50cf\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,80,147)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79\u5b66\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,10,123)"
                        }
                    }
                },
                {
                    "name": "\u9065\u611f\u56fe\u50cf\u5904\u7406\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,151,30)"
                        }
                    }
                },
                {
                    "name": "\u8def\u5f84\u89c4\u5212\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,8,156)"
                        }
                    }
                },
                {
                    "name": "\u6210\u50cf\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,122,31)"
                        }
                    }
                },
                {
                    "name": "\u7c7b\u8111\u667a\u80fd\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,111,139)"
                        }
                    }
                },
                {
                    "name": "SK6563-PTBU-\u4e2a\u6027\u5316\u63a8\u8350\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,160,131)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u89c6\u89c9\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,108,114)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,1,118)"
                        }
                    }
                },
                {
                    "name": "\u9884\u6d4b\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,19,29)"
                        }
                    }
                },
                {
                    "name": "\u5bfc\u822a\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,117,95)"
                        }
                    }
                },
                {
                    "name": "\u4e2a\u6027\u5316\u63a8\u8350\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,48,32)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u5546\u54c1\u641c\u7d22\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,45,86)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u97f3\u9891\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,42,141)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u8138\u8bc6\u522b\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,14,68)"
                        }
                    }
                },
                {
                    "name": "AI \u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,27,147)"
                        }
                    }
                },
                {
                    "name": "\u533a\u5757\u94fe\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,8,142)"
                        }
                    }
                },
                {
                    "name": "AI\u8d44\u6df1\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,32,97)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u68c0\u7d22\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,38,79)"
                        }
                    }
                },
                {
                    "name": "11122K-LT-310-\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,94,82)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9slam/vslam\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,16,30)"
                        }
                    }
                },
                {
                    "name": "\u3010\u4e0a\u6d77\u677e\u6c5f\u533a\u3011\u6545\u969c\u9884\u6d4b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,157,74)"
                        }
                    }
                },
                {
                    "name": "11417L-NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,63,5)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u7ade\u4ef7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,10,30)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u9690\u79c1\u8ba1\u7b97\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,85,126)"
                        }
                    }
                },
                {
                    "name": "AF\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,94,77)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u53f7/\u97f3\u4e50\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,21,104)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u8ba1\u7b97\u673a\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,63,60)"
                        }
                    }
                },
                {
                    "name": "\u5a92\u4f53\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,0,135)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7Gnss\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,8,88)"
                        }
                    }
                },
                {
                    "name": "\u76ee\u6807\u68c0\u6d4b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,114,144)"
                        }
                    }
                },
                {
                    "name": "39318E-\u8ba1\u7b97\u673a\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,53,31)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf/\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,145,67)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u667a\u80fd\u7ec4-\u98ce\u63a7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,60,70)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6316\u6398\u4e0e\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,24,86)"
                        }
                    }
                },
                {
                    "name": "39314F-\u901a\u7528\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,123,95)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u6c7d\u8f66\u4e8b\u4e1a\u90e8_\u8f66\u8f86\u63a7\u5236\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,66,14)"
                        }
                    }
                },
                {
                    "name": "2021\u6821\u62db-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,57,92)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1(\u63a8\u8350)\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,133,24)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u56e2APP\u90e8-\u5e7f\u544a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,152,96)"
                        }
                    }
                },
                {
                    "name": "RTK\u5b9a\u4f4d\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,52,132)"
                        }
                    }
                },
                {
                    "name": "254151-\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,157,84)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u56e2\u4f18\u9009-\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,16,126)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5e94\u7528\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,2,150)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u5b89\u5168-\u97f3\u9891\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,140,45)"
                        }
                    }
                },
                {
                    "name": "\u7f16\u8bd1\u5668\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,105,48)"
                        }
                    }
                },
                {
                    "name": "\u533b\u5b66\u5149\u8c31\u5b66\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,7,28)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,114,103)"
                        }
                    }
                },
                {
                    "name": "11413B-NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,123,128)"
                        }
                    }
                },
                {
                    "name": "2021\u6821\u56ed\u62db\u8058-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,13,129)"
                        }
                    }
                },
                {
                    "name": "Feed\u6d41\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,144,36)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u8425\u9500\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,39,108)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u7edc\u56fe\u8c31\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,121,121)"
                        }
                    }
                },
                {
                    "name": "1131OJ-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,59,38)"
                        }
                    }
                },
                {
                    "name": "\u589e\u957f\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,144,159)"
                        }
                    }
                },
                {
                    "name": "\u641c\u72d7\u624b\u5199\u8bc6\u522b-\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,38,49)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u9669\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,126,22)"
                        }
                    }
                },
                {
                    "name": "024294-AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,12,132)"
                        }
                    }
                },
                {
                    "name": "\u5168\u6c11K\u6b4c\u5185\u5bb9\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,77,40)"
                        }
                    }
                },
                {
                    "name": "0241VZ-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,61,11)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u5524\u9192\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,78,76)"
                        }
                    }
                },
                {
                    "name": "0241QC-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,44,16)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,159,84)"
                        }
                    }
                },
                {
                    "name": "\u9910\u996eSaaS\u6280\u672f\u90e8-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,104,72)"
                        }
                    }
                },
                {
                    "name": "11122N-LT-311-\u8bed\u97f3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,100,77)"
                        }
                    }
                },
                {
                    "name": "\u6d41\u5a92\u4f53\u4f20\u8f93\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,67,126)"
                        }
                    }
                },
                {
                    "name": "\u8def\u7f51\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,156,94)"
                        }
                    }
                },
                {
                    "name": "26310R-\u81ea\u7136\u8bed\u8a00\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,59,137)"
                        }
                    }
                },
                {
                    "name": "\u6c14\u8c61\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,110,154)"
                        }
                    }
                },
                {
                    "name": "05415O-AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,23,13)"
                        }
                    }
                },
                {
                    "name": "55413P-AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,138,97)"
                        }
                    }
                },
                {
                    "name": "PCG-\u5e7f\u544a\u589e\u957f\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,45,103)"
                        }
                    }
                },
                {
                    "name": "\u57ce\u5e02\u8ba1\u7b97\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,84,4)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u9645\u5316\u5b9a\u4ef7\u8865\u8d34\u4e13\u5bb6\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,64,152)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60/\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,17,7)"
                        }
                    }
                },
                {
                    "name": "TTS\u8bed\u97f3\u5408\u6210\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,77,6)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u56e2App\u90e8-\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,23,121)"
                        }
                    }
                },
                {
                    "name": "0241UC-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,156,37)"
                        }
                    }
                },
                {
                    "name": "\u641c\u72d7\u5730\u56fe-SLAM\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,133,135)"
                        }
                    }
                },
                {
                    "name": "1141DK-\u8d44\u6df1\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,84,160)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u4fe1\u53f7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,101,92)"
                        }
                    }
                },
                {
                    "name": "0232S5-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,21,101)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u5206\u6790\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,62,81)"
                        }
                    }
                },
                {
                    "name": "\u533a\u5757\u94fe\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,56,35)"
                        }
                    }
                },
                {
                    "name": "\u91cf\u5316\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,155,135)"
                        }
                    }
                },
                {
                    "name": "ADAS\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,24,12)"
                        }
                    }
                },
                {
                    "name": "3D \u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,125,50)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,74,74)"
                        }
                    }
                },
                {
                    "name": "\u878d\u5408\u5b9a\u4f4d\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,108,132)"
                        }
                    }
                },
                {
                    "name": "AEB/LKA/ACC\u7814\u53d1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,133,62)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u56fe\u5f62\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,73,148)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u89c6\u9891\u7f16\u89e3\u7801\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,147,8)"
                        }
                    }
                },
                {
                    "name": "npu\u67b6\u6784\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,91,160)"
                        }
                    }
                },
                {
                    "name": "\u533b\u5b66\u5f71\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,102,143)"
                        }
                    }
                },
                {
                    "name": "1141BD-\u81ea\u7136\u8bed\u8a00\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,59,158)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,94,76)"
                        }
                    }
                },
                {
                    "name": "324121-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,72,144)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u98ce\u63a7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,23,74)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u4e0eNLP\u90e8-\u641c\u7d22\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,129,139)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,96,78)"
                        }
                    }
                },
                {
                    "name": "PCG09-\u7528\u6237\u589e\u957f\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,153,47)"
                        }
                    }
                },
                {
                    "name": "AI\u4e13\u5bb6/\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,129,65)"
                        }
                    }
                },
                {
                    "name": "0341DO-NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,23,35)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u56e2App-\u4ea4\u6613\u94fe\u8def\u63a8\u8350-\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,153,111)"
                        }
                    }
                },
                {
                    "name": "1141BI-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,148,86)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,152,36)"
                        }
                    }
                },
                {
                    "name": "00239-\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,129,140)"
                        }
                    }
                },
                {
                    "name": "11416Z-AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,125,117)"
                        }
                    }
                },
                {
                    "name": "SPBU-\u9ad8\u7ea7\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,84,33)"
                        }
                    }
                },
                {
                    "name": "\u58f0\u7eb9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,115,115)"
                        }
                    }
                },
                {
                    "name": "\u753b\u8d28\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,96,86)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u89c6\u9891\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,24,56)"
                        }
                    }
                },
                {
                    "name": "024254-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,19,140)"
                        }
                    }
                },
                {
                    "name": "\u521d\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,64,18)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u722c\u866b\u7b56\u7565\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,103,82)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u641c\u7d22\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,113,153)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,83,43)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u56e2APP\u2014\u9ad8\u7ea7\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,30,104)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u4eba\u4f53/\u4e09\u7ef4\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,91,52)"
                        }
                    }
                },
                {
                    "name": "3D\u91cd\u5efa\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,13,94)"
                        }
                    }
                },
                {
                    "name": "CG8005-SPBU-3D\u6e32\u67d3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,46,85)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7GNSS\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,61,140)"
                        }
                    }
                },
                {
                    "name": "024208-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,108,63)"
                        }
                    }
                },
                {
                    "name": "ARVR/\u673a\u5668\u89c6\u89c9/\u56fe\u50cf\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,53,132)"
                        }
                    }
                },
                {
                    "name": "Soul App-\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,65,95)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,125,153)"
                        }
                    }
                },
                {
                    "name": "\u5343\u5bfb\u4f4d\u7f6e-RTK\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,104,20)"
                        }
                    }
                },
                {
                    "name": "\u3010\u6821\u62db\u3011\u641c\u7d22\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,13,117)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7/\u4e2d\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,35,59)"
                        }
                    }
                },
                {
                    "name": "114125-\u8d44\u6df1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,125,7)"
                        }
                    }
                },
                {
                    "name": "\u8f66\u8f86\u52a8\u529b\u5b66\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,101,80)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u7ffb\u8bd1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,68,46)"
                        }
                    }
                },
                {
                    "name": "AR\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,130,127)"
                        }
                    }
                },
                {
                    "name": "11122I-LT-312-NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,45,31)"
                        }
                    }
                },
                {
                    "name": "BK4658-SPBU-NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,128,149)"
                        }
                    }
                },
                {
                    "name": "AI\u5730\u56fe\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,0,106)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9/\u70b9\u4e91\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,19,100)"
                        }
                    }
                },
                {
                    "name": "OP2255-PTBU-\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,133,106)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\uff08\u56fe\u50cf\u8bc6\u522b\uff09\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,98,39)"
                        }
                    }
                },
                {
                    "name": "\u3010\u5357\u4eac\u3011\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,56,154)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,43,21)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u9875\u641c\u7d22-\u641c\u7d22\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,10,17)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,23,61)"
                        }
                    }
                },
                {
                    "name": "\u4eca\u65e5\u5934\u6761-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,28,97)"
                        }
                    }
                },
                {
                    "name": "2021\u6821\u62db-\u5927\u6570\u636e\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,20,155)"
                        }
                    }
                },
                {
                    "name": "114114-\u9ad8\u7ea7/\u8d44\u6df1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,12,138)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u5e7f\u544a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,79,125)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u548c\u89c6\u9891\u7406\u89e3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,77,146)"
                        }
                    }
                },
                {
                    "name": "\u5546\u4e1a\u5e7f\u544a-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,3,42)"
                        }
                    }
                },
                {
                    "name": "DL5011-nlp\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,119,105)"
                        }
                    }
                },
                {
                    "name": "\u76f4\u64ad\u5b89\u5168\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,16,133)"
                        }
                    }
                },
                {
                    "name": "AIOPs\u5e94\u7528\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,156,148)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,46,118)"
                        }
                    }
                },
                {
                    "name": "11413S-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,58,44)"
                        }
                    }
                },
                {
                    "name": "1131HA-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,146,72)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u6280\u672f\u5e73\u53f0\u90e8-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,24,151)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u63a8\u8350\u5f00\u53d1\u5de5\u7a0b\u5e08(J11384)",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,50,153)"
                        }
                    }
                },
                {
                    "name": "VU1966-SPBU-AI\u5de5\u7a0b\u5316\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,88,62)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u8f6f\u5185\u63a8 - \u5f00\u53d1/\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,153,38)"
                        }
                    }
                },
                {
                    "name": "11412I-\u8d44\u6df1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,138,52)"
                        }
                    }
                },
                {
                    "name": "LJ5001-SPBU-\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,104,108)"
                        }
                    }
                },
                {
                    "name": "\u5546\u54c1\u7ecf\u8425\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,108,56)"
                        }
                    }
                },
                {
                    "name": "RU0112-SPBU-\u89c6\u9891\u7f16\u89e3\u7801\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,104,13)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u8bed\u97f3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,93,119)"
                        }
                    }
                },
                {
                    "name": "MIG-\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,21,36)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u7814\u53d1\u5de5\u7a0b\u5e08-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,145,136)"
                        }
                    }
                },
                {
                    "name": "55414C-AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,71,136)"
                        }
                    }
                },
                {
                    "name": "0341DN-\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,77,52)"
                        }
                    }
                },
                {
                    "name": "\u5546\u4e1a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,100,10)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u6c7d\u8f66\u4e8b\u4e1a\u90e8_\u611f\u77e5\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,136,12)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u8bed\u97f3\u8bc6\u522b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,154,19)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,53,60)"
                        }
                    }
                },
                {
                    "name": "\u89c4\u5212\u5bfc\u822a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,23,49)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u5b89\u5168\u53ca\u5bc6\u7801\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,70,39)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u603b\u76d1\uff08\u6570\u636e\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,20,114)"
                        }
                    }
                },
                {
                    "name": "\u878d\u5408\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,140,61)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u63a7\u5236\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,37,100)"
                        }
                    }
                },
                {
                    "name": "\u30102021\u6821\u62db\u3011\u8ba1\u7b97\u673a\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,61,111)"
                        }
                    }
                },
                {
                    "name": "254138-NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,141,133)"
                        }
                    }
                },
                {
                    "name": "2021\u6821\u62db-GNSS\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,23,37)"
                        }
                    }
                },
                {
                    "name": "\u3010\u5357\u4eac\u3011\u56fe\u5f62\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,27,31)"
                        }
                    }
                },
                {
                    "name": "\u641c\u72d7\u6570\u5b57\u4eba-3D\u4eba\u8138\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,49,61)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,127,52)"
                        }
                    }
                },
                {
                    "name": "\u533b\u5b66\u5f71\u50cf\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,76,136)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u81ea\u7136\u8bed\u8a00\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,146,129)"
                        }
                    }
                },
                {
                    "name": "2021\u6821\u62db-\u5b8c\u597d\u6027\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,87,20)"
                        }
                    }
                },
                {
                    "name": "\u751f\u7269\u4fe1\u606f\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,68,63)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u5de5\u7a0b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,111,36)"
                        }
                    }
                },
                {
                    "name": "0341ET-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,107,96)"
                        }
                    }
                },
                {
                    "name": "\u6821\u62db-\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,10,96)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6316\u6398\u5de5\u7a0b\u5e08/AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,135,39)"
                        }
                    }
                },
                {
                    "name": "\u30102021\u6821\u62db\u3011\u8bed\u97f3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,94,38)"
                        }
                    }
                },
                {
                    "name": "25317O-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,45,159)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u4eba\u9a7e\u9a76\u8f66\u8f86\u63a7\u5236\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,148,5)"
                        }
                    }
                },
                {
                    "name": "[\u6025]\u7f51\u5b89\u8d44\u6df1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,128,71)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u4e0e\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,38,149)"
                        }
                    }
                },
                {
                    "name": "\u5929\u732b\u597d\u623f-\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,88,160)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u6d6a\u8d22\u7ecf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,29,93)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7136\u8bed\u8a00\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,57,15)"
                        }
                    }
                },
                {
                    "name": "\u5b9e\u65f6\u8def\u51b5\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,111,21)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5206\u6790\uff08\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,132,11)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u8bc4\u6d4b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,68,64)"
                        }
                    }
                },
                {
                    "name": "\u7814\u7a76\u578b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,74,69)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,59,102)"
                        }
                    }
                },
                {
                    "name": "00233-\u5d4c\u5165\u5f0f\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,33,78)"
                        }
                    }
                },
                {
                    "name": "\u51b3\u7b56\u548c\u8fd0\u52a8\u89c4\u5212\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,36,97)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u6280\u53d1\u5c55\u90e8-AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,139,88)"
                        }
                    }
                },
                {
                    "name": "\u79fb\u52a8\u7aef\u63a8\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,83,16)"
                        }
                    }
                },
                {
                    "name": "\u5b9e\u4e60\u9065\u611f\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,60,150)"
                        }
                    }
                },
                {
                    "name": "11318V-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,10,68)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u77e5\u8bc6\u56fe\u8c31\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,120,68)"
                        }
                    }
                },
                {
                    "name": "5G\u57fa\u5e26\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,110,144)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5916\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,13,62)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u5e73\u53f0-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,29,32)"
                        }
                    }
                },
                {
                    "name": "EIG-\u9065\u611f\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,155,5)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7/\u8d44\u6df1\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,88,30)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,159,51)"
                        }
                    }
                },
                {
                    "name": "\uff08\u6821\u62db\uff09\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,135,132)"
                        }
                    }
                },
                {
                    "name": "\u5916\u5356\u6280\u672f\u90e8-\u8d44\u6df1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,77,13)"
                        }
                    }
                },
                {
                    "name": "11414F-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,94,145)"
                        }
                    }
                },
                {
                    "name": "11312H-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,146,103)"
                        }
                    }
                },
                {
                    "name": "1141CU-\u8d44\u6df1\u81ea\u7136\u8bed\u8a00\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,101,84)"
                        }
                    }
                },
                {
                    "name": "\u663e\u793a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,8,19)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u89c6\u9891\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,70,52)"
                        }
                    }
                },
                {
                    "name": "\u6e32\u67d3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,19,1)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,50,128)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5916\u6d4f\u89c8\u5668\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,138,109)"
                        }
                    }
                },
                {
                    "name": "SG8103-SPBU-\u89c6\u9891\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,87,135)"
                        }
                    }
                },
                {
                    "name": "\u58f0\u5b66\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,8,36)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u89c4\u5212\u4e0e\u51b3\u7b56\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,22,55)"
                        }
                    }
                },
                {
                    "name": "\u3010\u6821\u62db\u3011\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,84,72)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u5de5\u7a0b\u5e08-\u56fe\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,157,67)"
                        }
                    }
                },
                {
                    "name": "\u3010\u7f8e\u56e2\u4f18\u9009\u3011-\u8425\u9500\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,94,93)"
                        }
                    }
                },
                {
                    "name": "\u8f68\u8ff9\u9884\u6d4b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,103,113)"
                        }
                    }
                },
                {
                    "name": "\u58f0\u5b66\u6a21\u578b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,47,98)"
                        }
                    }
                },
                {
                    "name": "0232KT-\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,69,139)"
                        }
                    }
                },
                {
                    "name": "WMPS-\u7f8e\u56e2\u914d\u9001-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,16,27)"
                        }
                    }
                },
                {
                    "name": "AI/\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,158,93)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u4ea7\u54c1\u7ecf\u7406(\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,29,4)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u56e2App-\u7f8e\u56e2\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,145,28)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,61,81)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9\u5b9a\u4f4d\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,40,77)"
                        }
                    }
                },
                {
                    "name": "\u5929\u732b\u7cbe\u7075\u4e8b\u4e1a\u90e8-\u8bed\u97f3\u5408\u6210\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,23,160)"
                        }
                    }
                },
                {
                    "name": "02416A-NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,105,82)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,100,84)"
                        }
                    }
                },
                {
                    "name": "\u5b9e\u4e60\u751f-\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,70,148)"
                        }
                    }
                },
                {
                    "name": "\u591a\u5a92\u4f53\u89c6\u9891\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,140,136)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u63a8\u8350\u5f00\u53d1\uff08\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,135,63)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u5b66\u4e60\u5e73\u53f0&\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,109,20)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u6392\u5e8f\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,111,56)"
                        }
                    }
                },
                {
                    "name": "BK32CA-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,77,71)"
                        }
                    }
                },
                {
                    "name": "\u63a5\u7ba1\u9884\u8b66\u7b56\u7565\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,42,109)"
                        }
                    }
                },
                {
                    "name": "1141BC-\u673a\u5668\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,47,36)"
                        }
                    }
                },
                {
                    "name": "XH4713-\u6d41\u5a92\u4f53\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,86,7)"
                        }
                    }
                },
                {
                    "name": "\u8f66\u8f86\u5b9a\u4f4d\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,130,118)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u56e2\u914d\u9001-\u667a\u80fd\u5b9a\u4ef7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,26,13)"
                        }
                    }
                },
                {
                    "name": "11122J-LT-312-NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,68,60)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u70b9\u4e91\u5206\u6790\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,78,46)"
                        }
                    }
                },
                {
                    "name": "\u6fc0\u5149\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,153,29)"
                        }
                    }
                },
                {
                    "name": "AR\u56fe\u5f62\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,25,3)"
                        }
                    }
                },
                {
                    "name": "\u30102021\u6821\u62db\u3011\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,85,93)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u673a\u56fe\u5f62\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,112,24)"
                        }
                    }
                },
                {
                    "name": "LJ5001-\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,48,84)"
                        }
                    }
                },
                {
                    "name": "\u58f0\u7eb9\u8bc6\u522b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,48,159)"
                        }
                    }
                },
                {
                    "name": "nlp/cv \u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,6,46)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,146,23)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u5168\u7b56\u7565\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,151,124)"
                        }
                    }
                },
                {
                    "name": "SLAM/VIO/\u4e09\u7ef4\u91cd\u5efa\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,51,100)"
                        }
                    }
                },
                {
                    "name": "Slam\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,90,83)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u81ea\u7136\u8bed\u8a00\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,3,147)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u98ce\u63a7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,159,129)"
                        }
                    }
                },
                {
                    "name": "\u5bf9\u8bdd\u63a8\u8350\u8d44\u6df1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,94,22)"
                        }
                    }
                },
                {
                    "name": "\u30102021\u6821\u62db\u3011\u5e7f\u544a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,62,52)"
                        }
                    }
                },
                {
                    "name": "11122M-LT-311-\u8bed\u97f3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,140,42)"
                        }
                    }
                },
                {
                    "name": "\u641c\u72d7\u533b\u7597\u641c\u7d22-\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,50,70)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5206\u6790/\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,100,19)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u6570\u636e\u6316\u6398\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,43,130)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u5f00\u53d1\u5de5\u7a0b\u5e08\uff08\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,153,116)"
                        }
                    }
                },
                {
                    "name": "\u3010\u6df1\u5733\u3011GNSS\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,52,47)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u4fe1\u53f7\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,87,100)"
                        }
                    }
                },
                {
                    "name": "02426A-NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,120,48)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,60,22)"
                        }
                    }
                },
                {
                    "name": "\u817e\u8baf\u770b\u70b9\u5546\u4e1a\u5316\u5e7f\u544a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,20,152)"
                        }
                    }
                },
                {
                    "name": "Vslam\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,144,12)"
                        }
                    }
                },
                {
                    "name": "09412L-NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,122,128)"
                        }
                    }
                },
                {
                    "name": "\u98de\u63a7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,31,141)"
                        }
                    }
                },
                {
                    "name": "\u5929\u773c\u67e5 \u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,49,62)"
                        }
                    }
                },
                {
                    "name": "024168-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,13,137)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u9875\u641c\u7d22-\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,127,9)"
                        }
                    }
                },
                {
                    "name": "3D\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,37,135)"
                        }
                    }
                },
                {
                    "name": "11312G-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,90,67)"
                        }
                    }
                },
                {
                    "name": "SS1060-SPBU-\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,130,39)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u56e2\u914d\u9001-\u5730\u56fe\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,14,38)"
                        }
                    }
                },
                {
                    "name": "\u591a\u4f20\u611f\u5668\u878d\u5408\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,107,143)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62\u5b66\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,78,100)"
                        }
                    }
                },
                {
                    "name": "1121XJ-\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,41,84)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,101,139)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u989c\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,92,147)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u7ea7AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,22,1)"
                        }
                    }
                },
                {
                    "name": "\u6fc0\u5149SLAM/\u591a\u4f20\u611f\u5668\u878d\u5408\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,59,122)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u7406\u89e3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,96,156)"
                        }
                    }
                },
                {
                    "name": "\u5e94\u7528\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,95,38)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7\u6a21\u578b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,133,119)"
                        }
                    }
                },
                {
                    "name": "\u5730\u56fe\u5b9a\u4f4d\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,104,17)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u4f533D\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,134,83)"
                        }
                    }
                },
                {
                    "name": "\u5168\u6c11K\u6b4c\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,38,32)"
                        }
                    }
                },
                {
                    "name": "113154-\u8d44\u6df1/\u4e13\u5bb6\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,39,154)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u53ca\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,140,115)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u7cfb\u7edf\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,69,109)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u8ba1\u7b97\u673a\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,44,28)"
                        }
                    }
                },
                {
                    "name": "29912-\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,100,79)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9\u56fe\u50cf\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,116,78)"
                        }
                    }
                },
                {
                    "name": "\u5bc6\u7801\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,54,31)"
                        }
                    }
                },
                {
                    "name": "02429L-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,131,30)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u5316\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,71,128)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u7ebf\u7535\u4fe1\u53f7\u8bc6\u522b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,6,124)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u95fb\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,4,131)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u70b9\u4e91\u5206\u6790\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,67,59)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u5e73\u53f0-\u8d44\u6df1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,19,15)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5206\u6790\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,110,131)"
                        }
                    }
                },
                {
                    "name": "\u6316\u6398\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,72,63)"
                        }
                    }
                },
                {
                    "name": "\u589e\u5f3a\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,133,160)"
                        }
                    }
                },
                {
                    "name": "\u4f9b\u5e94\u94fe\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,139,29)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u641c\u7d22\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,112,86)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u538b\u7f29\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,152,30)"
                        }
                    }
                },
                {
                    "name": "55413O-AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,47,9)"
                        }
                    }
                },
                {
                    "name": "SW-\u673a\u5668\u4eba\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,84,66)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u5e7f\u544a\u6295\u653e\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,24,91)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u56e2\u9a91\u884c-\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,74,93)"
                        }
                    }
                },
                {
                    "name": "\u89c4\u5212\u8c03\u5ea6\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,21,88)"
                        }
                    }
                },
                {
                    "name": "[\u6025]\u7f51\u5b89\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,119,141)"
                        }
                    }
                },
                {
                    "name": "\u3010\u7d27\u6025\u5c97\u4f4d\u3011\u301095\u5206\u3011\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,127,6)"
                        }
                    }
                },
                {
                    "name": "\u591a\u6a21\u6001\u8d44\u6df1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,59,151)"
                        }
                    }
                },
                {
                    "name": "\u7f16\u89e3\u7801\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,138,84)"
                        }
                    }
                },
                {
                    "name": "FF2824-\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,102,131)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u56e2App-\u7528\u6237\u589e\u957f\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,151,66)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u6570\u636e\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,19,19)"
                        }
                    }
                },
                {
                    "name": "55413N-AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,106,97)"
                        }
                    }
                },
                {
                    "name": "BL5944-SPBU-\u7f8e\u989c\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,29,61)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u7ed3\u6784\u5316\u6570\u636e\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,127,3)"
                        }
                    }
                },
                {
                    "name": "KHQ-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,32,49)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350/\u5e7f\u544a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,57,123)"
                        }
                    }
                },
                {
                    "name": "\u751f\u6001\u94fe-Slam\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,46,37)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u8a00\u6a21\u578b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,16,160)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,48,65)"
                        }
                    }
                },
                {
                    "name": "\u7acb\u4f53\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,98,104)"
                        }
                    }
                },
                {
                    "name": "\u672c\u5730\u751f\u6d3b-\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,120,13)"
                        }
                    }
                },
                {
                    "name": "AY0300-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,39,75)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u4fe1\u53f7\u5904\u7406/\u8bed\u97f3\u8bc6\u522b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,145,155)"
                        }
                    }
                },
                {
                    "name": "\u5546\u4e1a\u641c\u7d22-\u5e7f\u544a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,42,129)"
                        }
                    }
                },
                {
                    "name": "\u51b3\u7b56\u4e0e\u8fd0\u52a8\u89c4\u5212\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,91,123)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u56e2APP\u2014\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,43,130)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6316\u6398/\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,70,84)"
                        }
                    }
                },
                {
                    "name": "11312J-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,62,50)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u6d41\u5e7f\u544a-\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,132,106)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u5e94\u7528\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,106,68)"
                        }
                    }
                },
                {
                    "name": "00206-NLP\u9ad8\u7ea7\u5de5\u7a0b\u5e08/\u8d44\u6df1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,7,96)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5206\u6790\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,129,150)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7\u7b56\u7565\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,125,160)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5f81\u4fe1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,12,144)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9\u4e09\u7ef4\u9ad8\u7cbe\u5efa\u56fe\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,80,155)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u53f7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,59,89)"
                        }
                    }
                },
                {
                    "name": "1121PC-LT-354-\u5927\u6570\u636e\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,98,128)"
                        }
                    }
                },
                {
                    "name": "\u8bca\u65ad\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,142,30)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u63a7\u5236\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,70,148)"
                        }
                    }
                },
                {
                    "name": "113195-\u97f3\u89c6\u9891\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,149,32)"
                        }
                    }
                },
                {
                    "name": "2D/3D\u56fe\u5f62\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,92,41)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u7b56\u7565\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,80,35)"
                        }
                    }
                },
                {
                    "name": "\u6fc0\u5149\u5b9a\u4f4d\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,54,17)"
                        }
                    }
                },
                {
                    "name": "TX2980-SPBU-\u9ad8\u7ea7\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,117,90)"
                        }
                    }
                },
                {
                    "name": "\u5730\u56fe\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,23,71)"
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
                "\u9ad8\u7ea7\u7b97\u6cd5",
                "\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5",
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
        chart_d7721ad103e34051ab6322df22ea5d07.setOption(option_d7721ad103e34051ab6322df22ea5d07);
    </script>
                <div id="15c175c931ae472da08560676b8d5a86" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_15c175c931ae472da08560676b8d5a86 = echarts.init(
            document.getElementById('15c175c931ae472da08560676b8d5a86'), 'white', {renderer: 'canvas'});
            
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
    
        var option_15c175c931ae472da08560676b8d5a86 = {
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
                    "value": 250,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,27,115)"
                        }
                    }
                },
                {
                    "name": "\u516d\u9669\u4e00\u91d1",
                    "value": 121,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,21,152)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u5e74\u5047",
                    "value": 114,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,26,148)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u7a7a\u95f4\u5927",
                    "value": 103,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,34,101)"
                        }
                    }
                },
                {
                    "name": "\u5468\u672b\u53cc\u4f11",
                    "value": 85,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,145,27)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u5de5\u4f5c",
                    "value": 81,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,111,22)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u4f11",
                    "value": 68,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,2,16)"
                        }
                    }
                },
                {
                    "name": "\u8282\u65e5\u798f\u5229",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,86,88)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5e73\u53f0",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,47,0)"
                        }
                    }
                },
                {
                    "name": "\u4e0b\u5348\u8336",
                    "value": 59,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,69,73)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4\u597d",
                    "value": 58,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,38,114)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u5316\u7ba1\u7406",
                    "value": 55,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,11,120)"
                        }
                    }
                },
                {
                    "name": "\u7ee9\u6548\u5956\u91d1",
                    "value": 54,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,38,74)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956",
                    "value": 54,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,79,133)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5e02\u516c\u53f8",
                    "value": 45,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,15,144)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u725b",
                    "value": 45,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,147,124)"
                        }
                    }
                },
                {
                    "name": "\u80a1\u7968\u671f\u6743",
                    "value": 44,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,104,84)"
                        }
                    }
                },
                {
                    "name": "\u9910\u8865",
                    "value": 43,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,51,119)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f",
                    "value": 41,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,102,93)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4\u597d",
                    "value": 41,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,60,141)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u4e91\u96c6",
                    "value": 37,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,158,33)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u671f\u4f53\u68c0",
                    "value": 37,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,115,121)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u597d",
                    "value": 35,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,10,132)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u597d",
                    "value": 35,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,156,97)"
                        }
                    }
                },
                {
                    "value": 34,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,127,152)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u7ba1\u7406",
                    "value": 33,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,48,138)"
                        }
                    }
                },
                {
                    "name": "\u9886\u5bfcnice",
                    "value": 29,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,110,100)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u5e26\u961f",
                    "value": 28,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,141,128)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u597d",
                    "value": 27,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,133,132)"
                        }
                    }
                },
                {
                    "name": "\u5065\u8eab\u745c\u4f3d",
                    "value": 26,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,17,50)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd",
                    "value": 23,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,59,146)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u524d\u666f\u597d",
                    "value": 23,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,102,105)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u56e2\u961f",
                    "value": 22,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,123,75)"
                        }
                    }
                },
                {
                    "name": "\u671f\u6743\u6fc0\u52b1",
                    "value": 20,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,8,0)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u5927",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,111,26)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u7a7a\u95f4\u5927",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,159,0)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u5de5\u4f5c\u5236",
                    "value": 18,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,84,40)"
                        }
                    }
                },
                {
                    "name": "\u725b\u4eba\u56e2\u961f",
                    "value": 18,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,117,22)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u901f\u53d1\u5c55",
                    "value": 18,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,147,100)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u5316",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,111,134)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u6c1b\u56f4\u597d",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,77,108)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u591a",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,60,105)"
                        }
                    }
                },
                {
                    "name": "\u671f\u6743",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,108,62)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f\u7a7a\u95f4\u5927",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,0,156)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6c1b\u56f4\u597d",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,116,45)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u73ed\u8f66",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,3,52)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u5956\u91d1",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,18,128)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u91d1",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,140,93)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u5de5\u65f6",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,152,140)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u4e09\u9910",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,125,46)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u5927",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,141,40)"
                        }
                    }
                },
                {
                    "name": "\u8282\u5047\u65e5\u798f\u5229",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,21,78)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5b9e\u529b\u5f3a",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,2,117)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u5feb",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,42,16)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5382",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,15,5)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u9ad8\u5165\u804c\u5feb",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,42,69)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u624d\u623f\u7968",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,108,85)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u4e1a\u52a1",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,121,79)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u56e2\u961f",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,35,93)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u4f11\u5047",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,122,68)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u540d\u592e\u4f01",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,140,73)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u578b\u7814\u7a76\u9662",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,62,111)"
                        }
                    }
                },
                {
                    "name": "\u9886\u5bfc\u597d",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,140,127)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5e95\u53cc\u85aa",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,71,89)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,33,111)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u90e8\u95e8",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,53,154)"
                        }
                    }
                },
                {
                    "name": "16\u85aa",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,132,62)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u524d\u6cbf",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,133,12)"
                        }
                    }
                },
                {
                    "name": "\u4e0d\u6253\u5361",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,45,38)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u80cc\u666f\u4f18\u79c0",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,19,72)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u4f18\u79c0",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,77,38)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u597d",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,16,54)"
                        }
                    }
                },
                {
                    "name": "\u4e03\u9669\u4e00\u91d1",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,53,54)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u85aa",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,124,80)"
                        }
                    }
                },
                {
                    "name": "\u524d\u666f\u597d",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,43,3)"
                        }
                    }
                },
                {
                    "name": "\u79df\u623f\u8865\u8d34",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,137,120)"
                        }
                    }
                },
                {
                    "name": "\u80a1\u6743\u6fc0\u52b1",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,68,52)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7\u72ec\u89d2\u517d",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,128,76)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u7a7a\u95f4",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,145,57)"
                        }
                    }
                },
                {
                    "name": "\u6781\u5ba2\u6587\u5316",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,45,100)"
                        }
                    }
                },
                {
                    "name": "\u5c97\u4f4d\u664b\u5347",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,89,116)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u7ed9\u529b",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,30,68)"
                        }
                    }
                },
                {
                    "name": "\u7269\u8054\u7f51",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,73,154)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u7a7a\u95f4",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,93,60)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f\u7a7a\u95f4",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,59,59)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5347\u7a7a\u95f4\u5927",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,155,7)"
                        }
                    }
                },
                {
                    "name": "\u98de\u901f\u53d1\u5c55",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,40,32)"
                        }
                    }
                },
                {
                    "name": "\u7cbe\u82f1\u56e2\u961f",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,47,39)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5ea6\u4f53\u68c0",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,65,6)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5347\u7a7a\u95f4",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,56,40)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u4e0a\u73ed",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,68,3)"
                        }
                    }
                },
                {
                    "name": "\u7ee9\u6548\u5956",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,11,81)"
                        }
                    }
                },
                {
                    "name": "AI",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,45,14)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u539a\u5e74\u7ec8\u5956",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,3,41)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u79c0\u56e2\u961f",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,7,103)"
                        }
                    }
                },
                {
                    "name": "\u660e\u661f\u56e2\u961f",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,131,91)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961fnice",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,116,109)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u5efa",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,84,111)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u725b\u591a",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,145,98)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u4e0b\u5348\u8336",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,43,40)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u4e30\u539a",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,145,78)"
                        }
                    }
                },
                {
                    "name": "\u8bd5\u7528\u671f\u5168\u85aa",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,99,155)"
                        }
                    }
                },
                {
                    "name": "\u72ec\u89d2\u517d",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,145,136)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u9886\u5148",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,98,153)"
                        }
                    }
                },
                {
                    "name": "\u7a7a\u95f4\u5927",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,93,39)"
                        }
                    }
                },
                {
                    "name": "\u6709\u8f6c\u6b63\u673a\u4f1a",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,157,123)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u591a",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,43,110)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f\u5feb",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,116,127)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u4fbf\u5229",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,100,44)"
                        }
                    }
                },
                {
                    "name": "\u524d\u6cbf\u6280\u672f",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,40,43)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u91cf\u6570\u636e",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,151,30)"
                        }
                    }
                },
                {
                    "name": "\u804c\u4f4d\u664b\u5347",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,52,116)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u529e\u516c",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,73,144)"
                        }
                    }
                },
                {
                    "name": "\u5546\u4e1a\u822a\u5929\u884c\u4e1a\u524d\u666f\u826f\u597d",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,40,63)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u5185\u6280\u672f\u9886",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,71,74)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u9645\u5316\u6c1b\u56f4",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,7,84)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u4eba\u9a7e\u9a76",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,48,17)"
                        }
                    }
                },
                {
                    "name": "\u8865\u5145\u5546\u4e1a\u4fdd\u9669",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,41,158)"
                        }
                    }
                },
                {
                    "name": "\u5168\u989d\u4e94\u9669\u4e00\u91d1",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,53,51)"
                        }
                    }
                },
                {
                    "name": "\u9910\u8865\u7b49",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,85,20)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u6c1b\u56f4\u597d",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,21,91)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u5e7f\u9614",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,129,31)"
                        }
                    }
                },
                {
                    "name": "\u9886\u5bfcNICE",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,91,27)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u989d\u5e74\u7ec8",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,154,80)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u5de5\u4f5c\u65f6\u95f4",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,3,39)"
                        }
                    }
                },
                {
                    "name": "\u529e\u516c\u73af\u5883\u597d",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,147,105)"
                        }
                    }
                },
                {
                    "name": "\u5065\u8eab\u623f",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,1,121)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u5927\u725b\u591a",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,92,46)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u5feb",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,16,84)"
                        }
                    }
                },
                {
                    "name": "\u5065\u5168\u664b\u5347\u673a\u5236",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,120,131)"
                        }
                    }
                },
                {
                    "name": "\u5927\u843d\u5730\u573a\u666f",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,95,32)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u7a33\u5b9a",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,111,98)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,55,59)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u798f\u5229",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,148,99)"
                        }
                    }
                },
                {
                    "name": "12\u5929\u5e74\u5047",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,43,79)"
                        }
                    }
                },
                {
                    "name": "\u91cd\u70b9\u9879\u76ee",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,132,95)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u9f50\u5168",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,34,71)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u4e0e\u5b66\u4e60\u6c1b\u56f4\u3002",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,26,19)"
                        }
                    }
                },
                {
                    "name": "\u516c\u5f00\u516c\u6b63",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,104,12)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u5bfc\u5e08",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,94,34)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,7,82)"
                        }
                    }
                },
                {
                    "name": "\u826f\u597d\u53d1\u5c55\u8d8b\u52bf\u4e0e\u53d1\u5c55\u7a7a\u95f4",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,76,30)"
                        }
                    }
                },
                {
                    "name": "\u7814\u53d1\u4e2d\u5fc3",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,77,83)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u72ec\u89d2\u517d",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,8,158)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u9a71\u52a8",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,64,118)"
                        }
                    }
                },
                {
                    "name": "\u5927\u516c\u53f8",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,22,65)"
                        }
                    }
                },
                {
                    "name": "\u5168\u989d\u793e\u4fdd\u516c\u79ef\u91d1",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,34,15)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u989d\u5956\u91d1",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,74,0)"
                        }
                    }
                },
                {
                    "name": "\u51fa\u56fd\u65c5\u6e38",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,38,132)"
                        }
                    }
                },
                {
                    "name": "\u4e8b\u4e1a\u5355\u4f4d",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,37,18)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5927\u725b",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,59,3)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u5927\u725b",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,1,110)"
                        }
                    }
                },
                {
                    "name": "\u5730\u94c1\u5468\u8fb9",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,121,57)"
                        }
                    }
                },
                {
                    "name": "\u524d\u666f\u5e7f\u9614",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,112,112)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u671f\u56e2\u5efa",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,27,64)"
                        }
                    }
                },
                {
                    "name": "\u73ed\u8f66",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,155,20)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1\u5168\u989d",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,16,115)"
                        }
                    }
                },
                {
                    "name": "\u725b\u4eba\u4e91\u96c6",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,63,101)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5168",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,45,68)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u597d",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,59,72)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u597d",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,39,55)"
                        }
                    }
                },
                {
                    "name": "\u4e16\u754c\u4e94\u767e\u5f3a",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,27,42)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u591a\u591a",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,91,73)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u8865\u5145",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,120,115)"
                        }
                    }
                },
                {
                    "name": "\u6709\u517c\u804c\u5c97\u4f4d",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,121,34)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u4f18\u539a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,117,138)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u901f\u6210\u957f",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,141,81)"
                        }
                    }
                },
                {
                    "name": "\u843d\u6237\u5feb",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,145,91)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u6f5c\u529b",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,83,31)"
                        }
                    }
                },
                {
                    "name": "\u80a1\u4efd\u671f\u6743",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,22,123)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u4e0a\u4e0b\u73ed",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,82,22)"
                        }
                    }
                },
                {
                    "name": "\u6e05\u534e\u56e2\u961f",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,52,86)"
                        }
                    }
                },
                {
                    "name": "\u4f4f\u623f\u8865\u8d34",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,64,98)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u91d12-6\u4e2a\u6708",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,138,48)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5b8c\u5584",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,144,108)"
                        }
                    }
                },
                {
                    "name": "\u8f66\u5382\u5408\u4f5c",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,31,66)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4\u8f7b\u677e",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,80,59)"
                        }
                    }
                },
                {
                    "name": "\u671f\u6743\u5956\u52b1",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,20,60)"
                        }
                    }
                },
                {
                    "name": "\u751f\u65e5\u4f1a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,88,126)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u6210\u957f",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,55,12)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6c1b\u56f4\u6d53\u539a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,61,4)"
                        }
                    }
                },
                {
                    "name": "\u660e\u661f\u4ea7\u54c1",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,99,87)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u65c5\u6e38",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,114,59)"
                        }
                    }
                },
                {
                    "name": "\u8865\u5145\u533b\u7597",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,29,76)"
                        }
                    }
                },
                {
                    "name": "\u4f53\u68c0",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,30,92)"
                        }
                    }
                },
                {
                    "name": "\u5404\u79cd\u798f\u5229",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,24,34)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u5b66\u4e60",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,9,129)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u8fdc\u7a0b\u529e\u516c",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,88,137)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u6587\u5316\u597d",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,23,104)"
                        }
                    }
                },
                {
                    "name": "\u623f\u8865",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,45,124)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5ea6\u65c5\u6e38",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,87,55)"
                        }
                    }
                },
                {
                    "name": "\u521b\u4e1a\u56e2\u961f",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,88,126)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4\u4f73",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,97,102)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u665a\u9910",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,124,140)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c14\u6c1b\u597d",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,84,63)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u901f\u53d1\u5c55",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,142,56)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u7a0b\u5e08\u6587\u5316",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,0,84)"
                        }
                    }
                },
                {
                    "name": "AI\u673a\u5668\u4eba",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,103,92)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u8f7b\u56e2\u961f",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,98,135)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u8f6c\u6b63",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,54,61)"
                        }
                    }
                },
                {
                    "name": "8\u5929\u5e74\u5047",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,56,140)"
                        }
                    }
                },
                {
                    "name": "\u671f\u6743\u80a1\u7968",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,15,51)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7814\u56e2\u961f",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,86,109)"
                        }
                    }
                },
                {
                    "name": "\u673a\u4f1a\u591a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,135,88)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4nice",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,2,150)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c\u798f\u5229\u597d",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,123,33)"
                        }
                    }
                },
                {
                    "name": "\u4e16\u754c500\u5f3a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,134,75)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u4e0d\u9519",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,133,150)"
                        }
                    }
                },
                {
                    "name": "\u671d\u9633\u884c\u4e1a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,87,62)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u5c97\u4f4d",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,35,85)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u65e9\u9910",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,120,75)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u9ad8",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,53,61)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u5bb6\u5c45",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,45,156)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u524d\u6cbf",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,127,81)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5b9e\u529b",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,3,37)"
                        }
                    }
                },
                {
                    "name": "\u594b\u6597\u5956",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,155,104)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u65f6\u95f4",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,60,33)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u8fc7\u4ebf",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,73,119)"
                        }
                    }
                },
                {
                    "name": "\u4e0d\u52a0\u73ed",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,103,38)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u53d1\u5c55\u5f3a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,148,26)"
                        }
                    }
                },
                {
                    "name": "\u996d\u8865",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,56,93)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u53e3\u884c\u4e1a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,146,9)"
                        }
                    }
                },
                {
                    "name": "\u72ec\u89d2\u517d\u4f01\u4e1a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,62,149)"
                        }
                    }
                },
                {
                    "name": "\u7a7a\u95f4\u65e0\u9650",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,25,137)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,84,13)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u6f5c\u529b\u5927",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,124,35)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u6c14\u5341\u8db3",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,149,135)"
                        }
                    }
                },
                {
                    "name": "\u4e0d996",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,86,135)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u4e13\u4e1a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,43,64)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u6709\u524d\u666f",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,118,71)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u673a\u4f1a\u591a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,13,156)"
                        }
                    }
                },
                {
                    "name": "\u9910\u8d39\u8865\u8d34",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,135,37)"
                        }
                    }
                },
                {
                    "name": "\u671d\u4e5d\u665a\u516d",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,142,86)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5e95\u5956\u91d1",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,65,116)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6280\u672f\u884c\u4e1a\u9886\u5148",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,70,119)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u9f99\u5934",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,125,58)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u5e76\u53d1\u7cfb\u7edf",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,59,75)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u5e73\u53f0",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,17,116)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,28,143)"
                        }
                    }
                },
                {
                    "name": "\u51fa\u56fd\u57f9\u8bad",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,82,5)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u53d1\u5c55\u597d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,119,114)"
                        }
                    }
                },
                {
                    "name": "\u7a33\u5b9a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,88,103)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u901f\u6210\u957f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,111,71)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u574718\u85aa",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,31,145)"
                        }
                    }
                },
                {
                    "name": "\u91cd\u70b9\u4e1a\u52a1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,71,147)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5f52\u56e2\u961f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,137,130)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u524d\u666f\u597d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,74,152)"
                        }
                    }
                },
                {
                    "name": "\u6cd5\u5b9a\u8282\u5047\u65e5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,30,81)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u52b1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,67,96)"
                        }
                    }
                },
                {
                    "name": "\u8865\u5145\u5546\u4fdd",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,69,67)"
                        }
                    }
                },
                {
                    "name": "\u7b7e\u5b57\u73b0\u91d1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,95,136)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u75c5\u5047",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,129,40)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u68d2\u7684\u9886\u5bfc",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,80,71)"
                        }
                    }
                },
                {
                    "name": "\u5165\u804c\u80a1\u7968",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,104,124)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c\u798f\u5229",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,129,100)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u4e09\u9910",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,55,54)"
                        }
                    }
                },
                {
                    "name": "\u72ec\u89d2\u517d\u516c\u53f8",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,125,26)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5bfc\u5411",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,105,10)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4fdd\u516c\u79ef\u91d1\u5b9e\u4ea4",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,159,74)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u4e1a\u52a1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,40,26)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u5e74\u4f11\u5047",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,150,156)"
                        }
                    }
                },
                {
                    "name": "15\u85aa",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,74,16)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c\u798f\u5229\u4f73",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,133,152)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u725b\u7684\u6280\u672f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,23,3)"
                        }
                    }
                },
                {
                    "name": "\u7ee9\u6548\u80a1\u7968",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,142,95)"
                        }
                    }
                },
                {
                    "name": "\u5e02\u573a\u5316\u85aa\u916c",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,135,157)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c\u6fc0\u52b1\u8ba1\u5212",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,22,13)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u7cbe\u6e5b",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,128,123)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u6709\u5927\u884c\u76f4\u9500\u94f6\u884c",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,136,118)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,90,77)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,23,76)"
                        }
                    }
                },
                {
                    "name": "\u7814\u53d1\u5f00\u653e\u73af\u5883",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,77,99)"
                        }
                    }
                },
                {
                    "name": "\u6311\u6218\u5927",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,88,30)"
                        }
                    }
                },
                {
                    "name": "\u4f9b\u5e94\u94fe",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,142,45)"
                        }
                    }
                },
                {
                    "name": "\u611f\u77e5\u9636\u8dc3\u730e\u5934\u804c\u4f4d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,9,104)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1\u5168\u989d\u7f34\u7eb3",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,14,111)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5348\u9910",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,129,26)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u4f18",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,26,118)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u884c\u4e1a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,153,14)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u5236\u5ea6\u5b8c\u5584",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,49,141)"
                        }
                    }
                },
                {
                    "name": "\u672a\u6765\u53ef\u671f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,25,97)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5047",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,32,78)"
                        }
                    }
                },
                {
                    "name": "\u5343\u4e07\u7ea7\u7528\u6237",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,9,59)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u524d\u666f\u597d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,112,109)"
                        }
                    }
                },
                {
                    "name": "\u516d\u9669\u4e8c\u91d1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,6,49)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u5f85\u9047\u4f18\u8d8a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,103,132)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u6325\u6240\u957f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,133,158)"
                        }
                    }
                },
                {
                    "name": "14\u85aa",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,83,109)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u652f\u6301\u7ed9\u529b",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,45,123)"
                        }
                    }
                },
                {
                    "name": "\u5348\u9910\u8865\u52a9",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,17,43)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u9614\u53d1\u5c55\u7a7a\u95f4",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,71,73)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e8c\u91d1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,87,22)"
                        }
                    }
                },
                {
                    "name": "\u4e0d\u5f3a\u5236\u52a0\u73ed",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,155,154)"
                        }
                    }
                },
                {
                    "name": "\u7cbe\u6e5b\u7684\u56e2\u961f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,62,155)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4\u6d3b\u8dc3",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,75,76)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u65b0",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,6,23)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u9645\u5316\u56e2\u961f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,8,150)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u9ad8",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,59,14)"
                        }
                    }
                },
                {
                    "name": "\u98df\u5802",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,10,130)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u4f01",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,45,143)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u9ad8",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,59,53)"
                        }
                    }
                },
                {
                    "name": "\u524d\u666f\u53ef\u89c2",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,6,143)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u68d2",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,4,75)"
                        }
                    }
                },
                {
                    "name": "base",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,24,73)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u96f6\u98df",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,129,61)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u4f18\u539a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,147,77)"
                        }
                    }
                },
                {
                    "name": "\u52a0\u73ed\u5c11",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,136,76)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6709\u7231",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,96,1)"
                        }
                    }
                },
                {
                    "name": "\u6280\u80fd\u57f9\u8bad",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,80,89)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,88,159)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u9879\u76ee",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,39,42)"
                        }
                    }
                },
                {
                    "name": "\u72ec\u5f53\u4e00\u9762",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,32,59)"
                        }
                    }
                },
                {
                    "name": "\u521b\u65b0\u4e1a\u52a1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,44,108)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u4f1a\u7a7a\u95f4\u5927",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,81,67)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u5bcc\u9879\u76ee\u7ecf\u9a8c",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,82,60)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u4e1a\u56e2\u961f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,70,121)"
                        }
                    }
                },
                {
                    "name": "\u9910\u996e\u8865\u8d34",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,46,79)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u8fdb\u597d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,154,41)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u80fd\u529b\u5f3a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,91,84)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u65b9\u4fbf",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,150,70)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,19,93)"
                        }
                    }
                },
                {
                    "name": "\u591f\u6311\u6218\u591f\u523a\u6fc0",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,4,33)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u9ad8",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,141,40)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4\u73af\u5883\u597d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,109,27)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u7ebf\u798f\u5229",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,7,72)"
                        }
                    }
                },
                {
                    "name": "\u5168\u989d\u516c\u79ef\u91d1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,81,13)"
                        }
                    }
                },
                {
                    "name": "\u8001\u677fNice",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,135,73)"
                        }
                    }
                },
                {
                    "name": "\u8fc7\u8282\u8d39",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,72,115)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44OPEN",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,124,16)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u7a33\u5b9a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,131,118)"
                        }
                    }
                },
                {
                    "name": "\u8282\u5047\u65e5\u798f\u5229\u7b49",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,131,157)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u878d\u6d3d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,29,114)"
                        }
                    }
                },
                {
                    "name": "\u66f9\u64cd\u51fa\u884c",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,16,52)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5e95\u591a\u85aa",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,101,82)"
                        }
                    }
                },
                {
                    "name": "\u54e5\u5927",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,155,13)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u7a7a\u95f4\u5927",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,17,59)"
                        }
                    }
                },
                {
                    "name": "\u8f6c\u6b63\u673a\u4f1a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,117,58)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6210\u957f\u671f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,64,98)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5206\u7ea2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,89,74)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u9645\u5316\u5e73\u53f0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,107,24)"
                        }
                    }
                },
                {
                    "name": "\u521b\u65b0\u9879\u76ee",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,57,63)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u5f85\u9047\u597d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,47,31)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u7ebf\u5e7f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,88,65)"
                        }
                    }
                },
                {
                    "name": "\u5065\u8eab\u798f\u5229",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,43,104)"
                        }
                    }
                },
                {
                    "name": "\u963f\u91cc\u5e73\u53f0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,138,73)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u80fd\u529b\u5f3a\u3002",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,88,17)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u589e\u957f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,127,89)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u5185\u9886\u5148\u91d1\u878d\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,54,79)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u540d\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,109,56)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u7a33\u5b9a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,116,129)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u5e76\u53d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,47,120)"
                        }
                    }
                },
                {
                    "name": "\u73af\u5883\u8212\u9002",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,106,124)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5496\u4e91\u96c6",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,100,122)"
                        }
                    }
                },
                {
                    "name": "\u3010\u5929\u773c\u67e5\u3011\u730e\u5934\u804c\u4f4d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,158,116)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u5e73\u53f0\u5927",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,75,102)"
                        }
                    }
                },
                {
                    "name": "\u9910\u8865\u4ea4\u8865",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,45,21)"
                        }
                    }
                },
                {
                    "name": "P7+\u53ef\u4eab\u53d7\u963f\u91cc\u80a1\u7968",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,54,81)"
                        }
                    }
                },
                {
                    "name": "\u9760\u8c31\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,158,153)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u901a\u9053\u5b8c\u5584",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,18,68)"
                        }
                    }
                },
                {
                    "name": "\u5546\u4e1a\u4fdd\u9669",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,118,152)"
                        }
                    }
                },
                {
                    "name": "14-20\u85aa",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,45,90)"
                        }
                    }
                },
                {
                    "name": "\u5168\u7403\u5316",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,17,75)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6280\u672f\u6c1b\u56f4\u597d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,134,49)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u6c11APP",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,66,103)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u597d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,119,42)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5065\u8eab\u623f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,60,59)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u9886\u5148",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,91,92)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7531",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,74,38)"
                        }
                    }
                },
                {
                    "name": "\u73af\u5883\u597d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,127,137)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u5bbf\u820d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,160,135)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u7814\u7a76",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,3,114)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u5f8b\u5185\u9a71",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,24,67)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u6709\u7ade\u4e89\u529b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,95,135)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u4e0a\u5e02\u9884\u671f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,63,72)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u7ebf\u98ce\u6295",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,117,81)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u5973\u591a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,149,113)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u5185\u77e5\u540d\u4e0a\u5e02\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,67,134)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u4e30\u539a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,79,112)"
                        }
                    }
                },
                {
                    "name": "\u793e\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,90,74)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u673a\u4f1a\u591a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,106,62)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5496\u5e26\u961f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,122,74)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u65b0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,98,133)"
                        }
                    }
                },
                {
                    "name": "\u7cbe\u82f1\u6587\u5316",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,138,127)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u6027\u5316\u7ba1\u7406",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,120,22)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5ea6\u52a0\u85aa",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,2,136)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u5956\u91d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,69,141)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5b9e\u529b\u96c4\u539a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,132,56)"
                        }
                    }
                },
                {
                    "name": "13\u85aa",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,80,29)"
                        }
                    }
                },
                {
                    "name": "\u5404\u9879\u8865\u8d34",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,22,76)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u5e73\u53f0\u53d1\u5c55\u5feb",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,102,119)"
                        }
                    }
                },
                {
                    "name": "\u6bcf\u5468\u56e2\u5efa",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,55,143)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u6253\u5361",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,85,53)"
                        }
                    }
                },
                {
                    "name": "\u8fd1\u5730\u94c1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,150,3)"
                        }
                    }
                },
                {
                    "name": "2-6\u4e2a\u6708\u5e74\u7ec8\u5956",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,133,131)"
                        }
                    }
                },
                {
                    "name": "\u524d\u666f\u5e7f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,143,158)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5065\u8eab\u623f\u7406\u53d1\u5e97",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,149,68)"
                        }
                    }
                },
                {
                    "name": "\u5305\u4e09\u9910",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,75,117)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u5927\u4e0a\u73af\u5883",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,50,70)"
                        }
                    }
                },
                {
                    "name": "\u73ed\u8f66\u63a5\u9001",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,34,108)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u5168\u9762",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,109,15)"
                        }
                    }
                },
                {
                    "name": "6\u96692\u91d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,63,113)"
                        }
                    }
                },
                {
                    "name": "\u5404\u79cd\u8865\u8d34",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,3,104)"
                        }
                    }
                },
                {
                    "name": "\u6bcf\u5e74\u8c03\u85aa",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,100,59)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u80a1\u4e0a\u5e02",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,52,133)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u6548\u56e2\u961f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,115,25)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6311\u6218",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,125,34)"
                        }
                    }
                },
                {
                    "name": "\u51fa\u56fd\u6e38",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,74,84)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u524d\u666f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,146,102)"
                        }
                    }
                },
                {
                    "name": "\u516c\u5e73\u516c\u6b63",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,48,141)"
                        }
                    }
                },
                {
                    "name": "\u6e05\u534e\u6d59\u5927",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,120,95)"
                        }
                    }
                },
                {
                    "name": "\u529e\u516c\u73af\u5883\u4f18\u8d8a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,34,98)"
                        }
                    }
                },
                {
                    "name": "\u521b\u4e1a\u6fc0\u60c5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,156,96)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u8865",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,24,98)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u524d\u77bb\u6280\u672f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,10,106)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4nice",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,61,94)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u591a\u591a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,153,106)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u5956",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,110,11)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u591a\u5927\u725b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,126,134)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5065\u8eab/\u96f6\u98df",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,83,141)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u8865\u8d34",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,123,76)"
                        }
                    }
                },
                {
                    "name": "\u5177\u6709\u7ade\u4e89\u529b\u7684\u85aa\u8d44\u6c34\u5e73",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,4,100)"
                        }
                    }
                },
                {
                    "name": "AI\u97f3\u4e50",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,31,157)"
                        }
                    }
                },
                {
                    "name": "2D",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,40,134)"
                        }
                    }
                },
                {
                    "name": "\u817e\u8baf\u4e91",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,97,132)"
                        }
                    }
                },
                {
                    "name": "\u96c6\u56e2\u80cc\u666f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,123,71)"
                        }
                    }
                },
                {
                    "name": "\u4e24\u9910\u8865\u8d34",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,146,9)"
                        }
                    }
                },
                {
                    "name": "D\u8f6e\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,87,71)"
                        }
                    }
                },
                {
                    "name": "\u591a\u6b21\u8c03\u85aa",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,51,22)"
                        }
                    }
                },
                {
                    "name": "\u65af\u5766\u798f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,4,42)"
                        }
                    }
                },
                {
                    "name": "\u9e45\u5382\u798f\u5229/\u5065\u8eab\u623f/\u73ed\u8f66/\u5468\u672b\u53cc\u4f11",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,84,64)"
                        }
                    }
                },
                {
                    "name": "\u672a\u6765\u8d8b\u52bf",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,80,158)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u725b\u56e2\u961f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,14,79)"
                        }
                    }
                },
                {
                    "name": "\u6e05\u534e\u5927\u5b66\u7684\u667a\u80fd\u8fd0\u7ef4\u5b9e\u9a8c\u5ba4",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,1,8)"
                        }
                    }
                },
                {
                    "name": "\u8f7b\u677e\u6d3b\u8dc3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,71,63)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c\u5f85\u9047\u4f18",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,58,52)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u524d\u666f\u5e7f\u9614",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,75,62)"
                        }
                    }
                },
                {
                    "name": "\u505a\u4e94\u4f11\u4e8c",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,39,121)"
                        }
                    }
                },
                {
                    "name": "\u5065\u5eb7\u4f53\u68c0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,159,127)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,42,24)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u6325\u7a7a\u95f4\u5927",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,91,22)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u5916\u5408\u8d44",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,158,139)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u4e0a\u5e02\u671f\u6743\u591a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,151,151)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u798f\u5229\u597d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,66,90)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f\u5feb\u901f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,76,2)"
                        }
                    }
                },
                {
                    "name": "\u521b\u65b0\u4e1a\u52a1\u573a\u666f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,139,159)"
                        }
                    }
                },
                {
                    "name": "\u7ba1\u7406\u89c4\u8303",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,73,112)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u5021\u8ffd\u6c42\u5353\u8d8a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,103,62)"
                        }
                    }
                },
                {
                    "name": "\u826f\u597d\u7684\u6280\u672f\u6c1b\u56f4",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,53,87)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u91cf\u5927",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,99,41)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u8fc5\u901f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,149,24)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u9910",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,14,160)"
                        }
                    }
                },
                {
                    "name": "\u6781\u5177\u7ade\u4e89\u529b\u7684\u85aa\u8d44\u5f85\u9047",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,123,137)"
                        }
                    }
                },
                {
                    "name": "Geek\u6587\u5316",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,126,35)"
                        }
                    }
                },
                {
                    "name": "\u516d\u65e5\u53cc\u4f11",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,152,133)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79\u5b66",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,83,38)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u53e3\u6d6a\u5c16",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,67,39)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5927\u725b\u4f17\u591a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,118,108)"
                        }
                    }
                },
                {
                    "name": "\u901a\u8baf\u8865\u8d34",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,3,98)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u5e7f\u9614",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,82,99)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5f3a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,144,158)"
                        }
                    }
                },
                {
                    "name": "\u6301\u724c\u673a\u6784",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,101,107)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u901a\u9053",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,125,34)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u900f\u660e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,29,65)"
                        }
                    }
                },
                {
                    "name": "base*13+0-6\u4e2a\u6708\u5e74\u7ec8\u5956\u91d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,120,66)"
                        }
                    }
                },
                {
                    "name": "\u5b63\u5ea6\u5168\u85aa\u75c5\u5047",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,24,127)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u65e0\u9650",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,70,42)"
                        }
                    }
                },
                {
                    "name": "\u94f6\u884c\u80cc\u666f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,125,66)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u98df\u5802",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,9,2)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5f3a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,62,94)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4\u878d\u6d3d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,16,128)"
                        }
                    }
                },
                {
                    "name": "\u65e9\u9910\u52a0\u73ed\u9910",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,101,95)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u4f73",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,73,89)"
                        }
                    }
                },
                {
                    "name": "\u6ef4\u6ef4\u6253\u8f66",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,30,58)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u7a7a\u95f4\u597d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,138,136)"
                        }
                    }
                },
                {
                    "name": "\u5f3a\u52b2\u535a\u58eb\u56e2\u961f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,112,12)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u822c16\u85aa\u4ee5\u4e0a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,123,59)"
                        }
                    }
                },
                {
                    "name": "\u8d8b\u52bf\u8d5b\u9053",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,51,125)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,38,59)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u798f\u5229\u4f73",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,82,14)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u5bcc\u4e0b\u5348\u8336",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,45,128)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u843d\u5730",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,40,111)"
                        }
                    }
                },
                {
                    "name": "\u5468\u672b\u52a0\u73ed\u53cc\u500d\u5de5\u8d44",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,19,49)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u5e73\u53f0\u5927",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,159,104)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u9879\u76ee",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,44,41)"
                        }
                    }
                },
                {
                    "name": "\u516d\u9669\u4e00\u91d1\u5168\u989d\u7f34\u7eb3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,66,109)"
                        }
                    }
                },
                {
                    "name": "\u5f3a\u5927\u798f\u5229",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,93,70)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u751f\u65e5\u798f\u5229",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,96,1)"
                        }
                    }
                },
                {
                    "name": "offer14\u85aa",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,43,9)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f/\u85aa\u8d44\u798f\u5229",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,81,82)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,71,20)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6c1b\u56f4\u5f3a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,141,158)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u85aa\u8d44",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,130,32)"
                        }
                    }
                },
                {
                    "name": "\u524d\u6cbf\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,10,18)"
                        }
                    }
                },
                {
                    "name": "AI\u82af\u7247",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,43,79)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u6e38\u57fa\u91d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,50,130)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u6280\u672f\u9886\u5148",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,54,31)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4\u4f73",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,18,63)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u524d\u666f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,43,58)"
                        }
                    }
                },
                {
                    "name": "\u989c\u503c\u9ad8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,129,118)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u665a\u9910",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,150,93)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u7a33\u5b9a+\u6210\u957f\u664b\u5347+\u6280\u672f\u9a71\u52a8+\u80a1\u7968\u6fc0\u52b1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,67,53)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u6280\u672f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,152,39)"
                        }
                    }
                },
                {
                    "name": "\u6d25\u8d34\u8865\u52a9",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,44,32)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,7,147)"
                        }
                    }
                },
                {
                    "name": "\u6253\u8f66\u62a5\u9500",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,139,37)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u91d1+\u5b63\u5ea6\u5956\u91d1+\u597d\u5fc3\u60c5+\u798f\u5229\u591a\u591a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,139,102)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u98df\u996e\u6599",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,94,125)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u8f7b\u5316",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,111,138)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5e74\u8f7b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,48,46)"
                        }
                    }
                },
                {
                    "name": "\u9910\u8865\u8bdd\u8865",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,92,154)"
                        }
                    }
                },
                {
                    "name": "\u8865\u5145\u516c\u79ef\u91d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,62,127)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u957f\u5e74\u5047",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,49,8)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6c1b\u56f4\u6d53",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,123,9)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u7a7a\u95f4\u5927\u3002",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,37,25)"
                        }
                    }
                },
                {
                    "name": "IOT\u9886\u5148\u4f01\u4e1a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,116,120)"
                        }
                    }
                },
                {
                    "name": "\u5317\u5927\u540d\u6821\u540c\u4e8b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,59,140)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5348\u665a\u9910",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,148,150)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u4e2d\u53f0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,100,153)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5ea6\u664b\u5347",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,146,22)"
                        }
                    }
                },
                {
                    "name": "\u8bdd\u8865",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,110,138)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u798f\u5229",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,150,92)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u7ea2\u4e66",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,95,97)"
                        }
                    }
                },
                {
                    "name": "\u5730\u94c1\u4e0a\u76d6",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,12,155)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u4f4f\u5bbf",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,148,113)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u9645\u5316",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,62,69)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u53d1\u5c55\u5feb",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,109,77)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u5185TOP3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,12,43)"
                        }
                    }
                },
                {
                    "name": "\u6e05\u534e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,134,151)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u65c5\u6e38",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,133,53)"
                        }
                    }
                },
                {
                    "name": "3D\u89c6\u89c9\u6210\u50cf",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,89,129)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u6838\u5fc3\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,121,120)"
                        }
                    }
                },
                {
                    "name": "2\u4f4d\u9662\u58eb\u9886\u8854",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,140,47)"
                        }
                    }
                },
                {
                    "name": "\u5b9e\u529b\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,46,155)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u53d1\u5c55\u5feb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,145,96)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f\u6c1b\u56f4\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,21,134)"
                        }
                    }
                },
                {
                    "name": "\u7ee9\u6548\u85aa\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,147,151)"
                        }
                    }
                },
                {
                    "name": "\u7d2b\u5149\u96c6\u56e2\u65d7\u4e0b\u6559\u80b2\u4fe1\u606f\u5316\u5934\u90e8\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,41,104)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1(\u6700\u9ad8\u6bd4\u4f8b)",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,158,153)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,28,137)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u5927\u725b\u4e91\u96c6\u9879\u76ee\u5956\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,14,138)"
                        }
                    }
                },
                {
                    "name": "**\u533b\u9662\u5408\u4f5c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,20,71)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u798f\u5229\u4f18",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,20,7)"
                        }
                    }
                },
                {
                    "name": "\u811a\u8e0f\u5b9e\u5730",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,10,28)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u901f\u53d1\u5c55\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,84,140)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u79d1\u6280\u884c\u4e1aTOP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,136,41)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6210\u5458\u6765\u81eaBATJ\u7b49\u4e00\u7ebf\u5927\u5382",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,31,64)"
                        }
                    }
                },
                {
                    "name": "0-1\u65b0\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,117,28)"
                        }
                    }
                },
                {
                    "name": "\uff08\u77f3\u5934\u79d1\u6280\uff09\u730e\u5934\u804c\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,112,142)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u80fd\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,22,94)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u9886\u57df\u7684\u4eba\u5de5\u667a\u80fd\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,6,8)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u7ed9\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,22,25)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u53d1\u5c55\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,84,94)"
                        }
                    }
                },
                {
                    "name": "\u7ee9\u6548\u5956\u52b1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,126,38)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,123,108)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u7ba1\u7406\u9f13\u52b1\u8bd5\u9519",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,30,77)"
                        }
                    }
                },
                {
                    "name": "\u5f00\u653e\u578b\u6587\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,44,16)"
                        }
                    }
                },
                {
                    "name": "\u535a\u58eb\u843d\u6237",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,138,157)"
                        }
                    }
                },
                {
                    "name": "\u5b8c\u5584\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,46,144)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6280\u672f\u5927\u5496\u4e91\u96c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,19,97)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u6210\u719f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,151,93)"
                        }
                    }
                },
                {
                    "name": "\u8282\u65e5\u7ea2\u5305",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,46,61)"
                        }
                    }
                },
                {
                    "name": "\u98df\u5802\u7528\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,20,38)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u7a7a\u95f4\u5e7f\u9614",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,15,53)"
                        }
                    }
                },
                {
                    "name": "\u4f01\u4e1a\u5feb\u901f\u6210\u957f\u671f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,92,109)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u914d\u7f6e\u671f\u6743",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,94,148)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u98df\u81ea\u7531",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,101,105)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u5236\u9020",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,96,141)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u5b66\u4e60\u7b97\u6cd5\u5de5\u7a0b\u5e08",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,77,113)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5e02\u5238\u5546",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,108,157)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u524d\u666f\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,47,26)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5a92\u4f53/\u7535\u89c6\u53f0/\u4e92\u8054\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,66,108)"
                        }
                    }
                },
                {
                    "name": "\u975e\u5916\u5305",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,108,68)"
                        }
                    }
                },
                {
                    "name": "\u529f\u8bfe\u6280\u672f\u524d\u6cbf\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,136,96)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u7a33\u5b9a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,69,63)"
                        }
                    }
                },
                {
                    "name": "\u4eab\u6709\u80a1\u6743\u6fc0\u52b1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,67,37)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u5c97\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,63,118)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u7814\u548c\u5e94\u7528\u7ed3\u5408",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,95,95)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5a92\u4f53",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,6,100)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u5357\u4e9a\u5e02\u573a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,45,146)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u6e29\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,89,112)"
                        }
                    }
                },
                {
                    "name": "\u653f\u5e9c\u91cd\u70b9\u652f\u6301\u9879\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,104,72)"
                        }
                    }
                },
                {
                    "name": "\u524d\u6cbf\u9886\u57df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,113,110)"
                        }
                    }
                },
                {
                    "name": "\u7ef4\u5ea6\u964d\u4f4e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,137,106)"
                        }
                    }
                },
                {
                    "name": "\u4f01\u4e1a\u6c1b\u56f4\u7b80\u5355",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,54,34)"
                        }
                    }
                },
                {
                    "name": "\u5185\u90e8\u53d1\u5c55\u7a7a\u95f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,14,104)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5916\u5e02\u573a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,107,53)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u63a8\u8350",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,86,31)"
                        }
                    }
                },
                {
                    "name": "ipo",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,45,155)"
                        }
                    }
                },
                {
                    "name": "\u805a\u7126\u524d\u6cbf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,12,155)"
                        }
                    }
                },
                {
                    "name": "\u65e9\u4e5d\u665a\u516d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,63,125)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u4f11\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,28,140)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u4f18",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,79,157)"
                        }
                    }
                },
                {
                    "name": "\u8d1f\u8d23\u4eba\u5e26\u65b0\u624b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,43,104)"
                        }
                    }
                },
                {
                    "name": "\u51fa\u56fd\u56e2\u5efa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,124,58)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u6311\u6218",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,114,20)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u4f53\u68c0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,82,87)"
                        }
                    }
                },
                {
                    "name": "\u6bcf\u5e74\u591a\u6b21\u8c03\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,155,154)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u4e60\u7a7a\u95f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,65,111)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4\u5411\u4e0a\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,62,20)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u5185\u53e3\u7891",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,92,14)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u672a\u6765\u91cd\u70b9\u53d1\u5c55\u6295\u5165",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,28,60)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u4e8b\u5047\u4e94\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,139,106)"
                        }
                    }
                },
                {
                    "name": "\u9633\u5149\u900f\u660e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,133,49)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u9ad8\u798f\u5229\u597d\u5927\u725b\u8eab\u8fb9\u7ed5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,130,121)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u5e26\u9886",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,95,120)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u8c03\u5ea6\u4f18\u5316\u5f15\u64ce\u7684\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,113,146)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5047\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,113,42)"
                        }
                    }
                },
                {
                    "name": "\u9f13\u52b1\u521b\u65b0\u7684\u5de5\u4f5c\u73af\u5883",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,26,63)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u4e2a\u5c97\u4f4d\u6210\u5c31\u4e00\u756a\u4e8b\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,152,92)"
                        }
                    }
                },
                {
                    "name": "\u4f60\u7684\u4ee3\u7801\u5c06\u5f71\u54cd\u6570\u4ebf\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,66,139)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5e95\u53cc\u85aa-\u5e74\u7ec8\u5956-\u6241\u5e73\u5316\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,111,114)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u7814\u53d1\u5b9e\u529b\u96c4\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,73,128)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u73af\u5883",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,155,137)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u4f53\u7cfb\u5b8c\u5584",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,38,54)"
                        }
                    }
                },
                {
                    "name": "\u6709\u6d3b\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,30,76)"
                        }
                    }
                },
                {
                    "name": "\u5185\u90e8\u5b75\u5316\u9879\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,136,90)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u5bfc\u5e08\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,53,115)"
                        }
                    }
                },
                {
                    "name": "\u73af\u5883\u8d85\u68d2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,83,32)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c\u5f85\u9047\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,113,21)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u4f73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,0,25)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77/\u6b66\u6c49",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,110,30)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u7a33\u5b9a\u5feb\u901f\u589e\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,107,139)"
                        }
                    }
                },
                {
                    "name": "\u5305\u5403\u4f4f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,140,75)"
                        }
                    }
                },
                {
                    "name": "\u804c\u4e1a\u5927\u725b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,126,40)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5e95\u635e\u534a\u4ef7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,84,15)"
                        }
                    }
                },
                {
                    "name": "\u5bfc\u5e08\u4e00\u5e26\u4e00",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,70,41)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5927\u795e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,9,117)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6167\u57ce\u5e02",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,24,15)"
                        }
                    }
                },
                {
                    "name": "\u610f\u5916\u8865\u52a9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,50,98)"
                        }
                    }
                },
                {
                    "name": "\u8db3\u989d\u4fdd\u9669\u516c\u79ef\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,93,120)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u4f01\u80cc\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,20,33)"
                        }
                    }
                },
                {
                    "name": "\u9910\u8865\u623f\u8865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,107,127)"
                        }
                    }
                },
                {
                    "name": "AI\u573a\u666f\u4e30\u5bcc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,72,157)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,132,117)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u540d\u5927\u5382\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,152,85)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u5496\u5e26\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,7,129)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u98df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,58,14)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,32,45)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u65b0\u9896",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,33,38)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u89c4\u6a21\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,3,45)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5916\u9879\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,35,41)"
                        }
                    }
                },
                {
                    "name": "\u725b\u4eba\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,50,60)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1\u3002\u5e26\u85aa\u5e74\u5047\u3002\u798f\u5229\u597d\u5f85\u9047\u4f73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,14,68)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4\u68d2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,119,134)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5f52\u79d1\u7814\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,116,119)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u53d1\u5c55\u5feb\u901f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,101,43)"
                        }
                    }
                },
                {
                    "name": "\u5c31\u6765\u641c\u72d7\u5546\u4e1a\u641c\u7d22\u5427\uff01",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,155,110)"
                        }
                    }
                },
                {
                    "name": "\u573a\u666f\u4e30\u5bcc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,92,93)"
                        }
                    }
                },
                {
                    "name": "1.\u56e2\u961f\u4e1a\u52a1\u7d27\u8ddf\u96c6\u56e2\u7684\u4e1a\u52a1\u76ee\u6807",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,74,114)"
                        }
                    }
                },
                {
                    "name": "\u5bfc\u5e08\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,30,131)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u53d1\u5c55\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,111,44)"
                        }
                    }
                },
                {
                    "name": "\u5c97\u4f4d\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,147,148)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u521b\u65b0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,95,103)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u524d\u666f\u8d5e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,126,64)"
                        }
                    }
                },
                {
                    "name": "\u6d41\u91cf\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,32,32)"
                        }
                    }
                },
                {
                    "name": "\u524d\u666f\u53ef\u89c2\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,47,93)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u4e60\u73af\u5883\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,19,30)"
                        }
                    }
                },
                {
                    "name": "Pro\u529e\u516c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,43,36)"
                        }
                    }
                },
                {
                    "name": "\u524d\u6cbf\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,53,98)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u540c\u4e8bnice",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,138,145)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u9910\u98df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,82,105)"
                        }
                    }
                },
                {
                    "name": "\u7855\u58eb\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,0,121)"
                        }
                    }
                },
                {
                    "name": "\u4ece0\u52301",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,68,88)"
                        }
                    }
                },
                {
                    "name": "500\u5f3a\u7814\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,43,137)"
                        }
                    }
                },
                {
                    "name": "\u5168\u5458mac",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,61,11)"
                        }
                    }
                },
                {
                    "name": "\u6e05\u534e\u59da\u73edleader\u5e26\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,118,31)"
                        }
                    }
                },
                {
                    "name": "\u6ce8\u91cd\u4e2a\u4eba\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,104,36)"
                        }
                    }
                },
                {
                    "name": "\u5468\u672b\u53cc\u4f11/\u5e26\u85aa\u5e74\u5047/\u5168\u989d\u4e94\u9669\u4e00\u91d1/\u4e0a\u5e02\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,77,119)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,94,30)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7814\u7b97\u6cd5\u4ea7\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,72,18)"
                        }
                    }
                },
                {
                    "name": "\u521b\u65b0\u5e94\u7528",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,125,50)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u989d\u9910\u8865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,131,110)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u7814\u53d1\u5b9e\u529b\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,118,49)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u5bb6\u91cd\u70b9\u65b9\u5411",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,119,60)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u901f\u5ea6\u5feb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,15,59)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u9738",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,150,110)"
                        }
                    }
                },
                {
                    "name": "\u5b63\u5ea6\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,160,153)"
                        }
                    }
                },
                {
                    "name": "\u6709\u671f\u6743",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,72,52)"
                        }
                    }
                },
                {
                    "name": "\u80cc\u666f\u6280\u672f\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,126,2)"
                        }
                    }
                },
                {
                    "name": "B2B\u91d1\u878d\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,48,122)"
                        }
                    }
                },
                {
                    "name": "\u8c03\u85aa\u673a\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,118,159)"
                        }
                    }
                },
                {
                    "name": "NLP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,149,116)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u539a\u5e74\u7ec8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,62,106)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u4e13\u5bb6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,13,44)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u4ece\u4f18",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,80,121)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u9650\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,103,128)"
                        }
                    }
                },
                {
                    "name": "\u5c11\u52a0\u73ed",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,74,75)"
                        }
                    }
                },
                {
                    "name": "\u52a0\u73ed\u4ea4\u8865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,143,116)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5e95\u635e\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,115,143)"
                        }
                    }
                },
                {
                    "name": "\u516b\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,123,26)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u81ea\u7531\u5ea6\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,18,108)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u4ea7\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,66,105)"
                        }
                    }
                },
                {
                    "name": "\u505a\u4e8b\u81ea\u7531\u5ea6\u8db3\u591f\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,83,124)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u6027\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,99,130)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u5b9e\u529b\u96c4\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,45,18)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5206\u4eab",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,82,14)"
                        }
                    }
                },
                {
                    "name": "\u8c37\u6b4c\u7b49\u884c\u4e1a\u6700\u4f18\u79c0\u4eba\u624d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,61,77)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u5feb\u901f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,13,118)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u4ea7\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,160,113)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5382\u6838\u5fc3\u90e8\u95e8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,39,132)"
                        }
                    }
                },
                {
                    "name": "\u6d59\u5927\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,0,37)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u5feb\u901f\u53d1\u5c55",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,88,156)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u4e60\u6c1b\u56f4\u6d53\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,116,117)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u540d\u4e92\u8054\u7f51\u516c\u53f8\u80cc\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,131,153)"
                        }
                    }
                },
                {
                    "name": "\u6311\u6218\u4e0e\u521b\u65b0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,84,122)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u9886\u57df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,157,16)"
                        }
                    }
                },
                {
                    "name": "\u672a\u6765\u770b\u597d\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,151,42)"
                        }
                    }
                },
                {
                    "name": "\u5177\u6709",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,134,76)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u91cf\u6d41\u91cf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,23,10)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u725b\u6307\u5bfc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,72,159)"
                        }
                    }
                },
                {
                    "name": "13\u85aa+\u5956\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,91,70)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u9650\u6210\u957f\uff01",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,13,112)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5b9e\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,79,115)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5165\u63a5\u89e6\u4e1a\u754c\u6700\u524d\u6cbf\u4eba\u5de5\u667a\u80fd\u6838\u5fc3\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,28,87)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u5e7f\u9614\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,11,56)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u798f\u5229\u5f85\u9047\u4f18\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,97,54)"
                        }
                    }
                },
                {
                    "name": "10\u5929\u6625\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,79,64)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u5b9e\u6218",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,118,111)"
                        }
                    }
                },
                {
                    "name": "\u843d\u5730\u573a\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,111,122)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5347\u5e73\u53f0\u6253\u901a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,146,54)"
                        }
                    }
                },
                {
                    "name": "\u79fb\u52a8\u4e92\u8054\u7f51\u5e7f\u544a\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,47,75)"
                        }
                    }
                },
                {
                    "name": "\u6784\u5efa\u4eba\u7c7b\u865a\u62df\u4e16\u754c\u65b0\u4f53\u9a8c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,126,75)"
                        }
                    }
                },
                {
                    "name": "\u7535\u89c6\u53f0\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,83,2)"
                        }
                    }
                },
                {
                    "name": "\u80fd\u529b\u7a81\u51fa\u8005\u664b\u5347\u5feb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,16,72)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6167\u533b\u7597",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,97,143)"
                        }
                    }
                },
                {
                    "name": "\u5165\u804c\u57f9\u8bad",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,2,111)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u597d\u5f85\u9047\u4f18",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,129,66)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u5feb\u901f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,17,135)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u65b9\u5f0f\u7075\u6d3b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,87,76)"
                        }
                    }
                },
                {
                    "name": "\u9ed1\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,92,154)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u56e2\u961f\u5747\u4e3a\u81ea\u52a8\u9a7e\u9a76",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,132,56)"
                        }
                    }
                },
                {
                    "name": "\u591a\u6837\u5316\u7684\u5b66\u4e60\u73af\u5883",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,42,34)"
                        }
                    }
                },
                {
                    "name": "\u6e05\u534e\u7814\u7a76\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,106,85)"
                        }
                    }
                },
                {
                    "name": "\u521b\u65b0\u6c1b\u56f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,127,26)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u91d1\u96c4\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,19,74)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6d3b\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,64,60)"
                        }
                    }
                },
                {
                    "name": "\u7d27\u6025\u804c\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,17,5)"
                        }
                    }
                },
                {
                    "name": "\u9876\u914dMac\u7b49",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,59,125)"
                        }
                    }
                },
                {
                    "name": "\u5341\u56db\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,53,80)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e24\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,80,35)"
                        }
                    }
                },
                {
                    "name": ".",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,151,31)"
                        }
                    }
                },
                {
                    "name": "\u529e\u516c\u73af\u5883\u4f73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,31,99)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5916\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,102,146)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u9910\u8865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,74,145)"
                        }
                    }
                },
                {
                    "name": "\u53cd\u9988\u5feb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,116,142)"
                        }
                    }
                },
                {
                    "name": "AI\u672a\u6765",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,146,93)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u6e38\u56e2\u5efa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,106,93)"
                        }
                    }
                },
                {
                    "name": "\u521b\u4e1a\u578b\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,77,92)"
                        }
                    }
                },
                {
                    "name": "500\u5f3a\u7814\u53d1\u4e2d\u5fc3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,92,134)"
                        }
                    }
                },
                {
                    "name": "\u535a\u58eb\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,45,107)"
                        }
                    }
                },
                {
                    "name": "\u9910\u8865\u4ea4\u901a\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,92,119)"
                        }
                    }
                },
                {
                    "name": "\u4ebf\u7ea7\u7528\u6237",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,20,119)"
                        }
                    }
                },
                {
                    "name": "\u76c8\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,26,81)"
                        }
                    }
                },
                {
                    "name": "\u5728\u8fd9\u91cc\u4f60\u6709\u66f4\u591a\u7684\u81ea\u7531\u53d1\u6325\u548c\u5c55\u793a\u81ea\u5df1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,124,52)"
                        }
                    }
                },
                {
                    "name": "\u5bbd\u5e7f\u7684\u53d1\u5c55\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,116,20)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5b9e\u529b\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,146,124)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5efa\u8bbe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,52,33)"
                        }
                    }
                },
                {
                    "name": "\u505a\u6700\u524d\u6cbf\u7684\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,147,13)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1;\u8282\u65e5\u8865\u8d34;\u7ee9\u6548\u5956\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,75,118)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u798f\u5229\u5f85\u9047\u597d\u4f11\u606f\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,69,97)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5e74\u8f7b\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,14,24)"
                        }
                    }
                },
                {
                    "name": "\u52a0\u73ed\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,156,124)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u4f01\u6ce8\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,79,66)"
                        }
                    }
                },
                {
                    "name": "\u80a1\u7968",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,27,102)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u7ebf\u4e92\u8054\u7f51\u516c\u53f8\u7d27\u6025\u804c\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,13,132)"
                        }
                    }
                },
                {
                    "name": "\u5546\u4e1a\u6c14\u8c61\u5934\u90e8\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,78,118)"
                        }
                    }
                },
                {
                    "name": "B\u8f6e\u878d\u8d44\u548c\u5927\u725b\u4e00\u8d77\u5de5\u4f5c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,50,125)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5e02",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,46,117)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u9a71\u52a8\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,5,137)"
                        }
                    }
                },
                {
                    "name": "\u72ec\u7acbAI\u5b9e\u9a8c\u5ba4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,119,29)"
                        }
                    }
                },
                {
                    "name": "A\u8f6e\u5feb\u624b\u878d\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,32,41)"
                        }
                    }
                },
                {
                    "name": "\u8282\u5047\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,73,76)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u8f7b\u56e2\u961f\u5e26\u85aa\u5e74\u5047\u505a\u4e94\u4f11\u4e8c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,78,15)"
                        }
                    }
                },
                {
                    "name": "AI\u4ea7\u54c1\u7814\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,41,156)"
                        }
                    }
                },
                {
                    "name": "15\u5929\u5e74\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,2,114)"
                        }
                    }
                },
                {
                    "name": "\u6bcf\u5e74\u6da8\u5de5\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,11,92)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u5e26\u961f\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,130,106)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u5047\u65e5\u4e94\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,93,124)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u9760\u8c31",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,85,94)"
                        }
                    }
                },
                {
                    "name": "\u805a\u96c6\u540c\u884c\u4e1a\u9ad8\u6d45\u4eba\u624d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,106,84)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u8fd8\u4e0d\u9519",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,107,43)"
                        }
                    }
                },
                {
                    "name": "LayaAir\u5f15\u64ce\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,151,22)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u98ce\u53e3\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,44,149)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u65e0\u4e0a\u9650",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,6,29)"
                        }
                    }
                },
                {
                    "name": "\u524d\u9014\u9886\u57df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,62,96)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u56e2\u961f\u5e26\u6559",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,49,93)"
                        }
                    }
                },
                {
                    "name": "\u5c97\u4f4d\u5408\u540c\u4e0e\u5317\u4eac\u4eac\u4e1c\u4e16\u7eaa\u6709\u9650\u516c\u53f8\u7b7e\u8ba2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,112,117)"
                        }
                    }
                },
                {
                    "name": "\u5177\u6709\u5e02\u573a\u7ade\u4e89\u529b\u7684\u85aa\u916c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,155,125)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u81ea\u52a9\u5348\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,69,15)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u52bf\u65b9\u5411\u6280\u672f\u7814\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,140,52)"
                        }
                    }
                },
                {
                    "name": "AI\u884c\u4e1a\u524d\u6cbf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,38,93)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u96f6\u552e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,59,58)"
                        }
                    }
                },
                {
                    "name": "\u4e0e\u559c\u9a6c\u62c9\u96c5APP\u8054\u5408\u62db\u8058",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,156,119)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u53d1\u5c55\u524d\u666f\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,88,127)"
                        }
                    }
                },
                {
                    "name": "\u4f4f\u623f\u514d\u606f\u8d37",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,43,36)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u89c6\u9891",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,54,22)"
                        }
                    }
                },
                {
                    "name": "\u5f00\u653e\u900f\u660e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,97,7)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u7d20\u8d28\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,38,47)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u7ebf\u4e92\u8054\u7f51\u516c\u53f8\u804c\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,141,90)"
                        }
                    }
                },
                {
                    "name": "14-15\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,17,82)"
                        }
                    }
                },
                {
                    "name": "\u5927\u91cf\u671f\u6743\u6c60",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,123,39)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u63a8\u8350\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,126,38)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5f52\u79d1\u7814\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,135,114)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u65b0\u6210\u7acb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,115,99)"
                        }
                    }
                },
                {
                    "name": "\u5927\u4f6c\u5e26",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,96,57)"
                        }
                    }
                },
                {
                    "name": "\u7a33\u5b9a\u53d1\u5c55",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,153,4)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u62ff\u4eb2\u81ea\u5e26",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,66,30)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u4f18\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,70,78)"
                        }
                    }
                },
                {
                    "name": "\u524d\u6cbfAR\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,148,77)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,155,3)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u5185\u9f99\u5934\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,115,157)"
                        }
                    }
                },
                {
                    "name": "5\u59297\u5c0f\u65f6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,45,68)"
                        }
                    }
                },
                {
                    "name": "\u821e\u53f0\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,10,152)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u6c1b\u56f4\u6d3b\u8dc3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,21,122)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4fdd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,10,145)"
                        }
                    }
                },
                {
                    "name": "\u5168\u989d\u8d2d\u4e70\u4e94\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,155,71)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4\u4f73\u7b49\u7b49",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,67,137)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c\u798f\u5229\u4f18\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,106,57)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u8f7b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,119,107)"
                        }
                    }
                },
                {
                    "name": "\u91cd\u70b9\u90e8\u95e8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,61,67)"
                        }
                    }
                },
                {
                    "name": "\u5496\u5561\u5385",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,13,1)"
                        }
                    }
                },
                {
                    "name": "\u8bd5\u7528\u671f\u4ea4\u4e94\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,140,106)"
                        }
                    }
                },
                {
                    "name": "\u65e5\u6570\u636e\u767e\u4ebf\u7ea7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,114,39)"
                        }
                    }
                },
                {
                    "name": "\u4f9b\u5e94\u4e09\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,157,12)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44open",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,48,12)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u4e0d\u5dee\u94b1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,8,97)"
                        }
                    }
                },
                {
                    "name": "\u5bfc\u5e081v1\u5e26",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,42,83)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u4eba\u8f66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,63,135)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7531\u5f00\u653e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,135,14)"
                        }
                    }
                },
                {
                    "name": "Mac",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,35,14)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u573a\u9762\u8bd5\u6d41\u7a0b\u4e00\u6b21\u8d70\u5b8c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,75,19)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u5927\u6570\u636e\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,156,124)"
                        }
                    }
                },
                {
                    "name": "\u7cbe\u81f4\u8212\u9002\u7684\u529e\u516c\u73af\u5883",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,98,57)"
                        }
                    }
                },
                {
                    "name": "\u7a7a\u95f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,125,91)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u6ce8\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,60,146)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4OPEN",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,128,136)"
                        }
                    }
                },
                {
                    "name": "3\u4f4d\u535a\u58eb\u751f\u5bfc\u5e08\u6302\u5e05\u7684\u79d1\u5b66\u5bb6\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,99,15)"
                        }
                    }
                },
                {
                    "name": "\u662f\u6781\u5177\u6f5c\u529b\u7684AI\u5e94\u7528\u65b9\u5411",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,29,91)"
                        }
                    }
                },
                {
                    "name": "\u6bcf\u5e742\u6b21\u8c03\u85aa\u7a97\u53e3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,2,146)"
                        }
                    }
                },
                {
                    "name": "AI\u533b\u7597\u9886\u57df\u72ec\u89d2\u517d\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,54,4)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7528\u8fd0\u7b79\u4f18\u5316\u77e5\u8bc6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,145,87)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a**",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,17,84)"
                        }
                    }
                },
                {
                    "name": "\u817e\u8baf\u6295\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,58,8)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u7ebf\u98ce\u6295\u52a0\u6301",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,32,124)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u8d28\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,73,89)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u5bcc\u4e1a\u52a1\u573a\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,39,102)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u4e30\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,20,50)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,34,25)"
                        }
                    }
                },
                {
                    "name": "\u805a\u4e00\u7fa4\u6709\u60c5\u4e49\u7684\u4eba\u505a\u6210\u6709\u610f\u4e49\u7684\u4e8b\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,154,10)"
                        }
                    }
                },
                {
                    "name": "\u6574\u4f53\u89e3\u51b3\u65b9\u6848\u80fd\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,115,45)"
                        }
                    }
                },
                {
                    "name": "\u5b8c\u5584\u7684\u664b\u5347\u901a\u9053",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,107,32)"
                        }
                    }
                },
                {
                    "name": "\u72ec\u7acb\u8d1f\u8d23",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,33,46)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1aTOP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,120,63)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5065\u8eab",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,15,160)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u5e7f\u544a\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,119,152)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u8c03\u5ea6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,68,0)"
                        }
                    }
                },
                {
                    "name": "\u597d\u73a9\u7684\u6e38\u620f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,130,16)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u989c\u503c\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,139,113)"
                        }
                    }
                },
                {
                    "name": "\u6709\u671f\u6743\u6388\u4e88",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,61,73)"
                        }
                    }
                },
                {
                    "name": "\u9910\u901a\u8baf\u4ea4\u901a\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,74,17)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u9971\u6ee1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,30,1)"
                        }
                    }
                },
                {
                    "name": "\u4e0e\u676d\u5dde\u5b9e\u5728\u667a\u80fd\u79d1\u6280\u6709\u9650\u516c\u53f8\u8054\u5408\u62db\u8058",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,28,44)"
                        }
                    }
                },
                {
                    "name": "\u4e2a\u4eba\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,15,96)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u80cc\u666f\u5f3a\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,77,140)"
                        }
                    }
                },
                {
                    "name": "\u5348\u9910\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,100,55)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546\u573a\u666f\u5546\u54c1\u63a8\u8350\u7b49",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,88,139)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u989d\u9910\u8865/TB\u8d39\u7528",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,117,107)"
                        }
                    }
                },
                {
                    "name": "\u671f\u6743\u6fc0\u52b1\u5e26\u85aa\u5e74\u5047\u4e94\u9669\u4e00\u91d1\u8282\u65e5\u793c\u7269\u5e74\u5ea6\u65c5\u6e38",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,118,84)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,146,54)"
                        }
                    }
                },
                {
                    "name": "\u90e8\u95e8\u8bc4\u4f18\u5956",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,116,86)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5e74\u8f7b\u6709\u6d3b\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,144,34)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u53d1\u5c55\u5feb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,120,147)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5e0212\u5e74",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,32,64)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u6838\u5fc3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,48,29)"
                        }
                    }
                },
                {
                    "name": "\u5145\u6ee1\u6d3b\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,77,19)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u4f6c\u5e26\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,92,24)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u53d1\u5c55\u5feb\u901f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,118,45)"
                        }
                    }
                },
                {
                    "name": "\u5927\u878d\u8d44\u80cc\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,108,157)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u5e7f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,117,149)"
                        }
                    }
                },
                {
                    "name": "\u52a0\u73ed\u9910\u8865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,73,52)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u91cf\u533b\u7597\u6570\u636e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,107,12)"
                        }
                    }
                },
                {
                    "name": "\u9910\u996e\u8865\u52a9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,149,159)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u7cfb\u7edf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,8,18)"
                        }
                    }
                },
                {
                    "name": "\u516d\u9669\u4e00\u91d1+\u5b63\u5ea6\u7ee9\u6548\u5956\u91d1/\u5e74\u7ec8\u5956",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,29,134)"
                        }
                    }
                },
                {
                    "name": "\u957f\u671f\u7a33\u5b9a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,15,110)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u6f5c\u529b\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,60,107)"
                        }
                    }
                },
                {
                    "name": "\u8ddf\u5927\u4f6c\u4e00\u8d77\u53c2\u52a0\u56fd\u9645\u9876\u4f1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,139,50)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u9614\u7a7a\u95f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,39,27)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u53d1\u5c55\u524d\u666f\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,0,145)"
                        }
                    }
                },
                {
                    "name": "\u964d\u566a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,140,85)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u4e1a\u52a1\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,53,43)"
                        }
                    }
                },
                {
                    "name": "\u8212\u5fc3\u4f01\u4e1a\u6587\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,84,154)"
                        }
                    }
                },
                {
                    "name": "\u8001\u677f\u683c\u5c40\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,70,79)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u53d1\u5c55\u524d\u666f\u5e7f\u9614",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,72,135)"
                        }
                    }
                },
                {
                    "name": "CBA\u660e\u661f\u521b\u4e1a\u9879\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,37,91)"
                        }
                    }
                },
                {
                    "name": "\u4e0e\u4e0a\u6d77\u91d1\u5353\u79d1\u6280\u6709\u9650\u516c\u53f8\u8054\u5408\u62db\u8058",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,141,8)"
                        }
                    }
                },
                {
                    "name": "\u5468\u672b\u53cc\u4f11/\u5f39\u6027\u5de5\u4f5c/\u548c\u8c10\u7684\u529e\u516c\u6c1b\u56f4/1\u5bf91\u5e2e\u5e26",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,128,147)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u9910\u514d\u8d39",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,82,46)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u8f7b\u6241\u5e73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,141,108)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u673a\u4f1a\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,143,115)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5f71\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,71,132)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u901f\u53d1\u5c55\u4e2d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,44,146)"
                        }
                    }
                },
                {
                    "name": "\u4f30\u503c\u767e\u4ebf\u7f8e\u5143",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,127,157)"
                        }
                    }
                },
                {
                    "name": "\u57f9\u8bad\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,99,142)"
                        }
                    }
                },
                {
                    "name": "\u804c\u4f4d\u664b\u5347\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,156,69)"
                        }
                    }
                },
                {
                    "name": "\u5185\u90e8\u521b\u4e1a\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,154,2)"
                        }
                    }
                },
                {
                    "name": "\u8282\u65e5\u798f\u5229\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,143,42)"
                        }
                    }
                },
                {
                    "name": "\u72ec\u7acb\u5e26\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,151,43)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u5185\u540d\u5217\u524d\u8305",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,113,62)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,91,58)"
                        }
                    }
                },
                {
                    "name": "\u6b22\u8fce\u52a0\u5165",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,72,128)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u9614\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,82,109)"
                        }
                    }
                },
                {
                    "name": "\u5916\u5305",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,124,10)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u4e1a\u56fe\u8c31",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,118,152)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u540d\u7535\u5546",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,138,27)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c\u798f\u5229\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,135,92)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u98de\u901f\u53d1\u5c55",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,155,126)"
                        }
                    }
                },
                {
                    "name": "\u5b9e\u4e60\u751f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,71,70)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u5b9e\u4e60\u8bc1\u660e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,88,29)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,151,105)"
                        }
                    }
                },
                {
                    "name": "90\u540e\u5e74\u8f7b\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,87,83)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5ea6\u8c03\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,93,55)"
                        }
                    }
                },
                {
                    "name": "\u5168\u7403\u6700\u5927\u4e09\u65b9\u5e7f\u544a\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,121,26)"
                        }
                    }
                },
                {
                    "name": "\u8282\u65e5\u793c\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,13,8)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u56e2\u961f20\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,34,10)"
                        }
                    }
                },
                {
                    "name": "\u7b80\u5355\u771f\u8bda",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,157,109)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u4e30\u5bcc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,32,27)"
                        }
                    }
                },
                {
                    "name": "AI\u4ea7\u54c1\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,121,73)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u516d\u9669\u4e00\u91d1\u996d\u8d34\u8f66\u8d34\u7ee9\u6548\u5956\u5b9a\u671f\u4f53\u68c0\u805a\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,144,59)"
                        }
                    }
                },
                {
                    "name": "10\u5929\u5e26\u85aa\u75c5\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,127,63)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956+\u53cc\u4f11+\u516d\u9669\u4e00\u91d1+\u665a\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,108,29)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u6210\u957f\u6027",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,67,93)"
                        }
                    }
                },
                {
                    "name": "12\u5929\u5e74\u5047\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,64,113)"
                        }
                    }
                },
                {
                    "name": "\u4f30\u503c\u8fd1\u767e\u4ebf\u7f8e\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,126,103)"
                        }
                    }
                },
                {
                    "name": "\u5927\u4f6c\u5e26\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,145,24)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5496\u6307\u5bfc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,133,134)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u5efa\u65c5\u6e38\u7b49",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,36,151)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u80a1\u4e1c\u9760\u8c31",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,28,158)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u9645\u5316\u4ea7\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,13,157)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u5496",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,89,157)"
                        }
                    }
                },
                {
                    "name": "\u7eff\u8c37\u5236\u836f\u5b50\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,108,153)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u53d1\u5c55\u524d\u666f\u5e7f\u9614",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,75,30)"
                        }
                    }
                },
                {
                    "name": "\u5305\u4e09\u9910\u96f6\u98df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,79,61)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u4e0a\u4e0b\u73ed\u53cc\u4f11",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,95,67)"
                        }
                    }
                },
                {
                    "name": "\u80a1\u6743\u8ba1\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,151,157)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u4eba\u5de5\u667a\u80fd\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,150,155)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u671f\u65c5\u6e38",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,129,45)"
                        }
                    }
                },
                {
                    "name": "\u6709\u7528\u6237\u57fa\u7840",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,157,77)"
                        }
                    }
                },
                {
                    "name": "\u8fc1\u79fb\u5b66\u4e60",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,62,105)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u57fa\u5efa\u9886\u57df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,126,70)"
                        }
                    }
                },
                {
                    "name": "\u7ee9\u6548\u5956\u91d1\u4e30\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,110,0)"
                        }
                    }
                },
                {
                    "name": "\u963f\u91cc+\u4e2d\u5175\u5408\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,140,33)"
                        }
                    }
                },
                {
                    "name": "\u4e0e\u5f97\u7269APP\u8054\u5408\u62db\u8058",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,70,151)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u725b\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,99,81)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u6280\u672f\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,104,71)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u6587\u5316\u56e2\u961fnice",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,133,111)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u5496\u4e91\u96c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,151,55)"
                        }
                    }
                },
                {
                    "name": "\u6709\u5348\u4f11",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,67,37)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5c0f\u800c\u7cbe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,34,134)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u5e74\u4e24\u6b21\u8c03\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,100,70)"
                        }
                    }
                },
                {
                    "name": "\u4f60\u7684\u6bcf\u4e00",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,126,23)"
                        }
                    }
                },
                {
                    "name": "\u5343\u4eba\u89c4\u6a21",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,85,90)"
                        }
                    }
                },
                {
                    "name": "\u4f53\u68c0/\u5f39\u6027\u4e0a\u4e0b\u73ed/\u5e74\u7ec8\u7ee9\u6548/\u514d\u8d39\u5348\u665a\u9910\u4e0b\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,104,91)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u6c1b\u56f4\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,40,88)"
                        }
                    }
                },
                {
                    "name": "\u7a33\u5b9a\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,133,63)"
                        }
                    }
                },
                {
                    "name": "\u6709XLNet\u4e00\u4f5c\u5927\u795e\u5e26\u60a8\u5728\u7b97\u6cd5\u91cc\u6df1\u8015",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,136,78)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,75,81)"
                        }
                    }
                },
                {
                    "name": "\u975e\u5e38\u4eba\u6027\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,103,22)"
                        }
                    }
                },
                {
                    "name": "\u7d2b\u5149\u96c6\u56e2\u65d7\u4e0b\u6559\u80b2\u4fe1\u606f\u5316\u884c\u4e1a\u5934\u90e8\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,106,104)"
                        }
                    }
                },
                {
                    "name": "\u6fc0\u52b1\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,154,98)"
                        }
                    }
                },
                {
                    "name": "\u8f6f\u4ef6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,94,139)"
                        }
                    }
                },
                {
                    "name": "\u521b\u4e1aAI\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,28,125)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u539a\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,149,74)"
                        }
                    }
                },
                {
                    "name": "\u5f15\u9886\u884c\u4e1a\u8d70\u52bf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,89,130)"
                        }
                    }
                },
                {
                    "name": "\u90e8\u95e8\u53d1\u5c55\u7a33\u5065",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,122,143)"
                        }
                    }
                },
                {
                    "name": "\u7279\u5f81\u63d0\u53d6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,53,142)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6167\u73af\u4fdd\u9886\u519b\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,108,75)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u7a33\u5b9a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,64,14)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u5168",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,152,49)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u63d0\u5347",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,146,57)"
                        }
                    }
                },
                {
                    "name": "\u591a\u91cd\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,93,121)"
                        }
                    }
                },
                {
                    "name": "\u7814\u7a76\u548c\u5b9e\u9645\u5e94\u7528\u7ed3\u5408",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,28,70)"
                        }
                    }
                },
                {
                    "name": "\u751f\u65e5\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,120,12)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u5b9a\u8282\u5047\u65e5\u653e\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,2,41)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u804c\u7ea7\u664b\u5347",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,141,147)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u5316\u7ba1\u7406\u5de5\u4f5c\u6c1b\u56f4\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,132,144)"
                        }
                    }
                },
                {
                    "name": "\u6536\u5165\u548c\u80fd\u529b\u6210\u957f\u6027\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,103,153)"
                        }
                    }
                },
                {
                    "name": "\u9769\u65b0\u7684\u9879\u76ee\u673a\u4f1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,107,40)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5382\u4f18\u79c0\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,27,23)"
                        }
                    }
                },
                {
                    "name": "7\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,4,21)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u4f9b\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,49,25)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u5e73\u53f0\u53d1\u5c55\u524d\u666f\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,100,2)"
                        }
                    }
                },
                {
                    "name": "\u521b\u4e1a\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,63,121)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u4f18\u6e25",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,103,10)"
                        }
                    }
                },
                {
                    "name": "\u7ba1\u7406\u6241\u5e73\u900f\u660e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,49,126)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5382\u5b9e\u4e60",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,17,43)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u884c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,7,102)"
                        }
                    }
                },
                {
                    "name": "\u878d\u8d44\u8fc7\u4ebf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,17,32)"
                        }
                    }
                },
                {
                    "name": "\u5047\u671f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,90,153)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u4e0d\u9519",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,106,29)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5347\u671f\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,75,33)"
                        }
                    }
                },
                {
                    "name": "\u5927\u4f6c\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,31,41)"
                        }
                    }
                },
                {
                    "name": "\u6709\u7ade\u4e89\u529b\u7684\u85aa\u916c\u5f85\u9047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,132,151)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u6548\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,42,112)"
                        }
                    }
                },
                {
                    "name": "\u671f\u6743\u80a1\u6743",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,32,102)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u597d\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,59,132)"
                        }
                    }
                },
                {
                    "name": "\u521b\u4e1a\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,154,55)"
                        }
                    }
                },
                {
                    "name": "A\u8f6e\u878d\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,72,81)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u9910\u8865\u52a9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,86,56)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u4e1a\u8def",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,130,12)"
                        }
                    }
                },
                {
                    "name": "\u63a2\u7d22\u524d\u6cbf\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,127,82)"
                        }
                    }
                },
                {
                    "name": "\u745c\u4f3d\u5065\u8eab",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,2,39)"
                        }
                    }
                },
                {
                    "name": "\u4ff1\u4e50\u90e8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,104,56)"
                        }
                    }
                },
                {
                    "name": "\u62e5\u6709TB\u7ea7\u6570\u636e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,154,137)"
                        }
                    }
                },
                {
                    "name": "\u6587\u827a\u6c1b\u56f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,44,17)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51\u6c1b\u56f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,14,151)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u4e1a\u57f9\u8bad",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,47,127)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u4e8b\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,107,78)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,103,55)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u7b97\u6cd5\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,29,52)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u5e7416\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,91,138)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u91cf\u7ea7\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,61,71)"
                        }
                    }
                },
                {
                    "name": "\u5229\u7528\u6700\u524d\u6cbf\u7684\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,136,67)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u53d1\u5c55\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,60,134)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u4e2d\u575a\u529b\u91cf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,35,156)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u65b0\u6280\u672f\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,42,10)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u6e38",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,15,146)"
                        }
                    }
                },
                {
                    "name": "\u6210\u719f\u4e14\u5c0f\u800c\u7cbe\u7684\u521b\u4e1a\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,13,73)"
                        }
                    }
                },
                {
                    "name": "\u6b22\u8fce\u60a8\u52a0\u5165\u4e00\u70b9\u5927\u5bb6\u5ead~",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,139,88)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5e02\u51c6\u5907\u671f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,98,148)"
                        }
                    }
                },
                {
                    "name": "\u5168\u989d\u516d\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,102,158)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u9886\u57df\u5927\u725b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,111,119)"
                        }
                    }
                },
                {
                    "name": "500\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,94,85)"
                        }
                    }
                },
                {
                    "name": "\u5730\u4ea7\u9f99\u5934",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,35,147)"
                        }
                    }
                },
                {
                    "name": "\u51c6\u72ec\u89d2\u517d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,73,100)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,153,44)"
                        }
                    }
                },
                {
                    "name": "\u5076\u5c14\u52a0\u73ed\u8c03\u4f11",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,74,7)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u52a8\u578b\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,40,108)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5b9e\u4e60\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,110,95)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u90e8\u95e8\u6838\u5fc3\u5c97\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,100,79)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1atop",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,151,92)"
                        }
                    }
                },
                {
                    "name": "\u7a7a\u95f4\u5de8\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,33,5)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u540d\u667a\u80fd\u9a7e\u9a76\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,129,48)"
                        }
                    }
                },
                {
                    "name": "\u5173\u952e\u5c97\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,56,28)"
                        }
                    }
                },
                {
                    "name": "\u521b\u9020\u524d\u6cbfAI\u4ea7\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,160,103)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u6c1b\u56f4\u878d\u6d3d\u53d1\u5c55\u6f5c\u529b\u5de8\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,38,94)"
                        }
                    }
                },
                {
                    "name": "\u516c\u79ef\u91d1\u5168\u989d\u6700\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,1,130)"
                        }
                    }
                },
                {
                    "name": "\u591a\u4e2a\u529e\u516c\u5730\u70b9\u53ef\u9009",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,17,82)"
                        }
                    }
                },
                {
                    "name": "\u5e02\u573a\u8d44\u6e90\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,0,43)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u5316\u5f15\u64ce\u7684\u7cfb\u7edf\u67b6\u6784",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,20,70)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u98df\u4e0b\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,62,145)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u5347\u4e2a\u4eba\u4ef7\u503c\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,79,47)"
                        }
                    }
                },
                {
                    "name": "\u8be5\u804c\u4f4d\u76f4\u63a5\u4e0e\u7528\u4eba\u5355\u4f4d\u7b7e\u8ba2\u5408\u540c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,31,113)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6709\u53ef\u4e3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,36,133)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u5efa\u7b49",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,14,18)"
                        }
                    }
                },
                {
                    "name": "\u5165\u804c\u8d2d\u4e70\u4e94\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,36,13)"
                        }
                    }
                },
                {
                    "name": "\u6625\u8282\u957f\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,127,9)"
                        }
                    }
                },
                {
                    "name": "\u5916\u4f01\u98ce\u683c\u7b49",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,30,149)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u5de5\u7a0b\u5e08-\u6570\u636e\u6316\u6398\u65b9\u5411",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,10,147)"
                        }
                    }
                },
                {
                    "name": "\u4e2a\u4eba\u804c\u4e1a\u53d1\u5c55\u4f18",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,30,150)"
                        }
                    }
                },
                {
                    "name": "\u5916\u4f01\u6c1b\u56f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,98,13)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u81ea\u7531",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,31,136)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u524d\u6cbf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,4,83)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u5f85\u9047\u4f18",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,2,32)"
                        }
                    }
                },
                {
                    "name": "AI\u7b97\u6cd5\u843d\u5730",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,71,47)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u5185**\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,153,121)"
                        }
                    }
                },
                {
                    "name": "\u8682\u8681\u63a7\u80a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,127,108)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u73ed\u5f00\u5fc3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,128,58)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u56e2\u961f\u4f18\u79c0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,147,34)"
                        }
                    }
                },
                {
                    "name": "\u6709\u5229\u4e8e\u53d1\u8bba\u6587",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,102,123)"
                        }
                    }
                },
                {
                    "name": "\u5173\u6ce8\u5458\u5de5\u53d1\u5c55",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,30,24)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u9886\u5148\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,118,86)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u5bf9\u4e00\u5e26\u6559",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,11,96)"
                        }
                    }
                },
                {
                    "name": "\u5927\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,74,63)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4fdd\u516c\u79ef\u91d1\u60c5\u51b5\uff1a\u516d\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,108,45)"
                        }
                    }
                },
                {
                    "name": "\u8001\u677fnice",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,103,31)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u5fc3\u7814\u7a76\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,151,37)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u73af\u5883\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,35,33)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u957f\u5e26\u85aa\u5e74\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,18,20)"
                        }
                    }
                },
                {
                    "name": "\u9876\u683c\u4f4f\u623f\u516c\u79ef\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,126,139)"
                        }
                    }
                },
                {
                    "name": "\u5e02\u573a\u524d\u666f\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,96,19)"
                        }
                    }
                },
                {
                    "name": "AI\u91d1\u878d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,22,130)"
                        }
                    }
                },
                {
                    "name": "\u4e3b\u52a8\u52a0\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,24,74)"
                        }
                    }
                },
                {
                    "name": "\u80a1\u4e1c\u80cc\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,53,150)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5065\u5168",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,112,55)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u7814\u53d1\u4eba\u6570\u5360\u6bd470%",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,150,106)"
                        }
                    }
                },
                {
                    "name": "\u4f9b\u5e94\u94fe\u91d1\u878d\u79d1\u6280\u5934\u90e8\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,36,144)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6709\u4f18\u5f02\u7684\u6280\u672f\u6df1\u5ea6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,104,118)"
                        }
                    }
                },
                {
                    "name": "\u73af\u5883open",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,158,50)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u5f85\u9047\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,24,62)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5e02\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,27,131)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u7a7a\u95f4\u53ca\u85aa\u916c\u9ad8\u4e8e\u540c\u884c\u4e1a\u6c34\u5e73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,61,33)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u8425\u98df\u5802",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,106,92)"
                        }
                    }
                },
                {
                    "name": "AI\u667a\u80fd\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,154,159)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u524d\u666f\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,73,0)"
                        }
                    }
                },
                {
                    "name": "\u5b9e\u4e60\u8f6c\u6b63",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,46,21)"
                        }
                    }
                },
                {
                    "name": "\u5b63\u5ea6\u5956",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,153,18)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u9760\u8c31",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,41,39)"
                        }
                    }
                },
                {
                    "name": "\u9f99\u5934\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,105,61)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u901f\u589e\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,51,148)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u505c\u8f66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,139,35)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u80cc\u666f\u5f3a\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,44,6)"
                        }
                    }
                },
                {
                    "name": "AI+\u6559\u80b2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,103,85)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51\u5a92\u4f53",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,12,42)"
                        }
                    }
                },
                {
                    "name": "\u9519\u8fc7\u4e8610\u5e74\u7684\u624b\u6dd8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,82,10)"
                        }
                    }
                },
                {
                    "name": "\u8d5b\u9053\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,30,66)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u521b\u65b0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,160,134)"
                        }
                    }
                },
                {
                    "name": "\u5173\u7cfb\u548c\u8c10",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,133,95)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u5e26\u961f\uff01\uff01",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,55,108)"
                        }
                    }
                },
                {
                    "name": "\u521b\u59cb\u56e2\u961f\u725b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,116,29)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u4f18\u52bf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,51,20)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5177\u6709\u6559\u80b2\u548c\u91d1\u878d\u4e24\u4e2a\u65b9\u5411\u843d\u5730\u573a\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,96,140)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5347\u7a7a\u95f4\u5de8\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,54,137)"
                        }
                    }
                },
                {
                    "name": "**\u751f\u7269\u533b\u5b66\u4fe1\u606f\u4e13\u5bb6\u5e26\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,4,57)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51\u51fa\u6d77\u4f01\u4e1a\u6807\u6746",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,27,14)"
                        }
                    }
                },
                {
                    "name": "\u6211\u53f8\u4e0e\u4eac\u4e1c\u96f6\u552e\u5408\u4f5c\u62db\u52df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,82,131)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u5185**\u6295\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,145,128)"
                        }
                    }
                },
                {
                    "name": "\u8f83\u5927\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,27,22)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u524d\u666f\u53ef\u89c2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,95,47)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u9a71\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,66,63)"
                        }
                    }
                },
                {
                    "name": "\u91cd\u65b0\u5b9a\u4e49\u884c\u4e1a\u89c4\u5219",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,92,150)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u7b97\u6cd5\u9a71\u52a8\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,37,124)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u5f85\u9047\u5f88\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,20,111)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6210\u5458\u6765\u81ea\u56fd\u5185\u5916\u540d\u6821",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,46,141)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,136,115)"
                        }
                    }
                },
                {
                    "name": "\u4e0d\u8bbe\u9650",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,153,116)"
                        }
                    }
                },
                {
                    "name": "\u5927\u516c\u53f8\u5e73\u53f0\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,136,26)"
                        }
                    }
                },
                {
                    "name": "\u6ca1\u6709KPI",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,96,21)"
                        }
                    }
                },
                {
                    "name": "\u5b9e\u4e60\u8bc1\u660e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,134,12)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u4eba\u914d\u9001",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,71,31)"
                        }
                    }
                },
                {
                    "name": "\u786c\u5b9e\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,136,50)"
                        }
                    }
                },
                {
                    "name": "E\u8f6e\u878d\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,159,17)"
                        }
                    }
                },
                {
                    "name": "\u6253\u9020\u4e16\u754c**\u7684\u6df7\u6c8c\u5de5\u7a0b\u4e50\u56ed",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,84,157)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,48,55)"
                        }
                    }
                },
                {
                    "name": "9\u70b9\u6253\u8f66\u62a5\u9500",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,154,33)"
                        }
                    }
                },
                {
                    "name": "\u826f\u597d\u7684\u884c\u4e1a\u524d\u666f\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,93,98)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u5e72\u9884\u662f\u7f8e\u56e2\u9a91\u884c\u4e1a\u52a1\u6838\u5fc3\u90e8\u5206",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,67,15)"
                        }
                    }
                },
                {
                    "name": "\u56fa\u5b9a\u53cc\u4f11",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,104,73)"
                        }
                    }
                },
                {
                    "name": "\u5165\u804c\u5373\u4e0a\u4e94\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,94,98)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6280\u672f\u7cbe\u6e5b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,145,108)"
                        }
                    }
                },
                {
                    "name": "\u6625\u8282\u5047\u671f\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,107,61)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u5185\u9886\u5148",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,96,0)"
                        }
                    }
                },
                {
                    "name": "\u96c6\u56e2\u5e73\u53f0\u80cc\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,90,19)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u4e60\u578b\u7ec4\u7ec7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,149,84)"
                        }
                    }
                },
                {
                    "name": "\u5404\u79cd\u4e0b\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,29,97)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u4f11\u4e94\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,45,23)"
                        }
                    }
                },
                {
                    "name": "***\u9879\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,111,74)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u957f\u5047\u671f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,93,94)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u98df\u65e0\u9650\u91cf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,87,43)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,88,7)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u5065\u8eab\u623f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,58,42)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u664b\u5347\u5feb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,47,68)"
                        }
                    }
                },
                {
                    "name": "\u76f4\u63a5\u8ddf\u9879\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,127,139)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u85aa\uff0b\u671f\u6743",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,5,92)"
                        }
                    }
                },
                {
                    "name": "\u535a\u5bfc\u5e26\u961f\u7684\u6df1\u5ea6\u5b66\u4e60\u4eba\u5de5\u667a\u80fd\u7814\u7a76\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,51,155)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u8c08\u671f\u6743",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,117,52)"
                        }
                    }
                },
                {
                    "name": "\u5929\u773c\u67e5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,44,35)"
                        }
                    }
                },
                {
                    "name": "\u521d\u521b\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,63,89)"
                        }
                    }
                },
                {
                    "name": "\u5bfc\u5e08\u5e26\u9886",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,25,106)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u4f17\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,34,137)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u7ea2\u4e66\u7b49\u516c\u53f8\u7b7e\u8ba2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,94,40)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,26,26)"
                        }
                    }
                },
                {
                    "name": "\u4e0e\u54c8\u5570\u51fa\u884c\u8054\u5408\u62db\u8058",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,6,72)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u79c0\u7684\u6280\u672f\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,45,101)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u65c5\u6e38\u4e0b\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,130,67)"
                        }
                    }
                },
                {
                    "name": "\u5305\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,104,39)"
                        }
                    }
                },
                {
                    "name": "\u7ec6\u5206\u9886\u57df\u9690\u5f62**",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,54,8)"
                        }
                    }
                },
                {
                    "name": "\u5305\u4f4f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,108,74)"
                        }
                    }
                },
                {
                    "name": "\u805a\u96c6\u9ad8\u6d45\u4eba\u624d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,94,81)"
                        }
                    }
                },
                {
                    "name": "\u8be5\u804c\u4f4d\u4e0e\u733f\u8f85\u5bfc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,32,31)"
                        }
                    }
                },
                {
                    "name": "\u624e\u624e\u5b9e\u5b9e\u505a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,94,67)"
                        }
                    }
                },
                {
                    "name": "\u592e\u4f01\u63a7\u80a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,19,142)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,99,2)"
                        }
                    }
                },
                {
                    "name": "\u725b\u4eba\u5e26\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,104,13)"
                        }
                    }
                },
                {
                    "name": "\u6bcf\u65e5\u96f6\u98df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,5,25)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u5efa\u65c5\u6e38",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,144,77)"
                        }
                    }
                },
                {
                    "name": "\u8f85\u52a9\u9a7e\u9a76",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,136,92)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u5185\u5916\u5c55\u4f1a\u4ea4\u6d41",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,114,26)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u91cf\u7ea7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,15,15)"
                        }
                    }
                },
                {
                    "name": "\u96c6\u4f53\u51fa\u6e38",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,13,67)"
                        }
                    }
                },
                {
                    "name": "\u6d41\u7a0b\u5feb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,57,130)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u53e3\u7891\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,137,99)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f\u7a7a\u95f4\u5de8\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,91,22)"
                        }
                    }
                },
                {
                    "name": "\u4f11\u95f2\u96f6\u98df\u4e0b\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,56,18)"
                        }
                    }
                },
                {
                    "name": "\u52a0\u73ed\u8d39\u53e6\u7b97",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,54,71)"
                        }
                    }
                },
                {
                    "name": "\u5168\u7403\u9886\u5148\u7684\u5546\u7528\u670d\u52a1\u673a\u5668\u4eba\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,20,143)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5927\u725b\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,42,145)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5e9514\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,112,34)"
                        }
                    }
                },
                {
                    "name": "\u6536\u5165\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,67,151)"
                        }
                    }
                },
                {
                    "name": "\u767e\u4eba\u6280\u672f\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,36,76)"
                        }
                    }
                },
                {
                    "name": "\u5168\u6808\u6280\u672f\u5927\u725b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,126,44)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5e74\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,38,108)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6709\u4f5c\u4e3a\uff01",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,24,46)"
                        }
                    }
                },
                {
                    "name": "\u4fdd\u5e9513\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,7,101)"
                        }
                    }
                },
                {
                    "name": "\u6709\u73ed\u8f66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,11,115)"
                        }
                    }
                },
                {
                    "name": "Top\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,11,35)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u98df\u996e\u6599\u4e0b\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,123,89)"
                        }
                    }
                },
                {
                    "name": "\u826f\u597d\u53d1\u5c55\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,12,140)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7814\u4ea7\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,53,44)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u901f\u53d1\u5c55\u9636\u6bb5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,112,69)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6280\u672f\u5927\u725b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,45,154)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u98df\u5bbf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,4,86)"
                        }
                    }
                },
                {
                    "name": "\u5f00\u653e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,149,30)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u6ee1\u5206",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,17,150)"
                        }
                    }
                },
                {
                    "name": "\u9662\u58eb\u5e26\u961f\u53c2\u4e0e\u9ad8\u6821\u8054\u5408\u7814\u7a76",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,57,46)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u7ea2\u5305",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,86,17)"
                        }
                    }
                },
                {
                    "name": "\u96c6\u56e2\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,108,117)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,69,12)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,3,10)"
                        }
                    }
                },
                {
                    "name": "\u7ba1\u7406\u6241\u5e73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,37,113)"
                        }
                    }
                },
                {
                    "name": "\u65e5\u6d3b\u5343\u4e07",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,12,91)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u6cdb\u6210\u957f\u7a7a\u95f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,95,3)"
                        }
                    }
                },
                {
                    "name": "\u540c\u4e8bnice",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,9,89)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u8d1f\u8d23\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,129,28)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1\u8282\u65e5\u798f\u5229\u5e74\u5ea6\u4f53\u68c0\u52a0\u73ed\u8865\u52a9\u5e26\u85aa\u5e74\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,76,51)"
                        }
                    }
                },
                {
                    "name": "\u4e0e\u901a\u8054\u6570\u636e\u8054\u5408\u62db\u8058",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,49,146)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5916\u56e2\u5efa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,92,116)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1|\u5e74\u7ec8\u5956\u91d1|\u4f53\u68c0|\u56e2\u961f\u65c5\u6e38",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,53,43)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u524d\u6cbf\u7814\u7a76\u53ca\u5e94\u7528",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,131,93)"
                        }
                    }
                },
                {
                    "name": "\u6301\u7eed\u521b\u65b0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,72,8)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u5e74\u4e24\u6b21\u8c03\u85aa\u673a\u4f1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,2,37)"
                        }
                    }
                },
                {
                    "name": "\u9910\u996e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,9,6)"
                        }
                    }
                },
                {
                    "name": "\u540c\u4e8b\u597d\u76f8\u5904",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,9,36)"
                        }
                    }
                },
                {
                    "name": "\u504f\u5e73\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,133,124)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,159,7)"
                        }
                    }
                },
                {
                    "name": "CTO\u7b97\u6cd5\u5927\u725b\u5e26\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,114,74)"
                        }
                    }
                },
                {
                    "name": "\u592e\u4f01\u5355\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,70,80)"
                        }
                    }
                },
                {
                    "name": "7\u5c0f\u65f6\u5de5\u4f5c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,37,48)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u7814\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,148,90)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u5927\u725b\u5e26\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,62,88)"
                        }
                    }
                },
                {
                    "name": "\u5305\u5403\u5305\u4f4f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,49,29)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u4f4f\u5bbf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,74,152)"
                        }
                    }
                },
                {
                    "name": "\u6253\u8f66\u514d\u8d39",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,135,102)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5185\u4e00\u534a\u6765\u81ea\u6e05\u534e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,90,30)"
                        }
                    }
                },
                {
                    "name": "\u521b\u65b0\u4e0e\u6311\u6218",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,101,31)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u5047\u671f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,100,105)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u9ad8P",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,25,6)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u73af\u7ed5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,115,15)"
                        }
                    }
                },
                {
                    "name": "\u8fdc\u7a0b\u529e\u516c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,94,149)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u8f6e\u5c97\u6216\u8f6c\u5c97\u664b\u5347",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,120,22)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5496\u5561",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,9,13)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f\u671f\u521b\u4e1a\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,119,67)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u665a\u9910&\u5348\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,160,129)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,78,153)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u4e60\u673a\u4f1a\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,18,23)"
                        }
                    }
                },
                {
                    "name": "\u641c\u72d7\u5730\u56fe\u6838\u5fc3\u4e1a\u52a1\u65b9\u5411",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,21,51)"
                        }
                    }
                },
                {
                    "name": "15-20\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,80,109)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u4e3a\u4e3b\u5bfc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,138,129)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7d20\u8d28\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,121,62)"
                        }
                    }
                },
                {
                    "name": "\u536b\u74f4\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,116,15)"
                        }
                    }
                },
                {
                    "name": "\u82f1\u96c4\u6587\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,45,16)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u8f6f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,117,102)"
                        }
                    }
                },
                {
                    "name": "\u6d53\u539a\u7684\u6280\u672f\u5b66\u4e60\u6c1b\u56f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,158,14)"
                        }
                    }
                },
                {
                    "name": "\u73af\u5883\u4f73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,93,69)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,109,53)"
                        }
                    }
                },
                {
                    "name": "\u522b\u518d\u9519\u8fc7Lazada",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,79,38)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4up",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,32,63)"
                        }
                    }
                },
                {
                    "name": "\u4f20\u97f3\u63a7\u80a1\u5168\u8d44\u5b50\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,155,124)"
                        }
                    }
                },
                {
                    "name": "\u5e05\u54e5\u7f8e\u5973",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,74,92)"
                        }
                    }
                },
                {
                    "name": "\u878d\u8d44\u8d8510\u4ebf\u7f8e\u5143",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,13,55)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,41,90)"
                        }
                    }
                },
                {
                    "name": "\u573a\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,72,130)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u73af\u5883\u8f7b\u677e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,62,17)"
                        }
                    }
                },
                {
                    "name": "\u5982\u679c\u4f60\u6b63\u5728\u8ffd\u68a6\u7684\u8def\u4e0a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,67,101)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,47,21)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u5de5\u4f5c\u673a\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,144,130)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6311\u6218\u548c\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,140,14)"
                        }
                    }
                },
                {
                    "name": "\u5730\u7406\u4f4d\u7f6e\u4fbf\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,121,47)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u8d5b\u9053",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,34,51)"
                        }
                    }
                },
                {
                    "name": "\u5404\u7c7b\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,18,154)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u4e00\u6d41",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,20,82)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u8bc6\u56fe\u8c31\u63a8\u8350",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,157,2)"
                        }
                    }
                },
                {
                    "name": "\u5305\u4f4f\u5bbf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,121,87)"
                        }
                    }
                },
                {
                    "name": "\u4e03\u9669\u4e8c\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,51,112)"
                        }
                    }
                },
                {
                    "name": "\u822a\u7a7aIT\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,89,141)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u4e09\u9910\u4e0b\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,160,75)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u56fe\u50cf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,146,68)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u53d1\u5c55\u7a7a\u95f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,100,127)"
                        }
                    }
                },
                {
                    "name": "open",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,23,118)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,57,28)"
                        }
                    }
                },
                {
                    "name": "\u6709\u80a1\u7968\u671f\u6743\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,101,88)"
                        }
                    }
                },
                {
                    "name": "\u8ddf\u725b\u4eba\u4e00\u8d77\u5de5\u4f5c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,59,105)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u725b\u6587\u6863\u968f\u4fbf\u770b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,7,52)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u4e1a\u4e13\u5fc3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,97,134)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u9886\u519b\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,5,25)"
                        }
                    }
                },
                {
                    "name": "\u5b5d\u987a\u57fa\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,57,134)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u901a\u7545",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,81,99)"
                        }
                    }
                },
                {
                    "name": "\u521b\u65b0\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,101,71)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u4e0b\u5348\u8336\u968f\u65f6\u51c6\u5907\u8d77\u7684",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,89,131)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u59561-3\u4e2a\u6708",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,130,130)"
                        }
                    }
                },
                {
                    "name": "\u91cd\u70b9\u53d1\u5c55\u7684\u53d8\u73b0\u9879\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,74,23)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u7814\u7ecf\u8d39",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,29,24)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u590d\u6742",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,89,96)"
                        }
                    }
                },
                {
                    "name": "\u8be5\u804c\u4f4d\u76f4\u63a5\u4e0e\u7528\u4eba\u5355\u4f4d\u7b7e\u8ba2\u52b3\u52a8\u5408\u540c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,59,40)"
                        }
                    }
                },
                {
                    "name": "\u6253\u8f66\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,87,150)"
                        }
                    }
                },
                {
                    "name": "\u9f13\u52b1\u8bd5\u9519",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,35,107)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f\u8fc5\u901f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,64,55)"
                        }
                    }
                },
                {
                    "name": "OCR/\u56fe\u50cf\u5904\u7406\u4e16\u754c\u9886\u5148\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,40,118)"
                        }
                    }
                },
                {
                    "name": "ai\u533b\u7597\u72ec\u89d2\u517d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,76,48)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u6e38\u6216\u6237\u5916\u62d3\u5c55\u57f9\u8bad",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,128,10)"
                        }
                    }
                },
                {
                    "name": "\u6e38\u620fUGC",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,88,57)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u6613\u6709\u9053",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,22,74)"
                        }
                    }
                },
                {
                    "name": "\u529f\u8bfe\u524d\u6cbf\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,47,67)"
                        }
                    }
                },
                {
                    "name": "\u5168\u52e4\u5956",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,42,2)"
                        }
                    }
                },
                {
                    "name": "\u817e\u8baf\u97f3\u4e50\u730e\u5934\u804c\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,23,53)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5bbf\u820d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,98,156)"
                        }
                    }
                },
                {
                    "name": "\u6709\u826f\u597d\u7684\u53d1\u5c55\u7a7a\u95f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,116,33)"
                        }
                    }
                },
                {
                    "name": "\u516d\u9669\u4e00\u91d1\u5e26\u85aa\u4e8b\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,75,89)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961fnice\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,116,16)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5382\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,13,111)"
                        }
                    }
                },
                {
                    "name": "\u6d3b\u529b\u65e0\u9650",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,134,157)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4Nice",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,66,0)"
                        }
                    }
                },
                {
                    "name": "bat\u5927\u725b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,46,123)"
                        }
                    }
                },
                {
                    "name": "12\u5929\u5e26\u85aa\u5e74\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,160,36)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u7f8e\u5473\u4e09\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,72,82)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u4ece0-1\u7684\u8fc7\u7a0b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,152,115)"
                        }
                    }
                },
                {
                    "name": "\u5168\u9762\u8f6c\u578bAI",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,149,145)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u6027\u5316\u7684\u4f01\u4e1a\u7ba1\u7406\u65b9\u5f0f\u548c\u8f7b\u677e\u6d3b\u6cfc\u7684\u5de5\u4f5c\u6c1b\u56f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,89,93)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,153,124)"
                        }
                    }
                },
                {
                    "name": "\u5b9e\u64cd\u5386\u7ec3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,133,47)"
                        }
                    }
                },
                {
                    "name": "\u5165\u804c\u5373\u7f34\u4e94\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,64,134)"
                        }
                    }
                },
                {
                    "name": "\u8865\u5145\u533b\u7597\u4fdd\u9669",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,21,156)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u7ebf\u6e38\u620f\u5927\u5382",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,92,11)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f\u901f\u5ea6\u5feb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,43,130)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6210\u719f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,98,27)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6269\u62db",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,124,108)"
                        }
                    }
                },
                {
                    "name": "B\u8f6e\u878d\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,66,8)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4\u68d2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,40,66)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u80cc\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,160,133)"
                        }
                    }
                },
                {
                    "name": "\u516d\u9669\u4e00\u91d1\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,97,32)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u9910\u4e0b\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,50,137)"
                        }
                    }
                },
                {
                    "name": "\u963f\u91cc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,66,90)"
                        }
                    }
                },
                {
                    "name": "2\u4e2a\u6708\u5e74\u7ec8\u5956",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,145,77)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u53d1\u5c55\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,144,147)"
                        }
                    }
                },
                {
                    "name": "\u6d3b\u529b\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,95,64)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u9ad8\u6210\u957f\u671f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,117,148)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u9760",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,90,158)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u4ea7\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,76,96)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5b9e\u529b\uff1a\u957f\u671f\u6280\u672f\u79ef\u6dc0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,81,70)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u7a33\u5b9a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,39,130)"
                        }
                    }
                },
                {
                    "name": "\u540d\u6821\u5927\u5382",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,53,42)"
                        }
                    }
                },
                {
                    "name": "\u5e02\u573a\u7ade\u4e89\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,75,37)"
                        }
                    }
                },
                {
                    "name": "\u804c\u4e1a\u53d1\u5c55\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,62,11)"
                        }
                    }
                },
                {
                    "name": "5\u59298\u5c0f\u65f6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,1,34)"
                        }
                    }
                },
                {
                    "name": "\u73af\u5883\u5bbd\u677e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,157,3)"
                        }
                    }
                },
                {
                    "name": "\u771f\u5b9e\u4e30\u5bcc\u7684\u5e94\u7528\u573a\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,120,104)"
                        }
                    }
                },
                {
                    "name": "Mac\u529e\u516c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,23,42)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u6807\u6746",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,85,71)"
                        }
                    }
                },
                {
                    "name": "\u5fd7\u540c\u9053\u5408\u7684\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,20,11)"
                        }
                    }
                },
                {
                    "name": "\u804c\u4f4d\u664b\u5347\u901a\u9053",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,81,88)"
                        }
                    }
                },
                {
                    "name": "\u798f\u7530CBD",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,106,32)"
                        }
                    }
                },
                {
                    "name": "\u540c\u884c\u4e1a\u9886\u519b\u54c1\u724c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,46,6)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u5bcc\u7684\u5458\u5de5\u6d3b\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,120,109)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u53d1\u5c55\u524d\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,126,47)"
                        }
                    }
                },
                {
                    "name": "\u5404\u79cd\u56e2\u5efa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,104,55)"
                        }
                    }
                },
                {
                    "name": "500\u5f3a\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,21,39)"
                        }
                    }
                },
                {
                    "name": "\u9f13\u52b1\u7814\u7a76\u65b0\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,119,24)"
                        }
                    }
                },
                {
                    "name": "\u6280\u80fd\u63d0\u5347",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,92,13)"
                        }
                    }
                },
                {
                    "name": "\u4e0e\u4e16\u754c\u9886\u5148\u7684AI\u7814\u53d1\u56e2\u961f\u5408\u4f5c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,11,33)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u6742\u4e8b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,39,12)"
                        }
                    }
                },
                {
                    "name": "2012\u5b9e\u9a8c\u5ba4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,70,121)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u89c4\u8303",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,125,24)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u805a\u96c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,133,142)"
                        }
                    }
                },
                {
                    "name": "\u5168\u5e7416-18\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,36,126)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51\u533b\u7597\u9886\u5934\u7f8a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,49,146)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6210\u957f\u5feb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,120,65)"
                        }
                    }
                },
                {
                    "name": "\u7ed3\u679c\u5bfc\u5411",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,62,27)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u699c****",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,113,41)"
                        }
                    }
                },
                {
                    "name": "\u90e8\u95e8\u4f18\u80dc\u5956",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,90,144)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u540d\u4e92\u8054\u7f51\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,148,95)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,126,73)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u65c5\u6e38\u5ea6\u5047\u4e94\u9669\u4e00\u91d1\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,132,14)"
                        }
                    }
                },
                {
                    "name": "\u5168\u7403\u5316\u89c6\u91ce",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,137,72)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u989d\u5e74\u7ec8\u5956",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,62,102)"
                        }
                    }
                },
                {
                    "name": "AI\u56e2\u961f\u7b79\u5efa\u4e2d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,99,153)"
                        }
                    }
                },
                {
                    "name": "\u5065\u8eab\u623f\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,98,121)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,131,46)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u5b9e\u529b\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,78,41)"
                        }
                    }
                },
                {
                    "name": "\u6c14\u6c1b\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,127,16)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u672f\u548c\u5e94\u7528\u7ed3\u5408",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,118,45)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u7fd8\u695a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,132,69)"
                        }
                    }
                },
                {
                    "name": "\u4e0b\u5348\u8336\u96f6\u98df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,127,69)"
                        }
                    }
                },
                {
                    "name": "\u5168\u7403\u9886\u5148",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,0,53)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5ea6\u7ee9\u6548",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,5,100)"
                        }
                    }
                },
                {
                    "name": "\u65bd\u5c55\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,122,16)"
                        }
                    }
                },
                {
                    "name": "\u5341\u4e94\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,100,145)"
                        }
                    }
                },
                {
                    "name": "\u7a33\u5065\u589e\u957f\u7684\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,71,142)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u5e7f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,68,10)"
                        }
                    }
                },
                {
                    "name": "\u826f\u597d\u7684\u5de5\u4f5c\u73af\u5883",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,44,60)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u5185\u4ea7\u54c1\u5f71\u54cd\u529b\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,62,44)"
                        }
                    }
                },
                {
                    "name": "\u8fd1\u4e07\u4eba\u89c4\u6a21",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,57,2)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u5916\u5408\u8d44\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,113,38)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u53d1\u5c55\u5f85\u9047\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,132,139)"
                        }
                    }
                },
                {
                    "name": "\u8d1f\u8d23\u641c\u72d7\u6570\u5b57\u4eba\u76843D\u4eba\u8138\u7b97\u6cd5\u65b9\u9762\u7684\u7814\u7a76",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,130,105)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u53d1\u5c55\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,107,159)"
                        }
                    }
                },
                {
                    "name": "\u91c7\u7f16\u5236\u64ad\u5b58",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,37,75)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u901f\u7684\u53d1\u5c55\u524d\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,13,6)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546\u5bfc\u8d2d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,93,97)"
                        }
                    }
                },
                {
                    "name": "\u7269\u6d41",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,131,61)"
                        }
                    }
                },
                {
                    "name": "\u767e\u4e07DAU",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,139,106)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6e90\u5e73\u53f0\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,72,83)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u85aa+\u80a1\u6743",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,147,31)"
                        }
                    }
                },
                {
                    "name": "\u4ebf\u7ea7\u6570\u636e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,154,71)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u53d1\u5c55\u7a7a\u95f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,33,29)"
                        }
                    }
                },
                {
                    "name": "\u804c\u4e1a\u53d1\u5c55\u826f\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,44,129)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u79c0\u5019\u9009\u4eba\u53ef\u4ee5\u6210\u4e3a\u6280\u672f\u5408\u4f19\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,29,60)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u516d\u9669\u4e00\u91d1\u996d\u8d34\u8f66\u8d34\u7ee9\u6548\u5956\u5b9a\u671f\u4f53\u68c0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,87,38)"
                        }
                    }
                },
                {
                    "name": "\u4e24\u4f4d\u9662\u58eb\u4e09\u4f4d\u535a\u58eb\u9886\u8854\u7684\u521d\u521b\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,5,97)"
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
        chart_15c175c931ae472da08560676b8d5a86.setOption(option_15c175c931ae472da08560676b8d5a86);
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
